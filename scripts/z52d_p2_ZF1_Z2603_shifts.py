# Z2603 follow-up: per-shift single-lambda bias (hard vs class-matched), and whether it is explained by N_e prime.
import numpy as np, sys, glob, json
from sympy import isprime
rows=np.vstack([np.loadtxt(f,dtype=np.int64) for f in sorted(glob.glob(sys.argv[1]+'/c*.txt'))])
p,R,pat=rows[:,0],rows[:,1].astype(float),rows[:,2]
score=R/np.log(p)**2; MOD=int(sys.argv[3]) if len(sys.argv)>3 else 840; cls=p%MOD; rng=np.random.default_rng(1)
hard=np.zeros(len(p),bool)
for c in np.unique(cls):
    idx=np.where(cls==c)[0]; o=idx[np.argsort(score[idx]+1e-9*rng.random(len(idx)))]; hard[o[:max(1,len(idx)//10)]]=True
N=(p+3)//4; out={}
def zt(x):  # stratified hard-vs-class difference of mean of x, z-score
    o=e=v=0.0
    for c in np.unique(cls):
        m=cls==c; nh=hard[m].sum(); mu=x[m].mean(); var=x[m].var(); n=m.sum()
        o+=x[m&hard].sum(); e+=nh*mu; v+=nh*var*(1-nh/n)
    return (o-e)/np.sqrt(v), o/hard.sum(), e/hard.sum()
for i in range(8):
    lm=((pat>>i)&1).astype(float)  # 1 if lambda(N+i)=-1
    pr=np.array([isprime(int(n)) for n in N+i],float)
    z,a,b=zt(lm); zp,ap,bp=zt(pr)
    # lambda effect after removing prime N+i
    keep=pr==0
    out[f"shift_e{3+4*i}"]={"z_lambda":round(z,2),"P(l=-1|hard)":round(a,4),"P(l=-1|ctrl)":round(b,4),"z_Nprime":round(zp,2),"P(prime|hard)":round(ap,4),"P(prime|ctrl)":round(bp,4)}
    print(3+4*i,out[f"shift_e{3+4*i}"])
out["MOD"]=MOD; json.dump(out,open(sys.argv[2],'w'),indent=1)
