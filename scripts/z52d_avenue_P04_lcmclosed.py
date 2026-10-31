# z52d avenue P04 / Z0858: check that ET Type II b=1 slice solutions (ad, acdn, cdn) are lcm-closed
# (largest denominator divisible by the other two), for primes p = 1 mod 4 < 3000.
from fractions import Fraction
from sympy import primerange
bad = 0; cnt = 0
for p in primerange(5, 3000):
    if p % 4 != 1: continue
    for e in range(1, 4*p):
        if (p + e) % 4: continue
        M = (p + e)//4               # 4ad = p + e, a = -1 mod e
        for a in range(e-1, M+1, e):
            if a == 0 or M % a: continue
            d = M//a; c = (a+1)//e
            x, y, z = a*d, a*c*d*p, c*d*p
            assert Fraction(1,x)+Fraction(1,y)+Fraction(1,z) == Fraction(4,p)
            s = sorted((x,y,z)); cnt += 1
            if s[2] % s[0] or s[2] % s[1]: bad += 1
print('b=1 solutions checked', cnt, 'non-lcm-closed', bad)
