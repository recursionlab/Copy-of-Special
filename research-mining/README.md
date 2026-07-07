# Research Mining — Ingestion & Deduplication

This small project extracts "ConceptUnits" from research artifacts, deduplicates and clusters them, and produces cleaned JSON and CSV outputs for downstream analysis.

Quick files:
- `ingest/pipeline.py` — main extraction pipeline (PDF/MD/TXT/JSON streaming)
- `ingest/run_pipeline.py` — runner to process a directory and export ConceptUnits
- `ingest/dedupe_cluster.py` — dedupe and token-Jaccard clustering
- `schemas/concept-unit-schema.json` — JSON Schema for ConceptUnit
- `archive/` — output directory for exports

Install (recommended in a virtualenv):

```pwsh
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Basic runs:

Extract from a directory (writes to `archive/conversation_export_units.json`):

```pwsh
python .\ingest\run_pipeline.py D:\149 --out archive/conversation_export_units.json
```

Deduplicate and cluster (reads `archive/conversation_export_units.json`):

```pwsh
python .\ingest\dedupe_cluster.py
```

Next steps implemented in this branch:
- Cluster aggregation (merging members into an enriched representative)
- Optional semantic clustering using `sentence-transformers` if installed

If you need help running on Windows PowerShell, share the exact error output and I'll help adjust commands.
# Research Mining

This repo ingests research artifacts (PDF/MD/TXT) into structured ConceptUnits and exports them for ΞKernel integration.

## Running tests

Locally (PowerShell):

```powershell
cd research-mining\ingest
python -m pytest -q
```

Or run the quick unit checks directly:

```powershell
python run_unit_checks.py
```

CI: a GitHub Actions workflow runs pytest on push/PR to `main` (see `.github/workflows/python-ci.yml`).

