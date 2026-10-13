"""O197: correlation of normalised counts r_m(p) = f_m(p)/fit_m(p) across numerators, primes in [lo, hi)
(fit = least squares a log^3 p + b log^2 p, ms_classes.normalised).  usage: ms_corr.py lo hi m1 m2 ..."""
import sys
import numpy as np
from ms_classes import normalised

lo, hi = int(sys.argv[1]), int(sys.argv[2]); ms = [int(a) for a in sys.argv[3:]]
R = {}
for m in ms:
    ps, r, f = normalised(m, lo, hi)
    R[m] = dict(zip(ps, r))
common = sorted(set.intersection(*[set(R[m]) for m in ms]))
X = np.array([[R[m][p] for p in common] for m in ms])
C = np.corrcoef(X)
print(f"{len(common)} primes in [{lo},{hi}); Pearson correlation of normalised counts:")
print("     " + "".join(f"{m:6d}" for m in ms))
for i, m in enumerate(ms):
    print(f"{m:4d} " + "".join(f"{C[i, j]:6.2f}" for j in range(len(ms))))
