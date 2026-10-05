"""O49 / POINTWISE_OMEGA14 §1 checks.

(1) Lemma 1.1 (planting): exact rational verification of the explicit law
    nu = mu + P0 * sum_J w_J sigma_J  on random instances satisfying (1.1), stratified
    k = 0..3: nu >= 0, nu(0) = 0, and all marginals on <= k coordinates agree with mu.
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


def planted_rho(p, k):
    """rho = nu - mu, supported on configurations 1_y with |y| <= k+1 (keys: frozenset y)."""
    n = len(p)
    r = [pi / (1 - pi) for pi in p]
    P0 = Fr(1)
    for pi in p:
        P0 *= 1 - pi
    rho = {}
    ek1 = esym(r, k + 1)
    for J in itertools.combinations(range(n), k + 1):
        w = Fr(1)
        for i in J:
            w *= r[i]
        if w == 0:
            continue
        w /= ek1
        for s_ in range(k + 2):
            for y in itertools.combinations(J, s_):
                key = frozenset(y)
                rho[key] = rho.get(key, Fr(0)) + P0 * w * (-1) ** (s_ + 1)
    return P0, r, rho


def check_planting(rng, ks=(0, 1, 2, 3), trials=25):
    """Stratified by k; p_i in [0.2, 0.5] plus one zero-probability coordinate.
    Checks exactly: nu(1_y) = mu(1_y) + rho(1_y) >= 0 on supp(rho), nu(0) = 0, and every
    marginal of rho on <= k coordinates vanishes (enough: mu's are unchanged)."""
    tot = bad = 0
    for k in ks:
        done = 0
        while done < trials:
            n = rng.randint(k + 3, 22)
            p = [Fr(rng.randint(20, 50), 100) for _ in range(n - 1)] + [Fr(0)]
            rng.shuffle(p)
            r = [pi / (1 - pi) for pi in p]
            if sum(r) < (k + 1) + (2 * k + 1) * max(r):
                continue
            done += 1
            P0, r, rho = planted_rho(p, k)
            ok = rho.get(frozenset(), 0) == -P0
            for y, v in rho.items():
                m = P0
                for i in y:
                    m *= r[i]
                ok &= m + v >= 0
            for K in itertools.combinations(range(n), k):
                Ks = set(K)
                marg = {}
                for y, v in rho.items():
                    z = frozenset(y & Ks)
                    marg[z] = marg.get(z, Fr(0)) + v
                ok &= all(v == 0 for v in marg.values())
            bad += not ok
        print(f"    k={k}: {trials} instances (n up to 22)")
        tot += trials
    return tot, bad


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
    assert res.success, res.message
    assert (A @ res.x <= F + 1e-9).all()
    return -res.fun, float(mu[0])


def main():
    seed = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    rng = random.Random(seed)
    print("(1) Lemma 1.1, stratified:")
    done, bad = check_planting(rng)
    print(f"(1) Lemma 1.1 exact check: {done} random instances satisfying (1.1), failures = {bad}")
    assert bad == 0
    print("(2) toy LP, n iid bits with P(1)=p, level k: max E B / E F  (Lemma 1.1 threshold R*)")
    print(" n  k     p      R    R*=(k+1)+(2k+1)r   LPopt/EF")
    for n, k in [(10, 1), (10, 2), (12, 3)]:
        for p in [0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.4]:
            r = p / (1 - p)
            opt, ef = lp_opt([p] * n, k)
            print(f"{n:2d} {k:2d} {p:6.2f} {n*r:6.2f} {(k+1)+(2*k+1)*r:8.2f}        {opt/ef: .4f}")


if __name__ == "__main__":
    main()
