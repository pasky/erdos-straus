"""Prop 3.1 check: for L = L_w (det p), E0 = adj(G): #{x in E0 : nrd x = tp} = r_L(t) for t <= T."""
import sys
from ce_classes import short_vectors
from ce_rank import adj
from cf_lib import words
from sympy import primerange
bad = tot = 0
for p in primerange(5, 400):
    for (t, u, v) in words(p)[:6]:
        G = [[v, -1, 0], [-1, t, -1], [0, -1, u]]
        T = 12
        rL = {}
        for q, x in short_vectors(G, T):
            rL[q] = rL.get(q, 0) + 1
        rE = {}
        for q, x in short_vectors(adj(G), T * p):
            if q % p == 0:
                rE[q // p] = rE.get(q // p, 0) + 1
        tot += 1
        if rL != rE:
            bad += 1; print('BAD', p, (t, u, v), rL, rE)
print('lattices', tot, 'bad', bad)
