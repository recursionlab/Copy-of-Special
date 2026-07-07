#!/usr/bin/env python3
"""
Continue processing remaining PDFs - skip already processed ones
"""

import json
from pathlib import Path
from ingest.llm_extractor import LLMExtractor

def get_processed_files():
    """Get list of already processed files from progress files"""
    processed = set()

    # Check all progress files
    for progress_file in Path(".").glob("llm_concepts_progress_*.json"):
        try:
            with open(progress_file) as f:
                concepts = json.load(f)
                for concept in concepts:
                    source = concept.get('source', '')
                    if source:
                        processed.add(source)
        except:
            continue

    return processed

def main():
    api_key = "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"
    extractor = LLMExtractor(api_key, model="openrouter/sonoma-sky-alpha")

    # Get all PDFs and already processed ones
    pdf_dir = Path("../meta-knowledge")
    all_pdfs = list(pdf_dir.glob("*.pdf"))
    processed_sources = get_processed_files()

    # Filter to only unprocessed PDFs
    remaining_pdfs = []
    for pdf in all_pdfs:
        if pdf.name not in processed_sources:
            remaining_pdfs.append(pdf)

    print(f"Total PDFs: {len(all_pdfs)}")
    print(f"Already processed: {len(processed_sources)}")
    print(f"Remaining to process: {len(remaining_pdfs)}")

    if not remaining_pdfs:
        print("All PDFs already processed!")
        return

    # Load existing concepts
    all_concepts = []
    try:
        with open("llm_concepts_progress_30.json") as f:
            all_concepts = json.load(f)
    except:
        pass

    print(f"Starting with {len(all_concepts)} existing concepts")
    print("-" * 60)

    processed_count = 30  # Starting from where we left off

    for pdf_file in remaining_pdfs:
        try:
            print(f"[{processed_count+1}] Processing: {pdf_file.name}")

            concepts = extractor.process_pdf(str(pdf_file))

            if concepts:
                all_concepts.extend(concepts)
                print(f"  -> {len(concepts)} concepts (total: {len(all_concepts)})")

            processed_count += 1

            # Save every 5 files
            if processed_count % 5 == 0:
                with open(f"llm_concepts_progress_{processed_count}.json", 'w') as f:
                    json.dump(all_concepts, f, indent=2)
                print(f"  -> Saved progress: {len(all_concepts)} total concepts")

        except Exception as e:
            print(f"  -> ERROR: {e}")

    # Final save
    with open("llm_extracted_concepts_FINAL.json", 'w') as f:
        json.dump(all_concepts, f, indent=2)

    print(f"\nFINAL: {len(all_concepts)} concepts from {processed_count} PDFs")
    print("Saved to: llm_extracted_concepts_FINAL.json")

if __name__ == "__main__":
    main()