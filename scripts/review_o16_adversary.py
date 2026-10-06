"""R61 from-scratch adversary against LS: events concentrated on large prime moduli.

Moduli: primes l in (alpha*T, T]; budget k classes per modulus (unit classes).
Greedy: walk primes p>T upward; if p survives, kill the class p mod l for the l (with budget left)
whose class contains the most surviving primes in the next LOOK primes. Stop at the first prime
that survives with no budget left that could kill it (every l exhausted) -> p_min.
delta = prod (1 - used_l/(l-1))   (exact Haar density of the avoider set in Z^x; prime moduli
are independent by CRT). LS ratio = log p_min / (log T + log(1/delta)).

usage: review_o16_adversary.py T k alpha Xmax [LOOK]
"""
import sys
import math
import numpy as np


def primes_upto(n):
    s = np.ones(n + 1, dtype=bool)
    s[:2] = False
    for i in range(2, int(n**0.5) + 1):
        if s[i]:
            s[i * i::i] = False
    return np.nonzero(s)[0].astype(np.int64)


def run(T, k, alpha, Xmax, LOOK=2000):
    P = primes_upto(Xmax)
    mods = [int(l) for l in P[(P > alpha * T) & (P <= T)]]
    budget = {l: k for l in mods}
    killed = {l: np.zeros(l, dtype=bool) for l in mods}
    cand = P[P > T]
    i = 0
    n = len(cand)
    blk_end = 0
    alive_blk = None
    while i < n:
        if i >= blk_end:
            blk_start, blk_end = i, min(i + 65536, n)
            b = cand[blk_start:blk_end]
            alive_blk = np.ones(len(b), dtype=bool)
            for l in mods:
                alive_blk &= ~killed[l][b % l]
            nz = np.nonzero(alive_blk)[0]
            if len(nz) == 0:
                i = blk_end
                continue
        nz = np.nonzero(alive_blk[i - blk_start:])[0]
        if len(nz) == 0:
            i = blk_end
            continue
        i = blk_start + (i - blk_start) + int(nz[0])
        p = int(cand[i])
        live = [l for l in mods if budget[l] > 0]
        if not live:
            break
        win = cand[i:i + LOOK]
        # surviving mask on window
        alive = np.ones(len(win), dtype=bool)
        for l in mods:
            alive &= ~killed[l][win % l]
        w = win[alive]
        best, bestc = None, -1
        for l in live:
            c = int(np.count_nonzero((w - p) % l == 0))
            if c > bestc:
                best, bestc = l, c
        killed[best][p % best] = True
        budget[best] -= 1
        b = cand[blk_start:blk_end]
        alive_blk &= (b % best) != (p % best)
        i += 1
    if i >= n:
        return None, mods, budget
    return int(cand[i]), mods, budget


if __name__ == "__main__":
    T, k, alpha, Xmax = int(sys.argv[1]), int(sys.argv[2]), float(sys.argv[3]), int(float(sys.argv[4]))
    LOOK = int(sys.argv[5]) if len(sys.argv) > 5 else 2000
    pmin, mods, budget = run(T, k, alpha, Xmax, LOOK)
    logdel = -sum(math.log(1 - (k - budget[l]) / (l - 1)) for l in mods)
    lam = math.log(T) + logdel
    if pmin is None:
        print(f"T={T} k={k} alpha={alpha} m={len(mods)} log(1/delta)={logdel:.3f} p_min>{Xmax} ratio>{math.log(Xmax)/lam:.3f}")
    else:
        rnd = math.log(pmin) / lam
        print(f"T={T} k={k} alpha={alpha} m={len(mods)} log(1/delta)={logdel:.3f} p_min={pmin} "
              f"logp={math.log(pmin):.2f} LSratio={rnd:.3f} delta*p/logp={math.exp(-logdel)*pmin/math.log(pmin):.1f}")
