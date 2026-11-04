"""z56 K4LIT — check of the density-adjusting weight in Lemma P (Z56_K4LIT.md §3).
w(m) = sum_{e | m, e <= E, e squarefree Q-composed} c_e,  c_e = prod_{q | e} c_q,  c_q = 1/(q-2)
should give, for squarefree Q-composed d,  sum_{m<=Y, m=3 (4), d|m} w(m) / sum_{m<=Y, m=3 (4)} w(m)  ->  g(d) = 1/phi(d)
(the local density of the shifted-prime sequences p+4, 4p+1).  EVIDENCE (finite Y, E).
Usage: uv run --with numpy python scripts/z56_k4lit_phiweight.py [Y=2e7] [E=2000]
"""
import sys
import numpy as np

Y = int(float(sys.argv[1])) if len(sys.argv) > 1 else 20_000_000
E = int(float(sys.argv[2])) if len(sys.argv) > 2 else 2000

sv = np.ones(E + 1, dtype=bool); sv[:2] = False
for p in range(2, int(E ** 0.5) + 1):
    if sv[p]:
        sv[p * p::p] = False
Q = [int(p) for p in np.nonzero(sv)[0] if p % 4 == 3]

# enumerate squarefree Q-composed e <= E with c_e
es = [(1, 1.0)]
for q in Q:
    es += [(e * q, c / (q - 2)) for (e, c) in es if e * q <= E]
w = np.zeros(Y + 1)
for e, c in es:
    w[e::e] += c
m = np.arange(Y + 1)
base = (m % 4 == 3)
tot = w[base].sum()
print(f"Y={Y}, E={E}, #e={len(es)}")
for d in [3, 7, 11, 19, 21, 33, 57, 231]:
    sel = base & (m % d == 0)
    ratio = w[sel].sum() / tot
    phi = 1
    for q in Q:
        if d % q == 0:
            phi *= (q - 1)
    print(f"d={d:4d}: ratio*phi(d) = {ratio*phi:.5f}   (ratio*d = {ratio*d:.5f})")
