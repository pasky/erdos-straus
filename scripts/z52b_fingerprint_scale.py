"""Out-of-sample checks at p≈1e6, 1e7 windows: Spearman(U, L_Q(1,chi_p)), k1/k2, and h(-4p) mod 8 (Rédei 4-/8-rank) effects at p<=2e5."""
import numpy as np, json, math
from sympy import legendre_symbol, primerange, isprime
from scipy.stats import spearmanr
import cypari2
pari=cypari2.Pari()
R='data/z52b/raw/'
def LQ(p,Q=31): return sum(-math.log(1-int(legendre_symbol(q,p))/q) for q in primerange(2,Q+1))
out={}
for f in ['pr_1e6_window.txt','pr_1e7_window.txt']:
    A=np.loadtxt(R+f,dtype=np.int64); A=A[A[:,0]%4==1]
    L=np.array([LQ(int(p)) for p in A[:,0]])
    out[f]=dict(n=len(A),spearman_U_logL=float(spearmanr(A[:,1],L)[0]),spearman_k1_logL=float(spearmanr(A[:,10],L)[0]),spearman_k2_logL=float(spearmanr(A[:,11],L)[0]),
                median_ratio=float(np.median(A[:,1]/np.log(A[:,0])**2)),median_k1_over_k2=float(np.median(A[:,10]/A[:,11])))
    print(f,out[f])
F=np.loadtxt(R+'f4_all_30000.txt',dtype=np.int64)
FP=np.vstack([F[[isprime(int(x)) for x in F[:,0]]],np.loadtxt(R+'pr_20001_200000.txt',dtype=np.int64)])
FP=FP[np.argsort(FP[:,0])]; FP=FP[np.concatenate([[True],np.diff(FP[:,0])>0])]
S=FP[(FP[:,0]%8==1)&(FP[:,0]>100)]; P=S[:,0]; lp=np.log(P.astype(float))
h=np.array([int(pari.qfbclassno(-4*int(p))) for p in P])
W=np.load(R+'words_3e6.npy')
def resid(y):
    X=np.vstack([np.ones_like(lp),lp,np.log(lp)]).T; return y-X@np.linalg.lstsq(X,y,rcond=None)[0]
for tn,t in [('U',S[:,1]),('k1',S[:,10]),('k2',S[:,11]),('R',W[P-1,3])]:
    r=resid(np.log(t+1.0))
    d={int(m):round(float(r[h%16==m].mean()),4) for m in (0,4,8,12)}
    out[f'{tn} residual by h(-4p) mod 16 (p≡1 mod 8)']=d; print(tn,d)
json.dump(out,open('data/z52b/scale_checks.json','w'),indent=1)
