from fractions import Fraction as F
from math import gcd
import sys
def sols(m,n):
    out=[]
    r=F(m,n)
    x0=max(1,int(1/r))
    for x in range(x0, int(3/r)+2):
        r1=r-F(1,x)
        if r1<=0: continue
        for y in range(max(x,int(1/r1)), int(2/r1)+2):
            r2=r1-F(1,y)
            if r2<=0: continue
            if r2.numerator==1 and r2.denominator>=y: out.append((x,y,r2.denominator))
    return out
m=int(sys.argv[1])
exc=[n for n in range(2,int(sys.argv[2])) if not sols(m,n)]
print('exceptions',m,exc)
# T1 test at odd squares coprime to m
for k in [5,7,11,13,17,19,23]:
    n=k*k
    if gcd(n,m)>1: continue
    S=sols(m,n); t=[]
    for s in S:
        div=[d for d in s if d%n==0]; nd=[d for d in s if d%n!=0]
        if len(div) in (1,2) and all(gcd(d,n)==1 for d in nd) and all(d%k==0 for d in div) :
            # coprimality: n coprime to non-divisible denominators
            t.append(s)
    print(n,len(S),'TypeI/II-like',len(t),t[:3])
