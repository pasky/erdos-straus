"""R124: recount the §8 ratio claim (first 2000 Mordell-hard primes, d=1, a<=50): #{(e,f,a): ef=p+4a^2} vs those with 4a|f+1."""
from sympy import primerange, divisors
H = {1, 121, 169, 289, 361, 529}
ps = [p for p in primerange(2, 10**7) if p % 840 in H][:2000]
tot = good = 0
for p in ps:
    for a in range(1, 51):
        for f in divisors(p + 4*a*a):
            tot += 1; good += (f + 1) % (4*a) == 0
print(len(ps), tot, good, good/tot)
