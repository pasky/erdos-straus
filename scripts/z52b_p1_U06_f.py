#!/usr/bin/env python3
"""z52b pass1 U06 — Z3132 follow-up: Legendre symbol (d/p) of certificate divisors d | 4Cp+1, d = -1 (mod 4C).
Tabulates (d/p) by primality of d, over all primes p = 1 (4) <= 3000 and C <= 60."""
import json
from collections import Counter
exec(open("scripts/z52b_p1_U06_a.py").read().split("# ---------- Z0769")[0])
def is_prime(n):
    if n < 2: return False
    return all(n % q for q in range(2, int(n ** 0.5) + 1))
tab = Counter()
for p in [q for q in sieve(3000) if q % 4 == 1]:
    for C in range(1, 61):
        N = 4 * C * p + 1
        for dv in divisors(factor(N)):
            if dv > 1 and dv % (4 * C) == 4 * C - 1:
                leg = 1 if pow(dv % p, (p - 1) // 2, p) == 1 else -1
                tab[("prime" if is_prime(dv) else "composite", leg)] += 1
print(dict(tab))
json.dump({f"{k[0]}_{k[1]}": v for k, v in tab.items()}, open("data/z52b/pass1/U06/z3132_legendre_divisors.json", "w"), indent=1)
