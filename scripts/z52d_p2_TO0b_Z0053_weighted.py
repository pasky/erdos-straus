"""z52d pass2 TO0b Z0053: depth-1 weighted relaxation 4/p = 1/x + 1/y + l/z (l = 5, 7, 11, z not divisible by l, x,y,z positive
integers, no ordering needed), exact, independent of scripts/z52b_analogues_weighted.py.  For each prime p (5..N) search
z <= 3p with l not | z and test whether r = 4/p - l/z is a sum of two unit fractions (divisor test on the reduced denominator)."""
from fractions import Fraction as Fr
import sys
def two_unit(r):
    """r > 0 Fraction: return (x,y) with r = 1/x+1/y, or None (divisors of b^2, b = denominator of r)."""
    if r <= 0: return None
    a, b = r.numerator, r.denominator
    # 1/x+1/y = a/b  <=>  (a x - b)(a y - b) = b^2 ; enumerate divisors d of b^2 with d = a x - b
    n = b * b
    # divisors of n by trial over factorization
    fac = {}
    m = b; q = 2
    while q * q <= m:
        while m % q == 0: fac[q] = fac.get(q, 0) + 1; m //= q
        q += 1
    if m > 1: fac[m] = fac.get(m, 0) + 1
    divs = [1]
    for q, e in fac.items():
        divs = [d * q ** k for d in divs for k in range(2 * e + 1)]
    for d in divs:
        if (d + b) % a == 0:
            x = (d + b) // a
            e2 = n // d
            if (e2 + b) % a == 0:
                y = (e2 + b) // a
                if x > 0 and y > 0 and Fr(1, x) + Fr(1, y) == r:
                    return (x, y)
    return None
def isprime(n):
    return n > 1 and all(n % q for q in range(2, int(n ** .5) + 1))
N = int(sys.argv[1]) if len(sys.argv) > 1 else 400
for l in (5, 7, 11):
    fails = []; tested = 0; example = None
    for p in range(5, N):
        if not isprime(p): continue
        tested += 1
        ok = False
        for z in range(1, 3 * p + 1):
            if z % l == 0: continue
            r = Fr(4, p) - Fr(l, z)
            if r <= 0: continue
            t = two_unit(r)
            if t is not None:
                ok = True
                if example is None or p == 5: example = (p, z, t)
                break
        if not ok: fails.append(p)
    print(f'l={l}: primes 5..{N-1}: {tested} tested, failures {fails[:15]} (count {len(fails)}); example for p=5: {example if example else None}', flush=True)
