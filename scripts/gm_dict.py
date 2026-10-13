"""gm_dict.py — check the (A,B) dictionary of GROWING_MUTE.md §1.

Claim (Prop 1.1): for odd n, A even, B odd, gcd(A,B)=1, gcd(B,n)=1 and a divisor g of nA^2+B^2 with
g ≡ -1 (mod 2AB): k=A/2, Q0=(g+1)/(4k), Q=Q0*B gives a shot g | n+4Q^2, and the Prop 2.1 solution
x=(n+m)/4, y=n(g+1)/4, z=n x (g+1)/(4Q^2) has den(z)=B^2 (B | Q0), so den(z) | y^2.
Conversely every shot (Q,g) with Q | K^2 (K=(g+1)/4), Q odd, gcd(Q,n)=1 arises this way.
Usage: gm_dict.py NMAX ABMAX QMAX
"""
import sys
from fractions import Fraction
from math import gcd
from sympy import divisors

NMAX, ABMAX, QMAX = map(int, sys.argv[1:4])

def solution(n, Q, g):
    N = n + 4 * Q * Q
    assert N % g == 0
    m = N // g
    assert (n + m) % 4 == 0
    x = (n + m) // 4
    y = n * (g + 1) // 4
    z = Fraction(n * x * (g + 1), 4 * Q * Q)
    assert Fraction(4, n) == Fraction(1, x) + Fraction(1, y) + 1 / z
    return x, y, z

fwd = 0
for n in range(3, NMAX + 1, 2):
    for A in range(2, ABMAX + 1, 2):
        for B in range(1, ABMAX + 1, 2):
            if gcd(A, B) != 1 or gcd(B, n) != 1:
                continue
            M = 2 * A * B
            for g in divisors(n * A * A + B * B):
                if (g + 1) % M:
                    continue
                k = A // 2
                Q0 = (g + 1) // (4 * k)
                assert Q0 % B == 0
                Q = Q0 * B
                x, y, z = solution(n, Q, g)
                assert z.denominator == B * B, (n, A, B, g, z)
                assert (y * y) % z.denominator == 0
                fwd += 1

# converse: shots with Q | K^2
bwd = 0
for n in range(3, NMAX + 1, 2):
    for Q in range(1, QMAX + 1, 2):
        if gcd(Q, n) != 1:
            continue
        for g in divisors(n + 4 * Q * Q):
            if g % 4 != 3:
                continue
            K = (g + 1) // 4
            if (K * K) % Q:
                continue
            Q0 = gcd(Q, K)
            Q1 = Q // Q0
            k = K // Q0
            A, B = 2 * k, Q1
            assert Q0 % Q1 == 0 and gcd(A, B) == 1
            assert (n * A * A + B * B) % g == 0 and (g + 1) % (2 * A * B) == 0
            x, y, z = solution(n, Q, g)
            assert z.denominator == B * B
            bwd += 1
print(f"forward (A,B) certificates checked: {fwd}; shots with Q | K^2 checked: {bwd}; all OK")
