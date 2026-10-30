"""Misc fingerprints: shift spectrum, Euler weights per q, p≡3(4) fit, U at squares, U(pq) multiplicativity."""
import numpy as np, json
from sympy import isprime, divisor_count, legendre_symbol, jacobi_symbol, primerange, factorint
from scipy.stats import spearmanr
R='data/z52b/raw/'
F=np.loadtxt(R+'f4_all_30000.txt',dtype=np.int64); Ud=dict(zip(F[:,0].tolist(),F[:,1].tolist()))
FP=np.vstack([F[[isprime(int(x)) for x in F[:,0]]],np.loadtxt(R+'pr_20001_200000.txt',dtype=np.int64)])
FP=FP[np.argsort(FP[:,0])]; FP=FP[np.concatenate([[True],np.diff(FP[:,0])>0])]
out={}
def resid(P,y):
    lp=np.log(P.astype(float)); X=np.vstack([np.ones_like(lp),lp,np.log(lp)]).T; return y-X@np.linalg.lstsq(X,y,rcond=None)[0]
for cls in (1,3):
    S=FP[(FP[:,0]%4==cls)&(FP[:,0]>100)]; P=S[:,0]; r=resid(P,np.log(S[:,1]+1.0))
    sp={}
    for s in range(1,41):
        sp[s]=round(float(spearmanr(r,np.array([int(divisor_count(int(p)+s)) for p in P],float))[0]),3)
    out[f'shift_spectrum_p{cls}mod4']=sp; print('shift spectrum',cls,sp,flush=True)
    qs=list(primerange(2,60))
    Xc=np.array([[int(legendre_symbol(q,int(p))) for q in qs] for p in P],float)
    Xm=np.array([[0 if q==2 else int(jacobi_symbol(-int(p),q)) for q in qs] for p in P],float)
    X=np.hstack([np.ones((len(P),1)),Xc,Xm[:,1:]]); b=np.linalg.lstsq(X,r,rcond=None)[0]
    res=r-X@b; out[f'euler_weights_p{cls}mod4']=dict(chi_p={q:round(float(v),4) for q,v in zip(qs,b[1:1+len(qs)])},chi_m4p={q:round(float(v),4) for q,v in zip(qs[1:],b[1+len(qs):])},R2=round(float(1-res.var()/r.var()),3))
    print('weights',cls,out[f'euler_weights_p{cls}mod4'],flush=True)
# squares
sq=[(m,Ud[m*m]) for m in range(3,174,2) if m*m in Ud]
ratio=[]
for m,u in sq:
    nb=[Ud[k] for k in range(m*m-40,m*m+41,4) if k!=m*m and k in Ud and k%4==(m*m)%4]
    ratio.append(u/np.median(nb))
out['U_square_over_neighbour_median']=dict(mean=float(np.mean(ratio)),median=float(np.median(ratio)),first=[(m,u) for m,u in sq[:15]])
print('squares',out['U_square_over_neighbour_median'])
# multiplicativity
rows=[]
for n in range(15,30001):
    f=factorint(n)
    if len(f)==2 and all(e==1 for e in f.values()):
        p,q=f; 
        if p>2 and q>2: rows.append((np.log(Ud[n]),np.log(Ud[p]),np.log(Ud[q]),np.log(n)))
A=np.array(rows); X=np.vstack([np.ones(len(A)),A[:,1],A[:,2],A[:,3]]).T; b=np.linalg.lstsq(X,A[:,0],rcond=None)[0]
out['multiplicativity_pq']=dict(coef_const=float(b[0]),coef_logUp=float(b[1]),coef_logUq=float(b[2]),coef_logn=float(b[3]),n=len(A))
print('pq',out['multiplicativity_pq'])
json.dump(out,open('data/z52b/misc_fp.json','w'),indent=1)
