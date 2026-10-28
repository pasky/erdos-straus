import numpy as np
from math import isqrt
MV=np.fromfile('/tmp/i3_1e8_minv.u32',dtype=np.uint32)
def rep(name, ns):
    ns=np.array(ns); mv=MV[ns].astype(np.int64); x0=np.array([isqrt(int(n))+2 for n in ns])
    surv=(mv>x0); zero=(mv==0xFFFFFFFF)
    print(f"{name}: count {len(ns)}, P1(census: no word with v<=sqrt n +2) = {surv.mean():.4e} ({surv.sum()}), zeros {zero.sum()}, P2 = {zero.sum()/max(1,surv.sum()):.3f}")
for lo,hi in [(10**4,10**5),(10**5,10**6),(10**6,10**7),(10**7,10**8)]:
    rep(f"even squares [{lo},{hi}]", [m*m for m in range(isqrt(lo)+1, isqrt(hi)+1) if m%2==0])
for lo,hi in [(10**3,10**4),(10**4,10**5),(10**5,10**6)]:
    n=np.arange(lo,hi); n=n[(n%2==0)]
    sq=np.array([isqrt(int(x))**2==x or (x%2==0 and 2*isqrt(int(x)//2)**2==x) for x in n]); n=n[~sq]
    rep(f"even non-sq [{lo},{hi}]", n)
