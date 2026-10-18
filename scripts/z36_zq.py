"""O266: Hypothesis ZQ_M numerics.  For primes p in [lo, hi) (step sampling optional) compute
  mz(p)  = min_a max digit of a/p            (Zaremba constant at p)
  mzq(p) = min over quadratic NON-residues a of max digit of a/p
and report the max of mzq over the range, the worst primes, and the histogram.  Odd squares as T1 control are trivial
(no Jacobi -1 numerators at all), reported for completeness.
Usage: z36_zq.py lo hi [stride]"""
import sys
import numpy as np
from z36_ladder import jacobi_vec

def maxdig(p):
    a = np.arange(1, p, dtype=np.int64)
    x = np.full_like(a, p); y = a.copy(); md = np.zeros_like(a)
    alive = y > 0
    while alive.any():
        yy = np.where(alive, y, 1)
        c = np.where(alive, x // yy, 0)
        md = np.maximum(md, c)
        x, y = np.where(alive, y, x), np.where(alive, x - c * yy, 0)
        alive = y > 0
    return a, md

def isprime(n):
    if n < 2: return False
    i = 2
    while i * i <= n:
        if n % i == 0: return False
        i += 1
    return True

lo, hi = int(sys.argv[1]), int(sys.argv[2]); stride = int(sys.argv[3]) if len(sys.argv) > 3 else 1
hist = {}; worst = []; cnt = 0
n = lo
while n < hi:
    if isprime(n) and n > 5:
        a, md = maxdig(n)
        chi = jacobi_vec(a, n)
        mz, mzq = int(md.min()), int(md[chi == -1].min())
        hist[mzq] = hist.get(mzq, 0) + 1; cnt += 1
        worst.append((mzq, mz, n))
    n += stride if stride > 1 else 1
worst.sort(reverse=True)
print("primes", cnt, "hist(mzq)", dict(sorted(hist.items())), "worst (mzq,mz,p)", worst[:6])
