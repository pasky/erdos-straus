# z52d Pass 2 NC0 — items Z0474 (family-indicator covariance), Z0922 (dispersion vs last exception), Z0877 (primitive-failure ∩ R-zeros)
# Uses data/z52b/raw/var_pr_1e5.txt (cols: p, U, then family k at col 2+k; names as in scripts/z52b_fingerprint_variants_an.py)
import numpy as np, json, math
from scipy.stats import hypergeom
R='data/z52b/raw/'
A=np.loadtxt(R+'var_pr_1e5.txt',dtype=np.int64)
names=['0 even','1 even','2 even','3 all even','primitive','x,y|z','x|y','isosceles','all squarefree','z<=n^2','z<=n^1.5','some power of 2','x or y prime','some coprime pair','no denom div 3','some denom div 4']
P=A[:,0]; sel=(P%24==1)
print('primes<=1e5, p≡1 mod 24:', sel.sum(), ' all p≡1 mod4:', (P%4==1).sum())
# Z0474: indicators (family has >=1 solution at p)
I=np.stack([(A[sel,2+k]>0) for k in range(16)],axis=1).astype(float)
C=np.corrcoef(I.T)
print('Z0474 family indicator correlations (p≡1 mod 24), max |offdiag| and pairs >0.5:')
pairs=[(names[i],names[j],round(C[i,j],2)) for i in range(16) for j in range(i+1,16) if abs(C[i,j])>0.5]
print(len(pairs),'pairs with |r|>0.5 of',16*15//2); print(pairs[:12])
print('freq of solvable (p≡1 mod24):',{names[k]:round(I[:,k].mean(),3) for k in range(16)})
# Z0922: mean, CV of counts in [5e4,1e5], p≡1 mod 4; last exception
s=(P%4==1)&(P>50000)&(P<=100000)
rows=[]
for k in range(16):
    c=A[s,2+k].astype(float); m=c.mean(); cv=c.std()/m if m>0 else float('nan')
    z=P[(A[:,2+k]==0)&(P>5)]; last=int(z.max()) if len(z) else 0
    rows.append((names[k],round(m,2),round(cv,3),last,int((A[:,2+k]==0)[(P>5)].sum())))
rows.sort(key=lambda r:r[1])
print('Z0922 (name, mean, CV, last exception<=1e5, #exceptions<=1e5):')
for r in rows: print(r)
from scipy.stats import spearmanr
nz=[r for r in rows if r[3]>0 and r[2]==r[2]]
rho=spearmanr([r[2] for r in nz],[r[3] for r in nz]); print('spearman(CV, last) over families with exceptions:',rho, len(nz))
rho2=spearmanr([r[1] for r in nz],[r[3] for r in nz]); print('spearman(mean, last):',rho2)
# Z0877: primitive failures among primes ≡1 mod 4 (<=1e5); R-zeros from words sieve
Pf=P[(A[:,6]==0)&(P>5)]
print('primitive failures (p>5):',len(Pf),'head',Pf[:12].tolist(),'tail',Pf[-5:].tolist())
RZ=np.loadtxt('data/z52b/pass1/U09/R_primes1mod4_le2e5.txt',dtype=np.int64,usecols=(0,1))   # p, R(p) (pass1 U09 core)
allp=[int(p) for p in RZ[:,0] if p<=100000]
Rz=[int(p) for p in RZ[:,0] if p<=98713 and RZ[RZ[:,0]==p,1][0]==0]
print('R-zeros (p<=98713, p≡1 mod4):',Rz)
Ncand=len(allp); K=len(Pf); M=len(Rz)
ov=len(set(Pf.tolist())&set(Rz))
pval=hypergeom.sf(ov-1,Ncand,M,K)
print('Z0877 overlap',ov,'of R-zeros',M,'primitive-fail',K,'universe',Ncand,'hypergeom P(X>=ov)=',pval)
json.dump({'primitive_fail_count':int(K),'R_zeros':Rz,'overlap':ov,'p_value':float(pval),'universe':Ncand,'family_table':rows,'spearman_CV_last':[float(rho.statistic),float(rho.pvalue)],'spearman_mean_last':[float(rho2.statistic),float(rho2.pvalue)]},open('data/z52b/pass2/NC0/families_summary.json','w'),indent=1,default=str)
