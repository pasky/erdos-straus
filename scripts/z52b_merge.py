#!/usr/bin/env python3
"""Wave z52b merge lane: build the master TODO of ES connections from data/z52b/<lane>.jsonl.

Usage (reproducible build, run from repo root):
    uv run --with numpy --with scikit-learn python scripts/z52b_merge.py validate
    uv run --with numpy --with scikit-learn python scripts/z52b_merge.py pairs   # candidate near-dup pairs -> data/z52b/merge/
    uv run --with numpy --with scikit-learn python scripts/z52b_merge.py build   # master.jsonl + ES_CONNECTIONS_TODO.md

Never drops items except true duplicates. Duplicate decisions = automatic (very high text similarity)
plus manual judgements recorded in data/z52b/merge/dup_decisions.tsv (pair-level: id_a, id_b, verdict, note).
"""
import collections
import glob
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, "data", "z52b")
MERGE_DIR = os.path.join(DATA, "merge")
LANES = ["analogues", "dividing", "fingerprint", "free_astra", "free_fable", "free_opus",
         "signature", "tools", "translate", "upgrades"]
CORE = ["id", "title", "connection", "why", "first_step", "refs", "tags", "confidence_not_nonsense", "effort"]
CONF = {"low": 0, "med": 1, "medium": 1, "high": 2}
EFFORT = {"cheap": 0, "medium": 1, "med": 1, "big": 2}


def _clean_str(s):
    if s is None:
        return ""
    if not isinstance(s, str):
        s = json.dumps(s, ensure_ascii=False)
    return re.sub(r"\s+", " ", s).strip()


def _clean_list(x):
    if x is None:
        return []
    if isinstance(x, str):
        x = [x] if x.strip() else []
    out, seen = [], set()
    for v in x:
        v = _clean_str(v)
        if v and v not in seen:
            seen.add(v)
            out.append(v)
    return out


def load(report=False):
    """Load + validate + normalise all lane items. Returns list of dicts (with 'lane' and 'extra')."""
    items, problems = [], []
    for lane in LANES:
        path = os.path.join(DATA, lane + ".jsonl")
        with open(path, encoding="utf-8") as fh:
            for ln, line in enumerate(fh, 1):
                if not line.strip():
                    problems.append(f"{lane}:{ln}: blank line (skipped)")
                    continue
                try:
                    o = json.loads(line)
                except json.JSONDecodeError as e:
                    problems.append(f"{lane}:{ln}: malformed JSON ({e}) — FIX IN SOURCE")
                    continue
                it = {"lane": lane}
                for k in ("id", "title", "connection", "why", "first_step"):
                    it[k] = _clean_str(o.get(k))
                    if not it[k]:
                        problems.append(f"{lane}:{ln}: empty/missing field {k}")
                it["refs"] = _clean_list(o.get("refs"))
                it["tags"] = _clean_list(o.get("tags"))
                c = _clean_str(o.get("confidence_not_nonsense")).lower()
                e = _clean_str(o.get("effort")).lower()
                if c not in CONF:
                    problems.append(f"{lane}:{ln}: bad confidence {c!r} -> med")
                    c = "med"
                if e not in EFFORT:
                    problems.append(f"{lane}:{ln}: bad effort {e!r} -> medium")
                    e = "medium"
                it["confidence_not_nonsense"] = "med" if c == "medium" else c
                it["effort"] = "medium" if e == "med" else e
                if not it["id"].startswith(lane + "-"):
                    problems.append(f"{lane}:{ln}: id {it['id']!r} lacks lane prefix")
                # lane-specific extra fields (analogues:world, signature:raw_id, upgrades:upgrade) kept verbatim
                it["extra"] = {k: v for k, v in o.items() if k not in CORE}
                items.append(it)
    ids = collections.Counter(it["id"] for it in items)
    for k, v in ids.items():
        if v > 1:
            problems.append(f"duplicate id {k} x{v}")
    if report:
        for p in problems:
            print("PROBLEM", p)
        cnt = collections.Counter(it["lane"] for it in items)
        for lane in LANES:
            print(f"{lane:12s} {cnt[lane]:5d}")
        print(f"{'TOTAL':12s} {len(items):5d}   problems: {len(problems)}")
    return items


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "build"
    if cmd == "validate":
        load(report=True)
    else:
        raise SystemExit(f"unknown command {cmd}")
