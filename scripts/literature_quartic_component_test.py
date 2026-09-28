"""HKRS-style test: is the quartic symbol (AB/p)_4 of the same-valuation pair a component invariant?

uv run --no-project --with sympy python scripts/literature_quartic_component_test.py 5 6000
Buckets components by kind (seed/pos/sterile) and number of nonpositive vertices (capped at 8);
iid-null = probability that k independent +-1 values coincide. Finite evidence only."""
import sys
from collections import Counter, defaultdict
from sympy import primerange
sys.path.insert(0,'scripts')
from pointwise_incidence import incidence_solutions
from pointwise_refactor import components, seed
def vp(n,p):
    k=0
    while n%p==0: n//=p; k+=1
    return k
def q4(a,p):
    a%=p; r=pow(a,(p-1)//4,p)
    return 0 if r==1 else (2 if r==p-1 else 1)
st=defaultdict(Counter)
for p in primerange(int(sys.argv[1]),int(sys.argv[2])):
    if p%4!=1: continue
    V=incidence_solutions(p); s=seed(p)
    for C in components(V):
        kind='seed' if s in C else ('pos' if any(min(v)>0 for v in C) else 'sterile')
        vals=[]
        for v in C:
            if min(v)>0: continue
            vv=[vp(abs(u),p) for u in v]
            pr=[i for i in range(3) if vv.count(vv[i])==2]
            A=v[pr[0]]//p**vv[pr[0]]; B=v[pr[1]]//p**vv[pr[1]]
            vals.append(q4(A*B,p))
        n=len(vals)
        if n==0: continue
        b=min(n,8)
        st[(kind,b)]['const' if len(set(vals))==1 else 'mixed']+=1
for k in sorted(st):
    c=st[k]; tot=c['const']+c['mixed']
    print(k, dict(c), "const-frac %.3f"%(c['const']/tot), " iid-null %.3f"%(2*0.5**k[1] if k[1]<8 else 0))
