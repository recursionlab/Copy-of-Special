from __future__ import annotations

import sqlite3
from pathlib import Path
from typing import Dict, Any, Optional
from datetime import datetime
import json

DB_PATH = Path(".provenance.db")


def _ensure():
    con = sqlite3.connect(str(DB_PATH))
    cur = con.cursor()
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS runs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            run_at TEXT,
            end_at TEXT,
            duration_seconds REAL,
            status TEXT,
            args TEXT,
            manifest TEXT,
            artifacts TEXT
        )
        """
    )
    con.commit()
    con.close()


def register_run(args: Dict[str, Any], manifest: Dict[str, Any], *,
                 start_at: Optional[datetime] = None,
                 end_at: Optional[datetime] = None,
                 status: str = "ok",
                 artifacts: Optional[Dict[str, Any]] = None) -> int:
    """Register a run and return the run id. start_at/end_at can be provided to compute duration.

    Args and manifest are serialized as JSON.
    """
    _ensure()
    start_at = start_at or datetime.utcnow()
    end_at = end_at
    duration = None
    if end_at:
        duration = (end_at - start_at).total_seconds()

    con = sqlite3.connect(str(DB_PATH))
    cur = con.cursor()
    cur.execute(
        "INSERT INTO runs (run_at, end_at, duration_seconds, status, args, manifest, artifacts) VALUES (?, ?, ?, ?, ?, ?, ?)",
        (
            start_at.isoformat(),
            end_at.isoformat() if end_at else None,
            duration,
            status,
            json.dumps(args, ensure_ascii=False),
            json.dumps(manifest, ensure_ascii=False),
            json.dumps(artifacts or {}, ensure_ascii=False),
        ),
    )
    con.commit()
    run_id = cur.lastrowid
    con.close()
    return run_id


def start_run(args: Dict[str, Any], manifest: Dict[str, Any]) -> int:
    """Create a run entry with status 'running' and return run_id."""
    return register_run(args, manifest, start_at=datetime.utcnow(), status="running")


def finish_run(run_id: int, status: str = "success", artifacts: Optional[Dict[str, Any]] = None) -> None:
    _ensure()
    end_at = datetime.utcnow()
    con = sqlite3.connect(str(DB_PATH))
    cur = con.cursor()
    # compute duration
    cur.execute("SELECT run_at FROM runs WHERE id=?", (run_id,))
    row = cur.fetchone()
    start_at = None
    if row and row[0]:
        start_at = datetime.fromisoformat(row[0])
    duration = None
    if start_at:
        duration = (end_at - start_at).total_seconds()
    cur.execute("UPDATE runs SET end_at=?, duration_seconds=?, status=?, artifacts=? WHERE id=?",
                (end_at.isoformat(), duration, status, json.dumps(artifacts or {}, ensure_ascii=False), run_id))
    con.commit()
    con.close()


def artifact_checksum(path: str) -> Optional[str]:
    import hashlib
    p = Path(path)
    if not p.exists():
        return None
    h = hashlib.sha256()
    with p.open("rb") as fh:
        for chunk in iter(lambda: fh.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()

