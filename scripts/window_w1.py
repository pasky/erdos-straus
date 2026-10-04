#!/usr/bin/env python3
"""POINTWISE_WINDOW.md section 3 -- EVIDENCE for Theorem W1.

Counts N_3(x) = #{p <= x prime, p = 1 (mod 840), (p+3)/4 has no prime factor = 2 (mod 3)}
(window 3 fails, so a_min(p) >= 7) and compares with x/(log x)^{3/2}.
Also re-checks a_min(p) >= 7 by the independent Rat_q routine of pointwise_size_amin
on a random subsample of the counted primes.

Usage: window_w1.py XMAX [NCHECK]
Segmented: p = 840k+1, n = (p+3)/4 = 210k+1.
"""
import sys
import json
import random
from math import log, isqrt
import numpy as np
from sympy import primerange, factorint, isprime
from pointwise_size_amin import amin


def run(XMAX, NCHECK=200, BLOCK=5_000_000):
    KMAX = (XMAX - 1) // 840
    P_SMALL = list(primerange(2, isqrt(XMAX) + 2))
    Q_SMALL = [r for r in primerange(2, isqrt(XMAX // 4) + 2)]
    edges = [10 ** e for e in range(6, 40) if 10 ** e < XMAX] + [XMAX]
    cnt_p = np.zeros(len(edges), dtype=np.int64)    # primes p=1 (840) <= edge
    cnt_f = np.zeros(len(edges), dtype=np.int64)    # ... with window 3 failing
    found = []          # reservoir sample (size NCHECK) of counted primes
    nfound = 0
    rng = random.Random(1)
    for k0 in range(0, KMAX + 1, BLOCK):
        k1 = min(k0 + BLOCK, KMAX + 1)
        k = np.arange(k0, k1, dtype=np.int64)
        p = 840 * k + 1
        isp = p > 1
        for l in P_SMALL:
            if l in (2, 3, 5, 7):
                continue
            # 840k+1 = 0 mod l  <=> k = -1/840 mod l
            r = (-pow(840, -1, l)) % l
            st = (r - k0) % l
            isp[st::l] = False
            # undo for p == l itself
            if (l - 1) % 840 == 0 and k0 <= (l - 1) // 840 < k1:
                isp[(l - 1) // 840 - k0] = True
        n = 210 * k + 1
        cof = n.copy()
        bad = np.zeros(len(k), dtype=bool)
        for r in Q_SMALL:
            if r in (2, 3, 5, 7):
                continue
            rr = (-pow(210, -1, r)) % r
            st = (rr - k0) % r
            idx = np.arange(st, len(k), r)
            if len(idx) == 0:
                continue
            if r % 3 == 2:
                bad[idx] = True
            # divide out r completely
            sub = cof[idx]
            while True:
                m = sub % r == 0
                if not m.any():
                    break
                sub[m] //= r
            cof[idx] = sub
        # remaining cofactor is 1 or a single prime > sqrt(n)
        bad |= (cof > 1) & (cof % 3 == 2)
        fail = isp & ~bad
        for i, e in enumerate(edges):
            cnt_p[i] += int(np.count_nonzero(isp & (p <= e)))
            cnt_f[i] += int(np.count_nonzero(fail & (p <= e)))
        for v in p[fail].tolist():
            nfound += 1
            if len(found) < NCHECK:
                found.append(v)
            else:
                j = rng.randrange(nfound)
                if j < NCHECK:
                    found[j] = v
    rows = []
    for i, e in enumerate(edges):
        rows.append(dict(x=int(e), primes=int(cnt_p[i]), fail3=int(cnt_f[i]),
                         ratio_to_x_log32=cnt_f[i] / (e / log(e) ** 1.5),
                         frac=cnt_f[i] / max(cnt_p[i], 1),
                         frac_times_sqrtlog=cnt_f[i] / max(cnt_p[i], 1) * log(e) ** 0.5))
    # independent re-check on a subsample
    sub = found
    hist = {}
    for p in sub:
        assert isprime(p) and p % 840 == 1
        n = (p + 3) // 4
        assert all(r % 3 == 1 for r in factorint(n)), p
        q, _ = amin(p, factorint)
        assert q >= 7, p
        hist[q] = hist.get(q, 0) + 1
    return dict(XMAX=XMAX, rows=rows, recheck=len(sub), amin_hist=dict(sorted(hist.items())))


if __name__ == "__main__":
    XMAX = int(float(sys.argv[1]))
    NCHECK = int(sys.argv[2]) if len(sys.argv) > 2 else 200
    out = run(XMAX, NCHECK)
    for r in out["rows"]:
        print(r)
    print("recheck", out["recheck"], "amin hist", out["amin_hist"])
    with open(f"data/pointwise_window/w1_{XMAX}.json", "w") as f:
        json.dump(out, f, indent=1)
