#!/usr/bin/env python3
"""
Test semantic knowledge evolution on conversation data
"""

import json
import sys
import os
from pathlib import Path

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from knowledge_evolution_engine import KnowledgeEvolutionEngine

def load_conversation_concepts(file_path):
    """Load concept units from conversation export"""
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def main():
    print("Testing Semantic Knowledge Evolution Engine")
    print("=" * 60)

    # Load conversation data
    archive_dir = Path("archive")
    conversation_file = archive_dir / "conversation_export_units.json"

    if not conversation_file.exists():
        print(f"ERROR: Conversation file not found: {conversation_file}")
        return

    print(f"Loading concepts from: {conversation_file}")
    concepts = load_conversation_concepts(conversation_file)
    print(f"  Loaded {len(concepts)} concept units")

    # Initialize knowledge evolution engine
    print(f"\nInitializing knowledge evolution engine...")
    engine = KnowledgeEvolutionEngine()

    # Add concepts from conversation data (more diverse sampling)
    print(f"Creating concept units from conversation concepts...")

    # Sample concepts more strategically to get diversity
    step_size = max(1, len(concepts) // 40)  # Sample every N concepts
    sampled_concepts = concepts[::step_size][:40]  # Take up to 40 diverse concepts

    for i, concept_data in enumerate(sampled_concepts):
        concept = engine.add_concept_from_unit(concept_data, force_unique_id=True)
        if i < 5:  # Show first 5
            print(f"  Created: {concept.label} (support: {concept.support_strength:.3f})")

    print(f"  Total concepts added: {len(engine.concepts)}")
    print(f"  Sampled from {len(concepts)} total with step size {step_size}")

    # Detect initial relations between concepts
    print(f"\nDetecting semantic relations...")
    concept_list = list(engine.concepts.values())
    relations_found = 0

    for i in range(len(concept_list)):
        for j in range(i+1, min(i+6, len(concept_list))):  # Check nearby concepts
            relations = engine.detect_semantic_relations(concept_list[i], concept_list[j])
            for relation in relations:
                concept_list[i].relations.append(relation)
                relations_found += 1

    print(f"  Found {relations_found} semantic relations")

    # Get initial stats
    initial_stats = engine.get_ecosystem_stats()
    print(f"\nInitial ecosystem state:")
    print(f"  Active concepts: {initial_stats['active_concepts']}")
    print(f"  Conceptual diversity: {initial_stats['conceptual_diversity']:.3f}")
    print(f"  Relations: {initial_stats['relation_count']}")
    print(f"  Contradictions: {initial_stats['contradiction_count']}")

    # Run knowledge evolution
    print(f"\nRunning knowledge evolution (12 cycles)...")
    engine.evolve_knowledge_ecosystem(cycles=12)

    # Get final stats
    final_stats = engine.get_ecosystem_stats()
    print(f"\nFinal ecosystem state:")
    print(f"  Total concepts: {final_stats['total_concepts']}")
    print(f"  Active concepts: {final_stats['active_concepts']}")
    print(f"  Conceptual diversity: {final_stats['conceptual_diversity']:.3f}")
    print(f"  Relations: {final_stats['relation_count']}")
    print(f"  Evolution events: {len(engine.evolution_log)}")

    # Show evolution summary
    print(f"\nEvolution Summary:")
    refinements = len([e for e in engine.evolution_log if e.operation.name == 'ASEXUAL_REFINEMENT'])
    syntheses = len([e for e in engine.evolution_log if e.operation.name == 'CROSS_SYNTHESIS'])

    print(f"  Concept refinements: {refinements}")
    print(f"  Cross-syntheses: {syntheses}")

    # Show some evolved concepts
    print(f"\nEvolved concepts (sample):")
    evolved_concepts = [c for c in engine.concepts.values() if c.generation > 0][:3]

    for concept in evolved_concepts:
        print(f"  {concept.label}")
        print(f"    Generation: {concept.generation}, Parents: {len(concept.lineage)}")
        print(f"    Definition: {concept.definition[:80]}...")
        print(f"    Support: {concept.support_strength:.3f}")

    # Export results
    output_file = "knowledge_evolution_results.json"
    print(f"\nExporting semantic knowledge evolution to {output_file}...")
    engine.export_knowledge_evolution(output_file)

    print(f"\nKnowledge Evolution Complete!")
    print("=" * 60)
    print(f"Concept growth: {initial_stats['active_concepts']} -> {final_stats['active_concepts']}")
    print(f"Diversity change: {initial_stats['conceptual_diversity']:.3f} -> {final_stats['conceptual_diversity']:.3f}")
    print(f"New concepts synthesized: {final_stats['total_concepts'] - initial_stats['active_concepts']}")

if __name__ == "__main__":
    main()