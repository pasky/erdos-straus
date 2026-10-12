"""Stats for bs_cubic_fclass output: class means mod 840 (square classes vs rest), dispersion."""
import sys, numpy as np
from math import log
d = np.loadtxt(sys.argv[1], dtype=np.int64)
p, r, fI, fII = d.T; f = fI + fII
L3 = np.log(p.astype(float))**3
sq = np.isin(r, [1, 121, 169, 289, 361, 529])
def leg(a, q): return pow(int(a), (q-1)//2, q)
# number of l in {3,5,7} with (p/l)=1, and p mod 8 == 1
qr = np.array([sum(leg(x % l, l) == 1 for l in (3, 5, 7)) + (x % 8 == 1) for x in p])
print(f"primes {p.min()}..{p.max()}: n={len(p)}, mean f/log^3p = {np.mean(f/L3):.4f}, min = {np.min(f/L3):.4f}")
for name, arr in [("f", f), ("fI", fI), ("fII", fII)]:
    a = arr/L3
    print(f"  {name}: square classes mean {a[sq].mean():.4f} (n={sq.sum()}), others {a[~sq].mean():.4f};"
          f" ratio {a[~sq].mean()/a[sq].mean():.2f}")
for k in range(5):
    m = qr == k
    if m.sum(): print(f"  #QR-conditions={k}: n={m.sum()}, mean f/log^3 {np.mean(f[m]/L3[m]):.4f}, min {np.min(f[m]/L3[m]):.4f},"
                      f" var/mean of f {f[m].var()/f[m].mean():.1f}")
# per-class means
cls = {}
for x, y in zip(r, f/L3): cls.setdefault(x, []).append(y)
cm = sorted((np.mean(v), c) for c, v in cls.items() if len(v) >= 8)
print("  lowest class means:", [(c, round(m, 4)) for m, c in cm[:6]], " highest:", [(c, round(m, 4)) for m, c in cm[-3:]])
