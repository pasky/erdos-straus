"""O257: 'complete levels'.  For numerator k and a level L (k | L), the witnesses with modulus H = k*a*b | L cover the
unit classes r mod L with r ≡ -e (mod H) [Type II] or r*e ≡ -1 (mod H) [Type I], e | a+b.  By full T1 (4 | k) no
square class is covered.  L is COMPLETE if every non-square unit class mod L is covered (visibility is sufficient
at level L).  Prints, for L = k*m (m <= MMAX), the number of uncovered non-square unit classes (deficiency)."""
import sys
from math import gcd
from sympy import divisors

k = int(sys.argv[1]); MMAX = int(sys.argv[2]); only = sys.argv[3] if len(sys.argv) > 3 else ''

def analyse(L):
    units = [r for r in range(1, L, 2) if gcd(r, L) == 1]
    sq = {r * r % L for r in units}
    cov = set()
    m = L // k
    for a in divisors(m):
        for b in divisors(m // a):
            if a > b:
                continue
            H = k * a * b
            for e in divisors(a + b):
                if gcd(e, H) != 1 and True:
                    pass
                r2 = (-e) % H          # Type II class mod H
                cov.update(r for r in range(r2, L, H) if gcd(r, L) == 1)
                if gcd(e, H) == 1:
                    r1 = (-pow(e, -1, H)) % H   # Type I class mod H
                    cov.update(r for r in range(r1, L, H) if gcd(r, L) == 1)
    bad_sq = sq & cov
    deficit = [r for r in units if r not in sq and r not in cov]
    return len(units), len(sq), len(bad_sq), deficit

if only:
    for L in map(int, only.split(',')):
        nu, ns, bs, D = analyse(L)
        print(f"L={L} units={nu} squares={ns} squares_covered={bs} deficiency={len(D)} sample={D[:12]}")
    sys.exit()
comp = []
for m in range(1, MMAX + 1):
    L = k * m
    nu, ns, bs, D = analyse(L)
    assert bs == 0, (L, bs)   # full T1 sanity: no square class covered
    if not D:
        comp.append(L)
print(f"k={k}: complete levels L=k*m, m<={MMAX}: {comp}")
