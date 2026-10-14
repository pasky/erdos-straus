"""R213: check CAP_TWO Thm 4.1 Example (c,w)=(1,1): D = 3 mod 4, D | 64n^3+1, B = 4n+D, a = (1+B^3)/D.
Report cases where B squarefree but gcd(a, n) > 1 (side condition omitted in the example's 'iff')."""
import sys
from math import gcd
from fractions import Fraction
from sympy import factorint, divisors
N = int(sys.argv[1]) if len(sys.argv) > 1 else 400
bad = []; good = 0
for n in range(3, N + 1, 2):
    for D in divisors(64 * n**3 + 1):
        if D % 4 != 3: continue
        B = 4 * n + D
        assert gcd(B, n) == 1
        a, r = divmod(1 + B**3, D); assert r == 0 and a % 4 == 0
        g = a * B - 1; Q1 = B * B; assert D * g == 4 * n + Q1 * Q1
        sqf = all(e == 1 for e in factorint(B).values())
        if not sqf: continue
        if gcd(a, n) > 1: bad.append((n, D, B, a, gcd(a, n)))
        else:
            good += 1
            if n == 13 and D == 7:
                Q = (g + 1) // 4 * Q1; m = (n + 4 * Q * Q) // g; x = (n + m) // 4; y = n * (g + 1) // 4
                z = Fraction(n * x * (g + 1), 4 * Q * Q)
                print("n=13,D=7: g =", g, "a =", a, "den z =", z.denominator, "== B^4", z.denominator == B**4,
                      "4/n ok", Fraction(4, n) == Fraction(1, x) + Fraction(1, y) + 1 / z, "y%B", y % B)
print("valid:", good, " B squarefree but gcd(a,n)>1:", len(bad), bad[:8])
from sympy import isprime
print("prime n among bad:", [t for t in bad if isprime(t[0])][:8], sum(isprime(t[0]) for t in bad))
