# z57 COMPLEMENT: sample lists of primes p ≡ 1 (mod 4): next such prime after 10^k + j*step (deterministic, as in CROSSF).
# usage: python z57_complement_samples.py K COUNT STEP > list
import sys
from sympy import isprime
k, count, step = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
for j in range(count):
    n = 10 ** k + j * step + 1
    while not (n % 4 == 1 and isprime(n)): n += 4 if n % 4 == 1 else 1
    print(n)
