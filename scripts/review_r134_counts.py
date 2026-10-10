"""R134: cheap recount of two §7 / Prop 4.10 numbers (counts of primes only)."""
from sympy import primerange, isprime
n1 = sum(1 for p in primerange(10**6, 3*10**6) if p % 12 == 5 and isprime(p*p+12))
n2 = sum(1 for p in primerange(5, 15*10**5) if p % 24 == 1)
print('p=5 mod 12 in [1e6,3e6) with p^2+12 prime:', n1, ' primes =1 mod 24 below 1.5e6:', n2)
