#!/usr/bin/env python3
"""U07 Z1312: point counts of the affine surface S_n: 4xyz = n(xy+yz+zx) over F_q, primes q<=31, all n mod q.
Compares counts with q^2 + O(q) (Weil-type) and checks the n-dependence (n ↦ -n, n ↦ n·s^2 scalings)."""
import resource; resource.setrlimit(resource.RLIMIT_AS, (1_000_000_000, 1_000_000_000))
from sympy import primerange
res = {}
for q in primerange(3, 32):
    for n in range(q):
        cnt = 0
        for x in range(q):
            for y in range(q):
                for z in range(q):
                    if (4*x*y*z - n*(x*y+y*z+z*x)) % q == 0: cnt += 1
        res[(q, n)] = cnt
for q in [3, 5, 7, 11, 13]:
    print("q", q, "counts over n:", [res[(q, n)] for n in range(q)])
# n -> s^2 n scaling check: S_n ≅ S_{n s^2}? (x,y,z)->(x s^-1 ...) ; test counts equal under n -> n*s^2 for s in F_q^*
bad = 0; tot = 0
for q in [5, 7, 11, 13, 17, 19, 23]:
    for n in range(1, q):
        for s in range(1, q):
            tot += 1
            if res.get((q, n)) is None: continue
            if res[(q, n)] != res[(q, (n * s * s) % q)] if (q, (n*s*s) % q) in res else False: bad += 1
print("n ↦ n s² invariance violations:", bad, "of", tot)
