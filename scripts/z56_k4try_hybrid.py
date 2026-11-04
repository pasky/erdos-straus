#!/usr/bin/env python3
"""z56 K4TRY: model ledger for the HYBRID route to P(4,15):
   weight r*(4p+1) (primitive representations; exact, level 1/2 via the hyperbola trick)  x
   semi-linear lower sieve on p+4 to z = x^thz (thz > 1/4) at level x^the, Iwaniec switching for p+4 = m q q'.
Units: X * M * W(z) (M = mean of the r*-weight on the sieved sequence).  Same F, f, B as scripts/z55_p415_sieve.py
(semi-linear beta sieve, kappa = 1/2, beta = 1), imported from there.

  main      = f(s),  s = the/thz  (needs s > 1)
  switched  = pen * (2/a) * B(thz),  a = level (x-exponent) at which the prime p = m q q' - 4 is detected by an upper
              linear sieve inside the switched sum; 2/a = its loss (P415 convention).  The r*-weight itself is evaluated
              exactly (hyperbola) at cost 1/2, so a = lam_sw - 1/2 where lam_sw is the level available for the switched
              sums (primes q' in progressions).  'same' : lam_sw = 1/2 + the (the hypothesis covers switched sums);
              'gauss': the switched sum is bounded without primes-in-progressions input (Poisson in Z[i] + Weil, level
              x^{1/6} relative to Y ~ sqrt x), both k and p sieved: loss (2/a)^2 with a = 1/3.
  total level L = 1/2 + the.
Output: minimal L with f(s) - switched > 0, for pen in {1, 2.35}.
Usage: python z56_k4try_hybrid.py
"""
import math, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__))))
from z55_p415_sieve import Fv, fv, B

def hybrid_margin(thz, the, pen, mode):
    s = the / thz
    if s <= 1: return -1e9, None
    if mode == 'same':
        a = the  # lam_sw = 1/2 + the
        sw = pen * (2 / a) * B(thz)
    elif mode == 'gauss':
        sw = pen * (2 / (1 / 3)) ** 2 * B(thz)
    else:
        raise ValueError(mode)
    return fv(s) - sw, (s, fv(s), sw)

def best_level(pen, mode):
    def ok(L):
        the = L - 0.5
        best = None
        for i in range(1, 2500):
            thz = 0.25 + i * 0.0001
            v, info = hybrid_margin(thz, the, pen, mode)
            if v > 0 and (best is None or v > best[1]): best = (thz, v, info)
        return best
    lo, hi = 0.5, 1.5
    if ok(hi) is None: return None, None
    for _ in range(24):
        mid = (lo + hi) / 2
        if ok(mid): hi = mid
        else: lo = mid
    return hi, ok(hi)

if __name__ == "__main__":
    print("# B(thz) = F(1/thz) - F(1) sqrt(thz): Buchstab mass of the two-Q-factor configurations (units W(z))")
    for t in [0.25, 0.26, 0.28, 0.3, 0.35, 0.4, 0.45, 0.48, 0.49, 0.499]:
        print(f"  thz={t:.3f}  B={B(t):.5f}")
    for mode in ('same', 'gauss'):
        for pen in (1.0, 2.35):
            L, det = best_level(pen, mode)
            print(f"mode={mode:5s} pen={pen:4.2f}: minimal sufficient total level L = {L}  (thz, margin, (s, f(s), switched)) = {det}")
