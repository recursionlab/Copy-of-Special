"""
CLI runner for research-mining ingestion
"""

import argparse
import os
from pathlib import Path

from ingest.pipeline import IngestionPipeline
from ingest import model_registry, embedding_cache, provenance
import json
import tempfile
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description="Research Mining Ingestion CLI")
    parser.add_argument("path", help="File or directory path to ingest")
    parser.add_argument("--schema", default="schemas/concept-unit-schema.json", help="Path to ConceptUnit JSON schema")
    parser.add_argument("--out", default="archive/extracted_concepts.json", help="Output JSON path")
    parser.add_argument("--recursive", action="store_true", help="Process directories recursively")
    args = parser.parse_args()

    os.makedirs("archive", exist_ok=True)

    pipeline = IngestionPipeline(args.schema)

    # start provenance run
    manifest = {"args": vars(args)}
    run_id = provenance.start_run(vars(args), manifest)
    print(f"Run started id={run_id}")

    input_path = Path(args.path)
    if input_path.is_dir():
        pipeline.process_directory(str(input_path), recursive=args.recursive)
    else:
        pipeline.process_file(str(input_path))

    # Export atomically: write to temp file then rename
    try:
        tmp = Path(tempfile.gettempdir()) / (Path(args.out).name + ".tmp")
        pipeline.export_concepts(str(tmp))
        # ensure parent exists
        out_path = Path(args.out)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        tmp.replace(out_path)
    except Exception as exc:
        provenance.finish_run(run_id, status="failed", artifacts={})
        raise

    stats = pipeline.get_statistics()
    print("\nExtraction Statistics:")
    for k, v in stats.items():
        print(f" - {k}: {v}")

    # compute artifact checksum
    checksum = provenance.artifact_checksum(str(out_path))
    artifacts = {"out": {"path": str(out_path), "sha256": checksum}}
    # finish provenance run as success
    provenance.finish_run(run_id, status="success", artifacts=artifacts)
    print(f"Run finished id={run_id}, artifact sha256={checksum}")


if __name__ == "__main__":
    main()
