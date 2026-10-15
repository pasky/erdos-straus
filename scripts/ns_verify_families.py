"""O221: independent check of families found by ns_polyfam.py: for every family and every m < MMAX in its classes,
the ET map gives positive integers (x, y, z) with 4/n = 1/x + 1/y + 1/z exactly (n = m^2 + k).
Type I: (x, y, z) = (abd n, acd, bcd); Type II: (abd, acd n, bcd n).  Usage: ns_verify_families.py K FAMFILE MMAX"""
import sys, ast
from fractions import Fraction as F
K = int(sys.argv[1]); fams = [ast.literal_eval(l) for l in open(sys.argv[2])]; MMAX = int(sys.argv[3])
def ev(cs, m): return sum(F(c) * m ** i for i, c in enumerate(cs))
checked = bad = 0
for kind, P, L, good in fams:
    if not good: continue
    for r in good:
        for m in range(r + L * (1 + 100 // L), MMAX, L):
            n = m * m + K
            v = {name: ev(cs, m) for name, cs in P.items()}
            if any(x.denominator != 1 or x <= 0 for x in v.values()): bad += 1; continue
            a, b, c, d = (int(v[s]) for s in "abcd")
            x, y, z = (a * b * d * n, a * c * d, b * c * d) if kind == "TypeI" else (a * b * d, a * c * d * n, b * c * d * n)
            checked += 1
            if F(1, x) + F(1, y) + F(1, z) != F(4, n): bad += 1
print(f"k={K}: {len(fams)} families, {checked} (family, m) instances checked, {bad} failures")
