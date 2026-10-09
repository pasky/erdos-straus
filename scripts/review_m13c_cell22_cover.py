#!/usr/bin/env python3
"""R100: covered side of Comp. 3.1 by own bounded search.
T-generic subcells u mod 11^2 13^2 (u = 2 mod 11 and mod 13; 143 of them). A class (fam,P) covers a subcell
iff M_T | 11^2 13^2, r = 1 (mod M') and r = u (mod M_T).  Candidate parameters: all T-parts | 11^2 13^2,
T-free parts <= B, and the third parameter from the (necessary) divisibility conditions; final test is literal
class membership via review_m13c_tree.family().  Usage: review_m13c_cell22_cover.py B
"""
import sys
from math import gcd
sys.path.insert(0, "scripts")
from sympy import divisors

F = 121 * 169
TD = divisors(F)
cells = {u for u in range(F) if u % 11 == 2 and u % 13 == 2}
def tpart(m):
    t = 1
    for q in (11, 13):
        while m % q == 0: m //= q; t *= q
    return t
covered = {}
def modulus(fam, P):
    a, b, c = P
    if fam == "I1": assert (4*a*a*b + 1) % c == 0; return 4*a*b
    if fam == "I2": assert gcd(4*a*b, c) == 1; return 4*a*b*c
    if fam == "I3": assert gcd(4*a*b, c) == 1; return 4*a*b*c
    if fam in ("I4", "II1"): assert (a + b) % c == 0 and gcd(c, 4*a*b) == 1; return 4*a*b
    if fam == "II2": assert (c + 1) % (4*a*b) == 0; return c
    if fam == "II3": assert gcd(4*a*b, c) == 1; return 4*a*b*c
def member(fam, P, n):
    """literal ET Prop 1.9 class membership of n (re-derived, cf. review_m13c_tree.family)"""
    a, b, c = P
    if fam == "I1": return (n + c) % (4*a*b) == 0
    if fam == "I2": return (n + c) % (4*a*b) == 0 and (a*n + b) % c == 0
    if fam == "I3": return (n + c) % (4*a*b) == 0 and (n*n + 4*a*a*b) % c == 0
    if fam == "I4": return (n*c + 1) % (4*a*b) == 0
    if fam == "II1": return (n + c) % (4*a*b) == 0
    if fam == "II2": return (n + 4*a*a*b) % c == 0
    if fam == "II3": return (n + 4*a*a*b + c) % (4*a*b*c) == 0
def test(fam, P):
    try: M = modulus(fam, P)
    except AssertionError: return
    MT = tpart(M); Mp = M // MT
    if F % MT: return
    for u in cells:
        if u in covered: continue
        n = (1 + Mp * ((u - 1) * pow(Mp, -1, MT))) % M if MT > 1 else 1 % M   # n = 1 (M'), u (M_T)
        if member(fam, P, n): covered[u] = (fam, P)

B = int(sys.argv[1])
free = [x for x in range(1, B + 1) if x % 11 and x % 13]
for A in TD:
    for D in TD:
        if F % (A * D): continue
        for a1 in free:
            for d1 in free:
                a, d = A * a1, D * d1
                for g in divisors(4 * a * a * d + 1):
                    test("I1", (a, d, g))
                    for E in TD:
                        if F % (A * D * E) == 0:
                            test("II3", (a, d, E * g)); test("I3", (a, d, E * g))
                for g in divisors(a + d):           # II1/I4 (a,b=d,e)
                    test("II1", (a, d, g)); test("I4", (a, d, g))
                    for E in TD:                     # I2 (a,c=d,f), f' | a+c
                        if F % (A * D * E) == 0: test("I2", (a, d, E * g))
                for E in TD:                         # II2 (a,d,f): f = E f', f' | 4a^2d+1, 4ad | f+1
                    for g in divisors(4 * a * a * d + 1):
                        if (E * g + 1) % (4 * a * d) == 0: test("II2", (a, d, E * g))
unc = sorted(cells - set(covered))
print("B", B, "covered", len(covered), "uncovered", len(unc))
print("uncovered x11 mod 121:", sorted({u % 121 for u in unc}), "x13 mod 169:", sorted({u % 169 for u in unc}))
