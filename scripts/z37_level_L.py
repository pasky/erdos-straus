"""O267 §3.3: per-level chi-bias of side divisors in near-square families p = m^2 + K versus L(1, chi_j), j = tK + 1.
For each level t <= T: S_t = mean over the family of (1/#range divisors) * sum_{d | tp+1, range} (d/p)   (signed bias).
Prediction (heuristic, §3.3): S_t grows with L_R(1, chi_j) = prod_{r<=R odd prime, r∤j} (1 - (j/r)/r)^{-1} (times 2-adic factor),
and S_t = 1 exactly when j is a square (clean). Prints Spearman correlation over non-square j and a few rows.
Usage: uv run python scripts/z37_level_L.py K T  (family file /tmp/z37/set_K{K}.txt)"""
import sys
from sympy import factorint, jacobi_symbol as J, primerange
from math import isqrt
K, T = int(sys.argv[1]), int(sys.argv[2])
P = [int(l) for l in open(f'/tmp/z37/set_K{K}.txt') if l.strip()][:80]
PR = list(primerange(3, 400))
def LR(j):
    v = 1.0
    for r in PR:
        if j % r: v /= (1 - J(j % r, r) / r)
    if j % 8 == 1: v *= 2.0
    elif j % 8 == 5: v *= 2 / 3
    return v
def divisors(f):
    ds = [1]
    for q, e in f.items(): ds = [d * q ** k for d in ds for k in range(e + 1)]
    return ds
rows = []
for t in range(2, T + 1):
    j = t * K + 1
    acc = 0.0; cnt = 0
    for p in P:
        N = t * p + 1; lo, hi = 2 * t - 1, N // (2 * t - 1)
        ds = [d for d in divisors(factorint(N)) if lo <= d <= hi]
        if ds: acc += sum(J(d, p) for d in ds) / len(ds); cnt += 1
    if cnt: rows.append((t, j, isqrt(j) ** 2 == j, acc / cnt, LR(j)))
ns = [r for r in rows if not r[2]]
def rank(x):
    o = sorted(range(len(x)), key=lambda i: x[i]); r = [0] * len(x)
    for k, i in enumerate(o): r[i] = k
    return r
a, b = rank([r[3] for r in ns]), rank([r[4] for r in ns])
n = len(ns); ma, mb = sum(a) / n, sum(b) / n
rho = sum((x - ma) * (y - mb) for x, y in zip(a, b)) / (sum((x - ma) ** 2 for x in a) * sum((y - mb) ** 2 for y in b)) ** .5
sq = [r[3] for r in rows if r[2]]
print(f"K={K} family size {len(P)}, levels 2..{T}: square-j levels {len(sq)} mean bias {sum(sq)/max(1,len(sq)):.3f}; "
      f"non-square levels {n}: mean bias {sum(r[3] for r in ns)/n:.3f}; Spearman(bias, L_R(1,chi_j)) = {rho:.3f}")
top = sorted(ns, key=lambda r: -r[4])[:3]; bot = sorted(ns, key=lambda r: r[4])[:3]
print("  highest L:", [(r[0], r[1], round(r[3], 3), round(r[4], 2)) for r in top])
print("  lowest  L:", [(r[0], r[1], round(r[3], 3), round(r[4], 2)) for r in bot])
