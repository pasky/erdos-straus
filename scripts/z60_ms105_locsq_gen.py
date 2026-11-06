# z60 MS105: random "locally square" non-squares n = x^2 + k*P_y with P_y = 8*prod(odd primes <= y), so n is a nonzero
# square residue mod every prime <= y and n = 1 (8) (Jacobi depth > y; n mod 840 in M; gcd(n,105) = 1), plus controls:
# random non-squares in M of the same size.  Output "n LS:y" / "n CT:y".
import random, math, sys
from sympy import primerange
random.seed(60106)
K = int(sys.argv[1]) if len(sys.argv) > 1 else 100
for y in [47, 59, 71, 79, 83]:
    P = 8
    for q in primerange(3, y + 1): P *= q
    for _ in range(K):
        while True:
            x = random.randrange(1, P)
            if math.gcd(x, P) == 1: break
        n = (x * x) % P + random.randrange(1, 400) * P
        assert math.isqrt(n) ** 2 != n and n < 2**126 and n % 8 == 1
        print(n, f'LS:{y}')
        while True:
            c = random.randrange(n // 2, n) * 840 // 840
            c = c - c % 840 + random.choice([1, 121, 169, 289, 361, 529])
            if math.isqrt(c) ** 2 != c: break
        print(c, f'CT:{y}')
