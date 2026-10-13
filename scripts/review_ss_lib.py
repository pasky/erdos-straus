"""R188 (review of O188 STERILE_STEER): from-scratch ET Prop 1.9 class machinery.

Written directly from Elsholtz-Tao arXiv:1107.1010, Prop 1.9 (p. 8) and Sec. 10 (p. 37-38); does not import the
author's code. A class is (fam, params, M, rho).

  I1 (a,d,f):  f | 4a^2d+1,            n = -f      mod 4ad
  I2 (a,c,f):  gcd(4ac,f)=1,           n = -f mod 4ac, n = -c/a mod f
  I3 (c,d,f):  gcd(4cd,f)=1,           n = -f mod 4cd, n^2 = -4c^2 d mod f
  I4 (a,b,e):  e | a+b, gcd(e,4ab)=1,  n = -1/e    mod 4ab
  II1 (a,b,e): e | a+b, gcd(e,4ab)=1,  n = -e      mod 4ab
  II2 (a,d,f): 4ad | f+1,              n = -4a^2d  mod f
  II3 (a,d,e): gcd(4ad,e)=1,           n = -4a^2d-e mod 4ade
"""
from fractions import Fraction
from math import gcd


def et_tuple(fam, P, n):
    """ET Sec.10 sextuple (a,b,c,d,e,f) and type for n in the class; None if not integral/positive."""
    def q(x, y):
        return x // y if y and x % y == 0 else None
    if fam == 'I1':
        a, d, f = P
        e = q(4 * a * a * d + 1, f); c = q(n + f, 4 * a * d)
        if e is None or c is None: return None
        t = (a, c * e - a, c, d, e, f); T = 'I'
    elif fam == 'I2':
        a, c, f = P
        b = q(n * a + c, f); d = q(n + f, 4 * a * c); e = q(n * a + a * f + c, f * c)
        if None in (b, d, e): return None
        t = (a, b, c, d, e, f); T = 'I'
    elif fam == 'I3':
        c, d, f = P
        a = q(n + f, 4 * c * d); b = q(n * n + 4 * c * c * d + n * f, 4 * c * d * f)
        e = q((n + f) ** 2 + 4 * c * c * d, 4 * c * c * d * f)
        if None in (a, b, e): return None
        t = (a, b, c, d, e, f); T = 'I'
    elif fam == 'I4':
        a, b, e = P
        c = q(a + b, e); d = q(n * e + 1, 4 * a * b)
        if None in (c, d): return None
        t = (a, b, c, d, e, 4 * a * c * d - n); T = 'I'
    elif fam == 'II1':
        a, b, e = P
        c = q(a + b, e); d = q(n + e, 4 * a * b)
        if None in (c, d): return None
        t = (a, b, c, d, e, 4 * a * c * d - 1); T = 'II'
    elif fam == 'II2':
        a, d, f = P
        c = q(f + 1, 4 * a * d); e = q(n + 4 * a * a * d, f)
        if None in (c, e): return None
        t = (a, c * e - a, c, d, e, f); T = 'II'
    elif fam == 'II3':
        a, d, e = P
        b = q(n + e, 4 * a * d); c = q(n + 4 * a * a * d + e, 4 * a * d * e); f = q(n + 4 * a * a * d, e)
        if None in (b, c, f): return None
        t = (a, b, c, d, e, f); T = 'II'
    else:
        raise ValueError(fam)
    if min(t) <= 0:
        return None
    return T, t


def check_V(T, t, n):
    """membership in V_I(n) / V_II(n) (bare N-point, no coprimality)."""
    a, b, c, d, e, f = t
    if T == 'I':
        return 4 * a * b * d == n * e + 1 and a + b == c * e and f == 4 * a * c * d - n
    return 4 * a * b * d == n + e and a + b == c * e and f == 4 * a * c * d - 1


def es_solution(fam, P, n):
    r = et_tuple(fam, P, n)
    if r is None:
        return None
    T, (a, b, c, d, e, f) = r
    if not check_V(T, (a, b, c, d, e, f), n):
        return None
    xyz = (a * b * d * n, a * c * d, b * c * d) if T == 'I' else (a * b * d, a * c * d * n, b * c * d * n)
    assert Fraction(4, n) == sum(Fraction(1, v) for v in xyz), (fam, P, n, xyz)
    return xyz


def divisors(m):
    out = [1]
    x = m; p = 2
    while p * p <= x:
        if x % p == 0:
            k = 0
            while x % p == 0:
                x //= p; k += 1
            out = [dd * p ** i for dd in out for i in range(k + 1)]
        p += 1 if p == 2 else 2
    if x > 1:
        out = out + [dd * x for dd in out]
    return out


def classes_upto(X):
    """yield (fam, P, M, rho) for every class of modulus M <= X (brute, from the definitions)."""
    Q = X // 4
    for a in range(1, Q + 1):
        for d in range(1, Q // a + 1):
            M = 4 * a * d
            for f in divisors(4 * a * a * d + 1):
                yield 'I1', (a, d, f), M, (-f) % M
            for e in divisors(a + d):          # here d plays b
                if gcd(e, M) == 1:
                    yield 'I4', (a, d, e), M, (-pow(e, -1, M)) % M
                    yield 'II1', (a, d, e), M, (-e) % M
    for f in range(3, X + 1, 4):
        g = (f + 1) // 4
        for a in divisors(g):
            for d in divisors(g // a):
                yield 'II2', (a, d, f), f, (-4 * a * a * d) % f
    for x in range(1, Q + 1):
        for y in range(1, Q // x + 1):
            for z in range(1, Q // (x * y) + 1):
                if gcd(4 * x * y, z) != 1:
                    continue
                m1 = 4 * x * y; M = m1 * z
                # I2 (a,c,f)=(x,y,z)
                r2 = (-y * pow(x, -1, z)) % z if z > 1 else 0
                yield 'I2', (x, y, z), M, crt(-z % m1, m1, r2, z)
                # I3 (c,d,f)=(x,y,z)
                for s in range(z):
                    if (s * s + 4 * x * x * y) % z == 0:
                        yield 'I3', (x, y, z), M, crt(-z % m1, m1, s, z)
                # II3 (a,d,e)=(x,y,z)
                yield 'II3', (x, y, z), M, (-4 * x * x * y - z) % M


def crt(r1, m1, r2, m2):
    if m2 == 1:
        return r1 % m1
    return (r1 + m1 * (((r2 - r1) * pow(m1, -1, m2)) % m2)) % (m1 * m2)
