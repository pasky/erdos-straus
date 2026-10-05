"""OMEGA10 Lemma 3.2 check: Q_mu(H) = E_P[Theta(H_avoid P)^2], P(v in P)=mu_v/(1+mu_v),
Theta(C)=sum_{J subset C}(-1)^|J| lam^{union J}.  Exact enumeration.  Usage: seed trials nmax"""
import sys, itertools, numpy as np
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
def Theta(C, lam):
    tot = 0.0
    for r in range(len(C) + 1):
        for J in itertools.combinations(C, r):
            U = set().union(*J) if J else set()
            tot += (-1) ** r * np.prod([lam[v] for v in U])
    return tot
worst = 0
for tr in range(trials):
    n = int(rng.integers(1, nmax+1)); kmax = int(rng.integers(1, n+1))
    edges = [tuple(sorted(rng.choice(n, int(rng.integers(1,kmax+1)), replace=False).tolist())) for _ in range(int(rng.integers(1,8)))]
    mu = rng.random(n) * rng.choice([0.3, 1.0, 3.0]); lam = 1 + mu; th = mu / lam
    E = 0.0
    for P in itertools.product([0,1], repeat=n):
        pr = np.prod([th[v] if P[v] else 1-th[v] for v in range(n)])
        C = [e for e in edges if not any(P[v] for v in e)]
        E += pr * Theta(C, lam) ** 2
    worst = max(worst, abs(E - Qmu(n, edges, mu)))
print(f"max |E_P Theta^2 - Q| over {trials} trials = {worst:.3g}")
