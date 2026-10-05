"""O53: vectorised relaxed SPW LP, K = inf (only full-class constraints).
R >= 0 on [-L, N+L]; exact window profile mod d <= N/2;
R(n0 + eZ) <= 1 - eta for every n0 in [1,N], e > C N (within the support;
e > span gives the pointwise bound on [1,N]).  Maximise eta.
Optionally Kz: pointwise cap R <= Kz off [1,N].
Usage: python spw2_relaxed_fast.py N L C [Kz] [out.npy]"""
import sys, time
import numpy as np
import scipy.sparse as sp
from scipy.optimize import linprog


def build(N, L, C):
    pts = np.arange(-L, N + L + 1); span = len(pts)
    rows, cols = [], []
    beq = []
    r0 = 0
    D = N // 2
    W = (pts >= 1) & (pts <= N)
    for d in range(1, D + 1):
        r = pts % d
        rows.append(r0 + r); cols.append(np.arange(span))
        beq.append(np.bincount(r[W], minlength=d))
        r0 += d
    Aeq = sp.csr_matrix((np.ones(sum(len(x) for x in rows)), (np.concatenate(rows), np.concatenate(cols))),
                        shape=(r0, span + 1))
    beq = np.concatenate(beq).astype(float)
    rows, cols = [], []
    r1 = 0
    emin = int(np.floor(C * N)) + 1
    for e in range(emin, span + 1):
        m = -np.ones(e, dtype=np.int64)
        m[np.arange(1, N + 1) % e] = np.arange(N)
        r = m[pts % e]
        ok = r >= 0
        rows.append(r1 + r[ok]); cols.append(np.nonzero(ok)[0])
        r1 += N
    # eta column for every full-class row
    rows.append(np.arange(r1)); cols.append(np.full(r1, span))
    Aub = sp.csr_matrix((np.ones(sum(len(x) for x in rows)), (np.concatenate(rows), np.concatenate(cols))),
                        shape=(r1, span + 1))
    bub = np.ones(r1)
    return pts, Aeq, beq, Aub, bub


if __name__ == "__main__":
    N, L, C = int(sys.argv[1]), int(sys.argv[2]), float(sys.argv[3])
    Kz = float(sys.argv[4]) if len(sys.argv) > 4 else None
    t0 = time.time()
    pts, Aeq, beq, Aub, bub = build(N, L, C)
    span = len(pts)
    W = (pts >= 1) & (pts <= N)
    bounds = [(0, 1.0) if W[i] else (0, Kz) for i in range(span)] + [(None, 1.0)]
    cost = np.zeros(span + 1); cost[-1] = -1
    res = linprog(cost, A_ub=Aub, b_ub=bub, A_eq=Aeq, b_eq=beq, bounds=bounds, method="highs")
    if res.status != 0:
        print(f"N={N} L={L} C={C}: {res.message}"); sys.exit()
    R = res.x[:-1]
    print(f"N={N} L={L} C={C} Kz={Kz}: eta={res.x[-1]:.4f} maxR_out={R[~W].max():.3f} "
          f"massW={R[W].sum():.2f} far={R[(pts < N - C*N) | (pts > C*N + 1)].sum():.2f} "
          f"rows={Aub.shape[0]} nnz={Aub.nnz} t={time.time()-t0:.0f}s")
    if len(sys.argv) > 5:
        np.save(sys.argv[5], np.vstack([pts, R]))
