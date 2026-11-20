"""Generic small-(p,q) Q hits: exhaustive at F=r (primes 17..3000) and F=17^3,13^3,17^5; checks (3.1),(3.2), identities and contact sizes."""
import sys
from math import gcd
sys.path.insert(0,'data/z78/xreview')
import r17e_hits as R
pairs=[(p,q) for p in range(1,11) for q in range(1,11) if gcd(p,q)==1 and (p,q)!=(1,1)]
Fs=[(r,r) for r in range(17,3000) if R.isprime(r)]+[(17**3,17),(13**3,13),(17**5,17)]
n=0
for F,r in Fs:
    for p,q in pairs:
        if p%r==0 or q%r==0: continue
        for t in R.Q_hits(F,r,p,q):
            if R.check_Q(F,r,p,q,*t) is not None:
                n+=1
                if F in (17**3,17**5,13**3) or (p,q) in ((1,5),(5,1)): print('Q hit',F,p,q,t)
print('Q generic hits',n,R.stats)
for k,v in sorted(R.worst.items()): print(k,v)
