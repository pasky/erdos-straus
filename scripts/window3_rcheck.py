#!/usr/bin/env python3
"""POINTWISE_WINDOW3 §2.2: r(S) spread of the cell-integrated law (cf. R29 M4).
Usage: window3_rcheck.py EPS K THETA [N]"""
import sys, numpy as np
from math import factorial
import window3_model as M
eps, K, th = float(sys.argv[1]), int(sys.argv[2]), float(sys.argv[3])
N = int(sys.argv[4]) if len(sys.argv) > 4 else 4000
L = M.Law(eps, K, N)
for par in (0, 1):
    W = M.window_configs(L.e, par); mu = np.array([L.mu(m) for m in W])
    V, _ = M.visible_one(L.e, th, "rep")
    rho = {S: sum(M.emb(S, C) * x for C, x in zip(W, mu)) for S in V}
    r0 = rho[tuple([0] * K)] if par == 0 else None
    if par == 0:
        R0 = r0
    rs = [rho[S] / np.prod([L.w[k] ** S[k] / factorial(S[k]) for k in range(K)]) / R0 for S in V if sum(S) % 2 == 0 or True]
    print("parity", par, "configs", len(W), "mu_tot", mu.sum(), "r(S) range", min(rs), max(rs))
    if par == 0: ev = rs
    else: print("max |r_even - r_odd| over S:", max(abs(a - b) for a, b in zip(ev, rs)))
