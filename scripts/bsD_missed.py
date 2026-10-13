"""O177 (bsD_): structure of the primes p = 1 (24) NOT covered by the quadratic slices 4cd | 24 (O176), and whether
a 'cubic/sextic layer' (slices 4cd | 504, i.e. (Z/4cd)^x of exponent | 6 -- the ray condition is a Boolean function
of characters of order | 6) catches them.  Divisor forms (STATUS):
  Type I : exists f | p^2 + 4c^2 d, f = -p (mod 4cd);   Type II: exists f | 1 + 4c^2 d p, f = -1 (mod 4cd).
Also prints, for each missed prime: least quadratic non-residue n_p, cubic-residue data (2, 3 cubic residues mod p),
and the least M = 4cd of any covering slice.
Run: PYTHONPATH=scripts uv run python scripts/bsD_missed.py X
"""
import sys
from sympy import primerange, divisors, isprime

X = int(sys.argv[1]) if len(sys.argv) > 1 else 10**5


def slices(L):  # (c,d) with cd | L
    return [(c, d) for c in divisors(L) for d in divisors(L) if L % (c * d) == 0]


SQ = sorted(slices(6), key=lambda t: t[0] * t[1])
SX = sorted(slices(126), key=lambda t: t[0] * t[1])


def hit(p, c, d):
    M = 4 * c * d
    if any((f + p) % M == 0 for f in divisors(p * p + 4 * c * c * d)):
        return 'I'
    if any((f + 1) % M == 0 for f in divisors(1 + 4 * c * c * d * p)):
        return 'II'
    return None


def cov(p, S):
    return any(hit(p, c, d) for c, d in S)


def least_cover(p, cap=400):
    best = None
    for cd in range(1, cap):
        for c in divisors(cd):
            d = cd // c
            h = hit(p, c, d)
            if h:
                return 4 * cd, c, d, h
    return best


def lqnr(p):
    for q in range(2, p):
        if isprime(q) and pow(q, (p - 1) // 2, p) == p - 1:
            return q


def cubic(a, p):
    return pow(a, (p - 1) // 3, p) == 1


miss, n = [], 0
for p in primerange(5, X):
    if p % 24 != 1:
        continue
    n += 1
    if not cov(p, SQ):
        miss.append(p)
print('X', X, 'primes p=1(24):', n, 'missed by quadratic slices (cd|6):', len(miss))
miss6 = [p for p in miss if not cov(p, SX)]
print('of these, missed also by sextic layer (cd|126):', len(miss6), miss6[:20])
# controls: n_p distribution for missed vs all
import statistics
allp = [p for p in primerange(5, X) if p % 24 == 1]
import random
random.seed(1)
ctrl = random.sample(allp, min(len(allp), 600))
print('mean least QNR: missed', statistics.mean(lqnr(p) for p in miss), ' random control', statistics.mean(lqnr(p) for p in ctrl))
print('frac 2 cubic residue: missed', sum(cubic(2, p) for p in miss) / len(miss), ' control', sum(cubic(2, p) for p in ctrl) / len(ctrl))
print('frac 3 cubic residue: missed', sum(cubic(3, p) for p in miss) / len(miss), ' control', sum(cubic(3, p) for p in ctrl) / len(ctrl))
print('frac p = cube mod 7: missed', sum(pow(p, 2, 7) == 1 for p in miss) / len(miss), ' control', sum(pow(p, 2, 7) == 1 for p in ctrl) / len(ctrl))
print('frac p = cube mod 9: missed', sum(p % 9 in (1, 8) for p in miss) / len(miss), ' control', sum(p % 9 in (1, 8) for p in ctrl) / len(ctrl))
print('frac p = QR mod 5,7: missed', sum(p % 5 in (1, 4) and pow(p, 3, 7) == 1 for p in miss) / len(miss),
      ' control', sum(p % 5 in (1, 4) and pow(p, 3, 7) == 1 for p in ctrl) / len(ctrl))
for p in miss[:40]:
    print(p, 'n_p', lqnr(p), '2cub', int(cubic(2, p)), '3cub', int(cubic(3, p)), 'p mod 7,9', p % 7, p % 9,
          'least cover (M,c,d,type)', least_cover(p))
# layers by exponent of (Z/M)^x, M = 4cd:  exponent | 4  <=>  M | 240 (cd | 60);  exponent | 12 <=> M | 65520 (cd | 16380)
S4 = sorted(slices(60), key=lambda t: t[0] * t[1])
S12 = sorted(slices(16380), key=lambda t: t[0] * t[1])
m4 = [p for p in miss if not cov(p, S4)]
print('missed by quadratic AND quartic layer (cd|60):', len(m4), m4[:20])
print('missed by quadratic AND exponent-12 layer (cd|16380):', [p for p in miss if not cov(p, S12)])
print('missed by quartic layer cd|60 but caught by sextic cd|126:', [p for p in m4 if cov(p, SX)])
