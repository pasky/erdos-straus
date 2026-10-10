"""R123: dyadic-window min/mean of f_I from review_r123_count.c output."""
import sys, numpy as np
from math import log
N = int(sys.argv[1]); a = np.fromfile(sys.argv[2], dtype=np.uint32)
s = np.ones(N + 1, bool); s[:2] = False
for i in range(2, int(N ** .5) + 1):
    if s[i]: s[i*i::i] = False
for k in [int(x) for x in sys.argv[3:]]:
    X = 2 ** k; idx = np.nonzero(s[X:2*X])[0] + X; v = a[idx]; L = log(1.5 * X)
    j = int(np.argmin(v))
    print(f"2^{k}: primes {len(idx)} min {v[j]} at {idx[j]} (mod 840 = {idx[j] % 840}) mean {v.mean():.1f} "
          f"mean/L^2 {v.mean()/L**2:.2f} mean/L^3 {v.mean()/L**3:.3f} min/mean {v[j]/v.mean():.3f}")
