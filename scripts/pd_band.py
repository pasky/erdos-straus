"""pd_band.py — check the double wall (band) for ES^[2] shots, PHASE_DIAGRAM.md §2.

For odd n <= NMAX, k <= KMAX and every odd B (= overflow Q1) up to BFAC x the claimed wall
W(k) = (16 k^3 n + 1)/(4k - 1), list all divisors g of 4k^2 n + B^2 with g ≡ -1 (mod 4kB)
(GROWING_MUTE Prop 1.1(c): ES^[2] shots with A = 2k, overflow B, gcd(B, 2kn) = 1).
Checks: (i) B <= W(k)  [dual wall]; (ii) B > (n+1)/2  =>  k < B^2/2  [Thm 2.1 case 1];
(iii) the shot solution is exact, den z = B^2, B | Q0, normal form k(4ab - n) = b + a B^2.
Reports max B/W(k) and max k/B^2 (for B > (n+1)/2).
Usage: pd_band.py NMAX KMAX BFAC
"""
import sys
from fractions import Fraction
from math import gcd
from sympy import divisors

NMAX, KMAX, BFAC = int(sys.argv[1]), int(sys.argv[2]), float(sys.argv[3])
cnt = 0; nonshot = 0; worst_wall = (0, None); worst_k = (0, None)
for n in range(3, NMAX + 1, 2):
    for k in range(1, KMAX + 1):
        W = (16 * k**3 * n + 1) / (4 * k - 1)
        Bmax = int(BFAC * W) + 2
        for B in range(1, Bmax + 1, 2):
            if gcd(B, 2 * k * n) != 1:
                continue
            N = 4 * k * k * n + B * B
            M = 4 * k * B
            for g in divisors(N):
                if (g + 1) % M:
                    continue
                Q0 = (g + 1) // (4 * k)
                Q = Q0 * B
                if gcd(Q, n) != 1:
                    nonshot += 1; continue
                cnt += 1
                assert Q0 % B == 0 and (n + 4 * Q * Q) % g == 0
                m = (n + 4 * Q * Q) // g
                x = (n + m) // 4; y = n * (g + 1) // 4
                z = Fraction(n * x * (g + 1), 4 * Q * Q)
                assert (n + m) % 4 == 0
                assert Fraction(4, n) == Fraction(1, x) + Fraction(1, y) + 1 / z
                # overflow exactly B needs gcd(B, k) = 1 (true) ; den z = B^2 when gcd(Q0, n) = 1
                if gcd(Q0, n) == 1:
                    assert z.denominator == B * B, (n, k, B, g, z)
                a = Q0; assert (m + n) % (4 * a) == 0
                b = (m + n) // (4 * a)
                assert k * (4 * a * b - n) == b + a * B * B
                r = B / W
                if r > worst_wall[0]:
                    worst_wall = (r, (n, k, B, g))
                assert B <= W, ("WALL", n, k, B, g)
                if B > (n + 1) / 2:
                    assert 2 * k < B * B, ("KWALL", n, k, B, g)
                    rk = k / B**2
                    if rk > worst_k[0]:
                        worst_k = (rk, (n, k, B, g))
print("shots (gcd(Q,n)=1)", cnt, "skipped gcd(Q,n)>1:", nonshot)
print("max B/W(k)", worst_wall)
print("max k/B^2 (B>(n+1)/2)", worst_k)
