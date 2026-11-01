# z52d Pass 2 NC0, item Z0093 — CM field K = Q(zeta8), K+ = Q(sqrt2), unit group rank 1 (eps=1+sqrt2, zeta8).
# Test (cheap, exact in the sense of numeric search + exact verification): are there 4/n = 1/u1+1/u2+1/u3 with all u_i UNITS of Z[zeta8]
# of the form zeta8^j * eps^k, |k|<=KMAX?  (the 'unit mechanism' of the item; non-unit denominators are NOT searched).
import sys, itertools, math
from fractions import Fraction
import sympy as sp
KMAX=int(sys.argv[1]) if len(sys.argv)>1 else 6
NMAX=int(sys.argv[2]) if len(sys.argv)>2 else 200
z=sp.exp(sp.I*sp.pi/4)
eps=1+sp.sqrt(2)
units=[]
for j in range(8):
    for k in range(-KMAX,KMAX+1):
        u=sp.nsimplify(0)
        units.append((j,k,complex(sp.N(z**j*eps**k,30))))
vals=[(j,k,v) for j,k,v in [(j,k,complex(z**j*eps**k)) for j in range(8) for k in range(-KMAX,KMAX+1)]]
recip=[(j,k,1/v) for j,k,v in vals]
hits=[]; exact_n=[]
import numpy as np
R=np.array([r for _,_,r in recip])
for n in range(2,NMAX+1):
    target=4.0/n
    # pairs (u1,u2) then check target - 1/u1 - 1/u2 equals a unit reciprocal (numerically)
    cnt=0
    for i in range(len(R)):
        for k2 in range(i,len(R)):
            rem=target-R[i]-R[k2]
            d=np.abs(R-rem)
            idx=np.where(d<1e-9)[0]
            for t in idx:
                # exact check in Q(zeta8): 4/n == 1/u1+1/u2+1/u3 (sympy, exact)
                def ex(j,k): return z**j*eps**k
                lhs=sp.Rational(4,n)
                expr=sp.simplify(sp.expand(sp.Rational(4,n)-1/ex(*recip[i][:2])-1/ex(*recip[k2][:2])-1/ex(*recip[t][:2])))
                if expr==0:
                    cnt+=1
                    if len(hits)<8: hits.append((n,recip[i][:2],recip[k2][:2],recip[t][:2]))
    if cnt: exact_n.append((n,cnt))
print('KMAX',KMAX,'units tested',len(R),'exact unit-only solutions (ordered-pair count) per n:',exact_n[:30]); print('first hits:',hits)
