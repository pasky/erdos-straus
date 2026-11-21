"""z80 final sign and divisor checks; stdlib, no discovery imports, assertions on."""
from math import gcd, isqrt, lcm
from pathlib import Path
import json
D=Path(__file__).resolve().parents[1]/'data/z80/proth'

def prime(n):return n>=2 and all(n%p for p in range(2,isqrt(n)+1))
def orbit(b,n):
    v=1;V={}
    while v not in V:V[v]=len(V);v=v*b%n
    assert v==1;return V

def signs():
    for h,p in ((343,7),(529,23)):
        H=2**h-1;M=2**(h//p)-1;N=H//M;v=1
        for a,e in json.loads((D/f'r3/sign-{h}.json').read_text()).items():
            a=int(a);assert gcd(a,h)==1 and e>0;v=v*pow((1+2**a)*pow(3,-1,H),e,H)%H
        assert v==H-1
        # Construct +p itself at the primitive layer, from the square of the
        # orbit product of D's and the certified sign. D_1=1, all B's in R1.
        prod=1;d=1;t=0
        for a in orbit(2,h):
            assert d==(pow(2,a,N)-1)%N;prod=prod*d%N;t+=a;d=d*(1+pow(2,a,N))%N
        assert v*prod**2*pow(2,-t,N)%N==p
    for h in range(3,201,2):
        O=orbit(2,h);F={p for p in range(3,h+1,2) if h%p==0 and prime(p)}
        twos={len(orbit(2,p))&-len(orbit(2,p)) for p in F}
        assert ((h-1) in O)==(len(twos)==1 and 1 not in twos)
        if len(F)!=1:continue
        p=next(iter(F));o=len(O);op=len(orbit(2,p));
        if op%2==0 and op<p-1:
            a=next(a for a in range(1,p) if a not in orbit(2,p));assert pow(a,o,p)!=1
        # Norm around the primitive doubling orbit is 1 modulo the layer.
        N=(2**h-1)//(2**(h//p)-1)
        for a in range(1,h):
            v=1
            for i in O:v=v*(1+pow(2,a*i,N))%N
            assert v==1

def sieve():
    P=497943285840;B=P//(P&-P);tau=int(json.loads((D/'r2/transfer.json').read_text())['T']);assert 2*(11+tau)-1>B+1
    for m in range(1,37):
        k=4**m-1;hits=[set() for _ in range(151)]
        for q in range(3,258,2):
            if not prime(q) or k%q==0:continue
            V=orbit(2,q);j=V.get(-pow(k,-1,q)%q)
            if j is not None:
                for s in range(j,151,len(V)):hits[s].add(q)
        for s in range(151):
            n=(k<<s)+1;assert hits[s]=={q for q in range(3,258,2) if prime(q) and n%q==0}
        # Scaled F1 negative control; no word on squares.
        assert (k<<(2*m+2))+1==(2**(2*m+1)-1)**2
    # Scaled versions of the sparse obstruction: enumerate ALL raw divisor
    # choices on short odd parts before specializing the (possibly huge) 2-part.
    for m in range(3,28):
        h=2*m-1;H=2**h-1;k=2*H+1
        for b in (1,3,5,7,9):
            if 2**b+1>=H:continue
            for f in range(1,2**b+2,2):
                if (2**b+1)%f:continue
                # c*f == -1 would give k/c == -f, with k/c in [1,2H+1].
                assert all(k%c0 for c0 in (H-f,2*H-f))
if __name__=='__main__':signs();sieve();print('global 343,529 sign and primitive rational-prime products; orbit, divisor and sparse screens OK')
