#!/usr/bin/env python3
"""z69 IDEAB sanity check for idea I17 (R8): reduced forms [A,B,C] of discriminant -4p with 4 | B, B>0 and
A == -1 (mod B) or C == -1 (mod B)  ==> Type II solution with d = 1.
Reports, for primes p == 1 (4) up to PMAX: class number, #good reduced forms, #all d=1 solutions (unordered),
and how often the reduced forms alone / the d=1 slice alone suffice."""
import sys, math
from sympy import primerange
PMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 20000
def stats(p):
    h = 0; good = 0
    for beta in range(0, int(math.isqrt(p // 3)) + 2):
        n = p + beta * beta
        A = max(2 * beta, 1)
        while A * A <= n:
            if n % A == 0:
                C = n // A
                if 2 * beta <= A <= C:
                    mult = 1 if (beta == 0 or 2 * beta == A or A == C) else 2   # B and -B
                    h += mult
                    B = 2 * beta
                    if beta > 0 and beta % 2 == 0 and ((A + 1) % B == 0 or (C + 1) % B == 0):
                        good += 1
            A += 1
    # all d=1 Type II solutions, UNORDERED in (a,b): p*c = 4abc - a - b  <=>  (4ac-1) | p + 4a^2, b = ((p+4a^2)/(4ac-1) + p)/(4a).
    # For a <= b and c >= 1: p = 4ab - (a+b)/c >= 4a^2 - 2a, so a <= (1 + sqrt(1+4p))/4.  (Fixed after internal review:
    # the earlier cutoff a <= 2 sqrt(p) with f stepping from 4a-1 dropped the mirror solutions and mixed ordered/unordered.)
    alld1 = 0
    a = 1
    while 4 * a * a - 2 * a <= p:
        n = p + 4 * a * a
        f = 4 * a - 1
        while f <= n:
            if n % f == 0:
                e = n // f; b = (e + p) // (4 * a)
                assert (e + p) % (4 * a) == 0
                if b >= a: alld1 += 1
            f += 4 * a
        a += 1
    return h, good, alld1
rows = []
for p in primerange(5, PMAX):
    if p % 4 == 1: rows.append((p,) + stats(p))
six = [r for r in rows if r[0] % 840 in (1, 121, 169, 289, 361, 529)]
for name, R in (("all p==1(4)", rows), ("six classes", six)):
    n = len(R)
    print(f"{name}: primes {n};  no good reduced form: {sum(1 for r in R if r[2]==0)}  ; no d=1 solution at all: {sum(1 for r in R if r[3]==0)}")
    for lo, hi in ((5, 1000), (1000, 10000), (10000, PMAX)):
        S = [r for r in R if lo <= r[0] < hi]
        if S: print(f"   p in [{lo},{hi}): n={len(S)}  mean h={sum(r[1] for r in S)/len(S):.1f}  mean good-reduced={sum(r[2] for r in S)/len(S):.2f}  mean #d=1 solutions (unordered)={sum(r[3] for r in S)/len(S):.2f}  frac(no d=1)={sum(1 for r in S if r[3]==0)/len(S):.3f}")
print("largest p with no d=1 solution:", max((r[0] for r in rows if r[3] == 0), default=None), " last few:", [r[0] for r in rows if r[3] == 0][-8:])
print("sample:", rows[:6])
