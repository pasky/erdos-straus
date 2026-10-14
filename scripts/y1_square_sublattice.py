"""y1_square_sublattice (O209): for n = q^2 (q odd prime) every path lattice L_w is an index-q sublattice ker(f mod q)
of Z^3 (y1_hurwitz_lift H2).  Which f in P^2(F_q)?  Report whether f.f = 0 mod q (f on the conic) for each word."""
import sys
from collections import Counter
from cf_lib import words
from y1_z3_gram import vecs, dot


def embed(t, u, v):
    for b in vecs(t):
        for a in vecs(v):
            if dot(a, b) != -1:
                continue
            for c in vecs(u):
                if dot(c, b) == -1 and dot(a, c) == 0:
                    return a, b, c
    return None


def cross(x, y):
    return (x[1] * y[2] - x[2] * y[1], x[2] * y[0] - x[0] * y[2], x[0] * y[1] - x[1] * y[0])


for q in map(int, sys.argv[1:]):
    C = Counter()
    for (t, u, v) in words(q * q):
        a, b, c = embed(t, u, v)
        f = cross(a, b)  # f.a = f.b = 0; need f.c = 0 mod q as well
        assert dot(f, c) % q == 0 or True
        # functional killing M = <a,b,c>: solve f with f.a=f.b=f.c=0 mod q: f = cross(a,b) mod q works iff det = +-q
        g = [x % q for x in f]
        if dot(g, c) % q:
            C['bad'] += 1
            continue
        C['iso' if dot(g, g) % q == 0 else 'aniso'] += 1
    print('q', q, dict(C))
