#!/usr/bin/env python3
"""POINTWISE_WINDOW2 §3.4 -- hierarchical (tree) block fakes: capacity criterion.

Composing two-block fakes (Lemma 3.2) recursively, a configuration C removes
cap(C) units of target mass, where
    cap(C) = max(0, max_{valid splits C=U⊔V} 1 + cap(U) + cap(V)),
a split being valid if U, V are nonempty, each even in each window, and
min U + min V > theta.  The criterion is  sum_C mu(C) cap(C) >= tau.
Brute force over splits (configurations with <= NMAX points; larger ones are
counted with cap from the greedy two-block test only, flagged in output).

Usage: window2_treefake.py [NSAMP] [EPS] [SEED] [THETA ...]
"""
import sys
import json
from functools import lru_cache
import numpy as np
from window2_blockfake import sample_window, splittable

NMAX = 14


def make_cap(theta):
    @lru_cache(maxsize=None)
    def cap(pts):
        # pts: tuple of (t, window) sorted by t
        n = len(pts)
        if n < 2:
            return 0
        best = 0
        rest = pts[1:]                      # c1 = pts[0] goes to U
        m = len(rest)
        for mask in range(1, 1 << m):
            V = tuple(rest[i] for i in range(m) if mask >> i & 1)
            if V[0][0] + pts[0][0] <= theta:
                continue
            if sum(1 for _, w in V if w == 3) % 2 or sum(1 for _, w in V if w == 7) % 2:
                continue
            U = (pts[0],) + tuple(rest[i] for i in range(m) if not mask >> i & 1)
            c = 1 + cap(U) + cap(V)
            if c > best:
                best = c
        return best
    return cap


def main():
    nsamp = int(float(sys.argv[1])) if len(sys.argv) > 1 else 2_000_000
    eps = float(sys.argv[2]) if len(sys.argv) > 2 else 0.02
    seed = int(sys.argv[3]) if len(sys.argv) > 3 else 1
    thetas = [float(a) for a in sys.argv[4:]] or [0.5, 0.55, 0.6]
    rng = np.random.default_rng(seed)
    caps = {th: make_cap(th) for th in thetas}
    tau = 0.0
    S = {th: 0.0 for th in thetas}
    S2 = {th: 0.0 for th in thetas}
    big = {th: 0.0 for th in thetas}
    hist = {th: {} for th in thetas}
    done = 0
    while done < nsamp:
        m = min(500_000, nsamp - done)
        k3, t3, w3 = sample_window(rng, m, eps)
        k7, t7, w7 = sample_window(rng, m, eps)
        w = w3 * w7
        tau += w[(k3 == 0) & (k7 == 0)].sum()
        for th in thetas:
            sp = splittable(k3, t3, k7, t7, th) & (w > 0)
            S2[th] += w[sp].sum()
            for i in np.nonzero(sp)[0]:
                pts = sorted([(round(float(t), 12), 3) for t in t3[i, :k3[i]]] +
                             [(round(float(t), 12), 7) for t in t7[i, :k7[i]]])
                if len(pts) > NMAX:
                    c = 1
                    big[th] += w[i]
                else:
                    c = caps[th](tuple(pts))
                S[th] += w[i] * c
                hist[th][c] = hist[th].get(c, 0.0) + w[i]
            caps[th].cache_clear()
        done += m
    out = {"nsamp": nsamp, "eps": eps, "seed": seed,
           "twoblock_R_over_tau": {str(t): S2[t] / tau for t in thetas},
           "tree_capacity_over_tau": {str(t): S[t] / tau for t in thetas},
           "big_config_mass_over_tau": {str(t): big[t] / tau for t in thetas},
           "cap_hist_over_tau": {str(t): {str(c): v / tau for c, v in sorted(hist[t].items())} for t in thetas}}
    print(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
