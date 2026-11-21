"""Large e AND f in Q: group c,d pairs, count class divisors of F²+4c²d."""
from z77_routes import *

def qlarge(n,E,T):
    # For F<=n, f<=F+2, f>=T and e>=E. Dyadic bins j=0,1,...
    bins=[];t=T
    while t<=n+2:
        h=min(2*t-1,n+2);bins.append((t,h,(n+h)**2//(4*(t*E-1))));t=h+1
    if not bins:return 0
    U=max(u for t,h,u in bins); V=n*n+4*U
    tb=min(ceildiv(rootup(V,k)*B,Q) for k in range(3,13) for A,B,Q in [tau_major(k)])
    edges=[1]
    while edges[-1]<=U:edges.append(edges[-1]*2)
    ans=0
    for C in edges:
        if C*C>U:break
        for D in edges:
            if C*C*D>U:break
            wc=min(C,isqrt(U//D)-C+1);wd=min(D,U//(C*C)-D+1)
            s=4*C*D;v=hi4(V);ct=0
            for t,h,u in bins:
                if C*C*D<=u:ct+=cap(v,lo4(t),1+(h-t)//s)
            ans+=2*wc*wd*min(tb,ct)
    return ans

if __name__=='__main__':
    import sys
    # contiguous cells in r with exact cutoffs lower at A^2, F upper at B^3
    a=int(sys.argv[1]);end=int(sys.argv[2]);J=int(sys.argv[3]);
    while a<=end:
        b=min(end,a+max(0,a//24));
        print(a,b,*(qlarge(b**3,a*a<<j,a*a<<l) for j in range(J+1) for l in range(J+1)),flush=True)
        a=b+1
