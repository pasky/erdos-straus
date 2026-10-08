"""Coverage of the T-generic target (x_13 non-residue mod 13) at resolution R=11^k*13^k by the union of
engine boxes (inv_*.pkl) and brute-force boxes (mordell_tgen pickle).  usage: m13b_cover.py k rundir [brute.pkl]
Prints the uncovered fraction per cell (x_11 mod 11, x_13 mod 13)."""
import glob, pickle, sys
import numpy as np
from collections import Counter
k = int(sys.argv[1]); R = 11 ** k * 13 ** k
boxes = set()
for fn in glob.glob(sys.argv[2] + '/inv_*.pkl'):
    for (fam, MT, r) in pickle.load(open(fn, 'rb'))['boxes']:
        boxes.add((MT, r))
if len(sys.argv) > 3:
    boxes |= set(pickle.load(open(sys.argv[3], 'rb')).keys())
cov = np.zeros(R, dtype=bool)
used = 0
for MT, r in boxes:
    if MT > 1 and R % MT == 0:
        cov[r % MT::MT] = True
        used += 1
v = np.arange(R)
tgt = (v % 11 != 0) & np.isin(v % 13, [2, 5, 6, 7, 8, 11])
unc = tgt & ~cov
print(f'boxes used {used}/{len(boxes)}; target {tgt.sum()}, uncovered {unc.sum()} ({unc.sum()/tgt.sum():.5f})')
print(sorted(Counter(zip(v[unc] % 11, v[unc] % 13)).items()))
print('x*=2 covered:', bool(cov[2]))
