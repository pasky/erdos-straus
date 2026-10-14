"""R213: Thm 1.2 first bullet. c = 4λ half of W_n -> ES^{[2]} shots (GROWING_MUTE Prop 1.1(c)), checked
directly: shot (Q = λB^2, g = caB - 1), den z = B^2, B | y. Also: which k = 1 cap-2 shots (c-odd half) are
ALSO ES^{[2]} shots (same (n, g, Q)) -> the halves overlap as SHOT sets."""
from fractions import Fraction
from math import gcd, isqrt
NMAX, GMAX = 200, 20000
def sol(n, Q, g):
    m = (n + 4*Q*Q)//g; assert (n + 4*Q*Q) % g == 0 and (n+m) % 4 == 0
    x = (n+m)//4; y = n*(g+1)//4; z = Fraction(n*x*(g+1), 4*Q*Q)
    assert Fraction(4, n) == Fraction(1, x) + Fraction(1, y) + 1/z
    return y, z
half0 = set(); bad = 0; cnt = 0
oddhalf = set()
for c in range(1, GMAX + 2):
    for B in range(1, (GMAX+1)//c + 1, 2):
        for a in range(1, (GMAX+1)//(c*B) + 1):
            g = c*a*B - 1
            if g < 3 or g % 2 == 0: continue
            n0 = (-B*B*pow(4*a*a % g, -1, g)) % g
            for n in range(n0, NMAX+1, g):
                if n < 3 or n % 2 == 0: continue
                if c % 4 == 0:
                    lam = c//4
                    if gcd(a, B) != 1 or gcd(lam*B, n) != 1: continue
                    Q = lam*B*B; cnt += 1
                    y, z = sol(n, Q, g)
                    if not (z.denominator == B*B and y % B == 0 and (g+1)//4 // gcd(Q, (g+1)//4) == a): bad += 1
                    half0.add((n, g, Q))
                elif c % 2 == 1 and a % 4 == 0 and gcd(c*a*B, n) == 1:
                    oddhalf.add((n, g, (c*a*B//4)*c*B*B, a, B, c))
print("c=0 mod 4 points:", cnt, "failures:", bad)
ov = [t for t in oddhalf if t[:3] in half0]
print("c-odd points whose shot is also an ES^[2] shot:", len(ov), sorted(ov)[:5])
