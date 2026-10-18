# z40_seeded.py (O270): seeded search for menu II-d (d constant, a(Y) linear) on n = c0 Y^D + 1 at mu = 0.
# Seed (A, d, X, X') with X X' = 4^J + 4 d A^2, X = -4^J, X' = -1 mod odd(A d) (EXP_15 (C2) with A = a(1)).
# Unknowns: A0 = a(0) and phi = value at Y = 0 of the quadratic factor g. a(Y) = A0 + (A - A0) Y, y0 = root of a.
# role fp: g = f' quadratic through (1, X'), (0, phi), (y0, -1); role f: g = f through (1, X), (0, phi), (y0, -n(y0)).
# Condition g | B = n + 4 d a^2 (2 polynomial equations in A0, phi); rational solutions are tested exactly by
# MENU_LADDER Lemma 2.1 (+ positive leading coefficients), as in z40_trinom.py.
# Usage: z40_seeded.py c0 DLIST SEEDFILE|boxed
import sys
import sympy as sp
from fractions import Fraction as F
c0 = int(sys.argv[1]); DL = [int(x) for x in sys.argv[2].split(',')]; J = (c0 + 1).bit_length() // 2; FJ = 4 ** J
def ok1(x):
    x = F(int(sp.numer(x)), int(sp.denom(x))); dd = x.denominator
    while dd % 2 == 0: dd //= 2
    return dd == 1
def ok0(x): return int(sp.denom(sp.Rational(x))) % 2 == 1
seeds = []
if sys.argv[3] == 'boxed':
    for a in range(1, 82):
        for d in range(1, 22):
            for m1 in range(1, 37):
                den = a * d * m1 - FJ
                if den <= 0 or (m1 + 4 * a) % den: continue
                m2 = (m1 + 4 * a) // den
                if a * (m1 * m2 * d - 4) == m1 + FJ * m2 and (m1 * a * d - FJ) * (m2 * a * d - 1) == FJ + 4 * a * a * d:
                    seeds.append((sp.Integer(a), d, m1 * a * d - FJ, m2 * a * d - 1))
print(len(seeds), 'seeds', flush=True)
Y, A0, phi = sp.symbols('Y A0 phi')
hits = 0; nsol = 0
for D in DL:
    n = c0 * Y ** D + 1
    for (A, d, X, Xp) in seeds:
        a = A0 + (A - A0) * Y; y0 = -A0 / (A - A0)
        B = sp.expand(n + 4 * d * a ** 2)
        for role in ('fp', 'f'):
            v1 = Xp if role == 'fp' else X
            vy = -1 if role == 'fp' else -(c0 * y0 ** D + 1)
            # quadratic through (0, phi), (1, v1), (y0, vy)
            g = sp.interpolate([(0, phi), (1, v1), (y0, vy)], Y)
            num, den = sp.fraction(sp.together(g))
            G = sp.Poly(sp.expand(num), Y)
            if G.degree() != 2: continue
            r = sp.Poly(sp.rem(sp.Poly(B, Y), G), Y)
            eqs = [sp.numer(sp.together(cf)) for cf in r.all_coeffs()]
            eqs = [e for e in eqs if e != 0]
            if not eqs: continue
            sols = []
            if len(eqs) == 1:
                continue
            R = sp.Poly(sp.resultant(eqs[0], eqs[1], phi), A0)
            if R.is_zero: print('degenerate', D, A, d, role); continue
            for fac, _ in sp.factor_list(R.as_expr(), A0)[1]:
                P = sp.Poly(fac, A0)
                if P.degree() != 1: continue
                a0v = -P.all_coeffs()[1] / P.all_coeffs()[0]
                gs = [sp.Poly(e.subs(A0, a0v), phi) for e in eqs]
                gg = sp.gcd(gs[0], gs[1])
                for ph in sp.roots(gg, filter='Q') if gg.degree() > 0 else []:
                    sols.append({A0: a0v, phi: ph})
            for so in sols:
                if A0 not in so or phi not in so: continue
                a0v, phv = so[A0], so[phi]
                if not (a0v.is_rational and phv.is_rational): continue
                if a0v == A or a0v == 0: continue
                nsol += 1
                av = sp.expand(a.subs(A0, a0v)); gv = sp.expand(g.subs({A0: a0v, phi: phv}))
                Bv = sp.expand(n + 4 * d * av ** 2); other, rr = sp.div(Bv, gv, Y)
                if rr != 0: continue
                f, fp = (other, gv) if role == 'fp' else (gv, other)
                c = sp.cancel((fp + 1) / (4 * av * d)); b = sp.cancel((f + n) / (4 * av * d))
                if not (c.is_polynomial(Y) and b.is_polynomial(Y)): continue
                vals = [av, b, c]
                lcs = [sp.Poly(v, Y).LC() for v in vals]
                good = all(ok1(v.subs(Y, 1)) and ok0(v.subs(Y, 0)) for v in vals) and all(l > 0 for l in lcs)
                tag = 'HIT' if good else 'alg'
                if good: hits += 1
                print(tag, 'D=%d seed=(%s,%d,%d,%d) role=%s A0=%s phi=%s a=%s c=%s lc=%s' % (D, A, d, X, Xp, role, a0v, phv, av, sp.factor(c), lcs), flush=True)
print('c0=%d D in %s: %d rational (A0, phi) solutions, %d valid families' % (c0, DL, nsol, hits))
