# z40_trinom.py (O270): one-constant moving-gap Type II families ("menu II-d", d constant, a(Y) = a1 (Y - y0) linear)
# on n = c0 Y^D + 1 at mu = 0 (Y = 2^{s/D}). Identity: f f' = B := n + 4 d a^2, f = 4abd - n (gap), f' = 4acd - 1.
# Search: a quadratic factor g = lam (Y^2 + pY + q) of B, either g = f' (needs g(y0) = -1) or g = f (needs g(y0) = -n(y0)).
# With R = r1 Y + r0 := (c0 Y^D + 1) mod (Y^2 + pY + q): 4 delta (p + 2 y0) = r1, 4 delta (y0^2 - q) = -r0, delta = d a1^2,
# so y0 solves y0^2 + 2(r0/r1) y0 + (p r0/r1 - q) = 0 (rational iff disc is a square). Then d = delta / a1^2 (d integer,
# a1 > 0 rational), and validity near mu = 0 is tested EXACTLY by MENU_LADDER Lemma 2.1 on a, b, c, d (values at Y = 1 in
# Z[1/2], at Y = 0 in Z_(2)) + positive leading coefficients.
# Usage: z40_trinom.py c0 D H DEN TMAX      (p = i/j, q = k/l, |i|,|k| <= H, j,l | DEN; d = sqfree(delta) * t^2, t <= TMAX)
import sys
from fractions import Fraction as F
from math import isqrt
import sympy as sp
c0, D, H, DEN, TMAX = map(int, sys.argv[1:6])
def ok1(x):   # in Z[1/2]
    x = F(x); d = x.denominator
    while d % 2 == 0: d //= 2
    return d == 1
def ok0(x):   # in Z_(2)
    return F(x).denominator % 2 == 1
def ratsqrt(x):
    x = F(x)
    if x < 0: return None
    a, b = isqrt(x.numerator), isqrt(x.denominator)
    return F(a, b) if a * a == x.numerator and b * b == x.denominator else None
def sqfree(n):
    out = 1
    for pr, e in sp.factorint(n).items():
        if e % 2: out *= pr
    return out
def rem(p, q):     # (c0 Y^D + 1) mod (Y^2 + pY + q): Y^k = u_k Y + v_k
    u, v = F(1), F(0)
    for _ in range(D - 1):
        u, v = -p * u + v, -q * u
    return c0 * u, c0 * v + 1
dens = [j for j in range(1, DEN + 1) if DEN % j == 0]
Ps = sorted({F(i, j) for i in range(-H, H + 1) for j in dens})
Y = sp.symbols('Y'); hits = 0; algebraic = 0
for p in Ps:
    for q in Ps:
        r1, r0 = rem(p, q)
        if r1 == 0: continue
        h = r0 / r1; disc = h * h - p * h + q
        s = ratsqrt(disc)
        if s is None: continue
        for y0 in {-h + s, -h - s}:
            if p + 2 * y0 == 0: continue
            delta = r1 / (4 * (p + 2 * y0))
            if delta <= 0: continue
            g0 = y0 * y0 + p * y0 + q
            if g0 == 0: continue
            for role in ('fp', 'f'):
                lam = (F(-1) if role == 'fp' else -(c0 * y0 ** D + 1)) / g0
                if lam <= 0: continue
                algebraic += 1
                g = lam * (Y ** 2 + p * Y + q); n = c0 * Y ** D + 1
                sf = sqfree(delta.numerator * delta.denominator)
                for t in range(1, TMAX + 1):
                    d = sf * t * t; a1 = ratsqrt(delta / d)
                    if a1 is None or a1 <= 0: continue
                    a = a1 * (Y - y0); B = sp.expand(n + 4 * d * a ** 2)
                    other, r = sp.div(B, g, Y)
                    assert r == 0
                    f, fp = (other, g) if role == 'fp' else (g, other)
                    c = sp.cancel((fp + 1) / (4 * a * d)); b = sp.cancel((f + n) / (4 * a * d))
                    if not (c.is_polynomial(Y) and b.is_polynomial(Y)): continue
                    vals = [a, b, c]
                    if not all(ok1(v.subs(Y, 1)) and ok0(v.subs(Y, 0)) for v in vals): continue
                    if not all(sp.Poly(v, Y).LC() > 0 for v in vals): continue
                    hits += 1
                    print('HIT D=%d role=%s p=%s q=%s y0=%s d=%d a=%s b=%s c=%s' % (D, role, p, q, y0, d, a, sp.factor(b), sp.factor(c)), flush=True)
print('c0=%d D=%d H=%d DEN=%d: %d algebraic (y0, delta, lam) configurations, %d valid families near mu = 0' % (c0, D, H, DEN, algebraic, hits))
