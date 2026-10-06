"""Probe one node x mod L: for each new prime l, which children x_l mod l stay uncovered
(classes with modulus M | L*l, M <= Mmax).  usage: mordell_probe.py L x Mmax lmax"""
import sys
import numpy as np
from mordell_cover import filt
L = int(sys.argv[1]); x = int(sys.argv[2]); Mmax = int(sys.argv[3]); lmax = int(sys.argv[4])
X = filt(np.array([x], dtype=np.int64), L, 1, Mmax)
print("node covered" if len(X) == 0 else "node uncovered")
for l in range(17, lmax + 1):
    if any(l % q == 0 for q in range(2, l)) or L % l == 0:
        continue
    t = np.arange(l, dtype=np.int64)
    Y = x + L * t
    Y = Y[Y % l != 0]
    Y = filt(Y, L * l, L, Mmax)
    surv = sorted(int(y % l) for y in Y)
    sq = sorted({(i * i) % l for i in range(1, l)})
    tag = "=squares" if surv == sq else ("subset of squares" if set(surv) <= set(sq) else "")
    print(l, len(surv), "/", l - 1, surv if len(surv) < 25 else "", tag, flush=True)
