"""R259 from-scratch check of NORMFORM_CUBIC Lemma 2.1's key geometric input for K = Q(cbrt 2):
the Zariski closure of a unit orbit {eps^j x0} is the whole level set {N = n} (T_eps = R^1 G_m has no proper Q-subtorus).
Test: the space of polynomials of degree <= D vanishing on {eps^(q i + r) x0 : 0 <= i < M} must equal (N - n)*{deg <= D-3},
of dimension C(D-3+3, 3). Also tests a sub-progression (q = 2, r = 1) and a real-quadratic analogue.
Run: uv run --with python-flint python scripts/review_r259_orbit_closure.py
"""
import itertools
from math import comb
import flint

def mul_theta(x):           # (x0 + x1 t + x2 t^2) * t, with t^3 = 2
    a, b, c = x
    return (2 * c, a, b)

def mul(x, y):               # multiply in Z[cbrt2] coordinates
    a, b, c = y
    r = [0, 0, 0]
    t = list(x)
    for coef in (a, b, c):
        r = [ri + coef * ti for ri, ti in zip(r, t)]
        t = list(mul_theta(t))
    return tuple(r)

def N(x):
    u, v, w = x
    return u**3 + 2 * v**3 + 4 * w**3 - 6 * u * v * w

def monoms(nv, D):
    return [m for d in range(D + 1) for m in itertools.product(range(d + 1), repeat=nv) if sum(m) == d]

def vanishing_dim(points, nv, D):
    ms = monoms(nv, D)
    rows = [[int(eval_m(p, m)) for m in ms] for p in points]
    M = flint.fmpz_mat(rows)
    return len(ms) - M.rank()

def eval_m(p, m):
    r = 1
    for x, e in zip(p, m):
        r *= x ** e
    return r

eps = (-1, 1, 0)             # cbrt2 - 1
assert N(eps) == 1
for x0 in [(1, 0, 0), (1, 1, 0), (3, 1, 1)]:
    n = N(x0)
    for q, r in [(1, 0), (2, 1)]:
        e_q = (1, 0, 0)
        for _ in range(q):
            e_q = mul(e_q, eps)
        pt = x0
        for _ in range(r):
            pt = mul(pt, eps)
        pts = []
        for i in range(60):
            pts.append(pt); pt = mul(pt, e_q)
        assert all(N(p) == n for p in pts)
        for D in (3, 4, 5):
            got = vanishing_dim(pts, 3, D)
            exp = comb(D - 3 + 3, 3)
            print(f'cubic x0={x0} n={n} q={q} r={r} D={D}: vanishing dim {got}, expected (N-n)*deg<={D-3}: {exp}')
            assert got == exp
# real quadratic Q(sqrt2): eps = 3 + 2 sqrt2 (norm 1)
def mulq(x, y):
    return (x[0] * y[0] + 2 * x[1] * y[1], x[0] * y[1] + x[1] * y[0])
pt, pts = (1, 1), []          # N = -1 for (1,1); use (3,1): 9-2 = 7
pt = (3, 1)
for i in range(40):
    pts.append(pt); pt = mulq(pt, (3, 2))
for D in (2, 3, 4):
    got = vanishing_dim(pts, 2, D); exp = comb(D - 2 + 2, 2)
    print(f'real quadratic D={D}: vanishing dim {got}, expected {exp}'); assert got == exp
print('Lemma 2.1 Zariski-closure check passed')
