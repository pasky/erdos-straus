"""O251 (LATTICE_MEETING Thm 1.4): at a slice g = 3 (4), gcd(g,p)=1, h=(g+1)/4, root rho:
  ES with y = p h (any ET d)  <=>  exists k | h with  d_k := (2 k rho)^2 mod g = (-4 k^2 p) mod g  dividing k.
Compare with the brute-force Prop 3.2 criterion: exists delta | (p h)^2, delta = -p h (mod g).
Also compare COUNTS: #Type II solutions (x,y,z) with y = p h, p !| x (unordered x,z distinct roles) vs #{k : d_k | k}.
Each criterion hit is turned into the ET solution (a,b,c,d) and checked exactly.
Usage: z23_alld.py P G
"""
import sys
from fractions import Fraction as F
from math import gcd
from sympy import primerange, divisors

P, G = int(sys.argv[1]), int(sys.argv[2])
st = dict(slices=0, es=0, mismatch=0, cnt_mismatch=0)
for p in primerange(5, P + 1):
    if p % 4 != 1:
        continue
    for g in range(3, G + 1, 4):
        if g % p == 0 or pow(-p, (g - 1) // 2, g) == g - 1 and False:
            continue
        if not any((r * r + p) % g == 0 for r in range(g)):
            continue
        st['slices'] += 1
        h = (g + 1) // 4
        hits = []
        for k in divisors(h):
            d = (-4 * k * k * p) % g
            if d and k % d == 0:
                a, c = h // k, k // d
                m = (p + 4 * a * a * d) // g
                assert (p + 4 * a * a * d) % g == 0 and (p + m) % (4 * a * d) == 0
                b = (p + m) // (4 * a * d)
                assert a + b == c * (4 * a * b * d - p)
                x, y, z = a * b * d, a * c * d * p, b * c * d * p
                assert y == p * h and F(4, p) == F(1, x) + F(1, y) + F(1, z)
                hits.append((x, z))
        ph = p * h
        sols = set()
        for de in divisors(ph * ph):
            if (de + ph) % g == 0:
                x = (ph + de) // g
                z = F(ph * x, de)
                assert F(4, p) == F(1, x) + F(1, ph) + 1 / z and z.denominator == 1
                if x % p:
                    sols.add((x, int(z)))
        st['es'] += bool(hits)
        st['mismatch'] += bool(hits) != bool(sols)
        st['cnt_mismatch'] += set(hits) != sols
print(st)
