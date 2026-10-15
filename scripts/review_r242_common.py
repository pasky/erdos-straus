"""R242 from-scratch helpers (no reuse of author's z13_* code)."""
from array import array
from fractions import Fraction
from math import gcd, isqrt


def spf_sieve(N):
    spf = array('i', [0]) * (N + 1)
    for i in range(2, N + 1):
        if spf[i] == 0:
            for j in range(i, N + 1, i):
                if spf[j] == 0:
                    spf[j] = i
    return spf


def factor(n, spf):
    f = {}
    while n > 1:
        p = spf[n]
        while n % p == 0:
            n //= p
            f[p] = f.get(p, 0) + 1
    return f


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


def order(s, q):
    s %= q
    o, x = 1, s
    while x != 1:
        x = x * s % q
        o += 1
    return o


def vp(n, p):
    v = 0
    while n % p == 0:
        n //= p
        v += 1
    return v


def check_def11(n, x, y, z, e, primes_hint):
    """Independent check of EXPONENT_CAP Def 1.1 for ES^{(y,e)}(n). Returns the true cap of this triple."""
    assert isinstance(x, int) and isinstance(y, int) and x > 0 and y > 0
    z = Fraction(z)
    assert z > 0
    assert Fraction(4, n) == Fraction(1, x) + Fraction(1, y) + 1 / z, 'identity'
    den = z.denominator
    r = isqrt(den)
    assert r * r == den, 'den not square'
    assert r % 2 == 1, 'den even'
    assert gcd(r, n) == 1, 'den meets n'
    cap = 0
    rr = r
    for p in primes_hint:
        if rr % p == 0:
            v = vp(rr, p)
            rr //= p ** v
            assert y % p == 0, 'rad den does not divide y'
            cap = max(cap, v)
    assert rr == 1, 'den has primes outside hint'
    assert cap <= e, ('cap exceeded', cap, e)
    return cap
