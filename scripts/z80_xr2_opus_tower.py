"""Opus round-2 independent signed census for EXTREME §8 (tower.txt).
Order coordinates by absolute value |x1|<=|x2|<=|x3|. Then k/n<=3/|x1|, and with
A=k/n-1/x1=a/b != 0 (k/n is not a unit fraction for these inputs), |x2|<=2/|A|.
x3 is then forced. Integer arithmetic only. Counts unordered triples by #negatives.
"""
from fractions import Fraction
from math import gcd

def census(k, n):
    assert n % k  # k/n is not 1/x, so A=0 never happens with x2=-x3
    out = [set(), set(), set(), set()]
    B1 = 3 * n // k
    for x1 in range(-B1, B1 + 1):
        if x1 == 0: continue
        a, b = k * x1 - n, n * x1          # A = a/b
        if a == 0: continue
        B2 = 2 * abs(b) // abs(a)
        for x2 in range(-B2, B2 + 1):
            if x2 == 0 or abs(x2) < abs(x1): continue
            den = a * x2 - b
            if den == 0: continue
            x3, r = divmod(b * x2, den)
            if r or x3 == 0 or abs(x3) < abs(x2): continue
            t = tuple(sorted((x1, x2, x3)))
            out[sum(v < 0 for v in t)].add(t)
    for s in out:
        for t in s: assert sum(Fraction(1, v) for v in t) == Fraction(k, n)
    return out

for k, n in [(8, 131), (8, 241), (4, 131), (4, 241)]:
    s = census(k, n)
    print(k, n, 'counts by #neg 0/1/2/3:', [len(x) for x in s],
          'examples:', [min(x, key=lambda t: (max(map(abs, t)), t)) if x else None for x in s[:3]])
