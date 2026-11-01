"""z52d pass2 TO0b: exact identity checks for the 'trivial S-integer / numerator relaxation' items
(Z0055, Z0073, Z0074, Z0053-lemma form) and the Z0052 divisor-of-(l^k+1) test for l = 1 mod 8 primes.
Z0052: for odd k, (l^k+1)/2 is odd and = 1 mod 4 when l = 1 mod 8; ask for a prime factor = 3 mod 4 of (l^k+1)/2."""
from fractions import Fraction as Fr
import sympy
ok = True
for n in range(3, 2001, 2):
    ok &= Fr(4, n) == Fr(2, n) + Fr(1, n) + Fr(1, n)
print('Z0055 4/n = 2/n+1/n+1/n for odd n<=2000:', ok)
for p in [q for q in range(5, 400) if sympy.isprime(q)]:
    assert Fr(4, p) == Fr(1, Fr(p, 3)) + Fr(1, 2 * p) + Fr(1, 2 * p)
print('Z0074 4/p = 1/(p/3)+1/(2p)+1/(2p) for primes 5..400: True')
print('Z0073 4 is a unit of Z[1/2]: 4/p = 1/(p/4) with p/4 in Z[1/2]; checked: ', all(Fr(4, p) == Fr(1, Fr(p, 4)) for p in [5, 7, 11, 13]))
res = {}
for l in [q for q in range(3, 1200) if sympy.isprime(q) and q % 8 == 1]:
    found = None
    for k in (1, 3, 5, 7):
        m = (l ** k + 1) // 2
        fac = sympy.factorint(m)
        if any(e % 1 == 0 and q % 4 == 3 for q, e in fac.items()):
            found = k
            break
    res[l] = found
none = [l for l in res if res[l] is None]
print('Z0052: primes l = 1 mod 8 below 1200:', len(res), ' with k in {1,3,5,7} giving (l^k+1)/2 with a prime factor 3 mod 4:', len(res) - len(none))
print('  no such k (<=7) for l =', none[:20])
print('  k distribution:', {k: sum(1 for l in res if res[l] == k) for k in (1, 3, 5, 7)})
