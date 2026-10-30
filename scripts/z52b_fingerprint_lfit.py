"""Fit log(count+1) ~ a + b log p + c loglog p + alpha*log L_Q(chi) for several targets/characters/truncations Q."""
import numpy as np, json
from sympy import primerange, legendre_symbol, jacobi_symbol
R='data/z52b/raw/'
A=np.load(R+'classical_feat.npy'); names=json.load(open(R+'classical_feat_names.json'))
P=A[0].astype(np.int64)
import sys
sys.path.insert(0,'scripts')
from sympy import isprime
F=np.loadtxt(R+'f4_all_30000.txt',dtype=np.int64)
FP=np.vstack([F[[isprime(int(x)) for x in F[:,0]]],np.loadtxt(R+'pr_20001_200000.txt',dtype=np.int64)])
FP=FP[np.argsort(FP[:,0])]; FP=FP[np.concatenate([[True],np.diff(FP[:,0])>0])]
FP=FP[(FP[:,0]%4==1)&(FP[:,0]>100)]; assert (FP[:,0]==P).all()
W=np.load(R+'words_3e6.npy')
lp=np.log(P.astype(float))
def LQ(Q, twist):
    out=np.zeros(len(P))
    for q in primerange(2,Q+1):
        if twist=='p': chi=np.array([legendre_symbol(q,int(p)) for p in P])
        elif twist=='-4p': chi=np.array([0 if q==2 else jacobi_symbol(-int(p),q) for p in P])  # chi_{-4p}(q)=(-p/q)
        elif twist=='-p': chi=np.array([jacobi_symbol(-int(p),q) if q>2 else (1 if (-p)%8==1 else -1) for p in P])
        out+= -np.log(1-chi.astype(float)/q)
    return out
targets={'U':FP[:,1],'k1 (one denom div p)':FP[:,10],'k2 (two denoms div p)':FP[:,11],'R(p) (★)':W[P-1,3],'Uv(p)':W[P-1,4],'I3(p)':W[P-1,2],'W(p)':W[P-1,1],'ESC(p)':W[P-1,5]}
base=np.vstack([np.ones_like(lp),lp,np.log(lp)]).T
out={}
for tn,t in targets.items():
    y=np.log(t.astype(float)+1)
    r0=y-base@np.linalg.lstsq(base,y,rcond=None)[0]; v0=r0.var()
    for twist in ['p','-4p']:
        for Q in [2,3,5,7,13,31,100,1000]:
            x=LQ(Q,twist); X=np.hstack([base,x[:,None]]); b=np.linalg.lstsq(X,y,rcond=None)[0]; r=y-X@b
            out[f'{tn}|{twist}|Q={Q}']=dict(alpha=round(float(b[-1]),3),R2_gain=round(float(1-r.var()/v0),3))
            print(tn,twist,Q,out[f'{tn}|{twist}|Q={Q}'],flush=True)
json.dump(out,open('data/z52b/lfit.json','w'),indent=1)
