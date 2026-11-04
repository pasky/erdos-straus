#!/usr/bin/env python3
"""z56 K4CHEN: Buchstab masses of the 𝒬-factor configurations of a z2-rough parity-even integer (semi-linear model).
d_j(u): density (units W(z2), z2 = x^zeta) of integers of size x^u, all 𝒬-factors >= z2, exactly j of them:
  d_0(u) = F(1) sqrt(zeta/u)   (S-numbers),   d_j(u) = (1/j) (1/2) int_zeta^u d_{j-1}(u-a) da/a.
Check: sum_{j even} d_j(1) = F(1/zeta)  (extremality of F for the parity-even sequence; cf. Z55_P415 'check')."""
import math, sys, os
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import z55_p415_sieve as P


def masses(zeta, jmax=14, n=4000):
    """d_j(1), j = 0..jmax.  Grid aligned with zeta: h = zeta/m (m integer), so the cutoff a >= zeta falls on a cell
    boundary (z56 internal review finding 1: the earlier non-aligned grid dropped a partial cell).  Values at u = 1 by
    linear interpolation.  Odd j are auxiliary masses (integers = 3 mod 4), not part of the parity-even sequence."""
    m = max(1, int(round(zeta * n)))
    h = zeta / m
    N = int(math.ceil(1.0 / h)) + 1
    u = (np.arange(N) + 1) * h            # right endpoints of cells ((i)h, (i+1)h]
    F1 = P.Fv(1.0)
    prev_avg = F1 * math.sqrt(zeta) * 2 * (np.sqrt(u) - np.sqrt(u - h)) / h   # exact cell averages of d_0
    out = [np.interp(1.0, u, F1 * np.sqrt(zeta / u))]
    for j in range(1, jmax + 1):
        cur = np.zeros(N)
        # cur(u_i) = (1/(2j)) int_zeta^{u_i} prev(u_i - a) da/a ; a-cells [ (i-mm)h, (i-mm+1)h ) paired with v-cell mm
        for i in range(N):
            mmax = i - m          # v = u_i - a <= u_i - zeta  -> v-cell index <= i - m
            if mmax < 0: continue
            ms = np.arange(0, mmax + 1)
            a = u[i] - (ms + 0.5) * h
            cur[i] = np.sum(prev_avg[ms] / a) * h / (2 * j)
        out.append(float(np.interp(1.0, u, cur)))
        prev_avg = cur
    return out


if __name__ == "__main__":
    for zeta in [float(a) for a in sys.argv[1:]] or [0.008, 0.02, 0.05]:
        m = masses(zeta)
        ev = sum(m[0::2])
        print(f"zeta={zeta}: F(1/zeta)={P.Fv(1/zeta):.5f} sum_even={ev:.5f}; d_j(1):",
              " ".join(f"{j}:{x:.3e}" for j, x in enumerate(m) if j % 2 == 0))
