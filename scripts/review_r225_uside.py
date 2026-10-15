# R225 probe (EVIDENCE only): is the beyond-clean K0 depletion carried by words whose u (or v) makes
# p + u = m^2 + (K0 + u) a sum of two squares with K0 + u = s^2 (m = isqrt(p))?  For such words, if gcd(m, s) = 1,
# every odd prime r | tu - 1 has r = 1 mod 4 and (r/p) = (-u/r), so chi is forced by u (and the 2-part).
import sys, random
from sympy import isprime, divisors, factorint
from math import isqrt, gcd
def leg(a, p):
    a %= p
    return 0 if a == 0 else (1 if pow(a, (p - 1) // 2, p) == 1 else -1)
def words(p):
    u = 1
    while (u - 2) * u <= p:
        for v in divisors(p + u):
            if v >= u and (p + u + v) % (u * v) == 0:
                t = (p + u + v) // (u * v); yield t, u, v, (1 if u == v else 2)
        u += 1
random.seed(1)
P = [p for p in range(100001, 1000000, 4) if isprime(p)]
near = [p for p in P if p - isqrt(p) ** 2 < 30]; far = random.sample([p for p in P if p - isqrt(p) ** 2 >= 300], 300)
for name, S in (('K0<30', near), ('K0>=300', far)):
    agg = {}
    for p in S:
        m = isqrt(p); K0 = p - m * m
        clean = {}
        for t, u, v, mult in words(p):
            if t not in clean: clean[t] = all(leg(r, p) == 1 for r in factorint(t * p + 1))
            if clean[t]: continue                           # beyond-clean words only
            flag = False
            for w in (u, v):
                s = isqrt(K0 + w)
                if s * s == K0 + w and gcd(m, s) == 1: flag = True
            ch = leg(t * u - 1, p)
            a = agg.setdefault(flag, [0, 0]); a[0] += mult; a[1] += mult * (ch == -1)
    print(name, len(S), 'primes; beyond-clean words: flagged (K0+u or K0+v = s^2, gcd(m,s)=1):',
          agg.get(True), 'chi=-1 rate %.3f' % (agg[True][1] / agg[True][0]) if True in agg else '',
          '| unflagged:', agg.get(False), 'rate %.3f' % (agg[False][1] / agg[False][0]))
