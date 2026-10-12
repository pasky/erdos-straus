"""O142(b): candidate common drivers of f_I and f_II (2500 random primes p=1 mod 24 in [2^23,3e7]).
Inputs /tmp/fII5_3e7.bin, /tmp/r123_3e7_fI.bin (see bs_prob_typecorr.py). Run: uv run --with sympy --with numpy python scripts/bs_prob_drivers.py"""
import numpy as np
from sympy import divisor_count as t
A=np.fromfile('/tmp/fII5_3e7.bin',dtype=np.uint32).reshape(-1,5).astype(np.int64)
fI=np.fromfile('/tmp/r123_3e7_fI.bin',dtype=np.uint32)
p,f2=A[:,0],A[:,1]; m=(p>=2**23)&(p%24==1); p,f2=p[m],f2[m]; f1=fI[p]
rng=np.random.default_rng(0); idx=rng.choice(len(p),2500,replace=False); p,f1,f2=p[idx],f1[idx].astype(float),f2[idx].astype(float)
L=np.log(p.astype(float))
y1,y2=np.log(f1/L**3),np.log(f2/L**3)
P=[int(q) for q in p]
cands={
 "tau(p-1)":[t(q-1) for q in P], "tau(p+1)":[t(q+1) for q in P],
 "tau((p+3)/4)":[t((q+3)//4) for q in P], "tau((3p+1)/4)":[t((3*q+1)//4) for q in P],
 "sum_e<=16 tau((p+e)/4)":[sum(t((q+e)//4) for e in (3,7,11,15)) for q in P],
 "sum_e<=16 tau((pe+1)/4)":[sum(t((q*e+1)//4) for e in (3,7,11,15)) for q in P],
 "tau((p-1)/24)":[t((q-1)//24) for q in P],
}
for k,v in cands.items():
    v=np.log(np.array(v,float)); print(f"{k:28s} corr w/ log fI {np.corrcoef(y1,v)[0,1]:.3f}  log fII {np.corrcoef(y2,v)[0,1]:.3f}")
print("corr(log fI, log fII) in sample:", np.corrcoef(y1,y2)[0,1].round(3))
