"""R25 from-scratch LP for SPW(C, sigma, Delta0) (EXCEPTIONAL_INTERFREQ2 §9).

SPW at N: R >= 0 on Z, summable, with
 (P1) R(b mod d) = c(b,d) = #{1<=n<=N : n = b (d)} for all d <= N/2,
 (P2) R(s) <= 1 - sigma for every class s of modulus d > C N,
 (P3) |R(s) - c(s)| <= Delta0 for N/2 < d <= C N   (only measured here).
We maximise sigma.

mode 'per Q': necessary condition (UPPER bound for sigma): any SPW R on Z projects to a
  measure on Z/Q' (Q' a multiple of L0 = lcm(1..N/2)) satisfying (P1) and (P2) for every
  d | Q' with d > CN (including d = Q', i.e. single points).
mode 'win a': sufficient condition (LOWER bound): R supported on [-aN, (a+1)N]; (P2) for all
  d up to the support length, pointwise beyond (a class of larger modulus has <= 1 support point).
usage: review_if2_spw.py per N C [Q']   |   review_if2_spw.py win N C a
"""
import sys
from math import gcd
import numpy as np
from scipy.optimize import linprog
from scipy.sparse import coo_matrix, vstack, hstack, csr_matrix

def lcm(a, b):
    return a * b // gcd(a, b)

def cnt(b, d, N):
    # #{1<=n<=N : n = b mod d}
    b %= d
    first = b if b >= 1 else d
    return 0 if first > N else (N - first) // d + 1

def class_rows(points, d):
    """rows: for each residue b mod d, indices of points congruent to b"""
    res = np.mod(points, d)
    return res

def solve(points, N, C, large_moduli, pointwise):
    """points: integer array (representatives); returns sigma, R, Delta0"""
    P = len(points)
    eq_r, eq_c, beq = [], [], []
    row = 0
    for d in range(1, N // 2 + 1):
        res = np.mod(points, d)
        for b in range(d):
            idx = np.nonzero(res == b)[0]
            eq_r += [row] * len(idx); eq_c += list(idx); beq.append(cnt(b, d, N)); row += 1
    Aeq = coo_matrix((np.ones(len(eq_r)), (eq_r, eq_c)), shape=(row, P + 1))
    ub_r, ub_c = [], []
    row = 0
    for d in large_moduli:
        res = np.mod(points, d)
        order = np.argsort(res, kind="stable")
        rs = res[order]
        # each residue present -> one row
        starts = np.r_[0, np.nonzero(np.diff(rs))[0] + 1]
        ends = np.r_[starts[1:], len(rs)]
        for s, e in zip(starts, ends):
            ub_r += [row] * (e - s); ub_c += list(order[s:e]); row += 1
    if pointwise:
        for i in range(P):
            ub_r.append(row); ub_c.append(i); row += 1
    nU = row
    A = coo_matrix((np.ones(len(ub_r)), (ub_r, ub_c)), shape=(nU, P + 1)).tolil()
    A[:, P] = np.ones((nU, 1))  # R(s) + sigma <= 1
    bub = np.ones(nU)
    cobj = np.zeros(P + 1); cobj[P] = -1
    bounds = [(0, None)] * P + [(None, None)]
    r = linprog(cobj, A_ub=A.tocsr(), b_ub=bub, A_eq=Aeq.tocsr(), b_eq=np.array(beq, float),
                bounds=bounds, method="highs")
    assert r.status == 0, r.message
    R = r.x[:P]
    # measure Delta0 over medium moduli
    D0 = 0.0
    for d in range(N // 2 + 1, int(C * N) + 1):
        res = np.mod(points, d)
        sums = np.bincount(res, weights=R, minlength=d)
        for b in range(d):
            D0 = max(D0, abs(sums[b] - cnt(b, d, N)))
    return -r.fun, R, D0

if __name__ == "__main__":
    mode, N, C = sys.argv[1], int(sys.argv[2]), float(sys.argv[3])
    if mode == "per":
        L0 = 1
        for d in range(1, N // 2 + 1):
            L0 = lcm(L0, d)
        Q = int(sys.argv[4]) if len(sys.argv) > 4 else L0
        assert Q % L0 == 0
        pts = np.arange(Q)
        large = [d for d in range(1, Q + 1) if Q % d == 0 and d > C * N]
        sig, R, D0 = solve(pts, N, C, large, pointwise=False)
        print(f"per N={N} C={C} Q'={Q}: sigma_max={sig:.4f} (upper bound for SPW) Delta0={D0:.3f}")
    else:
        a = int(sys.argv[4])
        pts = np.arange(-a * N, (a + 1) * N + 1)
        L = len(pts)
        large = [d for d in range(int(C * N) + 1, L)]
        sig, R, D0 = solve(pts, N, C, large, pointwise=True)
        on = R[(pts >= 1) & (pts <= N)]
        print(f"win N={N} C={C} support=[{-a*N},{(a+1)*N}]: sigma_max={sig:.4f} (lower bound) Delta0={D0:.3f} "
              f"mass on [1,N]={on.sum():.3f} max R={R.max():.3f}")
