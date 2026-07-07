"""Clean dedupe + cluster implementation (separate file).

This avoids editing the corrupted `dedupe_cluster.py` and provides a
small, validated script to run immediately.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from collections import defaultdict
from pathlib import Path
from typing import Dict, List, Tuple
import sys


def text_signature(u: Dict) -> str:
    m = hashlib.sha256()
    parts = [str(u.get(k) or "").strip().lower() for k in ("definition", "mathematical_formulation", "notes")]
    m.update("\n".join(parts).encode("utf-8"))
    return m.hexdigest()


def tokenize(text: str):
    if not text:
        return set()
    return set(t for t in re.findall(r"\w+", text.lower()) if len(t) > 2)


def jaccard(a: set, b: set) -> float:
    if not a or not b:
        return 0.0
    return len(a & b) / len(a | b)


def dedupe_units(units: List[Dict]) -> Tuple[List[Dict], Dict[str, List[Tuple[int, Dict]]]]:
    hm: Dict[str, List[Tuple[int, Dict]]] = defaultdict(list)
    for i, u in enumerate(units):
        hm[text_signature(u)].append((i, u))

    deduped: List[Dict] = []
    for h, items in hm.items():
        rep = max(items, key=lambda t: len((t[1].get("definition") or "")))
        rep_unit = dict(rep[1])
        rep_unit.setdefault("_member_indices", [])
        rep_unit["_member_indices"].extend([idx for idx, _ in items])
        rep_unit["_dedupe_hash"] = h
        deduped.append(rep_unit)
    return deduped, hm


def cluster_jaccard(units: List[Dict], threshold: float = 0.45) -> List[List[int]]:
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


def aggregate_cluster(units: List[Dict], member_indices: List[int]) -> Dict:
    members = [units[i] for i in member_indices]
    rep = max(members, key=lambda u: len((u.get("definition") or "")))
    agg = dict(rep)
    agg["members"] = [m.get("id") for m in members if m.get("id")]
    return agg


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--input", help="Path to conversation_export_units.json")
    p.add_argument("--out-dir", help="Output directory")
    p.add_argument("--threshold", type=float, default=0.45)
    args = p.parse_args()

    repo = Path(__file__).resolve().parents[1]
    src = Path(args.input) if args.input else repo / "archive" / "conversation_export_units.json"
    outdir = Path(args.out_dir) if args.out_dir else repo / "archive"
    if not src.exists():
        print(f"Missing input: {src}")
        sys.exit(1)

    units = json.loads(src.read_text(encoding="utf-8"))
    print(f"Loaded {len(units)} units")

    deduped, hash_map = dedupe_units(units)
    print(f"Deduped -> {len(deduped)} units (from {len(units)})")

    clusters = cluster_jaccard(deduped, threshold=args.threshold)
    print(f"Produced {len(clusters)} clusters")

    outdir.mkdir(parents=True, exist_ok=True)
    cleaned = [deduped[c[0]] for c in clusters]
    (outdir / "conversation_export_units_cleaned.json").write_text(json.dumps(cleaned, ensure_ascii=False, indent=2), encoding="utf-8")

    aggregated = []
    for ci, c in enumerate(clusters, start=1):
        agg = aggregate_cluster(deduped, c)
        agg["cluster_id"] = ci
        agg["member_count"] = len(c)
        aggregated.append(agg)
    (outdir / "conversation_export_units_aggregated.json").write_text(json.dumps(aggregated, ensure_ascii=False, indent=2), encoding="utf-8")

    print("Wrote cleaned and aggregated outputs")


if __name__ == '__main__':
    main()
