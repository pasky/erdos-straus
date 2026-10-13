"""bsA_cover2: finite covering test for (W) using BOTH fixed-pair types:
 (t,u) fixed: n = -u (mod tu-1);  (u,v) fixed: n = -(u+v) (mod uv). Moduli must divide M. Usage: ... M"""
import sys
import numpy as np
M = int(sys.argv[1]); cov = np.zeros(M, dtype=bool)
for m in range(3, M + 1):
    if M % m: continue
    for u in range(2, m):            # type 1: m = tu-1
        if (m + 1) % u == 0 and (m + 1)//u >= 2: cov[(-u) % m::m] = True
    for u in range(2, m):            # type 2: m = uv
        if m % u == 0 and m//u >= 2: cov[(-(u + m//u)) % m::m] = True
unc = np.nonzero(~cov)[0]
print("M=%d uncovered %d (%.4f); first: %s" % (M, len(unc), len(unc)/M, unc[:15].tolist()))
print("residue M-1 uncovered:", bool(not cov[M - 1]))
