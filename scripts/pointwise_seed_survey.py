"""Survey of seed-to-positive distances in the signed refactor graph.

uv run python scripts/pointwise_seed_survey.py LO HI [--mod 24] [--jobs N]

For every prime p=1 (mod 4) in [LO,HI] (optionally only p=1 mod --mod),
run the exact lazy BFS of pointwise_fibres.explore from the seed.  Output
one JSON line per prime: status FOUND (with shortest distance), STERILE
(entire seed component exhausted, i.e. a counterexample to the seed-component
conjecture), or UNKNOWN (budget/certification limit; no verdict).
Finite evidence only; nothing here is a proof.
"""
from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from multiprocessing import Pool

from sympy import primerange

from pointwise_fibres import FibreOracle, IncompleteSearch, explore


def run(p: int, max_vertices: int = 200_000):
    try:
        result = explore(FibreOracle(p), max_vertices=max_vertices)
    except IncompleteSearch as error:
        return {"p": p, "status": "UNKNOWN", "reason": str(error)}
    out = {"p": p, "status": result.status, "visited": result.visited,
           "expanded": result.expanded}
    if result.path is not None:
        out["dist"] = len(result.path) - 1
        out["end"] = result.path[-1]
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("lo", type=int)
    ap.add_argument("hi", type=int)
    ap.add_argument("--mod", type=int, default=4)
    ap.add_argument("--jobs", type=int, default=8)
    ap.add_argument("--max-vertices", type=int, default=200_000)
    args = ap.parse_args()
    primes = [p for p in primerange(max(args.lo, 5), args.hi + 1)
              if p % 4 == 1 and p % args.mod == 1]
    hist, worst = Counter(), []
    with Pool(args.jobs) as pool:
        for row in pool.imap_unordered(run, primes, chunksize=4):
            print(json.dumps(row), flush=True)
            key = row.get("dist", row["status"])
            hist[key] += 1
            if row["status"] != "FOUND":
                worst.append(row)
    print("SUMMARY", json.dumps({str(k): v for k, v in sorted(hist.items(), key=str)}),
          file=sys.stderr)


if __name__ == "__main__":
    main()
