"""R176: numerical sanity of DIFF_DEEP Prop 2.3 on Ibukiyama orders O(q,r), p = 1 (24):
for 3 <= M <= MMAX (p !| M), the least nrd x, x in O ∩ B^0, with nrd x = -1 (mod M); report max of (least)/(M^2 p).
Also successive-minima proxy: lambda1*lambda2/p (Kaneko: >= 1/4) via the two smallest non-proportional vectors."""
import sys
from math import isqrt
from sympy import primerange, isprime, legendre_symbol, sqrt_mod
sys.path.insert(0,'scripts')
import importlib.util
spec=importlib.util.spec_from_file_location("canon","scripts/review_dd_canonical.py")
src=open("scripts/review_dd_canonical.py").read().split("P0,P1,BF=")[0]
ns={}; exec(src,ns); vecs=ns['vecs']
P,MMAX,CB=int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3])
worst=0; kmin=9
for p in primerange(5,P):
    if p%24!=1: continue
    q=3
    while not (isprime(q) and q%8==3 and legendre_symbol(p%q,q)==-1): q+=1
    r=sqrt_mod(-p,q)
    V=sorted(vecs(p,q,r,CB*p), key=lambda v:v[3])
    x=V[0]
    for y in V:
        if (x[1]*y[2]-x[2]*y[1],x[0]*y[2]-x[2]*y[0],x[0]*y[1]-x[1]*y[0])!=(0,0,0):
            kmin=min(kmin, x[3]*y[3]/p); break
    for M in range(3,MMAX+1):
        if M%p==0: continue
        best=min((v[3] for v in V if (v[3]+1)%M==0), default=None)
        if best is None: raise SystemExit(f"none found below {CB}p for p={p}, M={M}: enlarge CB")
        worst=max(worst,best/(M*M*p))
print(f"p=1(24)<{P}, 3<=M<={MMAX}: max (least nrd = -1 mod M)/(M^2 p) = {worst:.3f}; min lambda1*lambda2/p = {kmin:.3f}")
