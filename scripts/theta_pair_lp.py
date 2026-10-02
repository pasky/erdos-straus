"""Toy LP for EXCEPTIONAL_THETA.md §5.7: do pair (AND) conditions beat single-slice
conditions of the same mass at the same level?

Product space: n coordinates, each uniform on Z/q.  A *pair system* forbids, for
each pair {i,j}, r random value-pairs (x_i,x_j) (the AND-conditions of balanced
moduli).  A *single system* of exactly the same total mass forbids, at each coordinate,
a set of probability p = (pair mass)/n (exchangeable; its level-m LP is the exact
polynomial LP in K ~ Bin(n,p) after symmetrisation).  For level m (majorant terms depend on at
most m coordinates; all coordinates have equal cost) we compute exactly by LP
    W(m) = min { E nu : nu = sum_{|T|<=m} nu_T(x_T), nu >= 0, nu >= 1 on avoid set }
and report savings -log W(m) (floating-point HiGHS; numerical, not certified).
Also reported: the void probability P(A), and the spectral bound from the proof of
Theorem 5.5 at level m (g of level m/2, g >= 1 on A):
    E g^2 >= P(A)^2 / ||Pi_{<=m/2} 1_A||^2   (Efron-Stein, floating point).
This projection bound is stronger than the displayed noise relaxation (5.1).
Run: uv run --with scipy python scripts/theta_pair_lp.py
"""
import itertools
import math
import random

import numpy as np
from scipy.optimize import linprog


def lp_level(n, q, avoid, m):
    from scipy.sparse import csr_matrix
    pts = np.array(list(itertools.product(range(q), repeat=n)))
    N = len(pts)
    # non-redundant basis: 1[x_T = a] with a in {1..q-1}^T (spans all functions of <= m coords)
    rows, colsx = [], []
    off = 0
    for k in range(m + 1):
        for T in itertools.combinations(range(n), k):
            ok = np.ones(N, dtype=bool)
            code = np.zeros(N, dtype=np.int64)
            for t in T:
                ok &= pts[:, t] > 0
                code = code * (q - 1) + (pts[:, t] - 1)
            rows.append(np.nonzero(ok)[0])
            colsx.append(off + code[ok])
            off += (q - 1) ** k
    A = csr_matrix((np.ones(sum(len(r_) for r_ in rows)), (np.concatenate(rows), np.concatenate(colsx))), shape=(N, off))
    c = np.asarray(A.mean(axis=0)).ravel()
    b = np.array([-1.0 if avoid(tuple(x)) else 0.0 for x in pts])
    res = linprog(c, A_ub=-A, b_ub=b, bounds=[(None, None)] * off, method="highs-ipm", options={"time_limit": 900})
    assert res.status == 0, res.message
    return res.fun


def es_energy_ratio(n, q, avoid, mh):
    """P(A)^2 / sum_{|T|<=mh} ||(1_A)_T||^2 via Efron-Stein on the uniform cube."""
    pts = list(itertools.product(range(q), repeat=n))
    f = np.array([1.0 if avoid(x) else 0.0 for x in pts]).reshape([q] * n)
    PA = f.mean()
    # projection onto level <= mh: sum over T, |T|<=mh, of ||f_T||^2 = sum_T sum_{S subset T} (-1)^{|T|-|S|} E[(E[f|x_S])^2]
    cond_energy = {}
    for k in range(mh + 1):
        for S in itertools.combinations(range(n), k):
            axes = tuple(i for i in range(n) if i not in S)
            g = f.mean(axis=axes) if axes else f
            cond_energy[S] = float((g ** 2).mean())
    tot = 0.0
    for k in range(mh + 1):
        for T in itertools.combinations(range(n), k):
            e = 0.0
            for j in range(k + 1):
                for S in itertools.combinations(T, j):
                    e += (-1) ** (k - j) * cond_energy[S]
            tot += e
    return PA, PA * PA / tot


def main():
    random.seed(7)
    n, q = 5, 5
    for r in [2, 3, 4]:
        pairs = {}
        for i, j in itertools.combinations(range(n), 2):
            vals = set()
            while len(vals) < r:
                vals.add((random.randrange(q), random.randrange(q)))
            pairs[(i, j)] = vals
        mass = len(pairs) * r / q ** 2

        def avoid_pair(x):
            return all((x[i], x[j]) not in v for (i, j), v in pairs.items())

        # single system with exactly the same mass: forbidden probability p = mass/n per
        # coordinate (exchangeable; its level-m LP is the exact polynomial LP in Bin(n,p))
        p = mass / n
        print(flush=True)
        print(f"r={r}: pair mass {mass:.2f} (n={n}, q={q}); single mass {mass:.2f} (p={p:.3f} per coordinate)")
        PA_p, _ = es_energy_ratio(n, q, avoid_pair, 0)
        PA_s = (1 - p) ** n
        print(f"   void: pair P(A)={PA_p:.4f} (-log {-math.log(PA_p):.3f}),"
              f" single P(A)={PA_s:.4f} (-log {-math.log(PA_s):.3f})")
        for m in [1, 2, 3, 4]:
            Wp = lp_level(n, q, avoid_pair, m)
            line = f"   m={m}: pair LP saving {-math.log(Wp):.3f}"
            # single system: exchangeable binary reduction is exact (thinning not needed: equal p)
            # min E Q(K), K~Bin(n,p), deg Q<=m, Q>=0 on 0..n, Q(0)>=1
            ks = np.arange(n + 1)
            pmf = np.array([math.comb(n, k) * p ** k * (1 - p) ** (n - k) for k in ks])
            V = np.vander(ks.astype(float), m + 1, increasing=True)
            bb = np.zeros(n + 1); bb[0] = -1
            res = linprog(pmf @ V, A_ub=-V, b_ub=bb, bounds=[(None, None)] * (m + 1), method="highs")
            line += f" | single LP saving {-math.log(res.fun):.3f}"
            if m % 2 == 0:
                _, sel = es_energy_ratio(n, q, avoid_pair, m // 2)
                line += f" | pair spectral (Lambda^2) bound: saving <= {-math.log(sel):.3f}"
            print(line, flush=True)


if __name__ == "__main__":
    main()
