"""Coverage of the T={11,13}-generic target (x_13 non-square; main variant) by box pickles.
usage: mordell_cellcov.py k pkl1 [pkl2 ...] -- resolution 11^k 13^k; boxes with v_q(F)<=k."""
import sys, pickle
import numpy as np
k = int(sys.argv[1])
boxes = {}
for f in [a for a in sys.argv[2:] if not a.startswith("--")]:
    boxes.update(pickle.load(open(f, 'rb')))
R1, R2 = 11 ** k, 13 ** k
R = R1 * R2
v = np.arange(R, dtype=np.int64)
ok = (v % 11 != 0) & (v % 13 != 0)
sq13 = np.zeros(13, bool); sq13[[(i * i) % 13 for i in range(1, 13)]] = True
ok &= ~sq13[v % 13]
cov = np.zeros(R, bool)
nb = 0
for (F, res) in boxes:
    if R % F:
        continue
    nb += 1
    cov |= (v % F == res)
tgt = ok.sum(); unc = (ok & ~cov)
print(f"k={k} boxes used {nb}, target {tgt}, uncovered {unc.sum()} ({unc.sum()/tgt:.5f})")
from collections import Counter
print(Counter(zip((v[unc] % 11).tolist(), (v[unc] % 13).tolist())))
c22 = ok & (v % 11 == 2) & (v % 13 == 2)
print(f"(2,2) cell: {c22.sum()} subcells, uncovered {(c22 & ~cov).sum()} ({(c22 & ~cov).sum()/c22.sum():.4f})")
if '--struct' in sys.argv or True:
    U = v[ok & ~cov & (v % 11 == 2) & (v % 13 == 2)]
    A = sorted(set((U % R1).tolist())); B = sorted(set((U % R2).tolist()))
    print("proj 11:", len(A), "of", R1 // 11, " proj 13:", len(B), "of", R2 // 13, " product?", len(A) * len(B) == len(U))
    print("11-digits:", sorted(set(((a - 2) // 11) % 11 for a in A)), sorted(set(((a - 2) // 121) for a in A))[:20])
    print("13-digits:", sorted(set(((b - 2) // 13) % 13 for b in B)))
