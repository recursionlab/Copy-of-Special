#!/usr/bin/env python3
"""
Test Projects Research System - Corpus Orchestrator
"""

import sys
import os
from pathlib import Path

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from projects_research_system import ProjectsResearchSystem

def main():
    print("Testing Projects Research System - Corpus Orchestrator")
    print("=" * 60)

    # Check if projects directory exists (create demo if not)
    projects_path = Path("projects")
    if not projects_path.exists():
        print(f"Creating demo projects directory: {projects_path}")
        create_demo_projects(projects_path)

    # Initialize research system
    print(f"Initializing Projects Research System...")
    research_system = ProjectsResearchSystem(str(projects_path))

    # Run complete research cycle
    print(f"\n🔬 Running Research Cycle...")
    stats = research_system.run_research_cycle()

    print(f"\n📊 Research Cycle Results:")
    print(f"  Cycle number: {stats['cycle']}")
    print(f"  Concepts extracted: {stats['concepts_extracted']}")
    print(f"  Semantic clusters: {stats['clusters_formed']}")
    print(f"  Relationships mapped: {stats['relationships_mapped']}")
    print(f"  Gaps detected: {stats['gaps_detected']}")
    print(f"  File types: {stats['file_types_processed']}")

    # Show some extracted concepts
    print(f"\n🧠 Sample Extracted Concepts:")
    concept_sample = list(research_system.concept_units.values())[:3]
    for i, concept in enumerate(concept_sample, 1):
        print(f"  {i}. {concept.term}")
        print(f"     Definition: {concept.definition[:60]}...")
        print(f"     Source: {Path(concept.source_file).name}:{concept.page_section}")
        print(f"     Confidence: {concept.extraction_confidence:.3f}")
        print(f"     Tags: {concept.domain_tags}")

    # Show semantic clusters
    print(f"\n🏷️  Semantic Clusters:")
    for i, cluster in enumerate(list(research_system.semantic_clusters.values())[:3], 1):
        print(f"  {i}. {cluster.cluster_label}")
        print(f"     Members: {len(cluster.members)} concepts")
        print(f"     Strength: {cluster.cluster_strength:.3f}")
        print(f"     Rationale: {cluster.rationale[:60]}...")

    # Show relationship edges
    print(f"\n🕸️  Relationship Edges:")
    for i, edge in enumerate(list(research_system.relationship_edges.values())[:3], 1):
        source_term = research_system.concept_units[edge.source_concept].term
        target_term = research_system.concept_units[edge.target_concept].term
        print(f"  {i}. {source_term} --{edge.relation_type}--> {target_term}")
        print(f"     Evidence: {edge.evidence[:50]}...")
        print(f"     Confidence: {edge.confidence:.3f}")

    # Show gaps and contradictions
    print(f"\n🔍 Gaps and Contradictions:")
    for i, gap in enumerate(list(research_system.gap_units.values())[:3], 1):
        print(f"  {i}. {gap.gap_type.value}: {gap.gap_description[:60]}...")
        print(f"     Priority: {gap.resolution_priority.value}")
        print(f"     Location: {gap.evidence_location}")

    # Show next steps
    print(f"\n📋 Next Refinement Steps:")
    for i, step in enumerate(stats['next_steps'], 1):
        print(f"  {i}. {step}")

    # Export complete results
    output_file = "projects_research_results.json"
    print(f"\n💾 Exporting complete research results to {output_file}...")
    research_system.export_research_results(output_file)

    print(f"\n✅ Projects Research System Complete!")
    print("=" * 60)
    print("Research Cathedral Status:")
    print(f"  📁 Files processed: {len(set(c.source_file for c in research_system.concept_units.values()))}")
    print(f"  🧠 Knowledge units: {len(research_system.concept_units)}")
    print(f"  🏷️  Semantic neighborhoods: {len(research_system.semantic_clusters)}")
    print(f"  🕸️  Relationship network: {len(research_system.relationship_edges)} edges")
    print(f"  🔍 Gaps identified: {len(research_system.gap_units)}")
    print(f"  🔄 Recursive documentation: {len(research_system.method_notes)} cycles")

def create_demo_projects(projects_path: Path):
    """Create demo projects directory with sample files"""
    projects_path.mkdir(exist_ok=True)

    # Demo markdown file
    demo_md = projects_path / "demo_concepts.md"
    demo_md.write_text("""
# Fundamental Concepts

## Consciousness
Consciousness is the subjective experience of being aware and having phenomenal states.
It involves the integration of sensory information with memory and cognitive processes.

## Recursion
Recursion is a computational process where a function calls itself with modified parameters.
In cognitive science, recursion enables infinite generative capacity from finite rules.

## Emergence
Emergence refers to properties that arise from complex interactions but cannot be reduced
to the properties of individual components. Consciousness emerges from neural networks.

## Information Theory
Information Theory quantifies the transmission and processing of information using mathematical frameworks.
It provides the foundation for understanding communication systems and computational processes.
""", encoding='utf-8')

    # Demo JSON file
    demo_json = projects_path / "extracted_data.json"
    demo_json.write_text("""
{
  "concepts": [
    {
      "term": "Autopoiesis",
      "definition": "Self-creating and self-maintaining systems that reproduce their own components while maintaining structural integrity.",
      "domain": "systems_theory"
    },
    {
      "term": "Cognitive Load",
      "definition": "The amount of mental effort used in working memory during learning and problem-solving tasks.",
      "domain": "psychology"
    }
  ]
}
""", encoding='utf-8')

    # Demo text file
    demo_txt = projects_path / "research_notes.txt"
    demo_txt.write_text("""
Research Notes on Complex Systems

Complex Systems exhibit nonlinear behavior where small changes can have large effects.
These systems are characterized by emergence, self-organization, and adaptive behavior.

Feedback Loops are essential components that create stability or instability in complex systems.
Positive feedback amplifies changes while negative feedback maintains equilibrium.

Networks in complex systems show small-world properties with high clustering and short path lengths.
Scale-free networks have power-law degree distributions with highly connected hubs.
""", encoding='utf-8')

    print(f"  Created demo files in {projects_path}")

if __name__ == "__main__":
    main()