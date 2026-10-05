#!/usr/bin/env python3
"""POINTWISE_WINDOW2 §3 -- Monte Carlo for the two-block fake criterion R(theta)/tau.

Continuum model of one window (§3.1): bad prime factors of n_q with log-size
t = log r / log x >= eps form a configuration B with (unnormalised) density
    prod_i 1/(2 t_i) * (1 - sum t)^(-1/2)   (|B| even, sum t <= 1),
the clean configuration B = {} having weight 1.  Two windows independent.

Sampling: Poisson process of intensity dt/(2t) on [eps,1] (mean L=(1/2)ln(1/eps)),
weight (1-sum)^(-1/2) * [sum<1] * [|B| even].  (The factor exp(-L) is common to
all configurations and cancels in ratios.)

A configuration C=(B3,B7) != ({},{}) is *theta-splittable* if C = U ⊔ V with
U, V nonempty, each with an even number of points in each window, and
min U + min V > theta.  Optimal split: c1 = min C in U; V = two largest points
of a window q (if that leaves U nonempty and does not take c1), min V = 2nd
largest of B_q.  (Lemma 3.3.)

Output: tau = mass(clean,clean), R(theta) = mass(splittable), ratio R/tau.
Usage: window2_blockfake.py [NSAMP] [EPS] [SEED]
"""
import sys
import json
import numpy as np


def sample_window(rng, n, eps, kmax=40):
    L = 0.5 * np.log(1.0 / eps)
    k = rng.poisson(L, size=n)
    k = np.minimum(k, kmax)
    U = rng.random((n, kmax))
    t = eps ** U                      # density prop. to 1/t on [eps,1]
    mask = np.arange(kmax)[None, :] < k[:, None]
    t = np.where(mask, t, np.nan)
    s = np.nansum(t, axis=1)
    w = np.where((s < 1.0) & (k % 2 == 0), (1.0 - np.minimum(s, 1 - 1e-300)) ** -0.5, 0.0)
    ts = np.sort(np.where(mask, t, np.inf), axis=1)   # ascending, inf padding
    return k, ts, w


def top2(ts, k):
    """second largest point of each config (nan if k<2)."""
    n = len(k)
    out = np.full(n, np.nan)
    ok = k >= 2
    out[ok] = ts[np.arange(n)[ok], k[ok] - 2]
    return out


def splittable(k3, t3, k7, t7, theta):
    n = len(k3)
    INF = np.inf
    m3 = np.where(k3 > 0, t3[:, 0], INF)
    m7 = np.where(k7 > 0, t7[:, 0], INF)
    c1 = np.minimum(m3, m7)
    c1_in3 = m3 <= m7
    best = np.full(n, -INF)
    # V = top two of window 3: need k3>=2, U nonempty (k3>=4 or k7>0), c1 not in top2(B3)
    s3 = top2(t3, k3)
    ok3 = (k3 >= 2) & ((k3 >= 4) | (k7 > 0)) & ~(c1_in3 & (k3 == 2))
    best = np.where(ok3, np.maximum(best, s3), best)
    s7 = top2(t7, k7)
    ok7 = (k7 >= 2) & ((k7 >= 4) | (k3 > 0)) & ~((~c1_in3) & (k7 == 2))
    best = np.where(ok7, np.maximum(best, s7), best)
    nonclean = (k3 > 0) | (k7 > 0)
    return nonclean & (c1 + best > theta)


def main():
    nsamp = int(float(sys.argv[1])) if len(sys.argv) > 1 else 2_000_000
    eps = float(sys.argv[2]) if len(sys.argv) > 2 else 0.02
    seed = int(sys.argv[3]) if len(sys.argv) > 3 else 1
    rng = np.random.default_rng(seed)
    thetas = [0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.8, 0.9]
    chunk = 500_000
    tau = 0.0
    R = {th: 0.0 for th in thetas}
    tot = 0.0
    done = 0
    while done < nsamp:
        m = min(chunk, nsamp - done)
        k3, t3, w3 = sample_window(rng, m, eps)
        k7, t7, w7 = sample_window(rng, m, eps)
        w = w3 * w7
        tot += w.sum()
        tau += w[(k3 == 0) & (k7 == 0)].sum()
        for th in thetas:
            R[th] += w[splittable(k3, t3, k7, t7, th)].sum()
        done += m
    res = {"nsamp": nsamp, "eps": eps, "seed": seed,
           "P_clean_clean": tau / tot,
           "R_over_tau": {str(th): R[th] / tau for th in thetas}}
    print(json.dumps(res, indent=1))


if __name__ == "__main__":
    main()
