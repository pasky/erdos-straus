"""OMEGA10 numerics (see POINTWISE_OMEGA10.md)."""
import sys, numpy as np
from omega10_gen import *
def apply_Lam(f, lam):
    # Lam = tensor over v of (lam_v I - (lam_v-1) E_v)
    g = f.copy()
    for v in range(f.ndim):
        g = lam[v]*g - (lam[v]-1)*g.mean(axis=v, keepdims=True)
    return g
rng = np.random.default_rng(int(sys.argv[1]))
worst=-9
for t in range(int(sys.argv[2])):
    q = int(rng.choice([2,3,4,5])); n = int(rng.integers(2, 7 if q>3 else 9))
    k = int(rng.integers(1, n+1)); m = int(rng.integers(1, 3*n))
    ev = random_system(rng, q, n, k, m)
    lam = 1 + rng.random(n)*rng.choice([0.3,1.0,3.0])
    grids = np.indices((q,)*n)
    h = np.zeros((q,)*n); Wmin = np.full((q,)*n, np.inf)
    for E in ev:
        A = np.ones((q,)*n, dtype=bool)
        for c,v in E.items(): A &= grids[c]==v
        wE = np.prod([lam[c] for c in E])
        h = np.maximum(h, A); Wmin = np.where(A, np.minimum(Wmin,wE), Wmin)
    Lh = apply_Lam(h, lam)
    val = np.max(np.where(h>0, Lh - Wmin, -np.inf))
    if val > worst:
        worst = val; print("pointwise max(Lam h - wmin) on bad = %.4g"%val, q,n,k,m, flush=True)
