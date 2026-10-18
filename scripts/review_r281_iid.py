"""R281 from-scratch search: menu II-d (d constant, a = alpha (Y - y0) linear) on n = c0 Y^3 + 1, D = 3, near mu = 0.
B = n + 4 d a^2 must split as (linear) x (quadratic), i.e. have a rational root r. Parametrise by (r, y0):
  d alpha^2 = -(c0 r^3 + 1) / (4 (r - y0)^2)   (needs c0 r^3 + 1 < 0).
f' = 4acd - 1 must satisfy f'(y0) = -1 (a | f'+1); f'(y0) = -1 fixes the scalar of whichever factor is f'.
Then b = (f + n)/(4ad), c = (f' + 1)/(4ad) are polynomials; validity near mu = 0 iff (MENU_LADDER Lemma 2.1)
a, b, c in Z[1/2] at Y = 1, in Z_(2) at Y = 0, and positive leading coefficients (alpha > 0, f, f' > 0 at infinity).
Unlike z40_trinom (monic quadratic coefficients with denominators | 8) this enumerates r, y0 with ANY denominator <= DEN.
Usage: review_r281_iid.py c0 H DEN TMAX"""
import sys
from fractions import Fraction as F
from math import isqrt
import sympy as sp

c0, H, DEN, TMAX = map(int, sys.argv[1:5])
Y = sp.symbols('Y')
n = c0 * Y**3 + 1

def odd_den(x):
    return F(x).denominator % 2 == 1
def z_half(x):
    dd = F(x).denominator
    while dd % 2 == 0:
        dd //= 2
    return dd == 1
def ratsqrt(x):
    if x < 0:
        return None
    a, b = isqrt(x.numerator), isqrt(x.denominator)
    return F(a, b) if a * a == x.numerator and b * b == x.denominator else None
def sqfree(m):
    out = 1
    for pr, e in sp.factorint(m).items():
        if e % 2:
            out *= pr
    return out

rats = sorted({F(i, j) for j in range(1, DEN + 1) for i in range(-H * j, H * j + 1)})
negr = [r for r in rats if c0 * r**3 + 1 < 0]
alg = valid = 0
for r in negr:
    nr = c0 * r**3 + 1
    for y0 in rats:
        if y0 == r:
            continue
        delta = -nr / (4 * (r - y0) ** 2)  # = d alpha^2 > 0
        ny0 = c0 * y0**3 + 1
        # role A: f' = lam (Y - r): lam (y0 - r) = -1
        # role B: f = kap (Y - r), f' = B/f: f'(y0) = n(y0) / (kap (y0 - r)) = -1  => kap = -n(y0)/(y0 - r)
        for role in ('fp_lin', 'f_lin'):
            s = -1 / (y0 - r) if role == 'fp_lin' else -ny0 / (y0 - r)
            if s <= 0:
                continue
            alg += 1
            sf = sqfree(delta.numerator * delta.denominator)
            for t in range(1, TMAX + 1):
                d = sf * t * t
                al = ratsqrt(delta / d)
                if al is None or al <= 0:
                    continue
                a = sp.Rational(al.numerator, al.denominator) * (Y - sp.Rational(y0.numerator, y0.denominator))
                B = sp.expand(n + 4 * d * a**2)
                lin = sp.Rational(s.numerator, s.denominator) * (Y - sp.Rational(r.numerator, r.denominator))
                q, rem = sp.div(B, lin, Y)
                assert rem == 0
                fp, f = (lin, q) if role == 'fp_lin' else (q, lin)
                if sp.Poly(f, Y).LC() <= 0 or sp.Poly(fp, Y).LC() <= 0:
                    continue
                b = sp.cancel((f + n) / (4 * a * d))
                c = sp.cancel((fp + 1) / (4 * a * d))
                if not (b.is_polynomial(Y) and c.is_polynomial(Y)):
                    continue
                if sp.Poly(b, Y).LC() <= 0 or sp.Poly(c, Y).LC() <= 0:
                    continue
                vals1 = [F(str(e.subs(Y, 1))) for e in (a, b, c)]
                vals0 = [F(str(e.subs(Y, 0))) for e in (a, b, c)]
                if all(z_half(v) for v in vals1) and all(odd_den(v) for v in vals0):
                    valid += 1
                    print("VALID", c0, "a =", a, "d =", d, "b =", b, "c =", c)
print(f"c0={c0} D=3 H={H} DEN<={DEN} TMAX={TMAX}: {alg} algebraic (r,y0,role), {valid} valid families")
