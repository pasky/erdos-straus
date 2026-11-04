#!/usr/bin/env python3
"""z56 K4CHEN: LP-optimal additive weighted sieve (with parity) for Omega_Q(4p+1), with p+4 in S exact
(vector sieve + Iwaniec switching, the Z55_P415 model).  Assessment-level model numerics.

Model (units X*G*W(z1)*W(z2), z1 = x^th1, z2 = x^zeta), all as in Z55_P415 §1.4:
  Sum_{p: N1 z1-rough, N2 z2-rough} (1 - sum_{q|N2, q in Q, q>=z2} w(log q/log x))
     >= fvec(s1,s2) - (1/2) int w(al) U(theta - al) dal/al ,     s1*th1 + s2*zeta = theta, s_i >= 1
  U(lam) = min_{t1*th1 + t2*zeta = lam} F(t1) F(t2)        (product of upper semi-linear sieves)
  T1 = pen * min_{a+b=lamsw, a<=th1} (2/a) F(b/zeta) * B(th1)       (switched 2-Q-factor mass of N1)
If  fvec - cost - T1 > 0  then some p has N1 in S, N2 z2-rough and W>0.
Weight constraint (parity): every multiset of k = r+2 numbers al_i >= zeta with sum <= 1 has sum w(al_i) >= 1,
so W > 0 forces Omega_Q(N2) <= r  (Omega_Q(N2) is even; repeated Q-primes >= z2 are O(x^{1-zeta})).
w is piecewise constant on cells [zeta + j h, zeta + (j+1) h), zero from al_max on; constraints use left
endpoints (conservative).  LP solved by cutting planes with an exact DP separation oracle.
Usage: python z56_k4chen_lp.py [demo|scan] ...
"""
import math, sys, os
import numpy as np
from scipy.optimize import linprog

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import z55_p415_sieve as P  # Fv, fv, B, fvec, best_upper

Fv, fv, B, fvec, best_upper = P.Fv, P.fv, P.B, P.fvec, P.best_upper


def Uup(lam, th1, zeta, n=80):
    """upper vector bound min F(t1)F(t2), t1*th1 + t2*zeta = lam."""
    if lam <= 0: return math.inf
    best = math.inf
    for k in range(1, n):
        t1 = lam / th1 * k / n
        t2 = (lam - t1 * th1) / zeta
        best = min(best, Fv(t1) * Fv(t2))
    return best


def cell_costs(th1, zeta, theta, h, amax, nsub=6):
    """c_j = (1/2) int_{cell j} U(theta - al)/al dal (midpoint rule on nsub subcells; U is increasing in al,
    so we use the right end of each subcell for U -- conservative)."""
    n = int(round((amax - zeta) / h))
    c = np.zeros(n)
    for j in range(n):
        a0 = zeta + j * h
        tot = 0.0
        for i in range(nsub):
            l = a0 + i * h / nsub; r_ = l + h / nsub
            tot += 0.5 * Uup(theta - r_, th1, zeta) * math.log(r_ / l)
        c[j] = tot
    return c


def min_config(w, k, J, nbig):
    """min sum of w over multisets of exactly k indices in {0..n-1} U {big (index nbig, weight 0)},
    with sum of indices <= J.  Returns (value, multiset)."""
    n = len(w)
    INF = 1e18
    # dp[c][s] = min weight using c items with index-sum s; items considered with nondecreasing index (multiset)
    # simple unbounded knapsack with exact count: iterate items, allow repeats.
    dp = np.full((k + 1, J + 1), INF); dp[0][0] = 0.0
    choice = {}
    items = list(range(n)) + ([nbig] if nbig <= J else [])
    for it in items:
        wt = w[it] if it < n else 0.0
        for c in range(1, k + 1):
            # allow repeated use: process in increasing c so dp[c-1] already includes this item
            prev = dp[c - 1]
            if it > J: continue
            cand = np.full(J + 1, INF)
            cand[it:] = prev[:J + 1 - it] + wt
            better = cand < dp[c] - 1e-15
            if better.any():
                dp[c][better] = cand[better]
                for s in np.nonzero(better)[0]: choice[(c, int(s))] = it
    s_best = int(np.argmin(dp[k])); val = dp[k][s_best]
    # reconstruct
    ms = []; c, s = k, s_best
    while c > 0:
        it = choice[(c, s)]; ms.append(it); s -= it; c -= 1
    return val, ms


def solve_lp(th1, zeta, theta, r, h=0.004, amax=None, verbose=False, maxit=3000):
    if amax is None: amax = theta - 0.02
    k = r + 2
    J = int(math.floor((1 - k * zeta) / h + 1e-9))
    if J < 0: return 0.0, None  # no config with k factors >= zeta: weights unnecessary
    c = cell_costs(th1, zeta, theta, h, amax)
    n = len(c); nbig = n  # index of al >= amax
    rows = []
    w = np.zeros(n)
    for it in range(maxit):
        val, ms = min_config(w, k, J, nbig)
        if val >= 1 - 1e-9: break
        row = np.zeros(n)
        for m in ms:
            if m < n: row[m] += 1
        if row.sum() == 0: return math.inf, None  # config made only of big factors: infeasible
        rows.append(row)
        res = linprog(c, A_ub=-np.array(rows), b_ub=-np.ones(len(rows)), bounds=[(0, None)] * n, method='highs')
        if res.status != 0: return math.inf, None
        w = res.x
    # final exact feasibility check; constraints are homogeneous, so rescaling makes w feasible (valid upper bound)
    val, _ = min_config(w, k, J, nbig)
    if val <= 1e-12: return math.inf, None
    if val < 1: w = w / val
    return float(c @ w), w


def margin(th1, zeta, theta, r, lamsw=0.5, pen=1.0, ns=12, h=0.004):
    T1 = best_upper(zeta, lamsw, th1, pen) * B(th1)
    best = (-1e9, None)
    smax = (theta - zeta) / th1
    if smax < 1: return best
    cost, w = solve_lp(th1, zeta, theta, r, h=h)
    for i in range(ns + 1):
        s1 = 1 + i * (smax - 1) / ns
        s2 = (theta - s1 * th1) / zeta
        if s2 < 1: continue
        M = fvec(s1, s2)
        v = M - T1 - cost
        if v > best[0]: best = (v, dict(s1=s1, s2=s2, main=M, T1=T1, cost=cost))
    return best


if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else 'demo'
    if mode == 'demo':
        th1, zeta, theta = 0.42, 0.008, 0.5
        for r in (10, 8, 6):
            print(r, margin(th1, zeta, theta, r))


def scan(r, theta=0.5, lamsw=0.5, pen=1.0, th1s=None, zetas=None, h=0.004):
    th1s = th1s or [0.36, 0.38, 0.40, 0.42, 0.44, 0.46]
    zetas = zetas or [0.004, 0.008, 0.012, 0.016, 0.02, 0.025, 0.03]
    best = (-1e9, None)
    for th1 in th1s:
        for z in zetas:
            v, d = margin(th1, z, theta, r, lamsw=lamsw, pen=pen, h=h)
            if v > best[0]: best = (v, (th1, z, d))
    return best


if __name__ == "__main__" and len(sys.argv) > 1 and sys.argv[1] == 'scan':
    theta = float(sys.argv[2]); lamsw = float(sys.argv[3]); pen = float(sys.argv[4])
    for r in [int(a) for a in sys.argv[5].split(',')]:
        print(f"theta={theta} lamsw={lamsw} pen={pen} r={r}:", scan(r, theta, lamsw, pen), flush=True)
