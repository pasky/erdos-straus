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


# ---------------------------------------------------------------- step 2a: candidate near-duplicate pairs

def _ref_keys(it):
    ks = set()
    for r in it["refs"]:
        for m in re.findall(r"(\d{4}\.\d{4,5}|[a-z\-]+/\d{7})", r):
            ks.add("arx:" + m)
        for m in re.findall(r"\bA\d{6}\b", r):
            ks.add("oeis:" + m)
    return ks


def _problem_no(it):
    m = re.match(r"Problem (\d+)", it["title"])
    return m.group(1) if m else None


def candidate_pairs(items):
    """TF-IDF cosine (title+connection) always; bge-small embedding cosine if sentence-transformers is available
    (`uv run --no-project --with sentence-transformers --with scikit-learn --extra-index-url
    https://download.pytorch.org/whl/cpu --index-strategy unsafe-best-match`). Thresholds calibrated by eye."""
    import numpy as np
    from sklearn.feature_extraction.text import TfidfVectorizer
    txt = [it["title"] + " . " + it["title"] + " . " + it["connection"] for it in items]
    vec = TfidfVectorizer(ngram_range=(1, 2), sublinear_tf=True, stop_words="english",
                          token_pattern=r"(?u)\b\w[\w₀-₉⁰-⁹]*\b")
    X = vec.fit_transform(txt)
    S = (X @ X.T).toarray()
    try:
        from sentence_transformers import SentenceTransformer
        m = SentenceTransformer("BAAI/bge-small-en-v1.5", device="cpu")
        E = m.encode([it["title"] + ". " + it["connection"] for it in items], batch_size=64,
                     normalize_embeddings=True, show_progress_bar=False)
        C = E @ E.T
    except ImportError:
        print("WARNING: sentence-transformers unavailable; TF-IDF candidates only", file=sys.stderr)
        C = S * 0
    K = [_ref_keys(it) for it in items]
    P = [_problem_no(it) for it in items]
    out = []
    n = len(items)
    for i in range(n):
        for j in range(i + 1, n):
            e, t = float(C[i, j]), float(S[i, j])
            shared = bool(K[i] & K[j])
            same = items[i]["lane"] == items[j]["lane"]
            if same:  # lanes already removed literal in-lane dups; only very close in-lane pairs are candidates
                ok = e >= 0.90 or t >= 0.40
            else:
                ok = e >= 0.85 or t >= 0.30 or (shared and e >= 0.78)
            if not ok:
                continue
            if P[i] and P[j] and P[i] != P[j]:  # signature lane: distinct Erdős problems are distinct items
                continue
            out.append((items[i]["id"], items[j]["id"], round(e, 3), round(t, 3), int(shared)))
    out.sort(key=lambda r: -max(r[2], r[3] + 0.55))
    return out


def cmd_pairs():
    items = load()
    os.makedirs(MERGE_DIR, exist_ok=True)
    pairs = candidate_pairs(items)
    with open(os.path.join(MERGE_DIR, "candidates.tsv"), "w") as fh:
        fh.write("id_a\tid_b\temb_cos\ttfidf_cos\tshared_ref\n")
        for r in pairs:
            fh.write("\t".join(map(str, r)) + "\n")
    print(len(pairs), "candidate pairs")


# ---------------------------------------------------------------- step 2b: clusters from verdicts + overrides

def _read_tsv(path):
    rows = []
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            line = line.rstrip("\n")
            if not line or line.startswith("#") or line.startswith("id_a\t"):
                continue
            rows.append(line.split("\t"))
    return rows


def clusters(items):
    """Union-find over DUP verdicts (data/z52b/merge/dup_decisions.tsv), then manual group overrides
    (data/z52b/merge/cluster_overrides.tsv). Returns list of id-lists (singletons included), in lane order."""
    ids = [it["id"] for it in items]
    known = set(ids)
    groups = []
    overridden = set()
    with open(os.path.join(MERGE_DIR, "cluster_overrides.tsv"), encoding="utf-8") as fh:
        for line in fh:
            line = line.split("#", 1)[0].strip()
            if not line:
                continue
            g = line.split()
            for x in g:
                assert x in known, f"override: unknown id {x}"
                assert x not in overridden, f"override: {x} listed twice"
                overridden.add(x)
            groups.append(g)
    par = {x: x for x in ids}

    def find(x):
        while par[x] != x:
            par[x] = par[par[x]]
            x = par[x]
        return x

    for a, b, verdict, *_ in _read_tsv(os.path.join(MERGE_DIR, "dup_decisions.tsv")):
        assert a in known and b in known, (a, b)
        if verdict == "DUP" and a not in overridden and b not in overridden:
            par[find(a)] = find(b)
    comp = collections.defaultdict(list)
    for x in ids:
        if x not in overridden:
            comp[find(x)].append(x)
    allg = list(comp.values()) + groups
    order = {x: i for i, x in enumerate(ids)}
    allg = [sorted(g, key=order.get) for g in allg]
    allg.sort(key=lambda g: order[g[0]])
    assert sum(len(g) for g in allg) == len(ids)
    return allg


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "build"
    if cmd == "validate":
        load(report=True)
    elif cmd == "pairs":
        cmd_pairs()
    elif cmd == "clusters":
        its = load()
        cl = clusters(its)
        sz = collections.Counter(len(g) for g in cl)
        print(f"{len(its)} raw -> {len(cl)} distinct; cluster sizes {sorted(sz.items())}")
        with open(os.path.join(MERGE_DIR, "clusters.json"), "w") as fh:
            json.dump([g for g in cl if len(g) > 1], fh, indent=0)
    else:
        raise SystemExit(f"unknown command {cmd}")
