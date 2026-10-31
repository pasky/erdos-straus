#!/usr/bin/env python3
"""U07 Z1590/Z1604. Z1590: C-form check: prime p ≡ 1 mod 4, p ≤ 10^4: does some C ≤ 50 have a divisor d of 4Cp+1 with d ≡ −1 (mod 4C)?
Lists failures. Z1604: table for p=409: 4C·409+1 factorisation and residue mod 4C for C ≤ 12."""
import resource; resource.setrlimit(resource.RLIMIT_AS, (1_000_000_000, 1_000_000_000))
from sympy import primerange, factorint, divisors
fails = []
for p in primerange(5, 10001):
    if p % 4 != 1: continue
    ok = False
    for C in range(1, 51):
        N = 4 * C * p + 1
        # divisor d ≡ -1 mod 4C (d may be composite); check all divisors (N small)
        if any(d % (4 * C) == (4 * C - 1) for d in divisors(N)):
            ok = True; break
    if not ok: fails.append(p)
print("C-form failures (C<=50, p≡1 mod 4, p<=10^4):", fails)
p = 409
for C in range(1, 13):
    N = 4 * C * p + 1
    print("C=%d N=%d factors=%s  mod 4C=%d" % (C, N, factorint(N), N % (4 * C)), end=" | ")
    cands = [d for d in divisors(N) if d % (4 * C) == (4 * C - 1)]
    print("divisors ≡ -1 mod 4C:", cands[:3])
