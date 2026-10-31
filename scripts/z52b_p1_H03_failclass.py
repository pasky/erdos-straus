# Z1446: classify (p,C) level failures of (★): N = 4Cp+1 has no divisor d ≡ -1 (mod 4C).
#  (a) omega(N) <= 1;  (b) -1 not in H = <prime factors of N> in G=(Z/4C)^x  [character obstruction]
#      (b2) of which: a quadratic character suffices (-1 not in H*G^2)  vs (b3) only higher-order characters;
#  (c) -1 in H but no divisor hits -1 (bounded exponents / subset-product failure).
# Compare all primes vs the hardest primes (lowest R). p ≡ 1 (4), p < 1e5, C ≤ 100.
import json, sys
from sympy import primerange, factorint, jacobi_symbol
from math import gcd
from collections import Counter
CMAX=100; PMAX=int(sys.argv[1]) if len(sys.argv)>1 else 100000
units={C:[x for x in range(1,4*C) if gcd(x,4*C)==1] for C in range(1,CMAX+1)}
sq={C:{x*x%(4*C) for x in units[C]} for C in range(1,CMAX+1)}
def closure(gens,m):
    H={1}; fr=[1]
    while fr:
        x=fr.pop()
        for g in gens:
            y=x*g%m
            if y not in H: H.add(y); fr.append(y)
    return H
def classify(p,C):
    m=4*C; N=m*p+1; f=factorint(N)
    divs={1}
    for q,k in f.items():
        divs={d*pow(q,j,m)%m for d in divs for j in range(k+1)}
    if m-1 in divs: return 'hit'
    if sum(f.values())<=1: return 'a'
    H=closure([q%m for q in f],m)
    if m-1 not in H:
        HG2={h*s%m for h in H for s in sq[C]}
        if m-1 in HG2: return 'b3'
        # is it the Brauer–Manin character chi_{-4C}: (-C/q) = +1 for every prime q | N ?
        return 'b2BM' if all(jacobi_symbol((-C)%q,q)==1 for q in f) else 'b2oth'
    return 'c'
res={}; tot=Counter(); Rp={}
for p in primerange(5,PMAX):
    if p%4!=1: continue
    cl=[classify(p,C) for C in range(1,CMAX+1)]
    res[p]=Counter(cl)
hits={p:res[p]['hit'] for p in res}
order=sorted(res,key=lambda p:hits[p])
hard=order[:200]
def summ(ps):
    c=Counter()
    for p in ps: c.update(res[p])
    fails=sum(v for k,v in c.items() if k!='hit')
    return {k:round(c[k]/fails,3) for k in ['a','b2BM','b2oth','b3','c']}|{'fail_frac':round(fails/(len(ps)*CMAX),3)}
out=dict(nprimes=len(res),CMAX=CMAX,all=summ(res),hard200=summ(hard),hard_hits_range=[hits[hard[0]],hits[hard[-1]]],
         bigp=summ([p for p in res if p>PMAX//2]), smallp=summ([p for p in res if p<PMAX//10]))
print(json.dumps(out,indent=1)); json.dump(out,open('data/z52b/pass1/H03/failclass.json','w'),indent=1)
