"""OMEGA10 Conjecture Q: for a hypergraph H (nonempty) on n vertices with weights mu_v>=0,
prod_{v in E}(1+mu_v) <= 2 for all E in H, let tau(R)=1[R hits every edge], tauhat its
Moebius transform; Q = sum_V mu^V tauhat(V)^2.  Claim Q <= 1.
Usage: omega10_q.py seed trials nmax"""
import sys, numpy as np
seed, trials, nmax = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
rng = np.random.default_rng(seed)
def Q(n, edges, mu):
    N = 1 << n
    R = np.arange(N)
    tau = np.ones(N)
    for e in edges:
        m = sum(1 << v for v in e)
        tau *= ((R & m) != 0)
    t = tau.copy()
    for i in range(n):           # Moebius transform
        b = 1 << i
        idx = R[(R & b) != 0]
        t[idx] -= t[idx ^ b]
    lw = np.zeros(N)
    for i in range(n):
        lw += ((R >> i) & 1) * np.log(mu[i]) if mu[i] > 0 else ((R >> i) & 1) * -1e300
    return float(np.sum(np.exp(lw) * t * t))
worst = -1
for tr in range(trials):
    n = int(rng.integers(2, nmax + 1))
    m = int(rng.integers(1, 3 * n))
    kmax = int(rng.integers(1, n + 1))
    edges = []
    for _ in range(m):
        r = int(rng.integers(1, kmax + 1))
        edges.append(tuple(sorted(rng.choice(n, r, replace=False).tolist())))
    a = rng.random(n) * rng.choice([0.0, 1.0], n, p=[0.1, 0.9])
    s = max(sum(a[v] for v in e) for e in edges)
    if s == 0: continue
    lam = 2 ** (a / s); mu = lam - 1
    q = Q(n, edges, mu)
    if q > worst:
        worst = q; print(f"Q={q:.6f} n={n} m={m} kmax={kmax}", flush=True)
