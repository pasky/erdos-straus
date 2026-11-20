"""Exact finite P-box bounds; see notes/z76/PROOF_LIFT.md. Run from repo root."""
from functools import lru_cache
from math import comb, isqrt
from fractions import Fraction
from pathlib import Path
from decimal import Decimal
import sys


def ceildiv(a,b): return -(-a//b)

def rootup(n,k):
    lo, hi=0,1<<ceildiv(n.bit_length(),k)
    while hi-lo>1:
        m=(lo+hi)//2
        if m**k<n: lo=m
        else: hi=m
    return hi

@lru_cache(None)
def major(k,G):
    """Upper bounds for first moment and end-effect in units of U."""
    U=1<<40
    A=B=U
    for p in range(2,3**k):
        if any(p%i==0 for i in range(2,isqrt(p)+1)): continue
        g=G; a=0
        while g%p==0: g//=p; a+=1
        F=U; mass=U; j=a
        while (2*(j-a)+3)**k>p*(2*(j-a)+1)**k:
            j+=1
            V=max(F,rootup(ceildiv((U*(2*(j-a)+1))**k,p**j),k))
            mass+=ceildiv(V-F,p**j); F=V
        A=ceildiv(A*mass,U); B=ceildiv(B*F,U)
    return A,B,U

@lru_cache(None)
def wheel(bits):
    from math import lcm
    G=1; i=2
    while lcm(G,i)<=1<<bits:
        G=lcm(G,i); i+=1
    return G

@lru_cache(None)
def moment(n,j):
    # e < 2^j; exact group e in [2^i,2^(i+1)).
    if j==0: return 0
    i=j-1; m=(n+(1<<j))//4; H=ceildiv(1<<i,4)
    arr=[]
    for bits,cost in ((i//2,1),(i,2)):
        G=wheel(bits)
        for k in range(3,8):
            A,B,U=major(k,G); arr.append(cost*ceildiv(rootup(m,k)*(H*A+B),U))
    return min(arr)+moment(n,j-1)

@lru_cache(maxsize=200000)
def divcap(mbits, sbits, zbits):
    # Fixed pair with modulus s >= 2^sbits, z in [Z,2Z), f=sz-1.
    # f >= 2^(sbits+zbits-1); M <= 2^mbits. Power-of-two partitions in z.
    ans=1<<zbits
    for w in (2,3,4,6,8,12,16):
        v=w*(w-1)//2
        for h in range(1,w):
            R=(sbits+zbits-1)*h*w-mbits*(h*(h+1)//2)
            # for interval width <= 2^l, v*l < R
            l=(R-1)//v
            if l<0: continue
            ans=min(ans,(w-1)<<max(0,zbits-l))
    return ans

@lru_cache(None)
def boxes(bits):
    # uniform for N<=2^bits. Exclude e<=2^j at end using acd <= (N/e+1)/2.
    n=1<<bits
    layers=[0]*(bits+1)
    for a in range((bits+1)//2+1):
        for d in range(bits-2*a+1):
            for c in range(bits-a-d+1):
                s=a+c+d
                bnd=min(1<<s,
                    (1<<(a+d))*divcap(bits+2,2+a+d,c), # f | N+4a²d <= 3N
                    (1<<(a+c))*divcap(bits+c+2,2+a+c,d), # f | Nc+a
                    (1<<(c+d))*divcap(bits+2*c+d+6,2+c+d,a)) # f | 4c²dN+1
                # fixed a,d: e=(N+4a²d)/f <= N/(2acd-1); e=-N mod 4ad.
                bnd=min(bnd,(1<<(a+d))*(1+(n//((2<<s)-1))//(4<<(a+d))))
                layers[s]+=bnd
    for i in range(1,len(layers)): layers[i]+=layers[i-1]
    # Ordered triples for small e already count both orientations
    return min((moment(n,j)+2*layers[bits-j-1],j) for j in range(1,bits-1))

if __name__=='__main__':
    for b in map(int,sys.argv[1:]):
        v,j=boxes(b); print(b,v,j, 'boxes/sqrtN',round(v/2**(b/2),3),flush=True)
