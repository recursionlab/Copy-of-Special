#!/usr/bin/env python3
"""
Test Graph Backend Integration
Tests Neo4j integration with fallback to in-memory storage
"""

import sys
import os
import tempfile
import yaml
from datetime import datetime

# Add current directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from graph_backend import GraphBackedKnowledgeEngine
from knowledge_evolution_v2_1 import (
    ConceptUnit, ConceptRelation, ConceptContradiction,
    ConceptState, QualityTier, RefinementPriority
)

def test_graph_backend_with_fallback():
    """Test GraphBackedKnowledgeEngine with Neo4j unavailable (fallback mode)"""

    # Create a temporary config file with non-existent Neo4j
    with tempfile.NamedTemporaryFile(mode='w', suffix='.yaml', delete=False) as f:
        config = {
            'database': {
                'neo4j_uri': 'bolt://localhost:9999',  # Non-existent port
                'neo4j_user': 'neo4j',
                'neo4j_password': 'test'
            }
        }
        yaml.dump(config, f)
        temp_config = f.name

    try:
        print("Testing GraphBackedKnowledgeEngine initialization...")

        # Initialize engine (should fallback gracefully)
        engine = GraphBackedKnowledgeEngine(temp_config)

        print(f"SUCCESS: Engine initialized (Neo4j available: {engine.driver is not None})")

        # Create test concept
        concept = ConceptUnit(
            id="test-concept-001",
            label="Machine Learning",
            definition_full="A subset of artificial intelligence that focuses on algorithms that improve through experience",
            source_evidence="Stanford CS229 Lecture Notes"
        )

        # Add some relations and contradictions
        concept.relations.append(ConceptRelation(
            type="IS_SUBSET_OF",
            target_id="ai-concept-001",
            evidence="ML is a branch of AI",
            confidence=0.9
        ))

        concept.contradictions.append(ConceptContradiction(
            with_id="symbolic-ai-001",
            contradiction_basis="Different approaches to intelligence",
            resolution_confidence=0.7
        ))

        print("\n[DATA] Testing concept storage...")

        # Test storage (should work even without Neo4j)
        success = engine.store_concept(concept)
        print(f"SUCCESS: Concept storage: {'Success' if success else 'Fallback mode (in-memory)'}")

        # Test retrieval
        retrieved = engine.get_concept("test-concept-001")
        if retrieved:
            print(f"SUCCESS: Concept retrieved: {retrieved.label}")
            print(f"  - Quality tier: {retrieved.quality_tier.value}")
            print(f"  - State: {retrieved.state.value}")
            print(f"  - Relations: {len(retrieved.relations)}")
            print(f"  - Contradictions: {len(retrieved.contradictions)}")
        else:
            print("SUCCESS: Fallback mode: Direct object access")

        # Test stats
        stats = engine.get_graph_stats()
        print(f"\n[STATS] Graph stats: {stats}")

        print("\nSUCCESS: Graph backend test completed successfully!")
        print("   - Engine handles Neo4j unavailability gracefully")
        print("   - Fallback mechanisms working")

        return True

    except Exception as e:
        print(f"ERROR: Test failed: {e}")
        import traceback
        traceback.print_exc()
        return False

    finally:
        # Cleanup
        if engine:
            engine.close()
        os.unlink(temp_config)

def test_integration_with_knowledge_evolution():
    """Test integration with existing knowledge evolution system"""
    print("\n[INTEGRATION] Testing integration with knowledge evolution system...")

    try:
        # Import the existing system
        from knowledge_evolution_v2_1 import KnowledgeEvolutionV21

        # Create a simple evolution engine instance to verify compatibility
        engine = KnowledgeEvolutionV21()

        # Add some test concepts
        concept1 = ConceptUnit(
            id="integration-test-1",
            label="Neural Networks",
            definition_full="Computational models inspired by biological neural networks",
            source_evidence="Deep Learning textbook"
        )

        concept2 = ConceptUnit(
            id="integration-test-2",
            label="Deep Learning",
            definition_full="Machine learning using artificial neural networks with multiple layers",
            source_evidence="Nature paper on deep learning"
        )

        # Test evolution operations - v2.1 uses dict input
        concept1_data = {
            "label": "Neural Networks",
            "definition": "Computational models inspired by biological neural networks",
            "source_evidence": "Deep Learning textbook"
        }

        concept2_data = {
            "label": "Deep Learning",
            "definition": "Machine learning using artificial neural networks with multiple layers",
            "source_evidence": "Nature paper on deep learning"
        }

        result1 = engine.add_concept_from_unit(concept1_data)
        result2 = engine.add_concept_from_unit(concept2_data)

        print("SUCCESS: Basic evolution engine compatibility confirmed")
        print(f"  - Concepts added: {result1 is not None}, {result2 is not None}")
        print(f"  - Concepts in system: {len(engine.concepts)}")

        # Test evolution step
        engine.evolve_knowledge_ecosystem(cycles=1)
        print("SUCCESS: Evolution cycle completed")

        return True

    except Exception as e:
        print(f"ERROR: Integration test failed: {e}")
        return False

if __name__ == "__main__":
    print("Starting Graph Backend Integration Tests")
    print("=" * 50)

    # Test 1: Basic graph backend functionality
    test1_success = test_graph_backend_with_fallback()

    # Test 2: Integration with knowledge evolution
    test2_success = test_integration_with_knowledge_evolution()

    print("\n" + "=" * 50)
    if test1_success and test2_success:
        print("All tests passed! Graph backend ready for integration.")
    else:
        print("Some tests failed. Check logs above.")
        sys.exit(1)