"""R271 from-scratch statistics for HARD_PAIR §2.2/§2.5 (own percentile, Spearman, cell, smooth-cell code).
Input: lines 'p N1 fII m0 ... e0 LI' (column indices given by --cols).  Raw columns were cross-checked against
scripts/review_r271_scores.c on all 11 291 primes in [4e4, 3.1e5] (0 mismatches).
Usage: review_r271_stats.py FILE P0 P1"""
import sys
import numpy as np
from scipy.stats import rankdata

f, P0, P1 = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
D = np.array([list(map(int, l.split())) for l in open(f) if l[0].isdigit()], dtype=np.int64)
p = D[:, 0]
# columns of z34_scores output: p N1 fII m0 Mpts S e0 LI
raw = {'N1': -D[:, 1], 'fII': -D[:, 2], 'm0': D[:, 3], 'S': -D[:, 5],
       'e0': np.where(D[:, 6] == 0, 10**6, D[:, 6]), 'LI': -D[:, 7]}   # oriented: larger = harder
W = 1001
n = len(p)

def pct(x):
    u = np.empty(n)
    for i in range(n):
        lo = min(max(0, i - W // 2), n - W); w = x[lo:lo + W]
        u[i] = ((w < x[i]).sum() + 0.5 * ((w == x[i]).sum() - 1)) / (W - 1)
    return u

U = {k: pct(v) for k, v in raw.items()}
sel = (p >= P0) & (p <= P1)
names = list(U)
print('n =', sel.sum(), 'range', P0, P1)
print('Spearman of u:')
for i, a in enumerate(names):
    print(a, ' '.join(f'{np.corrcoef(rankdata(U[a][sel]), rankdata(U[b][sel]))[0, 1]:.2f}' for b in names[i + 1:]))

# profile cell: chi_p(l), l = 3,5,7,11,13 and p mod 8; size blocks of 5000 primes
def chi(l): return np.where(np.array([pow(int(x), (l - 1) // 2, l) for x in p]) == 1, 1, 0)
cell = sum(chi(l) << i for i, l in enumerate([3, 5, 7, 11, 13])) + ((p % 8 == 1).astype(int) << 5)
block = np.arange(n) // 5000
key = block * 64 + cell
R = {}
for k in names:
    r = U[k].copy()
    for c in np.unique(key[sel]):
        m = sel & (key == c); r[m] = U[k][m] - U[k][m].mean()
    R[k] = r
    print('var share', k, round(1 - R[k][sel].var() / U[k][sel].var(), 2))
print('residual Spearman N1-fII %.2f fII-S %.2f N1-S %.2f m0-e0 %.2f' % tuple(
    np.corrcoef(rankdata(R[a][sel]), rankdata(R[b][sel]))[0, 1] for a, b in [('N1', 'fII'), ('fII', 'S'), ('N1', 'S'), ('m0', 'e0')]))

# smooth p - 1 and joint top-5 % rates (controls: non-smooth primes in same range; u is already size-normalised)
def smooth(x, B):
    x = int(x)
    for l in [2, 3, 5, 7, 11, 13][:[2, 3, 5, 7, 11, 13].index(B) + 1]:
        while x % l == 0: x //= l
    return x == 1
for B in (11, 13):
    sm = np.array([smooth(x - 1, B) for x in p]) & sel
    ct = (~np.array([smooth(x - 1, B) for x in p])) & sel
    out = [f'{B}-smooth n={sm.sum()}']
    for a in names[:5]:
        out.append(f'mean u {a} {U[a][sm].mean():.2f}/{U[a][ct].mean():.2f}')
    for a, b in [('N1', 'S'), ('N1', 'm0'), ('m0', 'e0')]:
        r1 = ((U[a] >= .95) & (U[b] >= .95))[sm].mean(); r0 = ((U[a] >= .95) & (U[b] >= .95))[ct].mean()
        out.append(f'joint {a}&{b} {100*r1:.1f}% vs {100*r0:.2f}% (x{r1/r0:.1f})')
    print('; '.join(out))
