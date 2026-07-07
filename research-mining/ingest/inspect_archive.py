#!/usr/bin/env python3
"""Simple inspector for archive JSON files.

Usage examples:
  python -m ingest.inspect_archive --path archive/meta_knowledge_concepts.json --sample 3 --top-sources 5
"""
from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path
from typing import Iterable


def iter_units(path: Path):
    with path.open("r", encoding="utf-8") as f:
        data = json.load(f)
        if isinstance(data, dict):
            # single object
            yield data
        else:
            for item in data:
                yield item


def top_sources(units: Iterable[dict], k: int = 10):
    c = Counter()
    for u in units:
        c[u.get("source", "<unknown>")] += 1
    return c.most_common(k)


def sample_units(units: Iterable[dict], n: int = 5, by_source: str | None = None):
    out = []
    for u in units:
        if by_source and u.get("source") != by_source:
            continue
        out.append(u)
        if len(out) >= n:
            break
    return out


def find_candidate_archive(root: Path) -> Path | None:
    candidates = [root / "archive" / "meta_knowledge_concepts.json",
                  root / "archive" / "extracted_concepts.json"]
    for p in candidates:
        if p.exists():
            return p
    # fallback: first json under archive
    arch = root / "archive"
    if arch.exists():
        for p in arch.glob("*.json"):
            return p
    return None


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--path", type=Path, help="Path to archive JSON (default: project/archive/*.json)")
    ap.add_argument("--sample", type=int, default=3, help="Number of sample units to show")
    ap.add_argument("--top-sources", type=int, default=10, help="Show top N sources")
    ap.add_argument("--by-source", type=str, default=None, help="Filter samples by exact source filename")
    args = ap.parse_args()

    root = Path(__file__).resolve().parents[1]
    path = args.path or find_candidate_archive(root)
    if not path:
        print("No archive JSON found under project archive/; pass --path to specify a file.")
        return 2

    print(f"Inspecting archive: {path}")
    units = list(iter_units(path))
    total = len(units)
    print(f"Total units: {total}")

    # top sources
    ts = top_sources(units, args.top_sources)
    print("Top sources:")
    for src, cnt in ts:
        print(f"  {cnt:6d}  {src}")

    # sample
    print(f"\nSample units (n={args.sample}){f' from {args.by_source}' if args.by_source else ''}:")
    samples = sample_units(units, n=args.sample, by_source=args.by_source)
    for i, s in enumerate(samples, 1):
        sid = s.get("id", "<no-id>")
        src = s.get("source", "<no-source>")
        typ = s.get("type", "<no-type>")
        defin = s.get("definition", "").replace("\n", " ")[:400]
        print(f"\n[{i}] id={sid} src={src} type={typ}\n    {defin}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
"""Quick inspector for archive outputs: counts and sample clusters."""
from pathlib import Path
import json

archive = Path(__file__).resolve().parents[1] / "archive"
files = list(archive.glob("*"))
print("Archive files:")
for f in files:
    print(f" - {f.name} ({f.stat().st_size} bytes)")

agg_path = archive / "conversation_export_units_aggregated.json"
if not agg_path.exists():
    print("No aggregated file found.")
    raise SystemExit(1)

with agg_path.open("r", encoding="utf-8") as f:
    agg = json.load(f)

print(f"Aggregated clusters: {len(agg)}")
print("Sample clusters:")
for a in agg[:3]:
    print(f" - cluster {a.get('cluster_id')} members={a.get('member_count')} id={a.get('id')} def={str(a.get('definition') or '')[:120]!r}")
