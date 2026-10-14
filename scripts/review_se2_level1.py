"""R223: from-scratch level-1 cell coverage at r = 13, 17 (P-data of N = r, Q-data of F = r), checking the §3.4 remarks
'at r = 13 all non-residue cells are covered at level 1' and 'at r = 17 two of eight cells survive level 1'."""
import sys
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from review_se2_identities import P_data, Q_data, legendre
for r in (13, 17, 19, 23, 29, 31, 37, 41, 43, 47):
    cov = set()
    for (a, b, c, d, e) in P_data(r):
        if c % r and d % r and a % r and b % r:
            cov |= {(-(4 * a * c * d - 1)) % r, (-(4 * b * c * d - 1)) % r}
    for (a, b, c, d, e, f) in Q_data(r):
        if e % r and c % r:
            cov |= {(-4 * a * a * d) % r, (-4 * b * b * d) % r}
    nr = [u for u in range(1, r) if legendre(u, r) == -1]
    print(f"r={r}: non-residue cells {len(nr)}, covered at level 1: {sorted(set(nr) & cov)}, survivors {sorted(set(nr) - cov)}")
