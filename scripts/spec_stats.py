"""O123 step (1): statistics of exact Type I / II counts (output of spec_typecount.c).
f_I(p), f_II(p) count solutions with y <= z (each unordered pair {y,z} once)."""
import sys, math, numpy as np
from sympy import primerange
pre = sys.argv[1]; N = int(sys.argv[2])
FI = np.fromfile(pre + ".FI.bin", dtype=np.uint32)
FI1 = np.fromfile(pre + ".FI1.bin", dtype=np.uint32)
FII = np.fromfile(pre + ".FII.bin", dtype=np.uint32)
sieve = np.ones(N + 1, bool); sieve[:2] = False
for i in range(2, int(N ** .5) + 1):
    if sieve[i]: sieve[i*i::i] = False
P = np.nonzero(sieve)[0]
P = P[P > 2]
fi, fi1, fii = FI[P], FI1[P], FII[P]
print("primes 3..N:", len(P))
print("f_I(p)=0:", int((fi == 0).sum()), " f_II(p)=0:", int((fii == 0).sum()),
      " both 0:", int(((fi == 0) & (fii == 0)).sum()), " a=1 part 0 (p=1 mod 4):", int(((fi1 == 0) & (P % 4 == 1)).sum()))
z2 = P[fii == 0]; print("first primes with f_II=0:", z2[:20].tolist())
from collections import Counter
print("classes mod 840 of p with f_II=0 (top):", Counter((z2 % 840).tolist()).most_common(12))
z1 = P[(fi1 == 0) & (P % 4 == 1)]; print("p=1(4) with no a=1 Type I sol:", len(z1), z1[:20].tolist())
mh = np.isin(P % 840, [1, 121, 169, 289, 361, 529])
print("\n dyadic windows [X,2X): min f_I (argmin), mean f_I, mean/log^2 p, min over Mordell-hard, min f_II, min f_I+f_II")
X = 16
while 2 * X <= N + 1:
    m = (P >= X) & (P < 2 * X)
    if m.sum():
        q = P[m]; a = fi[m]; L = math.log(X * 1.5)
        mm = m & mh
        print(f"X=2^{int(math.log2(X)):2d} n={m.sum():8d} minI={a.min():4d} @{q[a.argmin()]:10d} meanI={a.mean():8.2f} "
              f"mean/L^2={a.mean()/L**2:.3f} min/L={a.min()/L:.2f} minI_MH={fi[mm].min() if mm.sum() else -1:4d} "
              f"minII={fii[m].min():3d} min(I+II)={(a+fii[m]).min():4d} minI1(p=1mod4)={fi1[m & (P%4==1)].min():3d}")
    X *= 2
