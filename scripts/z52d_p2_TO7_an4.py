# Z2639 follow-up: does the residue-class effect on mean nI (hard classes mod 840) survive conditioning on R(p)=#{3<=l<=47 prime: (l/p)=1}?
import numpy as np
tsv=np.genfromtxt('data/z52b/pass2/TO7/slices_1e6_T400.tsv',delimiter='\t',names=True,dtype=np.int64)
P=tsv['p']; nI=tsv['nI']; p840=tsv['p840']; hard=tsv['hard']==1
ls=[3,5,7,11,13,17,19,23,29,31,37,41,43,47]
R=np.zeros(len(P),int)
for l in ls:
    qr=set((x*x)%l for x in range(1,l))
    R+=np.array([(int(p)%l) in qr for p in P]).astype(int)
rs=[1,121,169,289,361,529]
for r in rs:
    s=(p840==r)&(P>=1000)
    print(f"class {r}: n={s.sum()} mean R={R[s].mean():.3f} mean nI={nI[s].mean():.3f}")
# OLS nI ~ class dummies + R (hard primes, p>=1000)
s=hard&(P>=1000)
X=np.column_stack([np.ones(s.sum())]+[(p840[s]==r).astype(float) for r in rs[1:]]+[R[s].astype(float)])
b,res,rk,sv=np.linalg.lstsq(X,nI[s].astype(float),rcond=None)
print("coef on R (class-adjusted):", round(b[-1],3))
X0=X[:,:-1]; b0=np.linalg.lstsq(X0,nI[s].astype(float),rcond=None)[0]
print("class coefs without R:", np.round(b0[1:],3))
print("class coefs with R:   ", np.round(b[1:-1],3))
