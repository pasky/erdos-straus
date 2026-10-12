"""O151 brainstorm: does the ES solution count f(p) follow an Euler-product (L(1,chi)-type) law?

Reads spec_typecount.c output arrays (<prefix>.FI.bin, <prefix>.FII.bin, uint32 indexed by n)
and, for primes p in [lo, hi], compares g(p) = f(p)/log^3 p with
   L_Y(p) = prod_{3 <= q <= Y, q prime} (1 - (p/q)/q)^{-1}   (Legendre symbols of p mod q)
and with the 'square depth' s(p) = least odd prime q with (p/q) = -1.
usage: bs_anal_lfun_corr.py prefix lo hi [Y]
"""
import sys
import numpy as np
from sympy import primerange

pre, lo, hi = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
Y = int(sys.argv[4]) if len(sys.argv) > 4 else 1000
FI = np.fromfile(pre + ".FI.bin", dtype=np.uint32)
FII = np.fromfile(pre + ".FII.bin", dtype=np.uint32)
P = np.array(list(primerange(max(lo, 11), hi + 1)), dtype=np.int64)
L3 = np.log(P.astype(float)) ** 3
qs = list(primerange(3, Y + 1))
logL = np.zeros(len(P))
depth = np.full(len(P), 10**9, dtype=np.int64)
leg = {}
for q in qs:
    sq = np.zeros(q, dtype=np.int8) - 1
    sq[(np.arange(1, q) ** 2) % q] = 1
    sq[0] = 0
    chi = sq[P % q].astype(float)
    leg[q] = chi
    logL -= np.log1p(-chi / q)
    newd = (chi == -1) & (depth == 10**9)
    depth[newd] = q
res = {"I": FI[P] / L3, "II": FII[P] / L3}
mod8 = P % 8
print(f"primes {len(P)} in [{lo},{hi}], Y={Y}")
for name, g in res.items():
    lg = np.log(np.maximum(g, 1e-9))
    pos = g > 0
    c = np.corrcoef(lg[pos], logL[pos])[0, 1]
    # fit log g = A + beta*logL within each class mod 8
    out = []
    for r in (1, 3, 5, 7):
        m = pos & (mod8 == r)
        b, a = np.polyfit(logL[m], lg[m], 1)
        rr = lg[m] - (a + b * logL[m])
        out.append(f"mod8={r}: beta={b:+.3f} R2={1 - rr.var() / lg[m].var():.3f} n={m.sum()}")
    print(f"f_{name}: mean g={g.mean():.4f} min g={g.min():.4f} corr(log g, log L_Y)={c:+.3f}")
    for o in out:
        print("   ", o)
    # dependence on square depth
    print("    depth s(p): mean g, min g, count")
    for s in [3, 5, 7, 11, 13, 17, 19, 23, 29, 31]:
        m = depth == s
        if m.sum():
            print(f"      s={s:3d}: {g[m].mean():.4f} {g[m].min():.4f} {m.sum()}")
    m = depth > 31
    if m.sum():
        print(f"      s>31 : {g[m].mean():.4f} {g[m].min():.4f} {m.sum()}")
    # how much variance do the first K Legendre symbols explain (linear regression on chi(q), q<=Q)?
    for Q in (13, 50, 200):
        X = np.column_stack([np.ones(len(P))] + [(mod8 == r).astype(float) for r in (3, 5, 7)]
                            + [leg[q] for q in qs if q <= Q])
        coef, *_ = np.linalg.lstsq(X[pos], lg[pos], rcond=None)
        rr = lg[pos] - X[pos] @ coef
        print(f"    R2 of log g on mod8 + chi(q), q<={Q}: {1 - rr.var() / lg[pos].var():.3f}")
    # residual dispersion vs Poisson: var(log f | local data) vs mean(1/f)
    X = np.column_stack([np.ones(len(P))] + [(mod8 == r).astype(float) for r in (3, 5, 7)]
                        + [leg[q] for q in qs if q <= 50])
    f = (FI if name == "I" else FII)[P].astype(float)
    m = f > 0
    lf = np.log(f[m]) - np.log(L3[m])
    coef, *_ = np.linalg.lstsq(X[m], lf, rcond=None)
    rr = lf - X[m] @ coef
    print(f"    residual var(log f)={rr.var():.4f}  Poisson prediction mean(1/f)={np.mean(1 / f[m]):.4f}"
          f"  overdispersion={rr.var() / np.mean(1 / f[m]):.2f}  mean f={f.mean():.1f}")
