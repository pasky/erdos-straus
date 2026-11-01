#!/usr/bin/env python3
"""Z53_NONCRTLOGIC -- does the quadratic character of a forest root matter?  For every Mordell-hard prime p in [A, B) and
every prime root l in [5, LMAX], test whether l has a bichromatic edge to a direct neighbour in F_p (a five-slice
certificate through l), and aggregate the rate by (l, (l/p)).  The same l is compared as a residue and as a non-residue,
so size and divisor-structure effects of l cancel.  Also: P(edge exists at all) by status.
Usage: uv run --with sympy --with gmpy2 python scripts/z53_noncrtlogic_rootparity.py A B LMAX
"""
import sys
import gmpy2
sys.path.insert(0, 'scripts')
from z53_noncrtlogic_forestroot import neighbours, chi

A, B, LMAX = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
ls = [l for l in range(5, LMAX + 1) if gmpy2.is_prime(l)]
st = {(l, s): [0, 0, 0] for l in ls for s in (1, -1)}   # [#p, #edge exists, #bichromatic]
n = 0
for p in range(A + (1 - A) % 24, B, 24):
    if p % 840 not in (1, 121, 169, 289, 361, 529) or not gmpy2.is_prime(p):
        continue
    n += 1
    for l in ls:
        s = gmpy2.legendre(l, p)
        nb = neighbours(p, l)
        a = st[(l, s)]
        a[0] += 1
        a[1] += bool(nb)
        a[2] += any(chi(w, p) != s for w in nb)
print(f"Mordell-hard primes in [{A},{B}): {n}")
print("  l | as QR: #p  P(edge) P(bichrom) | as QNR: #p  P(edge) P(bichrom)")
tq = [0, 0, 0]; tn = [0, 0, 0]
for l in ls:
    q, r = st[(l, 1)], st[(l, -1)]
    for i in range(3):
        tq[i] += q[i]; tn[i] += r[i]
    print(f"{l:3d} | {q[0]:6d} {q[1]/max(1,q[0]):.3f} {q[2]/max(1,q[0]):.3f} | {r[0]:6d} {r[1]/max(1,r[0]):.3f} {r[2]/max(1,r[0]):.3f}")
print(f"all | {tq[0]:6d} {tq[1]/tq[0]:.3f} {tq[2]/tq[0]:.3f} | {tn[0]:6d} {tn[1]/tn[0]:.3f} {tn[2]/tn[0]:.3f}")
tq = [0, 0, 0]; tn = [0, 0, 0]
for l in ls:
    if l < 11:
        continue
    q, r = st[(l, 1)], st[(l, -1)]
    for i in range(3):
        tq[i] += q[i]; tn[i] += r[i]
print(f"l>=11 | QR: n={tq[0]} P(edge)={tq[1]/tq[0]:.3f} P(bichrom)={tq[2]/tq[0]:.3f} P(b|e)={tq[2]/tq[1]:.3f} | "
      f"QNR: n={tn[0]} P(edge)={tn[1]/tn[0]:.3f} P(bichrom)={tn[2]/tn[0]:.3f} P(b|e)={tn[2]/tn[1]:.3f}")
