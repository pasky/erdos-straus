"""Opus cross-review of R17_WALK (NOT a certificate): brute-force ALL x=5 P hits at level L for prime r
(both orientations) with e <= mult*e0, e0=466 ceil(sqrt U), by sieving every M=(N+e)/4 completely.
Prints each hit with its four indices e, J, HZ, Hd so that domain searches can be checked for exact containment.
usage: python scripts/z80_xr_pbrute.py r L [mult]
"""
import sys
from math import isqrt
r,L=int(sys.argv[1]),int(sys.argv[2]);mult=int(sys.argv[3]) if len(sys.argv)>3 else 1
U=r**L;B=U//r;N=U*B;e0=466*(isqrt(U-1)+1);E=mult*e0
e1=(-N)%4 or 4
es=list(range(e1,E+1,4));M0=(N+e1)//4;n=len(es)
rem=[M0+i for i in range(n)];fac=[[] for _ in range(n)]
Mmax=M0+n-1;lim=isqrt(Mmax)+1
sieve=bytearray([1])*(lim+1);sieve[0]=sieve[1]=0
for i in range(2,isqrt(lim)+1):
    if sieve[i]:sieve[i*i::i]=bytearray(len(sieve[i*i::i]))
for P in range(2,lim+1):
    if not sieve[P]:continue
    for i in range((-M0)%P,n,P):
        k=0
        while rem[i]%P==0:rem[i]//=P;k+=1
        fac[i].append((P,k))
def divisors(f):
    ds=[1]
    for P,k in f:ds=[d*P**j for d in ds for j in range(k+1)]
    return ds
hits=[]
for i,e in enumerate(es):
    if e%r==0:continue
    f=fac[i]+([(rem[i],1)] if rem[i]>1 else []);M=M0+i;ds=sorted(divisors(f))
    for a in ds:
        if a*a>M:break
        R=M//a
        for b in ds:
            if b<a or R%b:continue
            d=R//b
            if (a+b)%e:continue
            c=(a+b)//e
            if any(z%r==0 for z in (a,b,d,c)):continue
            for p,q in ((1,5),(5,1)):
                if (p*a+q*b)%U:continue
                H=(p*a+q*b)//U;J=(4*p*a*a*d+q*e)//U;assert (4*p*a*a*d+q*e)%U==0
                # Z from eZ=r H J-(q-p) p a
                zn=r*H*J-(q-p)*p*a;assert zn%e==0;Z=zn//e
                hits.append((p,a,b,d,e,H,J,H*Z,H*d))
                print('HIT',r,L,p,a,b,d,e,'J',J,'HZ',H*Z,'Hd',H*d,'beyond_e0' if e>e0 else '',flush=True)
print('brute',r,L,'e0',e0,'E',E,'hits',len(hits),flush=True)
