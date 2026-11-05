# z57 BFII: brute-force validation of z57_bfii_enum.c for small n.
# For prime n: # Type II solutions (x,y,z) of 4/n = 1/x+1/y+1/z (n | y, n | z, gcd(n,x)=1), ordered (y,z),
# must equal prim[n]. For all odd n <= N: tot[n] must equal #{(a,b,d,e): e | a+b, 4abd - e = n} (direct loops).
import sys, numpy as np
from fractions import Fraction
from math import gcd
def load(path):
    with open(path,'rb') as f:
        X=int(np.frombuffer(f.read(8),dtype=np.int64)[0])
        arr=np.frombuffer(f.read(),dtype=np.uint32).reshape(5,X+1)
    return X,arr
X,A=load(sys.argv[1]); tot,c1,prim,cmax,emin=A
N=int(sys.argv[2])
def isprime(n):
    if n<2: return False
    i=2
    while i*i<=n:
        if n%i==0: return False
        i+=1
    return True
bad=0
for n in range(3,N+1,2):
    # direct quadruple count
    t=0; c=0; pr=0
    for a in range(1,n+2):
        if 3*a-1>n: break
        b=1
        while 4*a*b-(a+b)<=n:
            s=a+b; d=1
            while 4*a*b*d-s<=n:
                for e in range(1,s+1):
                    if s%e==0 and 4*a*b*d-e==n:
                        t+=1; cc=s//e
                        if cc==1: c+=1
                        if gcd(gcd(a,b),cc)==1: pr+=1
                d+=1
            b+=1
    if (t,c,pr)!=(tot[n],c1[n],prim[n]): bad+=1; print("MISMATCH quad",n,(t,c,pr),(tot[n],c1[n],prim[n]))
    if isprime(n) and n<=N:
        # brute ES type II: y=n*y1, z=n*z1, 4/n - 1/x = (4x-n)/(nx) = (1/y1+1/z1)/n -> (4x-n)/x = 1/y1+1/z1
        cnt=0
        for x in range(n//4+1, n//2+1):
            r=Fraction(4*x-n,x)
            if r<=0: continue
            # 1/y1 + 1/z1 = r, y1 from ceil(1/r) to floor(2/r)... count ordered
            lo=int(1/r)+1 if Fraction(1,int(1/r) if int(1/r)>0 else 1)!=r else int(1/r)
            y1=max(1,int(1/r))
            while Fraction(1,y1)>=r: y1+=1
            while Fraction(2,y1)>=r:
                rem=r-Fraction(1,y1)
                if rem.numerator==1: cnt+= 1 if Fraction(1,y1)==rem else 2
                y1+=1
        # also x with gcd(x,n)=1 automatically (x<n)
        if cnt!=prim[n]: bad+=1; print("MISMATCH ES",n,cnt,prim[n])
print("checked odd n <=",N,"mismatches",bad)
if bad: sys.exit(1)
sq=[m*m for m in range(1,int(X**0.5)+1) if m%2==1]
print("odd squares <= X with tot>0:", [s for s in sq if tot[s]>0][:20])
