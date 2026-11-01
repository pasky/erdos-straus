import gzip,json,math
from pathlib import Path
import numpy as np
D=Path('data/z52b/pass2/ZF0/Z1721')
a=np.loadtxt(gzip.open(D/'minu.csv.gz','rt'),delimiter=',',skiprows=1,dtype=np.int64)
p,u,k,c,n=a.T;good=u>0
assert np.all(p[good]==4*u[good]*k[good]*c[good]-u[good]-k[good])
out={'n':len(p),'zeros':p[~good].tolist(),'u_hist':dict(zip(*[x.tolist() for x in np.unique(u,return_counts=True)])),'quantiles':{},'decades':[],'max_u_logp_ratio':float(np.max(u[good]/np.log(p[good]))),'max_u_logp2_ratio':float(np.max(u[good]/np.log(p[good])**2))}
for name,z in [('u',u[good]),('selected_min_k',k[good]),('C_at_selected_k',c[good]),('kchoices',n[good])]:out['quantiles'][name]=dict(zip(['0','.5','.9','.99','1'],np.quantile(z,[0,.5,.9,.99,1]).tolist()))
for B in [100,1000,10000,100000,1000000,10000000]:
 ix=np.where(good&(p<=B))[0];j=ix[np.argmax(u[ix])];j2=ix[np.argmax(k[ix])]
 out['decades'].append({'bound':B,'maxu':int(u[j]),'p':int(p[j]),'k':int(k[j]),'C':int(c[j]),'max_selected_k':int(k[j2]),'k_argmax':int(p[j2])})
(D/'analysis.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({x:v for x,v in out.items() if x!='u_hist'},indent=2))
