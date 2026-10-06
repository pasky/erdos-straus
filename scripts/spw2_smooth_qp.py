"""O53: a 'spread' RSPW measure: fix eta, minimise sum R^2 (QP) to expose structure.
Usage: python spw2_smooth_qp.py N L C eta out.npy"""
import sys
import numpy as np
import cvxpy as cp
sys.path.insert(0, '.')
from spw2_relaxed_fast import build

N, L, C, eta = int(sys.argv[1]), int(sys.argv[2]), float(sys.argv[3]), float(sys.argv[4])
pts, Aeq, beq, Aub, bub = build(N, L, C)
span = len(pts)
Aeq = Aeq[:, :span]; Aub = Aub[:, :span]
R = cp.Variable(span)
cons = [R >= 0, Aeq @ R == beq, Aub @ R <= 1 - eta]
prob = cp.Problem(cp.Minimize(cp.sum_squares(R)), cons)
prob.solve(solver="CLARABEL")
print(prob.status, prob.value)
r = R.value
np.save(sys.argv[5], np.vstack([pts, r]))
W = (pts >= 1) & (pts <= N)
print("mass W", r[W].sum(), "max on W", r[W].max())
for a, b in [(-L, -4 * N), (-4 * N, -2 * N), (-2 * N, -N), (-N, 0), (N + 1, 2 * N), (2 * N, 3 * N), (3 * N, 5 * N), (5 * N, N + L)]:
    m = (pts > a) & (pts <= b)
    print(f"({a},{b}] mass {r[m].sum():.3f} max {r[m].max():.3f}")
