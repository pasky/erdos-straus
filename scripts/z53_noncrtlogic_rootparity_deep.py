#!/usr/bin/env python3
"""Z53_NONCRTLOGIC -- root-colour test at DEEPLY square-mimicking primes: p = 1 (24) with (l/p) = +1 for every prime
l < LMIN (so n_p >= LMIN).  For prime roots l in [LMIN, LMAX] compare residue vs non-residue roots: P(edge at l),
P(bichromatic edge at l), split by whether the bichromatic edge is to the smaller neighbour (-p mod l) or to a larger one.
Usage: uv run --with sympy --with gmpy2 python scripts/z53_noncrtlogic_rootparity_deep.py A B LMIN LMAX NMAX
"""
import sys
import gmpy2
from sympy import factorint
sys.path.insert(0, 'scripts')
from z53_noncrtlogic_forestroot import neighbours, chi

A, B, LMIN, LMAX, NMAX = map(int, sys.argv[1:6])
small = [l for l in range(3, LMIN) if gmpy2.is_prime(l)]
ls = [l for l in range(LMIN, LMAX + 1) if gmpy2.is_prime(l)]
st = {s: [0, 0, 0, 0, 0, 0, 0] for s in (1, -1)}   # [#inst, edge, bichrom, via smaller, via larger, #(p+l has a QNR prime), via larger & that]
n = 0
for p in range(A + (1 - A) % 24, B, 24):
    if any(gmpy2.legendre(p % l, l) != 1 for l in small):
        continue
    if not gmpy2.is_prime(p):
        continue
    n += 1
    for l in ls:
        s = gmpy2.legendre(l, p)
        nb = neighbours(p, l)
        a = st[s]
        a[0] += 1
        a[1] += bool(nb)
        bi = [w for w in nb if chi(w, p) != s]
        a[2] += bool(bi)
        a[3] += any(w < l for w in bi)
        big = any(w > l for w in bi)
        a[4] += big
        nf1 = any(gmpy2.legendre(f, p) == -1 for f in factorint(p + l))
        a[5] += nf1
        a[6] += big and nf1
    if n >= NMAX:
        break
print(f"deep square-mimicking primes p=1(24) in [{A},{B}) with (l/p)=1 for all l<{LMIN}: {n} (last p={p})")
for s, name in ((1, 'QR '), (-1, 'QNR')):
    a = st[s]
    print(f"  roots {name} l in [{LMIN},{LMAX}]: inst={a[0]}  P(edge)={a[1]/a[0]:.3f}  P(bichrom)={a[2]/a[0]:.3f}  "
          f"P(b|e)={a[2]/max(1,a[1]):.3f}  P(bichrom via smaller nbr)={a[3]/a[0]:.3f}  P(bichrom via larger nbr)={a[4]/a[0]:.3f}  P(p+l has QNR prime)={a[5]/a[0]:.3f}  P(larger-bichrom | p+l has QNR prime)={a[6]/max(1,a[5]):.3f}")
