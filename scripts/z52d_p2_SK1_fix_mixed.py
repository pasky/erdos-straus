# z52d pass2 SK1 fix (Z1035): mixed divisor counts for C=1, D=2 at primes p=1 mod 4 <= 1e5:
#   R1(p) = #{d | 4p+1 : d = -1 mod 4}  (the C=1 (star) divisor term),  R2(p) = #{e | 8p+1 : e = -1 mod 8}  (D=2 term)
#   collisions K(p) = #{(d,e): d = e, d | 4p+1, e | 8p+1} (common divisors) and the convolution S(p) = sum over pairs with d*e... (not used)
# Output: mean of R1, R2, their product mean, correlation over p, and the collision count.
import math, numpy as np
from sympy import divisors, primerange
ps=[p for p in primerange(5,100001) if p%4==1]
R1=[];R2=[];coll=0
for p in ps:
    D1=divisors(4*p+1); D2=divisors(8*p+1)
    r1=sum(1 for d in D1 if d%4==3); r2=sum(1 for e in D2 if e%8==7)
    coll+=len(set(D1)&set(D2))-1 if len(set(D1)&set(D2))>0 else 0
    R1.append(r1); R2.append(r2)
R1=np.array(R1); R2=np.array(R2)
print(f"primes 1 mod 4 <=1e5: {len(ps)}; mean R1 {R1.mean():.3f}, mean R2 {R2.mean():.3f}; mean R1*R2 {np.mean(R1*R2):.3f} vs product of means {R1.mean()*R2.mean():.3f}")
print(f"corr(R1,R2) = {np.corrcoef(R1,R2)[0,1]:+.4f}; common divisors of 4p+1 and 8p+1 (excluding 1): {coll}")
print(f"fraction of p with R1>0: {np.mean(R1>0):.4f}; with R2>0: {np.mean(R2>0):.4f}")
# residue control: correlation within classes mod 24 and within size deciles
import collections
cls=collections.defaultdict(list)
for p,a,b in zip(ps,R1,R2): cls[p%24].append((a,b))
for c in sorted(cls):
    arr=np.array(cls[c])
    if len(arr)>50 and arr[:,0].std()>0 and arr[:,1].std()>0:
        print(f"p mod 24 = {c}: n={len(arr)} corr(R1,R2)={np.corrcoef(arr[:,0],arr[:,1])[0,1]:+.3f}")
P=np.array(ps); q=np.quantile(P,[0,.5,1])
for lo,hi in [(q[0],q[1]),(q[1],q[2])]:
    m=(P>=lo)&(P<=hi)
    print(f"size half [{int(lo)},{int(hi)}]: corr(R1,R2) = {np.corrcoef(R1[m],R2[m])[0,1]:+.3f}")
