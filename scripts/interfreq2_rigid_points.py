"""O25: per-point max of mu(x) over the hybrid dual set 𝔐(Q') (see interfreq2_rigid.py).
Usage: python interfreq2_rigid_points.py N Qprime  -> prints the rigid-null points (max mu(x) = 0)
and summary counts."""
import sys
import numpy as np
import scipy.sparse as sp
from scipy.optimize import linprog
from sympy import divisors


def system(N, Qp):
    lam = np.zeros(Qp)
    for m in range(1, N + 1):
        lam[m % Qp] += 1
    r_e, c_e, beq = [], [], []
    r_u, c_u, v_u, bub = [], [], [], []
    ke = ku = 0
    for d in divisors(Qp):
        u, l = -(-N // d), N // d
        for b in range(d):
            pts = np.arange(b, Qp, d)
            if 2 * d <= N:
                r_e.append(np.full(len(pts), ke)); c_e.append(pts); beq.append(lam[pts].sum()); ke += 1
            else:
                r_u.append(np.full(len(pts), ku)); c_u.append(pts); v_u.append(np.ones(len(pts))); bub.append(u); ku += 1
                if l > 0:
                    r_u.append(np.full(len(pts), ku)); c_u.append(pts); v_u.append(-np.ones(len(pts))); bub.append(-l); ku += 1
    Aeq = sp.csr_matrix((np.ones(sum(len(x) for x in c_e)), (np.concatenate(r_e), np.concatenate(c_e))), shape=(ke, Qp))
    Aub = sp.csr_matrix((np.concatenate(v_u), (np.concatenate(r_u), np.concatenate(c_u))), shape=(ku, Qp))
    return lam, Aeq, np.array(beq), Aub, np.array(bub)


if __name__ == "__main__":
    N, Qp = int(sys.argv[1]), int(sys.argv[2])
    lam, Aeq, beq, Aub, bub = system(N, Qp)
    mx = np.zeros(Qp)
    for x in range(Qp):
        c = np.zeros(Qp); c[x] = -1
        res = linprog(c, A_ub=Aub, b_ub=bub, A_eq=Aeq, b_eq=beq, bounds=[(0, None)] * Qp, method="highs")
        mx[x] = -res.fun
    null = [x for x in range(Qp) if mx[x] < 1e-9]
    off = [x for x in range(Qp) if lam[x] == 0]
    print(f"N={N} Q'={Qp}: rigid-null points {len(null)} of {Qp} ({len([x for x in null if lam[x]==0])} off [1,N])")
    print("null:", null[:200])
    print("min max-mu on [1,N]:", min(mx[lam > 0]), " values on [1,N]:", np.round(mx[lam > 0], 3).tolist())
