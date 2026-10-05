"""R40 from-scratch BDW LP on Z/L0: min A s.t. rho in [0, A N/L0], window profile
mod every d <= D.  (EVIDENCE check of EXCEPTIONAL_SPW §2 numerics.)"""
import sys
from math import lcm
from functools import reduce
import numpy as np
from scipy.optimize import linprog
from scipy.sparse import coo_matrix, hstack, csr_matrix

for N in [int(a) for a in sys.argv[1:]]:
    D = N // 2
    L0 = reduce(lcm, range(1, D + 1), 1)
    rows, cols, b_eq = [], [], []
    r = 0
    for d in range(2, D + 1):
        for b in range(d):
            xs = list(range(b, L0, d))
            rows += [r] * len(xs); cols += xs
            b_eq.append(sum(1 for n in range(1, N + 1) if n % d == b) * L0 / N)  # y = rho L0/N
            r += 1
    rows += [r] * L0; cols += list(range(L0)); b_eq.append(L0); r += 1
    Aeq = coo_matrix((np.ones(len(rows)), (rows, cols)), shape=(r, L0 + 1)).tocsr()
    # y_x - A <= 0
    Aub = hstack([csr_matrix(np.eye(L0)) if L0 <= 3000 else coo_matrix((np.ones(L0), (range(L0), range(L0))), shape=(L0, L0)),
                  csr_matrix(-np.ones((L0, 1)))]).tocsr()
    obj = np.zeros(L0 + 1); obj[-1] = 1
    res = linprog(obj, A_ub=Aub, b_ub=np.zeros(L0), A_eq=Aeq, b_eq=b_eq,
                  bounds=[(0, None)] * (L0 + 1), method="highs")
    print(f"N={N} L0={L0}: BDW LP A = {res.fun:.6f}   A*(N) = 3/2-3/N = {1.5 - 3 / N:.6f}")
