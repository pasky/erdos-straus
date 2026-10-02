"""Brute-force check of the reduction steps (thinning + symmetrisation) in
Proposition 2.4 of EXCEPTIONAL_THETA.md on tiny instances.

For n independent Bernoulli(p_i) and level m (functions of <= m coordinates),
compute exactly by LP
    W(p, m) = min { E f : f = sum_{|T|<=m} f_T(x_T), f >= 0, f(0) >= 1 }
and the reduced quantity
    R(p, m) = E_w [ W_ex(|Z(w)|, q, m) ],  q = max p_i,  w_i ~ Bern(p_i/q),
where W_ex(z, q, m) = min{ E Q(K) : K~Bin(z,q), deg Q <= m, Q>=0 on 0..z, Q(0)>=1 }.
The proof shows W(p, m) >= R(p, m).  Also prints the Selberg value as reference.
Run: uv run --with scipy python scripts/theta_reduction_check.py
"""
import itertools
import math
import random

import numpy as np
from scipy.optimize import linprog


def W_full(p, m):
    n = len(p)
    pts = list(itertools.product([0, 1], repeat=n))
    probs = np.array([math.prod(pi if xi else 1 - pi for pi, xi in zip(p, x)) for x in pts])
    # basis: AND-monomials x^S, |S| <= m  (spans all functions of <= m coordinates)
    subsets = [S for k in range(m + 1) for S in itertools.combinations(range(n), k)]
    A = np.array([[1.0 if all(x[i] for i in S) else 0.0 for S in subsets] for x in pts])
    c = probs @ A  # E f = sum_S c_S P(x^S=1)
    # constraints: A coef >= 0 for all x ; A[0] coef >= 1
    A_ub = -A.copy()
    b_ub = np.zeros(len(pts))
    b_ub[0] = -1.0
    res = linprog(c, A_ub=A_ub, b_ub=b_ub, bounds=[(None, None)] * len(subsets), method="highs")
    assert res.status == 0, res.message
    return res.fun


def W_ex(z, q, m):
    if z == 0:
        return 1.0
    m = min(m, z)
    ks = np.arange(z + 1)
    pmf = np.array([math.comb(z, k) * q ** k * (1 - q) ** (z - k) for k in ks])
    V = np.vander(ks.astype(float), m + 1, increasing=True)  # Q(k) = sum a_j k^j
    c = pmf @ V
    A_ub = -V
    b_ub = np.zeros(z + 1)
    b_ub[0] = -1.0
    res = linprog(c, A_ub=A_ub, b_ub=b_ub, bounds=[(None, None)] * (m + 1), method="highs")
    assert res.status == 0, res.message
    return res.fun


def R_reduced(p, m):
    q = max(p)
    n = len(p)
    tot = 0.0
    for w in itertools.product([0, 1], repeat=n):
        pw = math.prod((pi / q) if wi else 1 - pi / q for pi, wi in zip(p, w))
        tot += pw * W_ex(sum(w), q, m)
    return tot


if __name__ == "__main__":
    random.seed(1)
    worst = math.inf
    for trial in range(40):
        n = random.choice([4, 5, 6, 7])
        m = random.choice([1, 2, 3])
        p = [random.uniform(0.02, 0.45) for _ in range(n)]
        Wf = W_full(p, m)
        Rr = R_reduced(p, m)
        void = math.prod(1 - pi for pi in p)
        ok = Wf >= Rr - 1e-9 and Wf >= void - 1e-9
        worst = min(worst, Wf - Rr)
        print(f"n={n} m={m} W={Wf:.6f} reduced={Rr:.6f} void={void:.6f} {'ok' if ok else 'FAIL'}")
        assert ok
    print("all ok; min(W - reduced) =", worst)
