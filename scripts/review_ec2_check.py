# review_ec2_check.py — R189 (reviewer 2) FROM-SCRATCH checker for data/ec/cert_k*.json.
# Does not import any author script.  Style deliberately different from scripts/ec_cert.py:
#  (1) identity 4xyz = n(xy+yz+zx) checked with sympy polynomial arithmetic;
#  (2) integrality on r + M t: Q(t) = D * p(r + M t) in Z[t] with D = lcm(denominators); p integer-valued on Z
#      iff Q(t) = 0 mod D for every t mod D (Q mod D is D-periodic) -- exhaustive residue check;
#  (3) positivity: exact isolation of all real roots of p (sympy intervals), bound R = max upper endpoint;
#      p(n) > 0 for n > R since LC > 0;
#  (4) coverage: per class, the set of exponents m mod L with n_m = r (mod M) is computed prime-power by prime-power
#      (m mod ord_{q^e}(2)), combined over Z/L; 2-part handled by r = 1 (mod 2^s) (valid for m >= s);
#      union over classes must be Z/L;
#  (5) threshold m* = max(s, first m with n_m > R for every class); ES for m < m* by own brute-force solver.
# Usage: PYTHONPATH=scripts uv run --with sympy python scripts/review_ec2_check.py data/ec/cert_k27.json
import sys, json
from math import lcm, gcd
import sympy as sp
from sympy import Rational, factorint, n_order

nn, tt = sp.symbols('n t')


def poly_of(coeffs):
    return sp.Poly(sum(Rational(c) * nn**i for i, c in enumerate(coeffs)), nn, domain='QQ')


def integer_valued_on_class(p, M, r):
    P = sp.Poly(p.as_expr().subs(nn, r + M * tt), tt, domain='QQ')
    D = 1
    for c in P.all_coeffs():
        D = lcm(D, sp.Rational(c).q)
    Q = [int(c * D) for c in P.all_coeffs()]  # high -> low
    if D == 1:
        return True, D
    for t0 in range(D):
        v = 0
        for c in Q:
            v = (v * t0 + c) % D
        if v:
            return False, D
    return True, D


def root_bound(p):
    """exact: max real root upper endpoint (or -inf); requires LC > 0"""
    assert p.LC() > 0, 'leading coefficient not positive'
    if p.degree() == 0:
        assert p.LC() > 0
        return None
    ivs = p.intervals()
    return max(sp.Rational(iv[0][1]) for iv in ivs) if ivs else None


def exps_for_class(k, L, M, r):
    """set of m in Z/L such that k 2^m + 1 = r (mod M) for all m >= s; returns (set, s)"""
    s = 0
    Mp = M
    while Mp % 2 == 0:
        Mp //= 2
        s += 1
    if (r - 1) % (2**s) != 0:
        return set(), s
    if Mp == 1:
        return set(range(L)), s
    ok = set(range(L))
    for q, e in factorint(Mp).items():
        qe = q**e
        o = n_order(2, qe)
        assert L % o == 0, ('ord does not divide L', qe, o, L)
        good = {j for j in range(o) if (k * pow(2, j, qe) + 1 - r) % qe == 0}
        ok = {m for m in ok if m % o in good}
    return ok, s


def es_solve(n):
    """own solver: 4/n = 1/x+1/y+1/z; for each x, 1/y+1/z = a/b <=> (a y - b)(a z - b) = b^2."""
    if n % 2 == 0:
        h = n // 2  # 4/n = 2/h ; 2/h = 1/h + 1/(2h)... need three terms: 2/h = 1/h + 1/(2h) + 1/(2h)
        return (h, 2 * h, 2 * h)
    fn = factorint(n)
    for x in range(n // 4 + 1, n + 1):
        a, b = 4 * x - n, n * x
        g = gcd(a, b)
        a, b = a // g, b // g
        fb = dict(fn)
        for p, e in factorint(x).items():
            fb[p] = fb.get(p, 0) + e
        # remove g from b's factorisation
        for p, e in factorint(g).items():
            fb[p] -= e
        fb = {p: 2 * e for p, e in fb.items() if e > 0}  # b^2
        divs = [1]
        for p, e in fb.items():
            divs = [d * p**i for d in divs for i in range(e + 1)]
        for d in divs:
            if d <= b and (d + b) % a == 0 and (b + b * b // d) % a == 0:
                y, z = (d + b) // a, (b + b * b // d) // a
                assert 4 * x * y * z == n * (x * y + y * z + x * z)
                return (x, y, z)
    return None


def check(path, verbose=True):
    C = json.load(open(path))
    k, b, c, L = C['k'], C['b'], C['c'], C['L']
    assert (b, c) == (2, 1)
    cover = set()
    mstar = 0
    info = []
    for cl in C['classes']:
        M, r = cl['M'], cl['r']
        assert 0 <= r < M
        X = [poly_of(p) for p in cl['xyz']]
        lhs = 4 * X[0] * X[1] * X[2]
        rhs = sp.Poly(nn, nn, domain='QQ') * (X[0] * X[1] + X[1] * X[2] + X[0] * X[2])
        assert (lhs - rhs).is_zero, ('identity', cl)
        Ds = []
        for p in X:
            okI, D = integer_valued_on_class(p, M, r)
            assert okI, ('not integer valued', cl)
            Ds.append(D)
        Rb = [root_bound(p) for p in X]
        R = max([x for x in Rb if x is not None], default=-1)
        E, s = exps_for_class(k, L, M, r)
        if 'exps' in cl:
            assert sorted(E) == sorted(cl['exps']), ('exps mismatch', cl, sorted(E))
        cover |= E
        m1 = s
        while k * 2**m1 + 1 <= R:
            m1 += 1
        mstar = max(mstar, m1)
        info.append((M, r, cl['fam'], sorted(E), Ds, float(R), s, m1))
        cl['_X'] = X
    assert cover == set(range(L)), ('uncovered', sorted(set(range(L)) - cover))
    # small m: own brute force
    small = {}
    for m in range(mstar):
        n = k * 2**m + 1
        sol = es_solve(n)
        assert sol, ('ES brute failed', n)
        small[m] = sol
    if verbose:
        print(f'k={k} L={L} classes={len(C["classes"])} m*={mstar}')
        for row in info:
            M, r, fam, E, Ds, R, s, m1 = row
            print(f'  M={M} r={r} {fam} |E|={len(E)} E[:8]={E[:8]} D={Ds} R={R:.1f} s={s} m1={m1}')
        print('  small-m brute force OK for m <', mstar, small)
    return C, mstar


if __name__ == '__main__':
    for p in sys.argv[1:]:
        check(p)
        print('PASS', p)
