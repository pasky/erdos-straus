"""Summarize sterile_survey.py output by dyadic ranges of p.

uv run python scripts/sterile_stats.py FILE.jsonl [FILE2 ...]
"""
import json, sys, math
from collections import Counter, defaultdict

rows = {}
for fn in sys.argv[1:]:
    for line in (__import__("gzip").open(fn, "rt") if fn.endswith(".gz") else open(fn)):
        r = json.loads(line)
        rows[r["p"]] = r
by = defaultdict(list)
for p, r in rows.items():
    by[int(math.log2(p))].append(r)
tot = Counter()
print("range      n   maxster  mean_max  frac_max>=8  min_seedfrac  mean_nster  record_p")
for k in sorted(by):
    R = by[k]
    mx = [r["maxsterile"] for r in R]
    best = max(R, key=lambda r: r["maxsterile"])
    sf = min(r["seedsize"] / r["V"] for r in R)
    nst = sum(sum(r["sterile_hist"].values()) for r in R) / len(R)
    for r in R:
        for s, c in r["sterile_hist"].items():
            tot[int(s)] += c
    print(f"2^{k:<3} {len(R):7d} {max(mx):6d} {sum(mx)/len(R):9.2f} {sum(m>=8 for m in mx)/len(R):10.4f} {sf:12.3f} {nst:10.1f}  {best['p']}")
print("aggregate sterile size histogram:", dict(sorted(tot.items())))
