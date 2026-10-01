#!/usr/bin/env python3
"""POINTWISE_SIZE.md section 7 -- the multiplier tail P(W > T).

W(n) = min{ M = 3 (mod 4) : n = -4D (mod M) for some D | ((M+1)/4)^2 }  (notes (58.3), (65.1)).

Two measurements:

 (A) the PROFINITE avoider density
        delta*(T) = Prob_{n in Zhat, n = 1 (24), n a unit at every l <= T} [ W(n) > T ],
     by exact Monte Carlo on Zhat: independent uniform unit residues n mod l^k (l^k <= Tmax)
     for every prime l, with n = 1 (mod 3) at l = 3 (2 never divides M); n mod M by CRT.
     For FIXED T, Dirichlet gives  #{p <= N hard : W(p) > T} ~ delta*(T) * pi_h(N)  (PROVED,
     since {W > T} is a union of unit classes mod lcm(M <= T)).

 (B) the EMPIRICAL tail on actual hard primes p = 1 (mod 24) sampled near 10^k.

Usage:
  PYTHONPATH=scripts uv run python scripts/pointwise_size_wtail.py profinite TMAX NBATCH BATCH SEED
  PYTHONPATH=scripts uv run python scripts/pointwise_size_wtail.py primes TMAX EXP NSAMPLE SEED
"""
import sys
import json
import numpy as np
from sympy import factorint, primerange, isprime


def build_rows(TMAX):
    """For each M = 3 mod 4, 3 <= M <= TMAX: (M, factorisation, boolean table of R(M))."""
    rows = []
    for M in range(3, TMAX + 1, 4):
        A = (M + 1) // 4
        fa = factorint(A)
        divs = [1]
        for l, e in fa.items():
            divs = [d * l ** i for d in divs for i in range(2 * e + 1)]
        tab = np.zeros(M, dtype=bool)
        for D in divs:
            tab[(-4 * D) % M] = True
        rows.append((M, factorint(M), tab))
    return rows


def thresholds(TMAX):
    ts, t = [], 7
    while t <= TMAX:
        ts.append(t)
        t = 2 * t + 1
    return ts


def profinite(TMAX, nbatch, batch, seed):
    rng = np.random.default_rng(seed)
    rows = build_rows(TMAX)
    kmax = {}
    for l in primerange(3, TMAX + 1):
        k = 1
        while l ** (k + 1) <= TMAX:
            k += 1
        kmax[l] = k
    ts = thresholds(TMAX)
    surv = {t: 0 for t in ts}
    total = 0
    for b in range(nbatch):
        n = batch
        res = {}                      # l -> residues mod l^kmax of current survivors
        alive = n
        ti = 0
        for (M, fM, tab) in rows:
            while ti < len(ts) and ts[ti] < M:
                surv[ts[ti]] += alive
                ti += 1
            if alive == 0:
                break
            r = np.zeros(alive, dtype=np.int64)
            for l, e in fM.items():
                if l not in res:
                    mod = l ** kmax[l]
                    if l == 3:     # n = 1 mod 3, uniform among such mod 3^k
                        res[l] = 1 + 3 * rng.integers(0, mod // 3, size=alive, dtype=np.int64)
                    else:          # uniform unit mod l^k
                        x = rng.integers(0, mod, size=alive, dtype=np.int64)
                        bad = (x % l) == 0
                        while bad.any():
                            x[bad] = rng.integers(0, mod, size=int(bad.sum()), dtype=np.int64)
                            bad = (x % l) == 0
                        res[l] = x
                le = l ** e
                Mp = M // le
                c = Mp * pow(Mp, -1, le)           # CRT idempotent mod M
                r = (r + (res[l] % le) * c) % M
            hit = tab[r]
            if hit.any():
                keep = ~hit
                alive = int(keep.sum())
                for l in res:
                    res[l] = res[l][keep]
        while ti < len(ts):
            surv[ts[ti]] += alive
            ti += 1
        total += n
    out = {'TMAX': TMAX, 'samples': total, 'seed': seed,
           'delta': {t: surv[t] / total for t in ts}, 'counts': surv}
    print(json.dumps(out))


def split(TMAX, nbatch, batch, seed):
    """Multilevel splitting estimate of delta*(T): whenever the survivors fall below batch/8
    at a dyadic threshold, every survivor is cloned (state = residues already drawn; fresh
    primes are drawn independently per clone) and the weight is divided accordingly.
    Unbiased; reaches far smaller densities than plain Monte Carlo."""
    rng = np.random.default_rng(seed)
    rows = build_rows(TMAX)
    kmax = {}
    for l in primerange(3, TMAX + 1):
        k = 1
        while l ** (k + 1) <= TMAX:
            k += 1
        kmax[l] = k
    ts = thresholds(TMAX)
    est = {t: [] for t in ts}
    for b in range(nbatch):
        alive = batch
        weight = 1.0 / batch
        res = {}
        ti = 0
        for (M, fM, tab) in rows:
            while ti < len(ts) and ts[ti] < M:
                est[ts[ti]].append(alive * weight)
                if 0 < alive < batch // 8:
                    f = max(1, batch // alive)
                    for l in res:
                        res[l] = np.tile(res[l], f)
                    alive *= f
                    weight /= f
                ti += 1
            if alive == 0:
                break
            r = np.zeros(alive, dtype=np.int64)
            for l, e in fM.items():
                if l not in res:
                    mod = l ** kmax[l]
                    if l == 3:
                        res[l] = 1 + 3 * rng.integers(0, mod // 3, size=alive, dtype=np.int64)
                    else:
                        x = rng.integers(0, mod, size=alive, dtype=np.int64)
                        bad = (x % l) == 0
                        while bad.any():
                            x[bad] = rng.integers(0, mod, size=int(bad.sum()), dtype=np.int64)
                            bad = (x % l) == 0
                        res[l] = x
                le = l ** e
                Mp = M // le
                c = Mp * pow(Mp, -1, le)
                r = (r + (res[l] % le) * c) % M
            hit = tab[r]
            if hit.any():
                keep = ~hit
                alive = int(keep.sum())
                for l in res:
                    res[l] = res[l][keep]
        while ti < len(ts):
            est[ts[ti]].append(alive * weight)
            ti += 1
    out = {'TMAX': TMAX, 'batches': nbatch, 'batch': batch, 'seed': seed,
           'delta': {t: float(np.mean(v)) for t, v in est.items()},
           'stderr': {t: float(np.std(v) / np.sqrt(len(v))) for t, v in est.items()}}
    print(json.dumps(out))


def primes(TMAX, exp, nsample, seed):
    import random
    random.seed(seed)
    rows = build_rows(TMAX)
    ts = thresholds(TMAX)
    W = []
    lo = 10 ** exp
    while len(W) < nsample:
        p = lo + 24 * random.randrange(10 ** exp // 24) + 1
        p -= (p - 1) % 24
        if not isprime(p):
            continue
        w = None
        for (M, _, tab) in rows:
            if tab[p % M]:
                w = M
                break
        W.append(w if w is not None else TMAX + 1)
    W = np.array(W)
    out = {'TMAX': TMAX, 'exp': exp, 'samples': nsample, 'seed': seed,
           'tail': {t: float((W > t).mean()) for t in ts}, 'counts': {t: int((W > t).sum()) for t in ts},
           'max': int(W.max())}
    print(json.dumps(out))


def census(TMAX, N):
    """Exact W(p) (capped at TMAX) for all hard primes p < N; counts of W > T."""
    rows = build_rows(TMAX)
    sieve = np.ones(N, dtype=bool)
    sieve[:2] = False
    for l in primerange(2, int(N ** 0.5) + 1):
        sieve[l * l::l] = False
    ps = np.flatnonzero(sieve[1::24]) * 24 + 1
    ps = ps[sieve[ps]]
    alive = ps.astype(np.int64)
    ts = thresholds(TMAX)
    counts, ti = {}, 0
    for (M, _, tab) in rows:
        while ti < len(ts) and ts[ti] < M:
            counts[ts[ti]] = int(len(alive))
            ti += 1
        alive = alive[~tab[alive % M]]
    while ti < len(ts):
        counts[ts[ti]] = int(len(alive))
        ti += 1
    print(json.dumps({'N': N, 'hard_primes': int(len(ps)), 'counts_W_gt_T': counts,
                      'survivors_beyond_TMAX': alive.tolist()[:20]}))


if __name__ == '__main__':
    mode = sys.argv[1]
    a = [int(x) for x in sys.argv[2:]]
    if mode == 'profinite':
        profinite(*a)
    elif mode == 'split':
        split(*a)
    elif mode == 'census':
        census(*a)
    else:
        primes(*a)
