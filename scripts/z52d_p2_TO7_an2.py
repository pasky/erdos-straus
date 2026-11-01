# controls: Z2566 (sqf | omega), Z2560 (random-integer control of P1 law), Z2614 (within residue class), Z2430 (full Q)
import sys, math, random; sys.path.insert(0,'scripts')
import numpy as np
from z52d_p2_TO7_load import load, bits
a=load(); B=bits(a)
tsv=np.genfromtxt('data/z52b/pass2/TO7/slices_1e6_T400.tsv',delimiter='\t',names=True,dtype=np.int64)
P=tsv['p']; hard=tsv['hard']==1; nI=tsv['nI']; p840=tsv['p840']
print("== Z2566 sqf rate for type I, k=3 and all k, by omega and dh")
m0=a['type']==0
for w in range(1,6):
    s=m0&(a['omega']==w)
    print(f"omega={w}: dh=1 sqf {B['sqf'][s&B['dh']].mean():.3f} (n={np.sum(s&B['dh'])}) | dh=0 sqf {B['sqf'][s&~B['dh']].mean():.3f} (n={np.sum(s&~B['dh'])})")
print("== Z2560 control: P1 law for random integers in [M-range] (same sizes as (p+3)/4, p<=1e6)")
Ms=((P.astype(np.int64)+3)//4)
def P1s(n):
    # largest prime factor by trial over a sieve table
    return None
N=250001
spf=np.zeros(N+1,dtype=np.int64)
for i in range(2,N+1):
    if spf[i]==0:
        spf[i::i][spf[i::i]==0]=i
def lpf(n):
    m=n; best=1
    while m>1:
        q=spf[m]; best=max(best,q)
        while m%q==0: m//=q
    return best
rng=np.random.default_rng(1)
sample=rng.integers(1000, 250000, 40000)
u_rand=np.array([math.log(lpf(int(n)))/math.log(int(n)) for n in sample])
u_M=np.array([math.log(lpf(int(m)))/math.log(int(m)) for m in Ms[P>=1000]])
print("random-int u mean", round(u_rand.mean(),4), "P(u<=1/2)", round((u_rand<=0.5).mean(),4), "P(u<=1/3)", round((u_rand<=1/3).mean(),4))
print("M=(p+3)/4 u mean", round(u_M.mean(),4), "P(u<=1/2)", round((u_M<=0.5).mean(),4), "P(u<=1/3)", round((u_M<=1/3).mean(),4), "n", len(u_M))
print("== Z2614 within residue classes (hard, p<=1e6): mean nI by R-bin")
primesS=[3,5,7,11,13,17,19,23,29,31,37,41,43,47]
R=np.zeros(len(P),int)
for l in primesS:
    qr=set((x*x)%l for x in range(1,l))
    R+= np.array([(int(p)%l) in qr for p in P]).astype(int)
for r in [1,169,361,529]:
    s0=(p840==r)
    lo=s0&(R<=np.percentile(R[s0],33)); hi=s0&(R>=np.percentile(R[s0],67))
    print(f"class {r}: low-R n={lo.sum()} mean nI={nI[lo].mean():.3f} | high-R n={hi.sum()} mean nI={nI[hi].mean():.3f}")
