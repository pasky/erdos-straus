"""Bounded exact checks for the round-2 lemmas, not tests of asymptotic inputs.
Run: ulimit -v 8000000; timeout 120 uv run python scripts/z49_i3astra_round2.py
"""
from fractions import Fraction as F
from itertools import combinations
from math import gcd, isqrt, lcm, log, prod
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'data/z49_i3astra'

def primes(n):
    return [p for p in range(2, n+1) if all(p%d for d in range(2,isqrt(p)+1))]

def vp(n,p):
    e=0
    while n%p==0:
        n//=p; e+=1
    return e

def squarefree(n):
    return all(n%(p*p) for p in primes(isqrt(n)))

# Envelope identity, exact partial conditioning probabilities, adaptive LLL certificate.
adaptive=[]
for H in (12,24,48,80):
    ps=primes(H)
    events=[]
    envelope=F()
    for u in range(3,H+1):
        for v in range(u,H+1):
            m=u*v; g=gcd(m,u+v+1)
            assert g == gcd(u,v+1)*gcd(v,u+1)
            envelope += F(g,m)
            events.append((u,v,m,g,{p:vp(m,p) for p in ps if m%p==0}))
    a={p:(2*max(e for e in range(1,100) if p**e<=H)
          if p<=log(H)**2 else 0) for p in ps}
    Q=prod(p**e for p,e in a.items()); steps=0
    while True:
        weights={p:F() for p in ps}; live=[]
        for u,v,m,g,exps in events:
            D=gcd(m,Q)
            if (u+v+1)%D: continue
            support=[p for p,e in exps.items() if e>a[p]]
            assert support  # a fully pinned event can never contain 1
            probability=F(D,m)
            assert probability<=F(g,m)
            live.append((probability,support))
            for p in support: weights[p]+=probability
        heavy=[p for p in ps if float(weights[p]) > (a[p]+1)*log(p)/(32*log(H))]
        if not heavy: break
        p=max(heavy,key=lambda p:float(weights[p])/((a[p]+1)*log(p)))
        a[p]+=1; Q*=p; steps+=1
        assert steps <= sum(2*vp(prod(range(1,H+1)),p) for p in ps)
    # These checks are exact, independent of floating-point choices of the pinning order.
    assert all(sum((weights[p] for p in supp),F())<=F(1,16) for _,supp in live)
    mass=sum((prob for prob,_ in live),F())
    assert mass<=envelope
    adaptive.append({'H':H,'steps':steps,'Q':str(Q),
                     'envelope':str(envelope),'final_mass':str(mass),
                     'max_event_neighborhood_mass':str(max(
                         (sum((weights[p] for p in supp),F()) for _,supp in live),default=F()))})

# Pair-sum structural identities in separated ranges; stream pairs, no product array.
es=[(u,v) for u in range(3,18) for v in range(5000,5101)
    if u%2 and v%2 and squarefree(u) and squarefree(v) and gcd(u,v)==1]
compatible=equal_sum=0
for (u,v),(up,vp_) in combinations(es,2):
    D=gcd(u*v,up*vp_)
    if D==1 or (u+v-up-vp_)%D: continue
    compatible+=1
    g,h,j,k=gcd(u,up),gcd(v,vp_),gcd(u,vp_),gcd(v,up)
    assert prod((g,h,j,k))==D
    assert all(gcd(x,y)==1 for x,y in combinations((g,h,j,k),2))
    aa,bb,cc,dd=u//(g*j),v//(h*k),up//(g*k),vp_//(h*j)
    assert (k*bb-j*dd)%g==0 and (j*aa-k*cc)%h==0
    assert (g*cc-h*bb)%j==0 and (g*aa-h*dd)%k==0
    assert F(1,lcm(u*v,up*vp_))==F(1,D*aa*bb*cc*dd)
    if u+v==up+vp_:
        equal_sum+=1
        assert u!=up and D<=u*up*abs(u-up)<=17**3<min(v,vp_)
    else:
        assert D<=abs(u+v-up-vp_)
    assert D<=4*max(v,vp_)

# Compatible divisor cluster survives pinning n=1 at small primes.
qs=[11,17,23,29,41]
P=prod(qs); H=P
Q=prod(p**(2*max(e for e in range(1,100) if p**e<=H)) for p in (2,3,5,7))
divs=[prod(qs[i] for i in range(len(qs)) if bits>>i&1) for bits in range(1<<len(qs))]
vs=[d for d in divs if d>=3 and d%3==2]
n=1+Q*((-4*pow(Q,-1,P))%P)
if n<3*H*H: n+=((3*H*H-n+Q*P-1)//(Q*P))*(Q*P)
assert n%Q==1 and (n+3)%P==0
for v in vs:
    assert (n+3+v)%(3*v)==0
    t=(n+3+v)//(3*v)
    assert t>=3 and 3*t*v-3-v==n

# Direct multiplier atoms and their fibre means. Finite sizes test the algebra only.
K=4; X=200; lower=6; upper=40; modulus=lcm(*range(1,K+1))
atoms=[]
for q in primes(X):
    if q<=50: continue
    for k in range(1,K+1):
        for u in range(lower,upper+1):
            if (k*q+1)%u or (k*q+1)//u<3: continue
            n=4*K*X+((-u-4*K*X)%(k*q))
            t,v=(k*q+1)//u,(n+u)//(k*q)
            assert min(t,u,v)>=3 and t*u*v-u-v==n
            atoms.append((k,q,u))
means=[]
for c in range(modulus):
    active=[(k,q,u) for k,q,u in atoms if (c+u)%k==0]
    assert all(gcd(c,k)==1 for k,q,u in active)
    for q in set(q for _,q,_ in active):
        residues=[(-u)%q for k,qq,u in active if qq==q]
        assert len(residues)==len(set(residues))
    means.append(sum((F(1,q) for k,q,u in active),F()))
assert sum(means,F())/modulus == sum((F(1,k*q) for k,q,u in atoms),F())

# Reuse the independent first-round census for the Vaughan-map counterexample.
zeros={int(r.split()[1]) for r in (OUT/'census.txt').read_text().splitlines() if r.startswith('ZERO ')}
assert 6336 in zeros and 42 in zeros and 21 not in zeros
n,a,b,w,q,s=6336,3,5,3,179,177
assert q+1==4*a*b*w and n*b+a==q*s
assert b*n==(4*b*w)*a*s-a-s
assert F(4,n)==F(1,s*a*w)+F(1,n*s*b*w)+F(1,n*a*b*w)

report={'adaptive':adaptive,'pair_family_size':len(es),
        'compatible_dependent_pairs':compatible,'equal_sum_pairs':equal_sum,
        'cluster':{'rough_primes':qs,'P':P,'events':len(vs),'all_survive_small_pinning':True},
        'multiplier_atoms':len(atoms),'fibre_mean_identity':True,
        'Vaughan_counterexample':6336}
(OUT/'round2_checks.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
