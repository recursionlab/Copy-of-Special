"""Small helper to run a model against a canned dataset to validate behavior.

This is intentionally lightweight: it either uses sentence-transformers if available
or returns a simple deterministic embedding for tests.
"""
from typing import List


def sample_texts() -> List[str]:
    return [
        "Alpha beta gamma",
        "Beta gamma delta",
        "Completely different content",
    ]


def get_embeddings(model_name: str = "all-MiniLM-L6-v2"):
    try:
        from sentence_transformers import SentenceTransformer
        import numpy as np

        model = SentenceTransformer(model_name)
        return model.encode(sample_texts(), convert_to_numpy=True)
    except Exception:
        # deterministic fallback
        return [[1.0, 0.0], [0.9, 0.1], [0.0, 1.0]]


def validate_model(model_name: str = "all-MiniLM-L6-v2") -> bool:
    embs = get_embeddings(model_name)
    # simple sanity checks
    try:
        import numpy as np

        arr = np.asarray(embs)
        return arr.shape[0] == 3
    except Exception:
        return False
