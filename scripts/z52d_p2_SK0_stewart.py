"""Z0408 (pass 2, SK0): check the two-unit-fraction criterion (Stewart 1964 form) against brute force.
Claim tested: m/n = 1/x+1/y (x,y positive integers) iff there exist coprime divisors d1,d2 of n with m | (d1+d2)?? -- we test
the exact statement recorded in BRAINSTORM/z52b_dividing.md (#255): 'iff two coprime divisors of n sum to a multiple of m'.
Brute force: x,y <= 3n^2 (complete since 1/x+1/y=m/n forces x,y <= n(n+... ) ; we use bound x,y <= 2 m n) ."""
from math import gcd
from fractions import Fraction as F
def brute(m, n):  # exact search over x <= 2mn
    t = F(m, n)
    for x in range(1, 2 * m * n + 2):
        r = t - F(1, x)
        if r <= 0: continue
        if r.numerator == 1: return True
        # 1/y = r  -> y = denominator
        y = r.denominator
        if F(1, y) == r: return True
    return False
def divisors(n): return [d for d in range(1, n + 1) if n % d == 0]
def stewart(m, n):
    D = divisors(n)
    for d1 in D:
        for d2 in D:
            if gcd(d1, d2) == 1 and (d1 + d2) % m == 0:
                return True
    return False
# Only coprime pairs: the unrestricted form fails for non-reduced m/n (e.g. 4/2=1+1), as expected.
bad = []; tot = 0; yes = 0
for n in range(1, 121):
    for m in range(1, 121):
        if gcd(m, n) != 1: continue
        b = brute(m, n); s = stewart(m, n); tot += 1; yes += b
        if b != s: bad.append((m, n, b, s))
print("coprime pairs", tot, "solvable", yes, "mismatches", len(bad), bad[:12])
