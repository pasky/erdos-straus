"""R233: illustrate Thm 3.2's construction p = 1 + M x (with the 2-power of M chosen > K+1) and verify K(p) >= K
directly by factoring p + s and s p + 1 (1 <= s <= K)."""
import sys
from sympy import isprime, primerange, factorint
from review_r233_common import jacobi

K = int(sys.argv[1]) if len(sys.argv) > 1 else 3
NEED = int(sys.argv[2]) if len(sys.argv) > 2 else 3
M = 1
for l in primerange(2, 2 * K + 2):
    a = 1
    while l ** a <= K + 1 or (l == 2 and a < 3):
        a += 1
    M *= l ** a
print("K", K, "M", M)


def isclean(x, p):
    return all(jacobi(r, p) != -1 for r in factorint(x))


def depth(p, smax=40):
    s = 1
    while s <= smax and isclean(p + s, p) and isclean(s * p + 1, p):
        s += 1
    return s - 1


found = 0
x = 0
while found < NEED:
    x += 1
    p = 1 + M * x
    forms = [p] + [(p + s) // (s + 1) for s in range(1, K + 1)] + [(s * p + 1) // (s + 1) for s in range(2, K + 1)]
    assert all((p + s) % (s + 1) == 0 and (s * p + 1) % (s + 1) == 0 for s in range(1, K + 1))
    if all(isprime(f) for f in forms):
        found += 1
        print("x", x, "p", p, "p%8", p % 8, "K(p)", depth(p))
