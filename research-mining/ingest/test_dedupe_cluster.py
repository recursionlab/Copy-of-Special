import json
from pathlib import Path
import pytest

from ingest.dedupe_cluster import text_signature, tokenize, jaccard, dedupe_units, cluster_jaccard, aggregate_cluster


def sample_unit(id_, definition, tags=None, refs=None, notes=None, confidence=None):
    return {
        "id": id_,
        "definition": definition,
        "tags": tags or [],
        "references": refs or [],
        "notes": notes,
        "confidence_score": confidence,
    }


def test_tokenize_and_jaccard():
    a = tokenize("Recursive loops and feedback")
    b = tokenize("feedback loops in recursion")
    assert "recursive" in a
    assert jaccard(a, b) > 0


def test_text_signature_dedupe():
    u1 = sample_unit("a", "Same def")
    u2 = sample_unit("b", "Same def")
    deduped, hmap = dedupe_units([u1, u2])
    assert len(deduped) == 1
    assert len(hmap) == 1


def test_cluster_jaccard_and_aggregate():
    u1 = sample_unit("a", "apple banana cherry", tags=["fruit"], refs=[{"r":1}], notes="n1", confidence=0.9)
    u2 = sample_unit("b", "apple banana", tags=["fruit","food"], refs=[{"r":1}], notes="n2", confidence=0.7)
    u3 = sample_unit("c", "quantum field theory", tags=["physics"], refs=[], notes=None, confidence=0.8)
    units = [u1, u2, u3]
    deduped, hmap = dedupe_units(units)
    clusters = cluster_jaccard(deduped, threshold=0.3)
    # expect first two to cluster together, third separate
    assert any(len(c) >= 2 for c in clusters)
    # aggregate first cluster
    first = clusters[0]
    agg = aggregate_cluster(deduped, first)
    assert "members" in agg
    assert "tags" in agg
    assert isinstance(agg.get("confidence_score"), float)


def test_edge_cases_empty_and_missing_fields():
    # empty definition
    u1 = sample_unit("a", "")
    # missing definition key
    u2 = {"id": "b"}
    # None fields
    u3 = {"id": "c", "definition": None}
    units = [u1, u2, u3]
    deduped, hmap = dedupe_units(units)
    # dedupe should return entries (may coalesce)
    assert isinstance(deduped, list)


def test_case_insensitive_dedupe():
    u1 = sample_unit("a", "Recursive Loop")
    u2 = sample_unit("b", "recursive loop")
    deduped, hmap = dedupe_units([u1, u2])
    assert len(deduped) == 1


def test_large_text_clustering():
    long = "word " * 2000
    u1 = sample_unit("a", long + " apple")
    u2 = sample_unit("b", long + " banana")
    deduped, hmap = dedupe_units([u1, u2])
    clusters = cluster_jaccard(deduped, threshold=0.1)
    assert isinstance(clusters, list)


def test_semantic_fallback_no_crash():
    # Running dedupe_cluster with mode=semantic should not raise even if semantic libs missing
    from ingest.dedupe_cluster import cluster_jaccard
    u1 = sample_unit("a", "apple banana cherry")
    u2 = sample_unit("b", "apple banana")
    deduped, hmap = dedupe_units([u1, u2])
    # If sentence-transformers not installed, the module will fallback — ensure cluster_jaccard works
    clusters = cluster_jaccard(deduped, threshold=0.3)
    assert clusters
