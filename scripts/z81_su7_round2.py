"""Extreme walks and the 24-class quadratic; examples are not necessary to the proofs."""
from math import gcd,isqrt
from z81_su7_walk import walk,primes_to
from z80_square_span import jac
P=[2238327841,4367159449,3153419441929,6955940568721,1590284203561]
ps=primes_to(isqrt(2*max(P))+1)
for p in P:
    u,path,t,v=walk(p,ps,20000); assert path;print('walk',p,u,path,t,v)
S={x*x%840 for x in range(1,840,2)};H={};E={}
for x in range(4,2000,4):
    n=70*x*x-38*x+1;f=2*x-1;r=x
    assert (f+1)%8==0 and n==2*x*(35*x-1)-x-(35*x-1) and jac(f,n)==-1
    if n%840 in S:H.setdefault(n%840,(x,n))
    if n%840 in S and gcd(n,840)==1 and all(n%l for l in ps if l<=isqrt(n)):
        E.setdefault(n%840,(x,n))
assert len(S)==24 and H.keys()==S and len(E)==6
print('quadratic first examples',sorted(H.items()));print('prime seeds',sorted(E.items()))
