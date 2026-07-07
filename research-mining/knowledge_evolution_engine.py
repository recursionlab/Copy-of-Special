#!/usr/bin/env python3
"""
Knowledge Evolution Engine - Semantic autopoiesis for concept units
Transforms biological autopoiesis into conceptual synthesis and refinement
"""

import json
import uuid
import random
from datetime import datetime
from typing import Dict, List, Optional, Set
from dataclasses import dataclass, field
from enum import Enum

class ConceptState(Enum):
    ACTIVE = "ACTIVE"
    REDUNDANT = "REDUNDANT"
    CONTRADICTORY = "CONTRADICTORY"

class EvolutionOperation(Enum):
    ASEXUAL_REFINEMENT = "ASEXUAL_REFINEMENT"
    CROSS_SYNTHESIS = "CROSS_SYNTHESIS"

@dataclass
class ConceptRelation:
    type: str  # supports, contradicts, refines, extends, specializes
    target_id: str
    evidence: str

@dataclass
class ConceptContradiction:
    with_id: str
    basis: str
    resolution: Optional[str] = None

@dataclass
class ConceptUnit:
    """Evolved concept with semantic relationships"""
    id: str
    label: str
    definition: str
    lineage: List[str] = field(default_factory=list)
    generation: int = 0
    state: ConceptState = ConceptState.ACTIVE
    relations: List[ConceptRelation] = field(default_factory=list)
    contradictions: List[ConceptContradiction] = field(default_factory=list)
    support_strength: float = 1.0  # evidence weight
    diversity_contribution: float = 0.0
    usage_frequency: int = 0
    timestamp: str = field(default_factory=lambda: datetime.now().isoformat())

@dataclass
class EvolutionEvent:
    """Record of concept synthesis/refinement"""
    operation: EvolutionOperation
    parent_ids: List[str]
    offspring_id: str
    transformation: str
    success: bool
    notes: str = ""
    timestamp: str = field(default_factory=lambda: datetime.now().isoformat())

class KnowledgeEvolutionEngine:
    """Autopoietic system for evolving conceptual knowledge"""

    def __init__(self):
        self.concepts: Dict[str, ConceptUnit] = {}
        self.evolution_log: List[EvolutionEvent] = []

        # Evolution parameters (lowered for more activity)
        self.REFINEMENT_THRESHOLD = 0.4  # min support strength to refine
        self.SYNTHESIS_THRESHOLD = 0.5   # min combined strength for cross-synthesis
        self.MAX_GENERATION = 4          # prevent infinite recursion

    def add_concept_from_unit(self, concept_data: dict, force_unique_id: bool = False) -> ConceptUnit:
        """Create concept from extracted ConceptUnit"""
        original_id = concept_data.get('id', f'concept-{uuid.uuid4().hex[:8]}')

        # Create unique ID if requested or if concept already exists
        if force_unique_id or original_id in self.concepts:
            concept_id = f"{original_id}-{uuid.uuid4().hex[:6]}"
        else:
            concept_id = original_id

        # Extract semantic content with better fallbacks
        label = concept_data.get('term',
                concept_data.get('type',
                concept_data.get('id', 'Unknown')))

        definition = concept_data.get('definition',
                    concept_data.get('notes',
                    'No definition available'))

        # Calculate support strength from confidence + definition quality
        confidence = concept_data.get('confidence_score', 0.5)
        definition_quality = min(1.0, len(definition) / 100.0)  # longer = better up to 100 chars
        support_strength = (confidence + definition_quality) / 2.0

        concept = ConceptUnit(
            id=concept_id,
            label=label,
            definition=definition,
            support_strength=support_strength,
            timestamp=concept_data.get('extraction_date', datetime.now().isoformat())
        )

        self.concepts[concept_id] = concept
        return concept

    def detect_semantic_relations(self, concept1: ConceptUnit, concept2: ConceptUnit) -> List[ConceptRelation]:
        """Detect potential semantic relations between concepts"""
        relations = []

        # Enhanced keyword-based relation detection
        def1_words = set(word.strip('.,!?') for word in concept1.definition.lower().split() if len(word) > 3)
        def2_words = set(word.strip('.,!?') for word in concept2.definition.lower().split() if len(word) > 3)
        label1_words = set(concept1.label.lower().split())
        label2_words = set(concept2.label.lower().split())

        overlap = def1_words.intersection(def2_words)
        overlap_ratio = len(overlap) / max(len(def1_words), len(def2_words), 1)

        # Strong semantic overlap
        if overlap_ratio > 0.3 or len(overlap) > 3:
            relations.append(ConceptRelation(
                type="related_to",
                target_id=concept2.id,
                evidence=f"Significant semantic overlap: {list(overlap)[:3]}"
            ))

        # Label-definition references
        if any(word in concept2.definition.lower() for word in label1_words):
            relations.append(ConceptRelation(
                type="supports",
                target_id=concept2.id,
                evidence=f"'{concept1.label}' concept referenced in definition"
            ))

        # Hierarchical relations
        hierarchy_signals = ['type of', 'kind of', 'example of', 'instance of', 'subtype']
        for signal in hierarchy_signals:
            if signal in concept1.definition.lower() and any(word in concept1.definition.lower() for word in label2_words):
                relations.append(ConceptRelation(
                    type="example_of",
                    target_id=concept2.id,
                    evidence=f"Hierarchical relationship detected: '{signal}'"
                ))

        # Extension/refinement relations
        extension_signals = ['extends', 'builds on', 'develops', 'expands']
        for signal in extension_signals:
            if signal in concept1.definition.lower():
                relations.append(ConceptRelation(
                    type="extends",
                    target_id=concept2.id,
                    evidence=f"Extension relationship: '{signal}'"
                ))

        # Contradiction detection
        contradiction_signals = ['not', 'opposite', 'against', 'contradiction', 'contrary', 'conflicts', 'disputes']
        negation_patterns = ['is not', 'does not', 'cannot', 'never']

        has_negation = any(pattern in concept1.definition.lower() for pattern in negation_patterns)
        has_contradiction = any(signal in concept1.definition.lower() for signal in contradiction_signals)

        if (has_negation or has_contradiction) and overlap_ratio > 0.2:
            relations.append(ConceptRelation(
                type="contradicts",
                target_id=concept2.id,
                evidence="Contradictory elements detected in definitions"
            ))

        return relations

    def asexual_refinement(self, parent_id: str) -> Optional[ConceptUnit]:
        """Refine a single concept (asexual evolution)"""
        if parent_id not in self.concepts:
            return None

        parent = self.concepts[parent_id]

        # Only refine concepts with sufficient support
        if parent.support_strength < self.REFINEMENT_THRESHOLD:
            return None

        if parent.generation >= self.MAX_GENERATION:
            return None

        # Create refined version
        offspring_id = f'refined-{parent_id}-{uuid.uuid4().hex[:6]}'

        # Refinement: enhance definition with more specificity
        refined_definition = self._refine_definition(parent.definition)

        offspring = ConceptUnit(
            id=offspring_id,
            label=f"{parent.label} (Refined)",
            definition=refined_definition,
            lineage=[parent_id],
            generation=parent.generation + 1,
            support_strength=parent.support_strength * 0.9,  # slight reduction for speculation
            relations=parent.relations.copy(),  # inherit relations
            contradictions=parent.contradictions.copy()
        )

        self.concepts[offspring_id] = offspring
        parent.usage_frequency += 1

        # Log evolution event
        event = EvolutionEvent(
            operation=EvolutionOperation.ASEXUAL_REFINEMENT,
            parent_ids=[parent_id],
            offspring_id=offspring_id,
            transformation="Definition refinement and specialization",
            success=True,
            notes=f"Refined '{parent.label}' with enhanced specificity"
        )
        self.evolution_log.append(event)

        return offspring

    def cross_synthesis(self, parent1_id: str, parent2_id: str) -> Optional[ConceptUnit]:
        """Synthesize two concepts into a hybrid (sexual evolution)"""
        if parent1_id not in self.concepts or parent2_id not in self.concepts:
            return None

        parent1 = self.concepts[parent1_id]
        parent2 = self.concepts[parent2_id]

        # Check synthesis viability
        combined_strength = (parent1.support_strength + parent2.support_strength) / 2
        if combined_strength < self.SYNTHESIS_THRESHOLD:
            return None

        max_generation = max(parent1.generation, parent2.generation)
        if max_generation >= self.MAX_GENERATION:
            return None

        # Create synthesized concept
        offspring_id = f'synthesis-{parent1_id[:8]}-{parent2_id[:8]}-{uuid.uuid4().hex[:4]}'

        # Synthesis: combine definitions meaningfully
        synthesized_definition = self._synthesize_definitions(parent1.definition, parent2.definition)
        hybrid_label = f"{parent1.label} × {parent2.label}"

        offspring = ConceptUnit(
            id=offspring_id,
            label=hybrid_label,
            definition=synthesized_definition,
            lineage=[parent1_id, parent2_id],
            generation=max_generation + 1,
            support_strength=combined_strength * 1.1,  # synthesis bonus
            relations=self._merge_relations(parent1.relations, parent2.relations),
            contradictions=self._merge_contradictions(parent1.contradictions, parent2.contradictions)
        )

        self.concepts[offspring_id] = offspring
        parent1.usage_frequency += 1
        parent2.usage_frequency += 1

        # Log evolution event
        event = EvolutionEvent(
            operation=EvolutionOperation.CROSS_SYNTHESIS,
            parent_ids=[parent1_id, parent2_id],
            offspring_id=offspring_id,
            transformation="Cross-synthesis of complementary concepts",
            success=True,
            notes=f"Synthesized '{parent1.label}' and '{parent2.label}' into hybrid concept"
        )
        self.evolution_log.append(event)

        return offspring

    def evolve_knowledge_ecosystem(self, cycles: int = 10):
        """Run knowledge evolution cycles"""
        for cycle in range(cycles):
            active_concepts = [cid for cid, c in self.concepts.items()
                             if c.state == ConceptState.ACTIVE]

            if len(active_concepts) < 2:
                break

            # Evolution attempts per cycle
            attempts = min(len(active_concepts) // 3, 5)

            for _ in range(attempts):
                if random.random() < 0.7:  # 70% refinement, 30% synthesis
                    parent = random.choice(active_concepts)
                    self.asexual_refinement(parent)
                else:
                    if len(active_concepts) >= 2:
                        parent1, parent2 = random.sample(active_concepts, 2)
                        self.cross_synthesis(parent1, parent2)

            # Update concept states
            self._update_concept_states()

            # Calculate diversity contributions
            self._calculate_diversity_contributions()

    def _refine_definition(self, definition: str) -> str:
        """Enhance definition with more specificity"""
        refinement_patterns = [
            "more specifically",
            "with particular emphasis on",
            "characterized by",
            "involving the process of"
        ]

        pattern = random.choice(refinement_patterns)
        return f"{definition} {pattern} enhanced conceptual precision."

    def _synthesize_definitions(self, def1: str, def2: str) -> str:
        """Combine two definitions meaningfully"""
        synthesis_patterns = [
            f"The integration of ({def1}) with ({def2})",
            f"A hybrid concept combining {def1[:50]}... and {def2[:50]}...",
            f"The emergent property arising from the intersection of '{def1}' and '{def2}'"
        ]

        return random.choice(synthesis_patterns)

    def _merge_relations(self, rel1: List[ConceptRelation], rel2: List[ConceptRelation]) -> List[ConceptRelation]:
        """Merge relation lists, removing duplicates"""
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

    def _update_concept_states(self):
        """Update concept states based on usage and redundancy"""
        concept_definitions = {}

        # Group by similar definitions to find redundancy
        for concept in self.concepts.values():
            def_key = concept.definition[:50].lower()  # first 50 chars as key
            if def_key not in concept_definitions:
                concept_definitions[def_key] = []
            concept_definitions[def_key].append(concept)

        # Mark redundant concepts
        for similar_concepts in concept_definitions.values():
            if len(similar_concepts) > 1:
                # Keep the one with highest support, mark others redundant
                best = max(similar_concepts, key=lambda c: c.support_strength)
                for concept in similar_concepts:
                    if concept != best and concept.usage_frequency == 0:
                        concept.state = ConceptState.REDUNDANT

    def _calculate_diversity_contributions(self):
        """Calculate how much each concept contributes to diversity"""
        total_concepts = len([c for c in self.concepts.values() if c.state == ConceptState.ACTIVE])

        for concept in self.concepts.values():
            if concept.state == ConceptState.ACTIVE:
                # Diversity based on unique relations + definition uniqueness
                unique_relations = len(set(r.type for r in concept.relations))
                definition_uniqueness = 1.0 / (1 + concept.usage_frequency)
                concept.diversity_contribution = unique_relations * definition_uniqueness

    def get_ecosystem_stats(self) -> dict:
        """Get knowledge ecosystem statistics"""
        active_concepts = [c for c in self.concepts.values() if c.state == ConceptState.ACTIVE]
        total_relations = sum(len(c.relations) for c in active_concepts)
        total_contradictions = sum(len(c.contradictions) for c in active_concepts)

        # Calculate conceptual diversity (Shannon entropy)
        import math
        diversity = 0.0
        if active_concepts:
            label_counts = {}
            for concept in active_concepts:
                label_type = concept.label.split()[0].lower()  # first word of label
                label_counts[label_type] = label_counts.get(label_type, 0) + 1

            total = len(active_concepts)
            for count in label_counts.values():
                if count > 0:
                    proportion = count / total
                    diversity -= proportion * math.log2(proportion)

        return {
            "total_concepts": len(self.concepts),
            "active_concepts": len(active_concepts),
            "conceptual_diversity": diversity,
            "relation_count": total_relations,
            "contradiction_count": total_contradictions
        }

    def export_knowledge_evolution(self, output_path: str):
        """Export results in semantic knowledge evolution format"""
        stats = self.get_ecosystem_stats()

        concepts_data = []
        for concept in self.concepts.values():
            concept_data = {
                "id": concept.id,
                "label": concept.label,
                "definition": concept.definition,
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
                        "basis": cont.basis,
                        "resolution": cont.resolution
                    }
                    for cont in concept.contradictions
                ],
                "metrics": {
                    "support_strength": concept.support_strength,
                    "diversity_contribution": concept.diversity_contribution,
                    "usage_frequency": concept.usage_frequency
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
                "success": event.success,
                "notes": event.notes,
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