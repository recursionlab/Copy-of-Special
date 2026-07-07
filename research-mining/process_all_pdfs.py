#!/usr/bin/env python3
"""
Process all PDFs in meta-knowledge with LLM extraction
"""

import json
import time
from pathlib import Path
from ingest.llm_extractor import LLMExtractor

def main():
    # Initialize with your API key
    api_key = "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"
    extractor = LLMExtractor(api_key, model="openrouter/sonoma-sky-alpha")

    # Find all PDFs
    pdf_dir = Path("../meta-knowledge")
    pdf_files = list(pdf_dir.glob("*.pdf"))

    print(f"Found {len(pdf_files)} PDFs to process")
    print("Using Sonoma Sky Alpha (Grok)")
    print("-" * 60)

    all_concepts = []
    processed = 0
    errors = []

    for pdf_file in pdf_files:
        try:
            print(f"\n[{processed+1}/{len(pdf_files)}] Processing: {pdf_file.name}")

            concepts = extractor.process_pdf(str(pdf_file))

            if concepts:
                all_concepts.extend(concepts)
                print(f"  -> Extracted {len(concepts)} concepts")
            else:
                print("  -> No concepts extracted")

            processed += 1

            # Minimal delay to maximize API usage
            time.sleep(0.1)

            # Save progress every 5 files for faster feedback
            if processed % 5 == 0:
                save_progress(all_concepts, processed)

        except Exception as e:
            error_msg = f"Error processing {pdf_file.name}: {str(e)}"
            print(f"  -> ERROR: {error_msg}")
            errors.append(error_msg)
            time.sleep(0.5)  # Minimal delay on error

    # Final save
    save_final_results(all_concepts, processed, errors)

def save_progress(concepts, count):
    """Save intermediate progress"""
    filename = f"llm_concepts_progress_{count}.json"
    with open(filename, 'w') as f:
        json.dump(concepts, f, indent=2)
    print(f"  -> Progress saved: {len(concepts)} concepts to {filename}")

def save_final_results(concepts, processed, errors):
    """Save final comprehensive results"""

    # Main results
    with open("llm_extracted_concepts_all.json", 'w') as f:
        json.dump(concepts, f, indent=2)

    # Summary stats
    stats = {
        "total_pdfs_processed": processed,
        "total_concepts_extracted": len(concepts),
        "concepts_by_type": {},
        "average_confidence": 0,
        "errors": errors
    }

    # Calculate stats
    if concepts:
        total_confidence = 0
        for concept in concepts:
            concept_type = concept.get('type', 'Unknown')
            stats["concepts_by_type"][concept_type] = stats["concepts_by_type"].get(concept_type, 0) + 1
            total_confidence += concept.get('confidence_score', 0)

        stats["average_confidence"] = total_confidence / len(concepts)

    with open("llm_extraction_summary.json", 'w') as f:
        json.dump(stats, f, indent=2)

    print("\n" + "="*60)
    print("FINAL RESULTS:")
    print(f"PDFs processed: {processed}")
    print(f"Concepts extracted: {len(concepts)}")
    print(f"Average confidence: {stats['average_confidence']:.3f}")
    print(f"Errors: {len(errors)}")
    print("\nConcepts by type:")
    for concept_type, count in stats["concepts_by_type"].items():
        print(f"  {concept_type}: {count}")
    print(f"\nResults saved to: llm_extracted_concepts_all.json")
    print(f"Summary saved to: llm_extraction_summary.json")

if __name__ == "__main__":
    main()