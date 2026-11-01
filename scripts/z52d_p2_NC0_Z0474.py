# z52d Pass 2 NC0, item Z0474 — covariance of the 50 most frequent certificate families over p≡1 (mod 24), p≤PMAX.
# Families = the (a,d)-Type I and (a,b)-Type II congruence families of scripts/z52b_dividing_leastfam.py (family with s=ad or ab):
# p is solved by family F iff p mod m_F ∈ R_F (exact, from divisors). Rank families by frequency over the window, take top 50.
import numpy as np, sys, json
from sympy import divisors, primerange
PMAX=int(sys.argv[1]) if len(sys.argv)>1 else 10**6
ps=np.array([p for p in primerange(5,PMAX) if p%24==1],dtype=np.int64)
fams=[]
X=60
for a in range(1,X+1):
    for d in range(1,X//a+1):
        m=4*a*d; R={(-f)%m for f in divisors(4*a*a*d+1)}
        fams.append(('I',a,d,m,R))
for a in range(1,X+1):
    for b in range(a,X//a+1):
        m=4*a*b; R={(-e)%m for e in divisors(a+b)}
        fams.append(('II',a,b,m,R))
ind={}
for f in fams:
    typ,a,b,m,R=f
    tab=np.zeros(m,dtype=bool); tab[list(R)]=True
    v=tab[ps%m]
    ind[(typ,a,b)]=(v.mean(),v)
ranked=sorted(ind.items(),key=lambda kv:-kv[1][0])
top=[]; seen=set()
for k,(fr,v) in ranked:          # drop families whose indicator vector duplicates an earlier one (identical solved sets)
    h=v.tobytes()
    if h in seen or fr==0: continue
    seen.add(h); top.append((k,(fr,v)))
    if len(top)==50: break
print('distinct indicator vectors among top ranks:',len(top))
M=np.stack([v for _,(fr,v) in top],axis=1).astype(float)
freq=np.array([fr for _,(fr,v) in top])
C=np.corrcoef(M.T)
n=len(top); iu=np.triu_indices(n,1)
r=C[iu]
print('primes p≡1 mod 24, p<=%d: %d'%(PMAX,len(ps)))
print('top-50 family frequency range: %.3f .. %.3f'%(freq.min(),freq.max()))
print('pairs: %d; |r|>0.3: %d; |r|>0.1: %d; max |r| = %.3f; mean r = %.3f'%(len(r),(np.abs(r)>0.3).sum(),(np.abs(r)>0.1).sum(),np.abs(r).max(),r.mean()))
top_pairs=sorted(zip(np.abs(r),[ (top[i][0],top[j][0]) for i,j in zip(*iu)]),key=lambda t:-t[0])[:5]
for val,(k1,k2) in top_pairs: print('  |r|=%.3f  %s  %s'%(val,k1,k2))
json.dump({'PMAX':PMAX,'n_primes':int(len(ps)),'families':[str(k) for k,_ in top],'freq':freq.tolist(),
           'n_pairs':int(len(r)),'n_abs_gt_0.3':int((np.abs(r)>0.3).sum()),'n_abs_gt_0.1':int((np.abs(r)>0.1).sum()),'max_abs':float(np.abs(r).max()),'mean_r':float(r.mean())},
          open(f'data/z52b/pass2/NC0/covariance_{PMAX}.json','w'),indent=1)
