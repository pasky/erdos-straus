# Analyses for Z2429, Z2430(partial), Z2566, Z2560, Z2614, Z2581, Z2639 on /tmp/feat_1e6.bin (+ slices TSV)
import sys, math; sys.path.insert(0,'scripts')
import numpy as np
from z52d_p2_TO7_load import load, bits
a=load(); B=bits(a)
tsv=np.genfromtxt('data/z52b/pass2/TO7/slices_1e6_T400.tsv',delimiter='\t',names=True,dtype=np.int64)
P=tsv['p']; hard=tsv['hard']==1; nI=tsv['nI']; nII=tsv['nII']; p840=tsv['p840']
def isprime(n): 
    return n>1 and all(n%d for d in range(2,int(n**0.5)+1))
print("== Z2429: prime slices k, Type II (M=(p+k)/4): fraction with -1 NOT in <prime factors of M> (i.e. |H| odd)")
for kk in [3,7,11,19,23,31,43,47,59,67,71,79,83,103,107,127,131,139,151,163,167,179,191,199]:
    m=(a['k']==kk)&(a['type']==1)&(a['p']>=5)
    if m.sum()==0: continue
    hm=m & np.isin(a['p'],P[hard])
    g=B['gen']
    print(f"k={kk:4d} all: n={m.sum():6d} notgen={(~g[m]).mean():.4f} | hard: n={hm.sum():5d} notgen={(~g[hm]).mean():.4f}")
    if kk>=199: break
print("== Z2430: type II prime slices, among gen=1 : fraction with divisor-hit b≡-1 (a=1 slice) ")
for kk in [3,7,11,19,23,31,43]:
    m=(a['k']==kk)&(a['type']==1)
    gm=m&B['gen']; print(f"k={kk} gen=1 n={gm.sum()} dh=1 frac={B['dh'][gm].mean():.4f}; gen=0 & dh=1 count {np.sum(m&~B['gen']&B['dh'])}")
print("== Z2566: squarefree rate of M (all slices k<=400, type I) by dh")
m0=a['type']==0
for lab,mm in [("all",m0),("dh=1",m0&B['dh']),("dh=0",m0&~B['dh'])]:
    print(lab, "sqf frac", round(B['sqf'][mm].mean(),4), "n", mm.sum())
print("   k=3 type I:", round(B['sqf'][m0&(a['k']==3)].mean(),4), " k=3 type I dh=1:", round(B['sqf'][m0&(a['k']==3)&B['dh']].mean(),4),"dh=0:", round(B['sqf'][m0&(a['k']==3)&~B['dh']].mean(),4))
print("   random ref 6/pi^2 =", round(6/math.pi**2,4))
print("== Z2560: P1 law for M=(p+3)/4 (type II,k=3), normalized u=log P1/log M; PD(1)/Dickman mean 0.6243")
m3=(a['k']==3)&(a['type']==1)
M=(a['p'][m3].astype(float)+3)/4; u=np.log(a['P1'][m3].astype(float))/np.log(M)
print("mean u", round(u.mean(),4), "n", len(u), "P(u<=1/2)", round((u<=0.5).mean(),4), "Dickman rho(2)=0.3069", "P(u<=1/3)", round((u<=1/3).mean(),4), "rho(3)=0.0486")
print("   by p>=1e5:", round(u[a['p'][m3]>=1e5].mean(),4), "p<1e5:", round(u[a['p'][m3]<1e5].mean(),4))
print("== Z2614: hit-rate vs QR-richness R(p)=#{l<=50 prime: (l/p)=1} (type I k=3 dh, and nI)")
primesS=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]
R=np.zeros(len(P),int)
for l in primesS:
    qr=set((x*x)%l for x in range(1,l)) if l>2 else {1}
    if l==2: continue
    R+= np.array([ (int(p)%l) in qr for p in P]).astype(int)
for lo,hi in [(0,5),(5,7),(7,9),(9,11),(11,20)]:
    s=(R>=lo)&(R<hi)&(P>=1000)
    print(f"R in [{lo},{hi}): n={s.sum():6d} mean nI={nI[s].mean():.3f} hard-only mean nI={nI[s&hard].mean() if (s&hard).sum() else float('nan'):.3f} (n={(s&hard).sum()}) minI median={np.median(tsv['minI'][s]):.0f}")
print("== Z2639: mean nI over hard residue classes mod 840 (p<=1e6)")
rs=[1,121,169,289,361,529]
means=[nI[p840==r].mean() for r in rs]; sds=[nI[p840==r].std() for r in rs]
for r,mu,sd,c in zip(rs,means,sds,[(p840==r).sum() for r in rs]): print(f"r={r}: n={c} mean nI={mu:.3f} sd={sd:.3f}")
print("CV of class means:", round(np.std(means)/np.mean(means),4))
print("== Z2581: var of nI in dyadic bins of p (log-correlation test)")
for lo,hi in [(1e3,1e4),(1e4,1e5),(1e5,1e6)]:
    s=(P>=lo)&(P<hi)&hard
    print(f"[{lo:.0e},{hi:.0e}) hard n={s.sum()} mean={nI[s].mean():.3f} var={nI[s].var():.3f} loglog={math.log(math.log(hi)):.3f}")
