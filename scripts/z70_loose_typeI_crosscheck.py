# z70 LOOSE #10: independent cross-check of Lemma S (exact Type I slice decision) for small p, d.
# Method A (Lemma S): a <= (p+1)/(2d), f = -p mod 4ad, f <= p+2, f | 4a^2 d + 1.
# Method B (direct): e over 1..E (E = 4p + 8), 4d | pe + 1, ab = (pe+1)/(4d), some divisor a of ab with e | a + b.
#   (Bound check: a point has e = (4a^2d+1)/f with a <= b, and e <= a + b <= ab + 1 = (pe+1)/(4d) + 1, i.e. e(1 - p/4d)
#    <= ...; we simply take E generous and also report the largest e used by any point found.)
import sys
from sympy import primerange, divisors
def A(p, d):
    for a in range(1, (p + 1) // (2 * d) + 1):
        g = 4 * a * d; N = g * a + 1; f = (-p) % g or g
        while f <= p + 2:
            if N % f == 0: return True
            f += g
    return False
def B(p, d, E):
    for e in range(1, E + 1):
        if (p * e + 1) % (4 * d): continue
        m = (p * e + 1) // (4 * d)
        for a in divisors(m):
            if (a + m // a) % e == 0: return e
    return 0
def recheck(pairs):
    for p, d in pairs:
        e = B(p, d, (p + 1) ** 2 // d + 2)
        print(f'  ({p}, {d}): method B with full e-range finds e = {e} -> {"agree" if e else "STILL MISMATCH"}')

if __name__ == '__main__':
    MM = []
    bad = 0; tot = 0; emax = 0
    for p in primerange(5, 3000):
        if p % 4 != 1: continue
        for d in range(1, 41):
            ra = A(p, d); rb = B(p, d, 4 * p + 8); tot += 1
            emax = max(emax, rb)
            if ra != bool(rb): bad += 1; print('MISMATCH', p, d, ra, rb); MM.append((p, d))
    print(f'(p, d) pairs: {tot}, mismatches: {bad}, largest e of a found point: {emax}')

    # second pass for the pairs where method B (e <= 4p + 8) found nothing but A did: rerun B with the full bound
    # e <= 4a^2 d + 1 <= (p+1)^2/d + 1 (from a <= (p+1)/(2d))
    print('re-check of mismatches with E = (p+1)^2/d + 2:')
    recheck(MM)
