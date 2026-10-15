"""R245 from-scratch checker for SYNTHESIS_SPARKS6 Thm 1.1 (ES for all 4^s + 105).
Does NOT import any s6_* / z8 / ec_cover code. Reads only the JSON parameters."""
import json, sys
from fractions import Fraction as F
from math import gcd
import sympy as sp

n = sp.symbols('n')
J = json.load(open('data/s6_cert105_et.json'))
K = 105

def poly(coeffs):
    return sum(sp.Rational(c) * n**i for i, c in enumerate(coeffs))

def ordmod(b, m):
    if m == 1: return 1
    k, x = 1, b % m
    while x != 1:
        x = x * b % m; k += 1
    return k

def int_valued(f, r, M):
    # g(t) = f(r + M t) of degree d is integer-valued on Z iff g(0..d) in Z
    d = sp.degree(f, n) if f.free_symbols else 0
    return all(sp.Rational(f.subs(n, r + M * t)).q == 1 for t in range(d + 1))

classes = []
for C in J['classes']:
    M, r, fam, P = C['M'], C['r'], C['fam'], C['params']
    x, y, z = (poly(c) for c in C['xyz'])
    if fam == 'II2':           # ET Prop 1.9, Type II family 2: n = -4a^2 d (mod f), 4ad | f+1
        a, d, f = P
        assert f == M and (f + 1) % (4 * a * d) == 0, C
        assert (r + 4 * a * a * d) % f == 0, C
        c = sp.Rational(f + 1, 4 * a * d); e = (n + 4 * a * a * d) / f; b = c * e - a
        X, Y, Z = sp.expand(a * b * d), sp.expand(a * c * d * n), sp.expand(b * c * d * n)
        # sextuple on Sigma^II_n (ET (2.13)-(2.21))
        for rel in [4*a*b*d - (n+e), c*e - (a+b), 4*a*b*c*d - (a+b+n*c), 4*a*c*d - (f+1), e*f - (n+4*a*a*d), b*f - (n*c+a)]:
            assert sp.simplify(rel) == 0, (C, rel)
    elif fam == 'D':           # divisor class n = 0 (mod p): scale a solution of 4/p
        (p,) = P
        assert M == p and r % p == 0
        X0, Y0, Z0 = (sp.Rational(x.coeff(n, 1)) * p, sp.Rational(y.coeff(n, 1)) * p, sp.Rational(z.coeff(n, 1)) * p)
        assert all(v.q == 1 and v > 0 for v in (X0, Y0, Z0)) and F(4, p) == F(1, int(X0)) + F(1, int(Y0)) + F(1, int(Z0)), C
        X, Y, Z = X0 * n / p, Y0 * n / p, Z0 * n / p
    else:
        raise SystemExit('unknown family ' + fam)
    # JSON polynomials equal the rebuilt ones (as a multiset)
    assert sorted(map(str, [sp.expand(X), sp.expand(Y), sp.expand(Z)])) == sorted(map(str, [sp.expand(x), sp.expand(y), sp.expand(z)])), C
    assert sp.simplify(4 / n - 1 / x - 1 / y - 1 / z) == 0, C
    for v in (x, y, z):
        assert int_valued(v, r, M), (C, v)
        assert all(sp.Rational(cf) >= 0 for cf in sp.Poly(v, n).all_coeffs()) and v != 0, (C, v)  # positive for n >= 1
    o = ordmod(4, M)
    assert 360 % o == 0, (M, o)
    classes.append((M, r, fam, (x, y, z), o))
    print(f"class M={M:5d} r={r:5d} {fam:3s} ord_M(4)={o:3d} ok")

# coverage of s mod 360 (M odd => 4^s mod M purely periodic with period ord_M(4) | 360, valid for ALL s >= 0)
assert all(M % 2 for M, *_ in classes)
unc = [s for s in range(360) if not any((pow(4, s, M) + K) % M == r for M, r, *_ in classes)]
print('uncovered s mod 360:', unc)
assert unc == [34, 124, 214, 304], unc

# exponential class
u = sp.symbols('u')
A = (64*u**3 + 2*u**2 - 2*u + 66) / 151
N = 256*u**3 + 105; Xe = 64*(u**3 + 1); Ye = N*A; Ze = 32*N*(u+1)*A
assert sp.expand(4*Xe - N) == 151
assert sp.expand(2*(32*u+33)*(u**2-u+1) - 151*A) == 0
assert sp.simplify(4/N - 1/Xe - 1/Ye - 1/Ze) == 0
Au = sp.expand(A.subs(u, 32 + 151*sp.Symbol('t')))
assert all(sp.Rational(cf).q == 1 for cf in sp.Poly(Au, sp.Symbol('t')).all_coeffs()), Au
print('exp class: identity ok; A(32+151t) =', Au, '(integer coefficients)')
o151 = ordmod(4, 151); print('ord_151(4) =', o151, ' 4^10 mod 151 =', pow(4, 10, 151))
for s in range(4, 4 + 3 * 45 * 10):
    if s % 45 == 34:
        assert (s - 4) % 3 == 0 and pow(4, (s - 4) // 3, 151) == 32
# every uncovered residue is = 34 (mod 45)
assert all(s % 45 == 34 for s in unc)

# exact solutions for every s <= SMAX
SMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 2000
lam = [(M, r, [[F(int(c.p), int(c.q)) for c in reversed(sp.Poly(v, n).all_coeffs())] for v in xyz]) for M, r, fam, xyz, o in classes]
def ev(cs, x):
    v = sum(c * x**i for i, c in enumerate(cs)); assert v.denominator == 1; return int(v)
def solve(s):
    nn = 4**s + K
    for M, r, fs in lam:
        if nn % M == r:
            return [ev(cs, nn) for cs in fs], f'ET M={M}'
    assert s % 45 == 34 and s >= 4
    uu = 4**((s - 4) // 3); assert uu % 151 == 32 and 256*uu**3 + 105 == nn
    AA = (64*uu**3 + 2*uu**2 - 2*uu + 66); assert AA % 151 == 0; AA //= 151
    return [64*(uu**3+1), nn*AA, 32*nn*(uu+1)*AA], 'EXP'
cnt = {}
for s in range(SMAX + 1):
    nn = 4**s + K
    (x0, y0, z0), tag = solve(s)
    assert min(x0, y0, z0) > 0 and 4*x0*y0*z0 == nn*(x0*y0 + y0*z0 + z0*x0), s
    cnt[tag.split()[0]] = cnt.get(tag.split()[0], 0) + 1
    if s < 6 or tag == 'EXP' and s < 400: print(s, tag, (x0, y0, z0) if s < 6 else '')
print('exact solutions verified for all s <=', SMAX, cnt)
