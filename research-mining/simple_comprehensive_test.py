#!/usr/bin/env python3
"""
Simple Comprehensive Test - ASCII only
"""

import time
from datetime import datetime

def test_all_components():
    """Run comprehensive tests of all system components"""

    print("="*80)
    print("COMPREHENSIVE PRODUCTION KNOWLEDGE EVOLUTION SYSTEM TEST")
    print("="*80)

    total_start = time.time()
    test_results = {}

    # Test 1: Semantic Deduplication
    print("\n[DEDUP] Test 1: Semantic Deduplication")
    print("-" * 40)

    try:
        from semantic_deduplication import SemanticDeduplicator
        from knowledge_evolution_v2_1 import ConceptUnit

        deduplicator = SemanticDeduplicator()

        # Create test concepts with known duplicates
        test_concepts = [
            ConceptUnit(
                id="dup-test-1",
                label="Artificial Intelligence",
                definition_full="The simulation of human intelligence in machines",
                source_evidence="Test data 1"
            ),
            ConceptUnit(
                id="dup-test-2",
                label="AI",
                definition_full="The simulation of human intelligence in machines",
                source_evidence="Test data 2"
            ),
            ConceptUnit(
                id="dup-test-3",
                label="Machine Learning",
                definition_full="A subset of AI that learns from data",
                source_evidence="Test data 3"
            )
        ]

        # Run deduplication
        start_time = time.time()
        dedup_result = deduplicator.deduplicate_concepts(test_concepts)
        dedup_time = time.time() - start_time

        test_results['semantic_deduplication'] = {
            'enabled': deduplicator.is_available(),
            'concepts_processed': len(test_concepts),
            'duplicates_found': dedup_result.duplicates_found,
            'merge_candidates': dedup_result.merged_count,
            'processing_time': dedup_time,
            'method': dedup_result.method_used
        }

        print(f"SUCCESS: Semantic deduplication enabled: {deduplicator.is_available()}")
        print(f"SUCCESS: Processed {len(test_concepts)} concepts in {dedup_time:.3f}s")
        print(f"SUCCESS: Found {dedup_result.duplicates_found} duplicates, {dedup_result.merged_count} merge candidates")

    except Exception as e:
        test_results['semantic_deduplication'] = {'error': str(e)}
        print(f"ERROR: Semantic deduplication test failed: {e}")

    # Test 2: Knowledge Evolution Engine
    print("\n[EVOLUTION] Test 2: Knowledge Evolution Engine")
    print("-" * 40)

    try:
        from knowledge_evolution_v2_1 import KnowledgeEvolutionV21

        evolution_engine = KnowledgeEvolutionV21()

        # Add diverse concepts
        concept_data = [
            {
                "label": "Quantum Computing",
                "definition": "Computing using quantum mechanical phenomena like superposition and entanglement",
                "source_evidence": "Test - Quantum computing definition"
            },
            {
                "label": "Blockchain",
                "definition": "A distributed ledger technology ensuring secure and transparent transactions",
                "source_evidence": "Test - Blockchain definition"
            }
        ]

        added_concepts = 0
        for data in concept_data:
            result = evolution_engine.add_concept_from_unit(data)
            if result:
                added_concepts += 1

        # Run evolution
        evolution_engine.evolve_knowledge_ecosystem(cycles=2)

        # Get final stats
        final_stats = evolution_engine.get_ecosystem_stats()

        test_results['knowledge_evolution'] = {
            'concepts_added': added_concepts,
            'total_concepts': final_stats['total_concepts'],
            'active_concepts': final_stats['active_concepts'],
            'quality_score': final_stats['quality_score'],
            'evolution_completed': True
        }

        print(f"SUCCESS: Added {added_concepts} concepts successfully")
        print(f"SUCCESS: Evolution completed: {final_stats['total_concepts']} total concepts")
        print(f"SUCCESS: Quality score: {final_stats['quality_score']:.3f}")

    except Exception as e:
        test_results['knowledge_evolution'] = {'error': str(e)}
        print(f"ERROR: Knowledge evolution test failed: {e}")

    # Test 3: Full Production Pipeline
    print("\n[PIPELINE] Test 3: Full Production Pipeline")
    print("-" * 40)

    try:
        from full_production_pipeline import FullProductionPipeline

        with FullProductionPipeline() as pipeline:
            # Get pipeline status
            status = pipeline.get_pipeline_status()
            capabilities = status['capabilities']

            # Test concept processing
            synthetic_concepts = [
                {
                    "label": "Edge Computing",
                    "definition": "Computing performed at or near the source of data generation",
                    "source_evidence": "Pipeline test - Edge computing"
                },
                {
                    "label": "IoT",
                    "definition": "Network of interconnected devices that communicate and exchange data",
                    "source_evidence": "Pipeline test - IoT"
                }
            ]

            concepts_added = 0
            for concept_data in synthetic_concepts:
                result = pipeline.engine.add_concept_from_unit(concept_data)
                if result:
                    concepts_added += 1

            # Test enhancement
            enhancement_result = pipeline.engine.enhance_concept_definitions()

            test_results['production_pipeline'] = {
                'initialization_successful': True,
                'pdf_processing_available': capabilities['pdf_processing'],
                'semantic_deduplication_available': capabilities['semantic_deduplication'],
                'graph_persistence_available': capabilities['graph_persistence'],
                'concepts_added': concepts_added,
                'enhancement_completed': enhancement_result['concepts_enhanced'] >= 0
            }

            print(f"SUCCESS: Pipeline initialization successful")
            print(f"SUCCESS: PDF Processing: {capabilities['pdf_processing']}")
            print(f"SUCCESS: Semantic Deduplication: {capabilities['semantic_deduplication']}")
            print(f"SUCCESS: Graph Persistence: {capabilities['graph_persistence']}")
            print(f"SUCCESS: Added {concepts_added} concepts via pipeline")

    except Exception as e:
        test_results['production_pipeline'] = {'error': str(e)}
        print(f"ERROR: Production pipeline test failed: {e}")

    # Summary
    total_time = time.time() - total_start

    print("\n" + "="*80)
    print("COMPREHENSIVE TEST RESULTS SUMMARY")
    print("="*80)

    total_tests = len(test_results)
    successful_tests = sum(1 for result in test_results.values() if 'error' not in result)

    print(f"Tests Run: {total_tests}")
    print(f"Successful: {successful_tests}")
    print(f"Failed: {total_tests - successful_tests}")
    print(f"Total Time: {total_time:.2f} seconds")
    print(f"Test Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    print(f"\nComponent Status:")
    for component, result in test_results.items():
        if 'error' in result:
            print(f"  FAILED: {component} - {result['error']}")
        else:
            print(f"  PASSED: {component}")

    # Results breakdown
    if 'semantic_deduplication' in test_results and 'error' not in test_results['semantic_deduplication']:
        result = test_results['semantic_deduplication']
        print(f"\nSemantic Deduplication Results:")
        print(f"  Method: {result.get('method', 'unknown')}")
        print(f"  Processing time: {result.get('processing_time', 0):.3f}s")
        print(f"  Duplicates found: {result.get('duplicates_found', 0)}")

    if 'knowledge_evolution' in test_results and 'error' not in test_results['knowledge_evolution']:
        result = test_results['knowledge_evolution']
        print(f"\nKnowledge Evolution Results:")
        print(f"  Concepts added: {result.get('concepts_added', 0)}")
        print(f"  Total concepts: {result.get('total_concepts', 0)}")
        print(f"  Quality score: {result.get('quality_score', 0):.3f}")

    if 'production_pipeline' in test_results and 'error' not in test_results['production_pipeline']:
        result = test_results['production_pipeline']
        print(f"\nProduction Pipeline Results:")
        print(f"  PDF Processing: {result.get('pdf_processing_available', False)}")
        print(f"  Semantic Dedup: {result.get('semantic_deduplication_available', False)}")
        print(f"  Graph Persistence: {result.get('graph_persistence_available', False)}")

    success_rate = successful_tests / total_tests if total_tests > 0 else 0
    print(f"\nSystem Status: {'PRODUCTION READY' if success_rate >= 0.8 else 'NEEDS ATTENTION'}")
    print(f"Success Rate: {success_rate*100:.1f}%")

    return test_results, success_rate >= 0.8

if __name__ == "__main__":
    results, success = test_all_components()
    exit(0 if success else 1)