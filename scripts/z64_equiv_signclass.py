"""z64 EQUIV push on E6/E7: the Jacobi sign of a length-3 word as a lens-space / Dedekind-sum invariant.
For a word n = tuv - u - v (t,u,v >= 2, n odd, A = tu - 1, A* = tv - 1, gcd(A,n) = 1):
 (1) check Hirzebruch/Barkan:  12 n s(A,n) = A + A* + n (t+u+v-9)   (exact, Fractions; n <= NCHK)
 (2) check Rademacher's congruence 12 n s(A,n) = n + 1 - 2 (A/n) (mod 8)
 (3) hence (A/n) is a function of (t,u,v) mod 8 (n is a polynomial in t,u,v): tabulate the sign classes
     Sigma- = {(t,u,v) mod 8 : sign -1} and check against direct Jacobi symbols for all words n <= NMAX;
 (4) check that the table is in fact a function of (t,u,v) mod 4 (= DEDEKIND_ES Thm 4.5 / Cor 4.1, re-derived here
     via the Dedekind-sum route; nothing new, an independent confirmation).
Usage: python z64_equiv_signclass.py NCHK NMAX"""
import sys
from fractions import Fraction as F
from math import gcd
from sympy import jacobi_symbol
NCHK = int(sys.argv[1]) if len(sys.argv) > 1 else 3000
NMAX = int(sys.argv[2]) if len(sys.argv) > 2 else 10**6
def saw(x):
    if x.denominator == 1: return F(0)
    return x - (x.numerator // x.denominator) - F(1, 2)
def dedekind_slow(a, n):
    return sum(saw(F(r, n)) * saw(F(a * r, n)) for r in range(1, n))
def dedekind(a, c):
    # reciprocity: s(a,c) + s(c,a) = (a/c + c/a + 1/(ac))/12 - 1/4, gcd(a,c)=1, c>0
    a %= c
    if a == 0: return F(0)
    if c == 1: return F(0)
    return F(a * a + c * c + 1, 12 * a * c) - F(1, 4) - dedekind(c, a)
bad = 0; c1 = 0
for c in range(2, 60):
    for a in range(1, c):
        if gcd(a, c) == 1: assert dedekind(a, c) == dedekind_slow(a, c)
for t in range(2, NCHK):
    for u in range(2, NCHK):
        if 2 * t * u - u - 2 > NCHK: break
        for v in range(2, NCHK):
            n = t * u * v - u - v
            if n > NCHK: break
            if n % 2 == 0: continue
            A, As = t * u - 1, t * v - 1
            if gcd(A, n) != 1: continue
            s12n = 12 * n * dedekind(A, n)
            if s12n != A + As + n * (t + u + v - 9): bad += 1; print("FAIL Hirzebruch", t, u, v)
            if (s12n - (n + 1 - 2 * jacobi_symbol(A, n))) % 8 != 0: bad += 1; print("FAIL Rademacher", t, u, v)
            c1 += 1
print("(1)(2) exact Dedekind checks on", c1, "words, n <=", NCHK, "; failures", bad)
# (3) sign as a function of (t,u,v) mod 8, from the congruence: (A/n) = (n + 1 - X)/2 with X = A+A*+n(t+u+v-9) mod 8
def sign_formula(t, u, v):
    n = t * u * v - u - v
    X = (t * u - 1) + (t * v - 1) + n * (t + u + v - 9)
    d = (n + 1 - X) % 8
    return 1 if d == 2 else (-1 if d == 6 else 0)
cls = {}
for a in range(8):
    for b in range(8):
        for c in range(8):
            if (a * b * c - b - c) % 2 == 0: continue
            cls[(a, b, c)] = sign_formula(a + 8, b + 8, c + 8)
neg = sorted(k for k, s in cls.items() if s == -1); pos = sorted(k for k, s in cls.items() if s == 1)
print("odd-n residue classes (t,u,v) mod 8:", len(cls), " sign -1:", len(neg), " sign +1:", len(pos),
      " undetermined:", sum(1 for s in cls.values() if s == 0))
bad3 = 0; cnt = 0
for t in range(2, NMAX):
    if 4 * t - 4 > NMAX: break
    for u in range(2, NMAX):
        if 2 * t * u - u - 2 > NMAX: break
        for v in range(2, NMAX):
            n = t * u * v - u - v
            if n > NMAX: break
            if n % 2 == 0 or gcd(t * u - 1, n) != 1: continue
            if jacobi_symbol(t * u - 1, n) != cls[(t % 8, u % 8, v % 8)]: bad3 += 1
            cnt += 1
print("(3) words n <=", NMAX, ":", cnt, " mismatches with the mod-8 class table:", bad3)
# describe Sigma- compactly: by t mod 8
from collections import defaultdict
byt = defaultdict(list)
for (a, b, c) in neg: byt[a].append((b, c))
for a in range(8): print(" t=%d mod 8: sign -1 for (u,v) mod 8 in" % a, byt[a])
# (4) is the class table already a function of the letters mod 4 (DK Thm 4.5 / Cor 4.1)?
mod4 = {}
ok4 = True
for (a, b, c), s in cls.items():
    k = (a % 4, b % 4, c % 4)
    if k in mod4 and mod4[k] != s: ok4 = False
    mod4[k] = s
print("(4) sign table depends only on (t,u,v) mod 4:", ok4, "; mod-4 cells with sign -1:",
      sorted(k for k, s in mod4.items() if s == -1))
