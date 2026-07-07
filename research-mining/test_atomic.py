#!/usr/bin/env python3
"""
Test atomic concept extraction
"""

import json
from ingest.atomic_extractor import AtomicExtractor

def main():
    api_key = "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"
    extractor = AtomicExtractor(api_key, model="openrouter/sonoma-sky-alpha")

    # Test with a sample PDF
    pdf_path = "../meta-knowledge/Knowledge Reproduction Processes.pdf"

    print("Testing atomic extraction...")
    print("Target: Short terms, crisp definitions, typed relations")
    print("-" * 60)

    try:
        concepts = extractor.process_pdf(pdf_path)

        if concepts:
            print(f"\nExtracted {len(concepts)} atomic concepts:")

            for i, concept in enumerate(concepts, 1):
                print(f"\n{i}. {concept.get('term', 'N/A')}")
                print(f"   Type: {concept.get('type', 'Unknown')}")
                print(f"   Definition: {concept.get('definition', 'N/A')}")
                print(f"   Relations: {len(concept.get('relations', []))}")

                # Show relations
                for rel in concept.get('relations', [])[:2]:  # First 2
                    print(f"     -> {rel.get('type', '?')}: {rel.get('target', '?')}")

            # Save results
            with open("atomic_test_results.json", 'w') as f:
                json.dump(concepts, f, indent=2)

            print(f"\nResults saved to: atomic_test_results.json")

            # Quick quality check
            avg_def_length = sum(len(c.get('definition', '')) for c in concepts) / len(concepts)
            total_relations = sum(len(c.get('relations', [])) for c in concepts)

            print(f"\nQuality metrics:")
            print(f"  Average definition length: {avg_def_length:.0f} chars")
            print(f"  Total relations: {total_relations}")
            print(f"  Relations per concept: {total_relations/len(concepts):.1f}")

        else:
            print("No concepts extracted")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()