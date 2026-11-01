"""Small exact helpers for the Pass-2 TO3 batch (solutions of m/N = 1/x+1/y+1/z, x<=y<=z)."""
from math import gcd
from sympy import factorint, divisors


def sols(m, N):
    """All unordered solutions x<=y<=z of m/N = 1/x+1/y+1/z in positive integers (exact)."""
    out = []
    for x in range(N // m + 1, 3 * N // m + 1):
        a = m * x - N
        if a <= 0:
            continue
        b = N * x
        g = gcd(a, b)
        A, B = a // g, b // g          # need 1/y+1/z = A/B
        # (A y - B)(A z - B) = B^2 ; d = A y - B divides B^2, d = -B mod A, y>=x
        for d in divisors(B * B):
            if (d + B) % A:
                continue
            y = (d + B) // A
            if y < x:
                continue
            e = (B * B) // d
            if (e + B) % A:
                continue
            z = (e + B) // A
            if y <= z:
                out.append((x, y, z))
    return sorted(set(out))


def is_sol(m, N, x, y, z):
    from fractions import Fraction
    return Fraction(m, N) == Fraction(1, x) + Fraction(1, y) + Fraction(1, z)
