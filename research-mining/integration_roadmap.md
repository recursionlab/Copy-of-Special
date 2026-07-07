# Knowledge Evolution Integration Roadmap
## From Schema v2.1 to Production System

Based on the comprehensive mapping table, here's the technical roadmap for integrating external tools into our knowledge evolution system.

## Phase 1: Core Infrastructure (Weeks 1-2)

### 1.1 Graph Database Backend
```python
# Replace in-memory dict storage with Neo4j
from neo4j import GraphDatabase

class GraphBackedKnowledgeEngine:
    def __init__(self, neo4j_uri="bolt://localhost:7687"):
        self.driver = GraphDatabase.driver(neo4j_uri)

    def store_concept(self, concept: ConceptUnit):
        # Store concept with full schema properties
        with self.driver.session() as session:
            session.run("""
                CREATE (c:Concept {
                    id: $id,
                    label: $label,
                    definition_full: $definition,
                    quality_tier: $tier,
                    generation: $generation
                })
            """, **concept.to_dict())
```

**Tool Integration**:
- **Neo4j Community Edition** for concept storage
- **NetworkX** for local graph analysis
- **py2neo** for Python integration

### 1.2 Enhanced PDF Processing
```python
# Replace basic file reading with structured extraction
from grobid_client.grobid_client import GrobidClient
import pdfplumber

class EnhancedPDFProcessor:
    def __init__(self):
        self.grobid = GrobidClient(config_path="./config.json")

    def extract_structured_concepts(self, pdf_path: str):
        # Use GROBID for structure + pdfplumber for text
        structure = self.grobid.process("processFulltextDocument", pdf_path)

        with pdfplumber.open(pdf_path) as pdf:
            for page_num, page in enumerate(pdf.pages):
                text = page.extract_text()
                # Enhanced concept extraction with page references
                concepts = self._extract_concepts_with_provenance(text, page_num)
```

**Tool Integration**:
- **GROBID** for PDF structure (headers, citations, references)
- **pdfplumber** for precise text extraction with coordinates
- **pymupdf** as fallback for complex PDFs

## Phase 2: Quality Enhancement (Weeks 3-4)

### 2.1 Definition Completeness with LLM
```python
import openai
from sentence_transformers import SentenceTransformer

class DefinitionEnhancer:
    def __init__(self):
        self.model = SentenceTransformer('all-MiniLM-L6-v2')

    def enhance_definition(self, concept: ConceptUnit) -> str:
        if concept.definition_completeness < 0.5:
            prompt = f"""
            Enhance this concept definition to be complete and precise:
            Term: {concept.label}
            Current: {concept.definition_full}
            Source: {concept.source_evidence}

            Requirements:
            - 2-3 complete sentences
            - Include essential characteristics
            - Maintain scientific accuracy
            """

            enhanced = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[{"role": "user", "content": prompt}]
            )
            return enhanced.choices[0].message.content
```

**Tool Integration**:
- **OpenAI GPT-4** for definition enhancement
- **Claude API** as alternative LLM
- **sentence-transformers** for similarity scoring

### 2.2 Semantic Deduplication with Embeddings
```python
import faiss
import numpy as np

class SemanticDeduplicator:
    def __init__(self, dimension=384):
        self.index = faiss.IndexFlatIP(dimension)  # Inner product similarity
        self.concept_embeddings = {}

    def find_duplicates(self, concepts: List[ConceptUnit], threshold=0.8):
        embeddings = []
        concept_ids = []

        for concept in concepts:
            embedding = self.model.encode(f"{concept.label} {concept.definition_full}")
            embeddings.append(embedding)
            concept_ids.append(concept.id)

        embeddings_array = np.array(embeddings)
        self.index.add(embeddings_array)

        # Find near-duplicates
        similarities, indices = self.index.search(embeddings_array, k=5)

        duplicates = []
        for i, (sims, idxs) in enumerate(zip(similarities, indices)):
            for j, (sim, idx) in enumerate(zip(sims[1:], idxs[1:])):  # Skip self
                if sim > threshold:
                    duplicates.append((concept_ids[i], concept_ids[idx], sim))

        return duplicates
```

**Tool Integration**:
- **FAISS** for efficient similarity search
- **sentence-transformers** for embeddings
- **Annoy** as alternative for approximate search

## Phase 3: Relation & Contradiction Detection (Weeks 5-6)

### 3.1 Automated Relation Extraction
```python
from transformers import pipeline
import spacy

class RelationExtractor:
    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")
        self.nli_model = pipeline("text-classification",
                                 model="microsoft/DialoGPT-medium")

    def extract_relations(self, concept1: ConceptUnit, concept2: ConceptUnit):
        # Use spaCy dependency parsing
        doc1 = self.nlp(concept1.definition_full)
        doc2 = self.nlp(concept2.definition_full)

        # Check for explicit mentions
        if concept1.label.lower() in concept2.definition_full.lower():
            return ConceptRelation(
                type="supports",
                target_id=concept2.id,
                evidence=f"'{concept1.label}' explicitly mentioned in definition",
                confidence=0.9
            )

        # Use NLI for implicit relations
        premise = concept1.definition_full
        hypothesis = f"This is related to {concept2.label}"

        result = self.nli_model(f"{premise} [SEP] {hypothesis}")
        if result['label'] == 'ENTAILMENT' and result['score'] > 0.7:
            return ConceptRelation(
                type="related_to",
                target_id=concept2.id,
                evidence=f"NLI entailment detected (confidence: {result['score']:.3f})",
                confidence=result['score']
            )
```

**Tool Integration**:
- **spaCy** for dependency parsing and NER
- **AllenNLP OpenIE** for open information extraction
- **RoBERTa-MNLI** for natural language inference

### 3.2 Contradiction Detection System
```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification

class ContradictionDetector:
    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-medium")
        self.model = AutoModelForSequenceClassification.from_pretrained(
            "ynie/roberta-large-snli_mnli_fever_anli_R1_R2_R3-nli"
        )

    def detect_contradictions(self, concept1: ConceptUnit, concept2: ConceptUnit):
        if concept1.label.lower() != concept2.label.lower():
            return None  # Only check same-label concepts

        # Use NLI to detect contradictions
        text1 = concept1.definition_full
        text2 = concept2.definition_full

        inputs = self.tokenizer(text1, text2, return_tensors="pt",
                               truncation=True, max_length=512)

        with torch.no_grad():
            outputs = self.model(**inputs)
            predictions = torch.softmax(outputs.logits, dim=-1)

        # Check for contradiction class
        contradiction_score = predictions[0][0].item()  # CONTRADICTION class

        if contradiction_score > 0.7:
            return ConceptContradiction(
                with_id=concept2.id,
                contradiction_basis=f"NLI model detected contradiction (score: {contradiction_score:.3f}) between definitions of '{concept1.label}'",
                resolution_confidence=1.0 - contradiction_score
            )
```

**Tool Integration**:
- **RoBERTa-large-SNLI-MNLI** for contradiction detection
- **DeBERTa** as alternative NLI model
- **SciFact** pipeline for scientific contradiction detection

## Phase 4: Advanced Clustering & Gap Analysis (Weeks 7-8)

### 4.1 Semantic Clustering with BERTopic
```python
from bertopic import BERTopic
from sklearn.feature_extraction.text import CountVectorizer

class SemanticClusterer:
    def __init__(self):
        vectorizer_model = CountVectorizer(stop_words="english")
        self.topic_model = BERTopic(
            vectorizer_model=vectorizer_model,
            verbose=True,
            calculate_probabilities=True
        )

    def cluster_concepts(self, concepts: List[ConceptUnit]):
        # Prepare documents
        documents = [f"{c.label} {c.definition_full}" for c in concepts]

        # Fit and transform
        topics, probs = self.topic_model.fit_transform(documents)

        # Create semantic clusters
        clusters = {}
        for i, (concept, topic_id, prob) in enumerate(zip(concepts, topics, probs)):
            if topic_id not in clusters:
                topic_info = self.topic_model.get_topic(topic_id)
                topic_words = [word for word, _ in topic_info[:5]]

                clusters[topic_id] = SemanticCluster(
                    cluster_id=f"topic_{topic_id}",
                    cluster_label=" + ".join(topic_words),
                    members=[],
                    rationale=f"Semantic clustering based on topic words: {', '.join(topic_words)}",
                    cluster_strength=prob
                )

            clusters[topic_id].members.append(concept.id)

        return list(clusters.values())
```

**Tool Integration**:
- **BERTopic** for semantic topic modeling
- **HDBSCAN** for density-based clustering
- **scikit-learn** for traditional clustering algorithms

### 4.2 Gap Analysis with Graph Algorithms
```python
import networkx as nx
from typing import Set

class GapAnalyzer:
    def __init__(self, graph: nx.Graph):
        self.graph = graph

    def find_missing_links(self) -> List[GapUnit]:
        gaps = []

        # Find concepts that should be connected but aren't
        for node1 in self.graph.nodes():
            for node2 in self.graph.nodes():
                if node1 != node2 and not self.graph.has_edge(node1, node2):
                    # Check if they share semantic similarity
                    similarity = self._calculate_semantic_similarity(node1, node2)

                    if similarity > 0.6:  # High similarity but no explicit edge
                        gaps.append(GapUnit(
                            gap_id=f"missing_link_{node1}_{node2}",
                            gap_type=GapType.MISSING_LINK,
                            concept_a=node1,
                            concept_b=node2,
                            gap_description=f"High semantic similarity ({similarity:.3f}) but no explicit relationship",
                            evidence_location="Graph analysis",
                            resolution_priority=Priority.MEDIUM
                        ))

        return gaps

    def find_isolated_concepts(self) -> List[GapUnit]:
        """Find concepts with no connections"""
        isolated = [node for node in self.graph.nodes()
                   if self.graph.degree(node) == 0]

        return [GapUnit(
            gap_id=f"isolated_{node}",
            gap_type=GapType.MISSING_LINK,
            concept_a=node,
            gap_description=f"Concept '{node}' has no relationships to other concepts",
            evidence_location="Graph connectivity analysis",
            resolution_priority=Priority.HIGH
        ) for node in isolated]
```

**Tool Integration**:
- **NetworkX** for graph analysis algorithms
- **Neo4j Graph Algorithms** for large-scale analysis
- **igraph** (Python) for advanced graph metrics

## Phase 5: Production Integration (Weeks 9-10)

### 5.1 Complete System Integration
```python
class ProductionKnowledgeEvolution:
    def __init__(self, config: Dict):
        # Initialize all components
        self.graph_engine = GraphBackedKnowledgeEngine(config['neo4j_uri'])
        self.pdf_processor = EnhancedPDFProcessor()
        self.definition_enhancer = DefinitionEnhancer()
        self.deduplicator = SemanticDeduplicator()
        self.relation_extractor = RelationExtractor()
        self.contradiction_detector = ContradictionDetector()
        self.clusterer = SemanticClusterer()
        self.gap_analyzer = GapAnalyzer(self.graph_engine.get_graph())

    def process_corpus(self, corpus_path: str) -> Dict:
        # Phase 1: Ingest
        raw_concepts = self.pdf_processor.process_directory(corpus_path)

        # Phase 2: Enhance Quality
        enhanced_concepts = []
        for concept in raw_concepts:
            if concept.definition_completeness < 0.5:
                concept.definition_full = self.definition_enhancer.enhance_definition(concept)
            enhanced_concepts.append(concept)

        # Phase 3: Deduplicate
        duplicates = self.deduplicator.find_duplicates(enhanced_concepts)
        unique_concepts = self._merge_duplicates(enhanced_concepts, duplicates)

        # Phase 4: Extract Relations
        for i, concept1 in enumerate(unique_concepts):
            for concept2 in unique_concepts[i+1:]:
                relation = self.relation_extractor.extract_relations(concept1, concept2)
                if relation:
                    concept1.relations.append(relation)

                contradiction = self.contradiction_detector.detect_contradictions(concept1, concept2)
                if contradiction:
                    concept1.contradictions.append(contradiction)

        # Phase 5: Cluster
        clusters = self.clusterer.cluster_concepts(unique_concepts)

        # Phase 6: Gap Analysis
        gaps = self.gap_analyzer.find_missing_links() + self.gap_analyzer.find_isolated_concepts()

        # Phase 7: Store in Graph DB
        for concept in unique_concepts:
            self.graph_engine.store_concept(concept)

        return {
            'concepts_processed': len(unique_concepts),
            'relations_found': sum(len(c.relations) for c in unique_concepts),
            'contradictions_found': sum(len(c.contradictions) for c in unique_concepts),
            'clusters_formed': len(clusters),
            'gaps_identified': len(gaps)
        }
```

## Implementation Priority Matrix

| **Component** | **Impact** | **Complexity** | **Priority** | **Dependencies** |
|---------------|------------|----------------|--------------|------------------|
| Neo4j Backend | High | Medium | 1 | None |
| GROBID PDF Processing | High | Low | 2 | Neo4j |
| LLM Definition Enhancement | High | Medium | 3 | PDF Processing |
| FAISS Deduplication | Medium | Low | 4 | Embeddings |
| spaCy Relation Extraction | Medium | Medium | 5 | Concepts stored |
| NLI Contradiction Detection | High | High | 6 | Relations |
| BERTopic Clustering | Medium | Medium | 7 | Full pipeline |
| Graph Gap Analysis | Low | Low | 8 | Neo4j + Relations |

## Installation & Dependencies

```bash
# Core infrastructure
pip install neo4j py2neo networkx

# PDF processing
pip install grobid-client pdfplumber pymupdf

# ML/NLP components
pip install transformers sentence-transformers spacy
pip install bertopic faiss-cpu scikit-learn

# Optional: GPU acceleration
pip install faiss-gpu torch

# Graph analysis
pip install igraph-python

# Download spaCy model
python -m spacy download en_core_web_sm
```

## Configuration Template

```yaml
# config.yaml
database:
  neo4j_uri: "bolt://localhost:7687"
  neo4j_user: "neo4j"
  neo4j_password: "password"

models:
  embedding_model: "all-MiniLM-L6-v2"
  nli_model: "microsoft/DialoGPT-medium"
  definition_enhancer: "gpt-4"

thresholds:
  similarity_threshold: 0.8
  contradiction_threshold: 0.7
  relation_confidence: 0.6
  quality_minimum: 0.3

processing:
  batch_size: 100
  max_concepts_per_file: 50
  refinement_queue_size: 20
```

This roadmap provides a **complete technical blueprint** for transforming the JSON Schema v2.1 into a production-ready knowledge evolution system using the mapped tools and repositories.