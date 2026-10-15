"""O230 SYNTHESIS_SPARKS5 §1: does three-side cleanliness explain the near-square (K0 = p - floor(sqrt p)^2) depletion
of chi = -1 words beyond the adelic cell?  Input: s5_sides output.  Cells as ns_hardness.py (p mod 8, (r/p) r <= RMAX, lnr capped).
Prints within-cell residual means (with naive SE) of N-/N, N-/(N-Nt), N-/(N-Nany) by K0 bin."""
import sys
import numpy as np
from math import isqrt
from sympy import legendre_symbol
rows = np.loadtxt(sys.argv[1], dtype=np.int64)
RMAX = int(sys.argv[2]) if len(sys.argv) > 2 else 31
PP = [int(x) for x in sys.argv[3].split(",")] if len(sys.argv) > 3 else []  # extra prime-power moduli (e.g. 9,16,25)
RS = [r for r in (3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43) if r <= RMAX]
p, N, Nm, Nt, Nuv, Na, q = rows.T
cells = {}
for i, pp in enumerate(p):
    key = (int(pp % 8),) + tuple(legendre_symbol(r, int(pp)) for r in RS) + (min(int(q[i]), max(RS) + 4),) + tuple(int(pp % m) for m in PP)
    cells.setdefault(key, []).append(i)
def within(v):
    out = np.empty_like(v, dtype=float)
    for idx in cells.values():
        idx = np.array(idx); out[idx] = v[idx] - v[idx].mean()
    return out
K0 = np.array([int(x) - isqrt(int(x)) ** 2 for x in p])
ys = {"N-/N": Nm / N, "N-/(N-Nt)": Nm / (N - Nt), "N-/(N-Nany)": Nm / np.maximum(N - Na, 1)}
R = {k: within(v) for k, v in ys.items()}
print(f"primes {len(p)}, cells {len(cells)}; words {N.sum()}, t-clean {Nt.sum()}, u/v-clean {Nuv.sum()}, any {Na.sum()}")
for lo, hi in ((1, 5), (5, 10), (10, 17), (17, 30), (30, 100), (100, 300), (300, 10**9)):
    s = (K0 >= lo) & (K0 < hi)
    print(f"K0 in [{lo},{hi}) n={s.sum():6d} " + "  ".join(f"{k}: {R[k][s].mean():+.4f}±{R[k][s].std()/np.sqrt(s.sum()):.4f}" for k in R)
          + f"  frac_any={ (Na[s]/N[s]).mean():.3f}")
for k0 in (1, 4, 8, 9, 12, 16, 24, 25, 28, 36):
    s = K0 == k0
    if s.sum(): print(f"K0={k0:3d} n={s.sum():4d} " + "  ".join(f"{k}: {R[k][s].mean():+.4f}" for k in R))
