"""O126 §3 checks: conic bundles (F1)-(F3) of the ES surface and restrictions of alpha.
Run: PYTHONPATH=scripts uv run python scripts/geo_fibrations.py"""
from fractions import Fraction as F
import sympy as sp
from geo_common import hilbert, es_solutions, primes_dividing

u1, u2, u3, n, t, lam, x0, x1, x2, x3 = sp.symbols('u1 u2 u3 n t lam x0 x1 x2 x3')
eq = 4*u1*u2*u3 - n*(u1*u2 + u1*u3 + u2*u3)

# (F1) u1 = t : n t * [ ((4t-n)u2 - nt)((4t-n)u3 - nt) - (nt)^2 ] proportional to eq|_{u1=t}
X = (4*t - n)*u2 - n*t; Y = (4*t - n)*u3 - n*t
lhs = sp.expand(X*Y - (n*t)**2); rhs = sp.expand(eq.subs(u1, t))
print("(F1) XY-(nt)^2 =", sp.factor(sp.simplify(lhs/rhs)), "* eq|_{u1=t}")
print("     fibre t=0:", sp.factor(eq.subs(u1, 0)), "; fibre t=n/4:", sp.factor(eq.subs(u1, n/4)))

# (F2) u1 = lam u2 : eq = u2 * (...) ; ZW - n^2 lam(lam+1) proportional to the residual factor
res = sp.factor(eq.subs(u1, lam*u2)); print("(F2) eq|_{u1=lam u2} =", res)
Z = 4*lam*u2 - n*(lam + 1); W = 4*lam*u3 - n*lam
resid = sp.cancel(eq.subs(u1, lam*u2)/u2)
print("     (ZW - n^2 lam(lam+1)) / residual =", sp.simplify(sp.expand(Z*W - n**2*lam*(lam + 1))/resid))

# (F3) planes through M1: 4x1 - n x0 = lam (x2 + x3). Points at infinity of the residual conic.
S = 4*x1*x2*x3 - n*x0*(x1*x2 + x1*x3 + x2*x3)
for P in [(0, lam, 0, 4), (0, lam, 4, 0), (0, 0, 1, -1)]:
    sub = dict(zip([x0, x1, x2, x3], P))
    assert sp.expand(S.subs(sub)) == 0 and sp.expand((4*x1 - n*x0 - lam*(x2 + x3)).subs(sub)) == 0
print("(F3) plane section meets x0=0 in (0:lam:0:4), (0:lam:4:0) [conic] and (0:0:1:-1) [on M1]")

# alpha restrictions at all places on actual solutions
c1 = c2 = 0
for N in range(3, 150):
    for sol in es_solutions(N):
        for perm in [(0, 1, 2), (1, 0, 2), (2, 1, 0), (0, 2, 1), (1, 2, 0), (2, 0, 1)]:
            a1, a2, a3 = [sol[k] for k in perm]
            L = F(a1, a2); Zv = 4*L*a2 - N*(L + 1); Wv = 4*L*a3 - N*L
            assert Zv*Wv == N*N*L*(L + 1)
            if Zv == 0:
                continue
            places = set(primes_dividing(abs(N*a1*a2*a3*Zv.numerator*Zv.denominator*L.numerator*L.denominator))) | {2, 'inf'}
            for p in places:
                assert hilbert(F(-a1, a3), F(-a2, a3), p) == hilbert(-L, -N*Zv, p), (N, sol, perm, p)
            c2 += 1
print(f"(F2) alpha|_lam = (-lam, -nZ) verified at all places on {c2} (solution, ordering) pairs")
