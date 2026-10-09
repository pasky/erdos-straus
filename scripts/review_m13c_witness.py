#!/usr/bin/env python3
"""R100: brute-force check of the completeness claim of m13c_witness.witness_all (POINTWISE_MORDELL13C §2).

Own enumeration of ALL ET Prop 1.9 parameter tuples whose class modulus divides L (no size cap; the
parameters are bounded by divisibility), own class residues (CRT done here), then for every unit x mod L
compare the witness set {(fam, P)} with the author's engine (run as the object under test).
Usage: review_m13c_witness.py L [L ...]
"""
import sys
from math import gcd
from collections import defaultdict

def divisors(n):
    ds = []; i = 1
    while i * i <= n:
        if n % i == 0:
            ds.append(i)
            if i * i != n: ds.append(n // i)
        i += 1
    return sorted(ds)

def classes(L):
    """yield (fam, P, M, residues)"""
    out = []
    Q = L // 4 if L % 4 == 0 else None
    DL = divisors(L)
    if Q:
        DQ = divisors(Q)
        for u in DQ:                     # u = a*d (or a*c, c*d, a*b) with 4u | L
            for a in divisors(u):
                d = u // a; m = 4 * u
                # I1 (a,d,f)
                for f in divisors(4*a*a*d + 1):
                    out.append(("I1", (a, d, f), m, {(-f) % m}))
                # I4, II1 (a,b,e) with b = d
                b = d
                for e in divisors(a + b):
                    if gcd(e, m) == 1:
                        out.append(("I4", (a, b, e), m, {(-pow(e, -1, m)) % m}))
                        out.append(("II1", (a, b, e), m, {(-e) % m}))
                for f in divisors(L // m):
                    if gcd(f, m) != 1: continue
                    M = m * f
                    # I2 (a,c,f) with c = d ; class: x = -f (m), a x = -c (f)
                    c = d
                    res = {x for x in range(0, M, 1) if False}
                    R = [x for x in range((-f) % m, M, m) if (a*x + c) % f == 0]
                    out.append(("I2", (a, c, f), M, set(R)))
                    # I3 (c,d,f) with (c,d) = (a,d)
                    cc = a
                    R = [x for x in range((-f) % m, M, m) if (x*x + 4*cc*cc*d) % f == 0]
                    if R: out.append(("I3", (cc, d, f), M, set(R)))
                    # II3 (a,d,e) with e = f
                    out.append(("II3", (a, d, f), M, {(-4*a*a*d - f) % M}))
    for f in DL:                          # II2 (a,d,f): modulus f, 4ad | f+1
        if (f + 1) % 4: continue
        for u in divisors((f + 1) // 4):
            for a in divisors(u):
                d = u // a
                out.append(("II2", (a, d, f), f, {(-4*a*a*d) % f}))
    return out

def main(L):
    sys.path.insert(0, "scripts")
    from m13c_witness import witness_all
    W = defaultdict(set)
    cl = classes(L)
    for fam, P, M, res in cl:
        assert L % M == 0
        for r in res:
            for x in range(r, L, M):
                if gcd(x, L) == 1: W[x].add((fam, tuple(P)))
    mism = 0; nunits = 0; tot = 0
    for x in range(1, L):
        if gcd(x, L) != 1: continue
        nunits += 1
        A = {(f, tuple(P)) for f, P in witness_all(x, L, first=False)}
        tot += len(W[x])
        if A != W[x]:
            mism += 1
            if mism <= 5: print("MISMATCH", x, "author-only", sorted(A - W[x])[:5], "brute-only", sorted(W[x] - A)[:5])
    print(f"L={L}: {len(cl)} classes, {nunits} units, {tot} witness incidences, mismatches {mism}")

if __name__ == "__main__":
    for L in map(int, sys.argv[1:]): main(L)
