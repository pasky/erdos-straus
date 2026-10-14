#!/usr/bin/env python3
"""R209 from-scratch check of PHASE_DIAGRAM Prop 4.1 (one axis for all caps).

For odd n, e, k, lam, odd R with gcd(R, 2kn) = 1: M = 4k*lam, g = M*R - 1, N_e = n*(2k*M^e)^2 + 1.
Check  g | 4k^2 n + R^(2e)  <=>  g | N_e, and in that case the datum Q = lam*R^(e+1) is an exact shot with
overflow R^e and den z = R^(2e) (when gcd(lam*R, n) = 1); verified via the explicit solution.
"""
import sys
from fractions import Fraction as F
from math import gcd, log
from review_pd_wall import shot_solution, classify

nmax, kmax, Rmax, emax = map(int, sys.argv[1:5])
tests = shots = 0
for n in range(3, nmax + 1, 2):
    for e in range(emax + 1):
        for k in range(1, kmax + 1):
            for lam in range(1, kmax + 1):
                M = 4 * k * lam
                Ne = n * (2 * k * M ** e) ** 2 + 1
                for R in range(1, Rmax + 1, 2):
                    if gcd(R, 2 * k * n) != 1:
                        continue
                    g = M * R - 1
                    lhs = (4 * k * k * n + R ** (2 * e)) % g == 0
                    rhs = Ne % g == 0
                    assert lhs == rhs, (n, e, k, lam, R)
                    tests += 1
                    if lhs and gcd(lam * R, n) == 1:
                        Q = lam * R ** (e + 1)
                        Q0, Q1, kk = classify(n, Q, g)
                        assert (Q0, Q1, kk) == (lam * R, R ** e, k), (n, e, k, lam, R)
                        x, y, z = shot_solution(n, Q, g)
                        assert z.denominator == R ** (2 * e)
                        if R > 1:
                            assert y % R == 0
                        shots += 1
print(f"Prop 4.1: {tests} equivalence tests, {shots} shots verified (n<={nmax}, k,lam<={kmax}, R<={Rmax}, e<={emax})")
# quoted example: n = 13, e = 1, k = 5, lam = 2, R = 3
n, e, k, lam, R = 13, 1, 5, 2, 3
M = 4 * k * lam; g = M * R - 1; Ne = n * (2 * k * M ** e) ** 2 + 1
print("example: g =", g, "N_e/g =", F(Ne, g), "D =", F(4 * k * k * n + R ** 2, g))
# theta: log M / log N_e for lam = 1 and large k
for e in range(4):
    k = 10 ** 6
    M = 4 * k; Ne = 13 * (2 * k * M ** e) ** 2 + 1
    print(f"e={e}: log M/log N_e at k=1e6, lam=1: {log(M)/log(Ne):.4f}  (1/(2e+2) = {1/(2*e+2):.4f})")
