# Z2807: "twisted parity" psi(n) = (n/p).  (i) generic sequence: weight w = 1 + psi preserves sieve axioms
# |A_d^w| = |A_d| (1 + small) for d <= D (Burgess regime); (ii) on ES words p = mcs - c - s (A = ms - 1) psi(A) is a
# function of (c,m,s) mod 8 (CHI_FLIP Cor 1.2), so 1 + psi = 2*1[cell], violating the axioms at modulus 8.
import numpy as np, sys, json
from sympy import isprime, legendre_symbol, primerange
out = {}
# (i) generic: A = {n <= x}, x = p/4, levels d <= D
for p in [1000081, 10000537]:          # primes = 1 (mod 24)
    assert isprime(p) and p % 24 == 1
    x = p // 4
    n = np.arange(1, x + 1, dtype=np.int64)
    # Legendre symbol via Euler criterion, vectorised in chunks
    psi = np.empty(x, dtype=np.int8)
    for s in range(0, x, 1 << 20):
        blk = n[s:s + (1 << 20)]
        e = np.array([pow(int(v), (p - 1) // 2, p) for v in blk], dtype=np.int64)
        psi[s:s + len(blk)] = np.where(e == 1, 1, -1)
    cs = np.cumsum(psi.astype(np.int64))
    res = {}
    for D in [10, 100, 1000, 10000]:
        worst = 0.0
        for d in range(1, D + 1):
            Ad = x // d
            tw = int(psi[d - 1::d].astype(np.int64).sum())   # sum_{n<=x, d|n} psi(n)
            worst = max(worst, abs(tw) / Ad)
        res[D] = round(worst, 4)
    out[f"generic_p{p}"] = {"x": x, "max_{d<=D} |sum_{d|n} psi(n)| / |A_d|": res}
    print(p, res)
# (ii) words: sign constant on cells mod 8?
cells = {}
viol = 0; nw = 0
for p in primerange(10**5, 10**5 + 20000):
    if p % 8 != 1: continue
    for s in range(2, p):
        if 2 * s - 1 > p: break
        m = 2
        while True:
            A = m * s - 1
            if 2 * A > p + s: break
            if (p + s) % A == 0:
                c = (p + s) // A
                if c >= 2:
                    key = (c % 8, m % 8, s % 8)
                    sg = legendre_symbol(A % p, p)
                    nw += 1
                    if key in cells and cells[key] != sg: viol += 1
                    cells.setdefault(key, sg)
            m += 1
neg = sum(1 for v in cells.values() if v == -1)
out["words"] = {"primes": "p = 1 (8) in [1e5, 1.2e5]", "n_words": nw, "cells_seen": len(cells), "cells_sign_-1": neg, "violations_of_cell_constancy": viol}
print(out["words"])
json.dump(out, open(sys.argv[1], "w"), indent=1)
