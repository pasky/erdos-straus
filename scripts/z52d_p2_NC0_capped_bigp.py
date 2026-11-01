# z52d Pass 2 NC0, item Z0949 — capped count of 4/N = 1/x+1/y+1/z solutions with shift s = 4x-N <= SMAX
# at the greedy-hard prime N = 119945383009 (A400619 record). Exact (python ints), all divisors of B^2 with d<=B.
import sys, time
from math import gcd
from fractions import Fraction as F
from sympy import factorint, divisors
N=int(sys.argv[1]) if len(sys.argv)>1 else 119945383009
SMAX=int(sys.argv[2]) if len(sys.argv)>2 else 200
fN=factorint(N); print('N',N,'factor',fN, 'N mod 4', N%4)
sols=[]; t0=time.time(); nX=0
for x in range((N)//4+1, (N+SMAX)//4+1):
    a=4*x-N
    if a<=0 or a>SMAX: continue
    nX+=1
    b=N*x; g=gcd(a,b); A=a//g; B=b//g
    fB=dict(fN)
    for p,e in factorint(x).items(): fB[p]=fB.get(p,0)+e
    for p,e in factorint(g).items(): fB[p]-=e
    B2={p:2*e for p,e in fB.items() if e>0}
    divs=[d for d in divisors_from(B2)] if False else None
    # enumerate divisors of B^2 via exponent dict
    ds=[1]
    for p,e in B2.items():
        ds=[d*p**k for d in ds for k in range(e+1)]
    cnt=0
    for d in ds:
        if d>B or (d+B)%A: continue
        y=(d+B)//A
        if y<x: continue
        z=((B*B//d)+B)//A
        assert F(4,N)==F(1,x)+F(1,y)+F(1,z)
        sols.append((a,x,y,z)); cnt+=1
print('x-window size',nX,'time',round(time.time()-t0,1))
print('solutions with shift<=%d (unordered, x<=y<=z):'%SMAX,len(sols))
for s in sols: print('shift',s[0],'x',s[1],'y',s[2],'z',s[3],' z has factor N:', s[3]%N==0, ' y%N==0:', s[2]%N==0)
print('min shift found:', min([s[0] for s in sols]) if sols else None)
