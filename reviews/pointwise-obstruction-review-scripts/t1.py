import sys; sys.path.insert(0,__import__('os').path.dirname(__file__))
from gp import *
from sympy import isprime
import itertools
P=[p for p in range(5,int(sys.argv[1])) if p%4==1 and isprime(p)]
bad=defaultdict(int)
for p in P:
    t=(p-1)//4
    V=all_vertices(p)
    inc=defaultdict(list)
    for v in V:
        for z in set(v): inc[z].append(v)
    # sanity: every vertex has positive denominator <=3p/4 -> enumerated. cross-check fibre consistency
    for z,L in inc.items():
        if set(L)!=fibre(p,z): bad['fibre-consistency']+=1
    pos=lambda v: all(x>0 for x in v)
    sig=tuple(sorted((t,-2*p*t,-2*p*t)))
    assert sig in V
    for v in V:
        vals=[vp(x,p) for x in v]
        nd=sum(1 for e in vals if e>0)
        if nd not in (1,2) or max(vals)>1: bad['val']+=1
        # equal-valuation pair
        if nd==1: A,B=[x for x in v if x%p]
        else: A,B=[x//p for x in v if x%p==0]
        if pos(v)!=(legendre(A*B,p)==-1): bad['BL']+=1
        # anchor
        pf=[x for x in v if x%p]
        if not any(1<=x<=2*t for x in pf): bad['anchor']+=1
        if nd==2 and not (1<=pf[0]<=2*t): bad['anchorII']+=1
        # labels
        for x in v:
            if x%p==0:
                m=x//p; lam=(4*m-1)%p
                if (nd==1)!=(lam==0): bad['label']+=1
        if len(set(v))<3 and v not in (sig,tuple(sorted((2*t,2*t,-p*t)))): bad['repeat']+=1
    for z,L in inc.items():
        if z%p:
            if (z<0 or z>2*t) and len(L)>1: bad['outer']+=1
        else:
            m=z//p
            if (4*m-1)%p:  # TypeII bucket
                if len(L)>2: bad['typeII>2']+=1
                if len({pos(v) for v in L})>1: bad['typeIImix']+=1
                if abs(m)>=2*t:
                    for v in L:
                        others=[x//p for x in v if x%p==0]
                        others.remove(m) if others.count(m)>=1 else None
                        n=others[0] if others else m
                        if not (-2*t<=n<=2*t): bad['typeIIrange']+=1
        if len({pos(v) for v in L})>1:
            ok = (z%p and t<z<=2*t) or (z%p==0 and (4*(z//p)-1)%p==0 and z>0)
            if not ok: bad['crossing']+=1
    # x+z<=6t claim in outer proof case 2t<z<p
    for v in V:
        if sum(1 for x in v if x%p==0)==1:
            pf=[x for x in v if x%p]
            for z in pf:
                x=[y for y in pf if y is not z][0] if pf[0]!=pf[1] else pf[0]
                if 2*t<z<p and x+z>6*t: bad['x+z>6t']+=1
    # fibre sizes of t and -pt
    from sympy import divisor_count
    tau=divisor_count(t*t)
    if len(inc[t])!=3*tau: bad['fib t']+=1
    if len(inc[-p*t])!=tau: bad['fib -pt']+=1
    # path
    for v in [(t,-t*(p+1),-p*t*(p+1)),(2*t,2*t+1,-p*t*(p+1)),(2*t,2*t,-p*t)]:
        if tuple(sorted(v)) not in V: bad['path']+=1
    # leaf lemma
    for v in V:
        pf=[x for x in v if x%p]
        if len(pf)==2 and all(1<=x<=2*t for x in pf) and v!=tuple(sorted((2*t,2*t,-p*t))): bad['leaf']+=1
print(len(P),'primes, max',P[-1], dict(bad))
