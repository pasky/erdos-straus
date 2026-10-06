"""O53: relaxed SPW LP (EXCEPTIONAL_SPW2 §2).
R >= 0 on [-L, N+L]; exact window profile mod every d <= N/2;
full classes (modulus e > C N, meeting [1,N]):  R(s) <= 1 - eta;
sparse classes (e > C N, missing [1,N]):        R(s) <= K   (K = inf: dropped);
optional medium bound |R(s) - c(s)| <= Delta for N/2 < e <= C N.
Maximise eta.  Finite support => the solution is a genuine measure on Z
(classes of modulus > span are points and are included).
Usage: python spw2_relaxed_lp.py N L C K [Delta|inf] [out.npy|-] [offW]
  offW: force R = 0 on [1,N] (pseudo-window supported off the window)."""
import sys
import numpy as np
import scipy.sparse as sp
from scipy.optimize import linprog


def solve(N, L, C, K=np.inf, Delta=np.inf, offW=False):
    pts = np.arange(-L, N + L + 1); span = len(pts)
    inside = (pts >= 1) & (pts <= N)
    nv = span + 1
    re, ce, beq = [], [], []
    ru, cu, vu, bub = [], [], [], []
    ke = ku = 0
    D = N // 2
    for d in range(1, D + 1):
        for b in range(d):
            idx = np.nonzero((pts - b) % d == 0)[0]
            re += [ke] * len(idx); ce += list(idx)
            beq.append(int(inside[idx].sum())); ke += 1
    emin = int(np.floor(C * N)) + 1
    if np.isfinite(Delta):
        for e in range(D + 1, emin):
            for b in range(e):
                idx = np.nonzero((pts - b) % e == 0)[0]
                c = int(inside[idx].sum())
                ru += [ku] * len(idx); cu += list(idx); vu += [1.0] * len(idx); bub.append(c + Delta); ku += 1
                ru += [ku] * len(idx); cu += list(idx); vu += [-1.0] * len(idx); bub.append(Delta - c); ku += 1
    for e in range(emin, span + 1):
        for b in range(e):
            idx = np.nonzero((pts - b) % e == 0)[0]
            c = int(inside[idx].sum())
            if c:
                ru += [ku] * len(idx) + [ku]; cu += list(idx) + [span]; vu += [1.0] * len(idx) + [1.0]
                bub.append(1.0); ku += 1
            elif np.isfinite(K) and len(idx) > 1:
                ru += [ku] * len(idx); cu += list(idx); vu += [1.0] * len(idx); bub.append(K); ku += 1
    # points (modulus > span): R <= 1 - eta on W, <= K off W
    for i in np.nonzero(inside)[0]:
        ru += [ku, ku]; cu += [i, span]; vu += [1.0, 1.0]; bub.append(1.0); ku += 1
    Aeq = sp.csr_matrix((np.ones(len(re)), (re, ce)), shape=(ke, nv))
    Aub = sp.csr_matrix((vu, (ru, cu)), shape=(ku, nv))
    ub_out = K if np.isfinite(K) else None
    bounds = [((0, 0) if (offW and inside[i]) else (0, None if not inside[i] and ub_out is None else (ub_out if not inside[i] else None)))
              for i in range(span)] + [(None, 1.0)]
    cost = np.zeros(nv); cost[-1] = -1
    res = linprog(cost, A_ub=Aub, b_ub=bub, A_eq=Aeq, b_eq=beq, bounds=bounds, method="highs")
    return pts, res


if __name__ == "__main__":
    N, L, C = int(sys.argv[1]), int(sys.argv[2]), float(sys.argv[3])
    K = float(sys.argv[4]) if len(sys.argv) > 4 else np.inf
    Delta = float(sys.argv[5]) if len(sys.argv) > 5 else np.inf
    out = sys.argv[6] if len(sys.argv) > 6 else '-'
    offW = len(sys.argv) > 7 and sys.argv[7] == 'offW'
    pts, res = solve(N, L, C, K, Delta, offW)
    if res.status != 0:
        print(f"N={N} L={L} C={C} K={K} Delta={Delta} offW={offW}: {res.message}"); sys.exit()
    R = res.x[:-1]; eta = res.x[-1]
    inside = (pts >= 1) & (pts <= N)
    print(f"N={N} L={L} C={C} K={K} Delta={Delta} offW={offW}: eta={eta:.4f} "
          f"maxR_out={R[~inside].max():.3f} massW={R[inside].sum():.2f} "
          f"mass|x|>CN+N={R[(pts < -C*N) | (pts > N + C*N)].sum():.2f}")
    span = len(pts); smax = 0.0; dev = 0.0
    for e in range(N // 2 + 1, span + 1):
        for b in range(e):
            idx = np.nonzero((pts - b) % e == 0)[0]
            c = int(inside[idx].sum()); m = R[idx].sum()
            if e > C * N and c == 0: smax = max(smax, m)
            if e <= C * N: dev = max(dev, abs(m - c))
    print(f"   max sparse class = {smax:.3f}, max medium dev = {dev:.3f}")
    if out != '-':
        np.save(out, np.vstack([pts, R]))
