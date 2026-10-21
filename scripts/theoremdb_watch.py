#!/usr/bin/env python3
"""Read-only watcher for Erdős–Straus-related records on TheoremDB and erdosproblems.ai.

Uses only the public, unauthenticated API (https://api.theoremdb.org, see /openapi.json).
Never writes to TheoremDB. Keeps a local snapshot and reports records that are new or changed
since the previous run.

    uv run python scripts/theoremdb_watch.py            # report changes, update snapshot
    uv run python scripts/theoremdb_watch.py --dry-run  # report changes, keep old snapshot
"""
import argparse, hashlib, json, re, sys, time, urllib.error, urllib.parse, urllib.request
from pathlib import Path

API = "https://api.theoremdb.org"
SNAP = Path(__file__).resolve().parent.parent / "data" / "theoremdb" / "snapshot.json"

# Problems tracked record-by-record (slugs as resolved by /v1/research/objects).
PROBLEMS = ["erdos-straus-conjecture", "erdos-problem-242"]
# Free-text research-search queries; any hit in an unexpected project is reported too.
# Search hits are kept only if their text matches this (the search endpoint is semantic and noisy).
RELEVANT = re.compile(r"(?i)straus|egyptian|unit[- ]fraction|\b4/n\b|\b5/n\b|schinzel|erdos-problem-242")
QUERIES = ["Erdős–Straus", "Erdos-Straus", "Straus", "Egyptian fraction", "unit fractions",
           "Sierpinski 5/n", "Schinzel unit fraction", "4/n = 1/x + 1/y + 1/z"]


def get(path, **params):
    url = API + path + ("?" + urllib.parse.urlencode(params) if params else "")
    req = urllib.request.Request(url, headers={"User-Agent": "es-campaign-watch/1 (read-only)"})
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            return json.load(r)
    except urllib.error.HTTPError as e:
        return {"error": {"message": f"HTTP {e.code} for {url}"}}


# erdosproblems.ai (Plasma AI) is built from this open repo; we watch commits touching the ES wiki pages.
GITHUB_WATCH = [("plasma-ai/erdos", "wiki/problems/unit_fractions/E0242")]


def digest(obj):
    return hashlib.sha256(json.dumps(obj, sort_keys=True).encode()).hexdigest()[:16]


def collect():
    recs = {}
    for prob in PROBLEMS:
        d = get("/v1/research/objects", problem_ref=prob, limit=200)  # API max is 200
        if "error" in d:
            print(f"WARN {prob}: {d['error'].get('message')}", file=sys.stderr)
            continue
        for o in d.get("objects", []):
            key = o.get("id") or o.get("record_ref")
            recs[key] = {"source": f"problem:{prob}", "ref": o.get("record_ref"), "type": o.get("object_type"),
                         "title": o.get("title"), "summary": (o.get("summary") or "")[:400],
                         "url": f"https://theoremdb.org/records/{o.get('slug')}" if o.get("slug") else None,
                         "digest": digest(o)}
        time.sleep(1)
    for q in QUERIES:
        d = get("/v1/research/search", q=q, limit=25)
        if "error" in d:
            print(f"WARN search {q!r}: {d['error'].get('message')}", file=sys.stderr)
            continue
        for o in d.get("results", []) or []:
            proj = o.get("project") or o.get("problem_ref") or ""
            if proj in PROBLEMS:
                continue  # already tracked in full above
            if not RELEVANT.search(json.dumps(o, ensure_ascii=False)):
                continue
            key = o.get("id") or o.get("record_ref") or digest(o)
            recs.setdefault(key, {"source": f"search:{q}", "ref": o.get("record_ref"), "type": o.get("object_type"),
                                  "title": f"[{proj}] " + (o.get("title") or "")[:200], "summary": "",
                                  "url": None, "digest": digest(o)})
        time.sleep(1)
    for repo, path in GITHUB_WATCH:
        url = f"https://api.github.com/repos/{repo}/commits?" + urllib.parse.urlencode({"path": path, "per_page": 30})
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "es-campaign-watch/1 (read-only)"})
            with urllib.request.urlopen(req, timeout=60) as r:
                commits = json.load(r)
        except urllib.error.HTTPError as e:
            print(f"WARN github {repo}:{path}: HTTP {e.code}", file=sys.stderr)
            continue
        for c in commits:
            recs[f"gh:{repo}:{c['sha']}"] = {"source": f"github:{repo}/{path}", "ref": c["sha"][:10], "type": "commit",
                                            "title": c["commit"]["message"].splitlines()[0][:200],
                                            "summary": c["commit"]["author"]["date"], "url": c.get("html_url"),
                                            "digest": c["sha"]}
    return recs


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    old = json.loads(SNAP.read_text())["records"] if SNAP.exists() else None
    new = collect()
    if old is None:
        print(f"Baseline: {len(new)} records.")
    else:
        added = [k for k in new if k not in old]
        changed = [k for k in new if k in old and new[k]["digest"] != old[k]["digest"]]
        gone = [k for k in old if k not in new]
        for tag, keys in (("NEW", added), ("CHANGED", changed)):
            for k in keys:
                r = new[k]
                print(f"{tag} {r['source']} {r['ref']} {r['type']}: {r['title']}\n    {r['url'] or ''}\n    {r['summary']}")
        for k in gone:
            print(f"GONE {old[k]['source']} {old[k]['ref']}: {old[k]['title']}")
        if not (added or changed or gone):
            print(f"No changes ({len(new)} records).")
    if not a.dry_run:
        SNAP.parent.mkdir(parents=True, exist_ok=True)
        SNAP.write_text(json.dumps({"fetched": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
                                    "records": new}, indent=1, ensure_ascii=False))


if __name__ == "__main__":
    main()
