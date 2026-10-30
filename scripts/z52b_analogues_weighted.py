# weighted ES (1,1,l): 4/p = 1/x + 1/y + l/z, l prime >= 5, l does not divide z; z searched in (l p/4, Zmax*p]
import sys
from math import gcd
from sympy import primerange, divisors
N=int(sys.argv[1]); Zmax=int(sys.argv[2])
def two_term(a,b):  # a/b = 1/x+1/y ?
    g=gcd(a,b); a//=g; b//=g
    for d in divisors(b*b):
        if d>b: break
        if (d+b)%a==0 and (b*b//d+b)%a==0: return True
    return False
for l in (5,7,11):
    fails=[]
    for p in primerange(5,N):
        if p%4!=1 or p==l: continue
        ok=False
        for z in range(l*p//4+1, Zmax*p):
            if z%l==0: continue
            a=4*z-l*p; b=p*z
            if a>0 and two_term(a,b): ok=True; break
        if not ok: fails.append(p)
    print(l, len(fails), fails[:20])
