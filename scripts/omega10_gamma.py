"""OMEGA10 Lemma A check: G_F(lam) <= Gamma := E_x[ Q_mu(H(x)) ], H(x) = supports of events
holding at x, Q_mu(H) = sum_V mu^V tauhat_H(V)^2 (=1 if H empty).  Usage: omega10_gamma.py seed trials"""
import sys, itertools, numpy as np
from omega10_gen import *
seed, trials = int(sys.argv[1]), int(sys.argv[2]); rng = np.random.default_rng(seed)
def Lam(f, lam):
    g = f.copy()
    for v in range(f.ndim):
        g = lam[v]*g - (lam[v]-1)*g.mean(axis=v, keepdims=True)
    return g
def Qmu(n, supps, mu):
    if not supps: return 1.0
    N = 1 << n; R = np.arange(N); tau = np.ones(N)
    for e in supps:
        m = sum(1 << v for v in e); tau *= ((R & m) != 0)
    t = tau.copy()
    for i in range(n):
        b = 1 << i; idx = R[(R & b) != 0]; t[idx] -= t[idx ^ b]
    w = np.ones(N)
    for i in range(n): w = np.where((R >> i) & 1, w * mu[i], w)
    return float(np.sum(w * t * t))
worst = -9; worstG = -9
for tr in range(trials):
    q = int(rng.choice([2,3,4])); n = int(rng.integers(2, 6 if q>3 else 7))
    k = int(rng.integers(1, n+1)); ev = random_system(rng, q, n, k, int(rng.integers(1, 3*n)))
    lam = 1 + rng.random(n) * rng.choice([0.5, 1.5, 3.0]); mu = lam - 1
    F = good_indicator(q, n, ev); G = (F*Lam(F, lam)).mean()
    cache = {}; Gam = 0.0
    for x in itertools.product(range(q), repeat=n):
        H = frozenset(tuple(sorted(E)) for E in ev if all(x[c]==v for c,v in E.items()))
        if H not in cache: cache[H] = Qmu(n, list(H), mu)
        Gam += cache[H]
    Gam /= q**n
    wmax = max(np.prod([lam[c] for c in E]) for E in ev)
    if G - Gam > worst: worst = G - Gam; print(f"G-Gamma={worst:.3g} (G={G:.4f} Gamma={Gam:.4f}) wmax={wmax:.2f}", flush=True)
    if wmax <= 2 and Gam > worstG: worstG = Gam; print(f"   [w<=2] Gamma={Gam:.5f}", flush=True)
