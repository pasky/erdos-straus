"""Finite-field box diagnostic; standard library, bounded storage per prime.
Run: uv run python scripts/z52d_p2_ZF0_Z2399_box.py
This measures the explicit point-supported representation, NOT minimal sheaf conductor.
"""
import json
from math import isqrt
from pathlib import Path


def divisors(n):
    lo = [d for d in range(1, isqrt(n) + 1) if n % d == 0]
    return sorted(set(lo + [n // d for d in lo]))


def prime(n):
    return n > 1 and all(n % d for d in range(2, isqrt(n) + 1))


rows = []
for q in [7, 11, 19, 31, 127, 1023, 4095, 65535, 942479, 999983]:
    if not prime(q):
        continue
    k = (q + 1) // 4
    box = {(-c * pow(j, -1, q)) % q for c in divisors(k) for j in divisors(k // c)}
    # Independent direct cube parametrization from FIXED_MODULUS_SHOTS 3.1.
    direct = {(-4 * c * c * d) % q for c in divisors(k) for d in divisors(k // c)}
    assert box == direct
    assert all(pow(r, (q - 1) // 2, q) == q - 1 for r in box)
    rows.append(dict(q=q, k=k, point_terms=len(box), prime_failure_density=(q-1-len(box))/(q-1)))
Path('data/z52b/pass2/ZF0/Z2399/box.json').write_text(json.dumps(rows, indent=2) + '\n')
print(json.dumps(rows))
