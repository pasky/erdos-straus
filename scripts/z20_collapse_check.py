"""z20_collapse_check: (1) symbolic checks of the rearrangements in NORMFORM_CUBIC Thms 1.1'/1.2' with P a free symbol
(degree-free); (2) random search for polynomial Type II / Type I families over P = u^3 + 2v^3 and over the ternary norm
form of Q(cbrt 2), P3 = u^3 + 2v^3 + 4w^3 - 6uvw, solving exactly for A; counts solutions with A,B,C,D not all in Q[P].
Expected (Thms 1.1'/3.1): every solution has all of A,B,C,D in Q[P], except never-valid degenerate families
(A+B=0, or B=b, D=-1/(4b^2), C=-bP); the search skips A+B=0 and reports the rest. Symbolic checks are asserted.
"""
import sympy as sp, random, sys
P, A, B, C, D, E, k, kp, EA, EB = sp.symbols('P A B C D E k kp EA EB')
chk = {}
Aexpr = (P + E) / (4 * B * D)                      # II (b2)
chk['II b2'] = sp.simplify((C * (4 * B * D * Aexpr - P) - (Aexpr + B)) * 4 * B * D - (E * (4 * B * D * C - 1) - P - 4 * B**2 * D)) == 0
Bexpr = (P + E) / (4 * C * D)                      # I c1, B of degree k: A(4BCD-P) - (PB+C) = 0 <=> E(4CD A - P) = P^2 + 4C^2 D
chk['I c1 B'] = sp.simplify(4 * C * D * ((A * (4 * Bexpr * C * D - P)) - (P * Bexpr + C)) - (E * (4 * C * D * A - P) - P**2 - 4 * C**2 * D)) == 0
Cexpr = P / (4 * B * D) + E                        # I c1, C of degree k
chk['I c1 C'] = sp.simplify(4 * A * B * Cexpr * D - P * (A + B) - Cexpr - (E * (4 * B * D * A - 1) - (B + 1 / (4 * B * D)) * P)) == 0
Dexpr = P / (4 * B * C) + E                        # I c1, D of degree k
chk['I c1 D'] = sp.simplify(4 * A * B * C * Dexpr - P * (A + B) - C - (4 * B * C * A * E - P * B - C)) == 0
Ae, Be = k * P + EA, kp * P + EB                   # I c2, mu = k
G = (4 * C * D * k - 1) * EB + (4 * C * D * kp - 1) * EA
chk['I c2'] = sp.expand(4 * C * D * Ae * Be - P * (Ae + Be) - C - ((4 * C * D * k * kp - k - kp) * P**2 + P * G + 4 * C * D * EA * EB - C)) == 0
print("symbolic checks:", chk); assert all(chk.values())

u, v, w = sp.symbols('u v w')
forms = {'u3+2v3': (u**3 + 2 * v**3, (u, v)), 'N3(cbrt2)': (u**3 + 2 * v**3 + 4 * w**3 - 6 * u * v * w, (u, v, w))}
def rp(rng, xs, deg):
    if rng.random() < 0.3: return sp.Integer(rng.choice([-2, -1, 1, 2]))
    mons = sorted(sp.itermonomials(xs, deg), key=sp.default_sort_key)
    return sp.expand(sum(rng.randint(-2, 2) * m for m in mons if rng.random() < 0.6))
def inQP(x, Pf, xs):  # x in Q[P]? degree must be multiple of deg P; check by trying x = sum c_i P^i
    d = sp.Poly(x, *xs).total_degree(); kdeg = sp.Poly(Pf, *xs).total_degree()
    if d % kdeg: return False
    c = sp.symbols('c0:%d' % (d // kdeg + 1)); expr = sp.expand(x - sum(c[i] * Pf**i for i in range(len(c))))
    sol = sp.solve(sp.Poly(expr, *xs).coeffs(), c, dict=True)
    return bool(sol)
N = int(sys.argv[1]) if len(sys.argv) > 1 else 3000
for name, (Pf, xs) in forms.items():
    rng = random.Random(248)
    for typ in ('II', 'I'):
        hits = bad = 0
        for _ in range(N):
            Bp, Cp, Dp = rp(rng, xs, 1), rp(rng, xs, 1), rp(rng, xs, 3)
            if 0 in (Bp, Cp, Dp): continue
            num, den = (Bp + Cp * Pf, 4 * Bp * Cp * Dp - 1) if typ == 'II' else (Pf * Bp + Cp, 4 * Bp * Cp * Dp - Pf)
            den = sp.expand(den)
            if den == 0: continue
            q, r = sp.div(sp.Poly(sp.expand(num), *xs, domain='QQ'), sp.Poly(den, *xs, domain='QQ'))
            if not r.is_zero or q.is_zero: continue
            Ap = q.as_expr()
            if sp.expand(Ap + Bp) == 0: continue          # degenerate (never valid)
            hits += 1
            if not all(inQP(x, Pf, xs) for x in (Ap, Bp, Cp, Dp)):
                bad += 1; print("  NON-COLLAPSING?", name, typ, Ap, Bp, Cp, Dp)
        print(f"{name} Type {typ}: trials {N}, polynomial families {hits}, outside Q[P]: {bad}")

# ---- Thm 3.1 (Type I, unit-group criterion): the rearrangements of cases (i)-(iii), with d = 1/(4ab)
a, b, A1, G = sp.symbols('a b A1 G'); d0 = 1 / (4 * a * b); Aa = a + P * A1
t31 = {}
t31['i: H = A1/a'] = sp.simplify((4 * Aa * b * d0 - 1) / P - A1 / a) == 0
Bb = b + k * P; H = sp.simplify((4 * Aa * Bb * d0 - 1) / P)
t31['ii: H'] = sp.simplify(H - 4 * d0 * (a * k + Bb * A1)) == 0
t31['ii: GH=A+B'] = sp.simplify(sp.expand(H * G - (Aa + Bb)) - sp.expand(A1 * (4 * d0 * G * Bb - P) - (a + Bb - 4 * d0 * G * a * k))) == 0
Dd = d0 + k * P; H = sp.simplify((4 * Aa * b * Dd - 1) / P)
t31['iii: H'] = sp.simplify(H - 4 * b * (a * k + A1 * Dd)) == 0
t31['iii: GH=A+B'] = sp.simplify(sp.expand(H * G - (Aa + b)) - sp.expand(A1 * (4 * b * G * Dd - P) - (a + b - 4 * b * G * a * k))) == 0
Af = sp.Symbol('Afree')  # degenerate family: B=b, D=-1/(4b^2), C=-bP, A arbitrary
t31['degenerate'] = sp.simplify(4 * Af * b * (-b * P) * (-1 / (4 * b**2)) - (P * (Af + b) + (-b * P))) == 0
print("Thm 3.1 checks:", t31); assert all(t31.values())
