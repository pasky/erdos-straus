# z52d Pass 2 NC0 — Z1094 synchronizing words on the elementary-move system of F_p.
# The item presupposes a modular transition system; the repo's well-defined elementary moves are the F_p edges (u -> v).
# A letter acts on states as a partial map: a move from u to a neighbour; a state with no move is fixed by every letter.
# Synchronization of a target set T needs every state to reach T; we measure how many states have any move at all.
import sys, json
sys.path.insert(0,'scripts')
from z52d_p2_NC0_fp_common import fp_edges, primes14
N=int(sys.argv[1]) if len(sys.argv)>1 else 3000
tot=0; movable=0; primes=0; no_sync=0
for p in primes14(N):
    E=fp_edges(p); V=p+2
    deg={}
    for u,v in E: deg[u]=deg.get(u,0)+1; deg[v]=deg.get(v,0)+1
    primes+=1; tot+=V; movable+=len(deg)
    if len(deg)<V: no_sync+=1       # some state (an isolated vertex) has no move -> no word moves it -> nothing synchronizes V
print('primes',primes,'states',tot,'states with >=1 move',movable,'share',round(movable/tot,4),
      'primes where some state is immobile (no word can move it):',no_sync)
json.dump(dict(primes=primes,states=tot,movable=movable),open('data/z52b/pass2/NC0/sub/Z1094_sync.json','w'))
