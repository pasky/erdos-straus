# z58 TERNARY: Shimura-orbit structure of the R(n)=0 census (LOGIC, n = 1 mod 4, n <= 1e10).
# For each non-square zero n write n = t*m^2 (t squarefree). Report: zeros with m > 1, those with t prime
# ("orbit zeros of the prime t"), and per-level survival (m coprime to a level N).
import gzip, sys
from sympy import factorint, isprime
src = 'data/z58/logic/zeros_1e10.txt.gz'
Z = [int(x) for x in gzip.open(src, 'rt') if x.strip() and x[0] != '#']
from math import isqrt
out = []
for n in Z:
    r = isqrt(n)
    if r * r == n: continue
    f = factorint(n); t = 1; m = 1
    for q, e in f.items():
        if e % 2: t *= q
        m *= q ** (e // 2)
    out.append((n, t, m, f))
print('# non-square zeros:', len(out))
comp = [x for x in out if not isprime(x[0])]
print('# composite non-square zeros:', len(comp), ' with m>1:', sum(1 for x in comp if x[2] > 1))
orb = [x for x in comp if x[2] > 1 and isprime(x[1])]
print('# orbit zeros n = t m^2, t prime, m > 1:', len(orb))
for n, t, m, f in orb:
    print('ORB', n, 't=%d' % t, 'm=%d' % m, 'm-factors', dict(factorint(m)), 't mod 840 =', t % 840)
# survival vs level: orbit zeros whose m is coprime to all odd primes <= P
for P in [3, 5, 7, 11, 13]:
    ps = [q for q in range(3, P + 1) if isprime(q)]
    s = [x for x in orb if all(x[2] % q for q in ps)]
    sq = [x for x in comp if x[2] > 1 and all(x[2] % q for q in ps)]
    print('# m coprime to odd primes <= %d: orbit zeros (t prime) %d ; all comp zeros with m>1 %d' % (P, len(s), len(sq)),
          [(x[0], x[1], x[2]) for x in s][:12])
