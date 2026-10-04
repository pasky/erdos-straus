"""O18 check of EXCEPTIONAL_INTERFREQ Thm 2.2 (EVIDENCE; floating-point LP).

For small D, solve exactly (HiGHS LP) the extremal problem
    min  sum_{n<=N} nu(n)   s.t.  nu >= 0 on Z/Q,  E nu = 1,
over nu = combinations of classes of moduli <= D (Q = lcm(1..D)).
Thm 2.2 predicts min >= N - D.  We print the LP minimum and N - D.
Memory: Q <= 2520 variables-ish; trivial.
"""
import sys
from math import gcd
import numpy as np
from scipy.optimize import linprog


def lcm_upto(D):
    q = 1
    for d in range(1, D + 1):
        q = q * d // gcd(q, d)
    return q


def run(D, N):
    Q = lcm_upto(D)
    # basis: indicator of class b mod d, for d<=D, b<d  (redundant but fine)
    cols = [(d, b) for d in range(1, D + 1) for b in range(d)]
    n = np.arange(Q)
    A = np.array([(n % d == b).astype(float) for d, b in cols]).T  # Q x m
    interval = np.array([((np.arange(1, N + 1) % d) == b).sum() for d, b in cols], float)
    mean = np.array([1.0 / d for d, b in cols])
    res = linprog(interval, A_ub=-A, b_ub=np.zeros(Q), A_eq=mean[None, :], b_eq=[1.0],
                  bounds=[(None, None)] * len(cols), method="highs")
    assert res.status == 0, res.message
    return res.fun


if __name__ == "__main__":
    print("D  N  LPmin  N-D  ok")
    for D in [2, 3, 4, 5, 6, 7, 8]:
        for N in sorted({D + 1, 2 * D, 3 * D + 1, 5 * D}):
            v = run(D, N)
            print(D, N, round(v, 6), N - D, v >= N - D - 1e-7)
            assert v >= N - D - 1e-7
