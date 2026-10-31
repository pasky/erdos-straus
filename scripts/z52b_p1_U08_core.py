"""z52b pass-1 batch U08 (redo pass): shared helpers.
  divs_from_fac / good_divs : divisors d>1 of N with d ≡ -1 (mod m)   (the (★)-type level-C condition with m = 4C)
  Cmin_R                    : per prime p, success vector over C <= Cmax, least C, and R(p) = sum_C #good divisors
  load_U                    : U(n) = #solutions of 4/n from data/z52b/raw/f4_all_30000.txt
"""
import numpy as np
from sympy import factorint, primerange

def divs_from_fac(fac):
    ds = [1]
    for q, e in fac.items():
        ds = [d * q ** k for d in ds for k in range(e + 1)]
    return ds

def good_divs(N, m, fac=None):
    """all divisors d > 1 of N with d ≡ -1 (mod m)."""
    if fac is None:
        fac = factorint(N)
    return [d for d in divs_from_fac(fac) if d > 1 and d % m == m - 1]

def load_U():
    F = np.loadtxt("data/z52b/raw/f4_all_30000.txt", dtype=np.int64)
    return dict(zip(F[:, 0].tolist(), F[:, 1].tolist()))

def primes_1mod4(lo, hi):
    return [p for p in primerange(lo, hi + 1) if p % 4 == 1]

def level_table(primes, Cmax):
    """S[i,C] (bool, C=1..Cmax), Cmin[i] (least successful C, or Cmax+1), R[i] = sum_C #good divisors."""
    S = np.zeros((len(primes), Cmax + 1), dtype=bool)
    R = np.zeros(len(primes), dtype=np.int64)
    for i, p in enumerate(primes):
        for C in range(1, Cmax + 1):
            N = 4 * C * p + 1
            g = good_divs(N, 4 * C)
            if g:
                S[i, C] = True
                R[i] += len(g)
    Cmin = np.array([int(np.argmax(S[i])) if S[i].any() else Cmax + 1 for i in range(len(primes))])
    return S, Cmin, R
