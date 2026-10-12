"""O141(d): the Type II divisibility system Phi_n: e | a+b, 4ab | n+e (a,b,e >= 1).
Checks emptiness at odd squares (ET Prop 1.6 shadow) and non-emptiness otherwise, n <= NMAX, n = 1 (mod 4).
Bounds: e <= a+b and 4ab <= n+e force (4a-1)(4b-1) <= 4n+1.
"""
import sys
from math import gcd, isqrt
NMAX = int(sys.argv[1])
def phi(n, coprime):
    for a in range(1, n + 1):
        if 4 * a - 1 > 4 * n + 1: break
        for b in range(a, n + 1):
            if (4 * a - 1) * (4 * b - 1) > 4 * n + 1: break
            if coprime and gcd(a, b) > 1: continue
            e = (-n) % (4 * a * b)
            if e > 0 and (a + b) % e == 0:
                return (a, b, e)
    return None
bad = []
for n in range(5, NMAX + 1, 4):
    sq = isqrt(n) ** 2 == n
    r1, r2 = phi(n, True), phi(n, False)
    if sq and (r1 or r2): print("square with solution!", n, r1, r2)
    if not sq and r2 is None: bad.append(n)
    if not sq and (r1 is None) != (r2 is None): print("coprime matters at", n)
print("n = 1 mod 4 non-squares <= NMAX with Phi_n empty:", len(bad), bad[:20])
# coprime Type II on Mordell-hard primes up to PMAX (argv[2], optional)
if len(sys.argv) > 2:
    from sympy import primerange
    HARD = {1, 121, 169, 289, 361, 529}
    fails = [p for p in primerange(5, int(sys.argv[2])) if p % 840 in HARD and phi(p, True) is None]
    print("hard primes <= PMAX with no coprime Type II point:", fails)
