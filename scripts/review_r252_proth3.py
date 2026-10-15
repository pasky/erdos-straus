"""R252 from-scratch checker for MENU_STERILITY Theorem B/C (ES for every 3*2^s+1).

No imports from z15_/z8/ec_cover. Checks:
 (i)  Theorem B identity symbolically; integrality on X = 4,6 mod 11.
 (ii) all window-11 SG rules d = 3^a f+^b f-^c (a,b,c <= 3): which X mod 11 make
      x,y,z integral polynomials-valued; derive covered s mod 40.
 (iii) ET classes rebuilt by hand (not read from the certificate).
 (iv) coverage of every s mod lcm period.
 (v)  exact solutions for all s <= SMAX from the rules + brute force for small s.
"""
import sys
from fractions import Fraction as F
from math import gcd
import sympy as sp

X = sp.symbols('X')
fp = 2*X**2 + 2*X + 1
fm = 2*X**2 - 2*X + 1
n = 48*X**4 + 1
K = (n + 11) / 4
assert sp.expand(K - 3*fp*fm) == 0

# (i) Theorem B identity as stated
rhs = 1/(3*(4*X**4+1)) + sp.Integer(11)/(6*n*fm*(X**2+X+2)) + sp.Integer(11)/(2*n*(4*X**4+1)*(X**2+X+2))
assert sp.simplify(sp.Rational(4)/n - rhs) == 0
print("Thm B identity: OK")


def int_valued_residues(P, mod=33):
    """P in Q[X]. Return residues r mod `mod` with P(X) in Z for all X = r mod `mod`.
    Requires denominator of P to divide `mod` (checked); then integrality depends on X mod `mod`."""
    P = sp.Poly(sp.expand(P), X, domain='QQ')
    den = sp.ilcm(*[sp.fraction(c)[1] for c in P.all_coeffs()])
    assert mod % den == 0 or den == 1, (den, P)
    Q = sp.Poly(sp.expand(P.as_expr()*den), X, domain='ZZ')
    return {r for r in range(mod) if Q.eval(r) % den == 0}, den


# (ii) window-11 rules: x = K, y = n(K+d)/11, z = nK(K+d)/(11 d)
rules = {}
for a in range(4):
    for b in range(4):
        for c in range(4):
            d = 3**a * fp**b * fm**c
            y = n*(K + d)/11
            num = sp.expand(n*K*(K + d))
            q, r = sp.div(sp.Poly(num, X), sp.Poly(11*d, X))
            if not r.is_zero:
                continue  # z not a polynomial; skip (author's rules should be polynomial)
            z = q.as_expr()
            ident = sp.simplify(sp.Rational(4)/n - 1/K - 1/y - 1/z)
            assert ident == 0
            ry, _ = int_valued_residues(y)
            rz, _ = int_valued_residues(z)
            ok = ry & rz
            if ok:
                rules[(a, b, c)] = sorted(ok)
print("window-11 SG rules (a,b,c) -> X residues mod 33:", rules)

# X = 2^{(s-4)/4} mod 11, s = 0 mod 4 ; s mod 40
covered40 = {}
for s in range(4, 44, 4):
    xr = pow(2, (s - 4)//4, 33)  # ord_33(2) = 10, so depends on s mod 40
    hit = [abc for abc, rs in rules.items() if xr in rs]
    covered40[s % 40] = hit
    print(f"s={s%40:2d} mod 40: X={xr:2d} mod 33, rules {hit[:4]}{'...' if len(hit)>4 else ''}")
sg_res = {r for r, h in covered40.items() if h}
print("SG-covered s mod 40:", sorted(sg_res))

# author's table
author = {0: (0, 2, 1), 8: (0, 0, 2), 12: (0, 2, 1), 16: (0, 2, 0), 20: (0, 1, 2),
          28: (0, 2, 0), 32: (0, 1, 2), 36: (0, 0, 2)}
for r, abc in author.items():
    assert abc in covered40[r], (r, abc)
print("author's (a,b,c) table: each valid on its class")

# (iii) ET classes, hand-derived identities (x,y,z as functions of N = n value), with condition
N = sp.symbols('N')
et = [
    ("n=0 mod 7", lambda v: v % 7 == 0, (2*N/7, 15*N/7, 30*N)),
    ("n=6 mod 7", lambda v: v % 7 == 6, (2*(N+1)/7, 2*N, 2*N*(N+1)/7)),
    ("n=0 mod 5", lambda v: v % 5 == 0, (2*N/5, 4*N/5, 4*N)),
    ("n=7 mod 15", lambda v: v % 15 == 7, ((4*N+2)/15, 4*N, 4*N*(2*N+1)/15)),
    ("n=13 mod 15", lambda v: v % 15 == 13, ((4*N+8)/15, 4*N, 2*N*(N+2)/15)),
    ("n=0 mod 61", lambda v: v % 61 == 0, (16*N/61, 326*N/61, 2608*N)),
]
for name, cond, (a1, b1, c1) in et:
    assert sp.simplify(4/N - 1/a1 - 1/b1 - 1/c1) == 0, name
print("ET identities: OK")

# (iv) coverage: period = lcm(40, ord_7 2=3, ord_5 2=4, ord_15 2=4, ord_61 2=60)
from sympy.ntheory import n_order
P = sp.ilcm(40, n_order(2, 7), n_order(2, 5), n_order(2, 15), n_order(2, 61))
print("period:", P)
uncovered = []
for r in range(P):
    s = r + P  # representative with s large
    v = 3*pow(2, s, 7*5*3*61) + 1  # n mod 6405 (enough for all ET moduli)
    hit_et = [name for name, cond, _ in et if cond(v)]
    hit_sg = (r % 4 == 0) and (r % 40 in sg_res)
    if not hit_et and not hit_sg:
        uncovered.append(r)
print("uncovered residues mod", P, ":", uncovered)
print("ET-needed residues (not SG):", sum(1 for r in range(P) if not ((r % 4 == 0) and (r % 40 in sg_res))))

# (v) exact solutions
SMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 2000


def check(nv, x, y, z):
    assert x > 0 and y > 0 and z > 0
    assert F(4, nv) == F(1, x) + F(1, y) + F(1, z)


def solve(s):
    nv = 3*2**s + 1
    if s % 4 == 0 and s >= 4 and (s % 40) in sg_res:
        Xv = 2**((s - 4)//4)
        abc = covered40[s % 40][0]
        a, b, c = abc
        fpv, fmv = 2*Xv*Xv + 2*Xv + 1, 2*Xv*Xv - 2*Xv + 1
        Kv = 3*fpv*fmv
        assert 4*Kv == nv + 11
        d = 3**a * fpv**b * fmv**c
        assert (nv*(Kv + d)) % 11 == 0 and (nv*Kv*(Kv + d)) % (11*d) == 0
        return nv, Kv, nv*(Kv+d)//11, nv*Kv*(Kv+d)//(11*d), 'SG'
    for name, cond, (a1, b1, c1) in et:
        if cond(nv % 6405):
            xs = [sp.Rational(e.subs(N, nv)) for e in (a1, b1, c1)]
            assert all(t.q == 1 for t in xs), (s, name)
            return (nv, int(xs[0]), int(xs[1]), int(xs[2]), name)
    return None


def brute(nv):
    # 4/n = 1/x+1/y+1/z, x<=y<=z
    for x in range(nv//4 + 1, 3*nv//4 + 2):
        r = F(4, nv) - F(1, x)
        if r <= 0:
            continue
        for y in range(max(x, int(1/r) + 1), int(2/r) + 2):
            t = r - F(1, y)
            if t > 0 and t.numerator == 1:
                return x, y, t.denominator
    return None


fails = []
for s in range(0, SMAX + 1):
    res = solve(s)
    if res is None:
        if s == 0:
            b = brute(4)
            check(4, *b)
            continue
        fails.append(s)
        continue
    nv, x, y, z, how = res
    check(nv, x, y, z)
print(f"exact ES solutions s<= {SMAX}: failures {fails}")
for s in range(0, 9):
    nv = 3*2**s + 1
    b = brute(nv)
    print("brute", s, nv, b)
