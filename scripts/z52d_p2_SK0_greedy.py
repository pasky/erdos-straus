"""Z0129 (pass 2, SK0): does the greedy first term of 4/p work?  For each prime p<=PMAX:
 g1 = floor(p/4)+1 (greedy first term, smallest x with 1/x < 4/p).  Exact 3-term rep with x1=g1 <=> 2-term rep of r1=4/p-1/g1.
 Also: smallest x1 >= ceil(p/4) (offset k=x1-ceil(p/4)) that admits an exact 3-term rep (search k<=KMAX), and
 the greedy 3-term underapproximation gap after 3 greedy terms (exact iff greedy completes)."""
import sys
from fractions import Fraction as F
from sympy import primerange, factorint, divisors
PMAX = int(sys.argv[1]); KMAX = int(sys.argv[2])

def two_term(a, b):
    """exists positive y,z with a/b = 1/y+1/z ; (a,b) reduced, a>0."""
    if a <= 0: return None
    # (a y - b)(a z - b) = b^2 ; u = a y - b > 0 divides b^2, u ≡ -b (mod a), b^2/u ≡ -b (mod a)
    nb = (-b) % a
    for u in divisors(b * b):
        if u % a == nb and (b * b // u) % a == nb:
            y = (b + u) // a; z = (b + b * b // u) // a
            assert F(1, y) + F(1, z) == F(a, b)
            return (y, z)
    return None

rows = []
for p in primerange(3, PMAX + 1):
    if p == 3: pass
    c = -(-p // 4)                      # ceil(p/4)
    g1 = p // 4 + 1                     # greedy first term
    r1 = F(4, p) - F(1, g1)
    greedy_ok = two_term(r1.numerator, r1.denominator) is not None
    # smallest offset with exact rep
    kmin = None
    for k in range(0, KMAX + 1):
        x1 = c + k
        r = F(4, p) - F(1, x1)
        if r <= 0: continue
        if two_term(r.numerator, r.denominator) is not None:
            kmin = k; break
    # greedy 3-term underapprox gap
    r = F(4, p); xs = []
    for _ in range(3):
        if r <= 0: break
        g = int(1 / r) + 1
        xs.append(g); r -= F(1, g)
    rows.append((p, g1, greedy_ok, kmin, float(r)))
n = len(rows)
print("primes", n)
print("greedy first term admits exact 3-term rep:", sum(1 for r in rows if r[2]), "of", n)
print("offset k=x1-ceil(p/4) of smallest exact rep: histogram", {k: sum(1 for r in rows if r[3] == k) for k in range(0, 6)}, "none<=KMAX:", sum(1 for r in rows if r[3] is None))
print("greedy 3-term remainder >0 (gap) count:", sum(1 for r in rows if r[4] > 0))
for r in rows[:12]: print(r)
