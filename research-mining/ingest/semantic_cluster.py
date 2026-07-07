"""Semantic clustering helper with lazy imports, embedding cache, and model approval checks.

APIs:
 - available() -> bool
 - cluster_by_embeddings(units, threshold=0.6, model_name='all-MiniLM-L6-v2', require_approved=False)

This module will use `embedding_cache` to store embeddings per text+model_name.
"""
from __future__ import annotations

from typing import List, Dict, Any
from collections import defaultdict


_HAS_DEPS = None


def _try_imports():
    global _HAS_DEPS, SentenceTransformer, np, AgglomerativeClustering, cosine_similarity
    if _HAS_DEPS is not None:
        return
    try:
        from sentence_transformers import SentenceTransformer
        import numpy as np
        from sklearn.cluster import AgglomerativeClustering
        from sklearn.metrics.pairwise import cosine_similarity
        _HAS_DEPS = True
    except Exception:
        SentenceTransformer = None  # type: ignore
        np = None  # type: ignore
        AgglomerativeClustering = None  # type: ignore
        cosine_similarity = None  # type: ignore
        _HAS_DEPS = False


def available() -> bool:
    _try_imports()
    return bool(_HAS_DEPS)


def _embed_with_cache(texts: List[str], model_name: str):
    from ingest import embedding_cache

    # simple cache: per-text entry; for multi-text inputs we return list of embeddings
    embeddings = []
    missing = []
    for i, t in enumerate(texts):
        cached = embedding_cache.get(t, model_name)
        if cached is not None:
            import json

            embeddings.append(json.loads(cached))
        else:
            embeddings.append(None)
            missing.append(i)

    if missing:
        _try_imports()
        if not _HAS_DEPS:
            # cannot compute missing embeddings
            raise ImportError("sentence-transformers not available to compute embeddings")
        model = SentenceTransformer(model_name)
        to_compute = [texts[i] for i in missing]
        new_embs = model.encode(to_compute, convert_to_numpy=True, show_progress_bar=False)
        import json

        for idx, emb in zip(missing, new_embs):
            emb_list = emb.tolist() if hasattr(emb, "tolist") else list(emb)
            embedding_cache.set_cache(texts[idx], model_name, json.dumps(emb_list))
            embeddings[idx] = emb_list

    # convert to numpy array for downstream use if numpy is available
    _try_imports()
    if np is not None:
        return np.asarray(embeddings)
    return embeddings


def cluster_by_embeddings(units: List[Dict[str, Any]], threshold: float = 0.6, model_name: str = "all-MiniLM-L6-v2", require_approved: bool = False) -> List[List[int]]:
    """Cluster units semantically; check model approval if require_approved is True.

    Raises ImportError if dependencies are unavailable or if the model is not approved when required.
    """
    from ingest import model_registry

    if require_approved and not model_registry.is_approved(model_name):
        raise PermissionError(f"Model {model_name} is not approved for production use")

    texts = [(u.get("definition") or "").strip() for u in units]
    if not any(texts):
        return [[i] for i in range(len(units))]

    embs = _embed_with_cache(texts, model_name)
    _try_imports()
    if not _HAS_DEPS:
        raise ImportError("semantic clustering dependencies not available")

    # normalize
    norms = embs / (np.linalg.norm(embs, axis=1, keepdims=True) + 1e-12)
    sim = cosine_similarity(norms)
    dist = 1.0 - sim

    try:
        clustering = AgglomerativeClustering(n_clusters=None, affinity='precomputed', linkage='average', distance_threshold=1.0 - threshold)
    except TypeError:
        clustering = AgglomerativeClustering(n_clusters=None, metric='precomputed', linkage='average', distance_threshold=1.0 - threshold)

    labels = clustering.fit_predict(dist)
    groups = defaultdict(list)
    for i, lab in enumerate(labels):
        groups[int(lab)].append(i)
    return list(groups.values())
"""Optional semantic clustering helper.

Requires `sentence_transformers` and `sklearn` for full functionality. If unavailable,
the calling code should fall back to token-based clustering.
"""
from typing import List, Dict, Any, Optional

try:
    from sentence_transformers import SentenceTransformer
    from sklearn.cluster import AgglomerativeClustering
    import numpy as np
    _HAS_MODEL = True
except Exception:
    _HAS_MODEL = False


def available() -> bool:
    return _HAS_MODEL


def embed_texts(texts: List[str], model_name: str = "all-MiniLM-L6-v2"):
    if not _HAS_MODEL:
        raise ImportError("sentence-transformers or sklearn not available")
    model = SentenceTransformer(model_name)
    return model.encode(texts, convert_to_numpy=True, show_progress_bar=False)


def cluster_by_embeddings(units: List[Dict[str, Any]], threshold: float = 0.6, model_name: str = "all-MiniLM-L6-v2") -> List[List[int]]:
    """Produce clusters using embeddings + agglomerative clustering.

    threshold: distance threshold for agglomerative clustering (0-1).
    Returns list of clusters as lists of indices into `units`.
    """
    if not _HAS_MODEL:
        raise ImportError("semantic clustering dependencies not available")

    texts = [(u.get("definition") or "") for u in units]
    embs = embed_texts(texts, model_name=model_name)
    # compute cosine distances
    # AgglomerativeClustering expects a distance matrix or feature vectors; we'll use embeddings + cosine affinity via linkage
    # sklearn's AgglomerativeClustering with affinity='cosine' is deprecated in some versions; instead, compute normalized vectors and use euclidean with threshold.
    norms = embs / (np.linalg.norm(embs, axis=1, keepdims=True) + 1e-12)
    # distance = 1 - cosine_similarity
    from sklearn.metrics.pairwise import cosine_similarity
    sim = cosine_similarity(norms)
    dist = 1.0 - sim

    # heuristic: convert threshold to distance threshold
    clustering = AgglomerativeClustering(n_clusters=None, affinity='precomputed', linkage='average', distance_threshold=1.0 - threshold)
    labels = clustering.fit_predict(dist)
    clusters = {}
    for idx, lab in enumerate(labels):
        clusters.setdefault(int(lab), []).append(idx)
    return list(clusters.values())
"""Optional semantic clustering helper.

Uses `sentence_transformers` to embed text then clusters via sklearn's AgglomerativeClustering.
This module is optional; callers should gracefully fall back to token-jaccard if imports fail.
"""
try:
    from sentence_transformers import SentenceTransformer
    import numpy as np
    from sklearn.cluster import AgglomerativeClustering
except Exception:
    # Expose a sentinel to indicate semantic clustering is unavailable
    SentenceTransformer = None
    np = None
    AgglomerativeClustering = None


def available() -> bool:
    return SentenceTransformer is not None and np is not None and AgglomerativeClustering is not None


def embed_texts(texts, model_name: str = 'all-MiniLM-L6-v2'):
    if not available():
        raise ImportError('sentence-transformers or sklearn not available')
    model = SentenceTransformer(model_name)
    embeddings = model.encode(texts, show_progress_bar=False)
    return np.asarray(embeddings)


def semantic_cluster(texts, n_clusters: int = None, distance_threshold: float = 1.0):
    """Cluster texts using embeddings.

    - If n_clusters is provided, AgglomerativeClustering uses that; otherwise it uses distance_threshold.
    - Returns a list of lists of indices representing clusters.
    """
    if not available():
        raise ImportError('semantic clustering unavailable')
    embs = embed_texts(texts)
    if n_clusters is not None:
        clustering = AgglomerativeClustering(n_clusters=n_clusters, affinity='euclidean', linkage='ward')
    else:
        clustering = AgglomerativeClustering(n_clusters=None, distance_threshold=distance_threshold, affinity='euclidean', linkage='ward')
    labels = clustering.fit_predict(embs)
    clusters = {}
    for i, l in enumerate(labels):
        clusters.setdefault(int(l), []).append(i)
    return list(clusters.values())
"""Optional semantic clustering helper using sentence-transformers.

This module tries to import `sentence_transformers`. If available it exposes
`semantic_clusters(units, threshold)` that returns cluster lists (list of index lists).
If not available, importing will raise ImportError and caller should fallback.
"""
from typing import List, Dict, Any

try:
    from sentence_transformers import SentenceTransformer
    import numpy as np
    from sklearn.cluster import AgglomerativeClustering
except Exception as e:
    raise ImportError("sentence-transformers or its dependencies are not installed") from e


MODEL = SentenceTransformer('all-MiniLM-L6-v2')


def embed_texts(texts: List[str]):
    return MODEL.encode(texts, show_progress_bar=False, convert_to_numpy=True)


def semantic_clusters(units: List[Dict[str, Any]], threshold: float = 0.6) -> List[List[int]]:
    """Cluster units semantically using embeddings and agglomerative clustering.

    Returns clusters as lists of indices into `units`.
    """
    texts = [(u.get('definition') or '') for u in units]
    if not any(texts):
        return [[i] for i in range(len(units))]

    emb = embed_texts(texts)
    # compute cosine distance matrix
    from sklearn.metrics.pairwise import cosine_distances
    D = cosine_distances(emb)
    # Agglomerative clustering with distance threshold
    clustering = AgglomerativeClustering(n_clusters=None, affinity='precomputed', linkage='average', distance_threshold=1.0 - threshold)
    labels = clustering.fit_predict(D)
    groups = {}
    for i, lab in enumerate(labels):
        groups.setdefault(int(lab), []).append(i)
    return list(groups.values())
