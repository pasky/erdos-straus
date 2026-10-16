"""R260: which twisted Astra fixtures (from review_r260_fixtures output) are Claude ES^{(y,e)} points (EXPONENT_CAP Def 1.1)."""
import sys, re
from fractions import Fraction as F
from math import isqrt, gcd, prod
from sympy import factorint
for line in open(sys.argv[1]):
    m = re.match(r"\s+twisted p=(\d+) n=(\d+) \((\d+), (\d+), (\d+)\)", line)
    if not m:
        continue
    p, n, *t = map(int, m.groups())
    pt = [F(v, n * n) for v in t]
    ints = [v for v in pt if v.denominator == 1]
    rat = [v for v in pt if v.denominator != 1]
    verdict = "not ES^(y,e): " + f"{len(rat)} non-integral coords"
    if len(rat) == 1:
        d = rat[0].denominator; r = isqrt(d)
        if r * r != d: verdict = f"den {d} not square"
        elif r % 2 == 0: verdict = f"den {d}: even root"
        elif gcd(r, p) > 1: verdict = f"den {d}: root not prime to p"
        else:
            R = prod(factorint(r))
            ok = [int(y) for y in ints if int(y) % R == 0]
            verdict = (f"ES^(y,{max(factorint(r).values())}) with y={ok[0]}" if ok else f"den {d}: rad {R} divides no integral coord")
    print(f"p={p} n={n} {tuple(t)} -> {verdict}")
