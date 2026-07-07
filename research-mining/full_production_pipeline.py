#!/usr/bin/env python3
"""
Full Production Knowledge Evolution Pipeline
Integrates all components: Neo4j + GROBID + LLM + FAISS + Evolution
"""

import os
import json
from typing import Dict, List, Optional, Any
from datetime import datetime
from pathlib import Path

from enhanced_production_engine import EnhancedProductionEngine
from semantic_deduplication import SemanticDeduplicator
from knowledge_evolution_v2_1 import ConceptUnit, QualityTier

class FullProductionPipeline:
    """Complete production pipeline integrating all knowledge evolution components"""

    def __init__(self, config_path: str = "config.yaml",
                 enable_neo4j: bool = True,
                 enable_grobid: bool = True,
                 enable_faiss: bool = True):
        """Initialize full production pipeline"""

        print("=== Initializing Full Production Knowledge Evolution Pipeline ===")

        # Initialize enhanced engine
        self.engine = EnhancedProductionEngine(
            config_path=config_path,
            use_graph_backend=enable_neo4j,
            use_grobid=enable_grobid
        )

        # Initialize semantic deduplicator
        self.deduplicator = None
        if enable_faiss:
            try:
                self.deduplicator = SemanticDeduplicator()
                print(f"Semantic deduplication enabled: {self.deduplicator.is_available()}")
            except Exception as e:
                print(f"Failed to initialize semantic deduplicator: {e}")

        # Pipeline state
        self.pipeline_stats = {
            'initialization_time': datetime.now().isoformat(),
            'components_enabled': {
                'neo4j_backend': enable_neo4j,
                'grobid_processor': enable_grobid,
                'faiss_deduplication': enable_faiss and self.deduplicator is not None,
                'llm_enhancement': True  # Always available (placeholder)
            },
            'components_status': {
                'neo4j_connected': False,
                'grobid_service': False,
                'faiss_available': False,
                'transformers_available': False
            }
        }

        self._check_component_status()

    def _check_component_status(self):
        """Check status of all pipeline components"""
        # Check Neo4j
        if self.engine.graph_backend:
            self.pipeline_stats['components_status']['neo4j_connected'] = (
                self.engine.graph_backend.driver is not None
            )

        # Check GROBID
        if self.engine.grobid_processor:
            self.pipeline_stats['components_status']['grobid_service'] = (
                self.engine.grobid_processor.is_grobid_available()
            )

        # Check FAISS and Transformers
        if self.deduplicator:
            self.pipeline_stats['components_status']['faiss_available'] = (
                self.deduplicator.is_available()
            )
            from semantic_deduplication import TRANSFORMERS_AVAILABLE
            self.pipeline_stats['components_status']['transformers_available'] = TRANSFORMERS_AVAILABLE

    def process_document_collection(self, pdf_directory: str,
                                   max_documents: int = 10,
                                   deduplicate_after_processing: bool = True,
                                   run_evolution_cycles: int = 3) -> Dict[str, Any]:
        """Process a collection of PDF documents through the full pipeline"""

        print(f"\n=== Processing Document Collection ===")
        print(f"Source directory: {pdf_directory}")
        print(f"Max documents: {max_documents}")

        pipeline_start = datetime.now()
        results = {
            'pipeline_start': pipeline_start.isoformat(),
            'input_directory': pdf_directory,
            'max_documents': max_documents,
            'stages': {}
        }

        # Stage 1: Document Processing with GROBID
        print(f"\n--- Stage 1: Document Processing ---")
        if os.path.exists(pdf_directory):
            batch_result = self.engine.process_pdf_batch(
                pdf_directory=pdf_directory,
                max_files=max_documents
            )

            results['stages']['document_processing'] = {
                'completed': True,
                'result': batch_result,
                'timestamp': datetime.now().isoformat()
            }

            if 'error' not in batch_result:
                print(f"SUCCESS: Processed {len(batch_result['processed_files'])} documents")
                print(f"SUCCESS: Added {batch_result['total_concepts_added']} concepts")
            else:
                print(f"ERROR: Document processing failed: {batch_result['error']}")
        else:
            print(f"ERROR: Directory not found: {pdf_directory}")
            results['stages']['document_processing'] = {
                'completed': False,
                'error': f"Directory not found: {pdf_directory}",
                'timestamp': datetime.now().isoformat()
            }

        # Stage 2: Concept Enhancement
        print(f"\n--- Stage 2: Concept Enhancement ---")
        enhancement_result = self.engine.enhance_concept_definitions()
        results['stages']['concept_enhancement'] = {
            'completed': True,
            'result': enhancement_result,
            'timestamp': datetime.now().isoformat()
        }
        print(f"SUCCESS: Enhanced {enhancement_result['concepts_enhanced']} concepts")

        # Stage 3: Semantic Deduplication
        print(f"\n--- Stage 3: Semantic Deduplication ---")
        if deduplicate_after_processing and self.deduplicator:
            concepts_list = list(self.engine.concepts.values())
            dedup_result = self.deduplicator.deduplicate_concepts(concepts_list)

            # Export deduplication report
            dedup_report = self.deduplicator.export_deduplication_report(
                dedup_result, self.engine.concepts, "pipeline_deduplication_report.json"
            )

            results['stages']['deduplication'] = {
                'completed': True,
                'result': {
                    'duplicates_found': dedup_result.duplicates_found,
                    'merge_candidates': dedup_result.merged_count,
                    'processing_time': dedup_result.processing_time,
                    'method_used': dedup_result.method_used
                },
                'report_file': "pipeline_deduplication_report.json",
                'timestamp': datetime.now().isoformat()
            }
            print(f"SUCCESS: Found {dedup_result.duplicates_found} potential duplicates")
            print(f"SUCCESS: Identified {dedup_result.merged_count} merge candidates")
        else:
            print("WARNING: Semantic deduplication skipped (not available or disabled)")
            results['stages']['deduplication'] = {
                'completed': False,
                'reason': 'not_available_or_disabled',
                'timestamp': datetime.now().isoformat()
            }

        # Stage 4: Knowledge Evolution
        print(f"\n--- Stage 4: Knowledge Evolution ---")
        if run_evolution_cycles > 0:
            print(f"Running {run_evolution_cycles} evolution cycles...")
            self.engine.evolve_knowledge_ecosystem(cycles=run_evolution_cycles)

            final_stats = self.engine.get_processing_summary()
            results['stages']['evolution'] = {
                'completed': True,
                'cycles_run': run_evolution_cycles,
                'final_stats': final_stats,
                'timestamp': datetime.now().isoformat()
            }
            print(f"SUCCESS: Completed {run_evolution_cycles} evolution cycles")
            print(f"SUCCESS: Final concept count: {final_stats['ecosystem_stats']['total_concepts']}")
        else:
            print("WARNING: Evolution cycles skipped (disabled)")
            results['stages']['evolution'] = {
                'completed': False,
                'reason': 'disabled',
                'timestamp': datetime.now().isoformat()
            }

        # Stage 5: Export Results
        print(f"\n--- Stage 5: Export Results ---")
        export_result = self.engine.export_production_results("full_pipeline_results")

        results['stages']['export'] = {
            'completed': True,
            'files_created': export_result['files_created'],
            'timestamp': datetime.now().isoformat()
        }
        print(f"SUCCESS: Exported results to {len(export_result['files_created'])} files")

        # Pipeline completion
        pipeline_end = datetime.now()
        total_time = (pipeline_end - pipeline_start).total_seconds()

        results['pipeline_end'] = pipeline_end.isoformat()
        results['total_processing_time'] = total_time
        results['component_status'] = self.pipeline_stats['components_status']

        print(f"\n=== Pipeline Completed ===")
        print(f"Total processing time: {total_time:.2f} seconds")

        return results

    def run_minimal_demo(self) -> Dict[str, Any]:
        """Run a minimal demonstration of the pipeline with synthetic data"""

        print(f"\n=== Running Minimal Pipeline Demo ===")

        # Add synthetic concepts
        synthetic_concepts = [
            {
                "label": "Artificial Intelligence",
                "definition": "The simulation of human intelligence processes by machines, especially computer systems",
                "source_evidence": "Synthetic demo data - AI definition"
            },
            {
                "label": "Machine Learning",
                "definition": "A subset of artificial intelligence that provides systems the ability to automatically learn and improve from experience",
                "source_evidence": "Synthetic demo data - ML definition"
            },
            {
                "label": "Deep Learning",
                "definition": "A subset of machine learning that uses neural networks with multiple layers to model and understand complex patterns",
                "source_evidence": "Synthetic demo data - DL definition"
            },
            {
                "label": "AI",  # Similar to first concept
                "definition": "The simulation of human intelligence processes by machines and computer systems",
                "source_evidence": "Synthetic demo data - AI acronym"
            },
            {
                "label": "Neural Networks",
                "definition": "Computing systems inspired by biological neural networks that constitute animal brains",
                "source_evidence": "Synthetic demo data - NN definition"
            }
        ]

        print(f"Adding {len(synthetic_concepts)} synthetic concepts...")
        for concept_data in synthetic_concepts:
            result = self.engine.add_concept_from_unit(concept_data)
            if result:
                print(f"  SUCCESS: Added: {result.label}")

        # Run deduplication
        if self.deduplicator:
            print(f"\nRunning semantic deduplication...")
            concepts_list = list(self.engine.concepts.values())
            dedup_result = self.deduplicator.deduplicate_concepts(concepts_list)
            print(f"  SUCCESS: Found {dedup_result.duplicates_found} potential duplicates")

        # Run evolution
        print(f"\nRunning knowledge evolution...")
        self.engine.evolve_knowledge_ecosystem(cycles=2)

        # Get final summary
        final_summary = self.engine.get_processing_summary()
        print(f"\nFinal Results:")
        print(f"  Total concepts: {final_summary['ecosystem_stats']['total_concepts']}")
        print(f"  Active concepts: {final_summary['ecosystem_stats']['active_concepts']}")
        print(f"  Quality distribution:")
        for tier in QualityTier:
            count = len(self.engine.get_concepts_by_quality_tier(tier))
            print(f"    {tier.value}: {count}")

        # Export minimal results
        export_result = self.engine.export_production_results("minimal_demo_results")
        print(f"\nSUCCESS: Results exported to {len(export_result['files_created'])} files")

        return {
            'synthetic_concepts_added': len(synthetic_concepts),
            'final_summary': final_summary,
            'deduplication_results': dedup_result.__dict__ if self.deduplicator else None,
            'export_files': export_result['files_created']
        }

    def get_pipeline_status(self) -> Dict[str, Any]:
        """Get comprehensive pipeline status"""
        current_summary = self.engine.get_processing_summary()

        status = {
            'pipeline_info': self.pipeline_stats,
            'current_state': current_summary,
            'capabilities': {
                'pdf_processing': self.engine.grobid_processor is not None,
                'semantic_deduplication': self.deduplicator is not None and self.deduplicator.is_available(),
                'graph_persistence': self.engine.graph_backend is not None,
                'concept_enhancement': True  # Always available
            },
            'status_timestamp': datetime.now().isoformat()
        }

        return status

    def close(self):
        """Clean shutdown of pipeline components"""
        print("Shutting down pipeline components...")
        if self.engine:
            self.engine.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()


def main():
    """Main pipeline demonstration"""
    print("Full Production Knowledge Evolution Pipeline")
    print("=" * 60)

    with FullProductionPipeline() as pipeline:

        # Show pipeline status
        status = pipeline.get_pipeline_status()
        print(f"\nPipeline Status:")
        capabilities = status['capabilities']
        print(f"  PDF Processing: {capabilities['pdf_processing']}")
        print(f"  Semantic Deduplication: {capabilities['semantic_deduplication']}")
        print(f"  Graph Persistence: {capabilities['graph_persistence']}")
        print(f"  Concept Enhancement: {capabilities['concept_enhancement']}")

        # Run minimal demo
        demo_result = pipeline.run_minimal_demo()

        print(f"\nPipeline demonstration completed successfully!")
        print(f"Created {demo_result['synthetic_concepts_added']} synthetic concepts")
        print(f"Exported to {len(demo_result['export_files'])} files")

        return demo_result


if __name__ == "__main__":
    main()