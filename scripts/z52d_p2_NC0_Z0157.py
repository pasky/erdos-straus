# z52d Pass 2 NC0, item Z0157 — Brieskorn link Σ(x,y,z) (exponents = denominators of an ES triple) is a Z-homology sphere iff x,y,z pairwise coprime
# (Brieskorn/Milnor: H1 = 0 iff pairwise coprime). Test: are there ES triples 4/n=1/x+1/y+1/z with pairwise coprime x,y,z?
import sys, json
from math import gcd
sys.argv=sys.argv[:1]
sys.path.insert(0,'scripts')
from z52d_p2_NC0_allsols import sols
NMAX=int(__import__('os').environ.get('NMAX','400'))
tot=0; cop=[]; ex=[]
for n in range(2,NMAX+1):
    S=sols(n)
    for (x,y,z) in S:
        tot+=1
        if gcd(x,y)==1 and gcd(y,z)==1 and gcd(x,z)==1: cop.append((n,x,y,z))
    if S and len(ex)<3: ex.append((n,S[0]))
print('n<=',NMAX,'unordered solutions',tot,'pairwise coprime',len(cop))
print('examples (n,first sol):',ex)
print('first pairwise-coprime:',cop[:5])
