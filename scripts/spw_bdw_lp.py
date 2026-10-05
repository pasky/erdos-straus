"""O40: bounded-density pseudo-window (BDW) LP on Z/L0, L0 = lcm(1..D), D = N//2.

y(x) = rho(x) * L0 / N  (relative density w.r.t. uniform);  y >= 0,
profile:  sum_{x = b (d)} y(x) = c(b,d) * L0 / N   for all d <= D, b mod d.
mode 'max': minimise A = max y.   (A <= C - ... gives SPW(C, 1 - A/C) via Lemma 1.1)
usage: spw_bdw_lp.py N
"""
import sys
from math import gcd
import numpy as np
from scipy.optimize import linprog
from scipy.sparse import coo_matrix, vstack, hstack, identity, csr_matrix

def cnt(b, d, N):
    b %= d
    first = b if b >= 1 else d
    return 0 if first > N else (N - first) // d + 1

def main(N):
    D = N // 2
    L0 = 1
    for d in range(1, D + 1):
        L0 = L0 * d // gcd(L0, d)
    x = np.arange(L0)
    rows, cols, beq = [], [], []
    r = 0
    # only maximal-in-divisibility d are needed, but include all d (redundant rows are fine)
    maximal = [d for d in range(1, D + 1) if not any(m % d == 0 for m in range(d + 1, D + 1))]
    for d in maximal:
        res = x % d
        rows.append(res + r); cols.append(x)
        beq += [cnt(b, d, N) * L0 / N for b in range(d)]
        r += d
    rows = np.concatenate(rows); cols = np.concatenate(cols)
    Aeq = coo_matrix((np.ones(len(rows)), (rows, cols)), shape=(r, L0 + 1)).tocsr()
    # y(x) - A <= 0
    Aub = hstack([identity(L0, format="csr"), -np.ones((L0, 1))], format="csr")
    c = np.zeros(L0 + 1); c[-1] = 1
    res = linprog(c, A_ub=Aub, b_ub=np.zeros(L0), A_eq=Aeq, b_eq=np.array(beq),
                  bounds=[(0, None)] * (L0 + 1), method="highs")
    assert res.status == 0, res.message
    y = res.x[:L0]
    print(f"N={N} D={D} L0={L0} #maximal d={len(maximal)}: min max-density A={res.fun:.4f}  "
          f"(min y={y.min():.3f}; frac of y>0: {(y>1e-9).mean():.3f})", flush=True)
    return y

if __name__ == "__main__":
    for N in map(int, sys.argv[1:]):
        main(N)
