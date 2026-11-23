"""Outward weighted norm-lattice switch: state is (pin count, sum of lower
bin edges, last lower edge). No floating signs. All exponents use 1/G.
"""
from fractions import Fraction as Q
from functools import lru_cache
import z82_gap11_r2_cert as z
S=z.S; G=4000; step=4; K=2666 # lattice .6665, fixed slack below 2/3
N=1000;cap=200;V=[S]*(cap*N+1)
for i in range(N,cap*N):
    V[i+1]=V[i]+V[i-N]*(i-N)*z.sq(i-N,i+1)//(2*(i+1)**2*S)

def lower(t,b):
    x=1-b/t;y=Q(z.sq(x.numerator,x.denominator),S)
    a=t*Q(31415927,10000000)
    return int(S*2*sum(y**(2*j+1)/(2*j+1) for j in range(15))/Q(z.sq(a.numerator,a.denominator)+1,S))

@lru_cache(None)
def base(C,R):
    j=min(cap*N,C*N//(2*max(1,R)))
    return z.ceildiv(3*(z.sq(31415927,10000000)+1)*2*G*S*S,4*C*z.sq(C,2*G)*V[j])

@lru_cache(None)
def node(k,s,i):
    # k pins. Upper cost as a coefficient of their marginal mass. At least
    # 4-k more bad primes >= last pin; omitted previous pins are distinct.
    if s+(4-k)*i>G:return 0
    C=min(2*i,K-s-k*step)
    if C<=0:return 10**9*S # invalid state; never used as finite bound
    R=G-s-(4-k)*i; u=base(C,R)
    if k==4:return u
    top=(G-s)//(4-k)
    if K-s-k*step-top-2*step<=0:return u
    alt=0
    for j in range(i,top+1,step):
        alt+=z.ceildiv(step*node(k+1,s+j,j),2*j)
        if alt>=u:return u
    return alt

def total(b):
    i=int(b*G);assert Q(i,G)==b and i%step==0
    # No terminal without first pin. Least bad <= X^(1/4).
    return sum(z.ceildiv(step*node(1,j,j),2*j) for j in range(i,G//4+1,step))
if __name__=='__main__':
    cs=[(Q(i,1000),total(Q(i,1000))) for i in range(90,205,2)]
    for ti in range(130,206,5):
        t=Q(ti,1000); m,b,c=max((lower(t,b)-c,b,c) for b,c in cs if b<t)
        print(t,b,lower(t,b),c,m,flush=True)
