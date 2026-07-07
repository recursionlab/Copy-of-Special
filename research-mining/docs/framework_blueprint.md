Framework Blueprint — Personal Research-Mining

Goal
---
A compact, pragmatic blueprint for a personal research-mining system built around your existing repo and the `meta-knowledge` corpus. Focus: clarity, reproducibility, fast iteration, minimal friction, and well-scoped primitives you can extend.

Principles
---
- Local-first: everything works offline and locally unless you opt-in to cloud or heavy models.
- Small-surface API: a few well-documented functions/classes that do the work; keep CLI glue thin.
- Deterministic-by-default: reproducible IDs, canonical text normalization, and versioned transforms.
- Incremental: prefer incremental runs and caches so iteration is fast.
- Observable: basic provenance, run manifests, and human-friendly inspection tools.

High-level architecture
---
- Ingest layer (extractors): convert PDFs/JSONs into ConceptUnits (dicts) with source metadata.
- Normalization layer: canonicalize text, tokenization, stopword removal, deterministic ID generation.
- Dedupe & clustering layer: deterministic dedupe (hash), token-Jaccard clustering as default; optional semantic clustering (lazy).
- Aggregation layer: select representatives and merge metadata.
- Persistence layer: simple file archives (JSON) + small SQLite index for querying.
- Ops primitives: embedding cache (.embedding_cache), model registry (.models/registry.json), provenance DB (.provenance.db).
- UX: `ingest_cli.py`, `inspect_archive.py`, `notebooks/` demo.

Core contracts / interfaces
---
1) ConceptUnit (dict): keys: `id`, `version`, `source`, `definition`, `tags`, `references`, `notes`, `confidence_score`, `extraction_date`.
   - `id` must be deterministic (short-sha prefix + human token) and stable given same input and `hash_version`.

2) Extractor API:
   - Input: filepath
   - Output: List[ConceptUnit]
   - Should never raise on malformed files; return empty list and write an error log entry instead.

3) Pipeline API (class IngestionPipeline):
   - __init__(schema_path: str, config: Optional[dict])
   - process_file(path: str) -> None
   - process_directory(path: str, recursive: bool = True) -> None
   - export_concepts(out_path: str) -> None
   - get_statistics() -> dict
   - checkpoint() -> write run manifest (for resume)

4) Semantic clustering API (ingest.semantic_cluster.cluster_by_embeddings):
   - Accepts `units: List[ConceptUnit]`, `threshold: float`, `model_name: str`, `require_approved: bool`
   - Returns List[List[int]] indices into `units`

Pros & Cons (patterns observed in meta-knowledge)
---
Pros:
- Rich corpus (`meta-knowledge`) supports testing of linguistic edge cases, domain concepts, and multi-discipline semantics.
- Current system already has dedupe, semantic optional paths, and provenance — good base primitives.

Cons / Risks:
- Heavy dependencies (sentence-transformers, numpy) can bloat dev setup; default should avoid installing them.
- Extractor outputs contain duplicated/fragmented units (see many same `id` repeats); need better canonicalization and merging.
- Too many optional features bundled — creates surface area for breakage; prefer small, explicit opt-in flags.

Design recommendations (applied)
---
- Use a `config.yaml` to define dev vs prod defaults (dev: sample corpus, no semantic, quick settings).
- Keep semantic clustering behind `--semantic` flag; default pipeline uses token-Jaccard.
- Introduce canonicalization stage that: unicode normalize, collapse whitespace, remove boilerplate tokens, and apply stemming/lemmatization optionally.
- Deduplicate by content hash over canonicalized significant fields: `definition`, `mathematical_formulation`, `notes`.
- Aggregation: choose representative by (1) longest useful `definition` (2) highest confidence (3) union of tags/references.

Test plan / sample test cases
---
- Unit tests
  - determinism: same file re-ingested yields same IDs
  - tokenizer invariants: "Recursive Loop" vs "recursive loop" → same tokens set
  - dedupe: identical definitions collapsed to single unit
  - cluster_jaccard: similar short texts cluster at expected threshold
  - semantic fallback: when sentence-transformers missing, cluster_jaccard still runs

- Integration tests
  - small corpus: run pipeline on 3 PDFs, assert output counts and no exceptions
  - checkpoint/resume: interrupt run mid-directory and resume — final output same as uninterrupted
  - export atomicity: ensure partial exports not left behind on failure

Minimal roadmap (personal-focused)
---
1. Add `config.yaml`, `--dev` flag, and a one-command runner script. (0.5–2h)
2. Add `inspect_archive.py` that prints counts, top tags, and sample entries. (1h)
3. Add canonicalization stage + unit tests (2–4h). Run on `meta-knowledge` subset.
4. Add embedding cache index file and `--semantic` toggle. (1–2h)
5. Add notebook demo for visual quick checks. (2–6h)

File templates / small snippets
---
- canonicalize_text(text: str) -> str
- deterministic_id(definition: str, source_path: str, salt: str) -> str
- run_manifest schema: {run_id, start_at, end_at, args, artifacts:[{path,sha256}], sample_counts}

How I'll help next (pick one)
---
- I can implement `docs/framework_blueprint.md` (done) plus `inspect_archive.py` to start.  
- Or I can implement `config.yaml` + `--dev` toggle in `ingest_cli.py`.  
- Or I can implement the canonicalization function and add unit tests.

Which do you want me to implement now? I can start with `inspect_archive.py` for quick iteration and exploration. 
