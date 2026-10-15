"""R251 from-scratch checker for MENU_STERILITY Theorems B/C (ES for all n = 3*2^s + 1).
No imports of z15_/z8/ec_cover. Rules are rebuilt by hand:
  * SG window m = 11 (CAP_DOWN Lemma 1.1): K = (n+11)/4, 4/n = 1/K + 11/(nK);
    11/(nK) = 1/y + 1/z with y = n(K+d)/11, z = nK(K+d)/(11 d).
  * ET classes rebuilt from ET Prop 1.9-type identities, re-derived below.
"""
import sys
from fractions import Fraction as F
import sympy as sp

X, N = sp.symbols('X n')
fp, fm = 2*X**2 + 2*X + 1, 2*X**2 - 2*X + 1
nX = 48*X**4 + 1
KX = sp.expand((nX + 11) / 4)
assert sp.expand(KX - 3*fp*fm) == 0

def sg_rule(a, b, c):
    d = 3**a * fp**b * fm**c
    x = KX
    y = nX*(KX + d)/11
    z = nX*KX*(KX + d)/(11*d)
    return d, x, y, z

def check_identity(x, y, z, n):
    return sp.simplify(1/x + 1/y + 1/z - 4/n) == 0

# ---- (i) Theorem B literally as stated
tb = [3*(4*X**4+1), 6*nX*fm*(X**2+X+2)/11, 2*nX*(4*X**4+1)*(X**2+X+2)/11]
assert check_identity(*tb, nX), 'Thm B identity'
print('Thm B identity OK')
d, x, y, z = sg_rule(0, 0, 1)
d9 = 9*fm
for a_, b_ in zip(tb, [KX, nX*(KX+d9)/11, nX*KX*(KX+d9)/(11*d9)]):
    assert sp.simplify(a_ - b_) == 0
print('Thm B == Lemma 1.1 with d = 9 f-  (a,b,c)=(2,0,1)')
for r in range(11):
    print(' X mod 11 =', r, ' X^2+X+2 mod 11 =', (r*r+r+2) % 11)

def poly_int_on_class(expr, r, mod=11):
    """expr = P(X)/q with P in Z[X]; integer on X = r mod `mod` iff q | P(t) for t = r + mod*k
    -- checked by: P in Z[X] (exact), denominator q | mod^k, and P(r + mod*j) % q == 0 for j in range(q)."""
    num, den = sp.fraction(sp.together(expr))
    num, den = sp.Poly(sp.expand(num), X), sp.Poly(sp.expand(den), X)
    if den.degree() > 0:
        q, rem = sp.div(num, den)
        if not rem.is_zero:
            return False, 'non-polynomial'
        num, den = q, sp.Poly(1, X)
    # num may have rational coeffs; clear
    cs = [sp.Rational(cf) for cf in num.all_coeffs()]
    L = sp.ilcm(*[cf.q for cf in cs]) * int(den.LC())
    P = sp.Poly(sp.expand(num.as_expr()*L/den.LC()), X)
    assert all(cf.is_integer for cf in P.all_coeffs())
    # integer-valued on class iff L | P(r + mod*j) for all j mod L (periodicity of P mod L)
    ok = all(int(P.eval(r + mod*j)) % L == 0 for j in range(L))
    return ok, L

# ---- (ii) all SG rules: which (a,b,c) with 0<=a,b,c<=2 fire on which X mod 11 / s mod 40
fires = {}
for a in range(3):
    for b in range(3):
        for c in range(3):
            d, x, y, z = sg_rule(a, b, c)
            assert check_identity(x, y, z, nX)
            for r in range(11):
                oky, _ = poly_int_on_class(y, r)
                okz, _ = poly_int_on_class(z, r)
                if oky and okz:
                    fires.setdefault(r, []).append((a, b, c))
print('SG window-11 firing residues X mod 11:', {r: v for r, v in sorted(fires.items())})
# X = 2^((s-4)/4); X mod 11 as function of s mod 40 (s = 0 mod 4)
sres = {}
for s in range(0, 40, 4):
    e = (s - 4) // 4 % 10
    r = pow(2, e, 11)
    sres[s] = (r, fires.get(r, []))
print('s mod 40 -> (X mod 11, rules):', sres)
claimed = {0: (0,2,1), 8: (0,0,2), 12: (0,2,1), 16: (0,2,0), 20: (0,1,2), 28: (0,2,0), 32: (0,1,2), 36: (0,0,2)}
for s, abc in claimed.items():
    assert abc in sres[s][1], (s, abc)
print('author rule table confirmed; dead s mod 40:', [s for s in sres if not sres[s][1]])
# positivity: all factors positive for real X (f+-, K+d, n), checked by discriminants
assert sp.discriminant(fp, X) < 0 and sp.discriminant(fm, X) < 0

# ---- (iii) ET / divisor classes, rebuilt by hand (x,y,z as polynomials in n)
ET = [  # (modulus, residue of n, x, y, z)
    (7, 0, 2*N/7, 15*N/7, 30*N),
    (7, 6, 2*(N+1)/7, 2*N, 2*N*(N+1)/7),
    (5, 0, 2*N/5, 4*N/5, 4*N),
    (15, 7, (4*N+2)/15, 4*N, 2*N*(4*N+2)/15),  # 4/n-15/(4n+2)-1/(4n) = 30/(4n(4n+2))
    (15, 13, (4*N+8)/15, 4*N, N*(4*N+2)/15 * 0 + N*(4*N+8)/30),  # placeholder, fixed below
    (61, 0, 16*N/61, 326*N/61, 2608*N),
]
# re-derive the 15/13 class: x = (4n+8)/15 -> 4/n - 1/x = (4x - n)/(n x)
x13 = (4*N+8)/15
rem = sp.simplify(4/N - 1/x13)
print('15|13 remainder 4/n - 1/x =', sp.factor(rem))
ET[4] = (15, 13, x13, 4*N, None)
z13 = sp.simplify(1/(rem - 1/(4*N)))
ET[4] = (15, 13, x13, 4*N, sp.factor(z13))
print('15|13 class z =', sp.factor(z13))
for M, r, x, y, z in ET:
    assert sp.simplify(1/x + 1/y + 1/z - 4/N) == 0, (M, r)
    for e in (x, y, z):
        P = sp.Poly(sp.expand(e), N)
        L = sp.ilcm(*[sp.Rational(cf).q for cf in P.all_coeffs()])
        Pi = sp.Poly(sp.expand(e*L), N)
        assert all(int(Pi.eval(r + M*j)) % L == 0 for j in range(L)), (M, r, e)
        assert all(cf >= 0 for cf in P.all_coeffs())
print('ET classes: identities, integrality, positivity OK')

# ---- (iv) coverage of every s modulo P = lcm(40, ords)
from math import lcm
ords = {M: sp.n_order(2, M) for M in (5, 7, 15, 61)}
P = lcm(40, *ords.values())
print('ord_M(2):', ords, ' period', P)
def covered(s):
    if s % 4 == 0 and sres[s % 40][1]:
        return 'SG'
    for M, r, *_ in ET:
        if (3*pow(2, s, M) + 1) % M == r:
            return 'ET%d|%d' % (M, r)
    return None
unc = [s for s in range(10, 10 + P) if covered(s) is None]
print('uncovered s mod', P, ':', unc)
assert not unc

# ---- (v) exact solutions s <= SMAX
SMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 2000
def solution(s):
    n = 3*2**s + 1
    if s % 4 == 0 and s >= 4 and sres[s % 40][1]:
        Xv = 2**((s-4)//4)
        a, b, c = sres[s % 40][1][0]
        d, x, y, z = sg_rule(a, b, c)
        return n, [int(sp.Rational(e.subs(X, Xv))) for e in (x, y, z)]
    for M, r, x, y, z in ET:
        if n % M == r:
            return n, [int(sp.Rational(e.subs(N, n))) for e in (x, y, z)]
    return n, None
bad = []
for s in range(0, SMAX + 1):
    n, sol = solution(s)
    if sol is None:
        bad.append(s); continue
    assert all(v > 0 for v in sol)
    assert F(1, sol[0]) + F(1, sol[1]) + F(1, sol[2]) == F(4, n), s
print('s with no rule (need brute force):', bad)
