"""Exact exponent checks for es-count-note.tex, Theorems 3.? (12/37) and (exponent pairs).

Run:  uv run --with sympy python paper/es-count-note.checks.py
For the exponent pair (kappa, kappa+1/2), theta* = 4/(13-4 kappa).  In Case 2 of the proof
(alpha, gamma >= theta*, beta >= alpha, alpha+beta+gamma = 1) every term of the block bound
must have exponent <= theta*, with 0 < 2 rho* < gamma.  The terms are affine in (alpha, gamma),
so it suffices to check the three vertices of the triangle.  For kappa = 1/6 the third-derivative
test gives one extra pair of terms (e - rho, rho + e), checked separately.
"""
import sympy as sp
k = sp.symbols('kappa', nonnegative=True)

def terms(a, b, g, kap, third=False):
    rho = ((1 + kap) * b - kap - g / 2) / 3
    d = kap + g / 2 - kap * b
    T = {'V/P': b - rho, 'V/(WP)': b - g - rho, 'd/P': d - rho, '1/P': -rho,
         'V/P^2': b - 2 * rho, 'V/W': b - g, 'P^2 d': 2 * rho + d, 'P^3': 3 * rho}
    if third:
        e = b / 6 + g - sp.Rational(1, 6)
        T.update({'e/P': e - rho, 'P e': rho + e})
    return rho, T

th = 4 / (13 - 4 * k)
verts = [(th, 1 - 2 * th, th), (th, th, 1 - 2 * th), ((1 - th) / 2, (1 - th) / 2, th)]
print('Deficits theta* - (term), and the side conditions 2 rho*, gamma - 2 rho*, as factored')
print('rational functions of kappa.  For 0 <= kappa < 1/4 the denominator 4 kappa - 13 is negative,')
print('4 kappa - 1 <= 0, and each factor has constant sign, so every deficit is >= 0 (strictly > 0')
print('except the two balanced terms at the first vertex, which are 0 by the choice of rho*).')
for (a, b, g) in verts:
    rho, T = terms(a, b, g, k)
    print('vertex', [sp.simplify(x) for x in (a, b, g)])
    for name, ex in T.items():
        print('   %-7s' % name, sp.factor(sp.simplify(th - ex)))
    print('   2rho*  ', sp.factor(2 * rho), '   gamma-2rho*', sp.factor(g - 2 * rho))

# exact checks at the three named instances, including the third-derivative extra terms at kappa=1/6
for kap, third in [(sp.Rational(1, 6), True), (sp.Rational(13, 84), False), (sp.Integer(0), False)]:
    t = sp.Rational(4) / (13 - 4 * kap)
    print('kappa =', kap, ' theta* =', t)
    for (a, b, g) in [(t, 1 - 2 * t, t), (t, t, 1 - 2 * t), ((1 - t) / 2, (1 - t) / 2, t)]:
        rho, T = terms(a, b, g, kap, third)
        m = max(T.values())
        assert m <= t and rho > 0 and 2 * rho < g
        print('   vertex', (a, b, g), 'rho* =', rho, 'max exponent =', m)
rho, T = terms(sp.Rational(1, 3), sp.Rational(1, 3), sp.Rational(1, 3), sp.Rational(1, 6), True)
print('cube: rho* =', rho, ' max exponent =', max(T.values()))
