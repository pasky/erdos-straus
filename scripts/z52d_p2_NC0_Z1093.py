# z52d Pass 2 NC0 — Z1093 weighted (shortest-path) search for economical certificates.
# Graph: states = (depth d, remainder r in Q); from r choose unit fraction 1/k with 1/k <= r, k <= (3-d)/r (sorted-type bound),
# edge cost = log k. Terminal: depth 2 with r = 1/z (z integer).  Dijkstra on total cost = log(x*y*z)  (min height product).
# Compared against direct enumeration of all ordered triples with x<=y<=z (sols() from z52d_p2_NC0_allsols.py).
import sys, math, heapq, json
from fractions import Fraction as F
sys.path.insert(0,'scripts')
from z52d_p2_NC0_fp_common import primes14
from z52d_p2_NC0_allsols import sols
N=int(sys.argv[1]) if len(sys.argv)>1 else 300
def dijkstra_min_product(p):
    # entries: (cost, kind, d, r, path); kind 0 = partial state, kind 1 = finished triple (cost already includes log z)
    pq=[(0.0,0,0,F(4,p),())]; expanded=0; pushed=1
    while pq:
        cost,kind,d,r,path=heapq.heappop(pq)
        expanded+=1
        if kind==1:
            return dict(cost=cost, sol=path, expanded=expanded, pushed=pushed)
        if d==2:
            if r.numerator==1:                       # last term forced: z = 1/r
                z=r.denominator
                heapq.heappush(pq,(cost+math.log(z),1,3,r,path+(z,))); pushed+=1
            continue
        lo=math.ceil(1/r); hi=math.floor((3-d)/r)   # next unit fraction 1/k, 1/k <= r, k <= (3-d)/r (sorted-type bound)
        for k in range(lo, hi+1):
            nr=r-F(1,k)
            heapq.heappush(pq,(cost+math.log(k),0,d+1,nr,path+(k,))); pushed+=1
    return None
rows=[]
for p in primes14(N):
    S=sols(p)
    best=min(x*y*z for x,y,z in S)
    dj=dijkstra_min_product(p)
    rows.append(dict(p=p,nsol=len(S),enum_min_product=best,dijkstra_min_product=(math.prod(dj['sol'])) if dj else None,
                     dj_sol=dj['sol'] if dj else None, expanded=dj['expanded'] if dj else None, pushed=dj['pushed'] if dj else None))
bad=[r for r in rows if r['dijkstra_min_product']!=r['enum_min_product']]
print('primes',len(rows),'mismatch (Dijkstra min product != enumeration):',len(bad))
print('median expansions before first solution:',sorted(r['expanded'] for r in rows)[len(rows)//2],
      'median pushes:',sorted(r['pushed'] for r in rows)[len(rows)//2])
print('sample', rows[:3])
json.dump(rows,open('data/z52b/pass2/NC0/sub/Z1093_dijkstra.json','w'))
