# y7 (O215): ET-shaped Type I / Type II solutions at odd squares n = k^2 (gcd(k, 2M) = 1).
# Type II: M a b d = n + e, e | a + b.   Type I: M a b d = n e + 1, e | a + b.
# Bound: a + b <= ab + 1 <= N + 1 with N = abd, so e <= N + 1; for Type II N=(n+e)/M => e <= (n+M)/(M-1).
# Type I: N=(ne+1)/M, e | a+b <= N+1: no a priori bound on e from this; we scan e <= EMAX.
import sys
from math import gcd
def divs(x):
    r=[];i=1
    while i*i<=x:
        if x%i==0: r+=[i,x//i] if i*i!=x else [i]
        i+=1
    return r
def hit(N,e):
    for a in divs(N):
        for b in divs(N//a):
            if (a+b)%e==0: return (a,b)
    return None
M=int(sys.argv[1]); K=int(sys.argv[2]); EMAX=int(sys.argv[3])
cntI=cntII=0; sq=0; exI=exII=None
for k in range(3,K+1,2):
    if gcd(k,2*M)>1: continue
    n=k*k; sq+=1
    fII=any((n+e)%M==0 and hit((n+e)//M,e) for e in range(1,(n+M)//(M-1)+1))
    fI=any((n*e+1)%M==0 and hit((n*e+1)//M,e) for e in range(1,EMAX+1))
    cntII+=fII; cntI+=fI
    if fII and exII is None: exII=n
    if fI and exI is None: exI=n
print(f"M={M}: odd squares k<= {K}: {sq}; with Type II: {cntII} (first {exII}); with Type I (e<= {EMAX}): {cntI} (first {exI})")
