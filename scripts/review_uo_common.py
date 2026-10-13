"""R186 from-scratch helpers: Hilbert symbols over Q, valuations, ES^(S) checks (no reuse of scripts/uo_*)."""
from fractions import Fraction
from math import gcd


def vp(n, p):
    """p-adic valuation of a nonzero int or Fraction."""
    if isinstance(n, Fraction):
        return vp(n.numerator, p) - vp(n.denominator, p)
    n = abs(n)
    assert n != 0
    k = 0
    while n % p == 0:
        n //= p
        k += 1
    return k


def legendre(a, p):
    a %= p
    if a == 0:
        return 0
    t = pow(a, (p - 1) // 2, p)
    return 1 if t == 1 else -1


def split(x, p):
    """x = p^k * u with u a p-adic unit given as (num, den) ints."""
    x = Fraction(x)
    k = vp(x, p)
    num, den = x.numerator, x.denominator
    if k > 0:
        num //= p ** k
    elif k < 0:
        den //= p ** (-k)
    return k, num, den


def hilbert(a, b, p):
    """Hilbert symbol (a,b)_p in {+1,-1} for nonzero rationals; p = 0 means the real place."""
    a, b = Fraction(a), Fraction(b)
    if p == 0:
        return -1 if (a < 0 and b < 0) else 1
    al, an, ad = split(a, p)
    be, bn, bd = split(b, p)
    if p != 2:
        s = (-1) ** ((al * be * ((p - 1) // 2)) % 2)
        u = legendre(an, p) * legendre(ad, p)
        v = legendre(bn, p) * legendre(bd, p)
        return s * (u ** (be % 2)) * (v ** (al % 2))
    u = (an * ad) % 8  # unit mod 8 (den^-1 = den mod 8)
    v = (bn * bd) % 8
    eps = lambda w: ((w - 1) // 2) % 2
    om = lambda w: ((w * w - 1) // 8) % 2
    e = eps(u) * eps(v) + al * om(v) + be * om(u)
    return -1 if e % 2 else 1


def inv(a, b, p):
    """invariant in {0, 1/2} encoded as 0/1."""
    return 0 if hilbert(a, b, p) == 1 else 1


def primes_upto(N):
    s = bytearray([1]) * (N + 1)
    s[0:2] = b"\x00\x00"
    for i in range(2, int(N ** 0.5) + 1):
        if s[i]:
            s[i * i::i] = bytearray(len(s[i * i::i]))
    return [i for i in range(N + 1) if s[i]]


def smonoid(S, bound):
    out = [1]
    for q in S:
        new = []
        for m in out:
            t = m
            while t <= bound:
                new.append(t)
                t *= q
        out = new
    return sorted(out)


def is_S_square_monoid(m, S):
    """m in <S>^2 ?"""
    for q in S:
        k = 0
        while m % q == 0:
            m //= q
            k += 1
        if k % 2:
            return False
    return m == 1


def check_ESS(n, x, y, z, S):
    """Exact check of ES^(S)(n): x,y positive ints, z positive in Z[1/S] with even negative q-valuations."""
    x, y, z = Fraction(x), Fraction(y), Fraction(z)
    assert x.denominator == 1 and y.denominator == 1 and x > 0 and y > 0 and z > 0
    assert 1 / x + 1 / y + 1 / z == Fraction(4, n)
    d = z.denominator
    for q in S:
        while d % q == 0:
            d //= q
    assert d == 1, "z not in Z[1/S]"
    for q in S:
        w = vp(z, q)
        if w < 0:
            assert w % 2 == 0, "odd negative valuation"
    return True
