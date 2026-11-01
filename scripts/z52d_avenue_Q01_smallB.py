# Z1925: fraction of primes p≡1 (4), p ≤ X, NOT covered by the small-B slices B ≤ K of (★):
# p + B has a divisor f ≡ -1 (mod 4B) (f = 4BC-1, cofactor u ≥ 1)

from sympy import primerange, divisors
X=2*10**5
ps=[p for p in primerange(5,X) if p%4==1]
Ks=[1,2,5,10,20,50,100]
first={}
for p in ps:
    for B in range(1,101):
        m=4*B
        if any(f%m==m-1 for f in divisors(p+B)):
            first[p]=B;break
    else: first[p]=10**9
for K in Ks:
    unc=[p for p in ps if first[p]>K]
    print(K, len(unc)/len(ps), unc[:6])
