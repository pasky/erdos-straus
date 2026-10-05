"""R49 from-scratch toy LP for POINTWISE_OMEGA14 §1 numerics (2).
n iid bits P(1)=p, F=1[all zero]. B in span of functions of <=k bits, B<=F.
By symmetrisation (F and the law are S_n-invariant, the k-junta span is S_n-invariant,
constraint set convex) the optimum is attained by a symmetric B; symmetric elements of the
k-junta span = g(|x|) with g a polynomial of degree <=k in |x|. Exact LP over g.
Report the smallest R=n p/(1-p) at which max E B / E F <= 1e-9, by bisection in p."""
import sys
from math import comb
import numpy as np
from scipy.optimize import linprog


def best_ratio(n, k, p):
    w = np.arange(n + 1)
    pi = np.array([comb(n, i) * p**i * (1 - p) ** (n - i) for i in w])
    V = np.vstack([w.astype(float) ** j for j in range(k + 1)]).T  # g = V c
    c_obj = -(pi @ V)
    b = np.zeros(n + 1)
    b[0] = 1.0
    res = linprog(c_obj, A_ub=V, b_ub=b, bounds=[(None, None)] * (k + 1), method="highs")
    if res.status == 3:  # unbounded cannot happen since g(w)<=..., but guard
        return float("inf")
    assert res.status == 0, res
    return -res.fun / (1 - p) ** n


def threshold(n, k):
    lo, hi = 1e-6, 0.95
    if best_ratio(n, k, hi) > 1e-9:
        return None
    for _ in range(60):
        mid = (lo + hi) / 2
        if best_ratio(n, k, mid) > 1e-9:
            lo = mid
        else:
            hi = mid
    p = hi
    return n * p / (1 - p), p / (1 - p)


if __name__ == "__main__":
    for n, k in [(10, 1), (10, 2), (12, 3), (20, 1), (20, 2), (20, 3), (30, 4)]:
        t = threshold(n, k)
        if t is None:
            print(n, k, "no threshold below p=0.95")
            continue
        R, r = t
        print(f"n={n} k={k}: optimum vanishes at R~{R:.3f}; sufficient (k+1)+(2k+1)r* = {(k+1)+(2*k+1)*r:.3f}")
