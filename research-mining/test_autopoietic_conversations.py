#!/usr/bin/env python3
"""
Test the updated autopoietic engine on conversation data
"""

import json
import sys
import os
from pathlib import Path

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from quantum_knowledge.autopoietic_engine import AutopoieticEngine

def load_conversation_concepts(file_path):
    """Load concept units from conversation export"""
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def create_organisms_from_concepts(engine, concepts, max_concepts=20):
    """Create organisms from concept units"""
    print(f"Creating organisms from first {max_concepts} concepts...")

    organisms = {}
    for i, concept in enumerate(concepts[:max_concepts]):
        concept_id = concept.get('id', f'concept-{i}')

        # Use concept type and definition to create genetic code
        concept_type = concept.get('type', 'unknown')
        definition = concept.get('definition', 'no definition')

        # Create genetic code from concept characteristics
        genetic_code = f"{concept_type}-{len(definition)}-{hash(definition) % 1000}"

        # Initial energy based on confidence score if available
        initial_energy = concept.get('confidence_score', 0.7) * 200 + 50  # 50-190 range

        organism = engine.create_organism(
            concept_id=concept_id,
            initial_energy=initial_energy,
            genetic_code=genetic_code
        )

        organisms[concept_id] = {
            'organism': organism,
            'original_concept': concept
        }

        print(f"  Created {concept_id}: energy={initial_energy:.1f}, genetic_code={genetic_code}")

    return organisms

def run_ecosystem_evolution(engine, cycles=10):
    """Run ecosystem evolution and track changes"""
    print(f"\nRunning ecosystem evolution for {cycles} cycles...")

    initial_stats = {
        'population': len(engine.organisms),
        'diversity': engine.calculate_diversity_index(),
        'total_energy': engine.total_ecosystem_energy()
    }

    print(f"Initial state:")
    print(f"  Population: {initial_stats['population']}")
    print(f"  Diversity: {initial_stats['diversity']:.3f}")
    print(f"  Total energy: {initial_stats['total_energy']:.1f}")

    # Evolution cycles
    for cycle in range(cycles):
        engine.evolve_ecosystem(time_step=1.0)

        if cycle % 3 == 0:  # Report every 3 cycles
            active_count = len([org for org in engine.organisms.values()
                              if org.state.name == 'ACTIVE'])
            diversity = engine.calculate_diversity_index()
            energy = engine.total_ecosystem_energy()

            print(f"  Cycle {cycle+1}: active={active_count}, diversity={diversity:.3f}, energy={energy:.1f}")

    # Final stats
    final_stats = {
        'population': len([org for org in engine.organisms.values() if org.state.name == 'ACTIVE']),
        'diversity': engine.calculate_diversity_index(),
        'total_energy': engine.total_ecosystem_energy(),
        'total_organisms': len(engine.organisms),
        'reproductions': len(engine.reproduction_log)
    }

    print(f"\nFinal state:")
    print(f"  Active population: {final_stats['population']}")
    print(f"  Total organisms created: {final_stats['total_organisms']}")
    print(f"  Diversity: {final_stats['diversity']:.3f}")
    print(f"  Total energy: {final_stats['total_energy']:.1f}")
    print(f"  Reproduction events: {final_stats['reproductions']}")

    return initial_stats, final_stats

def analyze_reproduction_events(engine):
    """Analyze reproduction patterns"""
    print(f"\nReproduction Analysis:")

    if not engine.reproduction_log:
        print("  No reproduction events occurred")
        return

    asexual_count = len([r for r in engine.reproduction_log if r.reproduction_mode.name == 'ASEXUAL'])
    sexual_count = len([r for r in engine.reproduction_log if r.reproduction_mode.name == 'SEXUAL'])

    print(f"  Asexual reproductions: {asexual_count}")
    print(f"  Sexual reproductions: {sexual_count}")

    # Show some recent reproduction events
    print(f"\n  Recent reproduction events:")
    for i, event in enumerate(engine.reproduction_log[-3:], 1):
        print(f"    {i}. {event.reproduction_mode.name}: {len(event.parent_ids)} parent(s) -> {event.offspring_id}")
        print(f"       Energy cost: {event.energy_cost:.1f}, Success: {event.success}")

def export_results(engine, organisms, output_path="autopoietic_results.json"):
    """Export ecosystem results"""
    print(f"\nExporting results to {output_path}...")

    results = {
        'ecosystem_stats': {
            'total_organisms': len(engine.organisms),
            'active_organisms': len([org for org in engine.organisms.values() if org.state.name == 'ACTIVE']),
            'diversity_index': engine.calculate_diversity_index(),
            'total_energy': engine.total_ecosystem_energy(),
            'total_reproductions': len(engine.reproduction_log)
        },
        'organisms': [],
        'reproduction_log': []
    }

    # Export organism data
    for org_id, org in engine.organisms.items():
        org_data = {
            'id': org_id,
            'concept_id': org.concept_id,
            'energy': org.energy,
            'genetic_code': org.genetic_code,
            'generation': org.generation,
            'age': org.age,
            'state': org.state.name,
            'reproduction_count': org.reproduction_count,
            'parent_ids': org.parent_ids,
            'offspring_ids': org.offspring_ids,
            'birth_timestamp': org.birth_timestamp
        }

        # Add original concept if available
        if org_id in organisms:
            org_data['original_concept'] = organisms[org_id]['original_concept']

        results['organisms'].append(org_data)

    # Export reproduction events
    for event in engine.reproduction_log:
        event_data = {
            'parent_ids': event.parent_ids,
            'offspring_id': event.offspring_id,
            'reproduction_mode': event.reproduction_mode.name,
            'energy_cost': event.energy_cost,
            'genetic_mutations': event.genetic_mutations,
            'success': event.success,
            'timestamp': event.timestamp
        }
        results['reproduction_log'].append(event_data)

    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

    print(f"  Results exported: {len(results['organisms'])} organisms, {len(results['reproduction_log'])} reproductions")

def main():
    print("Testing Updated Autopoietic Engine on Conversation Data")
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

    # Initialize autopoietic engine
    print(f"\nInitializing autopoietic engine...")
    engine = AutopoieticEngine()

    # Create organisms from concepts
    organisms = create_organisms_from_concepts(engine, concepts, max_concepts=30)
    print(f"  Created {len(organisms)} initial organisms")

    # Run evolution
    initial_stats, final_stats = run_ecosystem_evolution(engine, cycles=15)

    # Analyze results
    analyze_reproduction_events(engine)

    # Export results
    export_results(engine, organisms, "autopoietic_conversation_results.json")

    print("\nAutopoietic Analysis Complete!")
    print("=" * 60)
    print(f"Population change: {initial_stats['population']} -> {final_stats['population']}")
    print(f"Diversity change: {initial_stats['diversity']:.3f} -> {final_stats['diversity']:.3f}")
    print(f"Energy change: {initial_stats['total_energy']:.1f} -> {final_stats['total_energy']:.1f}")
    print(f"New organisms created: {final_stats['total_organisms'] - initial_stats['population']}")

if __name__ == "__main__":
    main()