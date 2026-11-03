#!/usr/bin/env python3
"""Independent, bounded checks for the z55 HCF review.

Complements the lane scripts: all (also composite) L in the central exclusion
algebra, and the previously untested T-line / odd-c prime-cofactor criterion.
Run: ulimit -v 6000000; timeout 120s uv run --with sympy python scripts/z55_xrev_hcf_check.py
"""
from sympy import divisors, factorint, jacobi_symbol, primerange


def core_check():
    counts = {"U": 0, "T": 0}
    for c in range(3, 5001):
        known_divisors = divisors(c + 1)
        for r in range(1, 13):
            for line, n in (("U", c + r), ("T", r * c + 1)):
                for ell in divisors(n):
                    if ell <= 3 * r + 1:
                        continue
                    for s in known_divisors:
                        counts[line] += 1
                        assert (ell * s + 1) % c, (line, c, r, ell, s)
    print("Core algebra: c=3..5000, R=1..12, all L>3R+1; checks", counts)


def cofactor_check():
    counts = {"U": 0, "T": 0}
    for p in primerange(17, 10000):
        if p % 8 != 1:
            continue
        for c in range(7, min(p, 65), 8):
            for line, n in (("U", p + c), ("T", c * p + 1)):
                actual = any(d % c == c - 1 for d in divisors(n))
                for q, exponent in factorint(n).items():
                    if exponent != 1:
                        continue
                    s = n // q
                    predicted = any(d % c == c - 1 or
                                    (line == "U" and (d + p) % c == 0)
                                    for d in divisors(s))
                    counts[line] += 1
                    assert actual == predicted, (line, p, c, q)
    print("Odd-c prime cofactor, p<10000: checks", counts)
    for c, p in ((23, 73), (31, 41), (39, 73), (47, 73)):
        numbers = (p + c, c * p + 1)
        assert not any(d % c == c - 1 for n in numbers for d in divisors(n))
        assert any(q != 2 and jacobi_symbol(q, c) == -1
                   for n in numbers for q in factorint(n))
    print("Four claimed larger-c counterexamples: confirmed")


if __name__ == "__main__":
    core_check()
    cofactor_check()
    print("All independent checks passed")
