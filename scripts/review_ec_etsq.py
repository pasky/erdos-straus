#!/usr/bin/env python3
"""R185: own implementation of the 7 Elsholtz–Tao Prop 1.9 families (from the ET paper text, not mordell_lib); for every class of
total modulus <= MMAX check (a) primitivity gcd(r, M) = 1 and (b) r is NOT a square mod M (Mordell/Schinzel prediction)."""
import sys
from math import gcd
MMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 3000
def crt(r1, m1, r2, m2):
    g = gcd(m1, m2)
    if (r2 - r1) % g: return None
    l = m1 // g * m2
    t = ((r2 - r1) // g * pow(m1 // g, -1, m2 // g)) % (m2 // g)
    return (r1 + m1 * t) % l, l
classes = set()
R = range(1, MMAX + 1)
for a in R:
    for d in range(1, MMAX // (4 * a) + 1):
        q = 4 * a * d
        # I1: -f mod 4ad, f | 4a^2 d + 1
        N = 4 * a * a * d + 1
        for f in range(1, min(N, 10**7) + 1) if N <= 10**6 else []:
            if N % f == 0: classes.add(((-f) % q, q, 'I1'))
        # I4 / II1: -1/e and -e mod 4ab (b=d), e | a+b, (e,4ab)=1
        for e in range(1, a + d + 1):
            if (a + d) % e == 0 and gcd(e, q) == 1:
                classes.add(((-pow(e, -1, q)) % q, q, 'I4')); classes.add(((-e) % q, q, 'II1'))
for x in R:
    for y in range(1, MMAX // (4 * x) + 1):
        q = 4 * x * y
        for f in range(1, MMAX // q + 1):
            if gcd(q, f) != 1: continue
            # I2: -f mod 4ac ∩ -c/a mod f   (a=x, c=y)
            r = crt((-f) % q, q, (-y * pow(x, -1, f)) % f if f > 1 else 0, f)
            if r: classes.add((r[0], r[1], 'I2'))
            # I3: -f mod 4cd ∩ n^2 = -4c^2 d mod f   (c=x, d=y)
            for s in range(f):
                if (s * s + 4 * x * x * y) % f == 0:
                    r = crt((-f) % q, q, s, f)
                    if r: classes.add((r[0], r[1], 'I3'))
        # II3: -4a^2 d - e mod 4ade, (4ad, e) = 1   (a=x, d=y)
        for e in range(1, MMAX // q + 1):
            if gcd(q, e) == 1:
                classes.add(((-4 * x * x * y - e) % (q * e), q * e, 'II3'))
# II2: -4a^2 d mod f, 4ad | f+1
for f in range(3, MMAX + 1, 4):
    A = (f + 1) // 4
    for a in range(1, A + 1):
        if A % a: continue
        for d in range(1, A // a + 1):
            if (A // a) % d == 0: classes.add(((-4 * a * a * d) % f, f, 'II2'))
classes = {c for c in classes if c[1] <= MMAX}
sqcache = {}
bad_prim, bad_sq = [], []
for r, M, fam in classes:
    if gcd(r, M) != 1: bad_prim.append((r, M, fam))
    if M not in sqcache: sqcache[M] = {s * s % M for s in range(M)}
    if r in sqcache[M]: bad_sq.append((r, M, fam))
print('classes:', len(classes), 'non-primitive:', bad_prim[:10], len(bad_prim), ' square residues:', bad_sq[:10], len(bad_sq))
