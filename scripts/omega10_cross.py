"""OMEGA10: cross-term signs.  F0 = good-ind of system 1, g = OR of system 2, F1 = F0(1-g).
X := <F1, Lam(F0 g)>.  Test  -G_{F0 g}/2 <= X <= 0.  Usage: omega10_cross.py seed trials lammax"""
import sys, numpy as np
from omega10_gen import *
def apply_Lam(f, lam):
    g = f.copy()
    for v in range(f.ndim):
        g = lam[v]*g - (lam[v]-1)*g.mean(axis=v, keepdims=True)
    return g
seed, trials = int(sys.argv[1]), int(sys.argv[2]); lmax = float(sys.argv[3])
rng = np.random.default_rng(seed)
up = lo = -9
for t in range(trials):
    q = int(rng.choice([2,3,4,5])); n = int(rng.integers(2, 6 if q>3 else 8))
    k = int(rng.integers(1, n+1))
    e1 = random_system(rng, q, n, k, int(rng.integers(1, 2*n)))
    e2 = random_system(rng, q, n, k, int(rng.integers(1, 2*n)))
    lam = 1 + rng.random(n)*(lmax-1)
    F0 = good_indicator(q, n, e1); F1 = good_indicator(q, n, e1+e2); B = F0 - F1
    X = (F1*apply_Lam(B, lam)).mean(); GB = (B*apply_Lam(B, lam)).mean()
    wmax = max(np.prod([lam[c] for c in E]) for E in e2)
    if X > up: up = X; print("upper viol X=%.4g"%X, q,n,k, "wmax2=%.3f"%wmax, flush=True)
    if -GB/2 - X > lo: lo = -GB/2 - X; print("lower viol %.4g"%lo, q,n,k, "wmax2=%.3f"%wmax, flush=True)
