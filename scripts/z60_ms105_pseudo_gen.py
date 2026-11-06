# z60 MS105: inputs for the pseudosquare test.  Each distinct Lehmer pseudosquare L (OEIS A002189 b-file, Bernstein /
# Sorenson tables; L = 1 (8), QR mod the first k odd primes, non-square) plus K controls: random non-squares
# n = L + 840*t (same class mod 840, |t| <= 10^6, so same size), and K "depth-matched controls" are not attempted.
# Output lines "n tag" with tag = PS:<index>:<depth> or CT:<index>.  depth = least odd prime l with (n/l) = -1.
import random, math, sys
from sympy import jacobi_symbol, nextprime
K = int(sys.argv[1]) if len(sys.argv) > 1 else 20
random.seed(60105)
L = [int(x) for x in open('data/z60/ms105/pseudo/A002189.txt')]
def depth(n):
    l = 3
    while True:
        if n % l and jacobi_symbol(n % l, l) == -1: return l
        l = nextprime(l)
for i, x in enumerate(L):
    print(x, f'PS:{i}:{depth(x)}')
    for j in range(K):
        while True:
            t = random.randint(-10**6, 10**6)
            n = x + 840 * t
            if n > 0 and math.isqrt(n) ** 2 != n: break
        print(n, f'CT:{i}:{depth(n)}')
