#!/usr/bin/env python3
"""
Production Knowledge Evolution Engine
Integrates Neo4j backend with knowledge evolution v2.1
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

from graph_backend import GraphBackedKnowledgeEngine
from knowledge_evolution_v2_1 import (
    ConceptUnit, ConceptRelation, ConceptContradiction,
    ConceptState, QualityTier, RefinementPriority, RefinementType,
    EvolutionOperation, RefinementAttempt,
    QueuedRefinement, EvolutionEvent, KnowledgeEvolutionV21
)

class ProductionKnowledgeEngine(KnowledgeEvolutionV21):
    """Production-ready knowledge engine with Neo4j backend"""

    def __init__(self, config_path: str = "config.yaml", use_graph_backend: bool = True):
        """Initialize with optional graph backend"""
        super().__init__()

        # Initialize graph backend
        self.use_graph_backend = use_graph_backend
        self.graph_backend = None

        if use_graph_backend:
            try:
                self.graph_backend = GraphBackedKnowledgeEngine(config_path)
                print(f"Graph backend initialized (Neo4j available: {self.graph_backend.driver is not None})")
            except Exception as e:
                print(f"Failed to initialize graph backend: {e}")
                self.graph_backend = None

    def add_concept_from_unit(self, concept_data: dict) -> Optional[ConceptUnit]:
        """Enhanced concept addition with graph backend persistence"""
        # Use parent method to create concept
        concept = super().add_concept_from_unit(concept_data)

        if concept and self.graph_backend:
            # Persist to graph database
            success = self.graph_backend.store_concept(concept)
            if success:
                print(f"Concept {concept.id} persisted to graph database")
            else:
                print(f"Warning: Failed to persist concept {concept.id} to graph database")

        return concept

    def _create_offspring(self, parent1: ConceptUnit, parent2: Optional[ConceptUnit] = None) -> ConceptUnit:
        """Create offspring with graph backend persistence"""
        # Use parent method to create offspring
        offspring = super()._create_offspring(parent1, parent2)

        if offspring and self.graph_backend:
            # Persist offspring to graph database
            success = self.graph_backend.store_concept(offspring)
            if success:
                print(f"Offspring concept {offspring.id} persisted to graph database")

        return offspring

    def load_concepts_from_graph(self) -> int:
        """Load existing concepts from graph database"""
        if not self.graph_backend:
            return 0

        try:
            graph_concepts = self.graph_backend.get_all_concepts()
            loaded_count = 0

            for concept in graph_concepts:
                # Add to in-memory storage
                self.concepts[concept.id] = concept
                loaded_count += 1

            print(f"Loaded {loaded_count} concepts from graph database")
            return loaded_count

        except Exception as e:
            print(f"Failed to load concepts from graph: {e}")
            return 0

    def get_concept_by_id(self, concept_id: str) -> Optional[ConceptUnit]:
        """Get concept from memory or graph backend"""
        # First check in-memory storage
        if concept_id in self.concepts:
            return self.concepts[concept_id]

        # Fall back to graph backend
        if self.graph_backend:
            concept = self.graph_backend.get_concept(concept_id)
            if concept:
                # Cache in memory
                self.concepts[concept_id] = concept
                return concept

        return None

    def get_concepts_by_quality_tier(self, tier: QualityTier) -> List[ConceptUnit]:
        """Get concepts filtered by quality tier using graph backend when available"""
        if self.graph_backend:
            try:
                return self.graph_backend.get_concepts_by_quality_tier(tier)
            except Exception as e:
                print(f"Graph backend query failed: {e}")

        # Fallback to in-memory filtering
        return [c for c in self.concepts.values() if c.quality_tier == tier]

    def get_enhanced_ecosystem_stats(self) -> dict:
        """Enhanced ecosystem statistics using graph backend"""
        # Get basic stats from parent
        basic_stats = self.get_ecosystem_stats()

        # Add graph backend stats if available
        if self.graph_backend:
            try:
                graph_stats = self.graph_backend.get_graph_stats()
                basic_stats['graph_database'] = {
                    'connected': self.graph_backend.driver is not None,
                    'stats': graph_stats
                }
            except Exception as e:
                basic_stats['graph_database'] = {
                    'connected': False,
                    'error': str(e)
                }
        else:
            basic_stats['graph_database'] = {
                'connected': False,
                'backend': 'not_initialized'
            }

        return basic_stats

    def sync_to_graph(self) -> Dict[str, int]:
        """Sync all in-memory concepts to graph database"""
        if not self.graph_backend:
            return {'synced': 0, 'failed': 0, 'total': 0}

        synced = 0
        failed = 0
        total = len(self.concepts)

        for concept in self.concepts.values():
            try:
                if self.graph_backend.store_concept(concept):
                    synced += 1
                else:
                    failed += 1
            except Exception as e:
                print(f"Failed to sync concept {concept.id}: {e}")
                failed += 1

        return {
            'synced': synced,
            'failed': failed,
            'total': total
        }

    def export_production_results(self, output_path: str) -> dict:
        """Enhanced export with graph backend information"""
        # Get basic export from parent
        result = self.export_knowledge_evolution_v2_1(f"{output_path}.json")

        # Add production metadata
        enhanced_stats = self.get_enhanced_ecosystem_stats()
        production_metadata = {
            'export_timestamp': datetime.now().isoformat(),
            'engine_type': 'ProductionKnowledgeEngine',
            'graph_backend_enabled': self.use_graph_backend,
            'graph_backend_connected': self.graph_backend.driver is not None if self.graph_backend else False,
            'ecosystem_stats': enhanced_stats,
            'total_concepts': len(self.concepts),
            'quality_distribution': {
                tier.value: len(self.get_concepts_by_quality_tier(tier))
                for tier in QualityTier
            }
        }

        # Write production metadata
        metadata_path = f"{output_path}_production_metadata.json"
        with open(metadata_path, 'w', encoding='utf-8') as f:
            json.dump(production_metadata, f, indent=2, ensure_ascii=False)

        print(f"Production results exported to {output_path}.json")
        print(f"Production metadata exported to {metadata_path}")

        return {
            'main_export': result,
            'production_metadata': production_metadata,
            'files_created': [f"{output_path}.json", metadata_path]
        }

    def close(self):
        """Clean shutdown of graph backend"""
        if self.graph_backend:
            self.graph_backend.close()
            print("Graph backend connection closed")

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()


def demo_production_engine():
    """Demonstrate production engine capabilities"""
    print("=== Production Knowledge Engine Demo ===")

    # Initialize engine
    with ProductionKnowledgeEngine() as engine:

        # Add some test concepts
        concepts_data = [
            {
                "label": "Machine Learning",
                "definition": "A subset of artificial intelligence that enables computers to learn and make decisions from data without being explicitly programmed for every task",
                "source_evidence": "Stanford CS229 Machine Learning Course"
            },
            {
                "label": "Deep Learning",
                "definition": "A subset of machine learning that uses artificial neural networks with multiple layers to model and understand complex patterns in data",
                "source_evidence": "Nature Deep Learning Review Paper"
            },
            {
                "label": "Neural Networks",
                "definition": "Computational models inspired by biological neural networks that consist of interconnected nodes (neurons) that process and transmit information",
                "source_evidence": "MIT Neural Networks and Deep Learning Textbook"
            }
        ]

        print(f"Adding {len(concepts_data)} test concepts...")
        for concept_data in concepts_data:
            result = engine.add_concept_from_unit(concept_data)
            if result:
                print(f"  Added: {result.label} (ID: {result.id})")
            else:
                print(f"  Failed to add: {concept_data['label']}")

        # Run evolution cycles
        print("\nRunning evolution cycles...")
        engine.evolve_knowledge_ecosystem(cycles=2)

        # Get enhanced stats
        stats = engine.get_enhanced_ecosystem_stats()
        print(f"\nEcosystem Stats:")
        print(f"  Total concepts: {stats['total_concepts']}")
        print(f"  Active concepts: {stats['active_concepts']}")
        print(f"  High quality: {stats['high_quality_concepts']}")
        print(f"  Mid quality: {stats['mid_quality_concepts']}")
        print(f"  Graph backend: {stats.get('graph_database', {}).get('connected', False)}")

        # Export results
        results = engine.export_production_results("demo_production_results")
        print(f"\nExported results: {len(results['files_created'])} files created")

if __name__ == "__main__":
    demo_production_engine()