"""z1: depth law conditional on n mod 16: among chi=-1 cells mod 32 with given n mod 16, fraction in S_8, S_16."""
from itertools import product
from fractions import Fraction as F
m = 32; tot = {}; h8 = {}; h16 = {}; one = {}
for t, u, v in product(range(m), repeat=3):
    n = (t*u*v - u - v) % m
    if n % 2 == 0: continue
    P = (t, u, v, (t*u-1) % m, (t*v-1) % m)
    if not any(x % 4 == 0 for x in P): continue
    c = n % 16
    tot[c] = tot.get(c, 0) + 1
    one[c] = one.get(c, 0) + (sum(x % 4 == 0 for x in P) == 1)
    h8[c] = h8.get(c, 0) + any(x % 8 == 0 for x in P)
    h16[c] = h16.get(c, 0) + any(x % 16 == 0 for x in P)
for c in sorted(tot):
    print('n=%2d mod 16: share one-iso %s  S8/S4 %s  S16/S4 %s' % (c, F(one[c], tot[c]), F(h8[c], tot[c]), F(h16[c], tot[c])))
