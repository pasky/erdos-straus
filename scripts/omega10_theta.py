"""OMEGA10: test |Theta(C)| <= 1, Theta(C) = sum_{J subset C} (-1)^|J| lam^{union J},
for hypergraphs C with all w_E = lam^E <= 2 (lam_v >= 1).  Computed via the transversal
form Theta = sum_{B} (-mu)^B lam^{V\\B} tau_C(B).  Usage: omega10_theta.py seed trials nmax"""
import sys, numpy as np
seed, trials, nmax = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
rng = np.random.default_rng(seed)
def theta(n, edges, lam):
    N = 1 << n; R = np.arange(N); t = np.ones(N)
    for e in edges:
        m = sum(1 << v for v in e); t *= ((R & m) != 0)
    w = np.ones(N)
    for i in range(n): w = np.where((R >> i) & 1, w * (1 - lam[i]), w * lam[i])
    return float(np.sum(w * t))
worst = 0
for tr in range(trials):
    n = int(rng.integers(1, nmax+1)); kmax = int(rng.integers(1, n+1))
    edges = [tuple(sorted(rng.choice(n, int(rng.integers(1,kmax+1)), replace=False).tolist())) for _ in range(int(rng.integers(1,3*n)))]
    a = rng.random(n) * rng.choice([0.,1.], n, p=[.1,.9])
    s = max(sum(a[v] for v in e) for e in edges)
    if s == 0: continue
    lam = 2 ** (rng.choice([1.0, rng.random()**0.3]) * a / s)
    used = set(v for e in edges for v in e); lam = np.array([lam[v] if v in used else 1.0 for v in range(n)])
    th = theta(n, edges, lam)
    if abs(th) > worst: worst = abs(th); print(f"|Theta|={worst:.6f} n={n} edges={edges}", flush=True)
