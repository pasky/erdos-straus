"""EXCEPTIONAL_TWIN2 Thm 1.4 check: exact log(Z2/Z1^2) vs (1+25δ)[Σ ρ̃ρ̃'π + Σ ρ̃_j q_j]
on small random binary systems (exact tensor computation).
usage: python twin2_binary_check.py [trials] [seed]"""
import sys, itertools
import numpy as np

def run(sizes, edges, nus, rho):
    k = len(sizes)
    A = np.ones(sizes)
    for (l, a, m, c) in edges:
        idx = [slice(None)] * k; idx[l] = a; idx[m] = c
        A[tuple(idx)] = 0.0
    P = np.ones(sizes)
    for l in range(k):
        sh = [1] * k; sh[l] = sizes[l]
        P = P * nus[l].reshape(sh)
    Z1 = float((A * P).sum())
    # Z2 = sum_{y,y'} prod mu(y_l,y'_l) A(y) A(y'); mu = rho Diag nu + (1-rho) nu nu^T
    T = A.copy()
    for l in range(k):
        nu = nus[l]
        M = rho[l] * np.diag(nu) + (1 - rho[l]) * np.outer(nu, nu)
        T = np.moveaxis(np.tensordot(M, T, axes=([1], [l])), 0, l)
    Z2 = float((T * A).sum())
    lhs = np.log(Z2 / Z1 ** 2)
    deg = [np.zeros(s) for s in sizes]
    w = np.zeros(k)
    diag = 0.0
    for (l, a, m, c) in edges:
        deg[l][a] += nus[m][c]; deg[m][c] += nus[l][a]
        pe = nus[l][a] * nus[m][c]
        w[l] += pe; w[m] += pe
        diag += rho[l] * rho[m] * pe
    q = np.array([(nus[l] * deg[l] ** 2).sum() for l in range(k)])
    rhs0 = diag + (rho * q).sum()
    return lhs, rhs0, w.max()

def main():
    trials = int(sys.argv[1]) if len(sys.argv) > 1 else 300
    rng = np.random.default_rng(int(sys.argv[2]) if len(sys.argv) > 2 else 1)
    worst = 0.0; worst_in = 0.0; n_in = 0
    for t in range(trials):
        k = rng.integers(3, 6)
        sizes = list(rng.choice([5, 7, 11, 13], size=k))
        if np.prod(sizes) > 200000: continue
        nus = [rng.dirichlet(np.ones(s) * rng.choice([0.5, 5.0])) for s in sizes]
        mode = rng.integers(3)
        edges = set()
        ne = rng.integers(1, 3 * k + 1)
        for _ in range(ne):
            l, m = rng.choice(k, 2, replace=False)
            if mode == 0:   # hub: concentrate on residue 0 at prime 0
                l = 0; a = 0
                if m == 0: m = int(rng.integers(1, k))
            else:
                a = rng.integers(sizes[l])
            c = rng.integers(sizes[m])
            edges.add((int(l), int(a), int(m), int(c)) if l < m else (int(m), int(c), int(l), int(a)))
        rho = rng.choice([1.0, 0.5, 0.1], size=k) * rng.random(k)
        if mode == 2: rho = np.ones(k)
        lhs, rhs0, wmax = run(sizes, list(edges), nus, rho)
        ratio = lhs / rhs0 if rhs0 > 0 else 0.0
        worst = max(worst, ratio)
        if wmax <= 1 / 16:
            n_in += 1
            bound = (1 + 25 * wmax) * rhs0
            assert lhs <= bound + 1e-12, (lhs, bound, wmax, sizes, sorted(edges), [list(np.round(x,4)) for x in nus], list(rho))
            worst_in = max(worst_in, ratio / (1 + 25 * wmax))
    print(f"trials={trials} in-hypothesis={n_in} max lhs/(1+25δ)rhs (in hyp)={worst_in:.4f} "
          f"max lhs/rhs (all, incl. δ>1/16)={worst:.4f}")

if __name__ == "__main__":
    main()
