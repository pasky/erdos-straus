"""Run the exhaustive depth<=3 test (depth3.py) on survivor lists from depth3_sieve.

uv run python scripts/depth3_batch.py FILE [--jobs N] [--all]

FILE has lines "p q" (as printed by the C++ prefilter). For each prime,
prints one JSON line: dist (2, 3, or ">=4"), and per-family hit statistics.
A ">=4" verdict is emitted only with fully certified factorizations
(depth3.Uncertified otherwise -> status UNKNOWN).
"""
from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from multiprocessing import Pool

from depth3 import Depth3, Uncertified, check_path


def run(args):
    p, all_hits = args
    try:
        r = Depth3(p).run(all_hits)
    except Uncertified as e:
        return {"p": p, "status": "UNKNOWN", "reason": str(e)}
    for h in r["hits"]:
        check_path(p, h["path"])
    fam = Counter(h["family"] for h in r["hits"])
    firsts = [(h["family"], h.get("h"), h.get("c"), h.get("d"), h.get("a"), h.get("via"), h.get("delta"))
              for h in r["hits"][:40]]
    return {"p": p, "t": (p - 1) // 4, "dist": r["dist"], "families": dict(fam), "hits": firsts}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("file")
    ap.add_argument("--jobs", type=int, default=16)
    ap.add_argument("--all", action="store_true")
    a = ap.parse_args()
    ps = [int(line.split()[0]) for line in open(a.file) if line.strip()]
    hist = Counter()
    with Pool(a.jobs) as pool:
        for r in pool.imap_unordered(run, [(p, a.all) for p in ps], chunksize=1):
            print(json.dumps(r, default=str), flush=True)
            hist[str(r.get("dist", r.get("status")))] += 1
    print("SUMMARY", dict(hist), file=sys.stderr)


if __name__ == "__main__":
    main()
