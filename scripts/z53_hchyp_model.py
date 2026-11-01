# z53 HCHYP: uniform-residue Kubilius model M for one line (Theorem M of Z53_HCHYP.md).
# k ~ Poisson(lam), lam = log log N; k i.i.d. uniform residues in G=(Z/x)^*, |G| = phi(x); target h = -1 != 1.
# P(success | k) is bracketed by [1/2 min(1,(2^k-1)/n), min(1,(2^k-1)/n)] (Lemma M1); we print the upper value U,
# a Monte-Carlo estimate in the cyclic group Z/n (exact subset-sum reachability), and the exponent predictions.
import math, sys, random
from math import exp, log, lgamma
def phi(n):
    r=n; m=n; q=2
    while q*q<=m:
        if m%q==0:
            while m%q==0: m//=q
            r-=r//q
        q+=1
    if m>1: r-=r//m
    return r
def pois(lam,k): return exp(-lam+k*log(lam)-lgamma(k+1))
def U(lam,n): return sum(pois(lam,k)*min(1.0,(2**k-1)/n) for k in range(0,200))
def mc(lam,n,trials=4000,seed=1):
    rnd=random.Random(seed); hit=0
    for _ in range(trials):
        # sample Poisson
        k=0; t=rnd.expovariate(1.0)
        while t<lam: k+=1; t+=rnd.expovariate(1.0)
        reach=1  # bitmask of reachable sums in Z/n, start {0}
        full=(1<<n)-1
        for _ in range(k):
            g=rnd.randrange(n)
            reach |= ((reach<<g)|(reach>>(n-g))) & full
        if (reach>>(n-1))&1: hit+=1   # target -1 = n-1 (cyclic model of the target)
    return hit/trials
def Q(a): return a*log(a)-a+1
if __name__=="__main__":
    for L in [18.43, 27.63, 35.93]:
        lam=log(L)
        print(f"log p = {L}: lam = {lam:.3f}; (log p)^log2 = {L**log(2):.1f}, (log p)^(2log2) = {L**(2*log(2)):.1f}")
        print("   x   phi   x*U/logp   x*MC/logp")
        for x in [4,8,16,32,64,128,256,512,1024,2048]:
            n=phi(x); u=U(lam,n); m=mc(lam,n) if n<=1024 else float('nan')
            print(f"  {x:5d} {n:5d}  {x*u/L:.3f}   {x*m/L:.3f}")
    print("exponent of expected successes up to (log p)^theta: theta - Q(theta/log2) (theta<=2log2)")
    for th in [0.7,0.8,1.0,1.2,1.3,2*log(2)]:
        print(f"  theta={th:.3f}: {th-Q(th/log(2)):.4f}")
