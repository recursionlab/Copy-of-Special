#!/usr/bin/env python3
"""
Test Knowledge Evolution v2.1 - Balanced Quality-Flexibility
Test with 3-tier concept examples: HIGH, MID, and CONTRADICTORY
"""

import json
import sys
import os
from pathlib import Path

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from knowledge_evolution_v2_1 import KnowledgeEvolutionV21

def create_test_concepts():
    """Create test concepts representing all quality tiers"""
    return [
        # HIGH QUALITY - Should survive and evolve
        {
            "id": "consciousness-high",
            "term": "Consciousness",
            "definition": "Consciousness is the subjective experience of being aware and having phenomenal states. It involves the integration of sensory information with memory, attention, and cognitive processes to create a unified first-person perspective of reality.",
            "confidence_score": 0.9,
            "notes": "Extracted from comprehensive philosophical analysis",
            "source": "Stanford Encyclopedia of Philosophy",
            "extraction_date": "2025-09-15T10:00:00"
        },

        # MID QUALITY - Should be refined and improved
        {
            "id": "recursion-mid",
            "term": "Recursion",
            "definition": "A process that calls itself with different parameters, enabling infinite generation from finite rules.",
            "confidence_score": 0.6,
            "notes": "Basic definition from computer science context",
            "source": "Programming textbook chapter 5"
        },

        # LOW QUALITY - Should be queued for refinement
        {
            "id": "emergence-low",
            "term": "Emergence",
            "definition": "Properties arising from interactions.",
            "confidence_score": 0.4,
            "notes": "Fragment from larger text",
        },

        # CONTRADICTORY PAIR 1
        {
            "id": "systems-closed",
            "term": "Systems",
            "definition": "Systems are closed structures that maintain stability through rigid boundaries and controlled inputs.",
            "confidence_score": 0.7,
            "source": "Classical systems theory"
        },

        # CONTRADICTORY PAIR 2
        {
            "id": "systems-open",
            "term": "Systems",
            "definition": "Systems are open networks that evolve through dynamic interactions with their environment.",
            "confidence_score": 0.7,
            "source": "Modern complexity theory"
        },

        # WILL BE MERGED - Similar to consciousness
        {
            "id": "awareness-duplicate",
            "term": "Awareness",
            "definition": "Consciousness involves the subjective experience of being aware and having phenomenal states through cognitive integration.",
            "confidence_score": 0.8,
            "source": "Cognitive science handbook"
        },

        # MID QUALITY - Different domain
        {
            "id": "autopoiesis-mid",
            "term": "Autopoiesis",
            "definition": "Self-creating systems that maintain their organization through continuous regeneration of components.",
            "confidence_score": 0.65,
            "source": "Maturana and Varela foundational work"
        }
    ]

def main():
    print("Testing Knowledge Evolution v2.1 - Balanced Quality-Flexibility")
    print("=" * 70)

    # Initialize balanced system
    engine = KnowledgeEvolutionV21()

    # Create test concept suite
    test_concepts = create_test_concepts()
    print(f"Testing with {len(test_concepts)} diverse quality concepts...")

    # Add concepts and show tiering
    print(f"\nConcept Quality Tiering:")
    added_concepts = {}

    for concept_data in test_concepts:
        concept = engine.add_concept_from_unit(concept_data)
        if concept:
            added_concepts[concept.id] = concept
            print(f"  {concept.label[:20]:20} | {concept.quality_tier.value:4} | {concept.state.value:15} | Quality: {concept.definition_completeness:.3f}")
        else:
            print(f"  {concept_data['term'][:20]:20} | REJECTED - Below minimum threshold")

    print(f"\nQuality Distribution:")
    print(f"  Added: {len(added_concepts)} concepts")
    print(f"  Merged: {engine.merged_concepts} duplicates")
    print(f"  Refinement queue: {len(engine.refinement_queue)} concepts")

    # Show refinement queue
    if engine.refinement_queue:
        print(f"\nRefinement Queue:")
        for i, queued in enumerate(engine.refinement_queue, 1):
            concept = engine.concepts[queued.concept_id]
            print(f"  {i}. {concept.label} - {queued.refinement_type.value} (Priority: {queued.priority.value})")

    # Get initial stats
    initial_stats = engine.get_ecosystem_stats()
    print(f"\nInitial Ecosystem State:")
    print(f"  Total concepts: {initial_stats['total_concepts']}")
    print(f"  High quality: {initial_stats['high_quality_concepts']}")
    print(f"  Mid quality: {initial_stats['mid_quality_concepts']}")
    print(f"  Queue size: {initial_stats['refinement_queue_size']}")
    print(f"  Quality score: {initial_stats['quality_score']:.3f}")
    print(f"  Contradictions: {initial_stats['contradiction_count']}")

    # Process refinement queue manually to see results
    print(f"\nProcessing Refinement Queue...")
    engine.process_refinement_queue(max_refinements=5)

    # Check refinement results
    refined_concepts = [c for c in engine.concepts.values() if c.refinement_attempts > 0]
    print(f"Refinement Results:")
    for concept in refined_concepts:
        improvement = concept.successful_refinements / max(1, concept.refinement_attempts)
        print(f"  {concept.label}: {concept.refinement_attempts} attempts, {concept.successful_refinements} successful ({improvement:.1%})")

    # Run balanced evolution
    print(f"\nRunning Balanced Knowledge Evolution (6 cycles)...")
    engine.evolve_knowledge_ecosystem(cycles=6)

    # Final stats
    final_stats = engine.get_ecosystem_stats()
    print(f"\nFinal Ecosystem State:")
    print(f"  Total concepts: {final_stats['total_concepts']}")
    print(f"  Active concepts: {final_stats['active_concepts']}")
    print(f"  High quality: {final_stats['high_quality_concepts']}")
    print(f"  Mid quality: {final_stats['mid_quality_concepts']}")
    print(f"  Quality score: {final_stats['quality_score']:.3f}")
    print(f"  Refinement success rate: {final_stats['refinement_success_rate']:.1%}")
    print(f"  Evolution events: {len(engine.evolution_log)}")
    print(f"  Contradictions detected: {final_stats['contradiction_count']}")

    # Show evolution event breakdown
    print(f"\nEvolution Event Analysis:")
    event_types = {}
    for event in engine.evolution_log:
        event_type = event.operation.value
        event_types[event_type] = event_types.get(event_type, 0) + 1

    for event_type, count in event_types.items():
        print(f"  {event_type}: {count}")

    # Show quality improvements
    quality_events = [e for e in engine.evolution_log if e.quality_improvement > 0]
    if quality_events:
        avg_improvement = sum(e.quality_improvement for e in quality_events) / len(quality_events)
        print(f"  Average quality improvement: {avg_improvement:.3f}")

    # Show tier upgrades
    tier_upgrades = [e for e in engine.evolution_log if e.quality_tier_change]
    if tier_upgrades:
        print(f"  Quality tier upgrades: {len(tier_upgrades)}")

    # Show top concepts by quality
    print(f"\nTop Concepts by Quality:")
    all_concepts = list(engine.concepts.values())
    top_concepts = sorted(all_concepts, key=lambda c: c.definition_completeness, reverse=True)[:5]

    for i, concept in enumerate(top_concepts, 1):
        print(f"  {i}. {concept.label} ({concept.quality_tier.value})")
        print(f"     Quality: {concept.definition_completeness:.3f}, Generation: {concept.generation}")
        print(f"     Definition: {concept.definition_full[:80]}...")
        if concept.refinement_history:
            print(f"     Refinements: {len(concept.refinement_history)} attempts")

    # Show contradictions found
    contradictory_concepts = [c for c in all_concepts if c.contradictions]
    if contradictory_concepts:
        print(f"\nContradictions Detected:")
        for concept in contradictory_concepts:
            for contradiction in concept.contradictions:
                other_concept = engine.concepts[contradiction.with_id]
                print(f"  {concept.label} vs {other_concept.label}")
                print(f"    Basis: {contradiction.contradiction_basis[:80]}...")

    # Export results
    output_file = "knowledge_evolution_v2_1_results.json"
    print(f"\nExporting v2.1 results to {output_file}...")
    engine.export_knowledge_evolution_v2_1(output_file)

    print(f"\nKnowledge Evolution v2.1 Test Complete!")
    print("=" * 70)
    print("BALANCED RESULTS:")
    print(f"  Quality Flexibility: {initial_stats['total_concepts']} -> {final_stats['total_concepts']} concepts")
    print(f"  Quality Improvement: {initial_stats['quality_score']:.3f} -> {final_stats['quality_score']:.3f}")
    print(f"  High-Quality Concepts: {initial_stats['high_quality_concepts']} -> {final_stats['high_quality_concepts']}")
    print(f"  Refinement Success: {final_stats['refinement_success_rate']:.1%}")
    print(f"  Contradiction Detection: {final_stats['contradiction_count']} found")
    print(f"  Deduplication: {engine.merged_concepts} concepts merged")

if __name__ == "__main__":
    main()