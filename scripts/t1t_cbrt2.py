"""O183: ES over Z[cbrt2] with positivity at the unique real place (T1-bearing by T1_TEMPLATE Cor 2.2).

Unit mechanism (Prop 1.2 with K = Q(cbrt2)): eta = eps^k > 0 (eps = theta - 1, theta^3 = 2), a = n + 4 eta.
If a = e g with g = -1 (mod 4), g > 0, e > 0 (real embedding) then x = (n+e)/4, y = n(g+1)/4,
z = n x (g+1)/(4 eta) solve 4/n = 1/x + 1/y + 1/z with x, y, z > 0.
Divisors g tried: products of the l-parts gcd(a, l^v) over subsets of the rational primes l | N(a), times units.
Usage: PYTHONPATH=scripts uv run python scripts/t1t_cbrt2.py PMAX KMAX SQMAX
"""
import sys
from itertools import combinations
from sympy import factorint, primerange

TH = 2 ** (1 / 3)


def mul(u, v):
    a, b, c = u
    d, e, f = v
    # theta^3 = 2, theta^4 = 2 theta
    return (a * d + 2 * (b * f + c * e), a * e + b * d + 2 * c * f, a * f + b * e + c * d)


def add(u, v):
    return tuple(x + y for x, y in zip(u, v))


def real(u):
    return u[0] + u[1] * TH + u[2] * TH * TH


def norm(u):
    a, b, c = u
    return a ** 3 + 2 * b ** 3 + 4 * c ** 3 - 6 * a * b * c


def adj(u):
    """u * adj(u) = norm(u)."""
    a, b, c = u
    return (a * a - 2 * b * c, 2 * c * c - a * b, b * b - a * c)


def exact_div(u, v):
    w = mul(u, adj(v))
    N = norm(v)
    if any(x % N for x in w):
        return None
    return tuple(x // N for x in w)


def gcd(u, v):
    while v != (0, 0, 0):
        w = mul(u, adj(v))
        N = norm(v)
        q = tuple(round(x / N) for x in w)
        r = add(u, tuple(-x for x in mul(q, v)))
        u, v = v, r
    return u


EPS = (-1, 1, 0)
EPSI = exact_div((1, 0, 0), EPS)


def epow(k):
    r = (1, 0, 0)
    for _ in range(abs(k)):
        r = mul(r, EPS if k > 0 else EPSI)
    return r


def mod4(u):
    return tuple(x % 4 for x in u)


UNITS = [mul((s, 0, 0), epow(j)) for s in (1, -1) for j in range(0, 64)]


def normalise(g):
    for u in UNITS:
        h = mul(u, g)
        if mod4(h) == (3, 0, 0) and real(h) > 0:
            return h
    return None


def try_k(n, k):
    eta = epow(k)
    a = add((n, 0, 0), mul((4, 0, 0), eta))
    fac = factorint(abs(norm(a)), limit=10 ** 5)
    parts = [gcd(a, (l ** v, 0, 0)) for l, v in fac.items() if l != 2]
    for r in (1, 2):
        for sub in combinations(parts, r):
            g = (1, 0, 0)
            for s in sub:
                g = mul(g, s)
            h = normalise(g)
            if h is None:
                continue
            e = exact_div(a, h)
            if e is None or real(e) <= 0:
                continue
            x = exact_div(add((n, 0, 0), e), (4, 0, 0))
            y = exact_div(mul((n, 0, 0), add(h, (1, 0, 0))), (4, 0, 0))
            z = exact_div(mul(mul((n, 0, 0), x), add(h, (1, 0, 0))), mul((4, 0, 0), eta))
            if None in (x, y, z):
                continue
            lhs = mul((4, 0, 0), mul(x, mul(y, z)))
            rhs = mul((n, 0, 0), add(add(mul(y, z), mul(x, z)), mul(x, y)))
            assert lhs == rhs and min(real(x), real(y), real(z)) > 0
            return (k, x, y, z)
    return None


def kseq(K):
    yield 0
    for j in range(1, K + 1):
        yield -j
        yield j


if __name__ == '__main__':
    PMAX, KMAX, SQMAX = map(int, sys.argv[1:4])
    hist, fails = {}, []
    for p in primerange(3, PMAX):
        for k in kseq(KMAX):
            if try_k(p, k):
                hist[abs(k)] = hist.get(abs(k), 0) + 1
                break
        else:
            fails.append(p)
    print('primes <', PMAX, 'min|k| hist', sorted(hist.items()), 'fails', fails)
    print('example p=13:', next(r for r in (try_k(13, k) for k in kseq(KMAX)) if r))
    bad = [m for m in range(3, SQMAX, 2) if any(try_k(m * m, k) for k in kseq(KMAX))]
    print('odd squares with unit solution', bad)
