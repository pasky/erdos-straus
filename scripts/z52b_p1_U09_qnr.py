# z52b pass1 U09 (Z0670, Z0891): R(p)/log^2 p vs quadratic-character statistics of p; and m^2+1 primes.
# Usage: python3 scripts/z52b_p1_U09_qnr.py data/z52b/pass1/U09/R_primes1mod4_le2e5.txt
import sys, math, numpy as np
from scipy.stats import spearmanr
def isprime(n): return n>1 and all(n%d for d in range(2,int(n**0.5)+1))
def leg(a,l):  # Legendre symbol (a/l) for odd prime l, Euler criterion
    a%=l
    if a==0: return 0
    return 1 if pow(a,(l-1)//2,l)==1 else -1
rows=[list(map(int,l.split())) for l in open(sys.argv[1])]
P=[r[0] for r in rows]; R=np.array([r[1] for r in rows],float)
y=R/np.log(np.array(P,float))**2
ells=[l for l in range(3,101) if isprime(l)]
def least_qnr(p):
    for l in range(3,10**4):
        if isprime(l) and leg(p,l)==-1: return l
    return 0
nqr=np.array([sum(1 for l in ells if l!=p and leg(p,l)==1) for p in P])
nl=np.array([least_qnr(p) for p in P])
print("Z0670: Spearman(R/log^2, least QNR n(p)) =", round(float(spearmanr(nl,y).correlation),4))
print("Z0670: Spearman(R/log^2, #{l<=100: (p/l)=+1}) =", round(float(spearmanr(nqr,y).correlation),4))
for k in sorted(set(nqr.tolist()))[:3]+sorted(set(nqr.tolist()))[-3:]:
    s=nqr==k
    if s.sum()>5: print(f"   #QR-primes={k}: n={int(s.sum())} mean R/log^2={y[s].mean():.3f}")
for n_ in [3,5,7,11,13]:
    s=nl==n_; print(f"   least QNR={n_}: n={int(s.sum())} mean R/log^2={y[s].mean():.3f}")
sq=set(p for p in P if math.isqrt(p-1)**2==p-1)
idx=[i for i,p in enumerate(P) if p in sq]
print("Z0891: m^2+1 primes <=2e5:", len(idx), " R=0 among them:", int(sum(1 for i in idx if R[i]==0)), " mean R/log^2:", round(float(y[idx].mean()),3), " overall:", round(float(y.mean()),3))
