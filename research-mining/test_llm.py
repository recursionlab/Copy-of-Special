#!/usr/bin/env python3
"""
Test LLM-based extraction on a sample PDF
"""

import json
from ingest.llm_extractor import LLMExtractor

def main():
    # Initialize with your API key
    api_key = "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"
    extractor = LLMExtractor(api_key, model="openrouter/sonoma-sky-alpha")

    # Test with a sample PDF
    pdf_path = "../meta-knowledge/CYBERNETICS.pdf"

    print(f"Testing LLM extraction on: {pdf_path}")
    print("Using model: openrouter/sonoma-sky-alpha")
    print("-" * 50)

    try:
        concepts = extractor.process_pdf(pdf_path)

        if concepts:
            print(f"\nSuccessfully extracted {len(concepts)} concepts!")
            print("\nConcepts found:")
            for i, concept in enumerate(concepts, 1):
                print(f"\n{i}. Type: {concept.get('type', 'Unknown')}")
                print(f"   Definition: {concept.get('definition', 'N/A')}")
                print(f"   Significance: {concept.get('significance', 'N/A')}")
                print(f"   Confidence: {concept.get('confidence_score', 0)}")

            # Save results
            output_file = "llm_test_results.json"
            with open(output_file, 'w') as f:
                json.dump(concepts, f, indent=2)
            print(f"\nResults saved to: {output_file}")
        else:
            print("No concepts extracted")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()