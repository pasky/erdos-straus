"""pd_theta.py — check the 'nX^2 + 1' dictionary of PHASE_DIAGRAM.md §4.
For odd n <= NMAX, e in {0,1,2,3}, k, lam <= KL: every divisor g ≡ -1 (mod 4 k lam) of N = n (2k (4k lam)^e)^2 + 1 with
R = (g+1)/(4 k lam) odd and gcd(R, 2kn) = 1 is a shot g | 4k^2 n + R^(2e) with Q = lam R^(e+1), overflow R^e;
verify the ES solution exactly and den z = R^(2e) (when gcd(Q, n) = 1). Conversely, for R <= RMAX, check
g | 4k^2 n + R^(2e) <=> g | N for g = 4 k lam R - 1. Usage: pd_theta.py NMAX KL RMAX"""
import sys
from fractions import Fraction
from math import gcd
from sympy import divisors
NMAX, KL, RMAX = map(int, sys.argv[1:4])
cnt = {0: 0, 1: 0, 2: 0, 3: 0}; bad = {0: 0, 1: 0, 2: 0, 3: 0}; conv = 0
for n in range(3, NMAX + 1, 2):
    for e in range(4):
        for k in range(1, KL + 1):
            for lam in range(1, KL + 1):
                M = 4 * k * lam
                X = 2 * k * M**e
                N = n * X * X + 1
                if e <= 2:
                    for g in divisors(N):
                        if (g + 1) % M: continue
                        R = (g + 1) // M
                        if R % 2 == 0 or gcd(R, 2 * k * n) != 1: continue
                        assert (4 * k * k * n + R**(2 * e)) % g == 0
                        Q = lam * R**(e + 1)
                        assert (n + 4 * Q * Q) % g == 0
                        m = (n + 4 * Q * Q) // g; x = (n + m) // 4; y = n * (g + 1) // 4
                        z = Fraction(n * x * (g + 1), 4 * Q * Q)
                        assert (n + m) % 4 == 0 and Fraction(4, n) == Fraction(1, x) + Fraction(1, y) + 1 / z
                        if gcd(Q, n) == 1: assert z.denominator == R**(2 * e), (n, e, k, lam, g)
                        if gcd(Q, n) == 1: cnt[e] += 1
                        else: bad[e] += 1
                for R in range(1, RMAX + 1, 2):
                    if gcd(R, 2 * k * n) != 1: continue
                    g = M * R - 1
                    assert ((4 * k * k * n + R**(2 * e)) % g == 0) == (N % g == 0)
                    conv += 1
print("shots (gcd(Q,n)=1) by e:", cnt, " solutions with gcd(Q,n)>1 (not shots):", bad, " converse checks:", conv)
