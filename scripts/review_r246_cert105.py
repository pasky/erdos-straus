# R246 from-scratch checker for SYNTHESIS_SPARKS6 Thm 1.1 (ES for all n = 4^s + 105).
# Does NOT import any s6_* / z8 / ec_cover code. Reads only the JSON class list.
import json, sys
from fractions import Fraction as F
from math import gcd
import sympy as sp

n, u, t = sp.symbols('n u t')
C = json.load(open('data/s6_cert105_et.json'))
assert C['k'] == 105 and C['c0'] == 1 and C['b'] == 4
classes = []
for i, cl in enumerate(C['classes']):
    M, r = cl['M'], cl['r']
    X = [sum(sp.Rational(c) * n**j for j, c in enumerate(p)) for p in cl['xyz']]
    # (1) symbolic ES identity
    assert sp.expand(4*X[0]*X[1]*X[2] - n*(X[0]*X[1] + X[1]*X[2] + X[0]*X[2])) == 0, i
    # (2) integer-valued on n = r + M t : expand in t and test values at deg+1 consecutive t
    #     (a rational poly integer-valued at deg+1 consecutive integers is integer-valued on Z)
    for P in X:
        Q = sp.Poly(sp.expand(P.subs(n, r + M*t)), t)
        d = Q.degree()
        for tt in range(-1, d + 1):
            v = Q.eval(tt)
            assert v.q == 1, (i, P, tt)
    # (3) positivity: all coefficients in n nonnegative and polynomial nonzero => positive for n>0
    for P in X:
        co = sp.Poly(P, n).all_coeffs()
        assert all(c >= 0 for c in co) and any(c > 0 for c in co), (i, P)
    # periodicity: M odd, ord_M(4) | 360
    assert M % 2 == 1
    o = sp.n_order(4, M)
    assert 360 % o == 0, (M, o)
    classes.append((M, r, X, cl['fam'], o))
    print(f"class {i:2d}: M={M:5d} r={r:5d} fam={cl['fam']:3s} ord_M(4)={o:3d} gcd(M,105)={gcd(M,105)}")

# (4) coverage of s mod 360 (n_s mod M depends only on s mod ord_M(4), valid for ALL s>=0 since M odd)
unc = [s for s in range(360) if not any((pow(4, s, M) + 105) % M == r % M for M, r, *_ in classes)]
print("uncovered s mod 360:", unc)
assert unc == [34, 124, 214, 304]

# (5) exponential class
x = 64*(u**3 + 1); A = (64*u**3 + 2*u**2 - 2*u + 66) / 151; N = 256*u**3 + 105
assert sp.simplify(4/N - 1/x - 1/(N*A) - 1/(32*N*(u + 1)*A)) == 0
assert sp.expand(4*x - N) == 151
assert sp.expand(2*(32*u + 33)*(u**2 - u + 1) - 151*A) == 0
QA = sp.Poly(sp.expand(A.subs(u, 32 + 151*t)), t)
assert all(QA.eval(tt).q == 1 for tt in range(-1, 4))
# A > 0 for u >= 1: 64u^3 - 2u + ... >0
assert all(c > 0 for c in [64, 66]) and sp.Poly(64*u**3 + 2*u**2 - 2*u + 66, u).eval(1) > 0
print("ord_151(4) =", sp.n_order(4, 151), " 4^10 mod 151 =", pow(4, 10, 151))
for s in range(34, 34 + 45*60, 45):
    assert (s - 4) % 3 == 0 and pow(4, (s - 4)//3, 151) == 32
print("exp class identity / integrality / s=34 (45) => u=32 (151): OK")

# (6) explicit exact solutions for every s <= SMAX
SMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 2000
cnt_exp = 0
for s in range(SMAX + 1):
    nn = 4**s + 105
    sol = None
    for M, r, X, fam, o in classes:
        if nn % M == r % M:
            sol = [int(P.subs(n, nn)) for P in X]; break
    if sol is None:
        assert s % 45 == 34, s
        uu = 4**((s - 4)//3); assert uu % 151 == 32 and 256*uu**3 + 105 == nn
        AA, rem = divmod(64*uu**3 + 2*uu**2 - 2*uu + 66, 151); assert rem == 0
        sol = [64*(uu**3 + 1), nn*AA, 32*nn*(uu + 1)*AA]; cnt_exp += 1
    a, b, c = sol
    assert min(sol) > 0 and 4*a*b*c == nn*(a*b + b*c + c*a), s
print(f"exact ES solutions verified for all 0 <= s <= {SMAX}; {cnt_exp} via exponential class")
