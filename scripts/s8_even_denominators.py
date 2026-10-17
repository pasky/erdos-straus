"""O258 item (vi): k/n = 1/x+1/y+1/z  <=>  4/n has the solution ((k/4)x, (k/4)y, (k/4)z) (4 | k).  So the numerator
model k is "ES with (k/4) | gcd(x, y, z)".  Count all solutions of 4/n and those with all denominators even.
Usage: PYTHONPATH=scripts uv run python scripts/s8_even_denominators.py n1 n2 ...
"""
import sys
from fractions import Fraction
from math import gcd

def sols(n, k=4):
    out = []
    r = Fraction(k, n)
    x = n // k + 1
    while Fraction(3, x) >= r:
        r1 = r - Fraction(1, x)
        if r1 > 0:
            y = max(x, int(1 / r1) + 1 if (1 / r1) != int(1 / r1) else int(1 / r1))
            while Fraction(2, y) >= r1:
                r2 = r1 - Fraction(1, y)
                if r2 > 0 and r2.numerator == 1 and r2.denominator >= y:
                    out.append((x, y, r2.denominator))
                y += 1
        x += 1
    return out

if __name__ == "__main__":
    for a in sys.argv[1:]:
        n = int(a); S = sols(n)
        ev = [s for s in S if all(t % 2 == 0 for t in s)]
        s8 = sols(n, 8)
        print(f"n={n}: 4/n solutions {len(S)}, with x,y,z all even {len(ev)}; 8/n solutions {len(s8)}"
              f" (consistent: {len(ev) == len(s8)})")
