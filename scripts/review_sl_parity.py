"""R175: parity of W(p) across 32 local classes (p mod 8, (p/3),(p/5),(p/7),(p/11)), primes p = 1 mod 4 in [A,B)."""
import sys, numpy as np
from collections import defaultdict
from review_sl_rayclass import jac
W = np.load(sys.argv[1]); A, B = int(sys.argv[2]), int(sys.argv[3])
sv = np.ones(B, bool); sv[:2] = False
for i in range(2, int(B ** .5) + 1):
    if sv[i]: sv[i*i::i] = False
cls = defaultdict(lambda: [0, 0]); tot = [0, 0]
for p in range(A, B):
    if sv[p] and p % 4 == 1:
        k = (p % 8,) + tuple(jac(p, l) for l in (3, 5, 7, 11))
        o = int(W[p]) % 2
        cls[k][0] += o; cls[k][1] += 1; tot[0] += o; tot[1] += 1
fr = [a / b for a, b in cls.values()]
print("classes", len(cls), "P(W odd) range", round(min(fr), 3), round(max(fr), 3), "overall", round(tot[0] / tot[1], 3), "n", tot[1])
