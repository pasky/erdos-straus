# Integer comparison for the FF a*-statistic: least u >= 1 such that p + u has a divisor d ≡ -1 (mod 4u)
# (u-form of (★)), for primes p ≡ 1 (mod 4) in [2, X]; prints max least-u per decade and the argmax.
import sys
from sympy import primerange, divisors
X = int(sys.argv[1]); CAP = 3000  # u beyond CAP: reported as zero/undecided
best = {}
for p in primerange(5, X):
    if p % 4 != 1: continue
    u = 1
    while True:
        m = 4 * u
        if any(d % m == m - 1 for d in divisors(p + u)): break
        u += 1
        if u > CAP: break
    dec = len(str(p))
    if u > CAP: print('no u <= CAP at p =', p); continue
    if dec not in best or u > best[dec][0]: best[dec] = (u, p)
# per-decade maxima (disjoint intervals [10^(k-1), 10^k) ∩ [5, X)) and cumulative maxima up to 10^k (and X)
cum = (0, 0)
for dec in sorted(best):
    if best[dec][0] > cum[0]: cum = best[dec]
    hi = min(10 ** dec, X)
    print("decade [10^%d, %d): max least u = %d at p = %d | cumulative p < %d: max %d at p = %d" % (dec - 1, hi, *best[dec], hi, *cum))
