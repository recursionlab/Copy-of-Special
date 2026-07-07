#!/usr/bin/env python3
"""
Enhanced Production Knowledge Engine
Integrates Neo4j backend + GROBID processing + LLM enhancement
"""

import json
import os
from typing import Dict, List, Optional, Any
from datetime import datetime

from production_knowledge_engine import ProductionKnowledgeEngine
from grobid_processor import GrobidProcessor
from knowledge_evolution_v2_1 import ConceptUnit, QualityTier

class EnhancedProductionEngine(ProductionKnowledgeEngine):
    """Production engine with enhanced PDF processing and LLM integration"""

    def __init__(self, config_path: str = "config.yaml",
                 use_graph_backend: bool = True,
                 use_grobid: bool = True):
        """Initialize enhanced engine with additional processors"""
        super().__init__(config_path, use_graph_backend)

        # Initialize GROBID processor
        self.use_grobid = use_grobid
        self.grobid_processor = None

        if use_grobid:
            try:
                self.grobid_processor = GrobidProcessor()
                grobid_available = self.grobid_processor.is_grobid_available()
                print(f"GROBID processor initialized (available: {grobid_available})")
            except Exception as e:
                print(f"Failed to initialize GROBID processor: {e}")
                self.grobid_processor = None

    def process_pdf_document(self, pdf_path: str,
                           min_concept_length: int = 50,
                           max_concepts_per_doc: int = 20) -> Dict[str, Any]:
        """Process PDF document and extract concepts using GROBID"""

        if not os.path.exists(pdf_path):
            return {'error': f"PDF file not found: {pdf_path}"}

        try:
            # Process with GROBID
            if self.grobid_processor:
                document = self.grobid_processor.process_pdf(pdf_path, extract_entities=True)

                if document:
                    print(f"GROBID processed: {document.title}")
                    print(f"  Sections: {len(document.sections)}")
                    print(f"  Entities: {len(document.entities)}")

                    # Convert to knowledge concepts
                    concepts_added = 0
                    concepts_filtered = 0

                    # Process sections as concepts
                    for section in document.sections:
                        if len(section.content) >= min_concept_length:
                            concept_data = {
                                'label': section.title,
                                'definition': section.content[:500],  # Limit length
                                'source_evidence': f"{document.title} - {section.title}",
                                'metadata': {
                                    'source_type': 'grobid_section',
                                    'document_title': document.title,
                                    'section_type': section.section_type,
                                    'authors': document.authors
                                }
                            }

                            concept = self.add_concept_from_unit(concept_data)
                            if concept:
                                concepts_added += 1
                            else:
                                concepts_filtered += 1

                            if concepts_added >= max_concepts_per_doc:
                                break

                    # Process high-confidence entities
                    for entity in document.entities:
                        if (entity.confidence > 0.7 and
                            concepts_added < max_concepts_per_doc and
                            len(entity.context) >= min_concept_length):

                            concept_data = {
                                'label': entity.text,
                                'definition': f"Entity of type {entity.entity_type}: {entity.context}",
                                'source_evidence': f"{document.title} - {entity.section_context}",
                                'metadata': {
                                    'source_type': 'grobid_entity',
                                    'entity_type': entity.entity_type,
                                    'confidence': entity.confidence,
                                    'document_title': document.title
                                }
                            }

                            concept = self.add_concept_from_unit(concept_data)
                            if concept:
                                concepts_added += 1
                            else:
                                concepts_filtered += 1

                    return {
                        'success': True,
                        'document_title': document.title,
                        'concepts_added': concepts_added,
                        'concepts_filtered': concepts_filtered,
                        'sections_processed': len(document.sections),
                        'entities_processed': len(document.entities),
                        'processing_method': 'grobid'
                    }

                else:
                    return {'error': 'GROBID processing failed'}

            else:
                return {'error': 'GROBID processor not available'}

        except Exception as e:
            return {'error': f"PDF processing failed: {e}"}

    def process_pdf_batch(self, pdf_directory: str,
                         file_pattern: str = "*.pdf",
                         max_files: int = 10) -> Dict[str, Any]:
        """Process multiple PDF files in batch"""

        from pathlib import Path

        pdf_dir = Path(pdf_directory)
        if not pdf_dir.exists():
            return {'error': f"Directory not found: {pdf_directory}"}

        pdf_files = list(pdf_dir.glob(file_pattern))[:max_files]

        if not pdf_files:
            return {'error': f"No PDF files found in {pdf_directory}"}

        batch_results = {
            'processed_files': [],
            'failed_files': [],
            'total_concepts_added': 0,
            'total_concepts_filtered': 0,
            'processing_start': datetime.now().isoformat()
        }

        print(f"Processing batch of {len(pdf_files)} PDF files...")

        for pdf_file in pdf_files:
            print(f"\nProcessing: {pdf_file.name}")
            result = self.process_pdf_document(str(pdf_file))

            if 'error' in result:
                batch_results['failed_files'].append({
                    'file': str(pdf_file),
                    'error': result['error']
                })
                print(f"  ERROR: {result['error']}")
            else:
                batch_results['processed_files'].append({
                    'file': str(pdf_file),
                    'result': result
                })
                batch_results['total_concepts_added'] += result.get('concepts_added', 0)
                batch_results['total_concepts_filtered'] += result.get('concepts_filtered', 0)
                print(f"  SUCCESS: {result.get('concepts_added', 0)} concepts added")

        batch_results['processing_end'] = datetime.now().isoformat()
        return batch_results

    def enhance_concept_definitions(self, quality_threshold: float = 0.5) -> Dict[str, Any]:
        """Enhance concept definitions using LLM (placeholder for future implementation)"""

        # Get concepts that could benefit from enhancement
        candidates = [
            concept for concept in self.concepts.values()
            if (concept.definition_completeness < quality_threshold and
                concept.quality_tier in [QualityTier.MID, QualityTier.LOW])
        ]

        enhanced_count = 0

        # Placeholder enhancement - in production, this would use an LLM
        for concept in candidates[:5]:  # Limit for demo
            # Simulate enhancement
            original_length = len(concept.definition_full)
            enhanced_definition = f"{concept.definition_full} Enhanced: This concept represents a fundamental element in the domain with specific operational characteristics and measurable properties."

            concept.definition_full = enhanced_definition
            concept.definition_completeness = min(1.0, concept.definition_completeness + 0.2)
            concept.successful_refinements += 1

            # Re-evaluate quality tier
            concept._assign_quality_tier()

            enhanced_count += 1
            print(f"Enhanced: {concept.label} (quality: {concept.definition_completeness:.2f})")

        return {
            'candidates_found': len(candidates),
            'concepts_enhanced': enhanced_count,
            'enhancement_method': 'placeholder_llm'
        }

    def get_processing_summary(self) -> Dict[str, Any]:
        """Get comprehensive processing summary"""
        base_stats = self.get_enhanced_ecosystem_stats()

        # Count concepts by source type
        source_types = {}
        grobid_concepts = 0

        for concept in self.concepts.values():
            # Check if concept has metadata
            if hasattr(concept, 'metadata') and concept.metadata:
                source_type = concept.metadata.get('source_type', 'unknown')
                source_types[source_type] = source_types.get(source_type, 0) + 1

                if source_type.startswith('grobid'):
                    grobid_concepts += 1

        processing_summary = {
            'ecosystem_stats': base_stats,
            'source_distribution': source_types,
            'grobid_concepts': grobid_concepts,
            'processors_status': {
                'graph_backend': self.graph_backend.driver is not None if self.graph_backend else False,
                'grobid_processor': self.grobid_processor is not None,
                'grobid_service': self.grobid_processor.is_grobid_available() if self.grobid_processor else False
            },
            'summary_timestamp': datetime.now().isoformat()
        }

        return processing_summary


def demo_enhanced_engine():
    """Demonstrate enhanced production engine capabilities"""
    print("=== Enhanced Production Knowledge Engine Demo ===")

    with EnhancedProductionEngine() as engine:

        # Show initial status
        print("\nProcessor Status:")
        summary = engine.get_processing_summary()
        processors = summary['processors_status']
        print(f"  Graph Backend: {processors['graph_backend']}")
        print(f"  GROBID Processor: {processors['grobid_processor']}")
        print(f"  GROBID Service: {processors['grobid_service']}")

        # Add some initial concepts
        initial_concepts = [
            {
                "label": "Artificial Intelligence",
                "definition": "The simulation of human intelligence in machines that are programmed to think and learn",
                "source_evidence": "Manual input - AI definition"
            },
            {
                "label": "Machine Learning",
                "definition": "A subset of AI that enables machines to learn from data",
                "source_evidence": "Manual input - ML definition"
            }
        ]

        print(f"\nAdding {len(initial_concepts)} initial concepts...")
        for concept_data in initial_concepts:
            result = engine.add_concept_from_unit(concept_data)
            if result:
                print(f"  Added: {result.label}")

        # Demonstrate PDF processing (if PDFs available)
        pdf_directory = "."
        if os.path.exists(pdf_directory):
            print(f"\nLooking for PDFs in {pdf_directory}...")
            batch_result = engine.process_pdf_batch(pdf_directory, max_files=2)

            if 'error' not in batch_result:
                print(f"  Processed: {len(batch_result['processed_files'])} files")
                print(f"  Failed: {len(batch_result['failed_files'])} files")
                print(f"  Total concepts added: {batch_result['total_concepts_added']}")
            else:
                print(f"  {batch_result['error']}")

        # Demonstrate concept enhancement
        print(f"\nTesting concept enhancement...")
        enhancement_result = engine.enhance_concept_definitions()
        print(f"  Candidates found: {enhancement_result['candidates_found']}")
        print(f"  Concepts enhanced: {enhancement_result['concepts_enhanced']}")

        # Run evolution
        print(f"\nRunning knowledge evolution...")
        engine.evolve_knowledge_ecosystem(cycles=1)

        # Final summary
        final_summary = engine.get_processing_summary()
        print(f"\nFinal Summary:")
        print(f"  Total concepts: {final_summary['ecosystem_stats']['total_concepts']}")
        print(f"  Active concepts: {final_summary['ecosystem_stats']['active_concepts']}")
        print(f"  GROBID concepts: {final_summary['grobid_concepts']}")
        print(f"  Source distribution: {final_summary['source_distribution']}")

        # Export enhanced results
        results = engine.export_production_results("enhanced_demo_results")
        print(f"\nExported enhanced results: {len(results['files_created'])} files")

        return final_summary


if __name__ == "__main__":
    demo_enhanced_engine()