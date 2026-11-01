# Z2603 analysis: Liouville patterns of consecutive Type II slices N_3..N_3+k-1 at hard primes vs class-matched controls.
import numpy as np, sys, glob, json
rows=np.vstack([np.loadtxt(f,dtype=np.int64) for f in sorted(glob.glob(sys.argv[1]+'/c*.txt'))])
p,R,pat=rows[:,0],rows[:,1].astype(float),rows[:,2]
L=np.log(p); score=R/L**2; cls=p%840
rng=np.random.default_rng(1)
# within-class rank of score -> hard = bottom 10% within each class
hard=np.zeros(len(p),bool)
for c in np.unique(cls):
    idx=np.where(cls==c)[0]; o=idx[np.argsort(score[idx]+1e-9*rng.random(len(idx)))]
    hard[o[:max(1,len(idx)//10)]]=True
out={"n_primes":int(len(p)),"range":[int(p.min()),int(p.max())],"n_hard":int(hard.sum())}
def stat(k,hardmask):
    q=pat&((1<<k)-1); chi=0.0; tab=[]
    for v in range(1<<k):
        obs=0.0; exp=0.0
        for c in np.unique(cls):
            m=cls==c; nh=hardmask[m].sum(); f=(q[m]==v).mean()
            obs+=((q==v)&m&hardmask).sum(); exp+=nh*f
        chi+=(obs-exp)**2/exp if exp>0 else 0; tab.append((v,int(obs),round(exp,1)))
    return chi,tab
for k in (1,2,3,4):
    chi,tab=stat(k,hard)
    # permutation null: shuffle hard labels within class
    null=[]
    for t in range(200):
        hm=np.zeros(len(p),bool)
        for c in np.unique(cls):
            idx=np.where(cls==c)[0]; hm[rng.choice(idx,hard[idx].sum(),replace=False)]=True
        null.append(stat(k,hm)[0])
    null=np.array(null); pv=(1+(null>=chi).sum())/(1+len(null))
    out[f"k{k}"]={"chi2":round(chi,2),"df":2**k-1,"perm_p":round(pv,3),"null_mean":round(null.mean(),2),"table(pattern,obs_hard,exp_hard)":tab}
    print(k,chi,pv,null.mean(),tab if k<=2 else '')
# global pattern frequencies vs 2^-k (TT log-density prediction is for ALL n; here n=(p+3)/4 restricted to primes)
for k in (1,2,3):
    q=pat&((1<<k)-1); fr=np.bincount(q,minlength=1<<k)/len(q); out[f"freq_all_k{k}"]=[round(x,4) for x in fr]; print('freq',k,np.round(fr,4))
# correlation of lambda(N_3) with log R within class (demeaned)
lam0=np.where(pat&1,-1,1).astype(float); lr=np.log(R+1)
d1=lam0.copy(); d2=lr.copy()
for c in np.unique(cls):
    m=cls==c; d1[m]-=d1[m].mean(); d2[m]-=d2[m].mean()
out["corr_lambdaN3_logR_within_class"]=round(float(np.corrcoef(d1,d2)[0,1]),4)
s=np.zeros(len(p))
for i in range(4): s+=np.where(pat>>i&1,-1,1)
d3=s.copy()
for c in np.unique(cls):
    m=cls==c; d3[m]-=d3[m].mean()
out["corr_sum4lambda_logR_within_class"]=round(float(np.corrcoef(d3,d2)[0,1]),4)
print(out["corr_lambdaN3_logR_within_class"],out["corr_sum4lambda_logR_within_class"])
json.dump(out,open(sys.argv[2],'w'),indent=1)
