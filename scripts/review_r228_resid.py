"""R228: independent within-cell residual computation for NEAR_SQUARE_EXIST §3 (input = per-prime counts
p Nw Nm Ncl Nclm Nfl Nflm ..., e.g. z2_hardness output, whose per-prime counts R228 matched with
review_r228_genus.py on two subranges). Cells: p mod 8, (r/p) for odd primes r <= 31, least non-residue capped at 35.
Residual = y - mean of y over the prime's cell; reported per K0 = p - floor(sqrt p)^2 bin, with SE and a cell-permutation
null (K0 labels shuffled within cells) to calibrate."""
import sys
from math import isqrt
import numpy as np
rows = [list(map(int, l.split()[:7])) for l in open(sys.argv[1])]
R = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
def leg(a, p):
    x = pow(a, (p - 1) // 2, p)
    return -1 if x == p - 1 else x
P = np.array([r[0] for r in rows]); Nw, Nm, Ncl, Nclm, Nfl, Nflm = (np.array([r[i] for r in rows], float) for i in range(1, 7))
K0 = np.array([p - isqrt(p) ** 2 for p in P])
key = []
for p in P:
    q = 2
    while leg(q, int(p)) == 1:
        q += 1
    key.append((int(p) % 8,) + tuple(leg(r, int(p)) for r in R) + (min(q, 35),))
cid = {}
c = np.array([cid.setdefault(k, len(cid)) for k in key])
def within(y):
    s = np.bincount(c, y); n = np.bincount(c)
    return y - (s / n)[c]
Y = {'old N-/(N-Ncl)': Nm / (Nw - Ncl), 'new N-/(N-Ncl-Nfl)': Nm / (Nw - Ncl - Nfl), 'Nfl/N': Nfl / Nw}
res = {k: within(v) for k, v in Y.items()}
print("primes", len(P), "cells", len(cid))
bins = [(1, 2), (2, 5), (5, 10), (10, 17), (17, 30), (30, 100), (100, 300), (300, 10 ** 12)]
for lo, hi in bins:
    s = (K0 >= lo) & (K0 < hi)
    print(f"[{lo},{hi}) n={s.sum():5d} " + "  ".join(f"{k}: {res[k][s].mean():+.4f}±{res[k][s].std()/np.sqrt(s.sum()):.4f}" for k in Y))
for K in (24,):
    s = K0 == K
    print(f"K0={K} n={s.sum()} " + "  ".join(f"{k}: {res[k][s].mean():+.4f}" for k in Y))
