# For odd primes l: smallest k<=K such that 1+l^k has a prime factor = 3 mod 4 (unit-sum mechanism over Z[1/l]).
from sympy import primerange, factorint
K=24
bad=[];mx=(0,0)
for l in primerange(3,3000):
    for k in range(1,K+1):
        n=1+l**k
        # trial: does n have a prime factor 3 mod 4 ? use odd part mod 4 shortcut first
        m=n
        while m%2==0: m//=2
        if m%4==3: break
        f=factorint(m, limit=10**6)
        if any(p%4==3 for p in f): break
    else:
        bad.append(l); continue
    if k>mx[0]: mx=(k,l)
print("no k<=%d for:"%K, bad[:30], "max k", mx)
