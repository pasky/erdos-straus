# Z2637 / Z2643 / Z2778 on I3 counts r(n) (n<=1e7, from scripts/z52d_p2_TO7_i3.c; binary kept in /tmp)
import numpy as np, math
r=np.fromfile('/tmp/i3_counts_1e7.bin',dtype=np.uint8).astype(float)
N=len(r)-1
n=np.arange(N+1)
print("== Z2778: mean r(n) by dyadic bin vs (log n)^2 and (log n)^3 (main-term shape)")
bins=[2**k for k in range(4,24)]
for lo,hi in zip(bins[:-1],bins[1:]):
    if hi>N+1: break
    s=r[lo:hi]; L=math.log(lo)
    print(f"[{lo},{hi}): mean r={s.mean():7.3f}  mean/(log n)^2={s.mean()/L**2:.4f}  mean/(log n)^3={s.mean()/L**3:.5f}  frac r=0={np.mean(s==0):.5f}")
print("== Z2637: Poisson check: P(r=0) vs exp(-local mean), local mean = mean of r over window of 2001 neighbours (n>=1000)")
from numpy.lib.stride_tricks import sliding_window_view
W=2001
c=np.convolve(r,np.ones(W)/W,mode='same')
m=(n>=1000)&(n<=N-1000)
lam=c[m]; z=(r[m]==0)
for a,b in [(0.5,1.5),(1.5,2.5),(2.5,3.5),(3.5,4.5),(4.5,6),(6,8),(8,20)]:
    s=(lam>=a)&(lam<b)
    if s.sum()==0: continue
    print(f"local mean in [{a},{b}): n={s.sum()}, empirical P(0)={z[s].mean():.5f}, exp(-mean)={np.exp(-lam[s]).mean():.5f}")
print("expected number of zeros in (1e6,1e7] under Poisson(local mean):", round(float(np.exp(-c[1000000:N-1000]).sum()),4), " observed:", int(np.sum(r[1000000:]==0)))
print("expected zeros in (1e5,1e6] (Poisson):", round(float(np.exp(-c[100000:1000000]).sum()),2), " observed:", int(np.sum(r[100000:1000000]==0)))
print("== Z2643: first-moment expectation threshold q*(n) with mu(n,q)=r(n) q^3 = 1 (independent triple coordinates), by dyadic bin")
for lo,hi in zip(bins[:-1],bins[1:]):
    if hi>N+1: break
    s=r[lo:hi]; s=s[s>0]
    q=(1.0/s)**(1/3)
    print(f"[{lo},{hi}): median q*={np.median(q):.4f}, min q*={q.min():.4f} (r_max={int(s.max())})")
