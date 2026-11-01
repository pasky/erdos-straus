"""Complete seeded components of a bounded elementary split/merge graph.
Seeds: (n,n,n,n) and every ordered ES triple with largest term <=D.
Never claim to enumerate components containing neither kind of seed.
"""
from collections import deque,Counter
from fractions import Fraction
from functools import lru_cache
from pathlib import Path
import json,time,sys
D=int(sys.argv[1]) if len(sys.argv)>1 else 1000000
L=int(sys.argv[2]) if len(sys.argv)>2 else 10
N=int(sys.argv[3]) if len(sys.argv)>3 else 100

def triples(n):
 out=[]
 for x in range(n//4+1,3*n//4+1):
  a=4*x-n;b=n*x
  for y in range(max(x,b//a+1),min(D,2*b//a)+1):
   t=a*y-b
   if b*y%t==0:
    z=b*y//t
    if y<=z<=D:out.append((x,y,z))
 return out

def neighbors(s):
 out=set();k=len(s)
 if k<L:
  for i,a in enumerate(s):
   if i and s[i-1]==a:continue
   if a*(a+1)<=D:out.add(tuple(sorted(s[:i]+s[i+1:]+(a+1,a*(a+1)))))
 for i,b in enumerate(s):
  if b<2 or (i and s[i-1]==b):continue
  a=b-1;c=a*b
  try:j=s.index(c,i+1)
  except ValueError:continue
  out.add(tuple(sorted(tuple(v for h,v in enumerate(s) if h!=i and h!=j)+(a,))))
 return out

sys.setrecursionlimit(10000)
@lru_cache(None)
def normalform(a):
 if a*(a+1)>D:return ((a,1),)
 c=Counter(dict(normalform(a+1)));c.update(dict(normalform(a*(a+1))))
 return tuple(sorted(c.items()))
def state_nf(s):
 c=Counter()
 for a in s:c.update(dict(normalform(a)))
 return tuple(sorted(c.items()))

start=time.monotonic();rows=[]
for n in range(2,N+1):
 ts=triples(n);seed=(n,)*4;visited=set();components=[];seed_stats=None;long_detour_components=0;detour_paths=[]
 for root in [seed]+ts:
  if root in visited:continue
  q=deque([root]);visited.add(root);nodes=0;degree=0;hist=Counter();three=[];four_seed=False
  while q:
   s=q.popleft();nodes+=1;hist[len(s)]+=1
   if len(s)==3:three.append(s)
   if s==seed:four_seed=True
   ns=neighbors(s);degree+=len(ns)
   for t in ns:
    if t not in visited:visited.add(t);q.append(t)
   if len(visited)>500000:raise RuntimeError((n,'state cap exceeded; reduce L explicitly'))
  assert degree%2==0
  if len(three)>1:
   short_seen={three[0]};short_q=deque([three[0]])
   while short_q:
    for t in neighbors(short_q.popleft()):
     if len(t)<=3 and t not in short_seen:short_seen.add(t);short_q.append(t)
   different=[t for t in three if t not in short_seen]
   long_detour_components+=bool(different)
   if different:
    target=different[0];parents={three[0]:None};search=deque([three[0]])
    while target not in parents:
     s=search.popleft()
     for t in sorted(neighbors(s)):
      if t not in parents:parents[t]=s;search.append(t)
    path=[];s=target
    while s is not None:path.append(s);s=parents[s]
    detour_paths.append(list(reversed(path)))
  st=dict(vertices=nodes,edges=degree//2,length_hist=dict(hist),triples=len(three),triple_examples=three[:4])
  components.append(st)
  if four_seed:seed_stats=st
 # Edges are exact identities by construction; independently check every stored vertex.
 for s in visited:assert sum((Fraction(1,a) for a in s),Fraction())==Fraction(4,n)
 r=dict(n=n,bounded_ES_triples=len(ts),components=len(components),vertices=len(visited),edges=sum(c['edges'] for c in components),four_copy_component=seed_stats,components_joining_multiple_triples=sum(c['triples']>1 for c in components),max_triples_in_component=max(c['triples'] for c in components))
 seed_nf=state_nf(seed);target_nfs={state_nf(t) for t in ts}
 r.update(detour_paths=detour_paths,components_requiring_length_above_3=long_detour_components,unlimited_length_seed_reaches_target=seed_nf in target_nfs,unlimited_length_seeded_components=len(target_nfs|{seed_nf}))
 rows.append(r);print(n,len(visited),len(components),seed_stats['triples'],flush=True)
p=Path('data/z52b/pass2/ZF0/Z0984');p.mkdir(parents=True,exist_ok=True)
summary={k:sum(r[k] for r in rows) for k in ['bounded_ES_triples','components','vertices','edges','components_joining_multiple_triples','components_requiring_length_above_3','unlimited_length_seeded_components']}
(p/'results.json').write_text(json.dumps(dict(D=D,L=L,n_range=[2,N],summary=summary,rows=rows,seconds=time.monotonic()-start),indent=2))
