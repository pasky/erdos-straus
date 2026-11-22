"""Look for a single scalar quadratic supplying primitive genus identities at three shifts.
Only a search for examples; no exhaustive nonexistence inferences. Trial division.
"""
from math import gcd,isqrt
from itertools import product
RS={1,121,169,289,361,529}
def prime(n):return n>1 and all(n%j for j in range(2,isqrt(n)+1))
def fs(n):
    out=[];r=2
    while r*r<=n:
        if n%r==0:
            out.append(r)
            while n%r==0:n//=r
        r+=1
    return out+([n] if n>1 else [])
def gap(p):
    for k in range(3,p,4):
        x=(p+k)//4; divs=[1];xx=x
        for r in fs(x):
            base=list(divs)
            while xx%r==0:
                xx//=r;base=[u*r for u in base];divs+=base
        R={v%k for u in divs for v in (u,u*p)}
        if any(k-v in R for v in R):return k
if __name__=='__main__':
    seen=set();hits=0
    for h in range(1,61):
      for a,b in product(range(-h,h+1),range(1,h+1)):
        if max(abs(a),b)!=h or gcd(a,b)!=1:continue
        u,v,w=abs(11*a*a-22*a*b-3*b*b),3*b*b+11*a*a,abs(3*b*b-6*a*b-11*a*a)
        e=gcd(gcd(u,v),w);u//=e;v//=e;w//=e
        D=(7*v*v-3*u*u)//4;C=3*(u*u-D)
        if not (0<D<2_000_000 and C and (C,D) not in seen):continue
        assert C+3*D==3*u*u and C+7*D==7*v*v and C+11*D==11*w*w
        seen.add((C,D));
        if gcd(C,D)>1:continue
        mods=fs(D);bad=any(r>2 and pow(-C%r,(r-1)//2,r)!=1 for r in mods)
        if bad:continue
        for t in range(1,40000):
            n,r=divmod(t*t+C,D)
            if r or not (1000<n<10**10 and n%840 in RS and prime(n)):continue
            if gcd(t,u*v*w)!=1:continue
            print('C D u v w t p g:',C,D,u,v,w,t,n,gap(n));hits+=1;break
        if hits>=6:break
      if hits>=6:break
