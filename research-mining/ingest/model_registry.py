from __future__ import annotations

import json
from pathlib import Path
from typing import Dict, Any, List, Optional
from datetime import datetime

REG_DIR = Path(".models")
REG_DIR.mkdir(exist_ok=True)
REG_PATH = REG_DIR / "registry.json"


def _load() -> Dict[str, Any]:
    if not REG_PATH.exists():
        return {"approved": []}
    try:
        return json.loads(REG_PATH.read_text(encoding="utf-8"))
    except Exception:
        return {"approved": []}


def _save(data: Dict[str, Any]):
    REG_PATH.write_text(json.dumps(data, indent=2), encoding="utf-8")


def approve_model(name: str, model_hash: Optional[str] = None, meta: Optional[Dict[str, Any]] = None) -> None:
    d = _load()
    meta = meta or {}
    entry = {"name": name, "hash": model_hash, "meta": meta, "approved_at": datetime.utcnow().isoformat()}
    # dedupe by name+hash
    for e in d.get("approved", []):
        if e.get("name") == name and (not model_hash or e.get("hash") == model_hash):
            return
    d.setdefault("approved", []).append(entry)
    _save(d)


def list_approved() -> List[Dict[str, Any]]:
    return _load().get("approved", [])


def is_approved(name: str, model_hash: Optional[str] = None) -> bool:
    for e in list_approved():
        if e.get("name") == name and (model_hash is None or e.get("hash") == model_hash):
            return True
    return False
