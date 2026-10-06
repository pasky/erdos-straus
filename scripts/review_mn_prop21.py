# From-scratch check of POINTWISE_MN Prop 2.1: prime atoms l = -1 (m) with event classes in both square cosets.
from sympy import primerange, divisors, legendre_symbol
for m in [5,6,7,9,10,11,13,14,15,18,21,22,30,33,35,42]:
    hits=[]; byconstr=0; tot=0
    for l in primerange(3,20000):
        if l%m!=m-1: continue
        A=(l+1)//m; s={legendre_symbol((-m*D)%l,l) for D in divisors(A*A)}
        tot+=1
        if s=={1,-1}: hits.append(l)
    print(m,"primes",tot,"both-coset",len(hits),"first",hits[:4])
# specific: m=5,l=29
print(sorted({(-5*D)%29 for D in divisors(36)}), [legendre_symbol((-5*D)%29,29) for D in divisors(36)])
