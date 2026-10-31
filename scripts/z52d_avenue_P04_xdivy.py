# z52d avenue P04 / Z0860: Type I a=1 slice (Lemma 1.1 of CONDITIONAL_ES): c(fg-1) - f = n, fg = 1 mod 4,
# d = (fg-1)/4, b = (n+c)/f, solution (bdn, cd, bcd). Check: sorted x | y for every such solution,
# and every prime p = 1 mod 4 < 20000 has one (so the x|y family contains the I1 slice / X_slice).
from fractions import Fraction
from sympy import primerange
bad = 0; cnt = 0; miss = []
for p in primerange(5, 20000):
    if p % 4 != 1: continue
    found = False
    for f in range(1, p+2):
        for c in range(1, p+2):
            if (p + c + f) % (c*f): 
                if c*f > p + c + f: break
                continue
            g = (p + c + f)//(c*f)
            if (f*g) % 4 != 1: continue
            d = (f*g - 1)//4; b = (p + c)//f
            if d == 0 or b == 0: continue
            x, y, z = sorted((b*d*p, c*d, b*c*d))
            assert Fraction(1,x)+Fraction(1,y)+Fraction(1,z) == Fraction(4,p)
            cnt += 1; found = True
            if y % x: bad += 1
        if f*1 > p + 2: break
    if not found: miss.append(p)
print('I1 solutions', cnt, 'sorted x∤y', bad, 'primes without I1 solution', miss[:20])
