"""Signed locus of the *even* 2-power-character tower vs positive locus.
Two integer-only finite engines, no ET. See EXTREME §8 for finiteness.
"""
from fractions import Fraction
from math import isqrt

def divisors(s):
    return sorted({v for j in range(1,isqrt(s)+1) if s%j==0 for v in (j,s//j)})
def factor(n,k):
    sets=[set() for _ in range(3)]
    for x in range(1,3*n//k+1): # least POSITIVE denominator
        a=k*x-n;b=n*x
        assert a
        for d in divisors(b*b):
            for h in (d,-d):
                y,r=divmod(h+b,a);z,r2=divmod(b*b//h+b,a)
                if r or r2 or not y*z or 0<y<x or 0<z<x:continue
                t=tuple(sorted((x,y,z)));sets[sum(u<0 for u in t)].add(t)
    return sets

def direct(n,k):
    sets=[set() for _ in range(3)]
    for x in range(1,3*n//k+1):
        a=k*x-n;b=n*x
        # With |y|<=|z|, |1/y+1/z|<=2/|y| irrespective of signs.
        Y=2*b//abs(a)
        for y in range(-Y,Y+1):
            if y==0 or 0<y<x or a*y==b:continue
            z,r=divmod(b*y,a*y-b)
            if r or z==0 or 0<z<x:continue
            t=tuple(sorted((x,y,z)));sets[sum(u<0 for u in t)].add(t)
    return sets
for k,n in [(8,131),(8,241),(4,131),(4,241)]:
    s=factor(n,k);assert s==direct(n,k);print(k,n,[(len(rows),min(rows,key=lambda t:(max(map(abs,t)),t))) if rows else (0,None) for rows in s]);assert all(sum(Fraction(1,x) for x in t)==Fraction(k,n) for rows in s for t in rows)
