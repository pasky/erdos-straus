#!/usr/bin/env python3
"""O24 (EXCEPTIONAL_TUPLES2.md §5): single-form (class -1) effects vs the TC precision.

For the prime family (l = 3 mod 4, l <= y) and N, computes
  * Z11_j : CRT mass of j-tuples whose class -1 part has product > N+1
            (forced zeros, Cor 1.2; lower bound for Z_j). Exact DP over primes
            with state (j, floor-binned log of the class -1 product); logs are
            rounded DOWN, so Z11_j is a lower bound.
  * Fl11_j: floor deficit of pure class -1 j-tuples with q <= N+1:
            sum ({(N+1)/q} - 1/q)/N  (exact enumeration, Lemma 3.1)
  * e_j, eta_K for the first even K >= e^2 mu_y, and Thm 2.1's bound.
usage: tuples2_forced.py N y [Jmax]
"""
import sys
from math import log, exp, comb, lgamma
import numpy as np
from tuples_moments import primes_upto, R_set, esym

N = int(float(sys.argv[1])); y = int(float(sys.argv[2]))
J = int(sys.argv[3]) if len(sys.argv) > 3 else 12
P = [int(l) for l in primes_upto(y) if l % 4 == 3]
ps = [len(R_set(l)) / l for l in P]
mu = sum(ps)
e = esym(ps, J)
# DP: state dp[j][b] where b = binned log of class -1 product (capped at B = over threshold)
step = 1e-3
thr = log(N + 1)
B = int(thr / step) + 1          # bin index B means "product certainly > N+1"
dp = np.zeros((J + 1, B + 1)); dp[0, 0] = 1.0
for l, p in zip(P, ps):
    w = int(log(l) / step)       # floor => lower bound on log
    new = dp.copy()
    # hit with a class other than -1: weight p - 1/l, no change of product
    new[1:, :] += (p - 1 / l) * dp[:-1, :]
    # hit with class -1: weight 1/l, product grows
    sh = np.zeros_like(dp)
    sh[:, w:] += dp[:, :B + 1 - w] if w <= B else 0
    if w <= B:
        sh[:, B] += dp[:, B + 1 - w:].sum(axis=1) if B + 1 - w <= B else 0
    else:
        sh[:, B] += dp.sum(axis=1)
    new[1:, :] += (1 / l) * sh[:-1, :]
    dp = new
Z11 = dp[:, B]  # bins >= B: sum of floored logs >= B*step > thr  (strict lower bound)
# floor deficit of pure class -1 tuples with q <= N+1 (DFS)
Fl = np.zeros(J + 1)
def dfs(i, q, j):
    if j >= 1:
        Fl[j] += ((N + 1) / q - (N + 1) // q) - 1 / q
    if j == J:
        return
    for k in range(i, len(P)):
        if q * P[k] > N + 1:
            break
        dfs(k + 1, q * P[k], j + 1)
dfs(0, 1, 0)
Fl /= N
K = 2 * int(np.ceil(exp(2) * mu / 2))
etaK = exp(-K / exp(2)) / K
Q = [l for l in P if l > y / 2]
sig = sum(1 / l for l in Q)
u0 = int(np.ceil(log(N + 2) / log(y / 2)))
thm = esym([1 / l for l in Q], u0)[u0] if u0 <= len(Q) else 0.0
print(f"# N={N:.3g} y={y} primes={len(P)} mu={mu:.4f} K={K} eta_K={etaK:.3e} u0={u0} "
      f"sigma_y={sig:.4f} Thm2.1: Z_u0 >= e_u0(q) = {thm:.3e}")
print("# j  e_j  Z11_j(lower bd)  Z11_j/e_j  Fl11_j  Z11_j/eta_K  (Z11+Fl11)/eta_K")
for j in range(1, J + 1):
    print(f"{j:3d} {e[j]:.4e} {Z11[j]:.4e} {Z11[j]/e[j]:.3e} {Fl[j]:.4e} "
          f"{Z11[j]/etaK:.3e} {(Z11[j]+Fl[j])/etaK:.3e}")
