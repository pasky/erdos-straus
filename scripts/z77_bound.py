"""Finite box bounds. Integer arithmetic throughout; see notes/z77/R17_F3.md."""
from z76_lift import (ceildiv, rootup, major, moment, wheel, lru_cache, isqrt)
from math import gcd

@lru_cache(None)
def tau_major(k):
    U=1<<40; A=B=U
    for p in range(2,2**k):
        if any(p%i==0 for i in range(2,isqrt(p)+1)): continue
        F=mass=U; j=0
        while (j+2)**k>p*(j+1)**k:
            j+=1; V=max(F,rootup(ceildiv((U*(j+1))**k,p**j),k))
            mass+=ceildiv(V-F,p**j); F=V
        A=ceildiv(A*mass,U); B=ceildiv(B*F,U)
    return A,B,U

def tau_sum(m,H):
    return min(2*(H*(isqrt(m).bit_length()+1)+isqrt(m)),
               *(ceildiv(rootup(m,k)*(H*A+B),U) for k in range(3,13) for A,B,U in [tau_major(k)]))

@lru_cache(None)
def small(n,j):
    if not j: return 0
    t=1<<(j-1); m=(n+2*t)//4; H=ceildiv(t,4)
    z=moment(n,j)-moment(n,j-1)
    # (a <= b). For a<t fix g=ad, determines a mod e. Otherwise fix a,
    # then smaller of b,d <= sqrt(m/a); each in a specified class mod e.
    z=min(z,2*(1+2*ceildiv(isqrt(m//t),t))*tau_sum(m,H))
    return small(n,j-1)+z

if __name__=='__main__':
    import sys
    for b in map(int,sys.argv[1:]):
        n=1<<b
        v,j=min((small(n,j)+ceildiv(n,1<<j)+2,j) for j in range(1,b//2+1)); print(b,v/n**.5,j,flush=True)
