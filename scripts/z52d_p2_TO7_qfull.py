# Z2430: full quotient test for prime slices e=k (Type II, M=(p+k)/4): -1 in Q_M = {a/b mod k : a*b | M}  (a+b ≡ 0 mod k, ab|M)
# compared with: gen = -1 in <prime-factor residues of M mod k>, and dh = a=1 divisor test (b|M, b≡-1 mod k).
import sys; sys.path.insert(0,'scripts')
import numpy as np, math
from z52d_p2_TO7_load import load, bits
a_=load(); B=bits(a_)
tsv=np.genfromtxt('data/z52b/pass2/TO7/slices_1e6_T400.tsv',delimiter='\t',names=True,dtype=np.int64)
hardp=set(int(x) for x in tsv['p'][tsv['hard']==1])
N=1000001
spf=np.zeros(N+1,dtype=np.int64)
for i in range(2,int(N**0.5)+1):
    if spf[i]==0:
        idx=np.arange(i*i,N+1,i); m=spf[idx]==0; spf[idx[m]]=i
def divisors(n):
    ds=[1]; m=n
    while m>1:
        q=int(spf[m]) or m; e=0
        while m%q==0: m//=q; e+=1
        ds=[d*q**j for d in ds for j in range(e+1)]
    return np.array(sorted(ds),dtype=np.int64)
res={}
for k in [7,11,19,23,31]:
    cnt=dict(n=0,Q=0,gen=0,dh=0,Q_and_notdh=0,gen_and_notQ=0)
    for p in sorted(hardp):
        if (p+k)%4: continue
        M=(p+k)//4
        if M<2: continue
        D=divisors(M)
        A=D[:,None]; Bm=D[None,:]
        ok=((M % (A*Bm))==0) & (((A+Bm)%k)==0)
        Qhit=bool(ok.any())
        # per-record flags
        pass
        cnt['n']+=1; cnt['Q']+=Qhit
    res[k]=cnt
    # flags from binary table for same (p,k,type1)
    m=(a_['k']==k)&(a_['type']==1)&np.isin(a_['p'],np.array(sorted(hardp)))
    gen=B['gen'][m].mean(); dh=B['dh'][m].mean()
    print(f"k={k}: hard primes n={cnt['n']}  -1 in Q: {cnt['Q']/cnt['n']:.4f}  -1 in <res>: {gen:.4f}  a=1 divisor hit: {dh:.4f}")
