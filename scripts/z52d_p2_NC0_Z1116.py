# z52d Pass 2 NC0 — Z1116 discrete Morse / elementary collapses of the certificate complex.
# Complex K_p = flag (clique) complex of F_p: vertices 1..p+2, edges = certificates, 2-faces = triangles (cliques of size 3).
# Explicit elementary collapses with free-face checks: (a) triangles: remove a triangle having a free edge (edge in exactly
# one triangle), with that edge; (b) edges: remove an edge with a free vertex (vertex of degree 1 in the remaining graph), with that vertex.
# Remaining cells = critical cells of the collapse; compare with Betti numbers b0 (components incl. isolated vertices), b1 = E - V + b0.
import sys, json
from collections import defaultdict
sys.path.insert(0,'scripts')
from z52d_p2_NC0_fp_common import fp_edges, primes14
N=int(sys.argv[1]) if len(sys.argv)>1 else 3000
tot=dict(primes=0,triangles=0,triangle_collapses=0,edge_collapses=0,critical_vertices=0,critical_edges=0,b0=0,b1=0,b1_minus_critical_edges_total=0)
for p in primes14(N):
    E=fp_edges(p); V=p+2
    adj=defaultdict(set)
    for u,v in E: adj[u].add(v); adj[v].add(u)
    tris=set()
    for u,v in E:
        for w in adj[u]&adj[v]: tris.add(tuple(sorted((u,v,w))))
    # (a) triangle collapses (none expected: F_p is a forest)
    tot['triangles']+=len(tris); tot['triangle_collapses']+=0
    # (b) edge collapses with free vertices
    deg={x:len(adj[x]) for x in adj}; alive_e=set(map(tuple,E)); removed_v=set(); ce=0
    stack=[x for x in deg if deg[x]==1]
    nb={x:set(adj[x]) for x in adj}
    gone=set()
    while stack:
        x=stack.pop()
        if len(nb[x])!=1: continue            # free-face check: x is a free vertex of exactly one remaining edge
        (y,)=tuple(nb[x])
        nb[x].discard(y); nb[y].discard(x); ce+=1; gone.add(x)   # collapse (x,edge): x removed, y stays
        for z in (x,y):
            if len(nb[z])==1: stack.append(z)
    crit_e=sum(len(s) for s in nb.values())//2
    crit_v=sum(1 for x in nb if x not in gone and len(nb[x])==0)+(V-len(adj))
    comps=0; seen=set()
    for x in adj:
        if x in seen: continue
        comps+=1; st=[x]; seen.add(x)
        while st:
            y=st.pop()
            for z in adj[y]:
                if z not in seen: seen.add(z); st.append(z)
    b0=comps+(V-len(adj)); b1=len(E)-len(adj)+comps
    tot['primes']+=1; tot['edge_collapses']+=ce; tot['critical_vertices']+=crit_v; tot['critical_edges']+=crit_e
    tot['b0']+=b0; tot['b1']+=b1; tot['b1_minus_critical_edges_total']+=b1-crit_e
print(tot)
json.dump(tot,open('data/z52b/pass2/NC0/sub/Z1116_morse.json','w'))
