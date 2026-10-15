# review_r235_cert.py -- R235 from-scratch checker for data/z8/cert_c1_k*.json (does NOT import ec_cert / z8 code).
# Certificate semantics (as used by ec_cert): n_s = k*b^s + c; class (M, r): if n_s = r (mod M) then
# x, y, z = polynomials in n (coefficient lists, low degree first) give 4/n = 1/x + 1/y + 1/z.
# Independent checks:
#  (1) identity 4xyz - n(xy+yz+zx) == 0 in Q[n] (sympy);
#  (2) integrality: D*p(n) has integer coeffs; D | D*p(n) checked for all n = r + M t, t over one full period of D;
#  (3) positivity: sympy real roots -> largest real root R; p > 0 for n > R with positive leading coefficient;
#  (4) periodicity: own derivation. n_s mod M: odd part M' needs b^L = 1 (mod M'); 2-part 2^e needs b^s = 0 (mod 2^e),
#      i.e. s >= s_e := ceil(e / v2(b)). Then n_{s+L} = n_s (mod M) for s >= s_e. Check covering for one window of L
#      residues starting at S0 = max s_e, AND directly check n_s mod M equality for s, s+L for s in window (redundant);
#  (5) direct exact verification for all s <= SMAX (any matching class, integer positive x,y,z, exact identity);
#  (6) for s < S0 and for every s where n_s is below the positivity threshold: own brute-force ES solver;
#  (7) list s with n_s a perfect square and report which class covers it.
import sys, json, glob
from fractions import Fraction as F
from math import isqrt, gcd
import sympy as sp

N = sp.Symbol('n')


def poly(coefs):
    return sum(sp.Rational(c) * N ** i for i, c in enumerate(coefs))


def es_solve(n):
    # 4/n = 1/x+1/y+1/z, x<=y<=z. n/4 < x <= 3n/4.
    for x in range(n // 4 + 1, 3 * n // 4 + 1):
        a, d = 4 * x - n, n * x  # a/d = 1/y + 1/z, y <= z => d/a < y <= 2d/a
        if a <= 0:
            continue
        for y in range(max(x, d // a + 1), 2 * d // a + 1):
            num, den = a * y - d, d * y
            if num > 0 and den % num == 0:
                return x, y, den // num
    return None


def v2(m):
    e = 0
    while m % 2 == 0:
        m //= 2
        e += 1
    return e


def check(path, SMAX=400):
    C = json.load(open(path))
    k, b, c, L = C['k'], C['b'], C['c'], C['L']
    assert b == 4 and k == 1
    ns = lambda s: k * b ** s + c
    cls = []
    S0 = 0
    for cl in C['classes']:
        M, r = cl['M'], cl['r']
        P = [poly(p) for p in cl['xyz']]
        x, y, z = P
        assert sp.expand(4 * x * y * z - N * (x * y + y * z + z * x)) == 0, ('identity', path, M, r)
        # integrality
        for p in P:
            pp = sp.Poly(p, N)
            D = sp.ilcm(*[sp.Rational(cf).q for cf in pp.all_coeffs()])
            q = sp.Poly(sp.expand(D * p), N)
            assert all(sp.Rational(cf).q == 1 for cf in q.all_coeffs())
            per = D // gcd(D, M)
            for t in range(per):
                val = q.eval(r + M * t)
                assert val % D == 0, ('integrality', path, M, r, p, t)
        # positivity threshold
        R = 0
        for p in P:
            pp = sp.Poly(p, N)
            assert pp.LC() > 0
            rts = [float(rt) for rt in sp.real_roots(pp)] if pp.degree() > 0 else []
            R = max([R] + rts)
        e = v2(M)
        Mo = M >> e
        assert pow(b, L, Mo) == 1 % Mo, ('period', path, M)
        se = -(-e // 2)
        S0 = max(S0, se)
        cls.append((M, r, P, R, cl))
    # covering window + redundant periodicity spot check
    for s in range(S0, S0 + L):
        hits = [cl for cl in cls if ns(s) % cl[0] == cl[1]]
        assert hits, ('uncovered', path, s % L)
        for cl in cls:
            assert ns(s) % cl[0] == ns(s + L) % cl[0] == ns(s + 7 * L) % cl[0]
    # direct verification s <= SMAX
    brute = []
    for s in range(0, SMAX + 1):
        n = ns(s)
        done = False
        if s >= S0:
            for M, r, P, R, cl in cls:
                if n % M == r and n > R:
                    vals = [p.subs(N, n) for p in P]
                    assert all(v.is_integer and v > 0 for v in vals)
                    X, Y, Z = (int(v) for v in vals)
                    assert 4 * X * Y * Z == n * (X * Y + Y * Z + Z * X)
                    done = True
                    break
        if not done:
            sol = es_solve(n)
            assert sol is not None, ('ES brute fails', n)
            X, Y, Z = sol
            assert 4 * X * Y * Z == n * (X * Y + Y * Z + Z * X)
            brute.append((s, n, sol))
    sq = []
    for s in range(0, 60):
        n = ns(s)
        if isqrt(n) ** 2 == n:
            cov = [(cl[0], cl[1], cl[4]['fam']) for cl in cls if n % cl[0] == cl[1] and s >= S0 and n > cl[3]]
            sq.append((s, n, cov))
    print(path, 'OK  L=%d S0=%d classes=%d brute=%s squares=%s' % (L, S0, len(cls), brute, sq))


if __name__ == '__main__':
    for f in sorted(glob.glob('data/z8/cert_c1_k*.json')):
        check(f, int(sys.argv[1]) if len(sys.argv) > 1 else 400)
