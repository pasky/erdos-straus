"""O25 (review R25, M1): periodic version of the `med` LP of interfreq2_flatF.py.
On Z/Q' (Q' a multiple of lcm(1..N/2)): maximise s subject to
  F <= lambda_N;  F(b mod d) = M/d for d | Q', d <= N/2;
  d | Q', d > C N:  F(s) >= M/d + s (s meets [1,N]),  F(s) >= M/d - 1 + s (misses);
  med (N/2 < d <= N, d | Q'): right-signed sign conditions with margin 0:
       c = u: F(s) >= M/d ;  c = l: F(s) <= M/d   (d = N: equality).
Any F on Z satisfying the Z-version projects to a feasible point here, so
max s <= 0 here is a rigorous (up to floating point) obstruction on Z, and
by Farkas its certificate is a Q'-periodic combination nu >= 0 on all of Z.
Usage: python interfreq2_med_periodic.py N Qprime t C [nomed|medall]
  medall: sign conditions (margin 0) on all of (N/2, CN], not only (N/2, N]"""
import sys
import numpy as np
import scipy.sparse as sp
from scipy.optimize import linprog
from sympy import divisors

N, Qp, t, C = int(sys.argv[1]), int(sys.argv[2]), float(sys.argv[3]), float(sys.argv[4])
MED = not (len(sys.argv) > 5 and sys.argv[5] == "nomed")
MEDALL = len(sys.argv) > 5 and sys.argv[5] == "medall"
M = t * N
lam = np.zeros(Qp)
for m in range(1, N + 1):
    lam[m % Qp] += 1
nv = Qp + 1
re, ce, beq = [], [], []; ru, cu, vu, bub = [], [], [], []
ke = ku = 0
for d in divisors(Qp):
    u, l = -(-N // d), N // d
    for b in range(d):
        pts = np.arange(b, Qp, d)
        c = lam[pts].sum()
        if 2 * d <= N:
            re += [ke] * len(pts); ce += list(pts); beq.append(M / d); ke += 1
        elif d > C * N:
            rhs = M / d - (0 if c > 0 else 1)
            ru += [ku] * len(pts) + [ku]; cu += list(pts) + [Qp]; vu += [-1.0] * len(pts) + [1.0]
            bub.append(-rhs); ku += 1
        elif MED and (d <= N or MEDALL):
            if c == u:
                ru += [ku] * len(pts); cu += list(pts); vu += [-1.0] * len(pts); bub.append(-M / d); ku += 1
            if c == l:
                ru += [ku] * len(pts); cu += list(pts); vu += [1.0] * len(pts); bub.append(M / d); ku += 1
Aeq = sp.csr_matrix((np.ones(len(re)), (re, ce)), shape=(ke, nv))
Aub = sp.csr_matrix((vu, (ru, cu)), shape=(ku, nv))
bounds = [(None, lam[i]) for i in range(Qp)] + [(None, 1.0)]
cost = np.zeros(nv); cost[-1] = -1
res = linprog(cost, A_ub=Aub, b_ub=bub, A_eq=Aeq, b_eq=beq, bounds=bounds, method="highs")
print(f"N={N} Q'={Qp} t={t} C={C} med={MED}: status={res.status} max s = {(-res.fun if res.status == 0 else float('nan')):.4f}")
