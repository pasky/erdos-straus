"""R222: from scratch, level-1 boxes for r = 13, 17 (P-data of N = r, Q-points of F = r; box centre -a/b mod r, both
orientations), and which quadratic non-residue cells mod r they cover.  Usage: uv run python scripts/review_se_level1.py"""
import sys; sys.path.insert(0, __file__.rsplit('/', 1)[0])
from review_se_lemmas import pdata, qdata
for r in (13, 17):
    nr = sorted({x * x % r for x in range(1, r)}); qnr = [u for u in range(1, r) if u not in nr]
    cov = set()
    for (a, b, c, d, e) in pdata(r):
        for (x, y) in ((a, b), (b, a)):
            if x % r and y % r: cov.add(-x * pow(y, -1, r) % r)
    for (a, b, c, d, e, f) in qdata(r):
        if e % r:
            for (x, y) in ((a, b), (b, a)): cov.add(-x * pow(y, -1, r) % r)
    print(f"r={r}: QNR cells {qnr}; level-1 centres {sorted(cov)}; uncovered QNR cells {[u for u in qnr if u not in cov]}")
