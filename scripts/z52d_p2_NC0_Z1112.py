# z52d Pass 2 NC0 — Z1112 nonbacktracking walks on the certificate graph F_p (forest, FOREST_CONNECTIVITY §0 "F_p is a forest").
# Counts walks of length <=8 from start vertices (all vertices of the component of 1 and of a sample of others):
#   W(L)  = unrestricted walks,  NB(L) = nonbacktracking walks (no immediate reversal).  Also distinct endpoints reached.
import sys, json
import numpy as np
sys.path.insert(0,'scripts')
from z52d_p2_NC0_fp_common import fp_edges, primes14
N=int(sys.argv[1]) if len(sys.argv)>1 else 2000
Lmax=8
res=[]
for p in primes14(N):
    E=fp_edges(p); V=p+2
    if not E: continue
    adj={}
    for u,v in E: adj.setdefault(u,[]).append(v); adj.setdefault(v,[]).append(u)
    starts=[1]+[s for s in adj if s!=1][:3]
    for s0 in starts:
        if s0 not in adj: continue
        # unrestricted walk counts and NB walk counts by length, plus endpoints
        cur_w={s0:1}; cur_nb={(s0,None):1}
        Wc=[1]; NBc=[1]; ends_nb=[{s0}]; ends_w=[{s0}]
        for L in range(1,Lmax+1):
            nw={}; 
            for x,c in cur_w.items():
                for y in adj.get(x,[]): nw[y]=nw.get(y,0)+c
            cur_w=nw; Wc.append(sum(nw.values()))
            nnb={}
            for (x,prev),c in cur_nb.items():
                for y in adj.get(x,[]):
                    if y!=prev: nnb[(y,x)]=nnb.get((y,x),0)+c
            cur_nb=nnb; NBc.append(sum(nnb.values()))
            ends_nb.append({x for (x,_) in nnb}); ends_w.append(set(nw))
        comp=len(set().union(*ends_w))
        Lnb=max(L for L in range(Lmax+1) if NBc[L]>0)
        res.append(dict(p=p,start=s0,deg=len(adj[s0]),W8=Wc[-1],NB8=NBc[-1],longest_NB=Lnb,
                        reach_NB=len(set().union(*ends_nb)),reach_W=len(set().union(*ends_w))))
print('samples',len(res))
print('max NB8 / max W8 :', max(r['NB8'] for r in res), max(r['W8'] for r in res))
from collections import Counter
print('longest NB walk (length<=8) distribution over starts:', sorted(Counter(r['longest_NB'] for r in res).items()))
print('starts with any NB walk of length 8:', sum(r['NB8']>0 for r in res), 'of', len(res))
print('all: reach_NB == reach_W ?', all(r['reach_NB']==r['reach_W'] for r in res))
print('NB walks of length 8 <= (max deg)*(deg-1)^... sample:', [(r['p'],r['deg'],r['NB8'],r['W8']) for r in res[:8]])
print('median W8 / NB8 over starts with NB8>0:', float(np.median([r['W8']/r['NB8'] for r in res if r['NB8']>0])) if any(r['NB8']>0 for r in res) else 'n/a')
json.dump(res,open('data/z52b/pass2/NC0/sub/Z1112_nb.json','w'))
