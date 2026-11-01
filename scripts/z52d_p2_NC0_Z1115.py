# z52d Pass 2 NC0 — Z1115 random spanning-tree exploration on the certificate graph F_p (a forest).
# Wilson's algorithm samples a uniform spanning tree of each component; we check it returns the component itself,
# then compare budgeted DFS vs tree-guided search (random root, BFS/DFS in the sampled tree) on the component of 1:
# regions = dyadic bins of the vertex value; budget = number of vertices expanded.
import sys, json, random
from collections import defaultdict
sys.path.insert(0,'scripts')
from z52d_p2_NC0_fp_common import fp_edges, primes14
random.seed(1)
N=int(sys.argv[1]) if len(sys.argv)>1 else 2000
def wilson(adj, nodes):
    # uniform spanning tree of a connected component via loop-erased random walks
    root=random.choice(nodes); intree={root}; nxt={}
    for s in nodes:
        u=s
        while u not in intree:
            nxt[u]=random.choice(adj[u]); u=nxt[u]
        u=s
        while u not in intree:
            intree.add(u); u=nxt[u]
    T=defaultdict(list)
    for u,v in nxt.items(): T[u].append(v); T[v].append(u)
    return T
out=dict(primes=0,tree_equals_component=0)
rows=[]
for p in primes14(N):
    E=fp_edges(p)
    if not E: continue
    adj=defaultdict(list)
    for u,v in E: adj[u].append(v); adj[v].append(u)
    # component of 1
    comp=[]; st=[1]; seen={1}
    while st:
        x=st.pop(); comp.append(x)
        for y in adj.get(x,[]):
            if y not in seen: seen.add(y); st.append(y)
    if len(comp)<2: continue
    out['primes']+=1
    T=wilson(adj,sorted(comp))
    tedges={frozenset((u,v)) for u in T for v in T[u]}
    Cedges={frozenset(e) for e in E if e[0] in seen}
    out['tree_equals_component']+= (tedges==Cedges)
    # budgeted exploration: visit order from DFS (stack) vs tree-guided (random root in sampled tree, DFS order)
    def explore(G, start, budget):
        order=[]; seen2={start}; st=[start]
        while st and len(order)<budget:
            x=st.pop(); order.append(x)
            nb=list(G.get(x,[])); random.shuffle(nb)
            for y in nb:
                if y not in seen2: seen2.add(y); st.append(y)
        return order
    rb=random.choice(comp)
    regions=lambda vs: len({v.bit_length() for v in vs})
    for b in (3,6,12):
        dfs=explore(adj,1,b); tg=explore(T,rb,b)
        rows.append(dict(p=p,budget=b,dfs_regions=regions(dfs),tree_regions=regions(tg),comp=len(comp)))
print(out)
import statistics as st_
for b in (3,6,12):
    R=[r for r in rows if r['budget']==b]
    print('budget',b,'mean regions DFS',round(st_.mean(r['dfs_regions'] for r in R),3),
          'tree-guided',round(st_.mean(r['tree_regions'] for r in R),3),'n',len(R))
json.dump(out,open('data/z52b/pass2/NC0/sub/Z1115_tree.json','w'))
