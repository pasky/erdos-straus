"""Round-2 integer replay (stdlib). Run without -O. Data generation is separate."""
import json
from math import gcd, isqrt, lcm
from pathlib import Path

root=Path('data/z79/proth')

def tower(j):
    h=3**j; H=2**h-1
    def X(a): return (1+pow(2,a,H))**3*pow(1+pow(2,3*a,H),-1,H)%H
    for i in range(2,j+1):
        stride=3**i; d=stride//3; t=2**d; N=1+t+t*t
        A=1
        for c in range(0,h,stride):
            a=1+d+c; b=1+2*d+c
            assert gcd(a,h)==gcd(b,h)==1 and gcd(3*a,h)==gcd(3*b,h)==3
            A=A*X(a)*pow(X(b),-1,H)%H
        assert A%N==N-1 and A%(H//N)==1

for j in range(2,8): tower(j)
print('layerwise sign formula checked through h=2187')
# Anchor for the cubic-order bound: verify the target in the X-ratio group at level 5.
old=json.loads(Path('data/z78/proth/tower-6.json').read_text()); M5=2**243-1
assert old['d']==243 and old['j']==6
v=1
for a,e in old['powers'].items():
    a=int(a); assert gcd(a,243)==1 and e>=0
    x=(1+pow(2,a,M5))**3*pow(3*(1+pow(2,3*a,M5)),-1,M5)%M5
    v=v*pow(x,e,M5)%M5
assert v==729
print('level-5 X-ratio anchor: 729 verified')

# odd-order lifting seed: the listed orders are distinct primes disjoint from the support
seeds=[(7,3,1),(23,11,6),(167,83,27),(263,131,20),(383,191,67),(863,431,257),(887,443,212),(983,491,381)]
def prime(n): return n>=2 and all(n%p for p in range(2,1+isqrt(n)))
assert len(set(q for _,q,_ in seeds))==len(seeds)
assert not set(p for p,_,_ in seeds)&set(q for _,q,_ in seeds)
for p,q,b in seeds:
    assert prime(p) and prime(q) and p%5 in (2,3)
    assert pow(2,q,p)==1 and pow(2,q,p*p)!=1 and pow(2,b,p)==(-5)%p
print('8 independent odd-order prime towers: lift hypotheses checked')

# Only upper bounds on orders are needed. No trusting discrete logs, HNF or PARI.
c=json.loads((root/'intersection.json').read_text()); T=int(c['T']); O=int(c['O']); M=T//(T&-T)
P0=3825360; cover=bytearray(P0); k=4**11-1
for P,j,t,*z in json.loads((root/'period-11-3825360.json').read_text())['rows']:
    if t=='X':continue
    if t=='K':
        f,K,D,E=z; mod=4*f*K if D[2] or E[2] else 4*lcm(f,K)
    elif t=='M':mod=840
    elif t in ('D','II'):mod=z[0]
    elif t=='W':mod=8*z[0]
    else:raise ValueError(t)
    assert (mod&-mod)<=2**64
    odd=mod//(mod&-mod);assert pow(4,T,odd)==1%odd
    cover[j::P]=b'\1'*(P0//P)
miss=[j for j in range(P0) if not cover[j]]
assert miss==c['missing'] and len(miss)==28 and all(j%41580==0 for j in miss)
assert all(pow(4,T,(k<<s)+1)==1 for s in range(1,64))
z=21-2**14
assert T>0 and T%36==0 and O>0 and O%4==0 and pow(2,O,M)==1
assert gcd(z,M)==1 and gcd(z-1,gcd(M,O))==1
print('transfer intersection: all row/small powers, 28 exact misses and CRT compatibility checked')
