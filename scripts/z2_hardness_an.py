"""O225: within-cell K0 gradient of chi=-1 word fractions after removing t-clean and u-genus-clean words.
Input: z2_hardness output; RMAX (cell = p mod 8, (r/p) for odd r <= RMAX, lnr capped), as ns_hardness/R225."""
import sys
import numpy as np
from sympy import legendre_symbol
rows = np.loadtxt(sys.argv[1], dtype=np.int64)
RMAX = int(sys.argv[2]) if len(sys.argv) > 2 else 31
RS = [r for r in (3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37) if r <= RMAX]
p, N, Nm, Ncl, Nclm, Nfl, Nflm, K0, q = rows.T
cells = {}
for i, pp in enumerate(p):
    key = (int(pp % 8),) + tuple(legendre_symbol(r, int(pp)) for r in RS) + (min(int(q[i]), max(RS) + 4),)
    cells.setdefault(key, []).append(i)
def within(v):
    out = np.empty_like(v, dtype=float)
    for idx in cells.values():
        idx = np.array(idx); out[idx] = v[idx] - v[idx].mean()
    return out
ys = {'N-/N': Nm / N, 'N-/(N-Ncl)': Nm / (N - Ncl), 'N-/(N-Ncl-Nfl)': Nm / (N - Ncl - Nfl)}
res = {k: within(v) for k, v in ys.items()}
fl = within(Nfl / N)
bins = [(1, 2), (2, 5), (5, 10), (10, 17), (17, 30), (30, 100), (100, 300), (300, 10**9)]
print('cells', len(cells), 'primes', len(p), '| mean flagged-beyond-clean fraction', (Nfl / N).mean().round(4))
print('K0 bin      n   ' + '   '.join(f'{k:>16}' for k in ys) + '   resid(Nfl/N)')
for lo, hi in bins:
    s = (K0 >= lo) & (K0 < hi)
    line = f'[{lo},{hi})'.ljust(12) + f'{s.sum():5d} '
    for k in ys:
        r = res[k][s]; line += f'   {r.mean():+.4f}±{r.std() / np.sqrt(max(s.sum(), 1)):.4f}'
    line += f'   {fl[s].mean():+.4f}'
    print(line)
for K in (24, 16, 4, 9, 1, 25, 36):
    s = K0 == K
    print(f'K0={K:3d} n={s.sum():4d} ' + '  '.join(f'{k}: {res[k][s].mean():+.4f}' for k in ys))
