"""R95: coverage from reviewer's own enumeration pickle (review_m13b_enum.py output).
usage: review_m13b_cover.py pkl k   -> (2,2)-cell uncovered count at 11^k 13^k, and whole target (x_11 unit,
x_13 non-residue mod 13) uncovered cells, using boxes with M_T | 11^k 13^k."""
import sys, pickle
import numpy as np
from collections import Counter
res = pickle.load(open(sys.argv[1], 'rb')); k = int(sys.argv[2]); R = 11**k * 13**k
boxes = {(MT, r) for N, (ns, D) in res.items() for f, P, (M, MT, rs) in D for r in rs if MT > 1 and R % MT == 0}
cov = np.zeros(R, dtype=bool)
for MT, r in boxes: cov[r::MT] = True
v = np.arange(R)
nr13 = [x for x in range(1, 13) if pow(x, 6, 13) == 12]
tgt = (v % 11 != 0) & np.isin(v % 13, nr13)
cell = (v % 11 == 2) & (v % 13 == 2)
unc = tgt & ~cov
print(f'k={k} boxes {len(boxes)}; target uncovered {unc.sum()}/{tgt.sum()}; cells with uncovered points:',
      sorted(Counter(zip((v[unc] % 11).tolist(), (v[unc] % 13).tolist())).items()))
uc = cell & ~cov
print(f' (2,2) cell: uncovered {uc.sum()}/{cell.sum()} = {uc.sum()/cell.sum():.4f}; distinct x11 mod 11^k {len(set((v[uc] % 11**k).tolist()))}, x13 mod 13^k {len(set((v[uc] % 13**k).tolist()))}')
if uc.sum() < 40: print(' survivors (x11 mod 11^k, x13 mod 13^k):', sorted(set(zip((v[uc] % 11**k).tolist(), (v[uc] % 13**k).tolist()))))
