"""z52d pass2 TO6 controls: (a) Z2050 split vs nonsplit, residue-matched mod 840 and vs Mordell square classes;
(b) Z2023 correlation of log l(p) with log R(p) within size bins."""
import math, statistics as st
from sympy import primerange, legendre_symbol as L
import numpy as np
D='data/z52b/pass2/TO6/'
R = {int(a):int(b) for a,b in (l.split() for l in open(D+'R_primes_1e5.txt'))}
P1=[p for p in R if p%4==1 and p>5]
def sq840(p):  # p a square mod 840 (Mordell hard classes when p≡1 mod 4 ... as used in CONDITIONAL_ES §1)
    return any((x*x-p)%840==0 for x in range(840))
def split(p,ds): return all(L((p-d)%p,p)==1 for d in ds)
res={}
hardM=[p for p in P1 if sq840(p)]; nonM=[p for p in P1 if not sq840(p)]
res['mordell_square_mod840']=dict(n=len(hardM), mean=round(st.mean(R[p] for p in hardM),2), median=st.median(R[p] for p in hardM),
                                  n_non=len(nonM), mean_non=round(st.mean(R[p] for p in nonM),2), median_non=st.median(R[p] for p in nonM))
# (3,5,7) split == (p/3)=(p/5)=(p/7)=1 ; compare with square mod 840 membership
sp=[p for p in P1 if split(p,(3,5,7))]
res['split357_vs_sq840']=dict(n_split=len(sp), frac_also_sq840=round(sum(sq840(p) for p in sp)/len(sp),4),
   mean_split_not_sq840=round(st.mean(R[p] for p in sp if not sq840(p)),2) if any(not sq840(p) for p in sp) else None,
   mean_split_and_sq840=round(st.mean(R[p] for p in sp if sq840(p)),2) if any(sq840(p) for p in sp) else None)
# residue-matched: for each class mod 840 among P1, compare mean R of split(3,5,7) vs nonsplit; weight by count
diffs=[];wts=[]
from collections import defaultdict
byc=defaultdict(lambda:{True:[],False:[]})
for p in P1: byc[p%840][split(p,(3,5,7))].append(R[p])
for c,d in byc.items():
    if len(d[True])>=3 and len(d[False])>=3:
        diffs.append(st.mean(d[True])-st.mean(d[False])); wts.append(min(len(d[True]),len(d[False])))
res['matched_mod840_split357_minus_nonsplit']=dict(classes=len(diffs), weighted_mean_diff=round(float(np.average(diffs,weights=wts)),2) if diffs else None,
   frac_classes_negative=round(sum(1 for x in diffs if x<0)/max(1,len(diffs)),3))
# Z2023 size-controlled: corr(log l, log R) inside p-bins
from sympy import legendre_symbol
def lqnr(p):
    for q in primerange(2,10**4):
        if q!=p and L(q,p)==-1: return q
bins=[(5,1000),(1000,10000),(10000,100000)]
res['Z2023_within_size_bins']={}
for lo,hi in bins:
    sub=[p for p in P1 if lo<=p<hi]
    x=np.log([lqnr(p) for p in sub]); y=np.log([R[p] for p in sub])
    res['Z2023_within_size_bins'][f'[{lo},{hi})']=dict(n=len(sub), pearson=round(float(np.corrcoef(x,y)[0,1]),3))
# Z2023: does ℓ(p) carry info beyond the mod-840 class? mean R by (ℓ bucket) within class-matched residual
resid=[]; lls=[]
clsmean={c:st.mean(v) for c,v in byc.items() for v in [v[True]+v[False]] if len(v)>0}
for p in P1:
    c=p%840; resid.append(R[p]/clsmean[c]); lls.append(lqnr(p))
x=np.log(lls); y=np.log(resid)
res['Z2023_resid_after_mod840']=dict(pearson=round(float(np.corrcoef(x,y)[0,1]),3))
print(res)
import json; json.dump(res, open(D+'control_TO6.json','w'), indent=1)
