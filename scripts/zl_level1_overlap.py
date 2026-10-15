"""zl_level1_overlap.py -- O228 exploration (EVIDENCE): level-1 classes of P-data (N = r) and Q-data (F = r), in-cell,
and their overlap; prints for primes r in a range: #P-classes, #Q-classes, #(Q \\ P), (r-1)/2."""
import sys
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from review_se2_identities import P_data, Q_data
from sympy import primerange
lo, hi = int(sys.argv[1]), int(sys.argv[2])
for r in primerange(lo, hi):
    Pc, Qc = set(), set()
    for (a, b, c, d, e) in P_data(r):
        if c % r and d % r and a % r and b % r:
            Pc |= {(-(4 * a * c * d - 1)) % r, (-(4 * b * c * d - 1)) % r}
    for (a, b, c, d, e, f) in Q_data(r):
        if e % r and c % r:
            Qc |= {(-4 * a * a * d) % r, (-4 * b * b * d) % r}
    print(r, len(Pc), len(Qc), len(Qc - Pc), len(Pc | Qc), (r - 1) // 2)
