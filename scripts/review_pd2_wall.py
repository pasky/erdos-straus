"""R210 from-scratch checks of PHASE_DIAGRAM Thm 2.1 via the duality face D*g = 4k^2 n + Q1^2.

(1) For odd n <= NMAX, k <= KMAX, odd Q1 <= 3*W(k), gcd(Q1, k) = 1: enumerate divisors D = -Q1^2 (mod 4k)
    of 4k^2 n + Q1^2, rebuild (Q0, g, Q) by Prop 1.3's converse, keep ES^{[2]} (Q1 | Q0), shot convention
    gcd(Q0 Q1, n) = 1 (count separately those failing it), verify the Egyptian identity exactly, and
    test Q1 <= W(k).  Also count those with Q1 <= 1.3 W(k) to compare with the author's 348 / 12.
(2) Equality family n = 2 (mod 3): Q1 = (16n+1)/3, g = (64n+1)/3, D = (4n+1)/3, and Q1 = 4n+3, D = 3.
Usage: review_pd2_wall.py NMAX KMAX FAMMAX
"""
import sys
from fractions import Fraction as F
from math import gcd
from sympy import factorint, divisors


def solution_ok(n, Q, g):
    x = F(n * (g + 1) + 4 * Q * Q, 4 * g)
    y = n * (g + 1) // 4
    z = x * y / (Q * Q)
    return x.denominator == 1 and F(4, n) == 1 / x + F(1, y) + 1 / z, z.denominator, y


def es2_from(n, k, Q1, D):
    N = 4 * k * k * n + Q1 * Q1
    g = N // D
    if (g + 1) % (4 * k):
        return None
    Q0 = (g + 1) // (4 * k)
    return g, Q0


def part1(NMAX, KMAX):
    tot = tot13 = bad = bad13 = viol = 0
    for n in range(3, NMAX + 1, 2):
        for k in range(1, KMAX + 1):
            W = F(16 * k ** 3 * n + 1, 4 * k - 1)
            for Q1 in range(1, int(3 * W) + 1, 2):
                if gcd(Q1, k) != 1:
                    continue
                N = 4 * k * k * n + Q1 * Q1
                for D in divisors(N):
                    if (D + Q1 * Q1) % (4 * k):
                        continue
                    r = es2_from(n, k, Q1, D)
                    assert r is not None  # Prop 1.3 converse says g = -1 mod 4k automatically
                    g, Q0 = r
                    if Q0 % Q1:
                        continue
                    Q = Q0 * Q1
                    in13 = Q1 <= F(13, 10) * W
                    if gcd(Q, n) != 1:
                        bad += 1
                        bad13 += in13
                        continue
                    ok, dz, y = solution_ok(n, Q, g)
                    assert ok and dz == Q1 * Q1 and (y * y) % dz == 0
                    assert gcd(Q, (g + 1) // 4) == Q0
                    tot += 1
                    tot13 += in13
                    if Q1 > W:
                        viol += 1
                        print("VIOLATION", n, k, Q1, D, g)
    print(f"part1: ES2 shots (Q1<=3W)={tot}, of which Q1<=1.3W: {tot13}; gcd(Q,n)>1 skipped: {bad} ({bad13}); violations={viol}")


def part2(FAMMAX):
    cnt = cnt2 = sqf = 0
    for n in range(5, FAMMAX + 1, 6):  # odd and = 2 mod 3
        Q1 = (16 * n + 1) // 3
        g = (64 * n + 1) // 3
        D = (4 * n + 1) // 3
        assert 3 * Q1 == 16 * n + 1 and D * g == 4 * n + Q1 * Q1 and D % 4 == 3 and g % 4 == 3
        Q0 = (g + 1) // 4
        assert Q0 == Q1 and gcd(Q1, n) == 1
        ok, dz, y = solution_ok(n, Q0 * Q1, g)
        assert ok and dz == Q1 * Q1 and Q1 == F(16 * n + 1, 3)
        cnt += 1
        sqf += all(e == 1 for e in factorint(Q1).values())
        # second family Q1 = 4n+3, D = 3
        Q1b = 4 * n + 3
        Nb = 4 * n + Q1b * Q1b
        assert Nb % 3 == 0
        gb = Nb // 3
        Q0b = (gb + 1) // 4
        assert (gb + 1) % 4 == 0 and Q0b % Q1b == 0 and gcd(Q0b * Q1b, n) == 1
        ok, dz, y = solution_ok(n, Q0b * Q1b, gb)
        assert ok and dz == Q1b * Q1b
        cnt2 += 1
    print(f"part2: equality family verified for {cnt} n (squarefree Q1: {sqf}); Q1=4n+3 family: {cnt2}")


if __name__ == "__main__":
    part1(int(sys.argv[1]), int(sys.argv[2]))
    part2(int(sys.argv[3]))
