"""Exact group census; compressed ladder templates applicable at every unit j."""
import json,math
from pathlib import Path
from cypari2 import Pari
p=Pari();root=Path('data/z78/proth')
def one(h):
    H=2**h-1;k=2*H+1;u=2*H
    if h==1:return {'h':h,'fail':'dyadic','candidates':[]}
    g=p.znstar(H,1);cyc=list(map(int,g[1][1]));r=len(cyc)
    B=[(pow(2,i,H)+1)%H for i in range(h)]; logs=[p.znlog(b,g) for b in B]; z=p.znlog(H-1,g);I=[i for i in range(h) if math.gcd(i,h)==1];R=[i for i in I if i!=1]
    def mat(v):return p.matrix(r,len(v),[a[i] for i in range(r) for a in v]);
    M=mat([logs[i]-logs[1] for i in R]);G=mat(logs);diag=p.matdiagonal(p.Vec(cyc));idx=lambda X:int(p.matdet(p.mathnf(p.concat(diag,X))));out={'h':h,'ambient':cyc,'full_index':idx(G),'ratio_index':idx(M),'unit_j':I};cs=[int(c) for c in p.divisors(k) if int(c)%16==(7*u-1)%16];out['full_hits']=[c for c in cs if p.matsolvemod(G,p.Col(cyc),z-p.znlog(c%H,g)).type()!='t_INT'];
    for c in cs:
        for a in [None,*range(h)]: # optional final slot pays B_a/B_1, realizable even for nonunit a
            t=z-p.znlog(c%H,g)-(logs[a]-logs[1] if a is not None else p.Col([0]*r))
            v=p.matsolvemod(M,p.Col(cyc),t)
            if v.type()!='t_INT':
                out.update(c=c,terminal=a,powers={i:int(e)%int(p.znorder(p.Mod(B[i]*pow(B[1],-1,H),H))) for i,e in zip(R,v) if e});return out
    return out
if __name__=='__main__':
    data=[]
    for h in range(1,62,2):
        d=one(h);data.append(d);print(h,d.get('full_index'),d.get('ratio_index'),len(d.get('full_hits',[])),d.get('c'),d.get('terminal'),flush=True)
    (root/'groups.json').write_text(json.dumps(data,separators=(',',':'))+'\n')
