# z52d Pass 2 NC0 — Z1114 graph covers / congruence refinement on F_p (non-isolated vertices only).
# For modulus m, residue-state graph Q_m: classes c = u mod m, with the neighbour-class multiset of each vertex.
# Covering (locally bijective, degree-preserving) <=> every vertex in a class has the same neighbour-class multiset.
# We count, for m=4 and m=8, the classes that are "clean" (uniform multiset) vs "exceptional" (non-uniform),
# and for the refinement 8 -> 4: whether each mod-4 class's uniform multiset is the sum of its mod-8 subclasses.
import sys, json
from collections import defaultdict, Counter
sys.path.insert(0,'scripts')
from z52d_p2_NC0_fp_common import fp_edges, primes14
N=int(sys.argv[1]) if len(sys.argv)>1 else 3000
stats={m:Counter() for m in (4,8)}
ref=Counter()
for p in primes14(N):
    E=fp_edges(p)
    if not E: continue
    adj=defaultdict(list)
    for u,v in E: adj[u].append(v); adj[v].append(u)
    for m in (4,8):
        cls=defaultdict(list)
        for u in adj: cls[u%m].append(tuple(sorted(Counter(w%m for w in adj[u]).items())))
        for c,L in cls.items():
            clean=len(set(L))==1
            stats[m]['classes']+=1; stats[m]['clean' if clean else 'exceptional']+=1
            if not clean: stats[m]['exc_example_p']+=0
    # refinement: mod-8 classes inside mod-4 class; is the mod-4 multiset the sum over subclasses (fibre-count consistency)?
    cls4=defaultdict(list); cls8=defaultdict(list)
    for u in adj:
        cls8[u%8].append(Counter(w%8 for w in adj[u])); cls4[u%4].append(Counter(w%4 for w in adj[u]))
    for c4 in cls4:
        # vertices of class c4 split over the 8-classes c8 ≡ c4 (mod 4); count of nbrs in each mod-4 class must agree
        sub=[c8 for c8 in cls8 if c8%4==c4]
        ok=True
        for c8 in sub:
            # per-vertex mod-4 neighbour profile of the subclass
            prof=set(tuple(sorted(Counter(w%4 for w in adj[u]).items())) for u in adj if u%8==c8)
            if len(prof)>1: ok=False
        ref['mod4 class %d consistent over mod8 refinement'%c4 if ok else 'mod4 class %d NOT consistent'%c4]+=1
for m in (4,8):
    print('m',m,dict(stats[m]))
print('refinement check (primes x mod-4 classes):',dict(ref))
json.dump({m:dict(stats[m]) for m in stats},open('data/z52b/pass2/NC0/sub/Z1114_cover.json','w'))
