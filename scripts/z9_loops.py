"""Loops of G_p/Frob versus small vectors of the edge lattice L (det p).
For every edge L: loop?  r_L(1), r_L(2), r_L(4) (vectors up to sign), path?  Tabulate joint counts over primes."""
import sys
from collections import Counter
from sympy import isprime
from z9_graph import build
from z9_lib import key_to_gram, vectors_upto

lo, hi = int(sys.argv[1]), int(sys.argv[2])
tab = Counter()
for p in range(lo, hi + 1):
    if not isprime(p) or p % 4 != 1:
        continue
    verts, edges, path = build(p)
    for k, (a, b) in edges.items():
        G = key_to_gram(k)
        vs = vectors_upto(G, 4)
        r = Counter(q for q, x in vs)
        tab[(a == b, r[1] > 0, r[2] > 0, k in path)] += 1
print("loop has1 has2 path : count")
for key in sorted(tab):
    print(key, tab[key])
