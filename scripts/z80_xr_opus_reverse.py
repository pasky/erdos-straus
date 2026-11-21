"""Opus cross-lab review of notes/z80/EXTREME.md §1: numerical sanity of the
reverse incidence (1).  For all primes p<=PMAX, enumerate every sorted solution
(direct divisor method), tally incoming witnesses per smallest denominator x,
check tally(x) <= w(x) for all x, and print sum_{x<=Z} w(x)^2 / (Z log^k Z)."""
import math, sys
from collections import Counter
PMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 6000
Z = 3*PMAX//4+1
spf = list(range(4*Z*Z+10)) if False else None
def fac(n):
    f = {}; q = 2
    while q*q <= n:
        while n % q == 0: f[q] = f.get(q, 0)+1; n //= q
        q += 1
    if n > 1: f[n] = f.get(n, 0)+1
    return f
def divs(f):
    ds = [1]
    for q, e in f.items(): ds = [d*q**i for d in ds for i in range(e+1)]
    return ds
def tau(n): return math.prod(e+1 for e in fac(n).values())
def isp(n): return n > 1 and all(n % q for q in range(2, math.isqrt(n)+1))
tally = Counter()
for p in range(3, PMAX+1):
    if not isp(p): continue
    for x in range(p//4+1, 3*p//4+1):
        g = 4*x-p; s = p*x; fx = fac(x); fs = dict(fx); fs[p] = fs.get(p, 0)+1
        for h in divs({q: 2*e for q, e in fs.items()}):
            if h > s or (s+h) % g or (s+s*s//h) % g: continue
            y = (s+h)//g
            if y >= x: tally[x] += 1
def w(x):
    fx = fac(x); tot = 0
    for a in divs(fx):
        for d in divs(fac(x//a)):
            c = x//a//d  # (a,c,d) ordered with acd=x ; also (a,b,d) with b=c
            tot += tau(4*a*a*d+1) + tau(a+c)
    return tot
W = {x: w(x) for x in range(1, Z+1)}
bad = [x for x in tally if tally[x] > W[x]]
print('primes <=', PMAX, 'witnesses', sum(tally.values()), 'distinct x', len(tally), 'violations', len(bad))
print('max tally/w', max(tally[x]/W[x] for x in tally))
for z in (Z//8, Z//4, Z//2, Z):
    S = sum(W[x]**2 for x in range(1, z+1)); print('Z', z, 'sum w^2 /Z', S/z, '/(Z log^4 Z)', S/z/math.log(z)**4)
