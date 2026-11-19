"""Certify the finite component by complementary-pair slice cardinalities."""
import csv
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]/'data/z72/counter_tail'
FILE=ROOT/'closed14281.csv'
P=14281

def generate():
    from z73_four_orbit import moves
    cur={(P,)*4}; seen=set(cur)
    with FILE.open('w') as f:
        w=csv.writer(f,lineterminator='\n'); w.writerow(['depth','w','x','y','z'])
        d=0
        while cur:
            for s in sorted(cur): w.writerow([d,*s])
            cur={t for s in cur for t in moves(s)}-seen
            seen|=cur; d+=1

def audit():
    from z72_counter_tail import fact_many
    sets=defaultdict(set); layers={}; graph=defaultdict(set)
    for r in csv.DictReader(FILE.open()):
        s=tuple(int(r[k]) for k in 'wxyz'); assert tuple(sorted(s))==s and s not in layers
        assert sum(Fraction(1,d) for d in s)==Fraction(4,P)
        layers[s]=int(r['depth'])
        for i,j in combinations(range(4),2):
            u=Fraction(1,s[i])+Fraction(1,s[j]); assert u.numerator>1
            key=tuple(s[k] for k in range(4) if k not in (i,j))
            sets[key].add(s)
    # There are exactly the saved states in every slice: count oriented
    # factor pairs by modular convolution without generating any neighboring quad.
    qs=sorted({x for s in layers for x in s}); fcts=dict(zip(qs,fact_many(qs)))
    for (a,b),ss in sets.items():
        left=Fraction(4,P)-Fraction(1,a)-Fraction(1,b); u,v=left.numerator,left.denominator
        # v divides product of the complementary two denominators.
        s=list(next(iter(ss)));s.remove(a);s.remove(b)
        fs={}; rem=v
        for q in fcts[s[0]].keys()|fcts[s[1]].keys():
            while rem%q==0: fs[q]=fs.get(q,0)+1; rem//=q
        assert rem==1
        rs={1%u:1}
        for q,e in fs.items():
            new=Counter()
            for i in range(2*e+1):
                m=pow(q,i,u)
                for t,n in rs.items(): new[t*m%u]+=n
            rs=new
        # (ux-v)(uy-v)=v^2; both orderings counted except x=y.
        assert rs.get((-v)%u,0)+int((2*v)%u==0)==2*len(ss)
        for s in ss: graph[s]|=ss-{s}
    cur={(P,)*4};seen=set(cur); d=0
    while cur:
        assert cur=={s for s in layers if layers[s]==d}
        cur={t for s in cur for t in graph[s]}-seen; seen|=cur; d+=1
    assert seen==layers.keys()
    print('vertices, edges, slices:',len(seen),sum(map(len,graph.values()))//2,len(sets),'first even:',min(d for s,d in layers.items() if any(x%2==0 for x in s)))

if __name__=='__main__':
    import sys
    if sys.argv[1:]==['--generate']:generate()
    audit()
