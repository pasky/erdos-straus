"""OMEGA10 Conjecture FM: if all w_E<=2 then Q_mu(H) <= prod_E (w_E-1)^{y_E} for every
fractional matching y (sum_{E ni v} y_E <= 1).  Tests log Q <= -max_y sum y_E log(1/(w_E-1)).
Usage: omega10_fm.py seed trials nmax"""
import sys, numpy as np
from scipy.optimize import linprog
seed, trials, nmax = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
rng = np.random.default_rng(seed)
def Qmu(n, edges, mu):
    N = 1 << n; R = np.arange(N); t = np.ones(N)
    for e in edges:
        m = sum(1 << v for v in e); t *= ((R & m) != 0)
    for i in range(n):
        b = 1 << i; idx = R[(R & b) != 0]; t[idx] -= t[idx ^ b]
    w = np.ones(N)
    for i in range(n): w = np.where((R >> i) & 1, w * mu[i], w)
    return float(np.sum(w * t * t))
worst = -9
for tr in range(trials):
    n = int(rng.integers(2, nmax+1)); kmax = int(rng.integers(1, n+1))
    edges = list({tuple(sorted(rng.choice(n, int(rng.integers(1,kmax+1)), replace=False).tolist())) for _ in range(int(rng.integers(1,3*n)))})
    a = rng.random(n) * rng.choice([0.,1.], n, p=[.1,.9])
    s = max(sum(a[v] for v in e) for e in edges)
    if s == 0: continue
    lam = 2 ** (rng.choice([1.0, rng.random()**0.3]) * a / s); mu = lam - 1
    w = np.array([np.prod([lam[v] for v in e]) for e in edges])
    if np.any(w - 1 <= 1e-12): continue
    c = -np.log(1 / (w - 1))                    # minimise -sum y log(1/(w-1))
    Aub = np.array([[1.0 if v in e else 0.0 for e in edges] for v in range(n)])
    res = linprog(c, A_ub=Aub, b_ub=np.ones(n), bounds=[(0, None)] * len(edges), method="highs")
    bound = -res.fun                             # max sum y log(1/(w-1))
    q = Qmu(n, edges, mu)
    if q <= 0: continue
    gap = np.log(q) + bound
    if gap > worst: worst = gap; print(f"logQ + maxLP = {gap:.4g}  Q={q:.4g} n={n} m={len(edges)}", flush=True)
