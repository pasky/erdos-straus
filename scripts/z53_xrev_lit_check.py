#!/usr/bin/env python3
"""Independent, bounded z53 LIT audit (stdlib only).
Run: timeout 120s uv run python scripts/z53_xrev_lit_check.py CENSUS.tsv
The input is the 64,380-row census, not a large Cartesian-product array.
"""
import csv
import math
import sys
from fractions import Fraction


def primes_to(n):
    sieve = bytearray(b"\x01") * (n + 1)
    sieve[:2] = b"\x00\x00"
    for d in range(2, math.isqrt(n) + 1):
        if sieve[d]:
            sieve[d * d::d] = b"\x00" * ((n - d * d) // d + 1)
    return [d for d in range(2, n + 1) if sieve[d]]


def divisors(n, primes):
    out = [1]
    for ell in primes:
        if ell * ell > n:
            break
        if n % ell:
            continue
        old = out[:]
        power = 1
        while n % ell == 0:
            n //= ell
            power *= ell
            out.extend(d * power for d in old)
    if n > 1:
        out += [d * n for d in out]
    return out


def star_count(p, primes):
    # Symmetry u <-> B reduces to u <= B; then 4u^2 - 2u <= p.
    total = 0
    for u in range(1, (1 + math.isqrt(1 + 4 * p)) // 4 + 1):
        for d in divisors(p + u, primes):
            B = (p + u) // d
            if B >= u and (d + 1) % (4 * u) == 0:
                total += 1 if B == u else 2
    return total


def discrepancy(points):
    points = sorted(points)
    n = len(points)
    return max(max(Fraction(i + 1, n) - v, v - Fraction(i, n))
               for i, v in enumerate(points))


def main():
    with open(sys.argv[1]) as source:
        rows = list(csv.reader(source, delimiter="\t"))
    assert len(rows) == 64380
    maxp = max(int(row[0]) for row in rows)
    primes = primes_to(math.isqrt(2 * maxp) + 1)
    selected = sorted(set(range(10)) | set(range(len(rows) - 10, len(rows)))
                      | set(range(0, len(rows), 5000))
                      | {i for i, row in enumerate(rows) if row[1] == "0"})
    for i in selected:
        row = rows[i]
        p, count = map(int, row[:2])
        assert star_count(p, primes) == count, (p, count)
        N = int(math.log(p) ** 2)
        D = discrepancy([Fraction(pow(x, -1, p), p) for x in range(1, N + 1)])
        assert f"{float(D):.5f}" == row[2], (p, D, row[2])
    print(f"Independent divisor enumeration R and rational discrepancy D: {len(selected)} census rows agree")

    pairs = 0
    for p in primes_to(500):
        for x in range(1, p):
            xb = pow(x, -1, p)
            k = (x * xb - 1) // p
            assert 0 <= k < x and (p * k + 1) % x == 0
            assert Fraction(xb, p) == Fraction(k, x) + Fraction(1, x * p)
            if x % 4 == 3:
                actual = [(e, (x + 1) // e) for e in range(4, x + 2, 4)
                          if (x + 1) % e == 0 and (p + (x + 1) // e) % x == 0]
                farey = [e for e in range(4, x + 2, 4)
                         if (x + 1) % e == 0 and e % x == k]
                assert [e for e, u in actual] == farey
            pairs += 1
    print(f"L2 identity and Farey equivalence: {pairs} (p,x) pairs agree")
    for p in (5, 11):
        points = [Fraction(pow(x, -1, p), p) for x in (1, 2)]
        anchors = [Fraction((x * pow(x, -1, p) - 1) // p, x) for x in (1, 2)]
        print(f"N=2, p={p}, p mod lcm=1: anchors={anchors}, D={discrepancy(points)}")
        assert abs(discrepancy(points) - discrepancy(anchors)) <= Fraction(1, p)


if __name__ == "__main__":
    main()
