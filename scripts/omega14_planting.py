"""O49 / POINTWISE_OMEGA14 §1 checks.

(1) Lemma 1.1 (planting): exact rational verification of the explicit law
    nu = mu + P0 * sum_J w_J sigma_J  on random small instances satisfying (1.1):
    nu >= 0, nu(0) = 0, and all marginals on <= k coordinates agree with mu.
(2) Theorem 1.3 toy LP: n independent bits, F = 1[all zero]; maximise E_mu B over
    B in span{functions of <= k bits}, B <= F pointwise. Lemma 1.1 predicts optimum 0
    whenever R >= (k+1)+(2k+1)r*; we report the LP optimum and the smallest R where it
    vanishes (sharpness of the constant).
Usage: PYTHONPATH=scripts uv run python scripts/omega14_planting.py [seed]
"""
import itertools
import random
import sys
from fractions import Fraction as Fr

import numpy as np
from scipy.optimize import linprog


def esym(vals, a):
    e = [Fr(0)] * (a + 1)
    e[0] = Fr(1)
    for v in vals:
        for j in range(a, 0, -1):
            e[j] += e[j - 1] * v
    return e[a]


def planted(p, k):
    n = len(p)
    r = [pi / (1 - pi) for pi in p]
    P0 = Fr(1)
    for pi in p:
        P0 *= 1 - pi
    mu = {}
    for x in itertools.product((0, 1), repeat=n):
        m = Fr(1)
        for xi, pi in zip(x, p):
            m *= pi if xi else 1 - pi
        mu[x] = m
    nu = dict(mu)
    ek1 = esym(r, k + 1)
    for J in itertools.combinations(range(n), k + 1):
        w = Fr(1)
        for i in J:
            w *= r[i]
        w /= ek1
        for s in range(k + 2):
            for y in itertools.combinations(J, s):
                x = tuple(1 if i in y else 0 for i in range(n))
                nu[x] += P0 * w * (-1) ** (s + 1)
    return mu, nu


def check_planting(rng, trials=300):
    bad = 0
    done = 0
    while done < trials:
        n = rng.randint(2, 9)
        k = rng.randint(0, min(3, n - 1))
        p = [Fr(rng.randint(1, 60), 100) for _ in range(n)]
        r = [pi / (1 - pi) for pi in p]
        if sum(r) < (k + 1) + (2 * k + 1) * max(r):
            continue
        done += 1
        mu, nu = planted(p, k)
        ok = min(nu.values()) >= 0 and nu[tuple([0] * n)] == 0
        for K in itertools.combinations(range(n), k):
            for z in itertools.product((0, 1), repeat=k):
                a = sum(v for x, v in mu.items() if all(x[i] == zi for i, zi in zip(K, z)))
                b = sum(v for x, v in nu.items() if all(x[i] == zi for i, zi in zip(K, z)))
                ok &= a == b
        bad += not ok
    return done, bad


def lp_opt(p, k):
    """max E B over B = sum_{|K|<=k} g_K(x_K), B <= 1[x=0]."""
    n = len(p)
    xs = list(itertools.product((0, 1), repeat=n))
    mu = np.array([np.prod([pi if xi else 1 - pi for xi, pi in zip(x, p)]) for x in xs])
    feats = []
    for s in range(k + 1):
        for K in itertools.combinations(range(n), s):
            for z in itertools.product((0, 1), repeat=s):
                feats.append(np.array([float(all(x[i] == zi for i, zi in zip(K, z))) for x in xs]))
    A = np.array(feats).T  # rows: points, cols: features
    F = np.array([1.0 if sum(x) == 0 else 0.0 for x in xs])
    res = linprog(-(mu @ A), A_ub=A, b_ub=F, bounds=[(None, None)] * A.shape[1], method="highs")
    return -res.fun, float(mu[0])


def main():
    seed = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    rng = random.Random(seed)
    done, bad = check_planting(rng)
    print(f"(1) Lemma 1.1 exact check: {done} random instances satisfying (1.1), failures = {bad}")
    print("(2) toy LP, n iid bits with P(1)=p, level k: max E B / E F  (Lemma 1.1 threshold R*)")
    print(" n  k     p      R    R*=(k+1)+(2k+1)r   LPopt/EF")
    for n, k in [(10, 1), (10, 2), (12, 3)]:
        for p in [0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.4]:
            r = p / (1 - p)
            opt, ef = lp_opt([p] * n, k)
            print(f"{n:2d} {k:2d} {p:6.2f} {n*r:6.2f} {(k+1)+(2*k+1)*r:8.2f}        {opt/ef: .4f}")


if __name__ == "__main__":
    main()
