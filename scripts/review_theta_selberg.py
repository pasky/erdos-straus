"""Reviewer checks of Theorem 5.5, Prop 5.7 (EXCEPTIONAL_THETA.md) and a numeric
look at Lemma 3.7.

(1) Theorem 5.5: on Omega = Z/m1 x ... with costs s_i = log m_i and an
    arbitrary event A (random AND-conditions incl. 'balanced' pairs), compute
      W2   = min { E g^2 : g in V_{lam/2}, g >= 1 on A }      (convex QP)
      proj = P(A)^2 / ||Pi_V 1_A||^2                        (proof's bound)
      thm  = max_alpha e^{-alpha lam/2} P(A)^2 / P(A cap A'_alpha)
    and check W2 >= proj >= thm.
(2) Prop 5.7: d/drho_l log P(A cap A'_rho) = E_{A cap A'}[Cov_l / J_l],
    checked against central finite differences at random rho.
(3) Lemma 3.7: S(x) = sum_{rh<=x} tau(4 r h^2 + 1) rh/phi(rh), ratio to x log^2 x.

Run: PYTHONPATH=scripts uv run --with scipy --with sympy python scripts/review_theta_selberg.py
"""
import itertools
import math
import random
import sys

import numpy as np
from scipy.optimize import minimize


def space(ms):
    pts = np.array(list(itertools.product(*[range(m) for m in ms])))
    return pts


def random_event(ms, rng, nconds):
    pts = space(ms)
    A = np.ones(len(pts), bool)
    for _ in range(nconds):
        k = rng.choice([1, 2, 2, 3])
        S = rng.sample(range(len(ms)), k)
        vals = [rng.randrange(ms[i]) for i in S]
        hit = np.ones(len(pts), bool)
        for i, v in zip(S, vals):
            hit &= pts[:, i] == v
        A &= ~hit
    return pts, A


def basis(ms, pts, kappa):
    """Indicator basis of V_kappa: functions of omega_T with sum log m_i <= kappa."""
    cols = []
    n = len(ms)
    for k in range(n + 1):
        for T in itertools.combinations(range(n), k):
            if sum(math.log(ms[i]) for i in T) <= kappa + 1e-12:
                for vals in itertools.product(*[range(ms[i]) for i in T]):
                    c = np.ones(len(pts))
                    for i, v in zip(T, vals):
                        c = c * (pts[:, i] == v)
                    cols.append(c)
    B = np.array(cols).T
    # orthonormal basis of span (uniform measure)
    U, s, _ = np.linalg.svd(B, full_matrices=False)
    r = (s > 1e-9 * s[0]).sum()
    return U[:, :r]


def noise_PAA(ms, pts, A, rho):
    """P(A cap A') with omega' rho-correlated (per coordinate)."""
    N = len(pts)
    f = A.astype(float) / N  # density wrt counting
    # apply T_rho coordinatewise on the tensor
    t = A.astype(float).reshape(ms)
    for i, m in enumerate(ms):
        mean = t.mean(axis=i, keepdims=True)
        t = rho[i] * t + (1 - rho[i]) * mean
    return float((A.astype(float).reshape(ms) * t).mean())


def part1(trials=25, seed=2):
    rng = random.Random(seed)
    worst = []
    for tr in range(trials):
        ms = rng.choice([[3, 5, 7], [3, 4, 5, 7], [5, 7, 11], [2, 3, 5, 7]])
        pts, A = random_event(ms, rng, rng.randint(3, 12))
        if A.sum() == 0:
            continue
        lam = rng.choice([2 * math.log(ms[0]), 2 * math.log(ms[1]), 2 * math.log(ms[0] * ms[1]), 2 * math.log(ms[-1] * ms[-2])])
        U = basis(ms, pts, lam / 2)
        N = len(pts)
        PA = A.mean()
        # projection bound
        proj1A = U @ (U.T @ A.astype(float))
        normsq = float((proj1A ** 2).mean())
        proj = PA ** 2 / normsq
        # QP in coordinates of U: g = U y ; E g^2 = |y|^2 / N
        Asub = U[A]
        cons = {"type": "ineq", "fun": lambda y: Asub @ y - 1.0, "jac": lambda y: Asub}
        y0 = U.T @ np.ones(N)  # g = 1 is feasible
        res = minimize(lambda y: y @ y / N, y0, jac=lambda y: 2 * y / N, constraints=[cons], method="SLSQP",
                       options={"maxiter": 2000, "ftol": 1e-14})
        W2 = res.fun
        feas = (Asub @ res.x).min()
        thm = max(math.exp(-a * lam / 2) * PA ** 2 / noise_PAA(ms, pts, A, [math.exp(-a * math.log(m)) for m in ms])
                  for a in np.geomspace(1e-3, 20, 200))
        ok = W2 >= proj * (1 - 1e-6) and proj >= thm * (1 - 1e-9) and feas > 1 - 1e-6
        print(f"  ms={ms} lam/2=log{math.exp(lam/2):.0f} P(A)={PA:.4f}: -log W2={-math.log(W2):.4f} "
              f"-log proj={-math.log(proj):.4f} -log thm={-math.log(thm):.4f} {'ok' if ok else 'FAIL'}")
        assert ok


def part2(trials=10, seed=4):
    rng = random.Random(seed)
    worst = 0.0
    for tr in range(trials):
        ms = rng.choice([[3, 5, 7], [2, 3, 5, 7], [5, 7, 11]])
        pts, A = random_event(ms, rng, rng.randint(3, 10))
        if A.sum() == 0:
            continue
        rho = [rng.uniform(0.05, 0.95) for _ in ms]
        Ar = A.reshape(ms)
        for l in range(len(ms)):
            h = 1e-6
            rp = list(rho); rp[l] += h
            rm = list(rho); rm[l] -= h
            fd = (math.log(noise_PAA(ms, pts, A, rp)) - math.log(noise_PAA(ms, pts, A, rm))) / (2 * h)
            # formula: condition on rest of both copies; rest coordinates coupled with rho
            others = [i for i in range(len(ms)) if i != l]
            num, den = 0.0, 0.0
            # enumerate rest pairs (omega_rest, omega'_rest) with coupling weights
            rest_vals = list(itertools.product(*[range(ms[i]) for i in others]))
            for w in rest_vals:
                for w2 in rest_vals:
                    wt = 1.0
                    for i, a, b in zip(others, w, w2):
                        m = ms[i]
                        wt *= (1.0 / m) * (rho[i] * (a == b) + (1 - rho[i]) / m)
                    if wt == 0:
                        continue
                    idx = [slice(None)] * len(ms)
                    sl1 = list(idx); sl2 = list(idx)
                    for i, a, b in zip(others, w, w2):
                        sl1[i] = a; sl2[i] = b
                    col1 = Ar[tuple(sl1)]  # in-A indicator over residues at l
                    col2 = Ar[tuple(sl2)]
                    m = ms[l]
                    F, F2 = ~col1, ~col2
                    p, p2 = F.mean(), F2.mean()
                    J = rho[l] * (1 - (F | F2).mean()) + (1 - rho[l]) * (1 - p) * (1 - p2)
                    Cov = (F & F2).mean() - p * p2
                    num += wt * Cov
                    den += wt * J
            formula = num / den
            worst = max(worst, abs(fd - formula))
    print(f"  Prop 5.7 derivative formula vs finite differences: max abs error {worst:.2e}")
    assert worst < 1e-5


def part3(xs):
    from sympy import divisor_count, totient
    for x in xs:
        S = 0.0
        for r in range(1, x + 1):
            for h in range(1, x // r + 1):
                n = r * h
                S += int(divisor_count(4 * r * h * h + 1)) * n / int(totient(n))
        print(f"  Lemma 3.7: x={x}: S(x)/(x log^2 x) = {S / (x * math.log(x) ** 2):.4f}", flush=True)


if __name__ == "__main__":
    which = sys.argv[1] if len(sys.argv) > 1 else "123"
    if "1" in which:
        print("Theorem 5.5:"); part1()
    if "2" in which:
        print("Prop 5.7:"); part2()
    if "3" in which:
        part3([300, 1000, 3000, 10000])
