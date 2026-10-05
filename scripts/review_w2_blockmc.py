#!/usr/bin/env python3
"""R29 independent MC of §3.3: R(theta)/tau for the continuum heuristic law.
One window: Poisson process of intensity 1/(2t) on [eps,1] (Lambda = ln(1/eps)/2),
reweighted by W = 1[sum<1, #even] (1-sum)^{-1/2}; two windows independent.
mu(set)/mu(empty,empty) = E[W3 W7 1_set] * e^{2 Lambda}.
Splittable: C = U ⊔ V, U,V nonempty, each even in each window, min U + min V > theta.
Split optimum found by BRUTE FORCE over all V (no author rule used) when |C|<=12.
Usage: review_w2_blockmc.py N EPS SEED theta1 theta2 ...
"""
import sys, math, itertools
import numpy as np

N, eps, seed = int(float(sys.argv[1])), float(sys.argv[2]), int(sys.argv[3])
ths = [float(t) for t in sys.argv[4:]]
rng = np.random.default_rng(seed)
Lam = 0.5 * math.log(1 / eps)

def sample():
    k = rng.poisson(Lam)
    return sorted(eps ** (1 - rng.random(k)))  # density ∝ 1/t on [eps,1]

def best_split(c3, c7):
    """max over valid (U,V) of minU+minV; -inf if none."""
    pts = [(t, 0) for t in c3] + [(t, 1) for t in c7]
    n = len(pts); best = -1.0
    if n > 12:
        return None
    for mask in range(1, (1 << n) - 1):
        V = [pts[i] for i in range(n) if mask >> i & 1]
        U = [pts[i] for i in range(n) if not mask >> i & 1]
        if sum(1 for _, q in V if q == 0) % 2 or sum(1 for _, q in V if q == 1) % 2:
            continue
        best = max(best, min(V)[0] + min(U)[0])
    return best

acc = {t: 0.0 for t in ths}; tgt = 0.0; skipped = 0
for _ in range(N):
    c3, c7 = sample(), sample()
    if len(c3) % 2 or len(c7) % 2:
        continue
    s3, s7 = sum(c3), sum(c7)
    if s3 >= 1 or s7 >= 1:
        continue
    Wt = (1 - s3) ** -0.5 * (1 - s7) ** -0.5
    if not c3 and not c7:
        tgt += Wt; continue
    b = best_split(c3, c7)
    if b is None:
        skipped += 1; continue
    for t in ths:
        if b > t:
            acc[t] += Wt
print(f"N={N} eps={eps}: P(clean,clean)~{tgt/N:.4f} (exact e^-2Λ={math.exp(-2*Lam):.4f}); skipped(>12 pts)={skipped}")
for t in ths:
    print(f"  theta={t}: R/tau = {acc[t]/tgt:.3f}")
