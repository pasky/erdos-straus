"""m13e_density.py — box mass near x** per ES level (13E §4).
C_k = {x : x_11 = u11 mod 11^k, x_13 = u13 mod 13^k}.  For every distinct box (fam, M_T, r) (first level N at
which it appears), mu_k = |box ∩ C_k| / |C_k| (0 if incompatible).  Prints per level: #boxes meeting C_k, their mass
S_k(N) = sum mu_k, and the union U_k of C_k covered by boxes with M_T | 11^K 13^K (exact, at resolution K).
usage: m13e_density.py rundir k K [u11 u13]"""
import glob, pickle, sys
import numpy as np
from fractions import Fraction
from m13e_boxtest import v

d, k, K = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
u = (Fraction(sys.argv[4]) if len(sys.argv) > 4 else Fraction(2), Fraction(sys.argv[5]) if len(sys.argv) > 5 else Fraction(15))
Q = {11: 11 ** K, 13: 13 ** K}
ur = {q: u[i].numerator * pow(u[i].denominator, -1, Q[q]) % Q[q] for i, q in enumerate((11, 13))}
first = {}
for fn in glob.glob(d + '/inv_*.pkl'):
    D = pickle.load(open(fn, 'rb'))
    for key in D['boxes']:
        if key not in first or D['N'] < first[key]:
            first[key] = D['N']
# subcells of C_k at resolution K: x_11 = ur11 + 11^k i (i < 11^{K-k}), x_13 = ur13 + 13^k j
n11, n13 = 11 ** (K - k), 13 ** (K - k)
cov = np.zeros((n11, n13), dtype=bool)
byN = {}
for (fam, MT, r), N in first.items():
    if MT == 1:
        continue
    mu, sl = 1.0, []
    for q, n in ((11, n11), (13, n13)):
        a = v(MT, q); qk = q ** min(a, k)
        if (r - ur[q]) % qk:
            mu = 0; break
        mu /= q ** max(0, a - k)
        if a > K:
            sl = None
        elif sl is not None:
            # indices i with ur + q^k i = r mod q^a, i.e. i = (r-ur)/q^k mod q^{a-k}
            if a <= k:
                sl.append(slice(None))
            else:
                st = ((r - ur[q]) // q ** k) % q ** (a - k)
                sl.append(slice(st, None, q ** (a - k)))
    if mu == 0:
        continue
    b = byN.setdefault(N, [0, 0.0, 0]); b[0] += 1; b[1] += mu
    if sl is not None:
        cov[sl[0], sl[1]] = True
    else:
        b[2] += 1
print(f'C_{k} around ({u[0]},{u[1]}), union at resolution {K}; levels {len(set(first.values()))}, boxes {len(first)}')
tot = 0.0
for N in sorted(byN):
    tot += byN[N][1]
    print(f'N={N:>12} meet={byN[N][0]:>6} mass={byN[N][1]:.3e} (cum {tot:.3e}) finer_than_K={byN[N][2]}')
print(f'union covered fraction of C_{k} (boxes with M_T | 11^{K}13^{K}): {cov.mean():.6f}; x** subcell covered: {cov[0,0]}')
