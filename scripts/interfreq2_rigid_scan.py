"""O25: scan for rigid-null sparse classes b mod e (max over 𝔐(e) of mu(b mod e) = 0),
e in (N, Cmax*N], e | lcm(1..N/2).  A rigid-null class is counted exactly (as 0) by a
hybrid using only moduli dividing e (Example 3.2 mechanism).
Usage: python interfreq2_rigid_scan.py N Cmax"""
import sys
import numpy as np
from math import gcd
from scipy.optimize import linprog
sys.path.insert(0, 'scripts')
from interfreq2_rigid_points import system


def lcm_upto(m):
    L = 1
    for k in range(1, m + 1):
        L = L * k // gcd(L, k)
    return L


N = int(sys.argv[1]); C = float(sys.argv[2])
L0 = lcm_upto(N // 2)
tot_null_density = 0.0
for e in range(N + 1, int(C * N) + 1):
    if L0 % e:
        continue
    lam, Aeq, beq, Aub, bub = system(N, e)
    nulls = []
    for b in range(e):
        if lam[b] > 0:
            continue
        c = np.zeros(e); c[b] = -1
        res = linprog(c, A_ub=Aub, b_ub=bub, A_eq=Aeq, b_eq=beq, bounds=[(0, None)] * e, method="highs")
        if -res.fun < 1e-9:
            nulls.append(b)
    if nulls:
        tot_null_density += len(nulls) / e
    print(f"N={N} e={e}: sparse={e - N} rigid-null={nulls}", flush=True)
print(f"sum over e of (#null/e) = {tot_null_density:.4f}")
