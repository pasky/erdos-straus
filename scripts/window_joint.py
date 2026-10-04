#!/usr/bin/env python3
"""POINTWISE_WINDOW.md sections 3-5 -- EVIDENCE: joint F1-failure of the first J windows.

For primes p = 840k+1 <= XMAX and windows q = 3, 7, 11, 15, ... (q = 3 mod 4), n_q = (p+q)/4.
Window q is "F1-clean" if every prime factor r of n_q has Jacobi (r/q) = +1 (Lemma 1.1:
then window q fails).  Counts, for each prefix J, the primes for which windows
3, 7, ..., 4J-1 are all F1-clean; normalised by x/(log x)^{1+J/2}.

Usage: window_joint.py XMAX JMAX
"""
import sys
import json
from math import log, isqrt
import numpy as np
from sympy import primerange
from sympy.functions.combinatorial.numbers import jacobi_symbol


def bad_mask(k0, k1, q, P_SMALL):
    """bool array: n_q = 210k + (q+1)/4 has a q-bad prime factor, k in [k0,k1)."""
    c = (q + 1) // 4
    k = np.arange(k0, k1, dtype=np.int64)
    cof = 210 * k + c
    bad = np.zeros(len(k), dtype=bool)
    for r in P_SMALL:
        if 210 % r == 0:
            if c % r:
                continue
            idx = np.arange(len(k))
        else:
            rr = (-c * pow(210, -1, r)) % r
            idx = np.arange((rr - k0) % r, len(k), r)
        if len(idx) == 0:
            continue
        if q % r and jacobi_symbol(r, q) == -1:
            bad[idx] = True
        sub = cof[idx]
        while True:
            m = sub % r == 0
            if not m.any():
                break
            sub[m] //= r
        cof[idx] = sub
    big = cof > 1   # a single prime > sqrt
    tab = np.array([jacobi_symbol(a, q) == -1 for a in range(q)])
    jb = big & tab[cof % q]
    return bad | jb


def run(XMAX, JMAX, BLOCK=2_000_000):
    KMAX = (XMAX - 1) // 840
    PP = list(primerange(2, isqrt(XMAX) + 2))
    QS = [4 * j + 3 for j in range(JMAX)]
    edges = [10 ** e for e in range(6, 40) if 10 ** e < XMAX] + [XMAX]
    cnt = np.zeros((len(edges), JMAX + 1), dtype=np.int64)
    for k0 in range(0, KMAX + 1, BLOCK):
        k1 = min(k0 + BLOCK, KMAX + 1)
        k = np.arange(k0, k1, dtype=np.int64)
        p = 840 * k + 1
        isp = p > 1
        for l in PP:
            if 840 % l == 0:
                continue
            r = (-pow(840, -1, l)) % l
            isp[(r - k0) % l::l] = False
            if (l - 1) % 840 == 0 and k0 <= (l - 1) // 840 < k1:
                isp[(l - 1) // 840 - k0] = True
        alive = isp.copy()
        for e_i, e in enumerate(edges):
            cnt[e_i, 0] += int(np.count_nonzero(alive & (p <= e)))
        for j, q in enumerate(QS):
            idx = np.flatnonzero(alive)
            if len(idx) == 0:
                break
            # only test the still-alive primes (cheap): compute bad mask on full block once per q
            bm = bad_mask(k0, k1, q, [r for r in PP if r * r <= 210 * k1 + q])
            alive &= ~bm
            for e_i, e in enumerate(edges):
                cnt[e_i, j + 1] += int(np.count_nonzero(alive & (p <= e)))
    rows = []
    for e_i, e in enumerate(edges):
        L = log(e)
        rows.append(dict(x=e, counts=cnt[e_i].tolist(),
                         norm=[cnt[e_i, J] / (e / L ** (1 + J / 2)) for J in range(JMAX + 1)]))
    return dict(XMAX=XMAX, windows=QS, rows=rows)


if __name__ == "__main__":
    XMAX = int(float(sys.argv[1]))
    JMAX = int(sys.argv[2])
    out = run(XMAX, JMAX)
    for r in out["rows"]:
        print(r["x"], r["counts"], ["%.4g" % v for v in r["norm"]])
    with open(f"data/pointwise_window/joint_{XMAX}_{JMAX}.json", "w") as f:
        json.dump(out, f, indent=1)
