# review_r235_t1.py -- R235: classify nu-words at odd squares by slot and by whether sqrt(-u) in Q(zeta_{nu u}).
import sys
from math import gcd
from sympy import factorint
from review_r235_words import words, slots


def disc_minus(u):
    f = factorint(u)
    u0 = 1
    for p, e in f.items():
        if e % 2:
            u0 *= p
    d = -u0
    return abs(d) if d % 4 == 1 else 4 * u0


out = {}
for m in range(3, int(sys.argv[1]), 2):
    n = m * m
    for (t, u, v) in words(n):
        S = slots((t, u, v)); A = S['A']
        for nu in [3, 5, 7, 11]:
            hit = [k for k, x in S.items() if x % nu == 0]
            if not hit:
                continue
            coprime = gcd(nu, u) == 1 and gcd(nu, n) == 1 and (n + u) % nu and gcd(A, nu) == 1
            if not coprime:
                continue
            inside = (nu * u) % disc_minus(u) == 0
            key = (nu, 'Aodd' if A % 2 else 'Aeven', 'inside' if inside else 'outside', tuple(sorted(hit)))
            out[key] = out.get(key, 0) + 1
for k in sorted(out):
    print(k, out[k])
