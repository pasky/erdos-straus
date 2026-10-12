"""O151 brainstorm (b): is the non-concentrating part of f(p) explained by divisor functions of small shifts?

For primes p == 1 (mod 4) in [lo, hi]: regress log(f(p)/log^3 p) on
  (i) local data: p mod 8 and Legendre symbols (p/q), q <= 50;
  (ii) + log tau_3((p+e)/4) for e in {3,7,11,...} (Type II e-slices: (p+e)/4 = abd, e | a+b);
  (iii) + log tau(4p+1), log tau(8p+1), log tau(p+4), ... (low Type II/Type I levels).
usage: bs_anal_shift_tau.py prefix lo hi
"""
import sys
import numpy as np
from sympy import primerange

pre, lo, hi = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
FI = np.fromfile(pre + ".FI.bin", dtype=np.uint32)
FII = np.fromfile(pre + ".FII.bin", dtype=np.uint32)
LIM = 16 * hi + 2
spf = np.zeros(LIM, dtype=np.int32)
for q in primerange(2, int(LIM ** 0.5) + 1):
    blk = spf[q::q]
    blk[blk == 0] = q
idx = np.nonzero(spf == 0)[0]
spf[idx] = idx


def taus(n):
    """(tau(n), tau_3(n)) for an array n of positive ints < LIM."""
    n = n.copy()
    t2 = np.ones(len(n))
    t3 = np.ones(len(n))
    while True:
        act = n > 1
        if not act.any():
            return t2, t3
        q = spf[n[act]]
        k = np.zeros(act.sum())
        m = n[act]
        while True:
            div = (m % q == 0) & (m > 1)
            if not div.any():
                break
            m[div] //= q[div]
            k[div] += 1
        t2[act] *= k + 1
        t3[act] *= (k + 1) * (k + 2) / 2
        n[act] = m


P = np.array([p for p in primerange(max(lo, 11), hi + 1) if p % 4 == 1], dtype=np.int64)
L3 = np.log(P.astype(float)) ** 3
cols = [np.ones(len(P)), (P % 8 == 5).astype(float)]
for q in primerange(3, 51):
    sq = np.zeros(q) - 1
    sq[(np.arange(1, q) ** 2) % q] = 1
    cols.append(sq[P % q])
loc = np.column_stack(cols)
shiftcols, names = [], []
for e in (3, 7, 11, 15, 19, 23, 27, 31):
    t2, t3 = taus((P + e) // 4)
    shiftcols.append(np.log(t3)); names.append(f"t3((p+{e})/4)")
low = []
for (A, B) in ((4, 1), (8, 1), (12, 1), (1, 4), (16, 1), (1, 1)):
    t2, _ = taus(A * P + B)
    low.append(np.log(t2))
for name, F in (("I", FI), ("II", FII)):
    f = F[P].astype(float)
    y = np.log(f / L3)
    def r2(X):
        c, *_ = np.linalg.lstsq(X, y, rcond=None)
        return 1 - (y - X @ c).var() / y.var(), c
    a, _ = r2(loc)
    b, cb = r2(np.column_stack([loc] + shiftcols))
    c, _ = r2(np.column_stack([loc] + low))
    d, _ = r2(np.column_stack([loc] + shiftcols + low))
    print(f"f_{name} (p=1 mod 4, n={len(P)}): var(log g)={y.var():.4f}; R2 local={a:.3f}, +shift tau3={b:.3f},"
          f" +low-level tau={c:.3f}, +both={d:.3f}")
    print("    shift coefficients:", " ".join(f"{n}:{v:+.3f}" for n, v in zip(names, cb[loc.shape[1]:])))
