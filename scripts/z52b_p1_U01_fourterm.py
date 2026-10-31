"""U01 Z3073/Z0310/Z1639: 4-term reps of 4/p (x1<=x2<=x3<=x4, p<=PMAX): count, mergeable pairs (1/a+1/b unit), vs 3-term count.
Ranges: x1 in [ceil(p/4), 2p]; x2 in [x1, 4p]; remainder after x2 handled by two_term (exact)."""
import sys, os, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from z52b_p1_U01_common import primes_upto
from z52b_p1_U01_twoterm import two_term
from fractions import Fraction as Fr
PMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 100
def unit_sum(a, b):
    n = a + b; return n // math.gcd(n, a*b) == 1
def reps4(p):
    out = []
    for x1 in range(-(-p//4), 2*p+1):
        r1 = Fr(4, p) - Fr(1, x1)
        if r1 <= 0: continue
        for x2 in range(x1, 4*p+1):
            r2 = r1 - Fr(1, x2)
            if r2 <= 0: continue
            # remainder must be 2-term with denominators >= x2
            t = two_term(r2.numerator, r2.denominator)
            if t and t[0] >= x2:
                out.append((x1, x2, t[0], t[1]))
    return out
def count3(p):
    c = 0
    for x in range(-(-p//4), 3*p//4+2):
        r = Fr(4, p) - Fr(1, x)
        if r > 0 and r.numerator and two_term(r.numerator, r.denominator): c += 1
    return c
tot = {"reps4": 0, "reps4_with_mergeable_pair": 0}; rows = []
for p in primes_upto(PMAX):
    if p < 5: continue
    R = reps4(p)
    # normalise to 4-tuples
    quads = set()
    for r in R:
        quads.add(tuple(sorted((r[0], r[1], r[2], r[3]))))
    mer = 0
    for q4 in quads:
        if any(unit_sum(q4[i], q4[j]) for i in range(4) for j in range(i+1, 4)): mer += 1
    tot["reps4"] += len(quads); tot["reps4_with_mergeable_pair"] += mer
    rows.append((p, len(quads), mer, count3(p)))
print("p, #4-term sets (x1<=x2<=x3<=x4, x1>=p/4, x<=4p), #with a mergeable pair, #3-term x1-count:")
for r in rows[:12]: print(r)
print("totals over p<=%d:" % PMAX, tot, "primes:", len(rows))
bad = [r for r in rows if r[1] > 0 and r[2] == 0]
print("primes where 4-term reps exist but none has a mergeable pair:", bad[:8])
