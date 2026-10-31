"""Z0530: the (★) covering system {n ≡ −(u+B) (mod 4uB) : gcd(u,B)=1} on integers n ≡ 1 (mod 4), n ≤ X.
For each n compute the least modulus q = 4uB covering it; report #uncovered non-squares (split prime/composite)
with all moduli ≤ M, as M grows. Odd squares are never covered (T1)."""
import numpy as np, math, sys
from math import gcd
X=int(sys.argv[1]); MMAX=int(sys.argv[2])
INF=np.iinfo(np.int64).max
best=np.full(X+1, INF, dtype=np.int64)
for u in range(1, MMAX//4+1):
    for B in range(1, MMAX//(4*u)+1):
        if gcd(u,B)!=1: continue
        q=4*u*B; r=(-(u+B))%q
        if r==0: r=q
        sl=best[r::q]; np.minimum(sl, q, out=sl)
# primality sieve
isp=np.ones(X+1,bool); isp[:2]=False
for i in range(2,int(X**.5)+1):
    if isp[i]: isp[i*i::i]=False
n=np.arange(X+1); sq=np.zeros(X+1,bool); m=np.arange(1,int(X**.5)+2,2); sq[m[m*m<=X]**2]=True
sel=(n%4==1)&(n>=5)&~sq
print("X=%d  #n≡1(4) non-square=%d  primes=%d"%(X,sel.sum(),(sel&isp).sum()))
print("M  uncovered_nonsq  uncovered_primes  uncovered_composites  frac_nonsq")
M=8
while M<=MMAX:
    unc=sel&(best>M)
    print(M, unc.sum(), (unc&isp).sum(), (unc&~isp).sum(), "%.3e"%(unc.sum()/sel.sum()))
    M*=2
unc=sel&(best>MMAX)
print("uncovered at M=%d (first 40):"%MMAX, list(np.nonzero(unc)[0][:40]))
# least-modulus statistics for primes
bp=best[sel&isp]; print("primes: max least modulus", bp.max(), "at", int(np.nonzero(sel&isp&(best==bp.max()))[0][0]) if bp.max()<INF else None)
