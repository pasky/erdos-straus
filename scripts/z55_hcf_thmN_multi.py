#!/usr/bin/env python3
"""z55 HCF: direct test of Theorem 3.1' (multi-prime form): S = all primes in [11, Y], R = 2 (or 3),
p == 1 (mod 8 * prod_{l'<=Y, l' not in S} l'^a), p == R (mod l^J) for all l in S (l^J > R(C+1)).
Claim: every certificate divisor d (c <= C) has a prime factor > Y.
"""
import sys, random
from sympy import factorint, isprime, primerange

def certificate_divisors(p, c):
    out = []
    for line, N in (('U', p+c), ('T', c*p+1)):
        f = factorint(N)
        divs = [1]
        for q, a in f.items():
            divs = [d*q**i for d in divs for i in range(a+1)]
        for d in divs:
            if d % c == c-1:
                out.append((line, d, factorint(d)))
    return out

def run(Y, C, R, nprimes, seed=2):
    S = [l for l in primerange(11, Y+1)]
    P = [q for q in primerange(2, Y+1) if q not in S]
    mod = 1; res = 0
    congr = []
    for q in P:
        qa = 8 if q == 2 else q
        while qa <= C+1: qa *= q
        congr.append((1, qa))
    for l in S:
        lJ = l
        while lJ <= R*(C+1): lJ *= l
        congr.append((R, lJ))
    # CRT
    from sympy.ntheory.modular import crt
    res, mod = crt([m for _, m in congr], [r for r, _ in congr])
    rng = random.Random(seed)
    found = 0; checked = 0; bad = []; nrs = None
    while found < nprimes:
        p = int(res) + rng.randrange(1, 10**6) * int(mod)
        if not isprime(p): continue
        found += 1
        if nrs is None:
            nrs = [l for l in S if pow(p, (l-1)//2, l) == l-1]
        for c in range(3, C+1):
            if not (c % 4 == 0 or c % 8 == 7): continue
            for line, d, fd in certificate_divisors(p, c):
                checked += 1
                if max(fd) <= Y:
                    bad.append((p, c, line, d, fd))
    print(f'Y={Y} C={C} R={R} S={S} modulus~1e{len(str(mod))-1}: primes={found}, non-residue primes among S for them={nrs}, '
          f'certificate divisors checked={checked}, violations (d {Y}-smooth)={len(bad)} {bad[:3]}')

if __name__ == '__main__':
    run(Y=23, C=40, R=2, nprimes=10)
    run(Y=31, C=24, R=2, nprimes=10)
    run(Y=23, C=40, R=3, nprimes=10)
