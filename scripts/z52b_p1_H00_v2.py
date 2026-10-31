"""Z0109/Z0110 pass-1: for primes p, enumerate all solutions 4/p = 1/x+1/y+1/z (x ≤ y ≤ z) and report
(#solutions, #all-even, #with some denominator ≡ 0 mod 4, #solutions where 4 | some denom but not all even).
Lemma (PROVED, 2-adic): all-even ⇒ some denominator ≡ 0 (mod 4)."""
import sys
from math import gcd
def sols(p):
    out = []
    for x in range(p//4 + 1, 3*p//4 + 1):
        num, den = 4*x - p, p*x          # 1/y + 1/z = num/den
        if num <= 0: continue
        g = gcd(num, den); num //= g; den //= g
        for y in range(max(x, den//num + 1), 2*den//num + 1):
            n2 = num*y - den; d2 = den*y
            if n2 > 0 and d2 % n2 == 0: out.append((x, y, d2//n2))
    return out
for p in map(int, sys.argv[1:]):
    S = sols(p)
    ae = [s for s in S if all(t % 2 == 0 for t in s)]
    f4 = [s for s in S if any(t % 4 == 0 for t in s)]
    print(p, len(S), len(ae), len(f4), [s for s in f4 if s not in ae][:3])
