#!/usr/bin/env python3
"""Audit the new arbitrary-witness extraction, reusing the existing full census.

No new CT test: pointwise_size_ct_check.py already tests prime-factor CT.
This checks the stronger, factor-free output and the denominator-height correction.
Run with a shell memory limit and timeout; only one prime's solutions are retained.
"""
import json
from math import gcd
from pathlib import Path

from sympy import primerange
from pointwise_size_ct_check import solutions


def extract(p, triple):
    """Only division, gcd, and modular powering; no factorization."""
    divisible = [x // p for x in triple if x % p == 0]
    free = [x for x in triple if x % p]
    pair = free if len(divisible) == 1 else divisible
    assert len(pair) == 2
    g = gcd(*pair)
    a, b = (x // g for x in pair)
    assert pow(a * b, (p - 1) // 2, p) == p - 1
    out = a if pow(a, (p - 1) // 2, p) == p - 1 else b
    assert pow(out, (p - 1) // 2, p) == p - 1
    other = divisible[0] if len(divisible) == 1 else free[0]
    assert other % (a * b) == 0
    c = other // (a * b)
    assert g % c == 0
    k = g // c
    if len(divisible) == 1:
        assert k * (4 * a * b * c - 1) == p * (a + b)
    else:
        assert k * (4 * a * b * c - p) == a + b
    return len(divisible), out, (a, b, c, k)


def main():
    primes = sorted(set(p for p in primerange(5, 1001) if p % 4 == 1)
                    | {1201, 193, 409, 577, 2521, 3361})
    counts = {"I": 0, "II": 0}
    raw_pair_checks = 0
    fixtures = {}
    free_residue_example = None
    for p in primes:
        sols = solutions(p)
        assert sols
        best = None
        for s in sols:
            x, y, z = s
            assert 4 * x * y * z == p * (x * y + x * z + y * z)
            typ, qnr, pars = extract(p, s)
            counts["I" if typ == 1 else "II"] += 1
            # The two denominators with the same p-divisibility have opposite signs
            # after removing their p factors. This is stronger than prime-factor CT.
            pair = [w for w in s if w % p] if typ == 1 else [w // p for w in s if w % p == 0]
            assert pow(pair[0] * pair[1], (p - 1) // 2, p) == p - 1
            raw_pair_checks += 1
            assert p * qnr <= max(s)
            assert 4 * max(s) ** 2 > p ** 3
            if typ == 1:
                pd = next(w for w in s if w % p == 0)
                assert 4 * pd >= p * (p + 1)
            if free_residue_example is None:
                qrfree = [w for w in s if w % p and pow(w, (p - 1) // 2, p) == 1]
                if qrfree:
                    free_residue_example = {"p": p, "solution": s, "QR_pfree": qrfree[0], "extracted_QNR": qnr}
            if best is None or max(s) < max(best[0]):
                best = (s, qnr, pars)
        if p in {193, 409, 577, 1201, 2521, 3361}:
            fixtures[str(p)] = {"solutions": len(sols), "minimum_max_denominator": max(best[0]),
                                "solution": best[0], "extracted_QNR": best[1], "parameters": best[2]}
    report = {"prime_count": len(primes), "solutions_by_type": counts,
              "factor_free_pair_checks": raw_pair_checks, "violations": 0,
              "QR_pfree_example": free_residue_example, "fixtures": fixtures}
    path = Path("data/z47_hardness_map/check.json")
    path.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
