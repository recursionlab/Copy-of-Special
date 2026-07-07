#!/usr/bin/env python3
"""
Test Knowledge Evolution Engine v2 - Quality-First
"""

import json
import sys
import os
from pathlib import Path

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from knowledge_evolution_v2 import KnowledgeEvolutionV2

def load_conversation_concepts(file_path):
    """Load concept units from conversation export"""
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def main():
    print("Testing Knowledge Evolution Engine v2 - Quality-First")
    print("=" * 65)

    # Load conversation data
    archive_dir = Path("archive")
    conversation_file = archive_dir / "conversation_export_units.json"

    if not conversation_file.exists():
        print(f"ERROR: Conversation file not found: {conversation_file}")
        return

    print(f"Loading concepts from: {conversation_file}")
    concepts = load_conversation_concepts(conversation_file)
    print(f"  Loaded {len(concepts)} concept units")

    # Initialize v2 engine
    print(f"\nInitializing Quality-First Knowledge Evolution Engine...")
    engine = KnowledgeEvolutionV2()

    # Add concepts with quality filtering
    print(f"Adding concepts with quality validation...")
    added_count = 0
    rejected_count = 0

    # Sample more strategically for diversity
    step_size = max(1, len(concepts) // 50)
    sampled_concepts = concepts[::step_size][:50]

    for i, concept_data in enumerate(sampled_concepts):
        concept = engine.add_concept_from_unit(concept_data)
        if concept:
            added_count += 1
            if added_count <= 5:  # Show first 5
                print(f"  Added: {concept.label} (quality: {concept.definition_completeness:.3f})")
        else:
            rejected_count += 1

    print(f"  Quality filtering results:")
    print(f"    Added: {added_count} high-quality concepts")
    print(f"    Rejected: {rejected_count} low-quality concepts")
    print(f"    Merged: {engine.merged_concepts} duplicate concepts")

    if added_count == 0:
        print("No quality concepts to evolve. Exiting.")
        return

    # Detect relations with evidence
    print(f"\nDetecting evidence-backed semantic relations...")
    concept_list = list(engine.concepts.values())
    relations_found = 0

    for i in range(min(len(concept_list), 20)):  # Limit for performance
        for j in range(i+1, min(i+8, len(concept_list))):
            relations = engine.detect_semantic_relations(concept_list[i], concept_list[j])
            for relation in relations:
                concept_list[i].relations.append(relation)
                relations_found += 1

    print(f"  Found {relations_found} evidence-backed relations")

    # Detect contradictions
    print(f"Detecting contradictions...")
    engine.detect_contradictions()
    contradiction_count = sum(len(c.contradictions) for c in engine.concepts.values())
    contradictory_concepts = len([c for c in engine.concepts.values() if c.state.name == 'CONTRADICTORY'])
    print(f"  Found {contradiction_count} contradictions affecting {contradictory_concepts} concepts")

    # Get initial stats
    initial_stats = engine.get_ecosystem_stats()
    print(f"\nInitial ecosystem state:")
    print(f"  Active concepts: {initial_stats['active_concepts']}")
    print(f"  Quality score: {initial_stats['quality_score']:.3f}")
    print(f"  Conceptual diversity: {initial_stats['conceptual_diversity']:.3f}")
    print(f"  Relations: {initial_stats['relation_count']}")
    print(f"  Contradictions: {initial_stats['contradiction_count']}")

    # Run quality-controlled evolution
    print(f"\nRunning quality-controlled knowledge evolution...")
    engine.evolve_knowledge_ecosystem(cycles=8)

    # Get final stats
    final_stats = engine.get_ecosystem_stats()
    print(f"\nFinal ecosystem state:")
    print(f"  Total concepts: {final_stats['total_concepts']}")
    print(f"  Active concepts: {final_stats['active_concepts']}")
    print(f"  Merged concepts: {final_stats['merged_concepts']}")
    print(f"  Quality score: {final_stats['quality_score']:.3f}")
    print(f"  Conceptual diversity: {final_stats['conceptual_diversity']:.3f}")
    print(f"  Relations: {final_stats['relation_count']}")
    print(f"  Contradictions: {final_stats['contradiction_count']}")
    print(f"  Evolution events: {len(engine.evolution_log)}")

    # Analyze evolution quality
    print(f"\nEvolution Quality Analysis:")
    refinements = [e for e in engine.evolution_log if e.operation.name == 'ASEXUAL_REFINEMENT']
    syntheses = [e for e in engine.evolution_log if e.operation.name == 'CROSS_SYNTHESIS']
    merges = [e for e in engine.evolution_log if e.operation.name == 'DEDUPLICATION_MERGE']

    print(f"  Concept refinements: {len(refinements)}")
    print(f"  Cross-syntheses: {len(syntheses)}")
    print(f"  Deduplication merges: {len(merges)}")

    # Quality improvements
    quality_improvements = [e.quality_improvement for e in engine.evolution_log if e.quality_improvement > 0]
    avg_quality_improvement = sum(quality_improvements) / len(quality_improvements) if quality_improvements else 0
    print(f"  Average quality improvement: {avg_quality_improvement:.3f}")

    # Show high-quality evolved concepts
    print(f"\nTop evolved concepts by quality:")
    evolved_concepts = [c for c in engine.concepts.values() if c.generation > 0]
    top_evolved = sorted(evolved_concepts, key=lambda c: c.definition_completeness, reverse=True)[:3]

    for i, concept in enumerate(top_evolved, 1):
        print(f"  {i}. {concept.label}")
        print(f"     Generation: {concept.generation}, Quality: {concept.definition_completeness:.3f}")
        print(f"     Lineage: {' -> '.join(concept.lineage[-2:]) if len(concept.lineage) > 1 else concept.lineage}")
        print(f"     Definition: {concept.definition_full[:80]}...")

    # Export results with v2 schema
    output_file = "knowledge_evolution_v2_results.json"
    print(f"\nExporting v2 quality-first results to {output_file}...")
    engine.export_knowledge_evolution_v2(output_file)

    print(f"\nKnowledge Evolution v2 Complete!")
    print("=" * 65)
    print(f"Quality Improvements:")
    print(f"  Concept quality: {initial_stats['quality_score']:.3f} -> {final_stats['quality_score']:.3f}")
    print(f"  Active concepts: {initial_stats['active_concepts']} -> {final_stats['active_concepts']}")
    print(f"  Deduplication: {engine.merged_concepts} concepts merged")
    print(f"  Contradiction detection: {final_stats['contradiction_count']} found")
    print(f"  Average evolution quality gain: {avg_quality_improvement:.3f}")

if __name__ == "__main__":
    main()