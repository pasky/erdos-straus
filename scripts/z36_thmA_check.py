"""O266: numerical check of the inequalities in ZAREMBA_TRANSFER Theorem A.
For primes p: N_k = #{(a,i): c_i(a/p) >= k} vs bound 2(p/k)(1+log p); fraction of a with sum c_i <= 10(1+log p)(1+log T)."""
import sys, math
import numpy as np

def digits_stats(p, ks):
    a = np.arange(1, p, dtype=np.int64)
    x = np.full_like(a, p); y = a.copy()
    cnt = {k: 0 for k in ks}; tot = np.zeros_like(a)
    alive = y > 0
    while alive.any():
        yy = np.where(alive, y, 1)
        c = np.where(alive, x // yy, 0)
        for k in ks:
            cnt[k] += int((c >= k).sum())
        tot += c
        x, y = np.where(alive, y, x), np.where(alive, x - c * yy, 0)
        alive = y > 0
    return cnt, tot

for p in map(int, sys.argv[1:]):
    ks = [1, 2, 5, 10, 100, 1000]
    cnt, tot = digits_stats(p, ks)
    L = math.log(p); T = math.ceil(10 * (1 + L)); thr = 10 * (1 + L) * (1 + math.log(T))
    ratios = {k: round(cnt[k] / (2 * (p / k) * (1 + L)), 3) for k in ks}
    print(p, "N_k/bound:", ratios, "frac(sum c<=thr)=", round(float((tot <= thr).mean()), 4), "thr=", round(thr, 1),
          "median sum c=", int(np.median(tot)))
