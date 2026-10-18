"""R280: unconditional repair of O269 Prop S(3).  For a prime l = 3 (mod 4) with (l/105) = -1 one has (-105/l) = +1,
so 105 m^2 + 1 = 0 (mod l) is solvable; for such odd m (gcd(m, l) = 1), b = l | n + 1, n = 105 m^2, and
(l/n) = (l/105) = -1, so n/l = (n+1)/l - 1/l is an HJ length-2 certificate: lambda(n) <= 2, n not in Z.
Checks the symbol identities for small l and the certificate for odd m < 20000 in the residue classes."""
from sympy import jacobi_symbol, primerange
good = [l for l in primerange(3, 200) if l % 4 == 3 and jacobi_symbol(l, 105) == -1]
print("primes l=3 (4), (l/105)=-1, <200:", good)
assert all(jacobi_symbol((-105) % l, l) == 1 for l in good)
for l in good[:6]:
    roots = [r for r in range(l) if (105 * r * r + 1) % l == 0]
    bad = 0
    for m in range(1, 20000, 2):
        if m % l in roots:
            n = 105 * m * m
            if (n + 1) % l or jacobi_symbol(l, n) != -1 or not (2 <= l <= (n + 1) // 2):
                bad += 1
    print(f"l={l}: roots of 105 r^2 = -1 mod l: {roots}; certificate failures for odd m<20000: {bad}")
