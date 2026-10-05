"""R27b from-scratch check of LARGESIEVE2 Lemma 8.1 (uniform-marginal measure on a band set).

For D = l*l' (distinct primes >= 5), a coprime to D, eta <= 1/8:
S = {n mod D : ||n a / D|| <= 1/2 - eta}.  Claim: there is a probability on S
whose marginals mod l and mod l' are uniform.  We test feasibility of the
transportation LP directly (no use of the author's reduction), and also scan
eta upward to see where it first fails (margin check).
"""
import itertools, math, random
import numpy as np
from scipy.optimize import linprog
from fractions import Fraction


def primes(lo, hi):
    return [p for p in range(lo, hi) if p > 1 and all(p % q for q in range(2, int(p**.5) + 1))]


def band_set(l, lp, a, eta):
    D = l * lp
    S = []
    for n in range(D):
        x = Fraction(n * a % D, D)
        dist = min(x, 1 - x)
        if dist <= Fraction(1, 2) - eta:
            S.append(n)
    return S


def feasible(l, lp, S):
    # variables: mass on each n in S; constraints: sum over n≡x (l) = 1/l, n≡y (l') = 1/l'
    m = len(S)
    A = np.zeros((l + lp, m))
    for j, n in enumerate(S):
        A[n % l, j] = 1
        A[l + n % lp, j] = 1
    b = np.concatenate([np.full(l, 1 / l), np.full(lp, 1 / lp)])
    res = linprog(np.zeros(m), A_eq=A, b_eq=b, bounds=[(0, None)] * m, method="highs")
    return res.status == 0


def main():
    random.seed(1)
    ps = primes(5, 48)
    fails = 0
    tested = 0
    for l, lp in itertools.combinations(ps, 2):
        D = l * lp
        for eta in (Fraction(1, 8), Fraction(1, 9), Fraction(1, 10), Fraction(1, 20)):
            avals = [a for a in range(1, D) if math.gcd(a, D) == 1]
            for a in random.sample(avals, min(6, len(avals))):
                for (L1, L2) in ((l, lp), (lp, l)):
                    S = band_set(L1, L2, a, eta)
                    tested += 1
                    if not feasible(L1, L2, S):
                        fails += 1
                        print("FAIL", L1, L2, a, eta)
    print(f"Lemma 8.1: tested {tested} cases (eta<=1/8), failures {fails}")
    # margin scan: smallest eta where infeasible, small primes
    worst = None
    for l, lp in [(5, 7), (5, 11), (7, 11), (11, 13), (5, 13)]:
        D = l * lp
        for a in [a for a in range(1, D) if math.gcd(a, D) == 1]:
            for k in range(8, 60):
                eta = Fraction(k, 160)
                if not feasible(l, lp, band_set(l, lp, a, eta)):
                    if worst is None or eta < worst[0]:
                        worst = (eta, l, lp, a)
                    break
    print("smallest infeasible eta found on scan grid (step 1/160):", worst,
          "~", float(worst[0]) if worst else None)


if __name__ == "__main__":
    main()
