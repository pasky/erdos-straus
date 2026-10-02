"""EXCEPTIONAL_TWIN §6 evidence: exact window LPs for binary conditions.

Toy block: m coordinates, each uniform on Z/L.  Binary hard constraints:
each pair i<j gets kappa random forbidden points (a,b).  sigma = the
sequential law (coordinates in order; at i uniform off the residues
forbidden by earlier coordinates' values), conditioned on the avoid set
(dead ends excluded).  For d-junta-sums f >= 0 (all of [L]^m),

    C*_d = max E_sigma f / E_U f            (exact LP, HiGHS)

is the best possible constant in the step inequality E_U f >= E_sigma f / C.
For comparison the same LP is solved for a *unary* block with the same
total mass (each coordinate forbids round(p L) residues, sigma = product
law off them), and the void  -log U(avoid)  is reported.
Usage: uv run --with scipy --with numpy python scripts/twin_window_lp.py m L d kappa seed [uniform]
('uniform' replaces the sequential law by the uniform law on the avoid set;
then log C*_d <= void, and log C*_d >= the block's own d-junta sieve saving.)
"""
import itertools
import math
import sys

import numpy as np
from scipy.optimize import linprog
from scipy.sparse import csr_matrix


def lp_ratio(m, L, d, sigma):
    """max E_sigma f / E_U f over f >= 0, f sum of d-juntas. sigma: array over [L]^m."""
    pts = np.array(list(itertools.product(range(L), repeat=m)))
    N = len(pts)
    Ts = list(itertools.combinations(range(m), d))
    nv = len(Ts) * L ** d
    rows, cols = [], []
    obj = np.zeros(nv)
    for k, T in enumerate(Ts):
        idx = np.zeros(N, dtype=np.int64)
        for t in T:
            idx = idx * L + pts[:, t]
        col = k * L ** d + idx
        rows.append(np.arange(N))
        cols.append(col)
        np.add.at(obj, col, sigma)
    A = csr_matrix((np.ones(N * len(Ts)), (np.concatenate(rows), np.concatenate(cols))), shape=(N, nv))
    # maximize obj.c  s.t. A c >= 0, sum(c) * L^-d = 1
    res = linprog(-obj, A_ub=-A, b_ub=np.zeros(N), A_eq=np.full((1, nv), L ** (-d)), b_eq=[1.0],
                  bounds=(None, None), method="highs")
    assert res.status == 0, res.message
    return -res.fun


def seq_binary(m, L, kappa, rng):
    forb = {}
    for i, j in itertools.combinations(range(m), 2):
        S = set()
        while len(S) < kappa:
            S.add((int(rng.integers(L)), int(rng.integers(L))))
        forb[(i, j)] = S
    pts = list(itertools.product(range(L), repeat=m))
    sig = np.zeros(len(pts))
    avoid = np.zeros(len(pts), dtype=bool)
    for n, y in enumerate(pts):
        pr = 1.0
        ok = True
        for j in range(m):
            bad = {b for i in range(j) for (a, b) in forb[(i, j)] if a == y[i]}
            if y[j] in bad:
                ok = False
                break
            pr *= 1.0 / (L - len(bad)) if len(bad) < L else 0.0
        if ok:
            sig[n] = pr
            avoid[n] = True
    if UNIFORM:
        sig = avoid.astype(float)
    sig /= sig.sum()
    m2 = sum(len(S) for S in forb.values()) / L ** 2
    void = -math.log(avoid.mean())
    return sig, m2, void


def unary_same_mass(m, L, mass):
    k = max(0, min(L - 1, round(mass / m * L)))
    pts = list(itertools.product(range(L), repeat=m))
    sig = np.array([1.0 if all(v >= k for v in y) else 0.0 for y in pts])
    return sig / sig.sum(), m * k / L


UNIFORM = False

if __name__ == "__main__":
    m, L, d, kappa, seed = (int(x) for x in sys.argv[1:6])
    UNIFORM = len(sys.argv) > 6 and sys.argv[6] == "uniform"
    rng = np.random.default_rng(seed)
    sig, m2, void = seq_binary(m, L, kappa, rng)
    cb = lp_ratio(m, L, d, sig)
    sigu, mu = unary_same_mass(m, L, m2)
    cu = lp_ratio(m, L, d, sigu)
    print(f"m={m} L={L} d={d} kappa={kappa} seed={seed} sigma={'U|A' if UNIFORM else 'seq'}  binary: mass={m2:.3f} void={void:.3f} "
          f"logC*={math.log(cb):.4f} | unary: mass={mu:.3f} logC*={math.log(cu):.4f}")
