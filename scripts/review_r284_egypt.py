"""R284: brute-force all x<=y<=z with m/n = 1/x+1/y+1/z (exact integer arithmetic)."""
import sys
from fractions import Fraction
def sols(m, n):
    out = []
    for x in range(n // m + 1, 3 * n // m + 2):
        r = Fraction(m, n) - Fraction(1, x)
        if r <= 0: continue
        y0 = max(x, -(-r.denominator // r.numerator))
        for y in range(y0, int(2 / r) + 2):
            s = r - Fraction(1, y)
            if s <= 0: continue
            if s.numerator == 1 and s.denominator >= y: out.append((x, y, s.denominator))
    return out
for m, n in [(8, 131), (8, 241), (4, 241), (4, 131)]:
    s = sols(m, n); print(m, n, len(s), s[:8])
