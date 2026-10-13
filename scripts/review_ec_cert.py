#!/usr/bin/env python3
"""R185 from-scratch certificate checker for data/ec/cert_k*.json (does NOT reuse ec_cert.py).

Certificate format (as observed): {k,b,c,L,classes:[{M,r,fam,params,exps,xyz:[px,py,pz]}]} where px is a list of
rational strings = coefficients of x(n) in ASCENDING powers of n (confirmed below by checking the identity).
We ignore 'exps' and 'fam' entirely; only (M, r, x(n), y(n), z(n)) are used.

Checks per class (sympy exact arithmetic):
 (i)   4*x*y*z - n*(x*y + y*z + z*x) == 0 in Q[n];
 (ii)  x,y,z integer-valued on n = r + M t: P(t) = x(r+Mt) in Q[t]; integer-valued iff P(0..deg) in Z
       (Polya basis); cross-checked by reducing numerator mod denominator for all t mod denominator.
 (iii) positivity: each of x,y,z has positive leading coeff (or is a positive constant); bound N_pos = 1 + floor of the
       largest real root (sympy real_roots, exact); then x,y,z > 0 for real n > N_pos.
 (iv)  coverage: M = 2^s M' with M' | 2^L - 1; for m >= s, n_m mod M is L-periodic. Choose m1 = max(s over classes,
       least m with n_m > N_pos for all classes). For each m in [m1, m1+L) find a class with n_m ≡ r (mod M).
       Since n_m increases in m, for m >= m1 positivity holds, and periodicity transports coverage from the
       representative to all m ≡ it (mod L), m >= m1 (both have m >= s for every class).
 (v)   for 0 <= m < m1: direct ES solve (independent search) and exact verification.
 Also: identity spot-check at the actual n_m for m1 <= m < m1 + 2L (redundant sanity).
"""
import json, sys
from fractions import Fraction as F
from math import gcd
import sympy as sp

n, t = sp.symbols('n t')


def es_solve(N, xmax_extra=10**6):
    """Find positive integers x<=y<=z with 4/N = 1/x+1/y+1/z (exact search)."""
    target = F(4, N)
    x0 = N // 4 + 1
    for x in range(x0, x0 + xmax_extra):
        r1 = target - F(1, x)
        if r1 <= 0:
            continue
        a, b = r1.numerator, r1.denominator
        # 1/y <= r1 and y >= x ... allow any y; y in [ceil(b/a), floor(2b/a)]
        ylo = max(x, -(-b // a))
        yhi = (2 * b) // a
        if yhi - ylo > 200000:
            # use divisor method: a/b = 1/y + 1/z  <=> (a y - b)(a z - b) = b^2
            bb = b * b
            # iterate d | b^2 with d ≡ -b mod a, d <= b  (y = (d+b)/a)
            for d in sp.divisors(bb):
                if d > b:
                    break
                if (d + b) % a == 0 and (bb // d + b) % a == 0:
                    return x, (d + b) // a, (bb // d + b) // a
            continue
        for y in range(ylo, yhi + 1):
            r2 = r1 - F(1, y)
            if r2 > 0 and r2.numerator == 1:
                return x, y, r2.denominator
    return None


def poly(coeffs):
    return sp.Poly(sum(sp.Rational(c) * n**i for i, c in enumerate(coeffs)), n, domain='QQ')


def int_valued_on_class(P, M, r):
    Q = sp.Poly(P.as_expr().subs(n, r + M * t), t, domain='QQ')
    d = Q.degree()
    vals_ok = all(sp.Rational(Q.eval(i)).q == 1 for i in range(max(d, 0) + 1))
    # cross-check: clear denominators, test all residues t mod D
    D = sp.ilcm(*[sp.Rational(c).q for c in Q.all_coeffs()])
    num = sp.Poly((Q * D).as_expr(), t, domain='ZZ')
    cc = [int(c) for c in num.all_coeffs()]
    def ev(tt):
        v = 0
        for c in cc:
            v = (v * tt + c) % D
        return v
    if D <= 10**6:
        res_ok = all(ev(tt) == 0 for tt in range(D))
    else:
        res_ok = None
    return vals_ok, res_ok, int(D)


def pos_bound(P):
    if P.degree() <= 0:
        c = P.as_expr()
        return (0 if c > 0 else None)
    if P.LC() <= 0:
        return None
    rr = sp.Poly(P.as_expr(), n).real_roots()
    if not rr:
        return 0
    return int(sp.floor(max(rr))) + 1


def check(path, verbose=True):
    C = json.load(open(path))
    k, b, c, L = C['k'], C['b'], C['c'], C['L']
    assert b == 2 and c == 1, (b, c)
    ok = True
    Npos = 0
    smax = 0
    cls = []
    for i, cl in enumerate(C['classes']):
        M, r = cl['M'], cl['r'] % cl['M']
        X = [poly(p) for p in cl['xyz']]
        x, y, z = X
        ident = (4 * x * y * z - poly(['0', '1']) * (x * y + y * z + z * x)).is_zero
        iv = [int_valued_on_class(P, M, r) for P in X]
        pb = [pos_bound(P) for P in X]
        s = 0
        Mo = M
        while Mo % 2 == 0:
            Mo //= 2; s += 1
        per = (pow(2, L, Mo) == 1 % Mo)
        good = ident and all(a and (bb is not False) for a, bb, _ in iv) and None not in pb and per
        if verbose:
            print(f'  class {i}: M={M} r={r} fam={cl["fam"]} ident={ident} intval={[(a, bb) for a, bb, _ in iv]} '
                  f'posbound={pb} s={s} Modd|2^L-1={per}')
        if not good:
            ok = False
            print('  *** CLASS FAILS ***')
            continue
        Npos = max(Npos, *pb)
        smax = max(smax, s)
        cls.append((M, r, X))
    m1 = smax
    while k * 2**m1 + 1 <= Npos:
        m1 += 1
    # coverage
    for m in range(m1, m1 + 2 * L):
        N = k * 2**m + 1
        hit = [j for j, (M, r, X) in enumerate(cls) if N % M == r]
        if not hit:
            ok = False
            print(f'  *** m={m} (mod L={m % L}) UNCOVERED ***')
            continue
        M, r, X = cls[hit[0]]
        vals = [int(P.eval(N)) if sp.Rational(P.eval(N)).q == 1 else None for P in X]
        if None in vals or min(vals) <= 0 or F(1, vals[0]) + F(1, vals[1]) + F(1, vals[2]) != F(4, N):
            ok = False
            print(f'  *** m={m}: evaluation failure {vals}')
    # small m
    for m in range(0, m1):
        N = k * 2**m + 1
        sol = es_solve(N)
        good = sol is not None and F(1, sol[0]) + F(1, sol[1]) + F(1, sol[2]) == F(4, N) and min(sol) > 0
        if verbose:
            print(f'  small m={m}: n={N} sol={sol} ok={good}')
        if not good:
            ok = False
    print(f'{path}: k={k} L={L} classes={len(C["classes"])} Npos={Npos} s_max={smax} m1={m1} => {"PASS" if ok else "FAIL"}')
    return ok


if __name__ == '__main__':
    res = [check(p, verbose='-q' not in sys.argv) for p in sys.argv[1:] if p != '-q']
    print('ALL PASS' if all(res) else 'SOME FAIL')
