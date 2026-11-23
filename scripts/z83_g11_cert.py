"""Outward integer certificates; replay needs the z82 published-in-repo tables.
Options: bv (~47 MB for two int64 grids), pair, complete, thin, example. No args: all.
The mixed Selberg denominator bound in the note uses only a first moment.
"""
import sys
from fractions import Fraction as Q
from math import gcd,isqrt
from array import array
import z82_gap11_r2_cert as z
S=z.S

def switch(a,b,tu):
    A=z.sq(a.numerator,a.denominator)+1
    H2=z.Hhi[2][z.ceildiv(z.N*a.denominator,a.numerator)]
    # rational upper, dimensions normalized as in z82 U0(a,b)
    return Q(z.up(z.up(z.Au,A),2*H2),S)/(tu-b)

def layers(a,b,tau,low):
    u=z.ceildiv(b.denominator*z.N,b.numerator)
    h=sum(v[u] for j,v in z.Hhi.items() if j>=low)
    r=a*b*2/tau
    return Q(3,2)*Q(z.Eu,S)*2/tau*Q(z.sq(r.numerator,r.denominator)+1,S)*Q(h,S)

def bv():
    G=4000;I=1453;B=280
    lo,_,j=z.arraytable(B,G,I)
    a,b,t=Q(I,G),Q(B,G),Q(j,G)
    L=Q(z.down(z.sq(I,B),lo[I]),S)
    c3=switch(a,b,t);c6=layers(a,b,t,6);c4=layers(a,b,t,4)
    for name,x in [('L',L),('C3',c3),('C7(>=6)',c6),('net',L-c3-c6),('C7(>=4)',c4)]:
        print(name, (x*S).__floor__(),(x*S).__ceil__())
    assert L-c3-c6>Q(1,10000)

def pair():
    G=2000;I=814;B=180;J=1158
    # arraytable's g parameter only sets its final residual-level index.
    lo,_,j=z.arraytable(B,2*(J+1),I);assert j==J
    a,b,t=Q(I,G),Q(B,G),Q(999,G)
    L=Q(z.down(z.sq(I,B),lo[I]),S)
    c3=switch(a,b,t);c4=layers(a,b,t,4)
    print('pair: tau, lower, C3, C7>=4, net (floors in scaled units)', Q(j,G),*[int(x*S) for x in (L,c3,c4,L-c3-c4)])
    assert L-c3-c4>Q(1,1000)

def thin():
    t,b,pan=Q(4548,10000),Q(433,1000),Q(49975,100000)
    # asinh sqrt(t/b-1) = atanh sqrt(1-b/t); all Taylor terms positive.
    r=1-b/t;x=Q(z.sq(r.numerator,r.denominator),S)
    rt=Q(z.sq(t.numerator,t.denominator)+1,S)
    l=4*sum(x**(2*j+1)/(2*j+1) for j in range(10))/(rt*Q(31415927,10000000))
    k=2/pan;h=Q(z.Hhi[2][z.ceildiv(z.N*b.denominator,b.numerator)],S)
    c=Q(3,2)*k*Q(z.sq(k.numerator,k.denominator)+1,S)*h
    print('thin: tau, b, lower, cost, margin (1e-12 bounds):',t,b,int(S*l),(S*c).__ceil__(),int(S*(l-c)))
    assert l-c>Q(1,2500)

def example():
    M=840*29*19; t=1+M; n=t*t+2520; l,r=1481,144646721
    assert n==l*r and all(all(v%d for d in range(2,isqrt(v)+1)) for v in (l,r))
    for q,y in ((3,29),(7,19)):
        u=(t-y)//2
        assert gcd(u,y)==1 and 4*(u*u+u*y+((q+1)//4)*y*y)==n+q
    x=(n+3)//4; s=x*n; Y=s*(l+1)//3; Z=(s//l)*(l+1)//3
    assert 4*x*Y*Z==n*(Y*Z+x*Z+x*Y) and x<min(Y,Z)
    print('primitive norms but composite hits 3:', n,l,r,'sorted triple',x,min(Y,Z),max(Y,Z))

def complete():
    # Exponent mesh 1/G: C = remaining level, R = remaining log-size,
    # W = upper exponent of largest remaining good prime. V rounds down.
    G=100000;N=1000;cap=300; V=array('q',[S])*(cap*N+1)
    for i in range(N,cap*N):V[i+1]=V[i]+V[i-N]*(i-N)//(2*(i+1)**2)
    def charge(C,W):
        assert C>0 and W>0
        j=min(cap*N,C*N//(2*W))
        return z.ceildiv(2*G*S*S,C*V[j])
    # At a first bad t >= .35, C/2 < t for all descendants. Test candidate
    # w (remaining good-prime cutoff) fractions of the capacity; terms
    # with pinned primes each pay their upper endpoint exponent. Rounding
    # at each endpoint is conservative. No floating quadrature in signs.
    from functools import lru_cache
    @lru_cache(150000)
    def peel(C,R,W,depth):
        W=min(R,W)
        U=charge(C,W)
        if depth==0 or W<20:return U
        d=max(1,W//40);cost=0; hi=W
        while hi>d:
            lo=hi-d
            cost+=z.ceildiv((hi-lo)*peel(C-hi,R-lo,hi,depth-1),2*lo)
            U=min(U,charge(C,lo)+cost);hi=lo
        return U
    tau=95430;st=35000;cost=0;ordinary=0
    for i in range(st,G//2,5):
        C=tau-i-5;R=G-2*i
        u=peel(C,R,R,2)
        cost+=z.ceildiv(5*u,i);ordinary+=z.ceildiv(5*charge(C,R),i)
    l=int(2*S*G*z.loglo(Q(tau,st)-1)/tau)
    print('two peels: tau, L, old cost, new cost, net (scaled):',Q(tau,G),l,ordinary,cost,l-cost)
    assert l-cost>S//10000

if __name__=='__main__':
    for test in (bv,pair,complete,thin,example):
        if len(sys.argv)==1 or test.__name__ in sys.argv:test()
