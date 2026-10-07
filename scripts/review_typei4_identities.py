"""R89 from-scratch check of POINTWISE_TYPEI4 Prop 1.2, Cor 1.4, Remark 1.6, Lemma 3.1 on brute-force
fibre certificates generated directly from the definition (TYPEI2 (2.2) + F = 7 mod 16).

For L, a (odd), b, c', X(=k') small: factor N = 1 + 2^{L+2} c' 7^{a+2b} X^2, list divisors F with
F = -1 mod c'X, F = 1 mod 7^{a+b}, F = 7 mod 16.  Then check every claimed identity.
Usage: uv run --with sympy python scripts/review_typei4_identities.py [Cmax] [Lmax]
"""
import sys
from math import gcd
from sympy import factorint, divisors

Cmax = int(sys.argv[1]) if len(sys.argv) > 1 else 45
Lmax = int(sys.argv[2]) if len(sys.argv) > 2 else 16
odd7 = [x for x in range(1, Cmax + 1, 2) if x % 7]
fails = 0
nfound = 0
bylevel = {}
for L in range(5, Lmax + 1):
    T = 2 ** (L - 4)
    for a in (1, 3, 5):
        for b in (0, 1, 2):
            s = a + 2 * b
            for cp in odd7:
                for X in odd7:
                    N = 1 + 2 ** (L + 2) * cp * 7 ** s * X * X
                    for F in divisors(N):
                        if F % 16 != 7 or (F + 1) % (cp * X) or (F - 1) % 7 ** (a + b):
                            continue
                        e = N // F
                        if F > e:
                            continue  # orient F<e; e is then also a fibre divisor (checked below)
                        nfound += 1
                        bylevel[L] = bylevel.get(L, 0) + 1
                        ok = True
                        co, ko = 7 ** a * cp, 7 ** b * X
                        n = co * ko
                        ok &= e % 16 == 7 and (e + 1) % (cp * X) == 0 and (e - 1) % 7 ** (a + b) == 0
                        ok &= (e - F) % (16 * n) == 0
                        delta = (e - F) // (16 * n)
                        ok &= delta % 2 == 1
                        M = co * delta ** 2 + T
                        d = co * M
                        A = (F + e) // 2
                        ok &= A * A - d * (8 * ko) ** 2 == 1
                        ok &= A % 32 == 31
                        # odd-part shapes
                        ok &= (A + 1) % (32 * cp * X * X) == 0 and (A - 1) % (2 * 7 ** (a + 2 * b)) == 0
                        P1 = (A + 1) // (32 * cp * X * X)
                        Q1 = (A - 1) // (2 * 7 ** (a + 2 * b))
                        ok &= P1 * Q1 == M and P1 % 7 != 0 and Q1 % 7 != 0
                        P, Q, Y = cp * P1, 7 ** a * Q1, 7 ** b
                        ok &= 16 * P * X * X - Q * Y * Y == 1 and P * Q == d
                        # Cor 1.4
                        D = 7 ** (a + b) * delta
                        g, h = 4 * P1 * X - D, 4 * P1 * X + D
                        K = T * 7 ** (a + 2 * b)
                        ok &= cp * g * h - P1 == K and g > 0
                        # Remark 1.6
                        ok &= F == 8 * cp * X * g - 1 and e == 8 * cp * X * h - 1
                        # Lemma 3.1
                        y = cp * g * delta
                        z = T * 7 ** b - y
                        ok &= 0 < y < T * 7 ** b and y % 2 == 1
                        ok &= P1 * (4 * cp * g * X - 1) == 7 ** (a + b) * z and z % P1 == 0
                        ok &= P1 == cp * g * g + 7 ** (a + b) * (2 * y - T * 7 ** b)
                        if 2 * y > T * 7 ** b:
                            ok &= 7 ** a < T / 2
                        else:
                            ok &= 4 * 7 ** a < T * T * 7 ** b
                        if not ok:
                            fails += 1
                            print("FAIL", L, a, b, cp, X, F, e)
                        else:
                            print("fibre", L, a, b, cp, X, F, e, "delta", delta, "P1", P1, "g", g)
print("found", nfound, "by level", bylevel, "fails", fails)
