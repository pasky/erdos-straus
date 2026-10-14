"""y6_dict.py — check CAP_TWO Thm 1.1/1.2 (dictionary k=1 cap-2 shots <-> W_n points, c odd; ES^[2] for c = 0 mod 4).
Usage: y6_dict.py NMAX Q1MAX ABMAX
(1) forward: every k=1 shot with odd Q1 <= Q1MAX, cap <= 2, odd n <= NMAX maps to a W_n point (a,B,c,E) with E = 3 mod 4.
(2) backward: every W_n point with a, B <= ABMAX (all divisors g = -1 mod aB of 4na^2+B^2), c odd, side conditions,
    gives an exact ES^{(y,2)} solution (exact rationals, Def 1.1) with den z = c^2 B^4; c = 0 mod 4 gives den z = B^2."""
import sys
from fractions import Fraction
from math import gcd
from sympy import factorint, divisors

NMAX, Q1MAX, ABMAX = map(int, sys.argv[1:4])
def sqf(x): return all(v == 1 for v in factorint(x).values())
def check_solution(n, Q, g, capmax):
    assert (n + 4*Q*Q) % g == 0 and g % 4 == 3 and gcd(Q, n) == 1
    m = (n + 4*Q*Q)//g; assert (n+m) % 4 == 0
    x = (n+m)//4; y = n*(g+1)//4; z = Fraction(n*x*(g+1), 4*Q*Q)
    assert Fraction(4, n) == Fraction(1, x) + Fraction(1, y) + 1/z
    q2 = z.denominator; q = int(round(q2**0.5)); assert q*q == q2 and q % 2 == 1 and gcd(q, n) == 1
    for l, v in factorint(q).items():
        assert y % l == 0 and v <= capmax
    return q
fw = 0; bw = {0: 0, 1: 0}; parity_bad = 0
for n in range(3, NMAX+1, 2):
    for Q1 in range(1, Q1MAX+1, 2):
        if gcd(Q1, n) != 1: continue
        f = factorint(Q1)
        if f and max(f.values()) > 2: continue
        c = 1; B = 1
        for l, v in f.items():
            if v == 1: c *= l
            else: B *= l
        for g in divisors(4*n + Q1*Q1):
            if g % 4 != 3 or ((g+1)//4) % (c*B): continue
            Q0 = (g+1)//4; Q = Q0*Q1
            if gcd(Q, n) != 1: continue
            a = 4*Q0//(c*B); assert a % 4 == 0 and g == c*a*B - 1
            E, r = divmod(4*n*a*a + B*B, g); assert r == 0 and E % 4 == 3
            assert 4*n*a*a + B*B + E == c*a*B*E
            assert check_solution(n, Q, g, 2) == c*B*B
            fw += 1
    for a in range(1, ABMAX+1):
        for B in range(1, ABMAX+1, 2):
            if gcd(B, n) != 1: continue
            N = 4*n*a*a + B*B
            for g in divisors(N):
                if (g+1) % (a*B): continue
                c = (g+1)//(a*B); E = N//g
                assert 4*n*a*a + B*B + E == c*a*B*E
                if c % 2 == 1:
                    if (E % 4 == 3) != (a % 4 == 0): parity_bad += 1
                    if a % 4 or not (sqf(c) and sqf(B) and gcd(c, B) == 1 and gcd(c*a*B, n) == 1): continue
                    Q = c*c*a*B**3//4
                    assert check_solution(n, Q, g, 2) == c*B*B; bw[1] += 1
                    # D-face (Thm 4.1): w = (4na + cB^3)/g, D = cBw - 4n = (4n + Q1^2)/g, a*D = w + cB^3, a*w = E + B^2
                    w, r = divmod(4*n*a + c*B**3, g); assert r == 0
                    D = c*B*w - 4*n; assert D > 0 and D*g == 4*n + (c*B*B)**2 and a*D == w + c*B**3 and a*w == E + B*B
                    assert D % 4 == 3 and (w*w + 4*n*B*B) % D == 0
                elif c % 4 == 0:
                    lam = c//4
                    if gcd(a, B) != 1 or gcd(lam*B, n) != 1: continue
                    Q = lam*B*B  # Q0 = lam*B, Q1 = B
                    assert check_solution(n, Q, g, 10**9) == B; bw[0] += 1
print(f"forward k=1 cap<=2 shots mapped: {fw}; backward W_n points -> solutions: c odd {bw[1]}, c=0 mod 4 {bw[0]}; parity violations {parity_bad}")
