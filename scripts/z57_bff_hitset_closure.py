#!/usr/bin/env python3
"""Is the hit set {d <= p^{3/4} : HIT(d)} closed under products / lcm / divisors?  (memo §2.2)"""
import sys; sys.path.insert(0, 'scripts')
from math import gcd
from sympy import nextprime
def hits(p, D):
    out = []
    for d in range(3, D + 1, 4):
        n = d - p % d
        if (d + 1) % (4 * n) == 0: out.append(d)
    return out
p = nextprime(10**8)
while p % 4 != 1: p = nextprime(p)
D = int(p ** 0.75)
S = hits(p, D); Sset = set(S)
print('p', p, 'D', D, '#hits', len(S), 'first', S[:12])
prod_ok = sum(1 for a in S for b in S if a < b and a * b <= D and a * b in Sset)
prod_tot = sum(1 for a in S for b in S if a < b and a * b <= D)
div_ok = sum(1 for a in S for b in S if a < b and b % a == 0)
subdiv = sum(1 for b in S for a in range(3, b, 4) if b % a == 0)  # divisors = 3 (4) of hits
subdiv_ok = sum(1 for b in S for a in range(3, b, 4) if b % a == 0 and a in Sset)
print('products of two hits (<=D) that are hits:', prod_ok, '/', prod_tot)
print('pairs a|b both hits:', div_ok, ';  3(4)-divisors of hits that are hits:', subdiv_ok, '/', subdiv)
nd = {d: d - p % d for d in S}
pairs = [(a, b, nd[a], nd[b]) for a in S for b in S if a < b and b % a == 0]
print('divisor pairs (a, b, n_a, n_b):', pairs)
