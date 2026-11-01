# z52d P2 TO8 Z3163: for fixed n, image of positive solutions of 4xyz=n(xy+yz+zx) (i.e. 4/n=1/x+1/y+1/z) in U_n(Z/q) vs |U_n(Z/q)|
from math import gcd
from sympy import factorint
def divisors(n):
    ds=[1]
    for q,e in factorint(n).items(): ds=[d*q**k for d in ds for k in range(e+1)]
    return ds
def sols(n):
    out=[]
    for x in range(-(-n//4), (3*n)//4+1):
        a=4*x-n; b=n*x
        if a<=0: continue
        g=gcd(a,b); aa=a//g; bb=b//g
        for d in divisors(bb*bb):
            if (d+bb)%aa==0 and ((bb*bb//d)+bb)%aa==0:
                out.append((x,(d+bb)//aa,(bb*bb//d+bb)//aa))
    return out
res=[]
for n in [5,13,29,37,53,61,73,89,97,101,113,137,149,157,173,181,193,197,229,233]:
    S=sols(n)
    if len(S)<8: continue
    for q in [3,5,7,11]:
        if n%q==0: continue
        img=set((x%q,y%q,z%q) for x,y,z in S)
        U=sum(1 for x in range(q) for y in range(q) for z in range(q) if (4*x*y*z-n*(x*y+y*z+z*x))%q==0)
        res.append((n,q,len(S),len(img),U))
import collections
for q in [3,5,7,11]:
    rs=[r for r in res if r[1]==q]
    if rs: print(f"q={q}: n with >=8 solutions: {len(rs)}; mean |image|/|U_n(Z/q)| = {sum(r[3]/r[4] for r in rs)/len(rs):.3f}; max {max(r[3]/r[4] for r in rs):.3f}; examples (n,|S|,|image|,|U|):", rs[:4])
