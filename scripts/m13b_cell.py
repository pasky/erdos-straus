"""Coverage of the cell x = (2,2) mod (11,13) at resolution 11^k 13^k (boxes with M_T | 11^k 13^k), engine
boxes inv_*.pkl only.  usage: m13b_cell.py k rundir   Prints uncovered count and the projections."""
import glob, pickle, sys
import numpy as np
from math import gcd
from collections import Counter
k = int(sys.argv[1]); R = 11 ** k * 13 ** k; S = R // 143
boxes = set()
for fn in glob.glob(sys.argv[2] + '/inv_*.pkl'):
    for (fam, MT, r) in pickle.load(open(fn, 'rb'))['boxes']:
        if MT > 1 and R % MT == 0:
            boxes.add((MT, r))
cov = np.zeros(S, dtype=bool)
for MT, r in boxes:
    g = gcd(MT, 143)
    if (r - 2) % g:
        continue
    L = MT * 143 // g
    v = next(x for x in range(r % MT, L, MT) if x % 143 == 2)   # CRT lift, v = 2 mod 143
    cov[(v - 2) // 143::L // 143] = True
unc = np.nonzero(~cov)[0] * 143 + 2
print(f'k={k}: boxes {len(boxes)}; cell size {S}, uncovered {len(unc)} ({len(unc)/S:.5f}); x*: {"covered" if cov[0] else "UNCOVERED"}')
p11 = Counter(unc % 11 ** k); p13 = Counter(unc % 13 ** k)
print(f' distinct x_11 mod 11^{k}: {len(p11)} of {11**(k-1)}; distinct x_13 mod 13^{k}: {len(p13)} of {13**(k-1)}; product {len(p11)*len(p13)}')
if len(unc) < 60: print(' uncovered:', [(int(u % 11 ** k), int(u % 13 ** k)) for u in unc])
