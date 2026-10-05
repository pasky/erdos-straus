#!/usr/bin/env python3
"""O24 (EXCEPTIONAL_TUPLES2.md §5): moment ratios S_j/(N e_j) on [t+1, t+N] for several t.
Single-form truncation (Cor 1.2) is a property of small integers (ns+r <= Ns+r); on a far
translate it disappears, so the ES deficit of [1,N] should vanish there.
usage: tuples2_translates.py N y t1,t2,... [Jmax]
"""
import sys
import numpy as np
from math import comb
from tuples_moments import primes_upto, R_set, esym

N = int(float(sys.argv[1])); y = int(float(sys.argv[2]))
ts = [int(float(t)) for t in sys.argv[3].split(',')]
J = int(sys.argv[4]) if len(sys.argv) > 4 else 13
P = [int(l) for l in primes_upto(y) if l % 4 == 3]
tabs = []
ps = []
for l in P:
    R = R_set(l); tb = np.zeros(l, dtype=np.int16); tb[R] = 1; tabs.append(tb); ps.append(len(R) / l)
e = esym(ps, J)
print(f"# N={N:.3g} y={y} mu={sum(ps):.4f}; columns: t, then S_j/(N e_j) for j=4,6,8,10,12")
for t in ts:
    ns = np.arange(t + 1, t + N + 1, dtype=np.int64)
    f = np.zeros(N, dtype=np.int16)
    for l, tb in zip(P, tabs):
        f += tb[ns % l]
    h = np.bincount(f)
    S = [sum(int(h[v]) * comb(v, j) for v in range(j, len(h))) / N for j in range(J + 1)]
    print(f"{t:.3e} " + " ".join(f"{S[j]/e[j]:.4f}" for j in (4, 6, 8, 10, 12)))
