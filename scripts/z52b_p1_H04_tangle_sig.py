#!/usr/bin/env python3
"""Z1486: 2-bridge knot K(p/A) signature (Murasugi sum, A taken odd in (-p,p)) vs HJ length r(p/A), r(p/(p-A)) and the ES5 bit."""
import sys, collections
sys.path.insert(0, 'scripts')
from bsA_hjlen import hj_len
from sympy import primerange, jacobi_symbol
def sig(p, A):
    q = A if A % 2 else A - p
    return sum((-1) ** ((i * q) // p) for i in range(1, p))
rel = collections.defaultdict(set); tab = collections.Counter()
for p in primerange(5, 700):
    if p % 4 != 1: continue
    for A in range(1, p):
        r1, r2 = hj_len(p, A), hj_len(p, p - A); s = sig(p, A)
        rel[(r1, r2)].add(s)
        if r1 <= 3: tab[(r1, s, jacobi_symbol(A, p))] += 1
amb = {k: v for k, v in rel.items() if len(v) > 1}
print("pairs (r(p/A), r(p/(p-A))) observed:", len(rel), " with non-unique signature:", len(amb))
print("sample sig vs r1-r2:", sorted({(k[0]-k[1], s) for k, v in rel.items() for s in v})[:30])
print("length<=3 words: (r, sigma, (A/p)) counts:", sorted(tab.items()))
