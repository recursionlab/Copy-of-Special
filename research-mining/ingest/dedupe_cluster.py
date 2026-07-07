"""Clean dedupe + clustering runner for ConceptUnits.

Minimal, deterministic implementation (atomic replacement).
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from collections import defaultdict
from pathlib import Path
from typing import Any, Dict, List, Set, Tuple

# Optional semantic clustering helper (best-effort import)
try:
    # Try package relative import first (when run as module)
    from . import semantic_cluster as semantic_cluster
except Exception:
    try:
        import semantic_cluster as semantic_cluster
    except Exception:
        semantic_cluster = None


DEDUPE_FIELDS = ("definition", "mathematical_formulation", "notes")


def text_signature(u: Dict[str, Any]) -> str:
    m = hashlib.sha256()
    parts = [str(u.get(k) or "").strip().lower() for k in DEDUPE_FIELDS]
    m.update("\n".join(parts).encode("utf-8"))
    return m.hexdigest()


def tokenize(text: str) -> Set[str]:
    if not text:
        return set()
    return set(t for t in re.findall(r"\w+", text.lower()) if len(t) > 2)


def jaccard(a: Set[str], b: Set[str]) -> float:
    if not a or not b:
        return 0.0
    return len(a & b) / len(a | b)


def dedupe_units(units: List[Dict[str, Any]]) -> Tuple[List[Dict[str, Any]], Dict[str, List[Tuple[int, Dict[str, Any]]]]]:
    hash_map: Dict[str, List[Tuple[int, Dict[str, Any]]]] = defaultdict(list)
    for i, u in enumerate(units):
        h = text_signature(u)
        hash_map[h].append((i, u))

    deduped: List[Dict[str, Any]] = []
    for h, items in hash_map.items():
        rep = max(items, key=lambda t: len((t[1].get("definition") or "")))
        rep_unit = dict(rep[1])
        rep_unit.setdefault("_member_indices", [])
        rep_unit["_member_indices"].extend([idx for idx, _ in items])
        rep_unit["_dedupe_hash"] = h
        deduped.append(rep_unit)

    return deduped, hash_map


def cluster_jaccard(units: List[Dict[str, Any]], threshold: float = 0.45) -> List[List[int]]:
    tokens = [tokenize(u.get("definition") or "") for u in units]
    clusters: List[List[int]] = []
    for i, t in enumerate(tokens):
        placed = False
        for c in clusters:
            if jaccard(t, tokens[c[0]]) >= threshold:
                c.append(i)
                placed = True
                break
        if not placed:
            clusters.append([i])
    return clusters


def aggregate_cluster(units: List[Dict[str, Any]], member_indices: List[int]) -> Dict[str, Any]:
    members = [units[i] for i in member_indices]
    rep = max(members, key=lambda u: len((u.get("definition") or "")))
    agg: Dict[str, Any] = dict(rep)
    agg["members"] = [m.get("id") for m in members if m.get("id")]

    tags = set()
    for m in members:
        for t in m.get("tags") or []:
            tags.add(t)
    if tags:
        agg["tags"] = sorted(tags)

    refs = []
    seen_refs = set()
    for m in members:
        for r in m.get("references") or []:
            key = json.dumps(r, sort_keys=True) if isinstance(r, dict) else str(r)
            if key not in seen_refs:
                refs.append(r)
                seen_refs.add(key)
    if refs:
        agg["references"] = refs

    confs = [float(m.get("confidence_score")) for m in members if m.get("confidence_score") is not None]
    if confs:
        agg["confidence_score"] = sum(confs) / len(confs)

    notes = [m.get("notes") for m in members if m.get("notes")]
    if notes:
        agg["notes"] = "\n---\n".join([n for n in notes if n])[:2000]

    return agg


def write_outputs(archive: Path, src: Path, units: List[Dict[str, Any]], deduped: List[Dict[str, Any]], clusters: List[List[int]], hash_map: Dict[str, List[Tuple[int, Dict[str, Any]]]], threshold: float, mode: str) -> None:
    archive.mkdir(parents=True, exist_ok=True)

    cleaned = [deduped[c[0]] for c in clusters]
    with (archive / "conversation_export_units_cleaned.json").open("w", encoding="utf-8") as f:
        json.dump(cleaned, f, ensure_ascii=False, indent=2)

    aggregated = []
    for ci, c in enumerate(clusters, start=1):
        agg = aggregate_cluster(deduped, c)
        agg["cluster_id"] = ci
        agg["member_count"] = len(c)
        aggregated.append(agg)

    with (archive / "conversation_export_units_aggregated.json").open("w", encoding="utf-8") as f:
        json.dump(aggregated, f, ensure_ascii=False, indent=2)

    with (archive / "concept_clusters_detailed.csv").open("w", encoding="utf-8") as f:
        f.write("cluster_id,representative_id,member_count,representative_definition,tags\n")
        for agg in aggregated:
            rep_id = agg.get("id") or ""
            member_count = agg.get("member_count", 0)
            rep_def = (agg.get("definition") or "").replace('\n', ' ')[:100].replace(',', ' ')
            tags = ' '.join(agg.get("tags") or [])
            f.write(f"{agg.get('cluster_id')},{rep_id},{member_count},{repr(rep_def)},{repr(tags)}\n")

    with (archive / "dedupe_hash_log.txt").open("w", encoding="utf-8") as f:
        for h, items in hash_map.items():
            for i, u in items:
                f.write(f"{i},{u.get('id')},{h}\n")

    metadata = {
        "dedupe_algorithm": "sha256",
        "dedupe_fields": list(DEDUPE_FIELDS),
        "clustering_mode": mode,
        "threshold": threshold,
        "units_input": str(src),
        "units_count": len(units),
        "deduped_count": len(deduped),
        "clusters_count": len(clusters),
    }
    with (archive / "cluster_metadata.json").open("w", encoding="utf-8") as f:
        json.dump(metadata, f, ensure_ascii=False, indent=2)


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser()
    p.add_argument("--mode", choices=["jaccard", "semantic"], default="jaccard")
    p.add_argument("--out-dir", default=None)
    p.add_argument("--input", default=None)
    p.add_argument("--threshold", type=float, default=0.45)
    return p.parse_args()


def main() -> None:
    args = parse_args()
    repo = Path(__file__).resolve().parents[1]
    archive = Path(args.out_dir) if args.out_dir else repo / "archive"
    src = Path(args.input) if args.input else archive / "conversation_export_units.json"
    if not src.exists():
        print(f"Missing {src} — run the pipeline first or pass --input")
        sys.exit(1)

    with src.open("r", encoding="utf-8") as f:
        units = json.load(f)

    print(f"Loaded {len(units)} units")

    deduped, hash_map = dedupe_units(units)
    print(f"Deduped -> {len(deduped)} units (hash groups: {len(hash_map)})")
    # Choose clustering mode: semantic when requested and available, otherwise token-jaccard
    clusters = []
    if args.mode == "semantic" and semantic_cluster is not None:
        try:
            if getattr(semantic_cluster, "available", lambda: False)():
                # prefer a semantic_clusters function if present
                if hasattr(semantic_cluster, "semantic_clusters"):
                    clusters = semantic_cluster.semantic_clusters(deduped, threshold=args.threshold)
                elif hasattr(semantic_cluster, "cluster_by_embeddings"):
                    clusters = semantic_cluster.cluster_by_embeddings(deduped, threshold=args.threshold)
                else:
                    # fallback to embedding-based function names
                    clusters = cluster_jaccard(deduped, threshold=args.threshold)
                print(f"Semantic clustering used: {len(clusters)} clusters")
            else:
                print("Semantic clustering dependencies not available — falling back to jaccard")
                clusters = cluster_jaccard(deduped, threshold=args.threshold)
        except Exception as e:
            print("Semantic clustering failed, falling back to jaccard:", e)
            clusters = cluster_jaccard(deduped, threshold=args.threshold)
    else:
        clusters = cluster_jaccard(deduped, threshold=args.threshold)
    print(f"Clusters produced: {len(clusters)}")

    write_outputs(archive, src, units, deduped, clusters, hash_map, args.threshold, args.mode)

    print("Done: outputs written to", archive)


if __name__ == "__main__":
    main()

