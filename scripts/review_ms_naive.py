"""R197: naive Fraction-based solution counter (cross-check of review_ms_census.c count mode for small p)."""
import subprocess
import sys
from fractions import Fraction as F


def f(m, n):
    c = 0
    q = F(m, n)
    x = n // m + 1
    while F(3, x) >= q:
        r = q - F(1, x)
        y = max(x, int(1 / r) + 1 if (1 / r).denominator != 1 else int(1 / r))
        while F(2, y) >= r:
            s = r - F(1, y)
            if s > 0 and s.numerator == 1 and s.denominator >= y:
                c += 1
            y += 1
        x += 1
    return c


bad = 0
for m in (4, 5, 8, 12):
    for p in (3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103):
        if m % p == 0:
            continue
        out = subprocess.run([sys.argv[1], str(m), str(p), "count"], capture_output=True, text=True).stdout
        c = int(out.split("solutions=")[1].split()[0])
        if c != f(m, p):
            bad += 1
            print("MISMATCH", m, p, c, f(m, p))
print("naive vs C count mismatches:", bad)
