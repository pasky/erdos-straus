"""z60 LOPEZ: statistics of joint least witnesses (output of z60_lopez_joint.c).
Columns: p aB aA fB fA CB cA (0 = none within bound -> treated as +inf).
Usage: python z60_lopez_jointstats.py file [inM_only 0/1]"""
import sys, numpy as np
d = np.loadtxt(sys.argv[1], dtype=np.int64)
if len(sys.argv) > 2 and sys.argv[2] == '1':
    r = d[:, 0] % 840; d = d[np.isin(r, [1, 121, 169, 289, 361, 529])]
INF = 10**12
X = d.copy(); X[X == 0] = INF
p = X[:, 0]; N = len(p)
print("N primes", N, "range", p.min(), p.max())
names = {1: 'a', 3: 'f', 5: 'T'}
for col, nm in names.items():
    B = X[:, col]; A = X[:, col + 1]; U = np.minimum(A, B)
    print(f"\n== coordinate {nm}: branch B col {col}, branch A col {col+1}")
    print(" max finite B", B[B < INF].max(), " max finite A", A[A < INF].max(), " max U", U.max(), "at p =", p[U.argmax()])
    print(" #B=inf", (B == INF).sum(), " #A=inf", (A == INF).sum(), " #both", ((A == INF) & (B == INF)).sum())
    print(" Pearson corr of log indices (finite both):", np.corrcoef(np.log(A[(A < INF) & (B < INF)]), np.log(B[(A < INF) & (B < INF)]))[0, 1].round(3))
    qs = sorted(set(np.quantile(U, [0.5, 0.9, 0.99, 0.999]).astype(int)))
    thr = sorted(set([int(np.quantile(B, q)) for q in (0.5, 0.75, 0.9, 0.97, 0.99, 0.997, 0.999)]))
    print(" X       P(B>X)     P(A>X)     P(both>X)   ratio=P(both)/P(A)P(B)")
    for x in thr:
        pb = (B > x).mean(); pa = (A > x).mean(); pab = ((A > x) & (B > x)).mean()
        print(f" {x:7d} {pb:.3e} {pa:.3e} {pab:.3e} {pab/(pa*pb) if pa*pb>0 else float('nan'):.3f}")
