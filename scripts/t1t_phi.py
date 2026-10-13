"""O183: the golden variant V_phi over O_K = Z[phi], K = Q(sqrt5), phi^2 = phi + 1.

V_phi(n): 4/n = 1/x + 1/y + 1/z, x, y, z in Z[phi], sigma1(x), sigma1(y), sigma1(z) > 0,
          and the sigma2-signs of (x, y, z) are NOT all equal ("mixed at sigma2").
Unit-Type-II mechanism (T1_TEMPLATE Prop 1.3): for k in Z, eta = phi^(2k+1), a_k = n + 4 eta.
If a_k = e*g with g = -1 (mod 4), sigma1(g) > 0, sigma1(e) > 0, then
   x = (n + e)/4,  y = n (g + 1)/4,  z = n x (g + 1)/(4 eta)
solves V_phi(n). Such g exists iff a_k has a prime factor q with chi(q) = -1, chi = character of K(sqrt(-phi))/K,
and chi(q) = (n/q) for q | a_k.
Usage: PYTHONPATH=scripts uv run python scripts/t1t_phi.py PMAX KMAX
"""
import sys
import math
from sympy import factorint, primerange

S5 = math.sqrt(5)
PHI1, PHI2 = (1 + S5) / 2, (1 - S5) / 2


def mul(u, v):
    a, b = u
    c, d = v
    return (a * c + b * d, a * d + b * c + b * d)


def add(u, v):
    return (u[0] + v[0], u[1] + v[1])


def conj(u):
    return (u[0] + u[1], -u[1])


def norm(u):
    a, b = u
    return a * a + a * b - b * b


def s1(u):
    return u[0] + u[1] * PHI1


def s2(u):
    return u[0] + u[1] * PHI2


def exact_div(u, v):
    """u / v if v | u in Z[phi], else None."""
    w = mul(u, conj(v))
    N = norm(v)
    if w[0] % N or w[1] % N:
        return None
    return (w[0] // N, w[1] // N)


def phipow(k):
    r = (1, 0)
    base = (0, 1) if k >= 0 else (-1, 1)  # phi^{-1} = phi - 1
    for _ in range(abs(k)):
        r = mul(r, base)
    return r


def egcd_prime(a, ell):
    """A generator of the prime ideal (ell, a) when it is a degree-1 prime (Euclid in Z[phi])."""
    u, v = (ell, 0), a
    while v != (0, 0):
        # u = q v + r, q = round(u/v)
        w = mul(u, conj(v))
        N = norm(v)
        q = (round(w[0] / N), round(w[1] / N))
        r = add(u, mul((-1, 0), mul(q, v)))
        u, v = v, r
    return u


def mod4(u):
    return (u[0] % 4, u[1] % 4)


UNITS = [(s, phipow(j)) for s in (1, -1) for j in range(12)]


def normalise_g(q):
    """unit multiple g of q with g = -1 (mod 4) and sigma1(g) > 0, or None."""
    for s, u in UNITS:
        g = mul((s, 0), mul(u, q))
        if mod4(g) == (3, 0) and s1(g) > 0:
            return g
    return None


def legendre(a, ell):
    r = pow(a % ell, (ell - 1) // 2, ell)
    return 1 if r == 1 else (-1 if r == ell - 1 else 0)


def solve_unit_typeII(n, k, trial=10**6):
    eta = phipow(2 * k + 1)
    a = add((n, 0), mul((4, 0), eta))
    N = abs(norm(a))
    f = factorint(N, limit=trial)
    for ell in f:
        if ell > trial or ell % 5 not in (1, 4) or legendre(n, ell) != -1:
            continue
        q = egcd_prime(a, ell)
        if abs(norm(q)) != ell:
            continue
        g = normalise_g(q)
        if g is None:
            continue
        e = exact_div(a, g)
        if e is None or s1(e) <= 0:
            continue
        x = exact_div(add((n, 0), e), (4, 0))
        y = exact_div(mul((n, 0), add(g, (1, 0))), (4, 0))
        z = exact_div(mul(mul((n, 0), x), add(g, (1, 0))), mul((4, 0), eta))
        if None in (x, y, z):
            return ('nonintegral', k, ell)
        # verify 4xyz = n(yz + xz + xy)
        lhs = mul((4, 0), mul(x, mul(y, z)))
        rhs = mul((n, 0), add(add(mul(y, z), mul(x, z)), mul(x, y)))
        assert lhs == rhs, (n, k, x, y, z)
        assert min(s1(x), s1(y), s1(z)) > 0
        sg = {s2(x) > 0, s2(y) > 0, s2(z) > 0}
        assert len(sg) == 2, ('not mixed', n, k)
        return (k, ell, x, y, z)
    return None


def kseq(K):
    yield 0
    for j in range(1, K + 1):
        yield -j
        yield j


if __name__ == '__main__':
    PMAX, KMAX = int(sys.argv[1]), int(sys.argv[2])
    hist = {}
    fails = []
    for p in primerange(3, PMAX):
        if p == 5:
            continue
        for k in kseq(KMAX):
            r = solve_unit_typeII(p, k)
            if r is not None and r[0] != 'nonintegral':
                hist[abs(k)] = hist.get(abs(k), 0) + 1
                break
        else:
            fails.append(p)
    print('primes', PMAX, 'min|k| histogram', sorted(hist.items()), 'fails', fails[:50], len(fails))
    print('example', solve_unit_typeII(13, 0) or solve_unit_typeII(13, -1))
    for m in (3, 7, 9, 11, 13):
        print('square', m * m, [solve_unit_typeII(m * m, k) for k in range(-3, 4)])
