"""O151 (c): Euler-product (Erdos-Wintner / L(1,chi)) model for f(p)/log^3 p.

Within p == 1 (mod 8): regress log g on chi(q) = (p/q) for odd q <= 61 and print q*coef_q
(an Euler-product law log g ~ -beta*log L(1,chi) predicts q*coef_q ~ -beta for all q);
and the mean g by square depth s(p) (least odd prime q with (p/q) = -1).
usage: bs_anal_euler_profile.py prefix lo hi
"""
import sys
import numpy as np
from sympy import primerange

pre, lo, hi = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
for name in ("FI", "FII"):
    F = np.fromfile(f"{pre}.{name}.bin", dtype=np.uint32)
    P = np.array([p for p in primerange(lo, hi + 1) if p % 8 == 1], dtype=np.int64)
    g = F[P] / np.log(P.astype(float)) ** 3
    y = np.log(g)
    qs = list(primerange(3, 62))
    chis, depth = [], np.full(len(P), 999)
    for q in qs:
        sq = np.zeros(q) - 1
        sq[(np.arange(1, q) ** 2) % q] = 1
        c = sq[P % q]
        chis.append(c)
        depth[(c == -1) & (depth == 999)] = q
    X = np.column_stack([np.ones(len(P))] + chis)
    coef, *_ = np.linalg.lstsq(X, y, rcond=None)
    print(f"{name}, p=1 mod 8 in [{lo},{hi}], n={len(P)}")
    print("   q*coef_q:", " ".join(f"{q}:{q * c:+.2f}" for q, c in zip(qs, coef[1:])))
    print("   mean g by depth:", " ".join(f"s={s}:{g[depth == s].mean():.4f}({(depth == s).sum()})"
                                     for s in (3, 5, 7, 11, 13, 17, 19, 23) if (depth == s).any()),
          f"s>23:{g[depth > 23].mean():.4f}({(depth > 23).sum()})")
