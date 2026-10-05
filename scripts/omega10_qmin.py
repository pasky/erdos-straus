"""OMEGA10: test Q': Q_mu(H) <= min_E w_E - 1 when all w_E <= 2.  Usage: seed trials nmax"""
import sys, numpy as np
seed, trials, nmax = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
rng = np.random.default_rng(seed)
def Qmu(n, edges, mu):
    N = 1 << n; R = np.arange(N); tau = np.ones(N)
    for e in edges:
        m = sum(1 << v for v in e); tau *= ((R & m) != 0)
    t = tau.copy()
    for i in range(n):
        b = 1 << i; idx = R[(R & b) != 0]; t[idx] -= t[idx ^ b]
    w = np.ones(N)
    for i in range(n): w = np.where((R >> i) & 1, w * mu[i], w)
    return float(np.sum(w * t * t))
worst = -9
for tr in range(trials):
    n = int(rng.integers(2, nmax+1)); kmax = int(rng.integers(1, n+1))
    edges = [tuple(sorted(rng.choice(n, int(rng.integers(1,kmax+1)), replace=False).tolist())) for _ in range(int(rng.integers(1,3*n)))]
    a = rng.random(n) * rng.choice([0.,1.], n, p=[.15,.85])
    s = max(sum(a[v] for v in e) for e in edges)
    if s == 0: continue
    scale = rng.choice([1.0, rng.random()])
    lam = 2 ** (scale * a / s); mu = lam - 1
    q = Qmu(n, edges, mu); m = min(np.prod([lam[v] for v in e]) for e in edges) - 1
    if q - m > worst: worst = q - m; print(f"Q-(wmin-1)={worst:.4g} Q={q:.4f} n={n} edges={edges}", flush=True)
