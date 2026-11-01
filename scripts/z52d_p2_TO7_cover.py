# Z2805 corrected: ES words (t,u,v), t,u,v>=2, tuv-u-v=p, with ES slot condition 4 | one of t,u,v,tu-1,tv-1 (FOREST/EXSET_I3 scope).
# Fixed (t,u): v=(p+u)/(tu-1) must be an integer >=2. Union density over (t,u) with tu<=T, via direct check on primes.
import numpy as np, sys
def isprime(n): return n>1 and all(n%d for d in range(2,int(n**.5)+1))
primes=np.array([p for p in range(1001,400000) if p%4==1 and isprime(p)])
print("primes sampled:",len(primes))
for T in [6,10,20,30,60,100,200]:
    covered=np.zeros(len(primes),bool); anyword=np.zeros(len(primes),bool)
    for t in range(2,T+1):
        for u in range(2,T//t+1):
            m=t*u-1
            ok=((primes+u)%m==0)
            v=np.where(ok,(primes+u)//m,0)
            slot=(t%4==0)|(u%4==0)|(m%4==0)|(((t*v-1)%4)==0)
            cov=ok&(v>=2)&slot
            covered|=cov
            anyword|=ok&(v>=2)
    print(f"T={T:4d}: uncovered by ES-slot words with tu<=T: {1-covered.mean():.5f}; uncovered by ANY word (no slot condition): {1-anyword.mean():.5f}")
