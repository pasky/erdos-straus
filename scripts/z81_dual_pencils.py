"""Local Brauer obstruction for shared small-weight sums. Complete sum matching
on finite samples; the unbounded obstruction itself only uses the reduction mod p.
"""
from itertools import permutations,combinations_with_replacement
from fractions import Fraction as F
from math import gcd,prod,lcm
from sympy import factorint
from z46_brauer_twists_check import hilbert
from z81_dual_chords import points

def weighted_test(p):
    a,b=(p-1)//2,(p+1)//2; D=a*b; w=(1,1,-1); N=p*p+3
    P=(a,b,-p*D); s0=sum(z*a for z,a in zip(P,w))
    assert 4*s0==p*N
    Q=[F(p*s0,4*z*a) for z,a in zip(P,w)]
    assert min(Q)>0 and sum(1/z for z in Q)==F(4,p) and sum(z*a for z,a in zip(Q,w))==s0
    assert lcm(*(v.denominator for v in Q))==p*p-1
    X=-p*p*N;Y=p*N*(N+1);A=N*N-2*N+5; B=-16*N
    assert Y*Y==X*(X*X+A*X+B)
    lam=F(3*X*X+2*A*X+B,2*Y); assert lam**2-A-2*X==F((p**4-p*p+4)**2,4*p*p)
    # At odd primes outside 2p, the derived directional character formula applies
    # to *all* positive rational points, in particular Q.
    k=lcm(*(z.denominator for z in Q))
    for ell,d in factorint(k).items():
        if ell in (2,p):continue
        low=[i for i,z in enumerate(Q) if z.denominator%(ell**d)==0]
        assert len(low)==2
        nonsplit=ell%4==3 and d%2 and w[low[0]]!=w[low[1]]
        assert hilbert(-Q[0]/Q[2],-Q[1]/Q[2],int(ell))==(-1 if nonsplit else 1)
    return k

def screen(p):
    S=points(4,p); pos={s for P in S if min(P)>0 for s in permutations(P)};neg={s for P in S if min(P)<0 for s in permutations(P)}
    weights=[w for w in combinations_with_replacement(range(1,6),3) if gcd(*w)==1 and prod(w)%p and all(pow(w[0]*a,(p-1)//2,p)==1 for a in w[1:])]
    weights=[(1,1,-1)]+weights
    nlocal=nmatch=0;example=None
    for w in weights:
        signs=[sum(x*y for x,y in zip(w,P))%p for P in pos]
        assert 0 not in signs
        sP={sum(x*y for x,y in zip(w,P)) for P in pos};sQ={sum(x*y for x,y in zip(w,P)) for P in neg}
        hits=sP&sQ
        if hits:nmatch+=1;example=(w,min(hits))
        for P in neg:
            if sum(x*y for x,y in zip(w,P))%p==0:nlocal+=1
    print('pencil',p,'jump denominator',weighted_test(p),'#weights',len(weights),'signed sums zero mod p',nlocal,'weights with an exact cross-sign common sum',nmatch,'example',example,flush=True)

if __name__=='__main__':
    for p in [13,17,241,409,577,2521,3361,5569,9601]:screen(p)
