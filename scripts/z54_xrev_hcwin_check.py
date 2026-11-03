#!/usr/bin/env python3
"""Independent bounded-memory checks for REVIEW_HCWIN.md.

Input: archive of side-agent/z54-hcwin at /tmp/xrev_HCWIN (or argv[1]).
Run: ulimit -v 6000000; timeout 300s uv run --with sympy python scripts/z54_xrev_hcwin_check.py
Only one integer's divisor list and one input row are materialized at a time.
Optional rerun files in the archive root are compared with committed controls.
"""
from collections import defaultdict
from functools import lru_cache
from math import gcd, log
from pathlib import Path
import gzip
import sys

from sympy import divisors

root = Path(sys.argv[1] if len(sys.argv) > 1 else "/tmp/xrev_HCWIN")
data = root / "data/z54/hcwin"


@lru_cache(maxsize=128)
def group(x):
    units = [a for a in range(x) if gcd(a, x) == 1]
    squares = {a * a % x for a in units}
    return len(units), squares, {(-a) % x for a in squares}


def masses(n, cap):
    lam = gam = lottery = 0.0
    at16 = None
    hc = 0
    pre = None
    for x in range(4, min(cap + 1, n)):
        if x % 4 != 0 and x % 8 != 7:
            continue
        old = (lam, gam, lottery)
        hit = False
        phi, squares, target = group(x)
        for ty, value in enumerate((n + x, x * n + 1)):
            ds = divisors(value)
            g = sum(d % x in target for d in ds)
            c = sum(d % x == x - 1 for d in ds)
            m = g / len(squares)
            lam += min(1, len(ds) / phi)
            gam += min(1, m)
            if x not in (4, 7, 8, 12, 15, 24):
                lottery += m / (1 if ty == 0 else 2)
            else:
                assert bool(c) == bool(g), (n, x, ty, c, g)
            hit |= bool(c)
        if hit and not hc:
            hc, pre = x, old
        if x == 16:
            at16 = gam
    return hc, pre if pre is not None else (lam, gam, lottery), at16


known = (193, 409, 577, 2521, 3361, 5569, 9601, 21841, 66529, 83449, 8813281)
print("Independent HC controls:", [(p, masses(p, 64)[0]) for p in known])
checked = hard20 = dead16 = 0
with (data / "hard.txt").open() as f:
    for line in f:
        a = line.split()
        p, expected_hc = map(int, a[:2])
        hc, pre, g16 = masses(p, 64)
        assert hc == expected_hc, (p, hc, expected_hc)
        assert all(abs(got - float(want)) < 0.000501 for got, want in zip(pre, a[2:5])), (p, pre, a[2:5])
        assert abs(g16 - float(a[13])) < 0.00501, (p, g16, a[13])
        checked += 1
        if hc >= 20:
            hard20 += 1
            dead16 += g16 == 0
        if p == 21841:
            print("21841: pre-Lambda, Gamma, S =", pre, "Gamma/log(p) =", pre[1] / log(p))
print("Independent hard checks:", checked, "HC>=20:", hard20, "Gamma(16)=0:", dead16)

for sample in ("stat_1e9", "stat_1e11", "stat_1e13", "stat_4e15"):
    bins = defaultdict(lambda: [0, 0, 0.0])
    with (data / (sample + ".txt.lines")).open() as f:
        for line in f:
            a = line.split()
            if a[0] != "G" or not 6 <= int(a[2]) < 10 or int(a[3]) == 0:
                continue
            b = bins[a[1], float(a[4])]
            b[0] += int(a[5])
            b[1] += int(a[6])
            b[2] += float(a[7 if a[1] == "E" else 8])
    for ty in "EL":
        errors = [(abs((s - pred) / n), lo, n) for (kind, lo), (n, s, pred) in bins.items() if kind == ty and lo >= -1]
        print(sample, ty, "largest pooled m>=1/2 discrepancy (fraction, log2-bin, count):", max(errors))

for sample, rerun in (("sq_1e10", "squares"), ("stat_1e9", "stat_1e9")):
    path = root / (rerun + ".txt")
    if not path.exists():
        continue
    with gzip.open(data / (sample + "_first5000.txt.gz"), "rt") as old, path.open() as new:
        for i, line in enumerate(old, 1):
            assert line == next(new), (sample, i)
    count = bad_genus = 0
    mean = 0.0
    with path.open() as f:
        for line in f:
            a = line.split()
            count += 1
            mean += float(a[54]) / log(int(a[0]))
            bad_genus += float(a[55]) != 0
    print(sample, "rows:", count, "mean Lambda(1024)/log(n):", mean / count, "nonzero Gamma rows:", bad_genus)
print("PASS: all independent hard-prime values and available rerun prefixes agree.")
