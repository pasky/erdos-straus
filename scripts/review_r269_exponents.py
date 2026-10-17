"""R269: from-scratch evaluation of the parameter choices in BALANCED_LATTICE Thm 4.1 / Thm 4.2.
For L2 := log log p, y := L2*log L2, S = odd primes <= y, x := C0*phi(8P)^2*log^4 p:
  Thm 4.1: 1/eps = 6 x^{2/(k+1)} (C logP/c3)^{(k-1)/(k+1)},  L = k^{3/2}/eps;
  Thm 4.2: eps = x^{-3/(2k)},  L = k^{3/2}/eps.
Prints log L / log L2 (claimed -> 13/2 and 9/2) and the side conditions (log-scale).
Usage: uv run --with numpy python scripts/review_r269_exponents.py
"""
import math
import numpy as np


def sieve(n):
    s = np.ones(n + 1, dtype=bool); s[:2] = False
    for i in range(2, int(n ** 0.5) + 1):
        if s[i]: s[i * i::i] = False
    return np.nonzero(s)[0]


PR = sieve(30_000_000)
C0 = C = 1e3; c3 = 1e-3
print("L2 | y | k | log x/y | Thm4.1 logL/logL2 (1/eps part, k^1.5 part) | Thm4.2 logL/logL2 | logL/log y (4.1, 4.2)")
for L2 in [1e2, 1e3, 1e4, 1e5, 1e6, 1.5e6]:
    y = L2 * math.log(L2)
    S = PR[(PR >= 3) & (PR <= y)].astype(np.float64)
    k = len(S); logP = float(np.log(S).sum())
    logphi = math.log(4) + float(np.log(S - 1).sum())
    logx = math.log(C0) + 2 * logphi + 4 * L2
    inv_eps1 = math.log(6) + 2 * logx / (k + 1) + (k - 1) / (k + 1) * math.log(C * logP / c3)
    logL1 = 1.5 * math.log(k) + inv_eps1
    inv_eps2 = 1.5 * logx / k
    logL2_ = 1.5 * math.log(k) + inv_eps2
    print(f"{L2:.0e} | {y:.3g} | {k} | {logx / y:.3f} | {logL1 / math.log(L2):.3f} ({inv_eps1 / math.log(L2):.3f}, {1.5 * math.log(k) / math.log(L2):.3f})"
          f" | {logL2_ / math.log(L2):.3f} | {logL1 / math.log(y):.3f}, {logL2_ / math.log(y):.3f}")
