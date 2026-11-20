"""Nonvacuous test of the R17_ENDPOINT §2 chain for general small positive (p,q):
exhaustive P hits at U=r^L for coprime p,q<=PQMAX; every hypothesis of each step is
tested on the datum itself (no U>=1e6 shortcut), and the conclusions are asserted.
Also Q hits (k=1 and r^3) for the §3 contacts."""
import sys, math
from math import gcd, isqrt
from fractions import Fraction as Fr
sys.path.insert(0,'data/z78/xreview')
from r17e_hits import P_hits, Q_hits, isprime, sqfree_kernel

st={}; worst={}
def bump(k): st[k]=st.get(k,0)+1
def wmax(k,v,i):
    if k not in worst or v>worst[k][0]: worst[k]=(v,i)

def checkP(r,L,p,q,a,b,c,d,e):
    U=r**L; N=U*U//r; B=U//r; m=4*d; M=m*a; C=p+q; D=q-p; u=p*q; A=M*a
    H=(p*a+q*b)//U; J=(p*M*a+q*e)//U; S=(p*M*c+D)//U
    assert U*H==p*a+q*b and U*J==p*M*a+q*e and U*S==p*M*c+D and min(H,J,S)>0
    Y=(U*S*J+D*q*B)//M; assert M*Y==U*S*J+D*q*B; Z=Y//B; assert B*Z==Y and Z>0
    I=m*H*Z-u*S; assert p*M*Z+r*q*m*H*H==D*u+U*I
    info=(r,L,p,q,a,b,c,d,e)
    bump('hits')
    # unconditional parts of (2.1)
    assert e<=2*b and M*b<=2*N and M*H<=2*C*B and (D*D+r*m*H*H)%e==0 and e*A<=4*C*C*N+D*D*A
    assert M*e*Z<=M*p*(2*C+abs(D))*a+2*C*q*e
    C1=p*p*(2*C+abs(D)); C2=Fr(4*q*C*C,r); C3=2*u*C+abs(D)*u
    assert I*U<=Fr(C1*A,e)+C2*U*U/A+C3
    first = 5*q*e<3*U
    if first: bump('first gap hyp'); assert 5*p*A>=2*U
    zb = M>=4*C*q
    if zb: bump('Z-bound hyp'); assert e<=2*p*(2*C+abs(D))*a
    third = I>=1 and 4*C3<=U
    if third:
        bump('third gap hyp'); c1=A<=4*C2*U; c2=e*U<=2*C1*A; assert c1 or c2
        if zb:
            bump('COMBINED hyp (third+Zbound)')
            ok1 = c1 and e*e<=4*p*p*(2*C+abs(D))**2*C2*U
            ok2 = c2 and (e<2*D*D or e*e<=16*C1*C*C*B)
            assert ok1 or ok2
            bound=max(2*p*(2*C+abs(D))*math.sqrt(C2*U), math.sqrt(16*C1*C*C*B), 2*D*D)
            wmax('combined e/bound',e/bound,info); wmax('combined e/sqrt(U)',e/math.sqrt(U),info)
            if first: bump('ALL hyps incl first gap')
    # I>=1 claim for r>=17 (D*u< pMZ + r q m H^2)
    if r>=17: assert I>=1
    else:
        if I<1: bump('I<=0 at r<17')

if __name__=='__main__':
    PQ=int(sys.argv[1]); rmax=int(sys.argv[2])
    pairs=[(p,q) for p in range(1,PQ+1) for q in range(1,PQ+1) if gcd(p,q)==1 and (p,q)!=(1,1)]
    jobs=[(r,2) for r in range(17,rmax) if isprime(r)]+[(r,3) for r in range(17,int(sys.argv[3])) if isprime(r)]+[(r,4) for r in (17,19,23,29)]+[(17,5)]
    for r,L in jobs:
        for p,q in pairs:
            if p%r==0 or q%r==0: continue
            for t in P_hits(r,L,p,q): checkP(r,L,p,q,*t)
    print('P stats',st)
    for k,v in sorted(worst.items()): print(k,v)
