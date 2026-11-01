# z52d pass2 SK1 (Z0895): brute-force check of the isosceles lemma. Solutions of 2/u+1/v=4/p (u>=1, v>=1) are
# exactly the (u,v) with A=4u-2p>0 dividing p*u (then v=p*u/A); the lemma predicts 2 solutions iff p=3 mod 4, else 0.
# u ranges over (p/2, p(p+1)/2+1]: the largest possible A=2p^2 gives u=p(p+1)/2, so this range is exhaustive.
import numpy as np
def isp(n): return n>1 and all(n%d for d in range(2,int(n**.5)+1))
bad=[]; n=0
for p in range(3,3001,2):
    if not isp(p): continue
    n+=1
    u=np.arange(p//2+1, p*(p+1)//2+2, dtype=np.int64)
    A=4*u-2*p
    ok=(A>0)&((p*u)%np.where(A>0,A,1)==0)
    cnt=int(ok.sum())
    pred=2 if p%4==3 else 0
    if cnt!=pred: bad.append((p,cnt))
print("primes checked:",n,"mismatches with lemma (2 iff p=3 mod 4):",bad[:10],len(bad))
