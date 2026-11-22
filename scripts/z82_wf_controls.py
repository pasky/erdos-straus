"""Direct fixed-coordinate split tests, including out-of-prime-domain controls.
Divisors of the squared residual denominator are made from the *unsquared*
inputs' factorizations (all inputs to factorint < 2^64).
"""
from math import gcd
from collections import Counter
from pathlib import Path
from sympy import factorint,isprime

def hits(n,x):
    h=gcd(4*x-n,n*x);j=(4*x-n)//h;g=n*x//h
    fn=Counter(factorint(n));fb=Counter(factorint((n+1)//2));fx=fb if x==(n+1)//2 else fn+fb
    f=fn+fx-Counter(factorint(h));ds=[1]
    assert all(isprime(l) for l in f)
    for l,e in f.items():ds=[v*l**i for v in ds for i in range(2*e+1)]
    assert max(ds)==g*g
    L=[(d+g)//j for d in ds if d<=g and (d+g)%j==0]
    for y in L:
        z,r=divmod(g*y,j*y-g);assert z>=y and not r and n*(x*y+y*z+z*x)==4*x*y*z
    return len(L),min(L,default=None)

if __name__=='__main__':
    panel=[int(s) for s in Path('data/z58/screens/star_prime_zeros.txt').read_text().splitlines() if s and s[0].isdigit()]
    for n in sorted(set(panel+[25,49,121,225,105,1465,3865,4545,10305,12145,39361,67425,17401609,11,17,131,241,2521,3361,21841,76441,113035442521,183783601,2238327841,4367159449,3153419441929,1590284203561,6955940568721])):
        b=(n+1)//2;print(n,'prime',int(isprime(n)),'4/n x=b',hits(n,b),'x=nb',hits(n,n*b))
