"""O194 TES_FINITE: independent Z[w] arithmetic (w = zeta_3) for the exhaustive TES solver.

Elements are pairs (a, b) = a + b*w, w^2 = -1 - w.  Written from scratch (does not import tw_eis.py).
"""
import math
from functools import lru_cache
from sympy import factorint

UNITS = [(1, 0), (0, 1), (-1, -1), (-1, 0), (0, -1), (1, 1)]
W, W2, TWO, NINE = (0, 1), (-1, -1), (2, 0), (9, 0)


def mul(x, y):
    a, b = x; c, d = y
    return (a * c - b * d, a * d + b * c - b * d)


def add(x, y): return (x[0] + y[0], x[1] + y[1])
def sub(x, y): return (x[0] - y[0], x[1] - y[1])
def conj(x): return (x[0] - x[1], -x[1])
def norm(x): return x[0] * x[0] - x[0] * x[1] + x[1] * x[1]


def div(x, y):
    """x / y if it lies in Z[w], else None."""
    n = norm(y)
    p = mul(x, conj(y))
    if p[0] % n or p[1] % n:
        return None
    return (p[0] // n, p[1] // n)


def two_primary(x):  # x = 1 mod 2O  <=>  a odd, b even
    return x[0] % 2 == 1 and x[1] % 2 == 0


def disk(R):
    """all nonzero x with N(x) <= R (R real)."""
    out = []
    bmax = int(math.isqrt(int(4 * R / 3) + 1)) + 1
    for b in range(-bmax, bmax + 1):
        # a^2 - ab + b^2 <= R  <=>  (a - b/2)^2 <= R - 3b^2/4
        s = R - 0.75 * b * b
        if s < 0:
            continue
        r = math.sqrt(s)
        for a in range(math.floor(b / 2 - r) - 1, math.ceil(b / 2 + r) + 2):
            if (a, b) != (0, 0) and norm((a, b)) <= R:
                out.append((a, b))
    return out


@lru_cache(maxsize=None)
def prime_above(p):
    """a prime element of norm p (p = 3 or p = 1 mod 3) or p itself (p = 2 mod 3, inert; norm p^2)."""
    if p == 3:
        return (1, -1)
    if p % 3 == 2:
        return (p, 0)
    for b in range(1, math.isqrt(4 * p // 3) + 2):
        # solve a^2 - ab + b^2 = p
        disc = 4 * p - 3 * b * b
        if disc < 0:
            break
        s = math.isqrt(disc)
        if s * s == disc and (b + s) % 2 == 0:
            a = (b + s) // 2
            assert norm((a, b)) == p
            return (a, b)
    raise ValueError(p)


def factor(x):
    """dict prime_element -> exponent with x = unit * prod; primes from prime_above and conjugates."""
    out = {}
    rem = x
    for p, e in factorint(norm(x)).items():
        P = prime_above(p)
        cands = [P] if (p == 3 or p % 3 == 2) else [P, conj(P)]
        for Q in cands:
            while True:
                q = div(rem, Q)
                if q is None:
                    break
                rem = q
                out[Q] = out.get(Q, 0) + 1
    assert norm(rem) == 1, (x, rem)
    return out


def divisors(fac):
    ds = [(1, 0)]
    for P, e in fac.items():
        new = []
        for d in ds:
            q = d
            for _ in range(e + 1):
                new.append(q)
                q = mul(q, P)
        ds = new
    return [mul(u, d) for d in ds for u in UNITS]


def merge(*facs):
    out = {}
    for f in facs:
        for P, e in f.items():
            out[P] = out.get(P, 0) + e
    return out


def check(n, xs, cs=(W, W2, TWO), t=NINE):
    """exact check of t/n = sum c_i/x_i: t*x1x2x3 == n*(c1 x2 x3 + c2 x1 x3 + c3 x1 x2)."""
    x1, x2, x3 = xs
    lhs = mul(t, mul(x1, mul(x2, x3)))
    rhs = add(add(mul(cs[0], mul(x2, x3)), mul(cs[1], mul(x1, x3))), mul(cs[2], mul(x1, x2)))
    return lhs == mul(n, rhs)
