"""Autocorrelation / Ramanujan-type spectrum of the normalised ES count over all n ≤ 30000, class means mod 840 at primes,
and consecutive-prime residual correlation."""
import numpy as np, json, math
from sympy import isprime, totient
R='data/z52b/raw/'
F=np.loadtxt(R+'f4_all_30000.txt',dtype=np.int64); n=F[:,0].astype(float); U=F[:,1].astype(float)
y=np.log(U+1); X=np.vstack([np.ones_like(n),np.log(n),np.log(np.log(n+2))]).T; r=y-X@np.linalg.lstsq(X,y,rcond=None)[0]
out={}
ac={L:round(float(np.corrcoef(r[:-L],r[L:])[0,1]),3) for L in [1,2,3,4,5,6,7,8,12,24,30,60,120,840]}
out['autocorr_lags']=ac; print('autocorr',ac)
# mean residual by n mod q for q ≤ 30 : variance explained
ve={}
for q in range(2,31):
    m=np.array([r[F[:,0]%q==a].mean() for a in range(q)]); g=m[F[:,0]%q]
    ve[q]=round(float(1-np.var(r-g)/np.var(r)),3)
out['variance_explained_by_n_mod_q']=ve; print('VE by n mod q',ve)
best=max(ve,key=ve.get)
# joint: n mod 840
m=np.array([r[F[:,0]%840==a].mean() if (F[:,0]%840==a).any() else 0 for a in range(840)]); g=m[F[:,0]%840]
out['VE_n_mod_840']=round(float(1-np.var(r-g)/np.var(r)),3); print('VE mod 840',out['VE_n_mod_840'])
# primes: class means mod 840 among p≡1(4)
FP=np.vstack([F[[isprime(int(x)) for x in F[:,0]]],np.loadtxt(R+'pr_20001_200000.txt',dtype=np.int64)])
FP=FP[np.argsort(FP[:,0])]; FP=FP[np.concatenate([[True],np.diff(FP[:,0])>0])]
S=FP[(FP[:,0]%4==1)&(FP[:,0]>100)]; P=S[:,0]; lp=np.log(P.astype(float))
rp=np.log(S[:,1]+1.0); Xp=np.vstack([np.ones_like(lp),lp,np.log(lp)]).T; rp=rp-Xp@np.linalg.lstsq(Xp,rp,rcond=None)[0]
cls={}
for a in sorted(set((P%840).tolist())):
    s=P%840==a
    if s.sum()>=30: cls[int(a)]=(round(float(rp[s].mean()),3),int(s.sum()))
srt=sorted(cls.items(),key=lambda kv:kv[1][0])
out['p_class_mod840_hardest10']=srt[:10]; out['p_class_mod840_easiest5']=srt[-5:]
print('hardest classes mod 840',srt[:10]); print('easiest',srt[-5:])
# consecutive primes p≡1(4)
out['consecutive_prime_resid_corr']=round(float(np.corrcoef(rp[:-1],rp[1:])[0,1]),4); print('consec',out['consecutive_prime_resid_corr'])
# k1-k2 complementarity
def res(t):
    yy=np.log(t+1.0); return yy-Xp@np.linalg.lstsq(Xp,yy,rcond=None)[0]
r1=res(S[:,10]); r2=res(S[:,11])
out['k1_k2_resid_corr']=round(float(np.corrcoef(r1,r2)[0,1]),3)
q1=np.quantile(r1,0.05); q2=np.quantile(r2,0.05)
out['both_below_5pct']=int(((r1<q1)&(r2<q2)).sum()); out['expected_indep']=round(0.0025*len(r1),1)
print('k1k2 corr',out['k1_k2_resid_corr'],'both low',out['both_below_5pct'],'expected',out['expected_indep'])
json.dump(out,open('data/z52b/spectral.json','w'),indent=1)
