#!/usr/bin/env python3
"""z69 IDEAB Phase-1 sanity checks (small, pure python).
 A. brute-force all solutions of 4/p for primes p==1 (4), p<PMAX; classify Type I / II.
 B. verify the special families F1, F2, R8(d=1), R6 (HJ continued fraction) produce genuine solutions and
    that 'some Type II solution exists' <=> 'K2 hit exists'.
 C. parity table for idea I5.
"""
import sys
from fractions import Fraction as Fr
from sympy import primerange, factorint
from collections import Counter

PMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 1500

def divisors_from(f):
    ds = [1]
    for q, e in f.items():
        ds = [d * q**i for d in ds for i in range(e + 1)]
    return ds

def all_solutions(p):
    sols = set()
    for x in range(p // 4 + 1, 3 * p // 4 + 1):
        e = 4 * x - p
        N = p * x
        f = factorint(x); f = {q: 2 * k for q, k in f.items()}
        if x % p == 0: continue
        f[p] = f.get(p, 0) + 2
        for u in divisors_from(f):
            if u > N: continue
            if (N + u) % e: continue
            v = N * N // u
            if (N + v) % e: continue
            y, z = (N + u) // e, (N + v) // e
            t = tuple(sorted((x, y, z)))
            if t[0] == x: sols.add(t)
    return sols

def k2_hit(p, kmax):
    # Type II <=> exists k, ad | k with p == -4a^2 d mod (4k-1)
    for k in range(1, kmax + 1):
        u = 4 * k - 1
        for a in range(1, k + 1):
            if k % a: continue
            for d in range(1, k // a + 1):
                if (k // a) % d: continue
                if (p + 4 * a * a * d) % u == 0: return (k, a, d)
    return None

def check(p, x, y, z): return Fr(1, x) + Fr(1, y) + Fr(1, z) == Fr(4, p)

par = Counter(); bad = 0; rows = []
for p in primerange(5, PMAX):
    if p % 4 != 1: continue
    S = all_solutions(p)
    assert all(check(p, *t) for t in S)
    t1 = sum(1 for t in S if sum(1 for w in t if w % p == 0) == 1)
    t2 = sum(1 for t in S if sum(1 for w in t if w % p == 0) == 2)
    assert t1 + t2 == len(S), (p, S)
    # F2: (-p mod (4k-1)) | k  -> a = that residue, d = k/a, b = (p+a)/(4k-1)
    nF2 = 0
    for k in range(1, (p + 3) // 2):
        u = 4 * k - 1; a = (-p) % u
        if a and k % a == 0:
            d = k // a; b = (p + a) // u
            assert check(p, a * b * d, a * d * p, b * d * p); nF2 += 1   # c = 1
    # F1: (-p mod 4q) | q+1 -> e, c=(q+1)/e, d=(p+e)/(4q)   (a=q,b=1)
    nF1 = 0
    for q in range(1, p + 2):
        e = (-p) % (4 * q)
        if e and (q + 1) % e == 0:
            c = (q + 1) // e; d = (p + e) // (4 * q)
            assert check(p, q * d, q * c * d * p, c * d * p); nF1 += 1
    # R8 d=1: (4ac-1) | p+4a^2 ; e=(p+4a^2)/f ; b=(e+p)/(4a)
    nR8 = 0
    for a in range(1, p + 1):
        for c in range(1, (p + 4 * a * a + 1) // (4 * a) + 1):
            f = 4 * a * c - 1
            if (p + 4 * a * a) % f == 0:
                e = (p + 4 * a * a) // f; b, r = divmod(e + p, 4 * a); assert r == 0
                assert (a + b) == c * e and check(p, a * b, a * c * p, b * c * p); nR8 += 1
    # R6: p/u = a - 1/(4d - 1/b) with u = 4db-1  <=> c=1 solutions; recount via continued fraction identity
    nR6 = 0
    for u in range(3, 4 * p, 4):
        # minus continued fraction p/u = a - 1/(m - 1/b), entries >= 1 allowed (trailing 1 permitted)
        a = -(-p // u); r1 = a * u - p            # p/u = a - r1/u
        if r1 == 0: continue
        m = u // r1 + 1; r2 = m * r1 - u          # u/r1 = m - r2/r1 with 1 <= r2 <= r1
        if r2 == 1 and m % 4 == 0:                # r1/r2 = b integer -> length 3, middle term 4d
            b = r1; d = m // 4
            assert 4 * a * b * d - a - b == p; nR6 += 1
    k2 = k2_hit(p, 400)
    if (t2 > 0) != (k2 is not None): bad += 1
    rows.append((p, len(S), t1, t2, nF1, nF2, nR8, nR6))
    par[(len(S) % 2, t1 % 2, t2 % 2, (nF2 // 2) % 2, (nR8 // 2) % 2, p % 8)] += 1
print("primes checked:", len(rows), " TypeII<=>K2 mismatches:", bad)
print("p, #sol, #I, #II, #F1, #F2(ordered c=1), #R8(d=1), #R6   [first 12 and six-class rows]")
for r in rows[:12]: print(r)
for r in rows:
    if r[0] % 840 in (1, 121, 169, 289, 361, 529): print("six-class", r)
print("zeros: F1", [r[0] for r in rows if r[4] == 0], " F2", [r[0] for r in rows if r[5] == 0], " R8", [r[0] for r in rows if r[6] == 0])
print("F2 == R6 count for all p:", all(r[5] == r[7] for r in rows))
print("F2 and R8 ordered counts always even:", all(r[5] % 2 == 0 and r[6] % 2 == 0 for r in rows))
print("parity classes (total, I, II, F2/2, R8/2, p mod 8) -> #primes:")
for k, v in sorted(par.items()): print(k, v)
