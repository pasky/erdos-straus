"""R213: verify CAP_TWO §6 explicit points and Thm 1.2 examples as genuine shots (exact rationals, Def 1.1)."""
from fractions import Fraction
from math import gcd, isqrt
from sympy import factorint
def check(n, a, B, c, E):
    W = 4*n*a*a + B*B + E == c*a*B*E
    g = c*a*B - 1; sqfB = all(e == 1 for e in factorint(B).values()); sqfc = all(e == 1 for e in factorint(c).values())
    side = a % 4 == 0 and B % 2 == 1 and c % 2 == 1 and gcd(c, B) == 1 and gcd(c*a*B, n) == 1
    Q1 = c*B*B; Q0 = c*a*B//4; Q = Q0*Q1
    m, r = divmod(n + 4*Q*Q, g); x = (n + m)//4; y = n*(g+1)//4; z = Fraction(n*x*(g+1), 4*Q*Q)
    ok = r == 0 and (n+m) % 4 == 0 and Fraction(4, n) == Fraction(1, x) + Fraction(1, y) + 1/z
    d = z.denominator; q = isqrt(d)
    radok = q*q == d and all(y % l == 0 for l in factorint(q)) and max(factorint(q).values(), default=0) <= 2 and q % 2 and gcd(q, n) == 1
    print(f"n={n} (a,B,c,E)=({a},{B},{c},{E}): W_n {W}, side {side}, B sqf {sqfB}, c sqf {sqfc}, g={g:.3e}, "
          f"4/n exact {ok}, ES^(y,2) {radok}, den z == Q1^2 {d == Q1*Q1}, E%4={E%4}")
check(379, 8207552, 1238990989, 7, 23)
check(13, 267468, 443777, 3, 11)
check(13, 32, 7, 1, 239)
check(41, 4, 1, 9, 75); check(41, 12, 3, 1, 675)
check(13, 29340, 59, 1, 29340*1 - 59**2)
