"""z52d audit A3, item Z1142: random-matrix baseline for the family-prime incidence matrix.
Families = levels C=1..NC ((★) line with t=4C): A[C,p]=1 iff 4Cp+1 has a divisor d=-1 (mod 4C), 4C-1<=d<=sqrt.
Columns = primes p=1 (4) from P0 on.  Compare singular values of A with (a) degree-preserving shuffles (curveball),
(b) curveball within column strata of equal p mod M (preserves per-stratum row sums), M = 840 and M = 9240."""
import sys, numpy as np
from sympy import factorint, nextprime
from math import isqrt

NC = int(sys.argv[1]) if len(sys.argv) > 1 else 40
NP = int(sys.argv[2]) if len(sys.argv) > 2 else 3000
P0 = int(sys.argv[3]) if len(sys.argv) > 3 else 10**6
rng = np.random.default_rng(1)

def hit(C, p):
    t = 4 * C; N = t * p + 1; r = isqrt(N)
    ds = [1]
    for q, e in factorint(N).items():
        ds = [d * q**i for d in ds for i in range(e + 1)]
    return any(d % t == t - 1 and d <= r for d in ds)

ps = []
p = P0
while len(ps) < NP:
    p = nextprime(p)
    if p % 4 == 1: ps.append(p)
A = np.array([[1 if hit(C, p) else 0 for p in ps] for C in range(1, NC + 1)], dtype=np.int8)
np.save(f"data/z52d/audit/A3/z1142_A_{NC}_{NP}_{P0}.npy", A)
ps = np.array(ps)

def sv(M):
    return np.linalg.svd(M.astype(float), compute_uv=False)

def curveball(M, iters, strata=None):
    M = M.copy().astype(bool)
    nr = M.shape[0]
    cols_list = [np.arange(M.shape[1])] if strata is None else strata
    for _ in range(iters):
        cols = cols_list[rng.integers(len(cols_list))]
        i, j = rng.choice(nr, 2, replace=False)
        a = M[i, cols]; b = M[j, cols]
        diff = np.nonzero(a ^ b)[0]
        if len(diff) < 2: continue
        k = int(a[diff].sum())
        perm = rng.permutation(len(diff))
        newa = np.zeros(len(diff), bool); newa[perm[:k]] = True
        a2 = a.copy(); b2 = b.copy()
        a2[diff] = newa; b2[diff] = ~newa
        M[i, cols] = a2; M[j, cols] = b2
    return M

s0 = sv(A)
print(f"NC={NC} NP={NP} P0={P0} density={A.mean():.4f} rowsums min/max={A.sum(1).min()}/{A.sum(1).max()} colsum0={int((A.sum(0)==0).sum())}")
print("actual top-6 sv:", np.round(s0[:6], 2))
for name, strata in [("global", None),
                     ("strat mod 840", [np.nonzero(ps % 840 == r)[0] for r in np.unique(ps % 840)]),
                     ("strat mod 9240", [np.nonzero(ps % 9240 == r)[0] for r in np.unique(ps % 9240)])]:
    S = []
    for rep in range(20):
        M = curveball(A, 4000 if strata is None else 20000, strata)
        S.append(sv(M)[:6])
    S = np.array(S)
    z = (s0[:6] - S.mean(0)) / (S.std(0) + 1e-9)
    print(f"{name:16s} null mean sv:", np.round(S.mean(0), 2), " z:", np.round(z, 1))
