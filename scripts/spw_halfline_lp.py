"""O40: LP for the half-line (single-edge) problem.

H >= 0 on [lo, hi]; for every d <= D: sum_{x = b mod d} H(x) = {-b/d} + k_d  (k_d free >= 0);
mass(H) <= mu*D; minimise h s.t. H(s) <= h for every class s mod e, e > E0 (pointwise beyond support length).
usage: spw_halfline_lp.py D E0 lo hi mu
"""
import sys
from fractions import Fraction
import numpy as np
from scipy.optimize import linprog
from scipy.sparse import coo_matrix

def main(D, E0, lo, hi, mu):
    pts = np.arange(lo, hi + 1); P = len(pts)
    nd = D  # k_d variables for d=1..D ; then h
    nv = P + nd + 1
    er, ec, ev, beq = [], [], [], []
    row = 0
    for d in range(1, D + 1):
        res = np.mod(pts, d)
        for b in range(d):
            idx = np.nonzero(res == b)[0]
            er += [row] * len(idx); ec += list(idx); ev += [1.0] * len(idx)
            er.append(row); ec.append(P + d - 1); ev.append(-1.0)
            beq.append(((-b) % d) / d); row += 1
    Aeq = coo_matrix((ev, (er, ec)), shape=(row, nv)).tocsr()
    ur, uc, uv, bub = [], [], [], []
    row = 0
    for e in range(E0 + 1, P):
        res = np.mod(pts, e)
        order = np.argsort(res, kind="stable"); rs = res[order]
        starts = np.r_[0, np.nonzero(np.diff(rs))[0] + 1]; ends = np.r_[starts[1:], len(rs)]
        for s, t in zip(starts, ends):
            ur += [row] * (t - s); uc += list(order[s:t]); uv += [1.0] * (t - s)
            ur.append(row); uc.append(nv - 1); uv.append(-1.0); bub.append(0.0); row += 1
    for i in range(P):
        ur += [row, row]; uc += [i, nv - 1]; uv += [1.0, -1.0]; bub.append(0.0); row += 1
    ur += [row] * P; uc += list(range(P)); uv += [1.0] * P; bub.append(mu * D); row += 1
    Aub = coo_matrix((uv, (ur, uc)), shape=(row, nv)).tocsr()
    c = np.zeros(nv); c[-1] = 1
    r = linprog(c, A_ub=Aub, b_ub=bub, A_eq=Aeq, b_eq=beq, bounds=[(0, None)] * nv, method="highs")
    if r.status != 0:
        print("status", r.status, r.message); return
    H = r.x[:P]
    print(f"D={D} E0={E0} supp=[{lo},{hi}] mu={mu}: h_min={r.fun:.4f}  mass={H.sum():.3f}  => sigma=1-2h={1-2*r.fun:.4f}")
    return H, pts

if __name__ == "__main__":
    D, E0, lo, hi = map(int, sys.argv[1:5]); mu = float(sys.argv[5])
    main(D, E0, lo, hi, mu)
