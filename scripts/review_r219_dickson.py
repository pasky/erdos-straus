"""R219: illustrate the repaired §2.4 argument. If n ≡ 1 (8) and every |t n + 1| (1 <= |t| <= T) is 2^a * (prime),
then every divisor A of t n + 1 has (-A/n) = +1, so no word with |t| <= T has chi = -1.
Search n ≡ 1 (8), n ≡ 0 mod all odd primes <= 2T+1, for such n and confirm by brute force."""
import sys, math
sys.path.insert(0,'scripts')
from review_r219_slots import jac, fac, brute
T=int(sys.argv[1]); LIM=int(sys.argv[2])
P=1
for p in range(3,2*T+2,2):
    if all(p%q for q in range(3,int(p**.5)+1,2)): P*=p
step=8*P; r=next(x for x in range(1,step) if x%8==1 and x%P==0)
found=0
for n in range(r,LIM,step):
    if math.isqrt(n)**2==n: continue
    ok=True
    for t in range(-T,T+1):
        if t==0: continue
        f=fac(abs(t*n+1)); odd=[q for q in f if q>2]
        if len(odd)!=1 or f[odd[0]]!=1: ok=False;break
    if ok:
        anyok=any(brute(n,t)[0] for t in range(-T,T+1) if t)
        print("n=",n,"all |tn+1| = 2^a*prime for |t|<=",T,"; some chi=-1 word with |t|<=T:",anyok)
        found+=1
        if found>=3: break
