"""Least quadratic non-residue n_p for the HC>=44 primes below 1e12 vs. all primes p = 1 (8) in a sample window."""
import re, glob
from sympy import legendre_symbol, primerange
def lqnr(p):
    q = 2
    while legendre_symbol(q, p) != -1: q += 1
    return q
high = []
for f in glob.glob('data/z55/hco/census_*.txt'):
    high += [int(p) for p in re.findall(r'HIGH p=(\d+) HC=', open(f).read())]
from collections import Counter
h = Counter(lqnr(p) for p in high)
print("HC>=44 (n=%d): least QNR distribution" % len(high), sorted(h.items()))
print("  fraction with least QNR >= 7: %.3f" % (sum(v for k, v in h.items() if k >= 7) / len(high)))
samp = [p for p in primerange(10**11, 10**11 + 2 * 10**6) if p % 8 == 1]
g = Counter(lqnr(p) for p in samp)
print("all p=1(8) in [1e11,1e11+2e6] (n=%d):" % len(samp), sorted(g.items())[:8], "...")
print("  fraction with least QNR >= 7: %.3f" % (sum(v for k, v in g.items() if k >= 7) / len(samp)))
