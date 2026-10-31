"""z52d audit A3, Z0873: at n=2^k no solution of 4/n=1/x+1/y+1/z (x<=y<=z) has exactly one denominator divisible by n.
Proof (2-adic): if n|z, n∤x, n∤y then v2(1/x+1/y) >= -(k-1) but v2(4/n-1/z) = -v2(z) <= -k. Brute-force check k<=9."""
from fractions import Fraction
def sols(n):
    out = []
    for x in range(n // 4 + 1, 3 * n // 4 + 1):
        r = Fraction(4, n) - Fraction(1, x)
        if r <= 0: continue
        for y in range(max(x, int(1 / r) + 1), int(2 / r) + 1):
            s = r - Fraction(1, y)
            if s > 0 and s.numerator == 1 and s.denominator >= y: out.append((x, y, s.denominator))
    return out
for k in range(1, 10):
    n = 2**k; S = sols(n)
    cnt = [sum(1 for d in s if d % n == 0) for s in S]
    print(n, "solutions", len(S), "#with exactly one denom div by n:", cnt.count(1), "hist", {c: cnt.count(c) for c in set(cnt)})
