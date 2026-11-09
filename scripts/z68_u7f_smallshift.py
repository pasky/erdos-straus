#!/usr/bin/env python3
"""z68 U7F Lemma 2 check: for primes p = 1 (mod 8) up to N (and the Z7 composites), compare for each small-letter
family (z=1,2,3,4; y=2,4,8; x=8) the three statements:
  W: a U7 word with that letter exists (direct enumeration);
  D: the divisor condition of Lemma 2;
  F: the 'fails iff norm-form / subgroup' condition (negated).
Prints the number of mismatches (must be 0) and the count of primes failing all eight families.
usage: smallshift.py N
"""
import sys
import numpy as np

N = int(sys.argv[1]) if len(sys.argv) > 1 else 10**6
LIM = 8 * N + 10
spf = np.zeros(LIM + 1, dtype=np.int32)
for i in range(2, int(LIM**0.5) + 1):
    if spf[i] == 0:
        sl = spf[i*i::i]
        sl[sl == 0] = i
        spf[i*i::i] = sl
idx = np.arange(LIM + 1)
spf[spf == 0] = idx[spf == 0]
spf[0] = spf[1] = 1

def factor(m):
    out = {}
    while m > 1:
        q = int(spf[m]); e = 0
        while m % q == 0:
            m //= q; e += 1
        out[q] = e
    return out

def divisors(m):
    ds = [1]
    for q, e in factor(m).items():
        ds = [d * q**k for d in ds for k in range(e + 1)]
    return ds

def in_S(m, mod, H):
    """all prime factors of m lie in H (subset of residues mod `mod`)"""
    return all((q % mod) in H for q in factor(m))

def word_with_z(n, z):
    # pair (x,z): x | n+z, z | n+x, x+z = 7 mod 8
    return any(((n + x) % z == 0) and ((x + z) % 8 == 7) for x in divisors(n + z))

def word_with_y(n, y):
    L = 8 * y // np.gcd(8, y)
    return any(d % L == L - 1 and d < n * y + 1 for d in divisors(n * y + 1))

def word_with_x8(n):
    return any(f % 8 == 7 for f in divisors(n + 8))

def check(n):
    res = {}
    m = (n + 1) // 2
    res['z1'] = (word_with_z(n, 1), any(d % 4 == 3 for d in divisors(m)), not in_S(m, 4, {1}))
    res['z2'] = (word_with_z(n, 2), any(d % 8 == 5 for d in divisors(n + 2)), not in_S(n + 2, 8, {1, 3}))
    res['z4'] = (word_with_z(n, 4), any(d % 8 == 3 for d in divisors(n + 4)), not in_S(n + 4, 4, {1}))
    if n % 3 == 1:
        m3 = (n + 3) // 4
        res['z3'] = (word_with_z(n, 3), any(d % 3 == 2 for d in divisors(m3)), not in_S(m3, 3, {1}))
    res['y2'] = (word_with_y(n, 2), any(d % 8 == 7 for d in divisors(2 * n + 1)), not in_S(2 * n + 1, 8, {1, 3}))
    res['y4'] = (word_with_y(n, 4), any(d % 8 == 7 for d in divisors(4 * n + 1)), not in_S(4 * n + 1, 4, {1}))
    res['y8'] = (word_with_y(n, 8), any(d % 8 == 7 for d in divisors(8 * n + 1)),
                 not (in_S(8 * n + 1, 8, {1, 3}) or in_S(8 * n + 1, 8, {1, 5})))
    res['x8'] = (word_with_x8(n), any(d % 8 == 7 for d in divisors(n + 8)),
                 not (in_S(n + 8, 8, {1, 3}) or in_S(n + 8, 8, {1, 5})))
    return res

isprime = np.ones(N + 1, dtype=bool); isprime[:2] = False
for i in range(2, int(N**0.5) + 1):
    if isprime[i]: isprime[i*i::i] = False
primes = [p for p in range(17, N + 1, 8) if isprime[p]]

mism = 0; allfail = []
for p in primes:
    r = check(p)
    for k, (W, D, F) in r.items():
        if not (W == D == F):
            mism += 1; print("MISMATCH", p, k, W, D, F)
    if not any(v[0] for v in r.values()):
        allfail.append(p)
print(f"primes p=1(8) <= {N}: {len(primes)}; mismatches {mism}; failing all 8 small families: {len(allfail)}")
print("all-fail primes:", allfail[:60], "..." if len(allfail) > 60 else "")
Z7 = [105, 1465, 3865, 4545, 10305, 12145, 39361, 67425]
for n in Z7:
    r = check(n)
    print("Z7", n, {k: v[0] for k, v in r.items()}, "all False" if not any(v[0] for v in r.values()) else "!!")
