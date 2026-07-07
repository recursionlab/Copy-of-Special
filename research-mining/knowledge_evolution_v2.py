#!/usr/bin/env python3
"""
Knowledge Evolution Engine v2 - Quality-First Semantic Evolution
Implements strict quality controls, deduplication, and contradiction detection
"""

import json
import uuid
import random
import math
from datetime import datetime
from typing import Dict, List, Optional, Set, Tuple
from dataclasses import dataclass, field
from enum import Enum
from difflib import SequenceMatcher

class ConceptState(Enum):
    ACTIVE = "ACTIVE"
    REDUNDANT = "REDUNDANT"
    CONTRADICTORY = "CONTRADICTORY"
    MERGED = "MERGED"

class EvolutionOperation(Enum):
    ASEXUAL_REFINEMENT = "ASEXUAL_REFINEMENT"
    CROSS_SYNTHESIS = "CROSS_SYNTHESIS"
    DEDUPLICATION_MERGE = "DEDUPLICATION_MERGE"
    CONTRADICTION_RESOLUTION = "CONTRADICTION_RESOLUTION"

@dataclass
class ConceptRelation:
    type: str  # supports, contradicts, refines, extends, specializes
    target_id: str
    evidence: str

@dataclass
class ConceptContradiction:
    with_id: str
    contradiction_basis: str
    resolution: Optional[str] = None

@dataclass
class ConceptUnit:
    """Quality-first concept with complete definitions"""
    id: str
    label: str
    definition_full: str
    source_evidence: str
    lineage: List[str] = field(default_factory=list)
    generation: int = 0
    state: ConceptState = ConceptState.ACTIVE
    relations: List[ConceptRelation] = field(default_factory=list)
    contradictions: List[ConceptContradiction] = field(default_factory=list)
    support_strength: float = 1.0
    definition_completeness: float = 0.0
    merge_count: int = 0
    timestamp: str = field(default_factory=lambda: datetime.now().isoformat())

    def __post_init__(self):
        self.definition_completeness = self._calculate_definition_quality()

    def _calculate_definition_quality(self) -> float:
        """Calculate quality score for definition"""
        if not self.definition_full:
            return 0.0

        # Length factor (50+ chars = good, 100+ chars = excellent)
        length_score = min(1.0, len(self.definition_full) / 100.0)

        # Completeness factor (sentence endings, no fragments)
        has_sentence_ending = self.definition_full.strip().endswith(('.', '!', '?'))
        no_fragments = '...' not in self.definition_full and not self.definition_full.endswith('se')
        completeness_score = 1.0 if (has_sentence_ending and no_fragments) else 0.5

        # Evidence backing
        evidence_score = 1.0 if self.source_evidence and len(self.source_evidence) > 10 else 0.7

        return (length_score + completeness_score + evidence_score) / 3.0

@dataclass
class EvolutionEvent:
    """Enhanced evolution tracking with quality deltas"""
    operation: EvolutionOperation
    parent_ids: List[str]
    offspring_id: str
    transformation: str
    delta: str  # Required: explicit change description
    quality_improvement: float = 0.0
    success: bool = True
    notes: str = ""
    timestamp: str = field(default_factory=lambda: datetime.now().isoformat())

class KnowledgeEvolutionV2:
    """Quality-first autopoietic knowledge evolution"""

    def __init__(self):
        self.concepts: Dict[str, ConceptUnit] = {}
        self.evolution_log: List[EvolutionEvent] = []
        self.merged_concepts: int = 0

        # Quality-first parameters
        self.MIN_DEFINITION_LENGTH = 50
        self.SIMILARITY_THRESHOLD = 0.80  # For deduplication
        self.REFINEMENT_THRESHOLD = 0.6   # Higher quality bar
        self.SYNTHESIS_THRESHOLD = 0.65   # Even higher for synthesis
        self.MAX_GENERATION = 3           # Tighter generation limit
        self.MIN_QUALITY_IMPROVEMENT = 0.1  # Minimum improvement required

    def add_concept_from_unit(self, concept_data: dict) -> Optional[ConceptUnit]:
        """Create quality concept with validation and deduplication"""
        # Extract and validate definition
        definition = concept_data.get('definition', concept_data.get('notes', ''))
        if len(definition) < self.MIN_DEFINITION_LENGTH:
            return None  # Reject short definitions

        # Create concept with quality validation
        concept_id = concept_data.get('id', f'concept-{uuid.uuid4().hex[:8]}')
        label = concept_data.get('term', concept_data.get('type', 'Unknown'))

        # Create source evidence from available fields
        source_evidence = self._extract_source_evidence(concept_data)

        # Check for existing similar concepts (deduplication)
        similar_concept = self._find_similar_concept(definition, label)
        if similar_concept:
            return self._merge_concepts(similar_concept, concept_data)

        concept = ConceptUnit(
            id=concept_id,
            label=label,
            definition_full=definition,
            source_evidence=source_evidence,
            support_strength=concept_data.get('confidence_score', 0.5),
            timestamp=concept_data.get('extraction_date', datetime.now().isoformat())
        )

        # Quality gate: only add high-quality concepts
        if concept.definition_completeness < 0.5:
            return None

        self.concepts[concept_id] = concept
        return concept

    def _extract_source_evidence(self, concept_data: dict) -> str:
        """Extract source evidence from concept data"""
        evidence_fields = ['notes', 'source', 'extraction_date', 'mathematical_formulation']
        evidence_parts = []

        for field in evidence_fields:
            if field in concept_data and concept_data[field]:
                evidence_parts.append(f"{field}: {str(concept_data[field])[:100]}")

        return " | ".join(evidence_parts) if evidence_parts else "No source evidence available"

    def _find_similar_concept(self, definition: str, label: str) -> Optional[ConceptUnit]:
        """Find existing concept with high similarity for deduplication"""
        for concept in self.concepts.values():
            # Check definition similarity
            def_similarity = SequenceMatcher(None, definition.lower(), concept.definition_full.lower()).ratio()
            label_match = label.lower() == concept.label.lower()

            if def_similarity >= self.SIMILARITY_THRESHOLD or (label_match and def_similarity > 0.6):
                return concept
        return None

    def _merge_concepts(self, existing_concept: ConceptUnit, new_data: dict) -> ConceptUnit:
        """Merge new concept data into existing concept"""
        # Update lineage and evidence
        new_source = self._extract_source_evidence(new_data)
        if new_source not in existing_concept.source_evidence:
            existing_concept.source_evidence += f" | MERGED: {new_source}"

        existing_concept.merge_count += 1
        existing_concept.state = ConceptState.MERGED
        self.merged_concepts += 1

        # Log merge event
        event = EvolutionEvent(
            operation=EvolutionOperation.DEDUPLICATION_MERGE,
            parent_ids=[existing_concept.id],
            offspring_id=existing_concept.id,
            transformation="Concept deduplication merge",
            delta=f"Merged similar concept, added source evidence. Merge count: {existing_concept.merge_count}",
            quality_improvement=0.05,
            notes=f"Prevented duplication, strengthened evidence base"
        )
        self.evolution_log.append(event)

        return existing_concept

    def detect_semantic_relations(self, concept1: ConceptUnit, concept2: ConceptUnit) -> List[ConceptRelation]:
        """Enhanced relation detection with evidence requirements"""
        relations = []

        def1_words = set(word.strip('.,!?') for word in concept1.definition_full.lower().split() if len(word) > 3)
        def2_words = set(word.strip('.,!?') for word in concept2.definition_full.lower().split() if len(word) > 3)

        overlap = def1_words.intersection(def2_words)
        overlap_ratio = len(overlap) / max(len(def1_words), len(def2_words), 1)

        # Only create relations with strong evidence
        if overlap_ratio > 0.4 or len(overlap) > 4:
            evidence = f"Strong semantic overlap ({overlap_ratio:.2f}): {', '.join(list(overlap)[:3])}"
            relations.append(ConceptRelation(
                type="supports",
                target_id=concept2.id,
                evidence=evidence
            ))

        return relations

    def detect_contradictions(self):
        """Detect contradictions between concepts with same labels"""
        label_groups = {}
        for concept in self.concepts.values():
            label = concept.label.lower()
            if label not in label_groups:
                label_groups[label] = []
            label_groups[label].append(concept)

        for label, concepts in label_groups.items():
            if len(concepts) > 1:
                # Check for contradictory definitions
                for i in range(len(concepts)):
                    for j in range(i + 1, len(concepts)):
                        contradiction = self._detect_contradiction_pair(concepts[i], concepts[j])
                        if contradiction:
                            concepts[i].contradictions.append(contradiction)
                            concepts[i].state = ConceptState.CONTRADICTORY

    def _detect_contradiction_pair(self, concept1: ConceptUnit, concept2: ConceptUnit) -> Optional[ConceptContradiction]:
        """Detect contradiction between two concepts"""
        def1 = concept1.definition_full.lower()
        def2 = concept2.definition_full.lower()

        # Look for opposing terms
        opposition_pairs = [
            ('open', 'closed'), ('finite', 'infinite'), ('stable', 'unstable'),
            ('recursive', 'non-recursive'), ('deterministic', 'random'),
            ('linear', 'non-linear'), ('requires', 'does not require')
        ]

        for term1, term2 in opposition_pairs:
            if term1 in def1 and term2 in def2:
                return ConceptContradiction(
                    with_id=concept2.id,
                    contradiction_basis=f"Opposing claims: '{term1}' vs '{term2}' in definitions of same concept '{concept1.label}'"
                )

        return None

    def asexual_refinement(self, parent_id: str) -> Optional[ConceptUnit]:
        """Quality-controlled concept refinement"""
        if parent_id not in self.concepts:
            return None

        parent = self.concepts[parent_id]

        # Quality gates
        if parent.support_strength < self.REFINEMENT_THRESHOLD:
            return None
        if parent.generation >= self.MAX_GENERATION:
            return None
        if parent.definition_completeness < 0.6:
            return None

        # Create meaningful refinement
        refinement_type, refined_definition, delta = self._generate_meaningful_refinement(parent)

        offspring_id = f'refined-{parent_id}-{uuid.uuid4().hex[:6]}'
        offspring = ConceptUnit(
            id=offspring_id,
            label=f"{parent.label} ({refinement_type})",
            definition_full=refined_definition,
            source_evidence=parent.source_evidence,
            lineage=[parent_id],
            generation=parent.generation + 1,
            support_strength=parent.support_strength * 0.95,  # Slight reduction for speculation
            relations=parent.relations.copy(),
            contradictions=parent.contradictions.copy()
        )

        # Quality improvement check
        quality_improvement = offspring.definition_completeness - parent.definition_completeness
        if quality_improvement < self.MIN_QUALITY_IMPROVEMENT:
            return None  # Reject low-quality refinements

        self.concepts[offspring_id] = offspring
        parent.support_strength *= 0.9  # Reduce parent strength to prevent over-refinement

        # Log detailed evolution event
        event = EvolutionEvent(
            operation=EvolutionOperation.ASEXUAL_REFINEMENT,
            parent_ids=[parent_id],
            offspring_id=offspring_id,
            transformation=f"Concept refinement: {refinement_type}",
            delta=delta,
            quality_improvement=quality_improvement,
            notes=f"Refined '{parent.label}' with {refinement_type}, generation {offspring.generation}"
        )
        self.evolution_log.append(event)

        return offspring

    def _generate_meaningful_refinement(self, parent: ConceptUnit) -> Tuple[str, str, str]:
        """Generate meaningful refinement with explicit delta"""
        refinement_strategies = [
            ("Precision", lambda d: f"{d} This refined understanding emphasizes precise boundaries and eliminates ambiguous interpretations.", "Added precision boundaries and eliminated ambiguity"),
            ("Context", lambda d: f"{d} Within the broader theoretical framework, this concept operates under specific contextual constraints.", "Added theoretical context and operational constraints"),
            ("Mechanisms", lambda d: f"{d} The underlying mechanisms involve feedback loops and emergent properties that stabilize the concept's manifestation.", "Added mechanistic explanation with feedback loops")
        ]

        strategy_name, refinement_func, delta = random.choice(refinement_strategies)
        refined_definition = refinement_func(parent.definition_full)

        return strategy_name, refined_definition, delta

    def cross_synthesis(self, parent1_id: str, parent2_id: str) -> Optional[ConceptUnit]:
        """Quality-controlled concept synthesis"""
        if parent1_id not in self.concepts or parent2_id not in self.concepts:
            return None

        parent1 = self.concepts[parent1_id]
        parent2 = self.concepts[parent2_id]

        # Enhanced quality gates
        combined_strength = (parent1.support_strength + parent2.support_strength) / 2
        combined_quality = (parent1.definition_completeness + parent2.definition_completeness) / 2

        if combined_strength < self.SYNTHESIS_THRESHOLD or combined_quality < 0.6:
            return None

        max_generation = max(parent1.generation, parent2.generation)
        if max_generation >= self.MAX_GENERATION:
            return None

        # Create meaningful synthesis
        hybrid_definition, delta = self._generate_meaningful_synthesis(parent1, parent2)

        offspring_id = f'synthesis-{parent1_id[:8]}-{parent2_id[:8]}-{uuid.uuid4().hex[:4]}'
        offspring = ConceptUnit(
            id=offspring_id,
            label=f"{parent1.label} ⊗ {parent2.label}",
            definition_full=hybrid_definition,
            source_evidence=f"SYNTHESIS: {parent1.source_evidence} | {parent2.source_evidence}",
            lineage=[parent1_id, parent2_id],
            generation=max_generation + 1,
            support_strength=combined_strength * 1.05,  # Synthesis bonus
            relations=self._merge_relations(parent1.relations, parent2.relations),
            contradictions=self._merge_contradictions(parent1.contradictions, parent2.contradictions)
        )

        quality_improvement = offspring.definition_completeness - combined_quality
        if quality_improvement < self.MIN_QUALITY_IMPROVEMENT:
            return None

        self.concepts[offspring_id] = offspring

        # Log detailed synthesis
        event = EvolutionEvent(
            operation=EvolutionOperation.CROSS_SYNTHESIS,
            parent_ids=[parent1_id, parent2_id],
            offspring_id=offspring_id,
            transformation="Cross-synthesis of complementary concepts",
            delta=delta,
            quality_improvement=quality_improvement,
            notes=f"Synthesized '{parent1.label}' and '{parent2.label}' into coherent hybrid concept"
        )
        self.evolution_log.append(event)

        return offspring

    def _generate_meaningful_synthesis(self, parent1: ConceptUnit, parent2: ConceptUnit) -> Tuple[str, str]:
        """Generate meaningful synthesis with bridging logic"""
        synthesis_templates = [
            ("Integration", f"The synthesis of {parent1.label} and {parent2.label} reveals that {parent1.definition_full[:60]}... while simultaneously {parent2.definition_full[:60]}... This integration resolves the apparent tension by showing how both aspects operate at different scales of analysis."),
            ("Emergence", f"When {parent1.label} and {parent2.label} interact, an emergent property arises: {parent1.definition_full[:50]}... creates the conditions for {parent2.definition_full[:50]}... to manifest in novel ways that transcend both original concepts."),
            ("Dialectical", f"The dialectical relationship between {parent1.label} and {parent2.label} demonstrates that {parent1.definition_full[:50]}... and {parent2.definition_full[:50]}... are not contradictory but complementary aspects of a higher-order unified process.")
        ]

        synthesis_type, hybrid_definition = random.choice(synthesis_templates)
        delta = f"Created {synthesis_type.lower()} synthesis bridging concepts through higher-order unification"

        return hybrid_definition, delta

    def _merge_relations(self, rel1: List[ConceptRelation], rel2: List[ConceptRelation]) -> List[ConceptRelation]:
        """Merge relation lists avoiding duplicates"""
        seen = set()
        merged = []
        for rel_list in [rel1, rel2]:
            for rel in rel_list:
                key = (rel.type, rel.target_id)
                if key not in seen:
                    seen.add(key)
                    merged.append(rel)
        return merged

    def _merge_contradictions(self, cont1: List[ConceptContradiction], cont2: List[ConceptContradiction]) -> List[ConceptContradiction]:
        """Merge contradiction lists"""
        seen = set()
        merged = []
        for cont_list in [cont1, cont2]:
            for cont in cont_list:
                if cont.with_id not in seen:
                    seen.add(cont.with_id)
                    merged.append(cont)
        return merged

    def evolve_knowledge_ecosystem(self, cycles: int = 8):
        """Quality-controlled ecosystem evolution"""
        for cycle in range(cycles):
            # Get quality concepts only
            quality_concepts = [
                cid for cid, c in self.concepts.items()
                if c.state == ConceptState.ACTIVE and c.definition_completeness > 0.5
            ]

            if len(quality_concepts) < 2:
                break

            # Fewer, higher-quality evolution attempts
            attempts = min(len(quality_concepts) // 5, 3)

            for _ in range(attempts):
                if random.random() < 0.6:  # 60% refinement
                    parent = random.choice(quality_concepts)
                    self.asexual_refinement(parent)
                else:  # 40% synthesis
                    if len(quality_concepts) >= 2:
                        parent1, parent2 = random.sample(quality_concepts, 2)
                        self.cross_synthesis(parent1, parent2)

            # Quality control: detect contradictions
            if cycle % 2 == 0:  # Every other cycle
                self.detect_contradictions()

            # Prune low-quality concepts
            self._prune_low_quality_concepts()

    def _prune_low_quality_concepts(self):
        """Remove concepts that fall below quality thresholds"""
        to_remove = []
        for concept_id, concept in self.concepts.items():
            if (concept.definition_completeness < 0.3 or
                concept.support_strength < 0.2 or
                (concept.generation > 0 and len(concept.definition_full) < 60)):
                to_remove.append(concept_id)
                concept.state = ConceptState.REDUNDANT

        for concept_id in to_remove:
            if concept_id in self.concepts:
                del self.concepts[concept_id]

    def get_ecosystem_stats(self) -> dict:
        """Enhanced ecosystem statistics with quality metrics"""
        active_concepts = [c for c in self.concepts.values() if c.state == ConceptState.ACTIVE]
        total_relations = sum(len(c.relations) for c in active_concepts)
        total_contradictions = sum(len(c.contradictions) for c in active_concepts)

        # Quality score
        quality_scores = [c.definition_completeness for c in active_concepts]
        avg_quality = sum(quality_scores) / len(quality_scores) if quality_scores else 0

        # Diversity calculation
        diversity = 0.0
        if active_concepts:
            label_counts = {}
            for concept in active_concepts:
                label_type = concept.label.split()[0].lower()
                label_counts[label_type] = label_counts.get(label_type, 0) + 1

            total = len(active_concepts)
            for count in label_counts.values():
                if count > 0:
                    proportion = count / total
                    diversity -= proportion * math.log2(proportion)

        return {
            "total_concepts": len(self.concepts),
            "active_concepts": len(active_concepts),
            "merged_concepts": self.merged_concepts,
            "conceptual_diversity": diversity,
            "relation_count": total_relations,
            "contradiction_count": total_contradictions,
            "quality_score": avg_quality
        }

    def export_knowledge_evolution_v2(self, output_path: str):
        """Export v2 schema with quality metrics"""
        stats = self.get_ecosystem_stats()

        concepts_data = []
        for concept in self.concepts.values():
            concept_data = {
                "id": concept.id,
                "label": concept.label,
                "definition_full": concept.definition_full,
                "source_evidence": concept.source_evidence,
                "lineage": concept.lineage,
                "generation": concept.generation,
                "state": concept.state.value,
                "relations": [
                    {
                        "type": rel.type,
                        "target_id": rel.target_id,
                        "evidence": rel.evidence
                    }
                    for rel in concept.relations
                ],
                "contradictions": [
                    {
                        "with_id": cont.with_id,
                        "contradiction_basis": cont.contradiction_basis,
                        "resolution": cont.resolution
                    }
                    for cont in concept.contradictions
                ],
                "metrics": {
                    "support_strength": concept.support_strength,
                    "definition_completeness": concept.definition_completeness,
                    "merge_count": concept.merge_count
                },
                "timestamp": concept.timestamp
            }
            concepts_data.append(concept_data)

        evolution_data = []
        for event in self.evolution_log:
            event_data = {
                "operation": event.operation.value,
                "parent_ids": event.parent_ids,
                "offspring_id": event.offspring_id,
                "transformation": event.transformation,
                "delta": event.delta,
                "quality_improvement": event.quality_improvement,
                "success": event.success,
                "timestamp": event.timestamp
            }
            evolution_data.append(event_data)

        result = {
            "ecosystem_stats": stats,
            "concepts": concepts_data,
            "evolution_log": evolution_data
        }

        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(result, f, indent=2, ensure_ascii=False)

        return result