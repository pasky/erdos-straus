#!/usr/bin/env python3
"""R209: from-scratch checks of the explicit families/examples quoted in PHASE_DIAGRAM §0, §1, §2, §4."""
from fractions import Fraction as F
from math import gcd
from review_pd_wall import shot_solution, classify, W


def check_shot(n, Q, g):
    Q0, Q1, k = classify(n, Q, g)
    x, y, z = shot_solution(n, Q, g)
    return Q0, Q1, k, z.denominator, y


# (a) equality family n = 2 (mod 3), odd, k = 1: Q1 = (16n+1)/3, g = (64n+1)/3, Q = Q1^2
bad = 0; cnt = 0
for n in range(5, 20001, 6):  # n = 5 mod 6
    Q1 = (16 * n + 1) // 3
    g = (64 * n + 1) // 3
    Q = Q1 * Q1
    Q0, q1, k, dz, y = check_shot(n, Q, g)
    D = (4 * n + Q1 * Q1) // g
    ok = (q1 == Q1 and k == 1 and Q0 == Q1 and dz == Q1 * Q1 and y * y % dz == 0
          and D * g == 4 * n + Q1 * Q1 and D == (4 * n + 1) // 3 and F(Q1) == W(n, 1))
    cnt += 1; bad += not ok
print(f"equality family n=5 mod 6 <= 20000: {cnt} checked, failures {bad}")

# (b) second family Q1 = 4n+3, D = 3, k = 1, n = 2 mod 3
bad = 0; cnt = 0
for n in range(5, 20001, 6):
    Q1 = 4 * n + 3
    N = 4 * n + Q1 * Q1
    assert N % 3 == 0
    g = N // 3
    if g % 4 != 3:
        bad += 1; continue
    Q0 = (g + 1) // 4
    Q = Q0 * Q1
    if gcd(Q, n) != 1:
        bad += 1; continue
    a, q1, k, dz, y = check_shot(n, Q, g)
    cnt += 1
    bad += not (q1 == Q1 and k == 1 and a % Q1 == 0 and y * y % dz == 0)
print(f"family Q1=4n+3 (n=5 mod 6 <= 20000): {cnt} checked, failures {bad}")

# (c) examples
for (n, k, Q1, g) in [(3, 2, 55, 439), (29, 126, 17, 8567)]:
    Q0 = (g + 1) // (4 * k)
    print((n, k, Q1, g), check_shot(n, Q0 * Q1, g)[:4], "W=", W(n, k))
# (Y2) n = 13: 64 + 13^3 = 7*17*19, D = 7, t = 5, g = 359 | 13 + 4*25^2
n = 13
print("Y2:", 64 + n ** 3, (n + 4 * 25 ** 2) % 359, check_shot(13, 25, 359)[:4])
# Prop 3.1(b) n = 59
print("W(59,1) =", W(59, 1))
# §4 scope example n = 113, k = 1, Q0 = 15, Q1 = 75, g = 59
print("n=113:", check_shot(113, 15 * 75, 59)[:4])
# §1 R-self-review counterexamples
for (n, lam, t, b) in [(9, 1, 1, 3), (61, 1, 3, 6)]:
    m = 4 * lam * t * b - n
    print("D-face ce", (n, lam, t, b), "m=", m, "m|b+lam t^3:", (b + lam * t ** 3) % m == 0,
          "m|n t^2+4b^2:", (n * t * t + 4 * b * b) % m == 0)
