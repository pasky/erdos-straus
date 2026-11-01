#!/usr/bin/env python3
"""Z53_NONCRTLOGIC -- deterministic re-check of the primality inputs of (F1)/(F2) below 2^64.
sympy.isprime is definitive for n < 2^64 (deterministic Miller-Rabin bases / BPSW, no pseudoprimes below 2^64).
(F2): every admissible t of the Gaussian toy (t < TMAX): t, 120t+1, 60t+1, 3600t^2+1, (120t)^2+1 all < 2^64 -> re-checked.
(F1): for the families whose values stay below 2^64 at q = 120120*t, t <= T, re-check that the gmpy2-accepted p are prime.
Usage: uv run --with sympy --with gmpy2 python scripts/z53_noncrtlogic_primecert.py TMAX T
"""
import sys
import gmpy2
from sympy import isprime, primerange

TMAX, T = int(sys.argv[1]), int(sys.argv[2])
B64 = 2 ** 64
adm = 0
bad = 0
for t in primerange(7, TMAX):
    q = 120 * t
    vals = [q * q + 1, 120 * t + 1, 60 * t + 1, 3600 * t * t + 1]
    if all(gmpy2.is_prime(v) for v in vals):
        adm += 1
        assert max(vals) < B64
        if not (isprime(t) and all(isprime(v) for v in vals)):
            bad += 1
print(f"(F2) admissible t < {TMAX}: {adm}; all values < 2^64; deterministic re-check failures: {bad}")
fams = {'X^2+1': lambda q: q * q + 1, '2X^2+1': lambda q: 2 * q * q + 1, '3X^2+1': lambda q: 3 * q * q + 1,
        'X^2-X+1': lambda q: q * q - q + 1, 'X+1': lambda q: q + 1, 'X^2-3X+1': lambda q: q * q - 3 * q + 1}
for name, f in fams.items():
    n = 0
    nb = 0
    big = 0
    for t in range(1, T + 1):
        for q in (120120 * t, 120120 * t + 4 * 15015, 120120 * t + 24):
            p = f(q)
            if gmpy2.is_prime(p):
                if p >= B64:
                    big += 1
                    continue
                n += 1
                nb += not isprime(p)
    print(f"(F1) {name}: gmpy2-accepted values < 2^64 re-checked {n}, failures {nb}, values >= 2^64: {big}")
