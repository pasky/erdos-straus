"""Independent, bounded checks for the z54 BILINJAC hostile review.
Run: ulimit -v 6000000; timeout 120s uv run --with sympy python scripts/z54_xrev_bilinjac_check.py
No dense Fourier arrays: at most one strip and one q-by-q residue table.
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations
from math import isqrt, sqrt
import cmath

from sympy import divisors, isprime, primerange


def legendre(a, q):
    r = pow(a % q, (q - 1) // 2, q)
    return -1 if r == q - 1 else r


def jacobi_pair(a, q, r):
    return legendre(a, q) * legendre(a, r)


def block_count(n):
    # Independent fixed-n pair enumeration, not the census's triple sweep.
    top = isqrt(isqrt(16 * n))
    points = []
    for u in range(1, top + 1):
        if n >= 16 * u**4:
            continue
        for b in range(1, top + 1):
            if n >= 16 * b**4:
                continue
            c, rem = divmod(n + u + b, 4 * u * b)
            if c > 0 and rem == 0:
                points.append((u, b, c))
    return points


def strip_by_divisors(n, v, w):
    # F2 rather than the author's scan through C.
    points = []
    for m in range((n + 2 * v) // 4 + 1, (n + 4 * v) // 4 + 1):
        s = 4 * m - n
        for c in divisors(m):
            if w < c <= 2 * w:
                k = m // c
                points.append((c, k, s * s - 4 * k))
    return points


def strip_check(n, v, w, p):
    points = strip_by_divisors(n, v, w)
    mass = len(points)
    pairs = list(combinations(primerange(p + 1, 2 * p + 1), 2))[:300]
    sums = [sum(jacobi_pair(f, q, r) for c, k, f in points) for q, r in pairs]
    q = 61
    # Direct Fourier sums over the sparse points, independent of the C program's separable DFT.
    counts = Counter((c % q, k % q) for c, k, f in points)
    roots = [cmath.exp(2j * cmath.pi * t / q) for t in range(q)]
    tmax = max(abs(sum(h * roots[(a * c + b * k) % q] for (c, k), h in counts.items()))
               for a in range(q) for b in range(q) if a or b)
    print(f"strip n={n} A={mass} P={p} pairs={len(pairs)} "
          f"SQrms={sqrt(sum(s*s for s in sums)/len(sums)/mass):.2f} "
          f"SQmax={max(map(abs, sums))/sqrt(mass):.2f} Tmax={tmax/sqrt(mass):.2f}")


def main():
    for n, expected in [(635674641, 20), (250810249, 14), (10000600009, 0)]:
        points = block_count(n)
        assert len(points) == expected, (n, points)
        print(f"fixed-n count n={n}: {len(points)}, prime={isprime(n)}")

    cases = 0
    for q in primerange(3, 24):
        for n in range(q):
            total = sum(legendre((4*c*k-n)**2 - 4*k, q)
                        for c in range(q) for k in range(q))
            assert total == (1 if n % q else -(q - 1))
            cases += 1
    for q, r in [(3, 5), (5, 7), (7, 11)]:
        mod = q * r
        for n in range(mod):
            total = sum(jacobi_pair((4*c*k-n)**2 - 4*k, q, r)
                        for c in range(mod) for k in range(mod))
            expected = (1 if n % q else -(q-1)) * (1 if n % r else -(r-1))
            assert total == expected
            assert abs(total) < mod
            cases += 1
    print(f"complete residue means: {cases} cases passed")

    strip_check(10000000033, 316, 6250, 18)
    strip_check(10000600009, 316, 6250, 18)
    strip_check(100000000000031, 3162, 625000, 56)

    # The alleged F6 counterexample does NOT satisfy the third bracket condition.
    quotient = Fraction(15 + 3 + 6, 3 * 6)
    assert quotient == Fraction(4, 3)
    print(f"F6 alleged counterexample quotient: {quotient}, not an integer divisible by 4")
    assert Fraction(13, 84) + 2 * Fraction(55, 84) == Fraction(41, 28)
    assert 1 + 4 * Fraction(3, 8) + Fraction(11, 48) == Fraction(131, 48)
    print("exponent arithmetic: Bourgain 41/28; DFI Thm 2 131/48; TS square-root 5/24")
    # The claimed all-Q additive LS expression misses repeated frequencies.
    # A full [1,L^2]^2 box has L^4 unit weights; Q=1..L repeats T(0,0)=L^4.
    for ell in [10, 100, 1000]:
        lhs_zero = ell**9
        rhs_expression = (ell + ell)**4 * ell**4
        print(f"all-Q LS zero-frequency lower bound / claimed expression, L={ell}: "
              f"{Fraction(lhs_zero, rhs_expression)} (unbounded)")


if __name__ == "__main__":
    main()
