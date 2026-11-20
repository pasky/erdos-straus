"""Compute quotient by the gcd-orbit ratio subgroup; explicit exact finite exceptions."""
from z78_proth_period import root,ds,pa as p
from math import gcd
import json

def one(h):
    Q=2**h-1;k=2*Q+1;tgt=14*Q-1
    if h==1:return {'h':1,'no':'dyadic: no c|3 congruent 13 mod 16'}
    g=p.znstar(Q,1);cyc=list(map(int,g[1][1]));B=[(1+pow(2,a,Q))%Q for a in range(h)];lg=[p.znlog(x,g) for x in B];ref=lambda a:gcd(a,h)%h;ids=[a for a in range(h) if a!=ref(a)];v=[lg[a]-lg[ref(a)] for a in ids];M=p.matrix(len(cyc),len(v),[z[i] for i in range(len(cyc)) for z in v]);diag=p.matdiagonal(p.Vec(cyc));idx=int(p.matdet(p.mathnf(p.concat(diag,M))));zneg=p.znlog(Q-1,g);F={}
    for d in ds(h):
        F[d]=B[d%h]
        for e in ds(d)[:-1]:F[d]=F[d]*pow(F[e],-1,Q)%Q
    E={1:[]}
    for d,t in F.items():E.update({x*t%Q:T+[d] for x,T in E.items()})
    row={'h':h,'orbit_index':idx,'unit_j':[i for i in range(h) if gcd(i,h)==1]}
    for c in ds(k):
        if c%16!=tgt%16:continue
        for x,T in E.items():
            z=p.matsolvemod(M,p.Col(cyc),zneg-p.znlog(x*c%Q,g))
            if z.type()!='t_INT':
                row.update(c=c,T0=T,ratios={a:int(b)%int(p.znorder(p.Mod(B[a]*pow(B[ref(a)],-1,Q),Q))) for a,b in zip(ids,z) if b});return row
    row['no']='quotient obstruction';return row
if __name__=='__main__':
    S=[one(h) for h in range(1,62,2)];(root/'exact-core.json').write_text(json.dumps(S,separators=(',',':'))+'\n');print([(a['h'],a.get('orbit_index'),a.get('c'),a.get('T0')) for a in S])
