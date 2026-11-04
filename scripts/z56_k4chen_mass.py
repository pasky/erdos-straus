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
    # grid on u in (0,1]; d_0 singular at 0 -> integrate with substitution handled by fine grid + analytic first step
    h = 1.0 / n
    u = (np.arange(n) + 1) * h            # right endpoints
    F1 = P.Fv(1.0)
    d = [F1 * np.sqrt(zeta / u)]
    for j in range(1, jmax + 1):
        prev = d[-1]
        cur = np.zeros(n)
        # cur(u_i) = (1/(2j)) sum over a in [zeta, u_i): prev(u_i - a) da / a ; use cell-averaged prev
        # cell average of prev on ((m)h,(m+1)h]: for j-1 = 0 use exact sqrt integral
        if j == 1:
            avg = F1 * math.sqrt(zeta) * 2 * (np.sqrt(u) - np.sqrt(u - h)) / h
        else:
            avg = prev
        ia0 = int(math.ceil(zeta / h))
        for i in range(n):
            # a = (i - m) h for m = 0..i-ia0 ; prev at index m-1 ... approximate: v = u_i - a in cells
            ms = np.arange(0, i - ia0 + 1)
            if len(ms) == 0: continue
            a = u[i] - (ms + 0.5) * h        # midpoint of a-cell matching v-cell m
            cur[i] = np.sum(avg[ms] / a) * h / (2 * j)
        d.append(cur)
    return [float(x[-1]) for x in d]


if __name__ == "__main__":
    for zeta in [float(a) for a in sys.argv[1:]] or [0.008, 0.02, 0.05]:
        m = masses(zeta)
        ev = sum(m[0::2])
        print(f"zeta={zeta}: F(1/zeta)={P.Fv(1/zeta):.5f} sum_even={ev:.5f}; d_j(1):",
              " ".join(f"{j}:{x:.3e}" for j, x in enumerate(m) if j % 2 == 0))
