"""O186 Prop 6.1 check: for shots (Q, g), g | n + 4Q^2, g = -1 mod 4 (all such divisors g), the Prop 2.1 solution has
z in Z iff g = -1 (mod 4Q). usage: uo_zint.py NMAX QMAX S..."""
import sys
from fractions import Fraction
from sympy import divisors
NMAX, QMAX = int(sys.argv[1]), int(sys.argv[2]); S = [int(s) for s in sys.argv[3:]]
Qs = [1]
for q in S: Qs = sorted({a*q**k for a in Qs for k in range(30) if a*q**k <= QMAX})
tot = agree = zint = 0
for n in range(5, NMAX, 2):
    if any(n % q == 0 for q in S): continue
    for Q in Qs:
        a = n + 4*Q*Q
        for g in divisors(a):
            if g % 4 != 3: continue
            e = a // g; x = (n + e)//4; z = Fraction(n*x*(g+1), 4*Q*Q)
            assert Fraction(4, n) == Fraction(1, x) + Fraction(4, n*(g+1)) + 1/z
            tot += 1; zi = z.denominator == 1; zint += zi
            agree += zi == ((g + 1) % (4*Q) == 0)
print(f"shots tested {tot}, z integral {zint}, criterion 'g = -1 mod 4Q' agrees in {agree}")
