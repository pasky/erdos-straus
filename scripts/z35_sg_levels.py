"""Spark 4: Sophie-Germain levels d = k^2.  Hit rate of the b=1 line at d=k^2 vs non-square d with (d/p)=+1 and (d/p)=-1,
d in [lo,hi].  Also: Burde-predicted identity (l/p)_4 = (p/l)_4 * ((a c - b e)/l), (p/l)_4 = (k/l) for l | p+4k^2, l=1(4)."""
import sys, math, collections; sys.path.insert(0,'scripts')
from z35_lib import *
N=int(sys.argv[1]); lo,hi=int(sys.argv[2]),int(sys.argv[3])
spf=spf_sieve(N+4*hi+10)
P=[p for p in primes_upto(N,spf) if p%4==1 and p>4*hi]
def leg(x,p):
    r=pow(x%p,(p-1)//2,p); return 0 if r==0 else (1 if r==1 else -1)
sq=set(k*k for k in range(1,int(hi**.5)+2))
st=collections.Counter(); tot=collections.Counter()
for p in P:
    for d in range(lo,hi+1):
        t=4*d; n=p+t
        h=any(w<n and w%t==t-1 for w in divisors_from(factor(n,spf)))
        cls='square' if d in sq else ('nsq,(d/p)=+1' if leg(d,p)==1 else 'nsq,(d/p)=-1')
        st[cls]+=h; tot[cls]+=1
print("primes",len(P),"<=",N,"levels",lo,"..",hi)
for c in tot: print(c, "rate %.4f  (%d trials)"%(st[c]/tot[c],tot[c]))
# Burde/SG identity check
bad=0;cnt=0
for p in P[:3000]:
    a,b=rep2(p)
    for k in range(1,12):
        for l in factor(p+4*k*k,spf):
            if l%4!=1 or k%l==0: continue
            c,e=rep2(l); cnt+=1
            pl4=1 if pow(p,(l-1)//4,l)==1 else -1
            lp4=1 if pow(l,(p-1)//4,p)==1 else -1
            if pl4!=leg(k,l): bad+=1
            if lp4!=pl4*leg(a*c-b*e,l): bad+=1
print("SG identity (p/l)_4=(k/l) and Burde on",cnt,"(p,k,l): violations",bad)
