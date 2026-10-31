#!/usr/bin/env python3
"""Z1488: (*) zero-rates on families n = k m^2, k m^4 vs matched controls (same n mod 840, same size window);
quartic symbols on (*) prime failures. Needs /tmp/h04_R.bin from z52b_p1_H04_rstar.c (N = 2e7)."""
import numpy as np, math
from sympy import isprime, primerange
R = np.fromfile('/tmp/h04_R.bin', dtype=np.uint16); N = len(R) - 1
assert R[409] == 0 and R[13] > 0
n_all = np.arange(N + 1)
sq = np.zeros(N + 1, bool); s = np.arange(1, int(math.isqrt(N)) + 1); sq[s * s] = True
def ctrl_rate(ns):
    """zero rate of matched controls: for each n, the 200 odd non-square n' near n in same class mod 840"""
    z = t = 0
    for n in ns:
        lo = max(1, n - 840 * 200); cand = np.arange(lo + ((n - lo) % 840), min(N, n + 840 * 200), 840)
        cand = cand[~sq[cand]]; z += (R[cand] == 0).sum(); t += len(cand)
    return z / max(t, 1)
print("k  family  #n(≡1 mod 4, >1e4)  zero-rate  control-rate")
for power in (2, 4):
    for k in range(2, 51):
        if math.isqrt(k) ** 2 == k: continue
        ns = [k * m ** power for m in range(1, int((N / k) ** (1 / power)) + 1)]
        ns = [n for n in ns if n % 4 == 1 and n > 10 ** 4 and n <= N]
        if len(ns) < 20: continue
        ns = ns[::max(1, len(ns) // 300)]
        zr = float((R[ns] == 0).mean()); cr = ctrl_rate(ns)
        flag = " <<<" if zr > 3 * cr + 0.01 else ""
        print(f"{k:3d} m^{power} {len(ns):5d}  {zr:.4f}  {cr:.4f}{flag}")
fails = [p for p in primerange(5, N) if p % 4 == 1 and R[p] == 0]
print("(*) prime failures <=", N, ":", fails)
def q4(a, p):  # quartic residue symbol of a mod p, p ≡ 1 mod 4: a^((p-1)/4) mod p in {1,-1,±i}
    v = pow(a, (p - 1) // 4, p); return {1: '1', p - 1: '-1'}.get(v, 'i')
for p in fails:
    print(p, p % 8, "(2/p)_4", q4(2, p), "(-1/p)_4", q4(p - 1, p), "(3/p)_4", q4(3, p))
