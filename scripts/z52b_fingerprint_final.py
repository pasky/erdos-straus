"""Final quick checks: height constant, lag-840 prime correlation, propagation to 4p+1 and (p+3)/4, lowest composites,
easy class 839 mod 840, Tunnell ternary counts vs residual U."""
import numpy as np, json, math
from sympy import isprime
from scipy.stats import spearmanr
R='data/z52b/raw/'
F=np.loadtxt(R+'f4_all_30000.txt',dtype=np.int64); Ud=dict(zip(F[:,0].tolist(),F[:,1].tolist()))
FP=np.vstack([F[[isprime(int(x)) for x in F[:,0]]],np.loadtxt(R+'pr_20001_200000.txt',dtype=np.int64)])
FP=FP[np.argsort(FP[:,0])]; FP=FP[np.concatenate([[True],np.diff(FP[:,0])>0])]
P=FP[:,0]; out={}
h=FP[:,4]/P.astype(float)**2; i=int(np.argmax(h[P>100])); out['max_minz_over_p2']=(float(h[P>100][i]),int(P[P>100][i]))
hh=np.log(FP[:,4].astype(float))/np.log(P.astype(float)); j=int(np.argmax(hh[P>1000])); out['max_log_minz_over_logp_p>1000']=(float(hh[P>1000][j]),int(P[P>1000][j]))
lp=np.log(P.astype(float)); X=np.vstack([np.ones_like(lp),lp,np.log(lp)]).T
y=np.log(FP[:,1]+1.0); r=y-X@np.linalg.lstsq(X,y,rcond=None)[0]; rd=dict(zip(P.tolist(),r.tolist()))
pairs=[(rd[p],rd[p+840]) for p in P.tolist() if p%4==1 and p+840 in rd]
out['lag840_prime_resid_corr']=float(np.corrcoef(*zip(*pairs))[0,1]); out['lag840_pairs']=len(pairs)
pairs=[(rd[p],rd[p+840*7]) for p in P.tolist() if p%4==1 and p+840*7 in rd]
out['lag5880_prime_resid_corr']=float(np.corrcoef(*zip(*pairs))[0,1])
a=[(Ud[p],Ud[4*p+1]) for p in P.tolist() if p%4==1 and 4*p+1<=30000]
b=[(Ud[p],Ud[(p+3)//4]) for p in P.tolist() if p%4==1 and p<=30000 and (p+3)//4>=2]
out['spearman_U(p)_U(4p+1)']=float(spearmanr(*zip(*a))[0]); out['spearman_U(p)_U((p+3)/4)']=float(spearmanr(*zip(*b))[0])
comp=[(u/math.log(n)**3,n) for n,u in Ud.items() if n>100 and not isprime(n)]
out['lowest_composites']=[(round(v,4),n) for v,n in sorted(comp)[:12]]
s3=(P%4==3)&(P>1000); ratio=FP[:,1]/lp**3
out['mean_U/log3_p839mod840']=float(ratio[s3&(P%840==839)].mean()); out['mean_U/log3_other_3mod4']=float(ratio[s3&(P%840!=839)].mean())
# Tunnell counts for p ≡ 1 (8) ≤ 20000
def rep(n,a,b,c):
    cnt=0
    for yv in range(0,int(math.isqrt(n//b))+1):
        for zv in range(0,int(math.isqrt(max(0,(n-b*yv*yv)//c)))+1):
            t=n-b*yv*yv-c*zv*zv
            if t<0: break
            if t%a==0:
                s=math.isqrt(t//a)
                if s*s==t//a: cnt+= (1 if s==0 else 2)*(1 if yv==0 else 2)*(1 if zv==0 else 2)
    return cnt
sel=[p for p in P.tolist() if p%8 in (1,3) and 100<p<=20000]
A=np.array([rep(p,1,2,8) for p in sel]); B=np.array([rep(p,1,2,32) for p in sel])
rr=np.array([rd[p] for p in sel])
out['tunnell_spearman_A']=float(spearmanr(rr,A)[0]); out['tunnell_spearman_B']=float(spearmanr(rr,B)[0]); out['tunnell_spearman_A-2B']=float(spearmanr(rr,A-2*B)[0])
out['tunnell_n']=len(sel)
print(json.dumps(out,indent=1))
json.dump(out,open('data/z52b/final_checks.json','w'),indent=1)
