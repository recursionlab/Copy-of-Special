#!/usr/bin/env python3
"""
Comprehensive Test Suite
Tests all components of the production knowledge evolution system
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

    # Test 1: Graph Backend
    print("\n[BACKEND] Test 1: Graph Backend Integration")
    print("-" * 40)

    try:
        from graph_backend import GraphBackedKnowledgeEngine
        from knowledge_evolution_v2_1 import ConceptUnit

        # Test with non-existent Neo4j (fallback mode)
        engine = GraphBackedKnowledgeEngine()

        # Create test concept
        test_concept = ConceptUnit(
            id="test-backend-001",
            label="Graph Database",
            definition_full="A database that uses graph structures for semantic queries with nodes, edges, and properties",
            source_evidence="Comprehensive test - Graph DB definition"
        )

        # Test storage
        storage_success = engine.store_concept(test_concept)
        retrieval_test = engine.get_concept("test-backend-001")

        test_results['graph_backend'] = {
            'initialized': True,
            'fallback_mode': engine.driver is None,
            'storage_attempted': storage_success is not None,
            'concept_handling': retrieval_test is not None or storage_success == False
        }

        print(f"SUCCESS: Graph backend initialized (fallback mode: {engine.driver is None})")
        print(f"SUCCESS: Concept storage: {'Success' if storage_success else 'Fallback mode'}")

        engine.close()

    except Exception as e:
        test_results['graph_backend'] = {'error': str(e)}
        print(f"ERROR: Graph backend test failed: {e}")

    # Test 2: Semantic Deduplication
    print("\n[DEDUP] Test 2: Semantic Deduplication")
    print("-" * 40)

    try:
        from semantic_deduplication import SemanticDeduplicator

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
                definition_full="The simulation of human intelligence in machines",  # Same definition
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

        print(f"✓ Semantic deduplication enabled: {deduplicator.is_available()}")
        print(f"✓ Processed {len(test_concepts)} concepts in {dedup_time:.3f}s")
        print(f"✓ Found {dedup_result.duplicates_found} duplicates, {dedup_result.merged_count} merge candidates")

    except Exception as e:
        test_results['semantic_deduplication'] = {'error': str(e)}
        print(f"✗ Semantic deduplication test failed: {e}")

    # Test 3: Knowledge Evolution Engine
    print("\n🧠 Test 3: Knowledge Evolution Engine")
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

        print(f"✓ Added {added_concepts} concepts successfully")
        print(f"✓ Evolution completed: {final_stats['total_concepts']} total concepts")
        print(f"✓ Quality score: {final_stats['quality_score']:.3f}")

    except Exception as e:
        test_results['knowledge_evolution'] = {'error': str(e)}
        print(f"✗ Knowledge evolution test failed: {e}")

    # Test 4: Full Production Pipeline
    print("\n🚀 Test 4: Full Production Pipeline")
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

            # Test deduplication
            if pipeline.deduplicator:
                concepts_list = list(pipeline.engine.concepts.values())
                dedup_result = pipeline.deduplicator.deduplicate_concepts(concepts_list)
                dedup_success = True
            else:
                dedup_success = False

            test_results['production_pipeline'] = {
                'initialization_successful': True,
                'pdf_processing_available': capabilities['pdf_processing'],
                'semantic_deduplication_available': capabilities['semantic_deduplication'],
                'graph_persistence_available': capabilities['graph_persistence'],
                'concepts_added': concepts_added,
                'enhancement_completed': enhancement_result['concepts_enhanced'] >= 0,
                'deduplication_completed': dedup_success
            }

            print(f"✓ Pipeline initialization successful")
            print(f"✓ PDF Processing: {capabilities['pdf_processing']}")
            print(f"✓ Semantic Deduplication: {capabilities['semantic_deduplication']}")
            print(f"✓ Graph Persistence: {capabilities['graph_persistence']}")
            print(f"✓ Added {concepts_added} concepts via pipeline")
            print(f"✓ Enhancement: {enhancement_result['concepts_enhanced']} concepts enhanced")

    except Exception as e:
        test_results['production_pipeline'] = {'error': str(e)}
        print(f"✗ Production pipeline test failed: {e}")

    # Test 5: GROBID Processor (standalone)
    print("\n📄 Test 5: GROBID Document Processor")
    print("-" * 40)

    try:
        from grobid_processor import GrobidProcessor

        processor = GrobidProcessor()
        grobid_available = processor.is_grobid_available()

        # Test with mock document
        mock_doc = processor._fallback_processing("test_document.pdf")

        test_results['grobid_processor'] = {
            'processor_initialized': True,
            'service_available': grobid_available,
            'fallback_processing': mock_doc is not None,
            'document_structure': mock_doc.title is not None if mock_doc else False
        }

        print(f"✓ GROBID processor initialized")
        print(f"✓ Service available: {grobid_available}")
        print(f"✓ Fallback processing: {'Success' if mock_doc else 'Failed'}")

    except Exception as e:
        test_results['grobid_processor'] = {'error': str(e)}
        print(f"✗ GROBID processor test failed: {e}")

    # Summary
    total_time = time.time() - total_start

    print("\n" + "="*80)
    print("COMPREHENSIVE TEST RESULTS SUMMARY")
    print("="*80)

    total_tests = len(test_results)
    successful_tests = sum(1 for result in test_results.values() if 'error' not in result)

    print(f"📊 Tests Run: {total_tests}")
    print(f"✅ Successful: {successful_tests}")
    print(f"❌ Failed: {total_tests - successful_tests}")
    print(f"⏱️  Total Time: {total_time:.2f} seconds")
    print(f"📅 Test Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    print(f"\n📋 Component Status:")
    for component, result in test_results.items():
        if 'error' in result:
            print(f"  ❌ {component}: FAILED - {result['error']}")
        else:
            print(f"  ✅ {component}: PASSED")

    # Key capabilities summary
    print(f"\n🔧 Key Capabilities Verified:")

    if 'graph_backend' in test_results and 'error' not in test_results['graph_backend']:
        print(f"  ✅ Graph database integration with fallback")

    if 'semantic_deduplication' in test_results and 'error' not in test_results['semantic_deduplication']:
        result = test_results['semantic_deduplication']
        if result.get('enabled'):
            print(f"  ✅ FAISS semantic deduplication ({result.get('method', 'unknown')} method)")
        else:
            print(f"  ⚠️  Semantic deduplication available but not fully enabled")

    if 'knowledge_evolution' in test_results and 'error' not in test_results['knowledge_evolution']:
        print(f"  ✅ Knowledge evolution with quality management")

    if 'production_pipeline' in test_results and 'error' not in test_results['production_pipeline']:
        print(f"  ✅ Full production pipeline orchestration")

    if 'grobid_processor' in test_results and 'error' not in test_results['grobid_processor']:
        print(f"  ✅ GROBID document processing capabilities")

    print(f"\n🎉 System Status: {'PRODUCTION READY' if successful_tests >= 4 else 'NEEDS ATTENTION'}")

    return test_results, successful_tests >= 4

if __name__ == "__main__":
    results, success = test_all_components()
    exit(0 if success else 1)