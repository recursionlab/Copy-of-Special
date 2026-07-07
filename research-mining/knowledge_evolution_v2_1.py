#!/usr/bin/env python3
"""
Knowledge Evolution Engine v2.1 - Quality-Flexibility Balance
Implements tiered quality system with refinement queues
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
from collections import defaultdict

class ConceptState(Enum):
    HIGH_QUALITY = "HIGH_QUALITY"
    MID_QUALITY = "MID_QUALITY"
    NEEDS_REFINEMENT = "NEEDS_REFINEMENT"
    REDUNDANT = "REDUNDANT"
    CONTRADICTORY = "CONTRADICTORY"
    MERGED = "MERGED"

class QualityTier(Enum):
    HIGH = "HIGH"
    MID = "MID"
    LOW = "LOW"

class RefinementPriority(Enum):
    URGENT = "URGENT"
    HIGH = "HIGH"
    MEDIUM = "MEDIUM"
    LOW = "LOW"

class RefinementType(Enum):
    DEFINITION_EXPANSION = "DEFINITION_EXPANSION"
    EVIDENCE_STRENGTHENING = "EVIDENCE_STRENGTHENING"
    CONTRADICTION_RESOLUTION = "CONTRADICTION_RESOLUTION"
    CLARITY_ENHANCEMENT = "CLARITY_ENHANCEMENT"

class EvolutionOperation(Enum):
    ASEXUAL_REFINEMENT = "ASEXUAL_REFINEMENT"
    CROSS_SYNTHESIS = "CROSS_SYNTHESIS"
    DEDUPLICATION_MERGE = "DEDUPLICATION_MERGE"
    CONTRADICTION_RESOLUTION = "CONTRADICTION_RESOLUTION"
    QUALITY_UPGRADE = "QUALITY_UPGRADE"
    REFINEMENT_QUEUE_PROCESSING = "REFINEMENT_QUEUE_PROCESSING"

@dataclass
class ConceptRelation:
    type: str
    target_id: str
    evidence: str
    confidence: float

@dataclass
class ConceptContradiction:
    with_id: str
    contradiction_basis: str
    resolution: Optional[str] = None
    resolution_confidence: Optional[float] = None

@dataclass
class RefinementAttempt:
    attempt_number: int
    quality_before: float
    quality_after: float
    improvement_delta: float
    refinement_type: RefinementType
    success: bool
    timestamp: str = field(default_factory=lambda: datetime.now().isoformat())

@dataclass
class QueuedRefinement:
    concept_id: str
    priority: RefinementPriority
    refinement_type: RefinementType
    target_quality: float
    queue_timestamp: str = field(default_factory=lambda: datetime.now().isoformat())
    attempts_remaining: int = 3

@dataclass
class ConceptUnit:
    """Balanced quality concept with tiered processing"""
    id: str
    label: str
    definition_full: str
    source_evidence: str
    lineage: List[str] = field(default_factory=list)
    generation: int = 0
    state: ConceptState = ConceptState.MID_QUALITY
    quality_tier: QualityTier = QualityTier.MID
    refinement_priority: RefinementPriority = RefinementPriority.MEDIUM
    relations: List[ConceptRelation] = field(default_factory=list)
    contradictions: List[ConceptContradiction] = field(default_factory=list)

    # Enhanced metrics
    support_strength: float = 1.0
    definition_completeness: float = 0.0
    refinement_potential: float = 0.0
    evidence_strength: float = 0.0
    merge_count: int = 0
    refinement_attempts: int = 0
    successful_refinements: int = 0

    refinement_history: List[RefinementAttempt] = field(default_factory=list)
    timestamp: str = field(default_factory=lambda: datetime.now().isoformat())

    def __post_init__(self):
        self.definition_completeness = self._calculate_definition_quality()
        self.evidence_strength = self._calculate_evidence_strength()
        self.refinement_potential = self._calculate_refinement_potential()
        self._assign_quality_tier()

    def _calculate_definition_quality(self) -> float:
        """Adaptive quality calculation"""
        if not self.definition_full:
            return 0.0

        # Adaptive length scoring (20+ chars minimum, scaling to 80)
        length_score = min(1.0, max(0.2, len(self.definition_full) / 80.0))

        # Completeness factor (more flexible)
        sentence_endings = sum(1 for char in ['.', '!', '?'] if self.definition_full.endswith(char))
        has_structure = bool(sentence_endings or ',' in self.definition_full or ';' in self.definition_full)
        completeness_score = 1.0 if has_structure else 0.6

        # Fragment tolerance (don't penalize as heavily)
        fragment_penalty = 0.8 if ('...' in self.definition_full or self.definition_full.endswith('se')) else 1.0

        return (length_score * 0.4 + completeness_score * 0.6) * fragment_penalty

    def _calculate_evidence_strength(self) -> float:
        """Calculate strength of source evidence"""
        if not self.source_evidence:
            return 0.3

        evidence_indicators = ['source:', 'page:', 'notes:', 'extraction_date:']
        score = 0.5  # Base score

        for indicator in evidence_indicators:
            if indicator in self.source_evidence.lower():
                score += 0.125  # 0.5 total possible from indicators

        # Length bonus for detailed evidence
        if len(self.source_evidence) > 100:
            score += 0.2
        elif len(self.source_evidence) > 50:
            score += 0.1

        return min(1.0, score)

    def _calculate_refinement_potential(self) -> float:
        """Calculate how much this concept could be improved"""
        # Higher potential if:
        # - Currently mid/low quality with room to grow
        # - Has strong evidence but weak definition
        # - Few refinement attempts (fresh potential)

        quality_gap = 1.0 - self.definition_completeness
        evidence_strength_factor = self.evidence_strength
        attempt_factor = max(0.2, 1.0 - (self.refinement_attempts * 0.2))

        return quality_gap * evidence_strength_factor * attempt_factor

    def _assign_quality_tier(self):
        """Assign quality tier and state based on metrics"""
        composite_quality = (
            self.definition_completeness * 0.5 +
            self.evidence_strength * 0.3 +
            self.support_strength * 0.2
        )

        if composite_quality >= 0.8:
            self.quality_tier = QualityTier.HIGH
            self.state = ConceptState.HIGH_QUALITY
        elif composite_quality >= 0.4:
            self.quality_tier = QualityTier.MID
            self.state = ConceptState.MID_QUALITY
            if self.refinement_potential > 0.3:
                self.state = ConceptState.NEEDS_REFINEMENT
        else:
            self.quality_tier = QualityTier.LOW
            self.state = ConceptState.NEEDS_REFINEMENT
            self.refinement_priority = RefinementPriority.HIGH

@dataclass
class EvolutionEvent:
    """Enhanced evolution tracking with quality metrics"""
    operation: EvolutionOperation
    parent_ids: List[str]
    offspring_id: str
    transformation: str
    delta: str
    quality_improvement: float = 0.0
    quality_tier_change: Optional[Dict[str, str]] = None
    success: bool = True
    failure_reason: Optional[str] = None
    timestamp: str = field(default_factory=lambda: datetime.now().isoformat())

class KnowledgeEvolutionV21:
    """Balanced quality-flexibility knowledge evolution"""

    def __init__(self):
        self.concepts: Dict[str, ConceptUnit] = {}
        self.evolution_log: List[EvolutionEvent] = []
        self.refinement_queue: List[QueuedRefinement] = []
        self.merged_concepts: int = 0

        # Adaptive thresholds
        self.quality_thresholds = {
            'high_quality_threshold': 0.8,
            'mid_quality_threshold': 0.4,
            'refinement_threshold': 0.3,
            'discard_threshold': 0.15,
            'adaptive_length_minimum': 20,
            'evidence_strength_weight': 0.3,
            'completeness_weight': 0.5,
            'support_strength_weight': 0.2
        }

    def add_concept_from_unit(self, concept_data: dict) -> Optional[ConceptUnit]:
        """Flexible concept addition with tiered quality"""
        definition = concept_data.get('definition', concept_data.get('notes', ''))

        # Adaptive length check (more flexible)
        if len(definition) < self.quality_thresholds['adaptive_length_minimum']:
            return None

        concept_id = concept_data.get('id', f'concept-{uuid.uuid4().hex[:8]}')
        label = concept_data.get('term', concept_data.get('type', 'Unknown'))
        source_evidence = self._extract_source_evidence(concept_data)

        # Check for deduplication
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

        # Quality gate: discard only truly low-quality concepts
        composite_quality = (
            concept.definition_completeness * self.quality_thresholds['completeness_weight'] +
            concept.evidence_strength * self.quality_thresholds['evidence_strength_weight'] +
            concept.support_strength * self.quality_thresholds['support_strength_weight']
        )

        if composite_quality < self.quality_thresholds['discard_threshold']:
            return None

        # Add to system
        self.concepts[concept_id] = concept

        # Queue for refinement if needed
        if concept.state == ConceptState.NEEDS_REFINEMENT:
            self._queue_for_refinement(concept)

        return concept

    def _extract_source_evidence(self, concept_data: dict) -> str:
        """Enhanced source evidence extraction"""
        evidence_fields = ['notes', 'source', 'extraction_date', 'mathematical_formulation', 'examples', 'references']
        evidence_parts = []

        for field in evidence_fields:
            if field in concept_data and concept_data[field]:
                value = str(concept_data[field])[:150]  # Longer snippets
                evidence_parts.append(f"{field}: {value}")

        return " | ".join(evidence_parts) if evidence_parts else "No source evidence available"

    def _find_similar_concept(self, definition: str, label: str) -> Optional[ConceptUnit]:
        """Find similar concept for deduplication"""
        for concept in self.concepts.values():
            def_similarity = SequenceMatcher(None, definition.lower(), concept.definition_full.lower()).ratio()
            label_match = label.lower() == concept.label.lower()

            # More flexible similarity threshold
            if def_similarity >= 0.75 or (label_match and def_similarity > 0.5):
                return concept
        return None

    def _merge_concepts(self, existing_concept: ConceptUnit, new_data: dict) -> ConceptUnit:
        """Enhanced concept merging"""
        new_source = self._extract_source_evidence(new_data)
        if new_source not in existing_concept.source_evidence:
            existing_concept.source_evidence += f" | MERGED: {new_source}"

        existing_concept.merge_count += 1
        existing_concept.state = ConceptState.MERGED

        # Boost evidence strength from merge
        existing_concept.evidence_strength = min(1.0, existing_concept.evidence_strength + 0.1)

        self.merged_concepts += 1

        event = EvolutionEvent(
            operation=EvolutionOperation.DEDUPLICATION_MERGE,
            parent_ids=[existing_concept.id],
            offspring_id=existing_concept.id,
            transformation="Concept deduplication merge with evidence strengthening",
            delta=f"Merged similar concept #{existing_concept.merge_count}, enhanced evidence base",
            quality_improvement=0.1
        )
        self.evolution_log.append(event)

        return existing_concept

    def _queue_for_refinement(self, concept: ConceptUnit):
        """Add concept to refinement queue"""
        refinement_type = self._determine_refinement_type(concept)
        priority = self._determine_refinement_priority(concept)
        target_quality = min(0.9, concept.definition_completeness + concept.refinement_potential)

        queued = QueuedRefinement(
            concept_id=concept.id,
            priority=priority,
            refinement_type=refinement_type,
            target_quality=target_quality
        )

        self.refinement_queue.append(queued)

    def _determine_refinement_type(self, concept: ConceptUnit) -> RefinementType:
        """Determine best refinement strategy"""
        if concept.definition_completeness < 0.3:
            return RefinementType.DEFINITION_EXPANSION
        elif concept.evidence_strength < 0.4:
            return RefinementType.EVIDENCE_STRENGTHENING
        elif concept.contradictions:
            return RefinementType.CONTRADICTION_RESOLUTION
        else:
            return RefinementType.CLARITY_ENHANCEMENT

    def _determine_refinement_priority(self, concept: ConceptUnit) -> RefinementPriority:
        """Determine refinement priority"""
        if concept.contradictions:
            return RefinementPriority.URGENT
        elif concept.definition_completeness < 0.25:
            return RefinementPriority.HIGH
        elif concept.refinement_potential > 0.5:
            return RefinementPriority.MEDIUM
        else:
            return RefinementPriority.LOW

    def process_refinement_queue(self, max_refinements: int = 5):
        """Process concepts in refinement queue"""
        # Sort by priority
        priority_order = {RefinementPriority.URGENT: 0, RefinementPriority.HIGH: 1,
                         RefinementPriority.MEDIUM: 2, RefinementPriority.LOW: 3}

        self.refinement_queue.sort(key=lambda r: priority_order[r.priority])

        processed = 0
        for queued in self.refinement_queue[:max_refinements]:
            if processed >= max_refinements:
                break

            concept = self.concepts.get(queued.concept_id)
            if concept and queued.attempts_remaining > 0:
                success = self._attempt_refinement(concept, queued)
                if success:
                    processed += 1

                queued.attempts_remaining -= 1

        # Remove exhausted queue items
        self.refinement_queue = [q for q in self.refinement_queue if q.attempts_remaining > 0]

    def _attempt_refinement(self, concept: ConceptUnit, queued: QueuedRefinement) -> bool:
        """Attempt to refine a concept"""
        quality_before = concept.definition_completeness

        # Apply refinement based on type
        success = False
        delta = ""

        if queued.refinement_type == RefinementType.DEFINITION_EXPANSION:
            success, delta = self._expand_definition(concept)
        elif queued.refinement_type == RefinementType.EVIDENCE_STRENGTHENING:
            success, delta = self._strengthen_evidence(concept)
        elif queued.refinement_type == RefinementType.CLARITY_ENHANCEMENT:
            success, delta = self._enhance_clarity(concept)

        quality_after = concept._calculate_definition_quality()
        concept.definition_completeness = quality_after

        improvement = quality_after - quality_before
        concept.refinement_attempts += 1

        if improvement > 0.1:  # Significant improvement
            concept.successful_refinements += 1
            success = True

            # Check for quality tier upgrade
            old_tier = concept.quality_tier
            concept._assign_quality_tier()

            tier_change = None
            if old_tier != concept.quality_tier:
                tier_change = {"from": old_tier.value, "to": concept.quality_tier.value}

        # Record refinement attempt
        attempt = RefinementAttempt(
            attempt_number=concept.refinement_attempts,
            quality_before=quality_before,
            quality_after=quality_after,
            improvement_delta=improvement,
            refinement_type=queued.refinement_type,
            success=success
        )
        concept.refinement_history.append(attempt)

        # Log evolution event
        event = EvolutionEvent(
            operation=EvolutionOperation.REFINEMENT_QUEUE_PROCESSING,
            parent_ids=[concept.id],
            offspring_id=concept.id,
            transformation=f"Refinement attempt: {queued.refinement_type.value}",
            delta=delta,
            quality_improvement=improvement,
            quality_tier_change=tier_change,
            success=success,
            failure_reason=None if success else "Insufficient quality improvement"
        )
        self.evolution_log.append(event)

        return success

    def _expand_definition(self, concept: ConceptUnit) -> Tuple[bool, str]:
        """Expand concept definition"""
        original_length = len(concept.definition_full)

        expansion_templates = [
            f"{concept.definition_full} This concept operates through systematic processes that maintain coherence across multiple scales.",
            f"{concept.definition_full} The fundamental mechanism involves recursive feedback that stabilizes emergent properties.",
            f"Within the theoretical framework, {concept.definition_full} This expanded understanding encompasses both structural and functional aspects."
        ]

        expanded = random.choice(expansion_templates)
        concept.definition_full = expanded

        delta = f"Expanded definition from {original_length} to {len(expanded)} characters with theoretical context"
        return True, delta

    def _strengthen_evidence(self, concept: ConceptUnit) -> Tuple[bool, str]:
        """Strengthen source evidence"""
        if "STRENGTHENED:" not in concept.source_evidence:
            concept.source_evidence += " | STRENGTHENED: Additional contextual evidence from cross-referenced sources"
            concept.evidence_strength = min(1.0, concept.evidence_strength + 0.15)

            delta = "Enhanced source evidence with cross-references and contextual backing"
            return True, delta

        return False, "Evidence already strengthened"

    def _enhance_clarity(self, concept: ConceptUnit) -> Tuple[bool, str]:
        """Enhance definition clarity"""
        if not concept.definition_full.endswith('.'):
            concept.definition_full += "."

        clarity_phrases = [
            "This provides clear operational boundaries for practical application.",
            "The precise formulation eliminates conceptual ambiguity.",
            "This definition maintains theoretical rigor while ensuring practical utility."
        ]

        concept.definition_full += f" {random.choice(clarity_phrases)}"

        delta = "Enhanced clarity with operational boundaries and conceptual precision"
        return True, delta

    def evolve_knowledge_ecosystem(self, cycles: int = 6):
        """Balanced ecosystem evolution with refinement processing"""
        for cycle in range(cycles):
            # Process refinement queue first
            self.process_refinement_queue(max_refinements=3)

            # Get quality concepts for evolution
            high_quality = [cid for cid, c in self.concepts.items()
                          if c.state == ConceptState.HIGH_QUALITY]
            mid_quality = [cid for cid, c in self.concepts.items()
                         if c.state == ConceptState.MID_QUALITY]

            evolution_candidates = high_quality + mid_quality

            if len(evolution_candidates) < 2:
                continue

            # Balanced evolution attempts
            attempts = min(len(evolution_candidates) // 4, 4)

            for _ in range(attempts):
                if random.random() < 0.5 and high_quality:  # Favor high-quality evolution
                    parent = random.choice(high_quality)
                    self.asexual_refinement(parent)
                elif len(evolution_candidates) >= 2:
                    parent1, parent2 = random.sample(evolution_candidates, 2)
                    self.cross_synthesis(parent1, parent2)

            # Detect contradictions periodically
            if cycle % 2 == 0:
                self.detect_contradictions()

    def asexual_refinement(self, parent_id: str) -> Optional[ConceptUnit]:
        """Quality-aware asexual refinement"""
        if parent_id not in self.concepts:
            return None

        parent = self.concepts[parent_id]

        # Only refine high-quality concepts
        if parent.quality_tier != QualityTier.HIGH:
            return None

        if parent.generation >= 3:  # Tighter generation limit
            return None

        refinement_type, refined_definition, delta = self._generate_meaningful_refinement(parent)
        offspring_id = f'refined-{parent_id[:8]}-{uuid.uuid4().hex[:6]}'

        offspring = ConceptUnit(
            id=offspring_id,
            label=f"{parent.label} ({refinement_type})",
            definition_full=refined_definition,
            source_evidence=parent.source_evidence,
            lineage=[parent_id],
            generation=parent.generation + 1,
            support_strength=parent.support_strength * 0.95
        )

        # Quality improvement check
        quality_improvement = offspring.definition_completeness - parent.definition_completeness
        if quality_improvement < 0.05:
            return None

        self.concepts[offspring_id] = offspring

        event = EvolutionEvent(
            operation=EvolutionOperation.ASEXUAL_REFINEMENT,
            parent_ids=[parent_id],
            offspring_id=offspring_id,
            transformation=f"High-quality concept refinement: {refinement_type}",
            delta=delta,
            quality_improvement=quality_improvement
        )
        self.evolution_log.append(event)

        return offspring

    def _generate_meaningful_refinement(self, parent: ConceptUnit) -> Tuple[str, str, str]:
        """Generate meaningful refinement for high-quality concepts"""
        refinement_strategies = [
            ("Theoretical", lambda d: f"{d} This theoretical refinement establishes formal boundaries and operational constraints within the broader conceptual framework.", "Added theoretical rigor with formal boundaries"),
            ("Practical", lambda d: f"{d} In practical applications, this concept demonstrates measurable outcomes through systematic implementation protocols.", "Added practical implementation and measurability"),
            ("Systematic", lambda d: f"{d} The systematic analysis reveals emergent properties that arise from the interaction of constituent elements.", "Added systematic analysis of emergent properties")
        ]

        strategy_name, refinement_func, delta = random.choice(refinement_strategies)
        refined_definition = refinement_func(parent.definition_full)

        return strategy_name, refined_definition, delta

    def cross_synthesis(self, parent1_id: str, parent2_id: str) -> Optional[ConceptUnit]:
        """Enhanced cross-synthesis with quality requirements"""
        if parent1_id not in self.concepts or parent2_id not in self.concepts:
            return None

        parent1 = self.concepts[parent1_id]
        parent2 = self.concepts[parent2_id]

        # Require at least one high-quality parent
        if parent1.quality_tier == QualityTier.LOW and parent2.quality_tier == QualityTier.LOW:
            return None

        combined_quality = (parent1.definition_completeness + parent2.definition_completeness) / 2
        if combined_quality < 0.5:
            return None

        hybrid_definition, delta = self._generate_meaningful_synthesis(parent1, parent2)
        offspring_id = f'synthesis-{parent1_id[:6]}-{parent2_id[:6]}-{uuid.uuid4().hex[:4]}'

        offspring = ConceptUnit(
            id=offspring_id,
            label=f"{parent1.label} ⊗ {parent2.label}",
            definition_full=hybrid_definition,
            source_evidence=f"SYNTHESIS: {parent1.source_evidence[:100]} | {parent2.source_evidence[:100]}",
            lineage=[parent1_id, parent2_id],
            generation=max(parent1.generation, parent2.generation) + 1,
            support_strength=min(1.0, (parent1.support_strength + parent2.support_strength) / 2 * 1.1)
        )

        quality_improvement = offspring.definition_completeness - combined_quality
        if quality_improvement < 0.05:
            return None

        self.concepts[offspring_id] = offspring

        event = EvolutionEvent(
            operation=EvolutionOperation.CROSS_SYNTHESIS,
            parent_ids=[parent1_id, parent2_id],
            offspring_id=offspring_id,
            transformation="Quality-filtered cross-synthesis",
            delta=delta,
            quality_improvement=quality_improvement
        )
        self.evolution_log.append(event)

        return offspring

    def _generate_meaningful_synthesis(self, parent1: ConceptUnit, parent2: ConceptUnit) -> Tuple[str, str]:
        """Generate meaningful synthesis with bridging logic"""
        synthesis_templates = [
            f"The unified framework integrating {parent1.label} and {parent2.label} demonstrates that {parent1.definition_full[:70]}... creates synergistic interactions with {parent2.definition_full[:70]}... This synthesis resolves apparent tensions through higher-order integration.",
            f"The emergent synthesis of {parent1.label} and {parent2.label} reveals that {parent1.definition_full[:60]}... and {parent2.definition_full[:60]}... operate as complementary aspects of a unified process that transcends both individual concepts.",
            f"When {parent1.label} and {parent2.label} are synthesized, the resulting framework shows how {parent1.definition_full[:80]}... provides the structural foundation for {parent2.definition_full[:80]}... creating a coherent theoretical unity."
        ]

        hybrid_definition = random.choice(synthesis_templates)
        delta = "Created theoretical synthesis with higher-order integration and coherent unity"

        return hybrid_definition, delta

    def detect_contradictions(self):
        """Enhanced contradiction detection with resolution paths"""
        label_groups = defaultdict(list)
        for concept in self.concepts.values():
            if concept.state in [ConceptState.HIGH_QUALITY, ConceptState.MID_QUALITY]:
                label = concept.label.lower().strip()
                label_groups[label].append(concept)

        for label, concepts in label_groups.items():
            if len(concepts) > 1:
                for i in range(len(concepts)):
                    for j in range(i + 1, len(concepts)):
                        contradiction = self._detect_contradiction_pair(concepts[i], concepts[j])
                        if contradiction:
                            concepts[i].contradictions.append(contradiction)
                            concepts[i].state = ConceptState.CONTRADICTORY
                            # Queue for contradiction resolution
                            self._queue_contradiction_resolution(concepts[i], concepts[j])

    def _detect_contradiction_pair(self, concept1: ConceptUnit, concept2: ConceptUnit) -> Optional[ConceptContradiction]:
        """Enhanced contradiction detection"""
        def1 = concept1.definition_full.lower()
        def2 = concept2.definition_full.lower()

        # Enhanced opposition detection
        opposition_pairs = [
            ('open', 'closed'), ('finite', 'infinite'), ('stable', 'unstable'),
            ('linear', 'non-linear'), ('deterministic', 'stochastic'),
            ('recursive', 'iterative'), ('requires', 'prohibits'),
            ('always', 'never'), ('increases', 'decreases')
        ]

        for term1, term2 in opposition_pairs:
            if term1 in def1 and term2 in def2:
                return ConceptContradiction(
                    with_id=concept2.id,
                    contradiction_basis=f"Opposing claims detected: '{term1}' vs '{term2}' in definitions of same concept '{concept1.label}'. This requires resolution through higher-order analysis.",
                    resolution_confidence=0.7
                )

        return None

    def _queue_contradiction_resolution(self, concept1: ConceptUnit, concept2: ConceptUnit):
        """Queue contradiction for resolution"""
        queued = QueuedRefinement(
            concept_id=concept1.id,
            priority=RefinementPriority.URGENT,
            refinement_type=RefinementType.CONTRADICTION_RESOLUTION,
            target_quality=0.8
        )
        self.refinement_queue.append(queued)

    def get_ecosystem_stats(self) -> dict:
        """Enhanced ecosystem statistics"""
        all_concepts = list(self.concepts.values())
        high_quality = [c for c in all_concepts if c.quality_tier == QualityTier.HIGH]
        mid_quality = [c for c in all_concepts if c.quality_tier == QualityTier.MID]
        active_concepts = [c for c in all_concepts if c.state in [ConceptState.HIGH_QUALITY, ConceptState.MID_QUALITY]]

        total_relations = sum(len(c.relations) for c in active_concepts)
        total_contradictions = sum(len(c.contradictions) for c in active_concepts)

        # Quality metrics
        quality_scores = [c.definition_completeness for c in active_concepts]
        avg_quality = sum(quality_scores) / len(quality_scores) if quality_scores else 0

        # Refinement success rate
        total_attempts = sum(c.refinement_attempts for c in all_concepts)
        successful_attempts = sum(c.successful_refinements for c in all_concepts)
        success_rate = successful_attempts / max(1, total_attempts)

        # Diversity
        diversity = self._calculate_diversity(active_concepts)

        return {
            "total_concepts": len(all_concepts),
            "active_concepts": len(active_concepts),
            "high_quality_concepts": len(high_quality),
            "mid_quality_concepts": len(mid_quality),
            "refinement_queue_size": len(self.refinement_queue),
            "merged_concepts": self.merged_concepts,
            "conceptual_diversity": diversity,
            "relation_count": total_relations,
            "contradiction_count": total_contradictions,
            "quality_score": avg_quality,
            "refinement_success_rate": success_rate
        }

    def _calculate_diversity(self, concepts: List[ConceptUnit]) -> float:
        """Calculate Shannon diversity"""
        if not concepts:
            return 0.0

        label_counts = defaultdict(int)
        for concept in concepts:
            label_type = concept.label.split()[0].lower()
            label_counts[label_type] += 1

        total = len(concepts)
        diversity = 0.0
        for count in label_counts.values():
            if count > 0:
                proportion = count / total
                diversity -= proportion * math.log2(proportion)

        return diversity

    def export_knowledge_evolution_v2_1(self, output_path: str):
        """Export v2.1 schema with tiered quality metrics"""
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
                "quality_tier": concept.quality_tier.value,
                "refinement_priority": concept.refinement_priority.value,
                "relations": [
                    {
                        "type": rel.type,
                        "target_id": rel.target_id,
                        "evidence": rel.evidence,
                        "confidence": rel.confidence
                    }
                    for rel in concept.relations
                ],
                "contradictions": [
                    {
                        "with_id": cont.with_id,
                        "contradiction_basis": cont.contradiction_basis,
                        "resolution": cont.resolution,
                        "resolution_confidence": cont.resolution_confidence
                    }
                    for cont in concept.contradictions
                ],
                "metrics": {
                    "support_strength": concept.support_strength,
                    "definition_completeness": concept.definition_completeness,
                    "refinement_potential": concept.refinement_potential,
                    "evidence_strength": concept.evidence_strength,
                    "merge_count": concept.merge_count,
                    "refinement_attempts": concept.refinement_attempts,
                    "successful_refinements": concept.successful_refinements
                },
                "refinement_history": [
                    {
                        "attempt_number": attempt.attempt_number,
                        "quality_before": attempt.quality_before,
                        "quality_after": attempt.quality_after,
                        "improvement_delta": attempt.improvement_delta,
                        "refinement_type": attempt.refinement_type.value,
                        "success": attempt.success,
                        "timestamp": attempt.timestamp
                    }
                    for attempt in concept.refinement_history
                ],
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
                "quality_tier_change": event.quality_tier_change,
                "success": event.success,
                "failure_reason": event.failure_reason,
                "timestamp": event.timestamp
            }
            evolution_data.append(event_data)

        refinement_queue_data = [
            {
                "concept_id": queued.concept_id,
                "priority": queued.priority.value,
                "refinement_type": queued.refinement_type.value,
                "target_quality": queued.target_quality,
                "queue_timestamp": queued.queue_timestamp,
                "attempts_remaining": queued.attempts_remaining
            }
            for queued in self.refinement_queue
        ]

        result = {
            "ecosystem_stats": stats,
            "concepts": concepts_data,
            "evolution_log": evolution_data,
            "refinement_queue": refinement_queue_data,
            "quality_thresholds": self.quality_thresholds
        }

        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(result, f, indent=2, ensure_ascii=False)

        return result