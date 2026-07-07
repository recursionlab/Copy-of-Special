#!/usr/bin/env python3
"""
FAISS-based Semantic Deduplication
Implements advanced semantic similarity detection and deduplication
"""

import numpy as np
import json
from typing import Dict, List, Optional, Tuple, Any
from dataclasses import dataclass
from datetime import datetime
import hashlib

try:
    import faiss
    FAISS_AVAILABLE = True
except ImportError:
    FAISS_AVAILABLE = False
    print("FAISS not available. Install with: pip install faiss-cpu")

try:
    from sentence_transformers import SentenceTransformer
    TRANSFORMERS_AVAILABLE = True
except ImportError:
    TRANSFORMERS_AVAILABLE = False
    print("SentenceTransformers not available. Install with: pip install sentence-transformers")

from knowledge_evolution_v2_1 import ConceptUnit

@dataclass
class SimilarityMatch:
    """Represents a similarity match between concepts"""
    concept1_id: str
    concept2_id: str
    similarity_score: float
    similarity_type: str  # semantic, exact, near_duplicate
    match_reason: str
    should_merge: bool
    merge_confidence: float

@dataclass
class DeduplicationResult:
    """Result of deduplication process"""
    original_count: int
    duplicates_found: int
    merged_count: int
    similarity_matches: List[SimilarityMatch]
    processing_time: float
    method_used: str

class SemanticDeduplicator:
    """FAISS-based semantic deduplication engine"""

    def __init__(self, model_name: str = "all-MiniLM-L6-v2",
                 similarity_threshold: float = 0.85,
                 merge_threshold: float = 0.92):
        """Initialize semantic deduplicator"""

        self.similarity_threshold = similarity_threshold
        self.merge_threshold = merge_threshold
        self.model_name = model_name

        # Initialize embedding model
        self.embedding_model = None
        if TRANSFORMERS_AVAILABLE:
            try:
                self.embedding_model = SentenceTransformer(model_name)
                print(f"Loaded embedding model: {model_name}")
            except Exception as e:
                print(f"Failed to load embedding model: {e}")

        # Initialize FAISS index
        self.faiss_index = None
        self.concept_embeddings = {}
        self.concept_id_mapping = {}  # index -> concept_id

    def is_available(self) -> bool:
        """Check if semantic deduplication is available"""
        return FAISS_AVAILABLE and TRANSFORMERS_AVAILABLE and self.embedding_model is not None

    def create_embeddings(self, concepts: List[ConceptUnit]) -> Dict[str, np.ndarray]:
        """Create embeddings for concepts"""
        if not self.is_available():
            return {}

        embeddings = {}

        # Prepare texts for embedding
        texts = []
        concept_ids = []

        for concept in concepts:
            # Combine label and definition for more comprehensive embedding
            combined_text = f"{concept.label}: {concept.definition_full}"
            texts.append(combined_text)
            concept_ids.append(concept.id)

        try:
            # Generate embeddings in batch
            embedding_vectors = self.embedding_model.encode(texts, show_progress_bar=True)

            # Store embeddings
            for concept_id, embedding in zip(concept_ids, embedding_vectors):
                embeddings[concept_id] = embedding

            print(f"Generated embeddings for {len(embeddings)} concepts")
            return embeddings

        except Exception as e:
            print(f"Failed to generate embeddings: {e}")
            return {}

    def build_faiss_index(self, embeddings: Dict[str, np.ndarray]) -> bool:
        """Build FAISS index from embeddings"""
        if not FAISS_AVAILABLE or not embeddings:
            return False

        try:
            # Get embedding dimension
            embedding_dim = next(iter(embeddings.values())).shape[0]

            # Create FAISS index (using Inner Product for cosine similarity)
            self.faiss_index = faiss.IndexFlatIP(embedding_dim)

            # Prepare data for index
            embedding_matrix = []
            concept_ids = []

            for concept_id, embedding in embeddings.items():
                # Normalize for cosine similarity
                normalized_embedding = embedding / np.linalg.norm(embedding)
                embedding_matrix.append(normalized_embedding)
                concept_ids.append(concept_id)

            embedding_matrix = np.array(embedding_matrix).astype('float32')

            # Add to index
            self.faiss_index.add(embedding_matrix)

            # Store concept ID mapping
            self.concept_id_mapping = {i: concept_id for i, concept_id in enumerate(concept_ids)}
            self.concept_embeddings = embeddings

            print(f"Built FAISS index with {len(concept_ids)} concepts")
            return True

        except Exception as e:
            print(f"Failed to build FAISS index: {e}")
            return False

    def find_semantic_similarities(self, k: int = 10) -> List[SimilarityMatch]:
        """Find semantic similarities using FAISS"""
        if not self.faiss_index:
            return []

        similarity_matches = []

        try:
            # Search for each concept's k nearest neighbors
            for query_idx in range(self.faiss_index.ntotal):
                query_concept_id = self.concept_id_mapping[query_idx]

                # Get embedding for query
                query_embedding = None
                for concept_id, embedding in self.concept_embeddings.items():
                    if concept_id == query_concept_id:
                        query_embedding = embedding / np.linalg.norm(embedding)
                        break

                if query_embedding is None:
                    continue

                # Search for similar concepts
                scores, indices = self.faiss_index.search(
                    query_embedding.reshape(1, -1).astype('float32'), k + 1  # +1 to exclude self
                )

                # Process results (skip first result which is the concept itself)
                for i in range(1, len(indices[0])):
                    similar_idx = indices[0][i]
                    similarity_score = float(scores[0][i])

                    if similar_idx == -1:  # FAISS indicates no more results
                        break

                    similar_concept_id = self.concept_id_mapping[similar_idx]

                    # Only consider similarities above threshold
                    if similarity_score >= self.similarity_threshold:
                        # Avoid duplicate pairs (A->B and B->A)
                        pair_key = tuple(sorted([query_concept_id, similar_concept_id]))
                        existing_match = any(
                            tuple(sorted([m.concept1_id, m.concept2_id])) == pair_key
                            for m in similarity_matches
                        )

                        if not existing_match:
                            should_merge = similarity_score >= self.merge_threshold

                            similarity_matches.append(SimilarityMatch(
                                concept1_id=query_concept_id,
                                concept2_id=similar_concept_id,
                                similarity_score=similarity_score,
                                similarity_type="semantic",
                                match_reason=f"Semantic similarity: {similarity_score:.3f}",
                                should_merge=should_merge,
                                merge_confidence=similarity_score
                            ))

        except Exception as e:
            print(f"Error in semantic similarity search: {e}")

        # Sort by similarity score (descending)
        similarity_matches.sort(key=lambda x: x.similarity_score, reverse=True)

        return similarity_matches

    def find_exact_duplicates(self, concepts: List[ConceptUnit]) -> List[SimilarityMatch]:
        """Find exact and near-exact duplicates using text comparison"""
        exact_matches = []

        # Create text hashes for exact matching
        text_hashes = {}
        normalized_texts = {}

        for concept in concepts:
            # Hash for exact duplicates
            combined_text = f"{concept.label.strip()}: {concept.definition_full.strip()}"
            text_hash = hashlib.md5(combined_text.lower().encode()).hexdigest()

            if text_hash in text_hashes:
                # Exact duplicate found
                exact_matches.append(SimilarityMatch(
                    concept1_id=text_hashes[text_hash],
                    concept2_id=concept.id,
                    similarity_score=1.0,
                    similarity_type="exact",
                    match_reason="Exact text match",
                    should_merge=True,
                    merge_confidence=1.0
                ))
            else:
                text_hashes[text_hash] = concept.id

            # Normalized text for near-duplicates
            normalized_text = combined_text.lower().replace(" ", "").replace("\n", "")
            normalized_texts[concept.id] = normalized_text

        # Find near-duplicates using Levenshtein-like comparison
        concept_ids = list(normalized_texts.keys())

        for i in range(len(concept_ids)):
            for j in range(i + 1, len(concept_ids)):
                concept1_id = concept_ids[i]
                concept2_id = concept_ids[j]

                text1 = normalized_texts[concept1_id]
                text2 = normalized_texts[concept2_id]

                # Calculate similarity ratio
                if len(text1) > 0 and len(text2) > 0:
                    from difflib import SequenceMatcher
                    similarity_ratio = SequenceMatcher(None, text1, text2).ratio()

                    if similarity_ratio >= 0.95:  # Very similar text
                        exact_matches.append(SimilarityMatch(
                            concept1_id=concept1_id,
                            concept2_id=concept2_id,
                            similarity_score=similarity_ratio,
                            similarity_type="near_duplicate",
                            match_reason=f"Near-exact text match: {similarity_ratio:.3f}",
                            should_merge=similarity_ratio >= 0.98,
                            merge_confidence=similarity_ratio
                        ))

        return exact_matches

    def deduplicate_concepts(self, concepts: List[ConceptUnit]) -> DeduplicationResult:
        """Perform comprehensive deduplication"""
        start_time = datetime.now()
        original_count = len(concepts)

        # Find exact duplicates first
        exact_matches = self.find_exact_duplicates(concepts)

        # Find semantic similarities if available
        semantic_matches = []
        method_used = "text_only"

        if self.is_available():
            embeddings = self.create_embeddings(concepts)
            if embeddings and self.build_faiss_index(embeddings):
                semantic_matches = self.find_semantic_similarities()
                method_used = "faiss_semantic"

        # Combine all matches
        all_matches = exact_matches + semantic_matches

        # Remove duplicates in matches (same concept pair)
        unique_matches = []
        seen_pairs = set()

        for match in all_matches:
            pair_key = tuple(sorted([match.concept1_id, match.concept2_id]))
            if pair_key not in seen_pairs:
                unique_matches.append(match)
                seen_pairs.add(pair_key)

        # Count merge candidates
        merge_candidates = [m for m in unique_matches if m.should_merge]

        processing_time = (datetime.now() - start_time).total_seconds()

        result = DeduplicationResult(
            original_count=original_count,
            duplicates_found=len(unique_matches),
            merged_count=len(merge_candidates),
            similarity_matches=unique_matches,
            processing_time=processing_time,
            method_used=method_used
        )

        return result

    def export_deduplication_report(self, result: DeduplicationResult,
                                   concepts: Dict[str, ConceptUnit],
                                   output_path: str) -> Dict[str, Any]:
        """Export detailed deduplication report"""

        # Prepare detailed matches
        detailed_matches = []
        for match in result.similarity_matches:
            concept1 = concepts.get(match.concept1_id)
            concept2 = concepts.get(match.concept2_id)

            match_detail = {
                'concept1': {
                    'id': match.concept1_id,
                    'label': concept1.label if concept1 else 'Unknown',
                    'definition_snippet': concept1.definition_full[:100] + "..." if concept1 else ''
                },
                'concept2': {
                    'id': match.concept2_id,
                    'label': concept2.label if concept2 else 'Unknown',
                    'definition_snippet': concept2.definition_full[:100] + "..." if concept2 else ''
                },
                'similarity_score': match.similarity_score,
                'similarity_type': match.similarity_type,
                'match_reason': match.match_reason,
                'should_merge': match.should_merge,
                'merge_confidence': match.merge_confidence
            }
            detailed_matches.append(match_detail)

        # Create comprehensive report
        report = {
            'deduplication_summary': {
                'original_concept_count': result.original_count,
                'duplicates_found': result.duplicates_found,
                'merge_candidates': result.merged_count,
                'processing_time_seconds': result.processing_time,
                'method_used': result.method_used,
                'similarity_threshold': self.similarity_threshold,
                'merge_threshold': self.merge_threshold
            },
            'detailed_matches': detailed_matches,
            'statistics': {
                'exact_matches': len([m for m in result.similarity_matches if m.similarity_type == 'exact']),
                'near_duplicates': len([m for m in result.similarity_matches if m.similarity_type == 'near_duplicate']),
                'semantic_matches': len([m for m in result.similarity_matches if m.similarity_type == 'semantic']),
                'high_confidence_merges': len([m for m in result.similarity_matches if m.merge_confidence >= 0.95]),
                'medium_confidence_merges': len([m for m in result.similarity_matches if 0.85 <= m.merge_confidence < 0.95])
            },
            'technology_status': {
                'faiss_available': FAISS_AVAILABLE,
                'transformers_available': TRANSFORMERS_AVAILABLE,
                'semantic_deduplication_enabled': self.is_available(),
                'embedding_model': self.model_name if self.is_available() else None
            },
            'export_timestamp': datetime.now().isoformat()
        }

        # Write report
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, ensure_ascii=False)

        print(f"Deduplication report exported to {output_path}")
        print(f"  Duplicates found: {result.duplicates_found}")
        print(f"  Merge candidates: {result.merged_count}")
        print(f"  Processing time: {result.processing_time:.2f}s")

        return report


def demo_semantic_deduplication():
    """Demonstrate semantic deduplication capabilities"""
    print("=== Semantic Deduplication Demo ===")

    # Create demo concepts with some duplicates
    demo_concepts = [
        ConceptUnit(
            id="concept-1",
            label="Machine Learning",
            definition_full="A subset of artificial intelligence that enables computers to learn from data without explicit programming",
            source_evidence="Demo concept 1"
        ),
        ConceptUnit(
            id="concept-2",
            label="ML",
            definition_full="A subset of artificial intelligence that enables computers to learn from data without explicit programming",
            source_evidence="Demo concept 2"
        ),
        ConceptUnit(
            id="concept-3",
            label="Deep Learning",
            definition_full="A subset of machine learning using neural networks with multiple layers",
            source_evidence="Demo concept 3"
        ),
        ConceptUnit(
            id="concept-4",
            label="Neural Networks",
            definition_full="Computational models inspired by biological neural networks",
            source_evidence="Demo concept 4"
        ),
        ConceptUnit(
            id="concept-5",
            label="Machine Learning",  # Exact duplicate of concept-1
            definition_full="A subset of artificial intelligence that enables computers to learn from data without explicit programming",
            source_evidence="Demo concept 5"
        )
    ]

    # Initialize deduplicator
    deduplicator = SemanticDeduplicator()

    print(f"Deduplicator status:")
    print(f"  FAISS available: {FAISS_AVAILABLE}")
    print(f"  Transformers available: {TRANSFORMERS_AVAILABLE}")
    print(f"  Semantic deduplication enabled: {deduplicator.is_available()}")

    # Run deduplication
    print(f"\nRunning deduplication on {len(demo_concepts)} concepts...")
    result = deduplicator.deduplicate_concepts(demo_concepts)

    # Create concepts dict for report
    concepts_dict = {concept.id: concept for concept in demo_concepts}

    # Export report
    report = deduplicator.export_deduplication_report(
        result, concepts_dict, "demo_deduplication_report.json"
    )

    return result, report


if __name__ == "__main__":
    demo_semantic_deduplication()