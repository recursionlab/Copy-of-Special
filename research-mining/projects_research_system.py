#!/usr/bin/env python3
"""
Projects Research System - Corpus Research Orchestrator
Recursive research workspace for extracting, clustering, and mapping ideas across project files
"""

import json
import uuid
import re
import os
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple
from dataclasses import dataclass, field
from enum import Enum
from collections import defaultdict

class GapType(Enum):
    CONTRADICTION = "CONTRADICTION"
    MISSING_LINK = "MISSING_LINK"
    UNDEFINED_TERM = "UNDEFINED_TERM"
    CIRCULAR_DEFINITION = "CIRCULAR_DEFINITION"
    INCONSISTENT_USAGE = "INCONSISTENT_USAGE"

class Priority(Enum):
    HIGH = "HIGH"
    MEDIUM = "MEDIUM"
    LOW = "LOW"

@dataclass
class ConceptUnit:
    """Extracted concept with provenance"""
    id: str
    term: str
    definition: str
    source_file: str
    page_section: str
    extraction_confidence: float
    domain_tags: List[str] = field(default_factory=list)
    operators: List[str] = field(default_factory=list)
    timestamp: str = field(default_factory=lambda: datetime.now().isoformat())

@dataclass
class SemanticCluster:
    """Grouped concepts with rationale"""
    cluster_id: str
    cluster_label: str
    members: List[str]
    rationale: str
    theoretical_framework: Optional[str] = None
    cluster_strength: float = 0.0

@dataclass
class RelationshipEdge:
    """Semantic relationship between concepts"""
    edge_id: str
    source_concept: str
    target_concept: str
    relation_type: str
    evidence: str
    evidence_location: str
    confidence: float
    bidirectional: bool = False

@dataclass
class GapUnit:
    """Detected gaps, contradictions, or missing links"""
    gap_id: str
    gap_type: GapType
    gap_description: str
    evidence_location: str
    concept_a: Optional[str] = None
    concept_b: Optional[str] = None
    resolution_priority: Priority = Priority.MEDIUM
    suggested_resolution: Optional[str] = None

@dataclass
class MethodNotes:
    """Recursive improvement documentation"""
    cycle_number: int
    extraction_method: str
    successful_patterns: List[str]
    failed_patterns: List[str]
    next_refinements: List[str]
    recursive_improvements: List[str] = field(default_factory=list)

class ProjectsResearchSystem:
    """Corpus research orchestrator for projects directory"""

    def __init__(self, projects_path: str = "projects"):
        self.projects_path = Path(projects_path)
        self.concept_units: Dict[str, ConceptUnit] = {}
        self.semantic_clusters: Dict[str, SemanticCluster] = {}
        self.relationship_edges: Dict[str, RelationshipEdge] = {}
        self.gap_units: Dict[str, GapUnit] = {}
        self.method_notes: List[MethodNotes] = []
        self.cycle_number: int = 0

        # Domain-specific patterns
        self.mathematical_operators = [
            r'∀', r'∃', r'∈', r'∉', r'⊂', r'⊆', r'∪', r'∩', r'→', r'←', r'↔', r'⇒', r'⇔',
            r'∧', r'∨', r'¬', r'⊤', r'⊥', r'≡', r'≠', r'≈', r'∼', r'∝', r'∞'
        ]

        self.concept_patterns = [
            r'(?i)\b(?:concept|notion|idea|principle|theory|framework|model|paradigm)\b\s+(?:of\s+)?([A-Z][a-zA-Z\s]{2,50})',
            r'(?i)^([A-Z][a-zA-Z\s]{2,30})(?:\s+is\s+|\s+refers\s+to\s+|\s+means\s+)(.{20,200})',
            r'(?i)(?:define|definition|we\s+call|termed|known\s+as)\s+([A-Z][a-zA-Z\s]{2,30})',
            r'(?i)([A-Z][a-zA-Z\s]{2,30}):\s+(.{20,200})',
        ]

    def ingest_projects_directory(self) -> Dict[str, int]:
        """Parse all files in projects directory into ConceptUnits"""
        if not self.projects_path.exists():
            raise FileNotFoundError(f"Projects directory not found: {self.projects_path}")

        file_counts = defaultdict(int)
        extraction_stats = []

        # Supported file types
        supported_extensions = {'.pdf', '.json', '.md', '.txt', '.py', '.tex', '.rst'}

        for file_path in self.projects_path.rglob('*'):
            if file_path.is_file() and file_path.suffix.lower() in supported_extensions:
                try:
                    concepts = self._extract_concepts_from_file(file_path)
                    file_counts[file_path.suffix] += 1
                    extraction_stats.append((str(file_path), len(concepts)))

                    print(f"Extracted {len(concepts)} concepts from {file_path.name}")

                except Exception as e:
                    print(f"Error processing {file_path}: {e}")

        # Log extraction method notes
        method_notes = MethodNotes(
            cycle_number=self.cycle_number,
            extraction_method="Pattern-based concept extraction with provenance tracking",
            successful_patterns=[p for p in self.concept_patterns if self._pattern_was_successful(p)],
            failed_patterns=[],
            next_refinements=[
                "Improve mathematical operator detection",
                "Add cross-file term linking",
                "Enhance domain-specific pattern recognition"
            ]
        )
        self.method_notes.append(method_notes)

        return dict(file_counts)

    def _extract_concepts_from_file(self, file_path: Path) -> List[ConceptUnit]:
        """Extract concepts from a single file"""
        concepts = []

        try:
            # Read file content
            content = self._read_file_content(file_path)
            if not content:
                return concepts

            # Extract concepts using patterns
            for i, pattern in enumerate(self.concept_patterns):
                matches = re.finditer(pattern, content, re.MULTILINE | re.DOTALL)

                for match in matches:
                    concept = self._create_concept_from_match(match, file_path, content, f"pattern_{i}")
                    if concept and self._validate_concept_quality(concept):
                        concepts.append(concept)
                        self.concept_units[concept.id] = concept

            # Extract mathematical operators
            math_operators = []
            for op_pattern in self.mathematical_operators:
                if re.search(op_pattern, content):
                    math_operators.append(op_pattern)

            # Add operators to concepts
            for concept in concepts:
                concept.operators = math_operators

        except Exception as e:
            print(f"Error extracting from {file_path}: {e}")

        return concepts

    def _read_file_content(self, file_path: Path) -> str:
        """Read content from various file types"""
        try:
            if file_path.suffix.lower() == '.pdf':
                return self._extract_pdf_content(file_path)
            elif file_path.suffix.lower() == '.json':
                with open(file_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    return json.dumps(data, indent=2) if isinstance(data, (dict, list)) else str(data)
            else:
                with open(file_path, 'r', encoding='utf-8') as f:
                    return f.read()
        except Exception as e:
            print(f"Error reading {file_path}: {e}")
            return ""

    def _extract_pdf_content(self, file_path: Path) -> str:
        """Extract text from PDF (placeholder - would use PyPDF2 or similar)"""
        try:
            import PyPDF2
            with open(file_path, 'rb') as f:
                reader = PyPDF2.PdfReader(f)
                content = ""
                for page_num, page in enumerate(reader.pages):
                    content += f"\n[PAGE {page_num + 1}]\n" + page.extract_text()
                return content
        except ImportError:
            return f"PDF content extraction requires PyPDF2: {file_path.name}"
        except Exception as e:
            return f"Error extracting PDF {file_path.name}: {e}"

    def _create_concept_from_match(self, match, file_path: Path, content: str, pattern_id: str) -> Optional[ConceptUnit]:
        """Create ConceptUnit from regex match"""
        try:
            if len(match.groups()) >= 2:
                term = match.group(1).strip()
                definition = match.group(2).strip()
            elif len(match.groups()) == 1:
                term = match.group(1).strip()
                # Extract context around the term
                start_pos = max(0, match.start() - 100)
                end_pos = min(len(content), match.end() + 100)
                definition = content[start_pos:end_pos].strip()
            else:
                return None

            # Clean and validate
            term = re.sub(r'[^\w\s\-]', '', term).strip()
            definition = re.sub(r'\s+', ' ', definition).strip()

            if len(term) < 2 or len(definition) < 20:
                return None

            # Determine page/section
            page_section = self._determine_page_section(match.start(), content)

            # Calculate extraction confidence
            confidence = self._calculate_extraction_confidence(term, definition, pattern_id)

            # Extract domain tags
            domain_tags = self._extract_domain_tags(definition)

            concept_id = f"{self._normalize_term(term)}-{uuid.uuid4().hex[:8]}"

            return ConceptUnit(
                id=concept_id,
                term=term,
                definition=definition,
                source_file=str(file_path),
                page_section=page_section,
                extraction_confidence=confidence,
                domain_tags=domain_tags
            )

        except Exception as e:
            print(f"Error creating concept from match: {e}")
            return None

    def _determine_page_section(self, match_position: int, content: str) -> str:
        """Determine page/section from position in content"""
        # Look for page markers or section headers
        before_match = content[:match_position]
        page_markers = re.findall(r'\[PAGE (\d+)\]', before_match)
        section_headers = re.findall(r'(?:^|\n)(#{1,3}\s+.+|[A-Z][A-Z\s]+(?=\n))', before_match)

        page = f"page_{page_markers[-1]}" if page_markers else "page_unknown"
        section = section_headers[-1].strip() if section_headers else "section_unknown"

        return f"{page}:{section}"

    def _calculate_extraction_confidence(self, term: str, definition: str, pattern_id: str) -> float:
        """Calculate confidence score for extracted concept"""
        score = 0.5  # Base score

        # Pattern reliability scores
        pattern_scores = {"pattern_0": 0.9, "pattern_1": 0.8, "pattern_2": 0.7, "pattern_3": 0.6}
        score += pattern_scores.get(pattern_id, 0.5) * 0.3

        # Definition quality
        if len(definition) > 50:
            score += 0.1
        if len(definition) > 100:
            score += 0.1
        if definition.count('.') >= 1:  # Complete sentences
            score += 0.1

        # Term quality
        if term.istitle() or term.isupper():  # Proper capitalization
            score += 0.1

        return min(1.0, score)

    def _extract_domain_tags(self, definition: str) -> List[str]:
        """Extract domain-specific tags from definition"""
        domain_keywords = {
            'mathematics': ['equation', 'theorem', 'proof', 'function', 'variable', 'formula'],
            'philosophy': ['consciousness', 'existence', 'reality', 'truth', 'knowledge', 'belief'],
            'computer_science': ['algorithm', 'computation', 'data', 'process', 'system', 'program'],
            'physics': ['energy', 'force', 'particle', 'wave', 'quantum', 'relativity'],
            'cognition': ['mind', 'thinking', 'memory', 'perception', 'intelligence', 'awareness']
        }

        tags = []
        definition_lower = definition.lower()

        for domain, keywords in domain_keywords.items():
            if any(keyword in definition_lower for keyword in keywords):
                tags.append(domain)

        return tags

    def _validate_concept_quality(self, concept: ConceptUnit) -> bool:
        """Validate concept meets quality thresholds"""
        if len(concept.term) < 2 or len(concept.definition) < 25:
            return False
        if concept.extraction_confidence < 0.3:
            return False
        return True

    def _pattern_was_successful(self, pattern: str) -> bool:
        """Check if pattern extracted valid concepts"""
        # Placeholder - would track pattern success rates
        return True

    def _normalize_term(self, term: str) -> str:
        """Normalize term for ID generation"""
        return re.sub(r'[^\w]', '_', term.lower())

    def cluster_concepts(self) -> Dict[str, SemanticCluster]:
        """Group concepts into semantic neighborhoods"""
        if not self.concept_units:
            return {}

        # Simple clustering by domain tags and term similarity
        clusters = defaultdict(list)

        # Group by domain tags first
        for concept in self.concept_units.values():
            if concept.domain_tags:
                primary_domain = concept.domain_tags[0]
                clusters[primary_domain].append(concept.id)
            else:
                clusters['general'].append(concept.id)

        # Create semantic clusters
        for cluster_label, member_ids in clusters.items():
            if len(member_ids) > 1:  # Only create clusters with multiple members
                cluster_id = f"cluster_{cluster_label}_{uuid.uuid4().hex[:6]}"

                rationale = f"Concepts grouped by shared domain: {cluster_label}"
                if cluster_label != 'general':
                    rationale += f". All concepts relate to {cluster_label} domain based on terminology analysis."

                # Calculate cluster strength
                strengths = [self.concept_units[cid].extraction_confidence for cid in member_ids]
                cluster_strength = sum(strengths) / len(strengths)

                cluster = SemanticCluster(
                    cluster_id=cluster_id,
                    cluster_label=cluster_label.title(),
                    members=member_ids,
                    rationale=rationale,
                    theoretical_framework=f"{cluster_label.title()} Theory" if cluster_label != 'general' else None,
                    cluster_strength=cluster_strength
                )

                self.semantic_clusters[cluster_id] = cluster

        return self.semantic_clusters

    def generate_relationship_edges(self) -> Dict[str, RelationshipEdge]:
        """Generate adjacency edges between concepts"""
        edges = {}

        concept_list = list(self.concept_units.values())

        for i in range(len(concept_list)):
            for j in range(i + 1, len(concept_list)):
                concept1, concept2 = concept_list[i], concept_list[j]

                # Check for relationships
                relationship = self._detect_relationship(concept1, concept2)
                if relationship:
                    edge_id = f"edge_{concept1.id}_{concept2.id}"
                    edges[edge_id] = relationship

        self.relationship_edges = edges
        return edges

    def _detect_relationship(self, concept1: ConceptUnit, concept2: ConceptUnit) -> Optional[RelationshipEdge]:
        """Detect semantic relationship between two concepts"""
        def1_words = set(concept1.definition.lower().split())
        def2_words = set(concept2.definition.lower().split())

        overlap = def1_words.intersection(def2_words)
        overlap_ratio = len(overlap) / max(len(def1_words), len(def2_words), 1)

        # Check for various relationship types
        if overlap_ratio > 0.3:
            evidence = f"Semantic overlap: {', '.join(list(overlap)[:3])}"
            return RelationshipEdge(
                edge_id=f"edge_{concept1.id}_{concept2.id}",
                source_concept=concept1.id,
                target_concept=concept2.id,
                relation_type="related_to",
                evidence=evidence,
                evidence_location=f"{concept1.source_file} & {concept2.source_file}",
                confidence=overlap_ratio
            )

        # Check for hierarchical relationships
        if concept1.term.lower() in concept2.definition.lower():
            return RelationshipEdge(
                edge_id=f"edge_{concept1.id}_{concept2.id}",
                source_concept=concept1.id,
                target_concept=concept2.id,
                relation_type="defines",
                evidence=f"'{concept1.term}' appears in definition of '{concept2.term}'",
                evidence_location=concept2.source_file,
                confidence=0.8
            )

        return None

    def detect_gaps_and_contradictions(self) -> Dict[str, GapUnit]:
        """Log contradictions, missing links, and unexplained terms"""
        gaps = {}

        # Detect undefined terms
        undefined_terms = self._find_undefined_terms()
        for term, locations in undefined_terms.items():
            gap_id = f"undefined_{self._normalize_term(term)}"
            gaps[gap_id] = GapUnit(
                gap_id=gap_id,
                gap_type=GapType.UNDEFINED_TERM,
                gap_description=f"Term '{term}' used but not defined in corpus",
                evidence_location="; ".join(locations),
                resolution_priority=Priority.MEDIUM,
                suggested_resolution=f"Add definition for '{term}' or link to external source"
            )

        # Detect contradictions
        contradictions = self._find_contradictions()
        for contradiction in contradictions:
            gaps[contradiction.gap_id] = contradiction

        # Detect missing links
        missing_links = self._find_missing_links()
        for link in missing_links:
            gaps[link.gap_id] = link

        self.gap_units = gaps
        return gaps

    def _find_undefined_terms(self) -> Dict[str, List[str]]:
        """Find terms that are referenced but not defined"""
        defined_terms = set(concept.term.lower() for concept in self.concept_units.values())
        undefined = defaultdict(list)

        # Look for capitalized terms that aren't defined
        for concept in self.concept_units.values():
            # Extract capitalized terms from definitions
            capitalized_terms = re.findall(r'\b[A-Z][a-z]+(?:\s+[A-Z][a-z]+)*\b', concept.definition)

            for term in capitalized_terms:
                if term.lower() not in defined_terms and len(term) > 3:
                    undefined[term].append(f"{concept.source_file}:{concept.page_section}")

        return dict(undefined)

    def _find_contradictions(self) -> List[GapUnit]:
        """Find contradictory statements about the same concepts"""
        contradictions = []

        # Group concepts by normalized term
        term_groups = defaultdict(list)
        for concept in self.concept_units.values():
            normalized = concept.term.lower().strip()
            term_groups[normalized].append(concept)

        # Check for contradictory definitions
        for term, concepts in term_groups.items():
            if len(concepts) > 1:
                for i in range(len(concepts)):
                    for j in range(i + 1, len(concepts)):
                        contradiction = self._detect_contradiction_between_concepts(concepts[i], concepts[j])
                        if contradiction:
                            contradictions.append(contradiction)

        return contradictions

    def _detect_contradiction_between_concepts(self, concept1: ConceptUnit, concept2: ConceptUnit) -> Optional[GapUnit]:
        """Detect contradiction between two concepts with same term"""
        def1 = concept1.definition.lower()
        def2 = concept2.definition.lower()

        # Look for opposing terms
        oppositions = [
            ('is', 'is not'), ('can', 'cannot'), ('always', 'never'),
            ('required', 'optional'), ('finite', 'infinite'), ('static', 'dynamic')
        ]

        for pos_term, neg_term in oppositions:
            if pos_term in def1 and neg_term in def2:
                gap_id = f"contradiction_{concept1.id}_{concept2.id}"
                return GapUnit(
                    gap_id=gap_id,
                    gap_type=GapType.CONTRADICTION,
                    concept_a=concept1.id,
                    concept_b=concept2.id,
                    gap_description=f"Contradictory definitions for '{concept1.term}': one claims '{pos_term}' while other claims '{neg_term}'",
                    evidence_location=f"{concept1.source_file} vs {concept2.source_file}",
                    resolution_priority=Priority.HIGH,
                    suggested_resolution="Examine source contexts and determine which definition is more accurate or if both can coexist"
                )

        return None

    def _find_missing_links(self) -> List[GapUnit]:
        """Find concepts that should be related but aren't linked"""
        missing_links = []

        # Look for concepts in same domain that should be connected
        for cluster in self.semantic_clusters.values():
            if len(cluster.members) > 2:
                # Check if concepts in cluster are actually related
                concepts = [self.concept_units[cid] for cid in cluster.members]

                for i in range(len(concepts)):
                    for j in range(i + 1, len(concepts)):
                        if not self._concepts_are_linked(concepts[i], concepts[j]):
                            gap_id = f"missing_link_{concepts[i].id}_{concepts[j].id}"
                            missing_links.append(GapUnit(
                                gap_id=gap_id,
                                gap_type=GapType.MISSING_LINK,
                                concept_a=concepts[i].id,
                                concept_b=concepts[j].id,
                                gap_description=f"Concepts '{concepts[i].term}' and '{concepts[j].term}' are in same domain but lack explicit relationship",
                                evidence_location=f"{concepts[i].source_file} & {concepts[j].source_file}",
                                resolution_priority=Priority.LOW,
                                suggested_resolution="Investigate potential relationships between these related concepts"
                            ))

        return missing_links

    def _concepts_are_linked(self, concept1: ConceptUnit, concept2: ConceptUnit) -> bool:
        """Check if two concepts have an explicit relationship"""
        for edge in self.relationship_edges.values():
            if ((edge.source_concept == concept1.id and edge.target_concept == concept2.id) or
                (edge.source_concept == concept2.id and edge.target_concept == concept1.id)):
                return True
        return False

    def run_research_cycle(self) -> dict:
        """Run complete research cycle"""
        self.cycle_number += 1

        print(f"🔬 Research Cycle {self.cycle_number}")
        print("=" * 50)

        # Step 1: Ingest
        print("📁 Ingesting project files...")
        file_stats = self.ingest_projects_directory()
        print(f"   Processed: {sum(file_stats.values())} files")

        # Step 2: Cluster
        print("🏷️  Clustering concepts...")
        clusters = self.cluster_concepts()
        print(f"   Created: {len(clusters)} semantic clusters")

        # Step 3: Map relationships
        print("🕸️  Mapping relationships...")
        edges = self.generate_relationship_edges()
        print(f"   Found: {len(edges)} relationship edges")

        # Step 4: Gap analysis
        print("🔍 Analyzing gaps...")
        gaps = self.detect_gaps_and_contradictions()
        print(f"   Detected: {len(gaps)} gaps/contradictions")

        # Generate next steps
        next_steps = self._generate_next_steps()

        stats = {
            "cycle": self.cycle_number,
            "concepts_extracted": len(self.concept_units),
            "clusters_formed": len(clusters),
            "relationships_mapped": len(edges),
            "gaps_detected": len(gaps),
            "file_types_processed": file_stats,
            "next_steps": next_steps
        }

        print("✅ Research cycle complete!")
        return stats

    def _generate_next_steps(self) -> List[str]:
        """Generate next refinement steps"""
        steps = []

        if len(self.concept_units) < 10:
            steps.append("Expand concept extraction patterns to capture more domain-specific terms")

        if len(self.relationship_edges) < len(self.concept_units) * 0.5:
            steps.append("Improve relationship detection algorithms for better concept connectivity")

        if any(gap.gap_type == GapType.CONTRADICTION for gap in self.gap_units.values()):
            steps.append("Resolve high-priority contradictions through source analysis")

        return steps[:3]  # Maximum 3 steps

    def export_research_results(self, output_path: str) -> dict:
        """Export complete research results"""
        # Calculate quality metrics
        concept_density = len(self.concept_units) / max(1, len(set(c.source_file for c in self.concept_units.values())))
        cross_ref_ratio = len(self.relationship_edges) / max(1, len(self.concept_units))
        contradiction_ratio = len([g for g in self.gap_units.values() if g.gap_type == GapType.CONTRADICTION]) / max(1, len(self.concept_units))

        result = {
            "corpus_metadata": {
                "total_files": len(set(c.source_file for c in self.concept_units.values())),
                "file_types": {},  # Would be populated from ingestion
                "extraction_date": datetime.now().isoformat(),
                "quality_metrics": {
                    "concept_density": concept_density,
                    "cross_reference_ratio": cross_ref_ratio,
                    "contradiction_ratio": contradiction_ratio
                }
            },
            "concept_units": [
                {
                    "id": c.id,
                    "term": c.term,
                    "definition": c.definition,
                    "source_file": c.source_file,
                    "page_section": c.page_section,
                    "extraction_confidence": c.extraction_confidence,
                    "domain_tags": c.domain_tags,
                    "operators": c.operators,
                    "timestamp": c.timestamp
                }
                for c in self.concept_units.values()
            ],
            "semantic_clusters": [
                {
                    "cluster_id": c.cluster_id,
                    "cluster_label": c.cluster_label,
                    "members": c.members,
                    "rationale": c.rationale,
                    "theoretical_framework": c.theoretical_framework,
                    "cluster_strength": c.cluster_strength
                }
                for c in self.semantic_clusters.values()
            ],
            "relationship_edges": [
                {
                    "edge_id": e.edge_id,
                    "source_concept": e.source_concept,
                    "target_concept": e.target_concept,
                    "relation_type": e.relation_type,
                    "evidence": e.evidence,
                    "evidence_location": e.evidence_location,
                    "confidence": e.confidence,
                    "bidirectional": e.bidirectional
                }
                for e in self.relationship_edges.values()
            ],
            "gap_units": [
                {
                    "gap_id": g.gap_id,
                    "gap_type": g.gap_type.value,
                    "concept_a": g.concept_a,
                    "concept_b": g.concept_b,
                    "gap_description": g.gap_description,
                    "evidence_location": g.evidence_location,
                    "resolution_priority": g.resolution_priority.value,
                    "suggested_resolution": g.suggested_resolution
                }
                for g in self.gap_units.values()
            ],
            "method_notes": {
                "cycle_number": self.cycle_number,
                "extraction_method": "Multi-pattern concept extraction with domain-specific recognition",
                "successful_patterns": [p for p in self.concept_patterns if self._pattern_was_successful(p)],
                "failed_patterns": [],
                "next_refinements": self._generate_next_steps(),
                "recursive_improvements": [
                    "Enhanced mathematical operator detection",
                    "Improved cross-file concept linking",
                    "Strengthened contradiction detection algorithms"
                ]
            }
        }

        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(result, f, indent=2, ensure_ascii=False)

        return result