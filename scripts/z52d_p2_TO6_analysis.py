"""z52d pass2 TO6 analysis: Z2023 (least non-residue vs R(p)), Z2050 (total splitting vs R(p)), Z2378 (smoothness of t_min)
Inputs: data/z52b/pass2/TO6/R_primes_1e5.txt  (p, R(p) = #{x<=y<=z: 4/p=1/x+1/y+1/z}; egypt3 count mode)
        data/z52b/pass2/TO6/tmin_p1mod4_1e6.txt (p, t_min, sqrt p, ratio)
Memory: tiny."""
import math, statistics as st
from sympy import primerange, legendre_symbol as L, factorint
D='data/z52b/pass2/TO6/'
R = {int(a):int(b) for a,b in (l.split() for l in open(D+'R_primes_1e5.txt'))}
T = {int(r[0]):int(r[1]) for r in (l.split() for l in open(D+'tmin_p1mod4_1e6.txt'))}
def lqnr(p):
    for q in primerange(2, 10**4):
        if q!=p and L(q,p)==-1: return q
def ok(p): return p%4==1
P1 = [p for p in R if p%4==1 and p>5]
out={}
# Z2023: least QNR l(p) vs R(p) for p ≡ 1 mod 4 <= 1e5
rows=[(p,lqnr(p),R[p]) for p in P1]
bins={}
for p,l,r in rows:
    key = 'l<=5' if l<=5 else ('l<=11' if l<=11 else ('l<=23' if l<=23 else 'l>23'))
    bins.setdefault(key,[]).append(r)
out['Z2023']={k:dict(n=len(v),mean_R=round(st.mean(v),2),median_R=st.median(v),min_R=min(v)) for k,v in bins.items()}
# corr of log l and log R
import numpy as np
x=np.log([l for _,l,_ in rows]); y=np.log([r for _,_,r in rows])
out['Z2023']['pearson_logl_logR']=round(float(np.corrcoef(x,y)[0,1]),4)
# t_min vs l(p) on overlap
tt=[(lqnr(p),T[p]) for p in P1 if p in T and p<=10**5]
x2=np.log([a for a,_ in tt]); y2=np.log([b for _,b in tt])
out['Z2023']['pearson_logl_logtmin']=round(float(np.corrcoef(x2,y2)[0,1]),4)
out['Z2023']['n_pairs_tmin']=len(tt)
# Z2050: total splitting in Q(i, sqrt-3, sqrt-5, sqrt-7, sqrt-11) i.e. (-d/p)=1 for d in 3,5,7,11 (p≡1 mod 4)
def split(p,ds): return all(L(-d%p if False else (p-d)%p, p)==1 for d in ds)
for ds in [(3,),(3,5),(3,5,7),(3,5,7,11)]:
    s=[R[p] for p in P1 if all(legendre_symbol(-d % p, p)==1 for d in ds)] if False else None
from sympy import legendre_symbol
res={}
for ds in [(3,),(3,5),(3,5,7),(3,5,7,11),(3,5,7,11,13)]:
    S=[];N=[]
    for p in P1:
        (S if all(legendre_symbol((p-d)%p,p)==1 for d in ds) else N).append(R[p])
    res[str(ds)]=dict(n_split=len(S), mean_R_split=round(st.mean(S),2) if S else None,
                      median_split=st.median(S) if S else None,
                      n_nonsplit=len(N), mean_R_nonsplit=round(st.mean(N),2) if N else None,
                      median_nonsplit=st.median(N) if N else None)
out['Z2050']=res
# Z2378: smoothness of t_min with y=(log p)^2 for p<=1e6; and for hard primes t_min>=30
def ysmooth(t,y):
    return all(q<=y for q in factorint(t))
sm_all=[]; sm_hard=[]
for p,t in T.items():
    if t==0: continue
    y=(math.log(p))**2
    s=ysmooth(t,y); sm_all.append(s)
    if t>=30: sm_hard.append(s)
out['Z2378']=dict(frac_tmin_ysmooth_all=round(sum(sm_all)/len(sm_all),4), n_all=len(sm_all),
                   frac_tmin_ysmooth_hard_t_ge30=round(sum(sm_hard)/len(sm_hard),4), n_hard=len(sm_hard))
print(out)
import json; json.dump(out, open(D+'analysis_TO6.json','w'), indent=1)
