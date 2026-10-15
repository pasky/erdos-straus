"""R237: the cube/D_e class family WITHOUT the counting truncation V < l/4 (Prop 5.1/CAP_GROWING Prop 1.3 need none).
For primes l = 11 (12) count distinct classes -4*9^j mod l (D = 9^j in D_inf(l), since 3 | K=(l+1)/4) vs the
truncated count used by Thm 3.1 (V < l/4), and exhibit an exact ES^(y) solution with D = 9^j > l.
Also: single-prime large-sieve sum L1 = sum_{l<=Q} w(l)/(l-w(l)) for the full e=inf family -> power saving."""
import sys
from fractions import Fraction
from sympy import primerange, isprime, factorint

def classes_9pow(l, jmax=None):
    seen, v, j = set(), 1, 0
    while True:
        c = (-4 * v) % l
        if c in seen or (jmax is not None and j > jmax): break
        seen.add(c); v = v * 9 % l; j += 1
    return len(seen)

Q = int(sys.argv[1]) if len(sys.argv) > 1 else 200000
L1 = 0.0; n = 0; small = 0
for l in primerange(11, Q):
    if l % 12 != 11: continue
    w = classes_9pow(l)            # e = inf, D = 9^j only (a SUBfamily of D_inf(l))
    n += 1; small += (w * w < l / (2 * len(str(l))))
    L1 += w / (l - w)
print(f"primes l=11 (12) below {Q}: {n}; #(w < sqrt(l)/~log) = {small}; L1 = sum w/(l-w) = {L1:.1f}; Q^(1/2) = {Q**0.5:.1f}")
for l in (11, 23, 47, 59, 83, 107):
    trunc = sum(1 for j in range(0, 40) if 4 * 9**j < l)
    print(f"l={l}: classes from D=9^j: full {classes_9pow(l)} (= (l-1)/2? {classes_9pow(l)==(l-1)//2}), with V<l/4: {trunc}")
# exact solution with D = 9^3 = 729 > l = 11 at e = infinity (and e = 2 since t = 6 <= 2*1 + 2*2)
l, D = 11, 729; A = 3
p = next(q for q in range(5, 10**6) if isprime(q) and (q + 4 * D) % l == 0)
E = (p + 4 * D) // l; x = (p + E) // 4; y = p * A; z = Fraction(p * x * A, D)
assert Fraction(4, p) == Fraction(1, x) + Fraction(1, y) + 1 / z
print(f"l=11, D=729, p={p}: x={x}, y={y}, z={z}, den z factor {factorint(z.denominator)} (3 | y: {y % 3 == 0})")
