"""H_k family: actual affine triples from z80 ET verification or direct enumeration.
Use --with cypari2 offline. Small excess output includes all hitting weights with
numerator and denominator <=B, not an extrapolation to untabulated inputs.
"""
from fractions import Fraction as F
from itertools import permutations
from math import isqrt
from sympy import isprime, jacobi_symbol
from z81_dual_chords import points
from z80_extreme_et import count
from z46_brauer_twists_check import hilbert
from sys import argv

def pts(p):
    C=count(p);R=[]
    for i,T in enumerate(C):
        for a,b,c,d in T:
            U,V=a*c*d,b*c*d; X=(a*b if i else a*c)*d
            L=(X,p*U,p*V) if i else (U,V,p*a*b*d)
            assert sum(F(1,z) for z in L)==F(4,p)
            R.append(tuple(sorted(L)))
    return set(R)

def audit(n,B=100):
    D=(n*n-1)//4;L=n+2;h=(n+1)//2;prime=isprime(n)
    if prime:
        s=next(i*L-1 for i in range(1,20000) if isprime(i*L-1) and jacobi_symbol(1-i*L,n)==-1)
    else:
        s=next(i*L-1 for i in range(1,20000) if isprime(i*L-1) and (i*L-1)%n)
    def Pk(k):
        m=n*h;Z=F(k*m+1,L);return (h,m*Z,Z/k)
    Q=Pk(s);A=(n-1)//2;P=(A,h,-n*D)
    assert sum(F(1,z) for z in Q)==F(4,n) and Q[0]+Q[1]-s*Q[2]==P[0]+P[1]-s*P[2]
    assert Q[1].denominator==1 and Q[2].denominator==s and min(Q)>0
    if prime: assert hilbert(-F(Q[0],Q[2]),-F(Q[1],Q[2]),n)==-1
    # Holding projective weights/parameter fixed for 8/n divides the entire
    # affine plane by 2. Neither consecutive signed seed can stay integral.
    assert sum(1/(F(z)/2) for z in P)==F(8,n) and any(F(z,2).denominator!=1 for z in P)
    assert sum(1/(F(z)/2) for z in Q)==F(8,n)
    N=4+s*(n*n-1); H=(s*n*n+4)*(s*n**4+16)
    rank2=(isqrt(N)**2!=N and isqrt(H)**2!=H and s>2 and n%s!=0)
    ES=N**2+(2*s-4)*N+s*s+4*s; EB=-16*s*N
    assert ES*ES-4*EB==s*(s*n*n+4)**2*(s*n**4+16)
    assert F(32,n*n)+ES-F(8*(N+s),n*n)==s*n*n*(s*n*n+4)
    assert F(32,n*n)+ES+F(8*(N+s),n*n)==F(H,n*n)
    S=pts(n) if prime else {t for t in points(4,n) if min(t)>0}
    if n<=4000:assert S=={t for t in points(4,n) if min(t)>0}
    good=[]
    for v in S:
        for x,y,z in permutations(v):
            if x>y or x+y<=n:continue
            k=F(x+y-n,z+n*D); assert x+y-k*z==n*(1+k*D)
            good.append((max(k.numerator,k.denominator),k,(x,y,z)))
    print('family',n,'s',s,'den(z)',Q[2].denominator,'rank2 test',rank2,'#triples',len(S),'#integral-k',sum(k.denominator==1 for _,k,_ in good),'#height<=',B,sum(H<=B for H,_,_ in good),'min by height',min(good,default=None),flush=True)

if __name__=='__main__':
    for n in map(int,argv[1:]):audit(n)
