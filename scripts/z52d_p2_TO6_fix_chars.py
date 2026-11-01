"""z52d pass2 TO6 fix: Z2062/Z2107/Z2310/Z2337 (character decomposition of R(p) over classes mod 840),
Z2071 (singular-series-type product), Z2369 (large values of R), Z2359 (continued-fraction lengths of p/4).
Data: data/z52b/pass2/TO6/R_primes_1e5.txt (R(p) = #{x<=y<=z: 4/p=1/x+1/y+1/z})."""
import json, math, numpy as np
from sympy import primerange, legendre_symbol as L
from fractions import Fraction
D='data/z52b/pass2/TO6/'
R={int(a):int(b) for a,b in (l.split() for l in open(D+'R_primes_1e5.txt'))}
P1=[p for p in R if p%4==1 and p>5]
out={}
# ---- classes mod 840 with p≡1 mod 4 (H, 96 classes); class mean of R
Hc=sorted({p%840 for p in P1})
idx={c:i for i,c in enumerate(Hc)}
cnt=np.zeros(len(Hc)); sm=np.zeros(len(Hc)); sq=np.zeros(len(Hc))
for p in P1:
    i=idx[p%840]; cnt[i]+=1; sm[i]+=R[p]; sq[i]+=R[p]**2
mean=sm/cnt; var_within=(sq/cnt-mean**2)
# ---- real characters of (Z/840)^*: products of chi8 * chi3 * chi5 * chi7 (all ±1-valued, order ≤2)
def chi8(c,k):  # k in 0..3 : trivial, (-4/c), (8/c), (-8/c)
    c8=c%8
    if k==0: return 1
    if k==1: return 1 if c8%4==1 else -1
    if k==2: return 1 if c8 in (1,7) else -1
    return 1 if c8 in (1,3) else -1
def leg(c,q): return int(L(c%q,q)) if c%q else 0
basis=[]; labels=[]
for a in range(4):
  for b in range(2):
    for c5 in range(2):
      for c7 in range(2):
        f=[chi8(c,a)*(leg(c,3) if b else 1)*(leg(c,5) if c5 else 1)*(leg(c,7) if c7 else 1) for c in Hc]
        basis.append(f); labels.append((a,b,c5,c7))
B=np.array(basis,dtype=float).T          # classes x 32 real characters
rank=np.linalg.matrix_rank(B)
w=cnt                                      # weighted least squares by class counts
def fit_r2(X,y,w):
    Xw=X*np.sqrt(w)[:,None]; yw=y*np.sqrt(w)
    beta,*_=np.linalg.lstsq(Xw,yw,rcond=None)
    pred=X@beta
    ybar=np.average(y,weights=w)
    return 1-np.sum(w*(y-pred)**2)/np.sum(w*(y-ybar)**2)
one=np.ones((len(Hc),1))
r2_triv=fit_r2(one,mean,w)
r2_real=fit_r2(np.hstack([one,B]),mean,w)
# noise baseline: shuffle R among primes (keeps class sizes), recompute class means
rng=np.random.default_rng(1)
vals=np.array([R[p] for p in P1]); cls=np.array([idx[p%840] for p in P1])
base=[]
for _ in range(200):
    perm=rng.permutation(vals)
    m=np.array([perm[cls==i].mean() for i in range(len(Hc))])
    base.append(fit_r2(np.hstack([one,B]),m,w))
out['Z2062_Z2107_Z2310_Z2337']=dict(classes_H=len(Hc), real_char_rank=int(rank), real_chars=len(labels),
    r2_real_chars_over_mean=round(float(r2_real),4), r2_trivial=round(float(r2_triv),4),
    r2_real_null_shuffle_mean=round(float(np.mean(base)),4), r2_real_null_shuffle_95=round(float(np.percentile(base,95)),4),
    noninteracting_part_r2=round(float(1-r2_real),4))
# which real characters carry the signal: correlation of class means with each character (weighted)
sig=[]
for k,lab in enumerate(labels):
    x=B[:,k]
    if np.allclose(x,x[0]): continue
    beta=np.average((mean-np.average(mean,weights=w))*x, weights=w)/np.average((x-np.average(x,weights=w))**2,weights=w)
    sig.append((round(abs(beta),2),lab))
sig.sort(reverse=True)
out['Z2062_top_real_characters_(a8,b3,c5,d7)']=[ (lab,v) for v,lab in sig[:6]]
# ---- Z2071: singular-series-type product S(p) = prod_{3<=l<=L} (1 - (p/l)/(l-1)), correlation with R/log^2 p
def S(p,Lmax=100):
    s=1.0
    for l in primerange(3,Lmax+1):
        s*= (1-leg(p,l)/(l-1))
    return s
ps=P1
x=np.log([S(p) for p in ps]); y=np.log([R[p]/math.log(p)**2 for p in ps])
cl=np.array([p%840 for p in ps]); ym=np.array([mean[idx[c]] for c in cl])
out['Z2071_BH_product']=dict(corr_logS_logR_over_log2p=round(float(np.corrcoef(x,y)[0,1]),4),
    corr_logS_vs_classmean_logR=round(float(np.corrcoef(x,np.log(ym))[0,1]),4),
    corr_logS_logR_after_class_mean=round(float(np.corrcoef(x,np.log([R[p]/ mean[idx[p%840]] for p in ps]))[0,1]),4))
# ---- Z2369: large values of R(p)/log^2 p
vals_n=sorted(((R[p]/math.log(p)**2,p,p%840) for p in P1), reverse=True)[:10]
out['Z2369_top_R_over_log2']=[dict(p=p,c840=c,R=R[p],ratio=round(v,3), mordell_square_mod840=bool(any((x*x-p)%840==0 for x in range(840)))) for v,p,c in vals_n]
# ---- Z2359: continued-fraction lengths for p/4, primes p≡1 mod 4 <= 10^5 (regular CF and ceiling/negative CF)
def cf_len(fr):
    n,d=fr.numerator, fr.denominator; k=0
    while d:
        q=n//d; n,d=d,n-q*d; k+=1
    return k
def negcf_len(fr):
    k=0; x=fr
    while x.denominator!=1 and k<10**4:
        a=-((-x.numerator)//x.denominator)   # ceil
        x=Fraction(1)/(Fraction(a)-x)
        k+=1
    return k+1
L1=[];L2=[]
for p in P1[:2000]:
    L1.append(cf_len(Fraction(p,4))); L2.append(negcf_len(Fraction(p,4)))
out['Z2359_CF_lengths_p_over_4_first2000']=dict(regular_median=int(np.median(L1)), regular_max=max(L1),
    negative_ceiling_median=int(np.median(L2)), negative_ceiling_max=max(L2), mean_log_p=round(float(np.mean([math.log(p) for p in P1[:2000]])),2))
json.dump(out, open(D+'chars_TO6.json','w'), indent=1, default=float)
print(json.dumps(out, default=float, indent=0)[:5000])
