import sys
from pathlib import Path
import json

# ensure project root is importable
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from ingest.dedupe_cluster import text_signature, dedupe_units, cluster_jaccard, aggregate_cluster


def make_unit(id, definition, tags=None, refs=None, conf=None, notes=None):
    return {
        "id": id,
        "definition": definition,
        "tags": tags or [],
        "references": refs or [],
        "confidence_score": conf,
        "notes": notes,
    }


def test_text_signature_and_dedupe():
    u1 = make_unit("a", "A simple concept")
    u2 = make_unit("b", "A simple concept")
    u3 = make_unit("c", "A different one")
    deduped, groups = dedupe_units([u1, u2, u3])
    # two groups expected
    assert len(groups) == 2
    # deduped representatives should be 2
    assert len(deduped) == 2


def test_cluster_jaccard_and_aggregate():
    u1 = make_unit("a", "neural network deep learning")
    u2 = make_unit("b", "deep learning for images")
    u3 = make_unit("c", "category theory basics")
    units = [u1, u2, u3]
    clusters = cluster_jaccard(units, threshold=0.2)
    # expect at least 2 clusters
    assert len(clusters) >= 2
    # aggregate first cluster
    agg = aggregate_cluster(units, clusters[0])
    assert "members" in agg
    assert isinstance(agg["members"], list)
import sys
import os
import pytest
# ensure the project `research-mining` package path is on sys.path for tests
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from ingest import dedupe_cluster


def make_unit(id_, definition, tags=None, references=None, confidence=None, notes=None):
    return {
        'id': id_,
        'definition': definition,
        'tags': tags or [],
        'references': references or [],
        'confidence_score': confidence,
        'notes': notes,
    }


def test_text_signature_and_dedupe():
    u1 = make_unit('a', 'This is a definition.')
    u2 = make_unit('b', 'This is a definition.')
    u3 = make_unit('c', 'Different definition')
    sig1 = dedupe_cluster.text_signature(u1)
    sig2 = dedupe_cluster.text_signature(u2)
    sig3 = dedupe_cluster.text_signature(u3)
    assert sig1 == sig2
    assert sig1 != sig3

    deduped, groups = dedupe_cluster.dedupe_units([u1, u2, u3])
    # should dedupe the first two into one representative
    assert len(deduped) == 2


def test_cluster_and_aggregate():
    u1 = make_unit('a', 'cat dog mouse', tags=['animal'], confidence=0.9, notes='note1')
    u2 = make_unit('b', 'cat dog', tags=['pet'], confidence=0.8, notes='note2')
    u3 = make_unit('c', 'quantum field theory', tags=['physics'], confidence=0.6)
    units = [u1, u2, u3]
    clusters = dedupe_cluster.cluster_jaccard(units, threshold=0.3)
    # expect at least 2 clusters
    assert len(clusters) >= 2
    # aggregate first cluster
    agg = dedupe_cluster.aggregate_cluster(units, clusters[0])
    assert 'members' in agg
    assert isinstance(agg.get('confidence_score', None), float) or agg.get('confidence_score') is None
