# Z0052: for every odd prime l, exists odd k with 1+l^k having a prime factor q ≡ 3 (mod 4).
# Proof idea: pick prime q ≡ 3 (4) with (l/q) = -1; then ord_q(l) = 2m, m odd, l^m ≡ -1 (mod q).
from sympy import primerange, legendre_symbol, n_order, factorint
bad=[]; mx=0
for l in primerange(3,3000):
    # least k via direct search
    kmin=None
    for k in range(1,60,2):
        if any(q%4==3 for q in factorint(1+l**k)): kmin=k;break
    # construction
    for q in primerange(3,10**6):
        if q%4==3 and q!=l and legendre_symbol(l%q,q)==-1:
            o=n_order(l,q); assert o%2==0 and (o//2)%2==1 and pow(l,o//2,q)==q-1; break
    if kmin is None: bad.append(l)
    mx=max(mx,kmin or 0)
print("fail",bad,"max kmin",mx)
