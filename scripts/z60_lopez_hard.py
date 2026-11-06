"""z60 LOPEZ: hardest primes (by U_II index min(B,A) in each coordinate) with both branches' least witnesses,
plus the joint 2-D histogram of (aB, aA) (capped at 40). Input: output of z60_lopez_joint.c.
Usage: python z60_lopez_hard.py file outprefix"""
import sys, numpy as np
d = np.loadtxt(sys.argv[1], dtype=np.int64); out = sys.argv[2]
INF = 10**12; X = d.copy(); X[X == 0] = INF; p = X[:, 0]
inM = np.isin(p % 840, [1, 121, 169, 289, 361, 529])
with open(out + "_hardest.txt", "w") as fo:
    fo.write("# columns: p aB aA fB fA CB cA inM  (0 = none within bounds AMAX=3000, FMAX=20000, TMAX=3000)\n")
    for col, nm in ((1, 'a'), (3, 'f'), (5, 'T')):
        U = np.minimum(X[:, col], X[:, col + 1])
        for sel, sn in ((np.ones(len(p), bool), 'all p ≡ 1 (24)'), (inM, 'p in M')):
            idx = np.where(sel)[0]; top = idx[np.argsort(-U[idx], kind='stable')[:15]]
            fo.write(f"## top 15 by U-index in coordinate {nm} ({sn})\n")
            for i in top: fo.write(" ".join(map(str, d[i])) + f" {int(inM[i])}\n")
H = np.zeros((41, 41), dtype=np.int64)
a = np.minimum(X[:, 1], 40); b = np.minimum(X[:, 2], 40)
np.add.at(H, (a, b), 1)
np.savetxt(out + "_hist_aB_aA.txt", H, fmt="%d", header="H[i][j] = #primes p ≡ 1 (24) <= 1e9 with min(aB,40)=i, min(aA,40)=j (40 = >=40 or none)")
print(open(out + "_hardest.txt").read())
