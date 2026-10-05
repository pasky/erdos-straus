"""O25: how much mass can a dual-feasible measure move off [1,N]?

On Z/Q' (Q' given), 𝔐(Q') = { mu >= 0 : mu(s) = lambda_N(s) for classes mod d | Q', d <= N/2;
                              l(d) <= mu(s) <= u(d) for classes mod d | Q', d > N/2 }.
Prints max mu(Z/Q' minus [1,N]) (= N iff a window-free measure exists) and,
optionally, the same with the d = Q' point constraints dropped.
Usage: python interfreq2_rigid.py N Qprime
"""
import sys
import numpy as np
import scipy.sparse as sp
from scipy.optimize import linprog
from sympy import divisors


def run(N, Qp, verbose=True):
    lam = np.zeros(Qp)
    for m in range(1, N + 1):
        lam[m % Qp] += 1
    rows_eq, beq, rows_ub, bub = [], [], [], []
    r_e, c_e, r_u, c_u = [], [], [], []
    ke = ku = 0
    for d in divisors(Qp):
        for b in range(d):
            pts = np.arange(b, Qp, d)
            c = lam[pts].sum()
            if 2 * d <= N:
                r_e.append(np.full(len(pts), ke)); c_e.append(pts); beq.append(c); ke += 1
            else:
                u, l = -(-N // d), N // d
                r_u.append(np.full(len(pts), ku)); c_u.append(pts); bub.append(u); ku += 1
                if l > 0:
                    r_u.append(np.full(len(pts), ku)); c_u.append(pts); bub.append(-l); ku += 1
                    # mark sign later
    # build ub matrix with signs: second row of a pair has -1 coefficients
    # (simpler: rebuild explicitly)
    r_u, c_u, v_u, bub2 = [], [], [], []
    ku = 0
    for d in divisors(Qp):
        if 2 * d <= N:
            continue
        u, l = -(-N // d), N // d
        for b in range(d):
            pts = np.arange(b, Qp, d)
            r_u.append(np.full(len(pts), ku)); c_u.append(pts); v_u.append(np.ones(len(pts))); bub2.append(u); ku += 1
            if l > 0:
                r_u.append(np.full(len(pts), ku)); c_u.append(pts); v_u.append(-np.ones(len(pts))); bub2.append(-l); ku += 1
    Aeq = sp.csr_matrix((np.ones(sum(len(x) for x in c_e)), (np.concatenate(r_e), np.concatenate(c_e))), shape=(ke, Qp))
    Aub = sp.csr_matrix((np.concatenate(v_u), (np.concatenate(r_u), np.concatenate(c_u))), shape=(ku, Qp))
    off = np.ones(Qp); off[lam > 0] = 0
    res = linprog(-off, A_ub=Aub, b_ub=np.array(bub2), A_eq=Aeq, b_eq=np.array(beq),
                  bounds=[(0, None)] * Qp, method="highs")
    assert res.status == 0, res.message
    val = -res.fun
    if verbose:
        print(f"N={N} Q'={Qp}: max mu(off [1,N]) = {val:.4f}  (N = {N})")
    return val, res.x


if __name__ == "__main__":
    run(int(sys.argv[1]), int(sys.argv[2]))
