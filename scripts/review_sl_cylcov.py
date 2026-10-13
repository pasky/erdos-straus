"""R175: covered fraction (Case B, K <= KMAX) inside the cylinders v = (c,0,...,0) mod T^e around x*_c,
from a review_sl_caseB output file.  Exact (Fraction)."""
import sys
from fractions import Fraction
cyls = set()
for line in open(sys.argv[1]):
    K, a, b, vc = line.split()[:4]
    cyls.add(tuple(int(ch) for ch in vc))
cyls = sorted(cyls, key=len); mins = []
for c in cyls:
    if not any(c[:len(m)] == m for m in mins): mins.append(c)
for c in (1, 2):
    for e in range(1, 7):
        pre = (c,) + (0,) * (e - 1)
        # measure of covered inside cylinder pre (relative)
        m = Fraction(0)
        for cy in mins:
            if len(cy) <= e:
                if pre[:len(cy)] == cy: m = Fraction(1); break
            elif cy[:e] == pre:
                m += Fraction(1, 3 ** (len(cy) - e))
        print(f"c={c} v=(c,0..) mod T^{e} (u mod T^{e+1}): covered fraction {float(m):.4f}")
