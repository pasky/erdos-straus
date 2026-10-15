"""R227 from-scratch within-cell residuals by K0 = p - floor(sqrt p)^2, from review_r227_census.c output (mode 0).
Columns: p N Nm U Ntc Na viol isprime.  Cells: (p mod 16, p mod 9, (r/p) for r in 3..13, min(lnr, 17)).
Residual of a statistic y = y - (mean of y over the cell, LEAVE-ONE-OUT so the prime itself is not in its own baseline).
Prints mean residual and a cell-aware SE (sd of residuals / sqrt n) for N-/N, N-/(N-Nt), N-/U.
usage: review_r227_resid.py FILE PLO PHI
"""
import sys
import numpy as np
from math import isqrt

d = np.loadtxt(sys.argv[1], dtype=np.int64)
lo, hi = int(sys.argv[2]), int(sys.argv[3])
d = d[(d[:, 0] > lo) & (d[:, 0] < hi)]
p, N, Nm, U, Ntc = d[:, 0], d[:, 1], d[:, 2], d[:, 3], d[:, 4]


def leg(a, q):
    r = pow(int(a), (int(q) - 1) // 2, int(q))
    return -1 if r == q - 1 else r


def lnr(q):
    a = 2
    while leg(a, q) == 1:
        a += 1
    return a


keys = [(int(x % 16), int(x % 9)) + tuple(leg(r, x) for r in (3, 5, 7, 11, 13)) + (min(lnr(int(x)), 17),) for x in p]
cid = {}
c = np.array([cid.setdefault(k, len(cid)) for k in keys])
K0 = np.array([int(x) - isqrt(int(x)) ** 2 for x in p])
ys = {"N-/N": Nm / N, "N-/(N-Nt)": Nm / (N - Ntc), "N-/U": Nm / U}
print(f"primes {len(p)} cells {len(cid)}")
R = {}
for k, y in ys.items():
    s = np.bincount(c, y)
    n = np.bincount(c)
    ok = n[c] > 1
    R[k] = np.where(ok, y - (s[c] - y) / np.maximum(n[c] - 1, 1), np.nan)
bins = [(1, 5), (5, 10), (10, 17), (17, 30), (30, 100), (100, 300), (300, 10 ** 9)]
for b in bins + [(8, 9), (16, 17), (24, 25), (4, 5), (12, 13), (28, 29)]:
    s = (K0 >= b[0]) & (K0 < b[1])
    out = []
    for k in ys:
        r = R[k][s]
        r = r[~np.isnan(r)]
        out.append(f"{k}: {r.mean():+.4f}±{r.std(ddof=1) / np.sqrt(len(r)):.4f}")
    print(f"K0 in [{b[0]},{b[1]}) n={s.sum():6d}  " + "  ".join(out))
# share of residual removed, per bin
