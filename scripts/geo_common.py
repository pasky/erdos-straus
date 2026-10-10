"""Common helpers for the GEOMETRY_ES (O126) scripts: Hilbert symbols, ES solution enumeration."""
from fractions import Fraction
from math import gcd
from sympy import factorint


def _vp(x, p):
    v = 0
    while x % p == 0:
        x //= p
        v += 1
    return v, x


def hilbert(a, b, p):
    """Hilbert symbol (a,b)_p for nonzero rationals a,b; p prime or 'inf'. Returns +1/-1."""
    a, b = Fraction(a), Fraction(b)
    assert a != 0 and b != 0
    if p == 'inf':
        return -1 if (a < 0 and b < 0) else 1
    # reduce to integers: multiply by squares of denominators
    A = a.numerator * a.denominator
    B = b.numerator * b.denominator
    al, u = _vp(A, p)
    be, v = _vp(B, p)
    if p != 2:
        eps = 1 if (p - 1) // 2 % 2 == 0 else -1  # (-1/p)
        def leg(x):
            r = pow(x % p, (p - 1) // 2, p)
            return 1 if r == 1 else -1
        s = (eps if (al * be) % 2 else 1)
        s *= leg(u) ** (be % 2) * leg(v) ** (al % 2)
        return s
    # p = 2
    def e(x):
        return ((x - 1) // 2) % 2
    def w(x):
        return ((x * x - 1) // 8) % 2
    ex = e(u % 8) * e(v % 8) + al * w(v % 8) + be * w(u % 8)
    return -1 if ex % 2 else 1


def es_solutions(n, positive=True):
    """All (x<=y<=z) positive integer solutions of 4/n = 1/x+1/y+1/z."""
    sols = []
    r0 = Fraction(4, n)
    for x in range(n // 4 + 1, 3 * n // 4 + 2):
        r1 = r0 - Fraction(1, x)
        if r1 <= 0:
            continue
        lo = max(x, int(1 / r1) + 1 if (1 / r1).denominator != 1 else int(1 / r1))
        hi = int(2 / r1)
        for y in range(max(x, lo), hi + 1):
            r2 = r1 - Fraction(1, y)
            if r2 <= 0:
                continue
            if r2.numerator == 1 and r2.denominator >= y:
                sols.append((x, y, r2.denominator))
    return sols


def primes_dividing(n):
    return list(factorint(n).keys())
