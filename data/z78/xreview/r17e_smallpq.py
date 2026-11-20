"""For every stored r=17 P tuple (data/m17b p1..p13, data/z17 p15), find ALL positive coprime
(p,q) with U | pa+qb and 4*C3<=U (the hypothesis of the R17_ENDPOINT third gap), then run the
fully hypothesis-checked chain of r17e_generic.checkP. This yields nonvacuous tests of the
combined (2.2) dichotomy at deep levels with genuine tuples."""
import sys, gzip
from math import gcd, isqrt
from pathlib import Path
sys.path.insert(0,'data/z78/xreview')
import r17e_generic as G

r=17
for K in range(1,16,2):
    L=(K+1)//2; U=r**L
    fn=Path(f'data/m17b/p{K}.txt') if K<15 else Path('data/z17/p15_r17.txt.gz')
    rows=[tuple(map(int,l.split())) for l in (gzip.open(fn,'rt') if K==15 else fn.open()) if l.strip()]
    for a,b,c,d in rows:
        e=(a+b)//c
        if (a*b*c*d*e)%r: pass
        else: continue
        rho=(-a*pow(b,-1,U))%U
        # 4*C3 = 4*(2uC+|D|u) >= 8pq(p+q) >= 8 p q^2 /... ; so p*q*(p+q) <= U/8 needed
        pmax=1
        while 8*pmax*(pmax+1)<=U: pmax+=1   # q>=1 => 8p(p+1)<=U necessary
        for p in range(1,pmax+1):
            q=rho*p%U
            if q==0 or gcd(p,q)>1: continue
            C=p+q; D=q-p; u=p*q
            if 4*(2*u*C+abs(D)*u)>U: continue
            G.checkP(r,L,p,q,a,b,c,d,e)
print('stats',G.st)
for k,v in sorted(G.worst.items()): print(k,v)
