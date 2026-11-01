"""Generates data/z52d/fourier/random400.txt: 400 random primes p ≡ 1 (mod 24) in [1e6, 1e7], seed 52041."""
import random
from z52d_fourier_lib import isprime
random.seed(52041)
out = set()
while len(out) < 400:
    q = random.randrange(10**6, 10**7) // 24 * 24 + 1
    if isprime(q): out.add(q)
open('../data/z52d/fourier/random400.txt', 'w').write('\n'.join(map(str, sorted(out))) + '\n')
