"""U01 Z0136 / Z0902 / Z0311 / Z0680 / Z0104 checks.
Z0136: per prime p<=PMAX, does some ES triple have pairwise coprime denominators?
Z0902: per prime p<=PMAX, count ES triples with x|yz±1 or y|xz±1 (x<=y<=z, any ordering checked over all 3 positions)
Z0311: p<=PMAX, is 4/p-1/x (x in [p/4,p]) a sum of two distinct PRIME-reciprocals 1/q1+1/q2 ?
Z0680: second implementation of U_m(p) for m=7..13 vs data/z52b/raw/m*_pr1e5.txt (p<=PMAX)
Z0104: Egyptian length over Z of a/b (a<=8, b<=40, a/b<1): min k<=3 with a/b = sum of k distinct unit fractions."""
import sys, os, math, gzip, itertools
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fractions import Fraction as Fr
import numpy as np
from z52b_p1_U01_common import primes_upto, load_m, REPO
from z52b_p1_U01_four import two_term_all
PMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 1000
def triples(p):
    S = set()
    for x in range(-(-p//4), (3*p)//4 + 1):
        A = 4*x - p
        if A <= 0: continue
        B = p*x; g = math.gcd(A, B)
        for a, b in two_term_all(A//g, B//g):
            if a >= x: S.add(tuple(sorted((x, a, b))))
    return S
res = {"coprime": 0, "n": 0, "dvd": [], "pr2": 0}
for p in primes_upto(PMAX):
    if p < 5: continue
    T = triples(p); res["n"] += 1
    if any(math.gcd(math.gcd(a, b), c) == 1 and math.gcd(a, b) == 1 and math.gcd(a, c) == 1 and math.gcd(b, c) == 1 for a, b, c in T):
        res["coprime"] += 1
    cnt = 0
    for a, b, c in T:
        for x, y, z in ((a, b, c), (b, a, c), (c, a, b)):
            if (y*z - 1) % x == 0 or (y*z + 1) % x == 0: cnt += 1; break
    res["dvd"].append((p, len(T), cnt))
    # Z0311: 4/p - 1/x = 1/q1+1/q2 with q1,q2 distinct primes
    def isprime(n):
        return n > 1 and all(n % q for q in range(2, int(n**0.5)+1))
    ok = False
    for x in range(-(-p//4), p+1):
        r = Fr(4, p) - Fr(1, x)
        if r <= 0: continue
        for a, b in two_term_all(r.numerator, r.denominator):
            if a != b and isprime(a) and isprime(b): ok = True; break
        if ok: break
    res["pr2"] += ok
print(f"Z0136: primes p<={PMAX}: {res['coprime']} of {res['n']} have an ES triple with pairwise coprime denominators")
dv = res["dvd"]
print(f"Z0902: triples with x|yz±1 in some position: primes with >=1 such triple {sum(1 for d in dv if d[2]>0)} of {len(dv)}; fraction of all triples {sum(d[2] for d in dv)/max(1,sum(d[1] for d in dv)):.3f}; primes where EVERY triple has it: {sum(1 for d in dv if d[1]>0 and d[2]==d[1])}")
print(f"Z0311: primes p<={PMAX} with 4/p-1/x = 1/q1+1/q2 (distinct primes) for some x in [p/4,p]: {res['pr2']} of {res['n']}")
# Z0680: second implementation for m=7..13 at p<=PMAX (ES-type triples with numerator m, p prime)
def triples_m(m, p):
    S = set()
    for x in range(-(-p//m), (3*p)//m + 1):
        A = m*x - p
        if A <= 0: continue
        B = p*x; g = math.gcd(A, B)
        for a, b in two_term_all(A//g, B//g):
            if a >= x: S.add(tuple(sorted((x, a, b))))
    return S
bad = {}
for m in range(7, 14):
    ref = load_m(m)
    mm = 0
    for p in primes_upto(PMAX):
        if p <= 5: continue
        if len(triples_m(m, p)) != ref[p]: mm += 1
    bad[m] = mm
print("Z0680: second-implementation mismatches vs raw U_m(p), p<=%d:" % PMAX, bad)
# Z0104: Egyptian length over Z (distinct unit fractions), a/b < 1, a<=8, b<=40
def length_le3(a, b):
    if Fr(a, b) >= 1: return None
    for k in (1, 2, 3):
        if k == 1:
            if a == 1: return 1
        if k == 2:
            if any(True for _ in two_term_all(a, b) if True): return 2
        if k == 3:
            r = Fr(a, b)
            for x in range(-(-b//a), 3*b//a + 2 if a else 2):
                q = r - Fr(1, x)
                if q <= 0: continue
                if any(c != x for c, d in [(0,0)]) : pass
                if two_term_all(q.numerator, q.denominator): return 3
    return None
dist = {}
for a in range(1, 9):
    for b in range(a+1, 41):
        if math.gcd(a, b) != 1: continue
        L = length_le3(a, b)
        dist[L] = dist.get(L, 0) + 1
print("Z0104: Egyptian length (<=3 vs >3) distribution over a<=8, b<=40 coprime, a<b:", dist)
