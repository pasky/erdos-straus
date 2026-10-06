# From-scratch check of POINTWISE_MN Lemma 1.1 (review R63). Independent of mn_jacobi.py.
import sys
from sympy import factorint, jacobi_symbol, divisors, legendre_symbol
def sqfree(n):
    r=1
    for p,e in factorint(n).items():
        if e%2: r*=p
    return r
def run(m, T):
    bad=0; vals=set(); natoms=0; sqc=0
    for A in range(1, (T+1)//m+1):
        M=m*A-1
        if M<3 or M%2==0: continue
        fM=factorint(M)
        for D in divisors(A*A):
            natoms+=1
            c=(-m*D)%M
            J=jacobi_symbol(c,M); vals.add(J)
            e=sqfree(m*D); t=1 if e%2==0 else 0; eo=e>>t
            # (a)
            for l in fM:
                if legendre_symbol(c%l,l)!=legendre_symbol((-e)%l,l): bad+=1
            s2=jacobi_symbol(2,M)
            pred = -(s2**t) if M%4==3 else (s2**t)*(-1)**((eo-1)//2)
            if pred!=J: bad+=1
    return natoms,bad,vals
T=int(sys.argv[1])
for m in map(int,sys.argv[2:]):
    n,b,v=run(m,T); print(m, "atoms",n,"fail",b,"symbols",sorted(v), "m%4",m%4)
