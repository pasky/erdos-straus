"""POINTWISE_BINARYFORM Lemma 2.2 check (Gaussian case): for M with 8 | M, a unit class
u0+i v0 mod M is of the form lambda*eps*alpha^2 (lambda in (Z/M)^*, eps in <i>, alpha a unit of
Z[i]/M) iff Q(u0,v0) = u0^2+v0^2 is a square unit mod M."""
import sys
from math import gcd
def run(M):
    mul = lambda x, y: ((x[0]*y[0]-x[1]*y[1]) % M, (x[0]*y[1]+x[1]*y[0]) % M)
    units = [(u, v) for u in range(M) for v in range(M) if gcd(u*u+v*v, M) == 1]
    H = {mul(a, a) for a in units}
    gens = [(l, 0) for l in range(1, M) if gcd(l, M) == 1] + [(0, 1)]
    while True:
        new = {mul(g, h) for g in gens for h in H} | H
        if new == H: break
        H = new
    sq = {(s*s) % M for s in range(M) if gcd(s, M) == 1}
    bad = [(u, v) for (u, v) in units if ((u, v) in H) != ((u*u+v*v) % M in sq)]
    return len(units), len(H), len(bad)
for M in map(int, sys.argv[1:]):
    print(M, *run(M))
