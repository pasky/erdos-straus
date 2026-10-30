"""Per-prime weights: residual log(count+1) ~ Σ_q β_q (q/p), p≡1 (mod 4) (χ_{-4p}(q) = (−1/q)(q/p) is collinear, so one set suffices).
Reports β_q, standard errors, and q·β_q (naive Euler-factor scaling predicts q·β_q ≈ const)."""
import numpy as np, json
from sympy import isprime, legendre_symbol, primerange
R='data/z52b/raw/'
F=np.loadtxt(R+'f4_all_30000.txt',dtype=np.int64)
FP=np.vstack([F[[isprime(int(x)) for x in F[:,0]]],np.loadtxt(R+'pr_20001_200000.txt',dtype=np.int64)])
FP=FP[np.argsort(FP[:,0])]; FP=FP[np.concatenate([[True],np.diff(FP[:,0])>0])]
W=np.load(R+'words_3e6.npy')
out={}
for cls in (1,3):
    S=FP[(FP[:,0]%4==cls)&(FP[:,0]>100)]; P=S[:,0]; lp=np.log(P.astype(float))
    qs=list(primerange(2,80))
    Xc=np.array([[int(legendre_symbol(q,int(p))) for q in qs] for p in P],float)
    tg={'U':S[:,1],'k1':S[:,10],'k2':S[:,11],'R':W[P-1,3],'Uv':W[P-1,4],'I3':W[P-1,2]}
    for tn,t in tg.items():
        y=np.log(t+1.0); X=np.hstack([np.vstack([np.ones_like(lp),lp,np.log(lp)]).T,Xc])
        b,res,rk,sv=np.linalg.lstsq(X,y,rcond=None); r=y-X@b; s2=r.var()*len(y)/(len(y)-X.shape[1])
        se=np.sqrt(np.diag(np.linalg.inv(X.T@X))*s2)
        d={q:(round(float(b[3+i]),4),round(float(se[3+i]),4),round(float(q*b[3+i]),3)) for i,q in enumerate(qs)}
        out[f'{tn}|p≡{cls}(4)']=d
        print(tn,cls,' '.join(f'{q}:{v[0]:+.3f}±{v[1]:.3f}' for q,v in d.items() if q<50),flush=True)
json.dump(out,open('data/z52b/qweights.json','w'),indent=1)
