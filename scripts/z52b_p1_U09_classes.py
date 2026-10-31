# z52b pass1 U09 (Z1980/Z1609/Z1534 follow-up): is the mod-840 class dependence of R(p)/log^2 p explained by
# local densities at 2, 3, 5, 7 (the (★) equation's p-adic factors)?  Usage: python3 scripts/z52b_p1_U09_classes.py <R file>
import sys, numpy as np, math
from scipy.stats import spearmanr
rows=[list(map(int,l.split())) for l in open(sys.argv[1])]
P=np.array([r[0] for r in rows]); R=np.array([r[1] for r in rows],dtype=float)
y = R/np.log(P.astype(float))**2
def local(q, k):
    m=q**k; r=np.arange(m)
    u,B,C=np.meshgrid(r,r,r,indexing='ij')
    cnt=np.bincount(((4*u*B*C-u-B)%m).ravel(),minlength=m)/m**2
    return cnt[P%m]
def r2(groups):
    # R^2 of group means
    g={}
    for k,v in zip(map(tuple,groups),y): g.setdefault(k,[]).append(v)
    pred=np.array([np.mean(g[tuple(k)]) for k in groups])
    return 1-np.sum((y-pred)**2)/np.sum((y-y.mean())**2)
print("R^2 of class-means mod 840 (96 classes):", round(r2(np.stack([P%840],1)),3))
for name,mods in [("mod 8",[8]),("mod 3",[3]),("mod 5",[5]),("mod 7",[7]),("mod 24",[24]),("mod 8·3·5·7",[8,3,5,7])]:
    key=np.stack([P%m for m in mods],1)
    print(f"R^2 of class-means {name}:", round(r2(key),3))
S2=local(2,3); S3=local(3,1); S5=local(5,1); S7=local(7,1)
for name,v in [("N_8(p)",S2),("N_3(p)",S3),("N_5(p)",S5),("N_7(p)",S7)]:
    print(f"Spearman corr({name}, R/log^2 p) = {spearmanr(v,y).correlation:.3f}")
Sl=np.log(S2)+np.log(S3)+np.log(S5)+np.log(S7)
print("Spearman corr(log prod local N_{8,3,5,7}, R/log^2 p) =", round(spearmanr(Sl,y).correlation,3))
print("R^2 of mean-by-(p mod 840) after regressing on log S_{8,3,5,7}:")
X=np.stack([np.ones(len(y)),Sl],1); beta=np.linalg.lstsq(X,y,rcond=None)[0]
res=y-X@beta
g={}
for k,v in zip(P%840,res): g.setdefault(int(k),[]).append(v)
print("   residual class-mean R^2 (fraction of residual variance explained by mod-840 classes):", round(1-np.sum((res-np.array([np.mean(g[int(k)]) for k in P%840]))**2)/np.sum((res-res.mean())**2),3))
