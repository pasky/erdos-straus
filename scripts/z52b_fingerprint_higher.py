"""Do higher-power residue characters of small primes (cubic/quartic/octic) influence ES counts beyond quadratic ones?
Within strata of fixed quadratic profile (Legendre symbols of 2,3,5,7), compare mean residual log U(p) by r-th power residuosity."""
import numpy as np, json, math
from sympy import isprime
from scipy.stats import mannwhitneyu
R='data/z52b/raw/'
F=np.loadtxt(R+'f4_all_30000.txt',dtype=np.int64)
FP=np.vstack([F[[isprime(int(x)) for x in F[:,0]]],np.loadtxt(R+'pr_20001_200000.txt',dtype=np.int64)])
FP=FP[np.argsort(FP[:,0])]; FP=FP[np.concatenate([[True],np.diff(FP[:,0])>0])]
FP=FP[(FP[:,0]%4==1)&(FP[:,0]>100)]; P=FP[:,0]; lp=np.log(P.astype(float))
W=np.load(R+'words_3e6.npy')
def resid(y):
    X=np.vstack([np.ones_like(lp),lp,np.log(lp)]).T; return y-X@np.linalg.lstsq(X,y,rcond=None)[0]
targets={'U':resid(np.log(FP[:,1]+1.0)),'k1':resid(np.log(FP[:,10]+1.0)),'k2':resid(np.log(FP[:,11]+1.0)),'R':resid(np.log(W[P-1,3]+1.0))}
def leg(a,p): return pow(a,(p-1)//2,p)==1
quad=np.array([[leg(q,int(p)) for q in (2,3,5,7)] for p in P])
out={}
tests=[]
for r in (3,4,8):
    for a in (2,3,5,7):
        tests.append((r,a))
for r,a in tests:
    elig=np.array([(int(p)-1)%r==0 and leg(a,int(p)) for p in P])  # a must be a QR for r-th power question (r even); for r=3 require p≡1 mod 3
    if r==3: elig=np.array([(int(p)-1)%3==0 for p in P])
    isres=np.array([pow(a,(int(p)-1)//r,int(p))==1 for p in P])
    for tn,t in targets.items():
        # stratify by quadratic profile, compare within strata
        diffs=[];ws=[]
        for prof in set(map(tuple,quad[elig])):
            s=elig&(quad==prof).all(1)
            a1=t[s&isres]; a0=t[s&~isres]
            if len(a1)>20 and len(a0)>20: diffs.append(a1.mean()-a0.mean()); ws.append(min(len(a1),len(a0)))
        if ws:
            d=float(np.average(diffs,weights=ws)); 
            # pooled z via permutation-free approx: within-stratum t-test aggregated
            s=elig; a1=t[s&isres]; a0=t[s&~isres]
            pv=float(mannwhitneyu(a1,a0).pvalue)
            out[f'{tn}: {a} is {r}-th power residue']=dict(stratified_mean_diff=round(d,4),n_res=int((elig&isres).sum()),n_non=int((elig&~isres).sum()),mw_p_unstratified=pv)
            print(tn,a,r,out[f'{tn}: {a} is {r}-th power residue'],flush=True)
for m in (16,32,9,27,25,49):
    for tn,t in targets.items():
        g=np.array([(int(p)-1)%m==0 for p in P]); base=np.array([(int(p)-1)%(m//(2 if m in(16,32) else int(round(m**(1/ (2 if m in (9,25,49) else 3)))) ))==0 for p in P])
        a1=t[g]; a0=t[base&~g]
        out[f'{tn}: p≡1 mod {m} vs p≡1 mod smaller power, not mod {m}']=dict(diff=round(float(a1.mean()-a0.mean()),4),n1=int(g.sum()),n0=int((base&~g).sum()))
        print(tn,m,out[f'{tn}: p≡1 mod {m} vs p≡1 mod smaller power, not mod {m}'])
json.dump(out,open('data/z52b/higher_residue.json','w'),indent=1)
