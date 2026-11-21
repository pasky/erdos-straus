"""Exact-prime Q competition for the both-large region: count allowable d,
then bound the f progression on each actual d-range and shift band."""
from math import isqrt
from z77_routes import hi4,lo4,cap,edges
from z76_lift import rootup
from pathlib import Path
from functools import lru_cache
@lru_cache(None)
def large(r,k,E,T):
    n=r**k;bins=[];t=T
    while t<=n+2:
        h=min(2*t-1,n+2);bins.append((t,h,(n+h)**2//(4*(t*E-1))));t=h+1
    if not bins:return 0
    U=max(v for t,h,v in bins);es=edges(U);pref=[0]
    for d in range(r):pref.append(pref[-1]+(pow(-d,(r-1)//2,r)==r-1))
    def count(d):return (d//r)*pref[-1]+pref[d%r]
    out=0
    for C,G in zip(es,es[1:]):
        if C*C>U:break
        for D,V in zip(es,es[1:]):
            if C*C*D>U:break
            for t,h,u in bins:
                if C*C*D>u:continue
                c=min(G-1,isqrt(u//D));d=min(V-1,u//(C*C));wd=count(d+1)-count(D)
                if wd:out+=2*(c-C+1)*wd*cap(hi4(n*n+4*u),lo4(t),1+(h-t)//(4*C*D))
    return out
if __name__=='__main__':
    import sys
    for l in open(sys.argv[1]):
        r,*v=map(int,l.split());m=len(v)//2;n=r**5;t=rootup(n,3)**2
        print(r,min(v[j]+2*v[m+i]+large(r,5,t<<j,t<<i) for j in range(m) for i in range(m)),flush=True)
