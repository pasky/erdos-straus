# review_ec2_facts.py — R189 reviewer 2: from-scratch checks of side claims in EXPONENT_COVERING.md.
import sys
from math import isqrt, gcd
from sympy import isprime, n_order, legendre_symbol, primerange, factorint

out = []
# (1) 27*2^m+1 mod 840 for m = 2 (12)
out.append(('27*2^m+1 mod 840, m=2,14,26,38', [(27 * 2**m + 1) % 840 for m in (2, 14, 26, 38)]))
out.append(('109, 27*2^26+1, 27*2^50+1 prime', [isprime(27 * 2**m + 1) for m in (2, 26, 50)]))
# (2) Section 2 example table, k=27, Q={5,7,13}
tab = []
for m in range(12):
    n = 27 * 2**m + 1
    tab.append((m, tuple(0 if n % q == 0 else legendre_symbol(n % q, q) for q in (3, 5, 7, 13)), n % 7))
out.append(('k=27 (chi3,chi5,chi7,chi13), n mod 7 by m mod 12 (m>=3 rep m+12)', [(m, ch, r) for (m, ch, r) in tab]))
# (3) congruences claimed for 315 and 15015
out.append(('315*2^m+1 = 1 mod 2520 for m=3..40', all((315 * 2**m + 1) % 2520 == 1 for m in range(3, 41))))
out.append(('15015*2^m+1 = 1 mod 120120 for m=3..40', all((15015 * 2**m + 1) % 120120 == 1 for m in range(3, 41))))
# (4) Section 4.3 (k=9)
out.append(('9*2^5+1', 9 * 2**5 + 1, 'ord_17(2)', n_order(2, 17), 'ord_38737(2)', n_order(2, 38737),
            '464844=4*3*38737', 4 * 3 * 38737, '-287 mod 38737 vs I1 residue', (-287) % 38737))
first = [q for q in primerange(3, 2000) if q != 7 and q != 41 and (n_order(2, q) % 8 == 0 and n_order(2, q) % 16 != 0)
         and legendre_symbol((-287) % q, q) == -1][:5]
out.append(('first primes with v2(ord_q 2)=3 and (-287/q)=-1', first))
# (5) Cor 1.5 integer obstruction points, brute force: k odd <= 20001, l in [-70,70]
def unit_square_point(k, l):
    if l >= 0:
        N = k * 2**l + 1           # need N = s^2 with s a power of 2 (unit at every odd q)
        s = isqrt(N)
        return s * s == N and s & (s - 1) == 0
    a = -l                         # q-components (k+2^a)/2^a, need 2^a (k+2^a) a square with odd part 1
    N = (k + 2**a) * 2**a
    s = isqrt(N)
    if s * s != N:
        return False
    odd = k + 2**a
    return odd & (odd - 1) == 0    # odd part must be a power of 2 (=1)
pts = [(k, l) for k in range(1, 20002, 2) for l in range(-70, 71) if unit_square_point(k, l)]
out.append(('Cor1.5 brute: unit-square integer points', pts,
            'all l=0 & k=4^j-1:', all(l == 0 and (k + 1) & k == 0 and ((k + 1).bit_length() - 1) % 2 == 0 for k, l in pts)))
for o in out:
    print(*o)
