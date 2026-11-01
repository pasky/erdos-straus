# Z0143: 4/p = 1/x + 1/y + 1/z^2. Check the Jacobi necessary condition derived in out_Q17:
# with a = 4z^2 - p, b = p z^2, 1/x+1/y = a/b needs d1 + d2 ≡ 0 (mod a') for divisors d1,d2 of b' (reduced fraction),
# which is impossible if every prime factor of b' is a Jacobi square mod a' (since a' ≡ 3 mod 4 when gcd small).
from sympy import primerange, divisors, jacobi_symbol, factorint
from math import gcd
def solvable2(a, b):
    g = gcd(a, b); a //= g; b //= g
    D = divisors(b)
    s = set(d % a for d in D)
    return any((-d) % a in s for d in D)
out = []
viol = 0; nsolv = 0
for p in primerange(5, 400):
    if p % 4 != 1: continue
    zs = [z for z in range(1, 400) if 4*z*z > p and solvable2(4*z*z - p, p*z*z)]
    for z in zs:
        nsolv += 1
        a = 4*z*z - p; b = p*z*z; g = gcd(a, b); a //= g; b //= g
        if a % 4 == 3 and all(jacobi_symbol(q % a, a) == 1 for q in factorint(b)):
            viol += 1
    out.append((p, zs[:3], len(zs)))
print("solvable (p,z) pairs:", nsolv, " violating 'some factor of b is a Jacobi non-square mod a' :", viol)
print("primes with no z <= 400:", [p for p, zs, n in out if n == 0])
print("first z for solvable:", [(p, zs[0]) for p, zs, n in out if n][:25])
