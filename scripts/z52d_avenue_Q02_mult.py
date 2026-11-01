# Z1877: (1+1/x)(1+1/y)(1+1/z) = 1 + 4/p, complete search for x <= y <= z (unbounded y, z).
# x in ((p)/4, ...]: e = 4x - p > 0; w = e*y - p(x+1) > 0; y = (w + p(x+1))/e; z = p(x+1)(y+1)/w.
# w | K := p(x+1)(p(x+1)+e) is necessary.  x <= y <= z and (1+1/x)^3 >= 1+4/p bound x.
import sys
from sympy import divisors, primerange
def sols(p, first=True):
    out=[]
    x=p//4+1
    while (x+1)**3*p >= (p+4)*x**3:
        e=4*x-p
        if e>0:
            K=p*(x+1)*(p*(x+1)+e)
            for w in divisors(K):
                if (w+p*(x+1))%e: continue
                y=(w+p*(x+1))//e
                if y<x: continue
                num=p*(x+1)*(y+1)
                if num%w: continue
                z=num//w
                if z<y: continue
                assert (x+1)*(y+1)*(z+1)*p==(p+4)*x*y*z
                out.append((x,y,z))
                if first: return out
        x+=1
    return out
N=int(sys.argv[1])
fails=[];ok=0
for p in primerange(5,N):
    if sols(p): ok+=1
    else: fails.append(p)
print("primes 5..",N,"solvable",ok,"fail",len(fails))
print("solvable mod 4:",sorted({p%4 for p in primerange(5,N) if p not in fails}))
print("first fails",fails[:30])
print("examples", {p:sols(p) for p in [5,13,17,29] })
