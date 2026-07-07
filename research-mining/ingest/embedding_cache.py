from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Optional

CACHE_DIR = Path(".embedding_cache")
CACHE_DIR.mkdir(exist_ok=True)


def _key(text: str, model_name: str) -> str:
    h = hashlib.sha256()
    h.update(text.encode("utf-8"))
    h.update(model_name.encode("utf-8"))
    return h.hexdigest()


def get(text: str, model_name: str) -> Optional[str]:
    k = _key(text, model_name)
    p = CACHE_DIR / (k + ".json")
    if not p.exists():
        return None
    try:
        return p.read_text(encoding="utf-8")
    except Exception:
        return None


def set_cache(text: str, model_name: str, emb_json: str) -> None:
    k = _key(text, model_name)
    p = CACHE_DIR / (k + ".json")
    p.write_text(emb_json, encoding="utf-8")
