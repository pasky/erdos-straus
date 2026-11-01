# Z0954: min over all solutions of 4/p = 1/x+1/y+1/z (x<=y<=z) of z/x, at primes p ≡ 1 (4)
from sympy import factorint, primerange, divisors
from math import gcd
res=[]
for p in primerange(5,2500):
    if p%4!=1: continue
    best=None
    for x in range(p//4+1, 3*p//4+2):
        a=4*x-p; b=p*x
        if a<=0: continue
        g=gcd(a,b); a//=g; b//=g
        # (a y - b)(a z - b) = b^2, d1 <= d2, d1 ≡ -b mod a
        for d1 in divisors(b*b):
            if d1*d1> b*b: break
            if (d1+b)%a: continue
            d2=b*b//d1
            if (d2+b)%a: continue
            y=(d1+b)//a; z=(d2+b)//a
            if y<x: continue
            r=z/x
            if best is None or r<best[0]: best=(r,x,y,z)
    res.append((p,best))
import math
worst=min(b[0]/p for p,b in res)
print("min over p of (min z/x)/p =", worst)
print("min over p of (min z/x)/p^(1/2) =", min(b[0]/math.sqrt(p) for p,b in res))
for p,b in res[:8]+res[-5:]: print(p, round(b[0],2), b[1:], round(b[0]/p,3))
