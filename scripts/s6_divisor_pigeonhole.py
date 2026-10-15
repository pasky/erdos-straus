# At the least forced window q (prime, q=3 mod 4, (q/p)=-1, K=(p+q)/4 odd) of primes p=1 (4) <= N:
# P = {d mod q : d | K}.  Criterion (PROVED): |P| > (q-1)/2  =>  P meets -P  =>  cap 0 at q.
# Report: how often the criterion fires, and how often cap 0 holds at q anyway (exact: -1 in P/P).
import sys
from sympy import primerange, factorint, legendre_symbol as L, divisors
N=int(sys.argv[1]); tot=crit=cap0=0; worst=0
for p in primerange(5,N):
    if p%4!=1: continue
    q=next(q for q in primerange(3,10**4) if q%4==3 and L(q,p)==-1 and ((p+q)//4)%2==1)
    K=(p+q)//4; P={d%q for d in divisors(K)}
    tot+=1; c=len(P)>(q-1)//2; crit+=c
    h=any((q-a)%q in P for a in P) if False else any(((-a)%q) in P for a in P)
    cap0+=h; assert h or not c
print("primes",tot,"criterion |P|>(q-1)/2 fires",crit,"cap0 at least odd-K forced window",cap0)
