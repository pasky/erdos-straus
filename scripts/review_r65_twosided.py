"""R65 from-scratch check of v5 Thm 18.1 (two-sided order-k sieve limit, CU Thm 4.1), symmetric case.

Fix x_s; n big coordinates, each hit independently with probability p (p <= 1/4), P = n p,
H = #hits, F = 1[H=0].  Averaging over the hit/non-hit sigma-algebra and over permutations
preserves V_k and the constraints, so the extremal problems reduce to polynomials g(h) of degree
<= k in h = H (Chebyshev basis for conditioning):
   lower:  max E g(H)  s.t. g(0) <= 1, g(h) <= 0 (h >= 1)      [(L-): value <= 0 if k <= 0.6P-1]
   upper:  min E g(H)  s.t. g(0) >= 1, g(h) >= 0 (h >= 1)      [(U+): <= 2e^{-P} for even k >= e^2 P]
Also checks Bonferroni Q_k(h) = sum_{j<=k} (-1)^j C(h,j): Q_k >= F for even k, <= F for odd k, and
E Q_k bounds of (U+)/(L+), exactly with Fractions.
"""
import math
from fractions import Fraction
import numpy as np
from scipy.optimize import linprog


def lp(n, p, k, sense):
    h = np.arange(n + 1)
    x = 2 * h / n - 1
    V = np.polynomial.chebyshev.chebvander(x, k)  # (n+1) x (k+1)
    w = np.array([math.comb(n, i) * p**i * (1 - p) ** (n - i) for i in range(n + 1)])
    obj = w @ V
    if sense == "lower":  # max obj.a s.t. V a <= F
        res = linprog(-obj, A_ub=V, b_ub=(h == 0).astype(float), bounds=[(None, None)] * (k + 1), method="highs")
        return -res.fun if res.status == 0 else float("inf")
    res = linprog(obj, A_ub=-V, b_ub=-(h == 0).astype(float), bounds=[(None, None)] * (k + 1), method="highs")
    return res.fun


bad = []
for n, p in [(60, 0.25), (100, 0.15), (200, 0.05), (400, 0.05)]:
    P = n * p
    first_pos = None
    for k in range(0, min(n, 60)):
        v = lp(n, p, k, "lower")
        if k <= 0.6 * P - 1 and v > 1e-9:
            bad.append(("L-", n, p, k, v))
        if first_pos is None and v > 1e-9:
            first_pos = k
    ub = {k: lp(n, p, k, "upper") for k in (int(P), int(2 * P), int(3 * P)) if k < n}
    print(f"n={n} p={p} P={P:.1f}: (L-) threshold 0.6P-1={0.6*P-1:.1f}; first k with positive minorant "
          f"(LP) = {first_pos};  min majorant E: " + ", ".join(f"k={k}: {v:.3e}" for k, v in ub.items())
          + f"; e^-P={math.exp(-P):.3e}")

# exact Bonferroni checks
for n, p in [(40, Fraction(1, 4)), (120, Fraction(1, 20))]:
    P = n * p
    for k in range(1, n):
        Q = [sum((-1) ** j * math.comb(h, j) for j in range(k + 1)) for h in range(n + 1)]
        F = [1] + [0] * n
        if k % 2 == 0:
            assert all(q >= f for q, f in zip(Q, F))
        else:
            assert all(q <= f for q, f in zip(Q, F))
        EQ = sum(Fraction(math.comb(n, h)) * p**h * (1 - p) ** (n - h) * Q[h] for h in range(n + 1))
        if k >= math.e**2 * P:
            if k % 2 == 0 and not EQ <= 2 * Fraction(math.exp(-P)):
                bad.append(("U+", n, p, k))
            if k % 2 == 1 and not EQ > 0:
                bad.append(("L+", n, p, k))
print("Bonferroni sign and (U+)/(L+) checks done")
print("violations:", bad)
assert not bad
print("OK")
