import json, math, random
from pathlib import Path
import numpy as np
from sympy import primerange
N=100000
ps=list(primerange(5,N+1)); ps=[p for p in ps if p%4==1]
spf=list(range(4*N+2))
for i in range(2,math.isqrt(4*N+1)+1):
 if spf[i]==i:
  for j in range(i*i,4*N+2,i):
   if spf[j]==j: spf[j]=i
def rcount(p):
 n=4*p+1; f={}
 while n>1:
  q=spf[n]; f[q]=f.get(q,0)+1; n//=q
 ds=[1]
 for q,e in f.items(): ds=[x*q**j for x in ds for j in range(e+1)]
 return sum((1 if x*x==4*p+1 else 2) for x in ds if x*x<=4*p+1 and x%4==3 and (4*p+1)//x%4==3)
R=np.array([rcount(p) for p in ps],float); y=np.log1p(R); P=np.array(ps)
rng=np.random.default_rng(1968); ix=rng.permutation(len(ps)); tr=ix[:int(.8*len(ix))]; te=ix[len(tr):]
mods=[3,4,5,7,8,11,12,13,840]
# Residue indicator feature concatenation realizes the stated sum kernel. Ridge selected by 5-fold CV on training.
X=np.concatenate([(P[:,None]%m==np.arange(m)[None,:]).astype(float)/math.sqrt(m) for m in mods],axis=1)
def fit_eval(X):
 xt=X[tr]; yt=y[tr]; xm=xt.mean(0)
 xt=xt-xm; xv=X[te]-xm
 folds=np.array_split(rng.permutation(len(tr)),5); vals=[]
 for lam in [1e-4,.001,.01,.1,1,10,100]:
  errs=[]
  for v in folds:
   a=np.setdiff1d(np.arange(len(tr)),v); coef=np.linalg.solve(xt[a].T@xt[a]+lam*np.eye(xt.shape[1]),xt[a].T@yt[a]); errs.extend((yt[v]-xt[v]@coef)**2)
  vals.append((np.mean(errs),lam))
 lam=min(vals)[1]; coef=np.linalg.solve(xt.T@xt+lam*np.eye(xt.shape[1]),xt.T@yt)
 pred=xv@coef; base=y[te].mean()
 return 1-np.sum((y[te]-pred)**2)/np.sum((y[te]-base)**2),lam,coef,xm
full=fit_eval(X)
# Nonnegative modulus-specific relevance via CV-tuned group ridge; weights summarized by squared coefficient norm.
weights={}
pos=0
for m in mods:
 width=m; w=float(np.sum(full[2][pos:pos+width]**2)); weights[str(m)]=w; pos+=width
X840=(P[:,None]%840==np.arange(840)[None,:]).astype(float)/math.sqrt(840)
r840=fit_eval(X840)
# Residue-only baseline is class-specific mean, same p mod 840; compare R2 in original log target.
means={int(c):float(y[tr[P[tr]%840==c]].mean()) for c in np.unique(P[tr]%840)}
pred=np.array([means.get(int(P[i]%840),float(y[tr].mean())) for i in te]); r2=1-np.sum((y[te]-pred)**2)/np.sum((y[te]-y[te].mean())**2)
out={'limit':N,'primes':len(ps),'definition':'R(p)=# ordered positive (u,B) with (4u-1)(4B-1)=4p+1; exact factor-divisor count','seed':1968,'train':len(tr),'test':len(te),'R_range':[int(R.min()),int(R.max())],'weighted_kernel_test_R2':full[0],'mod840_kernel_test_R2':r840[0],'mod840_class_mean_test_R2':float(r2),'ridge_lambda':full[1],'modulus_weight_squared_coef_norm':weights}
d=Path('data/z52b/pass2/NC2/Z1968'); d.mkdir(parents=True,exist_ok=True); (d/'metrics.json').write_text(json.dumps(out,indent=2)+'\n'); print(json.dumps(out))
