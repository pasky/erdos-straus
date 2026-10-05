"""O25: LP search for the weight phi of EXCEPTIONAL_INTERFREQ2 Prop 3.2.

phi is supported on [-L, N+L].  Conditions (t = M/N fixed, s = t*eta maximised):
 (P1) phi <= 1 on [1,N], phi <= 0 outside;
 (P2) sum_{n = b (d)} phi = t N / d   for all d <= N/2, all b;
 (P3) for d > N/2, all b, c = #([1,N] cap b mod d), u = ceil(N/d), l = floor(N/d):
        Phi >= c - u + t N/d + s
        Phi <= c - l + t N/d - s        (only for N/2 < d <= N, where l = 1)
 classes meeting the support in <= 1 point (d > span) reduce to pointwise rows.
mode "exact" (default; Prop 3.2 with rho uniform up to modulus N^K):
 the (P3) rows for d <= span carry no margin s; only the pointwise rows
 (classes of modulus > N^K) carry s.  mode "eta": margin s on all rows.
Usage: python interfreq2_phi_lp.py N L t [cut] [mode]
  cut (default 0.5): small cutoff D_s = floor(cut*N).
Prints the optimal s (= t*eta) and min of phi on [1,N].
"""
import sys
import numpy as np
import scipy.sparse as sp
from scipy.optimize import linprog


def solve(N, L, t, cut=0.5, verbose=True, mode="exact", dmax=None, points=True, dset=None):
    lo, hi = -L, N + L
    pts = np.arange(lo, hi + 1)
    span = len(pts)
    nv = span + 1  # last variable is s
    Ds = int(cut * N)
    rows_eq, beq = [], []
    rows_ub, bub = [], []
    def cls(b, d):
        return [i for i, n in enumerate(pts) if (n - b) % d == 0]
    inside = (pts >= 1) & (pts <= N)
    # (P2)
    for d in range(1, Ds + 1):
        for b in range(d):
            rows_eq.append((cls(b, d), 1.0, None))
            beq.append(t * N / d)
    # (P3) explicit classes for Ds < d <= span
    for d in (dset if dset is not None else range(Ds + 1, min(span, dmax or span) + 1)):
        u = -(-N // d)
        l = N // d
        for b in range(d):
            idx = cls(b, d)
            if not idx:
                continue
            c = int(sum(inside[i] for i in idx))
            if mode == "exact":
                # rho exactly uniform for d <= N^K (K large): no margin s here
                rows_ub.append((idx, -1.0, None))
                bub.append(-(c - u + t * N / d))
                rows_ub.append((idx, 1.0, None))
                bub.append(c - l + t * N / d)
                continue
            # -Phi + s <= -(c - u + tN/d)
            rows_ub.append((idx, -1.0, 1.0))
            bub.append(-(c - u + t * N / d))
            if d <= N:
                # Phi + s <= c - l + tN/d
                rows_ub.append((idx, 1.0, 1.0))
                bub.append(c - l + t * N / d)
    # pointwise rows for d > span (worst case d = span+1)
    dd = span + 1
    for i, n in (enumerate(pts) if points else []):
        c = 1 if inside[i] else 0
        rows_ub.append(([i], -1.0, 1.0))
        bub.append(-(c - 1 + t * N / dd))
    def build(rows):
        r, cidx, v = [], [], []
        for k, (idx, coef, scoef) in enumerate(rows):
            for i in idx:
                r.append(k); cidx.append(i); v.append(coef)
            if scoef is not None:
                r.append(k); cidx.append(span); v.append(scoef)
        return sp.csr_matrix((v, (r, cidx)), shape=(len(rows), nv))
    Aeq, Aub = build(rows_eq), build(rows_ub)
    bounds = [(None, 1.0 if inside[i] else 0.0) for i in range(span)] + [(None, t)]
    cobj = np.zeros(nv); cobj[-1] = -1.0
    res = linprog(cobj, A_ub=Aub, b_ub=np.array(bub), A_eq=Aeq, b_eq=np.array(beq),
                  bounds=bounds, method="highs")
    if res.status != 0:
        if verbose:
            print(f"N={N} L={L} t={t} cut={cut}: status {res.status} {res.message}")
        return None, None
    phi = res.x[:span]
    s = res.x[-1]
    if verbose:
        print(f"N={N} L={L} t={t} cut={cut}: s=t*eta={s:.5f} eta={s/t:.4f} "
              f"min phi[1,N]={phi[inside].min():.4f} min phi out={phi[~inside].min():.4f}")
    return s, phi


if __name__ == "__main__":
    N = int(sys.argv[1]); L = int(sys.argv[2]); t = float(sys.argv[3])
    cut = float(sys.argv[4]) if len(sys.argv) > 4 else 0.5
    mode = sys.argv[5] if len(sys.argv) > 5 else "exact"
    solve(N, L, t, cut, mode=mode)
