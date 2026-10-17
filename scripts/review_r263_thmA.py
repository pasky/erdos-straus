"""R263 from-scratch check of JOINT_BUDGET Theorem A / Remark 1.2 / Remark 1.3 example.
For random polynomial slice choices theta(u1,u2) (positive somewhere), factor each RT2 side number in Q[u1,u2,X]
and check: exactly one X-involving irreducible factor, multiplicity 1, of full X-degree.
Negative controls: d=-w^2 (Type I quadratic must split), and p-dependent slice d=(X+e)/(4ab) (Type II {c,d} splits).
"""
import random
from sympy import symbols, factor_list, degree, Poly, expand, Rational, simplify

u1, u2, X = symbols('u1 u2 X')
random.seed(263)


def rpoly(allow_shared=None):
    # random poly in u1,u2 of degree <=3, positive constant term so positive near 0
    terms = 0
    for i in range(4):
        for j in range(4 - i):
            if random.random() < 0.35:
                terms += random.randint(-5, 5) * u1**i * u2**j
    p = terms + random.randint(1, 6)
    if allow_shared is not None and random.random() < 0.5:
        p = expand(p * allow_shared)  # force common content with another slice poly
    return expand(p)


def check(N):
    c, facs = factor_list(expand(N), u1, u2, X)
    xf = [(f, k) for f, k in facs if degree(f, X) > 0]
    ok = len(xf) == 1 and xf[0][1] == 1 and degree(xf[0][0], X) == degree(N, X)
    return ok, facs


rows = {
    'I{c,d}': lambda s: X**2 + 4 * s['c']**2 * s['d'],
    'I{a,c}': lambda s: s['a'] * X + s['c'],
    'I{a,e}': lambda s: s['e'] * X + 1,
    'I{d,e}': lambda s: s['e'] * X + 1,
    'II{c,d}': lambda s: 4 * s['c']**2 * s['d'] * X + 1,
    'II{a,c}': lambda s: s['c'] * X + s['a'],
    'II{a,d}': lambda s: X + 4 * s['a']**2 * s['d'],
    'II{a,e}': lambda s: X + s['e'],
    'II{d,e}': lambda s: X + s['e'],
}
viol = 0
tot = 0
for trial in range(40):
    shared = rpoly()
    s = {k: rpoly(shared) for k in 'acde'}
    for name, fn in rows.items():
        ok, facs = check(fn(s))
        tot += 1
        if not ok:
            viol += 1
            print('VIOLATION', name, s, facs)
print('Theorem A: tests', tot, 'violations', viol)

# Remark 1.2 negative control
w, cc = rpoly(), rpoly()
ok, facs = check(X**2 + 4 * cc**2 * (-w**2))
print('Remark 1.2 (d=-w^2) irreducible?', ok, '(expected False); #X-factors',
      sum(1 for f, k in facs if degree(f, X) > 0))
# Remark 1.2 sharper: d>0 at some point but -d a square times positive? e.g. d = -(u1^2+1)^2 * (-1)... d must be >0 somewhere
# try d = (u1^2-2)^2 (nonneg, positive on open set): -d not a square in Q(u) -> irreducible expected
ok, _ = check(X**2 + 4 * (u1**2 - 2)**2)
print('d=(u1^2-2)^2 irreducible?', ok, '(expected True)')

# Remark 1.3 example: Type II, d=(X+e)/(4ab), e=(a+b)/c  -> 4c^2 d X + 1 = (4acd-1)(4bcd-1)
a, b, c = symbols('a b c')
e = (a + b) / c
d = (X + e) / (4 * a * b)
lhs = 4 * c**2 * d * X + 1
rhs = (4 * a * c * d - 1) * (4 * b * c * d - 1)
print('Remark 1.3 identity holds:', simplify(lhs - rhs) == 0)
