"""Exact rational residuals/Clifford identity, independent determinant identity,
and the closed prime-factor walk beginning at the least QNR 19."""
from fractions import Fraction as F
from math import gcd,prod,isqrt
from random import Random
from itertools import combinations
from z46_brauer_twists_check import hilbert
from z81_dual_chords import points
from sympy import factorint, primerange, jacobi_symbol

def alpha(P,place):return hilbert(-F(P[0],P[2]),-F(P[1],P[2]),place)

def run(M,n):
    rng=Random(M+n); S=points(M,n); tested=positive=0
    for _ in range(420):
        P,Q=[rng.sample(rng.choice(S),3) for _ in range(2)]
        V=[b-a for a,b in zip(P,Q)]
        if 0 in V: continue
        u,v,w=V;a,b,c=P
        k=F(n*(u*v+v*w+w*u)-M*(a*v*w+b*w*u+c*u*v),M*u*v*w)-1
        if k in (0,1):continue
        R=[a+k*v for a,v in zip(P,V)]
        if 0 in R:continue
        assert sum(1/F(z) for z in R)==F(M,n)
        d=-F(M,n); J=d**3*prod(P)*prod(Q)*prod(R)
        assert J>0 and isqrt(J.numerator)**2==J.numerator and isqrt(J.denominator)**2==J.denominator
        for place in (2,3,5,7,11,13,17,'inf')+tuple(map(int,factorint(n))):
            assert prod(alpha(T,place) for T in (P,Q,R))==alpha(V,place)
        tested+=1;positive+=int(min(R)>0)
    print('chord law',M,n,tested,positive)

def trap():
    n=183783601; r=(n+19)//20
    assert all(not any(x%d==0 for d in range(2,isqrt(x)+1)) for x in (n,r))
    assert n%840==1 and r%19==2 and r%4==1
    chi=[(int(q),int(jacobi_symbol(q,n))) for q in primerange(2,20)]
    assert all(s==1 for _,s in chi[:-1]) and chi[-1]==(19,-1)
    A={j for i in (1,5) for k in range(3) for j in [i*pow(2,k,19)%19]}
    assert not any(-j%19 in A for j in A)
    print('trap',n,r,chi,sorted(A))

if __name__=='__main__':
    trap()
    for M,n in [(4,25),(4,49),(4,409),(4,577),(4,2521),(4,3361),(4,4545),(8,11),(8,17),(8,131),(8,241)]:run(M,n)
