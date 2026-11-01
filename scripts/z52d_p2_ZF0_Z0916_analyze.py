"""Actual unordered U, not the pass-1 R_K proxy. Stratified rank null test."""
import json
from pathlib import Path
import numpy as np
from scipy.stats import rankdata,spearmanr
D=Path('data/z52b/pass2/ZF0/Z0916');a=np.loadtxt(D/'input.csv',delimiter=',',skiprows=1);b=np.loadtxt(D/'kloo.csv',delimiter=',',skiprows=1)
assert np.array_equal(a[:,0],b[:,0]);p=a[:,0].astype(int);U=a[:,1];K=b[:,1];kn=b[:,2]
assert np.max(abs(kn))<=2+1e-10
# Mod840 and 100000-wide size bins keep both residue and magnitude matched.
labels=(p%840)*10+np.minimum(p//100000,9);groups=[np.flatnonzero(labels==r) for r in np.unique(labels)]
x=rankdata(kn);y=rankdata(U)
for ix in groups:x[ix]-=x[ix].mean();y[ix]-=y[ix].mean()
r=float(x@y/np.sqrt((x@x)*(y@y)));rng=np.random.default_rng(916);null=[]
for _ in range(1000):
 yy=y.copy()
 for ix in groups:yy[ix]=rng.permutation(yy[ix])
 null.append(float(x@yy/np.sqrt((x@x)*(yy@yy))))
out={'n':len(p),'range':[int(min(p)),int(max(p))],'raw_K_U':list(map(float,spearmanr(K,U))),'normalized_K_U':list(map(float,spearmanr(kn,U))),'matched_rank_rho':r,'matched_permutation_p':(1+sum(abs(z)>=abs(r) for z in null))/1001,'null_sd':float(np.std(null)),'groups':len(groups),'max_abs_Knorm':float(max(abs(kn))),'size_bins':[]}
for lo in [0,200000,400000,600000,800000]:
 ix=(p>lo)&(p<=lo+200000);out['size_bins'].append({'lo':lo,'n':int(sum(ix)),'rho':float(spearmanr(kn[ix],U[ix]).statistic)})
# Independent complex sum on small inputs; exact inverses via Python pow.
checks=[]
for q in p[:30]:
 direct=sum(np.exp(2j*np.pi*(x+pow(x,-1,int(q)))/q) for x in range(1,int(q)))
 val=K[np.where(p==q)[0][0]];assert abs(direct.real-val)<1e-9 and abs(direct.imag)<1e-9
 checks.append(int(q))
out['independent_small_checks']=checks
(D/'analysis.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
