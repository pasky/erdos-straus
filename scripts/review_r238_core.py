"""R238 from-scratch core: Def 1.1 checker, window caps, exact solution builder.

Written independently of scripts/z12_* (not imported, not read for logic).
"""
from fractions import Fraction
from math import gcd, isqrt


def factor(n):
    f = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            f[d] = f.get(d, 0) + 1
            n //= d
        d += 1 if d == 2 else 2
    if n > 1:
        f[n] = f.get(n, 0) + 1
    return f


def is_prime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True


def jacobi(a, n):
    assert n > 0 and n % 2 == 1
    a %= n
    r = 1
    while a:
        while a % 2 == 0:
            a //= 2
            if n % 8 in (3, 5):
                r = -r
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3:
            r = -r
        a %= n
    return r if n == 1 else 0


def def11_cap(n, x, y, z):
    """Check 4/n = 1/x+1/y+1/z against EXPONENT_CAP Def 1.1 directly.
    Returns the least e for which the triple is ES^{(y,e)}(n), or None if it is not ES^{(y,inf)}."""
    if not (isinstance(x, int) and isinstance(y, int) and x > 0 and y > 0):
        return None
    z = Fraction(z)
    if z <= 0 or Fraction(4, n) != Fraction(1, x) + Fraction(1, y) + 1 / z:
        return None
    d = z.denominator
    q = isqrt(d)
    if q * q != d or q % 2 == 0 or gcd(q, n) != 1:
        return None
    e = 0
    for l, v in factor(q).items():
        if y % l:
            return None
        e = max(e, v)
    return e


def solution_from_Q(n, m, Q):
    """Given window m and Q with m | n+4Q^2, x = (n+m)/4; derive y, z from the equation (not from a formula)."""
    assert (n + 4 * Q * Q) % m == 0
    g = (n + 4 * Q * Q) // m
    assert g % 4 == 3
    x = (n + m) // 4
    y = n * (g + 1) // 4
    assert n * (g + 1) % 4 == 0
    zinv = Fraction(4, n) - Fraction(1, x) - Fraction(1, y)
    assert zinv > 0
    return x, y, 1 / zinv
