"""Analyse exact counts f_I+f_II (a<=b) of odd n from bs_corr_count.c output by the squarefree
part s(n) (n = s*m^2).  Prints the minima overall, for primes, and per small s, and the
mean of f/log^3 n binned by s.  Usage: bs_corr_nearsq.py file1 [file2 ...]"""
import sys, math
from collections import defaultdict
from sympy import factorint, isprime
def sqfree(n):
    s = 1
    for q, e in factorint(n).items():
        if e % 2: s *= q
    return s
rows = []
for fn in sys.argv[1:]:
    for line in open(fn):
        n, a, b = map(int, line.split()); rows.append((n, a + b, a, b))
by_s = defaultdict(list); primes = []
for n, t, a, b in rows:
    s = sqfree(n); r = t / math.log(n) ** 3
    by_s[min(s, 10**9)].append((r, n, t))
    if isprime(n): primes.append((r, n, t))
allr = sorted((t / math.log(n) ** 3, n, t, sqfree(n)) for n, t, a, b in rows)
print('n range', min(r[0] for r in rows), max(r[0] for r in rows), 'count', len(rows))
print('10 smallest f/log^3 overall (r, n, f, s(n)):'); [print('  %.4f %d %d %d' % x) for x in allr[:10]]
primes.sort(); print('primes: count %d, min r %.4f at n=%d (f=%d), mean %.4f' % (len(primes), primes[0][0], primes[0][1], primes[0][2], sum(x[0] for x in primes) / len(primes)))
print('per small squarefree part s: (#n, min r, n at min, mean r)')
for s in sorted(by_s):
    if s > 60: break
    L = sorted(by_s[s]); print('  s=%d: %d  %.4f  %d  %.4f' % (s, len(L), L[0][0], L[0][1], sum(x[0] for x in L) / len(L)))
bins = [(1, 1), (2, 30), (31, 1000), (1001, 30000), (30001, 10**9)]
for lo, hi in bins:
    L = [x[0] for s, v in by_s.items() if lo <= s <= hi for x in v]
    if L: print('s in [%d,%d]: #n=%d min r %.4f mean r %.4f' % (lo, hi, len(L), min(L), sum(L) / len(L)))
