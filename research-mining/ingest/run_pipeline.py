"""Runner script to process a directory with the ingestion pipeline"""
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parents[1]))  # Add project root

from ingest.pipeline import IngestionPipeline


def run(input_dir: str, output_file: str = 'archive/extracted_concepts.json'):
    pipeline = IngestionPipeline(schema_path='schemas/concept-unit-schema.json')
    pipeline.process_directory(input_dir)
    pipeline.export_concepts(output_file)
    print('Done')


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('input_dir', help='Directory to process')
    parser.add_argument('--out', default='archive/extracted_concepts.json', help='Output JSON file')
    args = parser.parse_args()
    run(args.input_dir, args.out)
