# Check: Frobenius number of <t*u, t*v, u+v> (gcd(u,v)=1, gcd(t,u+v)=1) equals t*u*v - u - v  (Johnson/Brauer–Shockley gluing)
from math import gcd
def frob(gens):
    m=min(gens); INF=10**18
    # Dijkstra-free: Apery set via shortest paths mod m (Nijenhuis)
    import heapq
    dist=[INF]*m; dist[0]=0; pq=[(0,0)]
    while pq:
        d,r=heapq.heappop(pq)
        if d>dist[r]: continue
        for g in gens:
            nd=d+g; nr=nd%m
            if nd<dist[nr]: dist[nr]=nd; heapq.heappush(pq,(nd,nr))
    return max(dist)-m
bad=0; n=0
for t in range(2,13):
    for u in range(1,15):
        for v in range(u,15):
            if gcd(u,v)!=1 or gcd(t,u+v)!=1: continue
            gens=[t*u,t*v,u+v]
            if gcd(gcd(gens[0],gens[1]),gens[2])!=1: continue
            if min(gens)==1: continue
            n+=1
            if frob(gens)!=t*u*v-u-v: bad+=1; print('mismatch',t,u,v,frob(gens),t*u*v-u-v)
print('checked',n,'mismatches',bad)
