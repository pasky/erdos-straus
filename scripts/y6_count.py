"""y6_count.py — growth of the number of k=1 cap-2 shots (W_n points, c odd, Thm 1.1 side conditions) with g <= G,
binned by decade of g, for a few n. Usage: y6_count.py G n1 n2 ..."""
import sys, numpy as np
from math import gcd, isqrt
G = int(sys.argv[1]); ns = list(map(int, sys.argv[2:]))
sqf = np.ones(G+2, bool)
for p in range(2, isqrt(G+1)+1): sqf[p*p::p*p] = False
A = []; Bs = []; Cs = []
for a in range(4, G+2, 4):
    for B in range(1, (G+1)//a + 1, 2):
        if not sqf[B]: continue
        cmax = (G+1)//(a*B)
        cs = np.arange(1, cmax+1, 2); cs = cs[sqf[cs]]
        cs = cs[np.gcd(cs, B) == 1]
        A.append(np.full(cs.size, a)); Bs.append(np.full(cs.size, B)); Cs.append(cs)
A = np.concatenate(A).astype(object); Bs = np.concatenate(Bs).astype(object); Cs = np.concatenate(Cs).astype(object)
g = Cs*A*Bs - 1
for n in ns:
    hit = ((4*n*A*A + Bs*Bs) % g == 0)
    ok = hit & np.array([gcd(int(x), n) == 1 for x in (Cs*A*Bs)[hit]]) if False else hit
    idx = np.nonzero(hit)[0]
    idx = [i for i in idx if gcd(int(Cs[i]*A[i]*Bs[i]), n) == 1]
    gs = np.array([int(g[i]) for i in idx]); bb = np.array([int(Bs[i]) for i in idx])
    dec = {d: int(((gs >= 10**d) & (gs < 10**(d+1))).sum()) for d in range(0, len(str(G)))}
    print(f"n={n}: shots with g<={G}: {len(gs)} (B>1: {int((bb>1).sum())}); by decade {dec}")
