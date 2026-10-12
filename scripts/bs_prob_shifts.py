"""O142(b): (1) depression of mean f_II/L^3 on square-mimicking classes p = 1 mod Q; (2) divisor counts of the
shifts (p+e)/4, e<=16, at random vs hardest primes in [2^24,2^25). Input /tmp/fII_1e8.bin = 3-field records (p, f_II, g)
from the first version of bs_prob_fII.c (git history); the current 5-field build needs reshape(-1,5). Run: uv run --with sympy --with numpy python scripts/bs_prob_shifts.py"""
import numpy as np
A=np.fromfile('/tmp/fII_1e8.bin',dtype=np.uint32).reshape(-1,3).astype(np.int64)
p,f,g=A.T; m=p>=2**22; p,f=p[m],f[m]; L=np.log(p.astype(float)); r=f/L**3
print("all", len(p), r.mean().round(4))
for Q in [24,120,840,9240,120120,2042040]:
    mm=p%Q==1; print("p=1 mod",Q, mm.sum(), "mean f/L^3", r[mm].mean().round(4), "ratio to all", (r[mm].mean()/r.mean()).round(3), "min", r[mm].min().round(4))
# squares mod 840 vs nonsquares among p=1 mod 24
sq=set((x*x)%840 for x in range(840))
isq=np.array([x in sq for x in range(840)])[p%840]
mm=p%24==1
print("p=1(24) square mod 840:", r[mm&isq].mean().round(4), " non-square:", r[mm&~isq].mean().round(4))
from sympy import divisor_count
m=(p>=2**24)&(p<2**25); p,f=p[m],f[m]
rng=np.random.default_rng(0); idx=rng.choice(len(p),3000,replace=False)
idx=np.concatenate([idx,np.argsort(f/np.log(p)**3)[:200]])
D=np.array([int(sum(divisor_count((int(q)+e)//4) for e in range(1,17) if (int(q)+e)%4==0)) for q in p[idx]],dtype=float)
r=f[idx]/np.log(p[idx].astype(float))**3
print("random 3000: mean sum_{e<=16} tau((p+e)/4) =",D[:3000].mean(), " 200 hardest:",D[3000:].mean())
print("corr(log r, log D) on random sample:", np.corrcoef(np.log(r[:3000]),np.log(D[:3000]))[0,1])
