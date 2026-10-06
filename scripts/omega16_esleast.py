"""OMEGA16 §6 (N2): least hard prime with W(p) > T, versus the Haar density delta*(T) (EVIDENCE).

'hard' here = p ≡ 1 (mod 24), as in POINTWISE_SIZE §7 (delta* normalised within 1 (24)).
Segmented sieve over [1, N); for each threshold T in 7,15,31,...,TMAX record the least p with
W(p) > T (W capped at TMAX), and the count.

Usage: PYTHONPATH=scripts uv run python scripts/omega16_esleast.py TMAX N [SEG]
"""
import sys, json, math
import numpy as np
from sympy import primerange
from pointwise_size_wtail import build_rows, thresholds


def main():
    TMAX = int(sys.argv[1])
    N = int(float(sys.argv[2]))
    SEG = int(float(sys.argv[3])) if len(sys.argv) > 3 else 10 ** 8
    rows = build_rows(TMAX)
    ts = thresholds(TMAX)
    small = np.array(list(primerange(2, int(math.isqrt(N)) + 2)), dtype=np.int64)
    best = {t: None for t in ts}
    count = {t: 0 for t in ts}
    lo = 0
    while lo < N:
        hi = min(N, lo + SEG)
        seg = np.ones(hi - lo, dtype=bool)
        for p in small:
            if p * p >= hi:
                break
            start = max(p * p, ((lo + p - 1) // p) * p)
            seg[start - lo :: p] = False
        if lo == 0:
            seg[:2] = False
        # candidates n ≡ 1 (24)
        first = (1 - lo) % 24
        cand = np.arange(lo + first, hi, 24, dtype=np.int64)
        alive = cand[seg[cand - lo]]
        ti = 0
        for (M, _, tab) in rows:
            while ti < len(ts) and ts[ti] < M:
                t = ts[ti]
                count[t] += int(len(alive))
                if len(alive) and best[t] is None:
                    best[t] = int(alive[0])
                ti += 1
            if len(alive) == 0:
                break
            alive = alive[~tab[alive % M]]
        while ti < len(ts):
            t = ts[ti]
            count[t] += int(len(alive))
            if len(alive) and best[t] is None:
                best[t] = int(alive[0])
            ti += 1
        lo = hi
        print(json.dumps({'upto': hi, 'best': best}), file=sys.stderr, flush=True)
    print(json.dumps({'TMAX': TMAX, 'N': N, 'least_p_W_gt_T': best, 'count_W_gt_T': count}))


if __name__ == '__main__':
    main()
