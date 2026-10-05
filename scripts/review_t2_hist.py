"""R24: from-scratch check of EXCEPTIONAL_TUPLES2 §5(d): histogram of f_y on [1,N] vs exact
Poisson-binomial CRT law.  usage: review_t2_hist.py N y"""
import sys
import numpy as np
from sympy import primerange, divisors
N = int(float(sys.argv[1])); y = int(sys.argv[2])
P = [l for l in primerange(3, y + 1) if l % 4 == 3]
f = np.zeros(N + 1, dtype=np.int16)
law = np.array([1.0])
for l in P:
    R = {(-4 * D) % l for D in divisors(((l + 1) // 4) ** 2)}
    for b in R:
        f[b::l] += 1
    p = len(R) / l
    law = np.convolve(law, [1 - p, p])
h = np.bincount(f[1:], minlength=len(law))
for k in range(len(h)):
    print(k, int(h[k]), f"{N * law[k]:.1f}")
