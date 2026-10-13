"""bsA_cover: sign-free word existence (W): n has a length-3 word with fixed (t,u) iff n = -u (mod tu-1) and
v = (n+u)/(tu-1) >= 2. Test whether the congruences n = -u (mod m), m = tu-1 | M, t,u >= 2, cover Z/M.
Usage: ... M"""
import sys
import numpy as np
M = int(sys.argv[1])
cov = np.zeros(M, dtype=bool); used = 0
divs = [m for m in range(3, M + 1) if M % m == 0]
for m in divs:
    for u in range(2, (m + 1)//2 + 1):
        if (m + 1) % u == 0 and (m + 1)//u >= 2:
            cov[(-u) % m::m] = True; used += 1
print("M=%d: %d congruences, uncovered classes %d (fraction %.4f)" % (M, used, (~cov).sum(), (~cov).mean()))
unc = np.nonzero(~cov)[0]
print("first uncovered residues:", unc[:20].tolist())
