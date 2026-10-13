"""R172: per-omega(M) aggregate of the quadratic part Q (KUDLA_ES §3 item 3) vs tau(N)/phi(M); slices cd<=60, primes 5<=p<1500.
Run: uv run --with sympy python scripts/review_kud_qomega.py"""
from math import gcd
from collections import defaultdict
from sympy import divisors, primerange, totient, factorint
R=defaultdict(lambda:[0,0,0])
sl=[(c,d) for c in range(1,61) for d in range(1,61) if c*d<=60]
for p in primerange(5,1500):
    for c,d in sl:
        N,M=1+4*c*c*d*p,4*c*d
        sq={x*x%M for x in range(M) if gcd(x,M)==1}
        dv=divisors(N)
        q=sum(1 for f in dv if (-f)%M in sq)/len(sq)
        es=sum(1 for f in dv if f%M==M-1)
        w=len(factorint(M)); R[w][0]+=q; R[w][1]+=len(dv)/int(totient(M)); R[w][2]+=es
for w in sorted(R): print(w, 'sumQ/sum(tau/phi)=%.3f'%(R[w][0]/R[w][1]), 'sumES/sum(tau/phi)=%.3f'%(R[w][2]/R[w][1]))
