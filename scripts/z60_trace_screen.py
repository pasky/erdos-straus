# Screens / positivity analysis for the Gamma(4C) trace identity (Theorem 2 of Z60_TRACE.md).
# usage: z60_trace_screen.py C k MODE arg   MODE=range nmax  |  MODE=list n1,n2,...
# Output TSV: n type ES TRIV E Tr X thr fires normTr identity_ok
import sys
from fractions import Fraction
from math import isqrt
sys.path.insert(0, __file__.rsplit('/',1)[0])
from z60_trace_identity import spectral, geom_pieces, pari
def mu(Q):
    r=Fraction(Q**3,2); q=Q; d=2
    while d*d<=q:
        if q%d==0:
            r*=Fraction(d*d-1,d*d)
            while q%d==0: q//=d
        d+=1
    if q>1: r*=Fraction(q*q-1,q*q)
    return r
C=int(sys.argv[1]); k=int(sys.argv[2]); mode=sys.argv[3]
assert k%2==1 and k>=3
ns = list(range(1,int(sys.argv[4])+1)) if mode=='range' else [int(x) for x in sys.argv[4].split(',')]
Q=4*C; m=mu(Q)
tot, dim = spectral(C, k, 4*C*max(ns)+1)
print(f"# C={C} k={k} dim={dim} mu={m} cusps={m/Q}")
print("n\ttype\tES\tTRIV\tE\tTr\tX\tthr\tfires\tnormTr\tid_ok")
for n in ns:
    N=4*C*n+1
    E,ES,TR=geom_pieces(C,n,k)
    Tr=Fraction(str(tot[N]))*(-1)**k
    S=Fraction(0); r=isqrt(N)
    if r*r==N:
        for lam in (r,-r):
            if (lam+1)%Q==0: S+=Fraction(k-1,12)*m*Fraction(lam)**(k-2)
    ok = (Tr == -m*E - m/(2*Q)*(ES-TR) + S)
    X = TR - 2*Q*E + (2*Q/m)*S
    tauN=sum(1 for d in range(1,isqrt(N)+1) if N%d==0)*2 - (1 if r*r==N else 0)
    D = dim*tauN*Fraction(N)**((k-1)//2)
    thr=(2*Q/m)*D
    rr=isqrt(n); typ='SQ' if rr*rr==n else ('P' if pari.isprime(n) else 'C')
    print(f"{n}\t{typ}\t{ES}\t{TR}\t{float(E):.6g}\t{Tr}\t{float(X):.6g}\t{float(thr):.6g}\t{int(X>thr)}\t{float(Tr/D) if D else 0:.4f}\t{int(ok)}")
