"""R223: from-scratch continuum check of STERILE_EXPLICIT (I3)/Prop 2.1: theta*(eta) = max over size patterns
(alpha, gamma, delta, eps), alpha+gamma+delta+eps = 1, 2 alpha + delta <= 1, eps >= 0, of the min over routes of the
route exponent (route formulas re-derived in the review, §D.2), with class-divisor exponent from Cor 1.4
(max(0, beta(1-beta) - rho/n) n, plus the trivial window/modulus bound, plus tau <= n^eta as fallback).
Fine grid + random local refinement (Nelder-Mead on the penalised objective). EVIDENCE only.
Usage: uv run --with scipy --with numpy python scripts/review_se2_rate.py [eta ...]"""
import sys
import numpy as np
from scipy.optimize import minimize

def cls(n, rho, sizes, eta, trivial=True):
    best = eta * n
    for s in sizes:
        b = np.where(n > 1e-12, s / np.maximum(n, 1e-12), 0)
        best = np.minimum(best, np.maximum(0.0, b * (1 - b) - rho / np.maximum(n, 1e-12)) * n)
        if trivial: best = np.minimum(best, np.maximum(0.0, s - rho))
    return best

def routes(al, ga, de, ep, eta, trivial=True):
    R = [np.maximum(ep, al + de),                                  # A
         ga + np.maximum(ep, al), ga + np.maximum(ep, de),         # I, J
         1 - np.maximum(np.maximum(al, ga), np.maximum(de, ep)),   # H (any three of a, c, d, e)
         al + de + cls(1 + 0 * al, al + de, [1 - ep, ep], eta, trivial),
         ga + de + cls(1 + 2 * ga + de, ga + de, [1 - ep, 1 - al + ga], eta, trivial),
         al + ga + cls(1 + ga, al + ga, [1 - ep, 1 - al - de], eta, trivial),
         np.maximum(ep, al) + cls(1 - al, ep, [1 - al - de, de], eta, trivial),
         np.maximum(ep, de) + cls(1 - de, ep, [al, 1 - al - de], eta, trivial),
         ep + eta]                                                  # tau3
    return np.min(np.stack(R), axis=0)

def theta(eta, n=120, trivial=True, seed=0):
    g = np.arange(n + 1) / n
    al, ga, de = np.meshgrid(g, g, g, indexing='ij')
    al, ga, de = al.ravel(), ga.ravel(), de.ravel()
    ep = 1 - al - ga - de
    ok = (ep >= -1e-12) & (2 * al + de <= 1 + 1e-12)
    al, ga, de, ep = al[ok], ga[ok], de[ok], np.maximum(ep[ok], 0)
    v = routes(al, ga, de, ep, eta, trivial)
    top = np.argsort(-v)[:40]
    best = (float(v[top[0]]), (al[top[0]], ga[top[0]], de[top[0]], ep[top[0]]))
    def f(x):
        a, c, d = x; e = 1 - a - c - d
        pen = 10 * (max(0, -a) + max(0, -c) + max(0, -d) + max(0, -e) + max(0, 2 * a + d - 1))
        a, c, d = max(a, 0), max(c, 0), max(d, 0); e = max(1 - a - c - d, 0)
        if 2 * a + d > 1 or a + c + d > 1: return 1.0 + pen
        return -float(routes(np.array([a]), np.array([c]), np.array([d]), np.array([e]), eta, trivial)[0]) + pen
    rng = np.random.default_rng(seed)
    starts = [np.array([al[i], ga[i], de[i]]) for i in top] + [rng.dirichlet([1, 1, 1, 1])[:3] for _ in range(200)]
    for x0 in starts:
        r = minimize(f, x0, method='Nelder-Mead', options={'xatol': 1e-10, 'fatol': 1e-12, 'maxiter': 4000})
        if -r.fun > best[0] + 1e-9 and f(r.x) < 0.5:
            a, c, d = r.x; best = (-r.fun, (a, c, d, 1 - a - c - d))
    return best

if __name__ == '__main__':
    etas = [float(x) for x in sys.argv[1:]] or [0.25, 0.3, 0.35]
    for eta in etas:
        for triv in (False, True):
            t, x = theta(eta, trivial=triv)
            print(f"eta={eta} trivial-bound={'on' if triv else 'off'}: theta* ~ {t:.6f} at (al,ga,de,ep) = {tuple(round(float(y), 4) for y in x)}")
