"""R237 from-scratch check of the Thm 4.2(a) certifying prime: least prime r = 11 (12) with (p/r) = -1 and
<3> = squares mod r, for all primes p = 1 (4) below PMAX; verifies the resulting solution exactly for a sample."""
import sys
from fractions import Fraction
from sympy import primerange, n_order, factorint
PMAX = int(sys.argv[1])
rs = [r for r in primerange(11, 5000) if r % 12 == 11 and n_order(3, r) == (r - 1) // 2]
mx = (0, 0); cnt = 0; checked = 0
for p in primerange(5, PMAX):
    if p % 4 != 1: continue
    r = next(r for r in rs if pow(p % r, (r - 1) // 2, r) == r - 1)
    cnt += 1
    if r > mx[0]: mx = (r, p)
    if cnt % 997 == 1:  # exact solution from D = 9^a
        tgt = (-p * pow(4, -1, r)) % r
        a = next(a for a in range(r) if pow(9, a, r) == tgt)
        D, A = 9**a, (r + 1) // 4
        E = (p + 4 * D) // r; assert (p + 4 * D) % r == 0
        x, y, z = (p + E) // 4, p * A, Fraction(p * ((p + E) // 4) * A, D)
        assert Fraction(4, p) == Fraction(1, x) + Fraction(1, y) + 1 / z
        f = factorint(z.denominator); assert set(f) <= {3} and all(v % 2 == 0 for v in f.values()) and y % 3 == 0
        checked += 1
print(f"p=1(4) primes < {PMAX}: {cnt}; max least r = {mx[0]} (at p = {mx[1]}); exact solutions checked: {checked}")
