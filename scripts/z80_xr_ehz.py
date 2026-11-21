"""Opus cross-review of R17_WALK (NOT a certificate): independent e- and HZ-domain P searches at x=5, r=17
(or any prime r>=17 for positive controls), factoring with sympy.factorint (rho/p-1/ECM, gmpy2 ground types)
instead of GNU factor.  Exact integer arithmetic only.
usage: uv run --offline --no-project --with sympy --with gmpy2 python -B scripts/z80_xr_ehz.py r L MODE CUT
  MODE e : every unit shift e<=CUT, all a<=b, d with abd=(N+e)/4; both orientations tested on each tuple.
  MODE HZ: both orientations; every H,Z>=1 with H*Z<=CUT, a | (B Z - q H)/p, b=(U H - p a)/q, d=floor(N/4ab)+1.
Prints HIT lines and a summary 'xr r L MODE CUT keys hits'.
"""
import sys
from math import isqrt
from sympy import factorint
r,L,mode,CUT=int(sys.argv[1]),int(sys.argv[2]),sys.argv[3],int(sys.argv[4])
U=r**L;B=U//r;N=U*B;e0=466*(isqrt(U-1)+1)
def divisors(n):
    ds=[1]
    for P,k in factorint(n).items():
        ds=[d*P**j for d in ds for j in range(k+1)]
    assert all(n%d==0 for d in ds[:50])
    return ds
def check(p,q,a,b,d):
    if a<1 or d<1 or a>b:return None
    e=4*a*b*d-N
    if e<1 or e>e0 or (a+b)%e:return None
    c=(a+b)//e
    if any(z%r==0 for z in (a,b,c,d,e)):return None
    if (p*a+q*b)%U:return None
    return (p,a,b,d,e)
hits=set();keys=0
if mode=='e':
    for e in range((-N)%4 or 4,CUT+1,4):
        if e%r==0:continue
        keys+=1;M=(N+e)//4;ds=sorted(divisors(M))
        for a in ds:
            if a*a>M:break
            R=M//a
            for b in ds:
                if b<a:continue
                if R%b:continue
                for p,q in ((1,5),(5,1)):
                    h=check(p,q,a,b,R//b)
                    if h:hits.add(h)
else:
    assert mode=='HZ'
    for p,q in ((1,5),(5,1)):
        for H in range(1,CUT+1):
            for Z in range(1,CUT//H+1):
                n=B*Z-q*H
                if n<=0 or n%p:continue
                keys+=1
                for a in divisors(n//p):
                    if a>U*H//(p+q):continue
                    nb=U*H-p*a
                    if nb%q:continue
                    b=nb//q;d=N//(4*a*b)+1
                    h=check(p,q,a,b,d)
                    if h:hits.add(h)
for h in sorted(hits):print('HIT',*h)
print('xr',r,L,mode,CUT,keys,len(hits),flush=True)
