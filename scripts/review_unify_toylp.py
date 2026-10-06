"""R60 independent float re-check of CEILINGS_UNIFIED §4.4 thresholds (EVIDENCE only).
n i.i.d. bits with P(1)=p; symmetric order-k functions = polynomials of degree <= k in
K = #ones (basis C(K,j)/C(n,j)). F = 1[K=0].
 minorant: max E B, B(0)<=1, B(K)<=0 (K>=1)
 majorant: min E G, G(0)>=1, G(K)>=0 (K>=1)
Reports least k with E B/E F > 1e-6 and least k with saving >= 0.9 log(1/EF).
Floating point (HiGHS) with mpmath-free rescaling; cross-check only."""
import math
import numpy as np
from scipy.optimize import linprog


def run(n, p, kmax):
    pmf = np.array([math.comb(n, K) * p ** K * (1 - p) ** (n - K) for K in range(n + 1)])
    EF = pmf[0]
    resB, resG = {}, {}
    for k in range(0, kmax + 1):
        A = np.array([[math.comb(K, j) / math.comb(n, j) for j in range(k + 1)] for K in range(n + 1)])
        mean = pmf @ A
        b = np.zeros(n + 1); b[0] = 1.0
        rB = linprog(-mean, A_ub=A, b_ub=b, bounds=[(None, None)] * (k + 1), method="highs")
        rG = linprog(mean, A_ub=-A, b_ub=-b, bounds=[(None, None)] * (k + 1), method="highs")
        resB[k] = -rB.fun / EF if rB.status == 0 else float("nan")
        resG[k] = math.log(1 / rG.fun) if rG.status == 0 and rG.fun > 0 else float("nan")
    return EF, resB, resG


if __name__ == "__main__":
    n = 40
    for P in (2, 4, 6, 8):
        p = P / n
        EF, B, G = run(n, p, 24)
        L = math.log(1 / EF)
        kB = min((k for k in B if B[k] > 1e-6), default=None)
        kG = min((k for k in G if G[k] >= 0.9 * L), default=None)
        print(f"P={P} log(1/EF)={L:.4f} least k minorant>0: {kB}  least k majorant>=90%: {kG}")
        print("   k:B/EF,saving " + " ".join(f"{k}:{B[k]:.3f},{G[k]:.3f}" for k in range(0, 18)))
