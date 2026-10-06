"""O53: local (single-modulus) RSPW LP with K = inf (EXCEPTIONAL_SPW2 §5).
rho >= 0 on Z/e; class sums mod every d | e, d <= N/2, equal c(b,d);
for every divisor e' | e with e' > C N and every class mod e' meeting
W = {1..N}: rho(class) <= 1 - eta.  No condition on other classes.
Maximise eta.  Any R with (P1) and the RSPW full-class bounds projects to a
feasible rho, so the optimum is an upper bound for the global eta*.
Usage: python spw2_local_K.py N C e [e2 ...]"""
import sys
import numpy as np
import scipy.sparse as sp
from scipy.optimize import linprog


def solve(N, C, e):
    D = N // 2
    x = np.arange(e)
    W = np.zeros(e, bool); W[np.arange(1, N + 1) % e] = True
    rows, cols, beq = [], [], []
    r0 = 0
    for d in range(1, D + 1):
        if e % d: continue
        r = x % d
        rows.append(r0 + r); cols.append(x)
        beq.append(np.bincount(r[W], minlength=d)); r0 += d
    Aeq = sp.csr_matrix((np.ones(e * len(rows)), (np.concatenate(rows), np.concatenate(cols))), shape=(r0, e + 1))
    beq = np.concatenate(beq).astype(float)
    rows, cols = [], []
    r1 = 0
    for ep in range(int(np.floor(C * N)) + 1, e + 1):
        if e % ep: continue
        r = x % ep
        full = np.unique(r[W])
        m = -np.ones(ep, dtype=np.int64); m[full] = np.arange(len(full))
        rr = m[r]; ok = rr >= 0
        rows.append(r1 + rr[ok]); cols.append(x[ok]); r1 += len(full)
    rows.append(np.arange(r1)); cols.append(np.full(r1, e))
    Aub = sp.csr_matrix((np.ones(sum(len(a) for a in rows)), (np.concatenate(rows), np.concatenate(cols))), shape=(r1, e + 1))
    cost = np.zeros(e + 1); cost[-1] = -1
    res = linprog(cost, A_ub=Aub, b_ub=np.ones(r1), A_eq=Aeq, b_eq=beq,
                  bounds=[(0, None)] * e + [(None, 1)], method="highs")
    return res


if __name__ == "__main__":
    N, C = int(sys.argv[1]), float(sys.argv[2])
    for e in map(int, sys.argv[3:]):
        res = solve(N, C, e)
        print(f"N={N} C={C} e={e}: " + (f"eta_loc={res.x[-1]:.4f}" if res.status == 0 else res.message), flush=True)
