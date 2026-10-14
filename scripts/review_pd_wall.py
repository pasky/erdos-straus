#!/usr/bin/env python3
"""R209 from-scratch check of PHASE_DIAGRAM Thm 2.1 (k-wall, band) and Prop 1.1.

Independent of scripts/pd_*.  Shot definition used (GROWING_MUTE / EXPONENT_CAP):
  n odd, Q >= 1, gcd(Q, n) = 1, g = 3 mod 4, g | n + 4Q^2; K = (g+1)/4, Q0 = gcd(Q, K), Q1 = Q/Q0, k = K/Q0.
Solution: y = n(g+1)/4, x from 4 g x = n(g+1) + 4Q^2, z := 1/(4/n - 1/x - 1/y) (exact Fraction).
ES^{[2]}: den z | y^2.

Mode A (direct, no duality used): for a = Q0 and Q1 | a, k: test (4ak-1) | n + 4 a^2 Q1^2.
  a-bound: gcd(g, 2a) = 1 and 4ak = 1 (mod g) => g | 4k^2 n + Q1^2 (derived by hand), so 4ak-1 <= 4k^2 n + Q1^2.
Mode B (band): for every odd Q1 <= QM, k <= KF*Q1^2, all divisors g = -1 (mod 4kQ1) of 4k^2 n + Q1^2.
"""
import sys
from fractions import Fraction as F
from math import gcd
from sympy import divisors


def shot_solution(n, Q, g):
    assert g % 4 == 3 and (n + 4 * Q * Q) % g == 0 and gcd(Q, n) == 1
    num = n * (g + 1) + 4 * Q * Q
    assert num % (4 * g) == 0
    x = num // (4 * g)
    y = n * (g + 1) // 4
    z = 1 / (F(4, n) - F(1, x) - F(1, y))
    assert z > 0 and F(4, n) == F(1, x) + F(1, y) + 1 / z
    return x, y, z


def classify(n, Q, g):
    K = (g + 1) // 4
    Q0 = gcd(Q, K)
    return Q0, Q // Q0, K // Q0


def W(n, k):
    return F(16 * k ** 3 * n + 1, 4 * k - 1)


def modeA(nmax, kmax, fac):
    cnt = 0; worst = F(0); viol = []
    for n in range(3, nmax + 1, 2):
        for k in range(1, kmax + 1):
            Wk = W(n, k)
            for Q1 in range(1, int(fac * Wk) + 1, 2):
                if gcd(Q1, k) != 1 or gcd(Q1, n) != 1:
                    continue
                amax = (4 * k * k * n + Q1 * Q1 + 1) // (4 * k)
                for a in range(Q1, amax + 1, Q1):
                    g = 4 * a * k - 1
                    Q = a * Q1
                    if gcd(Q, n) != 1 or (n + 4 * Q * Q) % g:
                        continue
                    Q0, q1, kk = classify(n, Q, g)
                    assert (Q0, q1, kk) == (a, Q1, k)
                    x, y, z = shot_solution(n, Q, g)
                    dz = z.denominator
                    assert y * y % dz == 0, (n, Q, g)
                    if gcd(Q0, n) == 1:
                        assert dz == Q1 * Q1
                    # Prop 1.1 normal form
                    m = (n + 4 * Q * Q) // g
                    assert (m + n) % (4 * a) == 0
                    b = (m + n) // (4 * a)
                    assert k * (4 * a * b - n) == b + a * Q1 * Q1
                    cnt += 1
                    worst = max(worst, F(Q1) / Wk)
                    if F(Q1) > Wk:
                        viol.append((n, k, Q1, g))
    print(f"modeA n<={nmax} k<={kmax} Q1<={fac}W: shots={cnt} max Q1/W={float(worst):.4f} violations={viol[:5]}")


def modeB(nmax, QM, KF):
    cnt = 0; worstk = F(0); viol = []; lowviol = []
    for n in range(3, nmax + 1, 2):
        for Q1 in range(1, QM + 1, 2):
            if gcd(Q1, n) != 1:
                continue
            for k in range(1, int(KF * Q1 * Q1) + 1):
                if gcd(Q1, k) != 1:
                    continue
                N = 4 * k * k * n + Q1 * Q1
                mod = 4 * k * Q1
                for g in divisors(N):
                    if g % mod != mod - 1:
                        continue
                    a = (g + 1) // (4 * k)
                    Q = a * Q1
                    if gcd(Q, n) != 1:
                        continue
                    assert (n + 4 * Q * Q) % g == 0
                    Q0, q1, kk = classify(n, Q, g)
                    assert (Q0, q1, kk) == (a, Q1, k)
                    x, y, z = shot_solution(n, Q, g)
                    assert (y * y) % z.denominator == 0
                    cnt += 1
                    if F(Q1) > W(n, k):
                        viol.append((n, k, Q1, g))
                    if 2 * Q1 > n + 1:
                        worstk = max(worstk, F(k, Q1 * Q1))
                        if 2 * k >= Q1 * Q1:
                            lowviol.append((n, k, Q1, g))
    print(f"modeB n<={nmax} Q1<={QM} k<={KF}Q1^2: shots={cnt} k-wall viol={viol[:5]} "
          f"max k/Q1^2 (Q1>(n+1)/2)={float(worstk):.4f} band viol={lowviol[:5]}")


if __name__ == "__main__":
    mode = sys.argv[1]
    if mode == "A":
        modeA(int(sys.argv[2]), int(sys.argv[3]), float(sys.argv[4]))
    else:
        modeB(int(sys.argv[2]), int(sys.argv[3]), float(sys.argv[4]))
