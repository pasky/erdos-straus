"""R53 from-scratch check of SPW2 Lemma 4.1 (dual of RSPW, K = inf) on Z/Q'.
Primal: max eta, rho>=0 on Z/Q', profile mod d<=D equals the window's,
rho(s) <= 1-eta on full classes (modulus e|Q', e>CN, meeting W).
Dual formula: eta* = 1 - sup{ -sum_W g / Z : g in V_D, z>=0 on full classes,
g + sum z_s 1_s >= 0, Z = sum z_s }  (normalise Z = 1)."""
import numpy as np, math, sys
from scipy.optimize import linprog

def setup(N, C, Q):
    D = N//2; x = np.arange(Q)
    W = np.zeros(Q, bool); W[np.arange(1, N+1) % Q] = True
    small = [(x % d == b).astype(float) for d in range(1, D+1) for b in range(d)]
    cvals = [float(sum(1 for n in range(1, N+1) if n % d == b)) for d in range(1, D+1) for b in range(d)]
    full = []
    for e in range(1, Q+1):
        if Q % e or e <= C*N: continue
        for n0 in range(1, N+1):
            full.append((x % e == n0 % e).astype(float))
    return np.array(small), np.array(cvals), np.array(full), W

def primal(N, C, Q):
    S, cv, F, W = setup(N, C, Q)
    nv = Q + 1; c = np.zeros(nv); c[-1] = -1
    Aeq = np.c_[S, np.zeros(len(S))]
    Aub = np.c_[F, np.ones(len(F))]
    r = linprog(c, A_ub=Aub, b_ub=np.ones(len(F)), A_eq=Aeq, b_eq=cv,
                bounds=[(0, None)]*Q + [(None, None)], method="highs")
    assert r.status == 0; return -r.fun

def dual(N, C, Q):
    S, cv, F, W = setup(N, C, Q)
    ny, nz = len(S), len(F)
    # variables y (free), z>=0 ; g = S^T y ; constraint g + F^T z >= 0 ; sum z = 1
    # maximise -sum_W g = -(S[:,W].sum(1)) . y
    c = np.r_[S[:, W].sum(1), np.zeros(nz)]          # minimise sum_W g
    Aub = -np.c_[S.T, F.T]
    Aeq = np.r_[np.zeros(ny), np.ones(nz)][None, :]
    r = linprog(c, A_ub=Aub, b_ub=np.zeros(Q), A_eq=Aeq, b_eq=[1.0],
                bounds=[(None, None)]*ny + [(0, None)]*nz, method="highs")
    assert r.status == 0; return 1 - (-r.fun)

if __name__ == "__main__":
    for (N, C, Q) in ((6, 2, 60), (12, 2, 27720), (12, 2, 60), (12, 1.1, 60), (16, 1.1, 840), (16, 2, 840), (20, 1.2, 2520), (12, 1.0, 27720)):
        p, d = primal(N, C, Q), dual(N, C, Q)
        print(f"N={N} C={C} Q'={Q}: primal eta*={p:.6f}  dual formula={d:.6f}  diff={abs(p-d):.1e}")
        assert abs(p - d) < 1e-6
