"""Search natural sub-counts of E(p) (X-slice certificates) for a forced parity on primes p = 1 (24). (O164 §6)
Features of (t,u,v): t%8, u%4, v%4, A%8, B%8 (A=tu-1, B=tv-1), order sign(u-v).
Tests all conjunctions of <= 2 feature=value literals; reports those with constant parity on all primes,
then checks them on odd squares (T1 control).  Usage: python wr_parity_search.py NMAX"""
import sys, itertools
from math import isqrt
from sympy import divisors, isprime

def elems(n):
    out = []
    for u in range(1, isqrt(n) + 4):
        for v in divisors(n + u):
            if v < u or (n + u + v) % (u * v): continue
            t = (n + u + v) // (u * v)
            for (a, b) in ((u, v), (v, u)) if u != v else ((u, v),):
                if (t * a - 1) % 4 == 0:
                    A, B = t * a - 1, t * b - 1
                    out.append((("t8", t % 8), ("u4", a % 4), ("v4", b % 4), ("A8", A % 8), ("B8", B % 8),
                                ("ord", (a > b) - (a < b)), ("t3", t % 3), ("u3", a % 3)))
    return out

N = int(sys.argv[1])
ps = [p for p in range(25, N + 1, 24) if isprime(p)]
data = [elems(p) for p in ps]
lits = sorted({l for d in data for e in d for l in e})
cands = [()] + [(l,) for l in lits] + [c for c in itertools.combinations(lits, 2) if c[0][0] != c[1][0]]
def par(d, c): return sum(all(l in e for l in c) for e in d) % 2
good = []
for c in cands:
    ps_par = {par(d, c) for d in data}
    if len(ps_par) == 1: good.append((c, ps_par.pop()))
print("primes", len(ps), "candidates", len(cands), "constant-parity subcounts:", len(good))
def cnt(d, c): return sum(all(l in e for l in c) for e in d)
nontriv = [(c, v) for c, v in good if v == 1 or any(cnt(d, c) for d in data)]
print("nontrivial (odd, or even but nonempty somewhere):", len(nontriv))
for c, v in nontriv: print(" ", c, "parity", v, "max count", max(cnt(d, c) for d in data))
