"""Z0184 (pass 2, SK0): series-parallel resistor networks built from k unit resistors.
R_1={1}; R_k = {a+b} U {ab/(a+b)} over a in R_i, b in R_j, i+j=k (all SP networks, multiset-free).
For ES: conductance 4/n = 1/(R) means resistance n/4 = parallel of three series chains of lengths x,y,z (x+y+z units),
i.e. 4/n=1/x+1/y+1/z.  Question: for each n, minimal k with n/4 in R_k, versus the minimal x+y+z over ES triples."""
from fractions import Fraction as F
import sys
KMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 6
R = {1: {F(1)}}
for k in range(2, KMAX + 1):
    s = set()
    for i in range(1, k):
        j = k - i
        for a in R[i]:
            for b in R[j]:
                s.add(a + b); s.add(a * b / (a + b))
    R[k] = s
    print("k", k, "distinct SP resistances", len(s), flush=True)
mink = {}
for k in range(1, KMAX + 1):
    for r in R[k]:
        mink.setdefault(r, k)
NMAX = 30
out = []
for n in range(5, NMAX + 1):
    r = F(n, 4)
    mk = mink.get(r)
    # minimal units of an ES-type 3-branch parallel: min over x<=y<=z with 1/x+1/y+1/z=4/n of x+y+z
    best = None
    for x in range(-(-n // 4), 3 * n // 4 + 2):
        t = F(4, n) - F(1, x)
        if t <= 0: continue
        for y in range(x, int(2 / t) + 2):
            t2 = t - F(1, y)
            if t2 > 0 and t2.numerator == 1 and t2.denominator >= y:
                s = x + y + t2.denominator
                best = s if best is None or s < best else best
    out.append((n, mk, best))
print("n, min k with n/4 in R_k (k<=%d), min units of 3-branch ES network:" % KMAX)
print(out)
