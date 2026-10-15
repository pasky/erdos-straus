# review_r236_cert.py — R236 FROM-SCRATCH checker for data/z8/cert_c1_k*.json (does not import ec_cert / z8 code).
# Claim checked: ES holds for every n_s = A*4^s + C, s >= 0 (A = json 'k', base json 'b' = 4, C = json 'c').
# Per class (n ≡ r mod M, x,y,z polynomials in n, coefficient lists low->high):
#   (1) 4xyz - n(xy+yz+zx) == 0 in Q[n]  (sympy, exact)
#   (2) integrality: D*p in Z[n] where D = lcm(denominators); p(n) in Z for all n ≡ r (M) iff D | D*p(n) for
#       every residue n mod lcm(M, D) with n ≡ r (M)  (exhaustive residue check)
#   (3) positivity: leading coeff > 0 and n > largest real root (sympy real_roots), giving n_pos
#   (4) periodicity: M = 2^a M', M' odd; for 2s >= a, n_s mod M has period ord_{M'}(4); require ord | L
#   (5) coverage: for s0 = max over classes of ceil(a/2) and n_{s0} >= all n_pos, every s in [s0, s0+L) hits a class
#   (6) s < s0: either a class gives positive integers (checked numerically) or independent ES search
#   (7) exact integer check of the identity for s <= SMAX
import sys, json, math
from fractions import Fraction as F
import sympy as sp

N = sp.Symbol('n')


def poly(coeffs):
    return sum(sp.Rational(F(c).numerator, F(c).denominator) * N ** i for i, c in enumerate(coeffs))


def es_small(n):
    """independent ES search: 4/n = 1/x + 1/y + 1/z via (a y - b)(a z - b) = b^2 for x in a window."""
    for x in range(n // 4 + 1, n // 4 + 5000):
        a, b = 4 * x - n, n * x
        g = math.gcd(a, b); a //= g; b //= g
        if a <= 0:
            continue
        for d in sp.divisors(b * b):
            if d > b:                 # need y <= z, i.e. d = a y - b <= b
                break
            if (d + b) % a == 0:
                y = (d + b) // a
                e = b * b // d
                if (e + b) % a == 0:
                    z = (e + b) // a
                    assert F(1, x) + F(1, y) + F(1, z) == F(4, n)
                    return (x, y, z)
    return None


def order4(m):
    if m == 1:
        return 1
    return sp.n_order(4, m)


def check(path, SMAX=400):
    C = json.load(open(path))
    A, B, Cc, L = C['k'], C['b'], C['c'], C['L']
    assert B == 4
    ns = lambda s: A * 4 ** s + Cc
    s0 = 0
    npos_all = 0
    cls = []
    for cl in C['classes']:
        M, r = cl['M'], cl['r']
        P = [poly(p) for p in cl['xyz']]
        x, y, z = P
        assert sp.expand(4 * x * y * z - N * (x * y + y * z + z * x)) == 0, ('identity', cl)
        for p, coeffs in zip(P, cl['xyz']):
            D = 1
            for c in coeffs:
                D = D * F(c).denominator // math.gcd(D, F(c).denominator)
            Q = [int(F(c) * D) for c in coeffs]
            Mod = M * D // math.gcd(M, D)
            for nn in range(r % M, Mod, M):
                assert sum(q * nn ** i for i, q in enumerate(Q)) % D == 0, ('integrality', cl, coeffs)
            pp = sp.Poly(p, N)
            assert pp.LC() > 0, ('leading coeff', cl)
            rr = [float(t) for t in sp.real_roots(pp)] if pp.degree() > 0 else []
            npos_all = max(npos_all, math.floor(max(rr)) + 1 if rr else 0)
        a = 0; Mo = M
        while Mo % 2 == 0:
            Mo //= 2; a += 1
        assert L % order4(Mo) == 0, ('period', cl)
        s0 = max(s0, (a + 1) // 2)
        cls.append((M, r, P))
    while ns(s0) < npos_all:
        s0 += 1
    for s in range(s0, s0 + L):
        assert any(ns(s) % M == r for M, r, _ in cls), ('uncovered', s % L)
    small = []
    for s in range(0, SMAX + 1):
        n = ns(s)
        hit = None
        for M, r, P in cls:
            if n % M == r:
                v = [p.subs(N, n) for p in P]
                if all(t.is_integer and t > 0 for t in v):
                    hit = v
                    break
        if hit is not None:
            x, y, z = (int(t) for t in hit)
            assert 4 * x * y * z == n * (x * y + y * z + x * z)
        else:
            assert s < s0, ('class fails at s >= s0', s)
            sol = es_small(n)
            assert sol is not None, ('no ES solution found', n)
            small.append((s, n, sol))
    print('%s: n = %d*4^s + %d, L = %d, classes = %d, s0 = %d, n_pos = %d -> COVERED; exact to s = %d; small %s'
          % (path, A, Cc, L, len(cls), s0, npos_all, SMAX, small))


if __name__ == '__main__':
    smax = int(sys.argv[-1]) if sys.argv[-1].isdigit() else 400
    for p in sys.argv[1:]:
        if not p.isdigit():
            check(p, smax)
