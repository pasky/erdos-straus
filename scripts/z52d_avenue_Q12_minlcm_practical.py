# Z0707: is minlcm(p)/p always practical? (all ES solutions, p prime <= PMAX)
from math import gcd
from sympy import primerange, factorint
def practical(m):
    if m==1: return True
    f=sorted(factorint(m).items()); s=1
    for q,e in f:
        if q> s+1: return False
        s*= (q**(e+1)-1)//(q-1)
    return True
def lcm(a,b): return a*b//gcd(a,b)
PMAX=1200; bad=[]; n=0
for p in primerange(5,PMAX):
    best=None
    for x in range(p//4+1, 3*p//4+1):
        num=4*x-p; den=p*x  # 1/y+1/z = num/den
        if num<=0: continue
        for y in range(max(x,den//num+1), 2*den//num+1):
            zn=den*y; zd=num*y-den
            if zd>0 and zn%zd==0:
                z=zn//zd; L=lcm(lcm(x,y),z)
                if best is None or L<best: best=L
    m=best//p; n+=1
    if not practical(m): bad.append((p,m,factorint(m)))
print("primes",n,"non-practical minlcm/p:",len(bad)); print(bad[:15])
