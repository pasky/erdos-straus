"""zl_level1_survivors.py -- O228 (STERILE_LOWER.md §4; CERTIFIED by exhaustive enumeration, exact integers):
for each prime r in [lo, hi), the number of quadratic non-residue classes mod r NOT covered at level 1 by in-cell P-data
(N = r) or Q-data (F = r) -- the same objects and enumeration as R223's review_se2_level1.py (P_data, Q_data)."""
import sys
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from review_se2_identities import P_data, Q_data, legendre
from sympy import primerange
lo, hi = int(sys.argv[1]), int(sys.argv[2])
for r in primerange(lo, hi):
    cov = set()
    for (a, b, c, d, e) in P_data(r):
        if c % r and d % r and a % r and b % r:
            cov |= {(-(4 * a * c * d - 1)) % r, (-(4 * b * c * d - 1)) % r}
    for (a, b, c, d, e, f) in Q_data(r):
        if e % r and c % r:
            cov |= {(-4 * a * a * d) % r, (-4 * b * b * d) % r}
    nr = [u for u in range(1, r) if legendre(u, r) == -1]
    surv = sorted(set(nr) - cov)
    print(r, len(nr), len(surv), surv[:8] if len(surv) <= 8 else len(surv))
