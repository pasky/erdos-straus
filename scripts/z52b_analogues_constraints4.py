# more constraint worlds, reusing the solver from constraints.py
import sys, json
sys.argv=[sys.argv[0]]+sys.argv[1:]
from math import gcd, isqrt
from sympy import primerange, factorint
_src=open('scripts/z52b_analogues_constraints.py').read().split('def sqfree')[0]; exec(_src.replace('N=int(sys.argv[1]) if len(sys.argv)>1 else 3000',''))
N=int(sys.argv[1])
def is_norm(n, forms):
    f=factorint(n)
    return forms(f)
def eis(f):  # x^2+xy+y^2 norms (incl. 3)
    return all(e%2==0 for q,e in f.items() if q%3==2)
def two(f):  # x^2+2y^2
    return all(e%2==0 for q,e in f.items() if q%8 in (5,7))
def sq(n): r=isqrt(n); return r*r==n
tests={
 'all Eisenstein norms': lambda s: all(eis(factorint(t)) for t in s),
 'all x^2+2y^2 norms': lambda s: all(two(factorint(t)) for t in s),
 'all den = 0 mod 3': lambda s: all(t%3==0 for t in s),
 'some den square': lambda s: any(sq(t) for t in s),
 'xyz square': lambda s: sq(s[0]*s[1]*s[2]),
 'x=y or y=z (repeat)': lambda s: s[0]==s[1] or s[1]==s[2],
 'x prime': lambda s: len(factorint(s[0]))==1 and max(factorint(s[0]).values())==1,
 'all den even, 8/p and some den = 0 mod 8': lambda s: all(t%2==0 for t in s) and any(t%8==0 for t in s),
 'denominators pairwise gcd = same g': lambda s: gcd(s[0],s[1])==gcd(s[1],s[2])==gcd(s[0],s[2]),
 'all den <= p^{3/2}': lambda s: max(s)**2<=P**3,
}
fails={k:[] for k in tests}
for P in primerange(5,N):
    if P%4!=1: continue
    S=sols(P)
    for k,f in tests.items():
        if not any(f(s) for s in S): fails[k].append(P)
json.dump(fails, open("data/z52b/analogues_constraints4_fails_%d.json"%N,"w"))
tot=sum(1 for p in primerange(5,N) if p%4==1)
for k,v in fails.items(): print(f"{k:42s} fails at {len(v):4d}/{tot}; first: {v[:10]}")
