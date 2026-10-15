"""z1 (O224): cell check of the Fano/tree-depth law. Over all cells (t,u,v) mod 2^K with n odd:
 - chi=-1 cells (some pentagon quantity = 0 mod 4) split by #pentagon quantities = 0 mod 4 (1 or 2);
 - fraction of chi=-1 cells in S_{2^k} vs the depth law f_k = (2/3)2^{-(k-2)} + (1/3)(1-(1-2^{-(k-2)})^2)
   (one or two independent fair bits per further level)."""
import sys
from itertools import product
from fractions import Fraction as F
K = int(sys.argv[1]); m = 2**K
tot = {1: 0, 2: 0}; hit = {k: {1: 0, 2: 0} for k in range(2, K + 1)}
for t, u, v in product(range(m), repeat=3):
    n = (t*u*v - u - v) % m
    if n % 2 == 0: continue
    P = (t, u, v, (t*u - 1) % m, (t*v - 1) % m)
    c4 = sum(1 for x in P if x % 4 == 0)
    if c4 == 0: continue
    assert c4 in (1, 2)
    tot[c4] += 1
    for k in range(2, K + 1):
        if any(x % (2**k) == 0 for x in P): hit[k][c4] += 1
T = tot[1] + tot[2]
print('K', K, 'chi=-1 cells', T, 'one iso pentagon vector', F(tot[1], T), 'two', F(tot[2], T))
for k in range(2, K + 1):
    s = 2**-(k-2)
    law = F(2, 3) * F(1, 2**(k-2)) + F(1, 3) * (1 - (1 - F(1, 2**(k-2)))**2)
    print('S_%d: fraction of chi=-1 cells %s ; law %s ; by type: one %s two %s' % (2**k, F(hit[k][1] + hit[k][2], T), law,
          F(hit[k][1], tot[1]), F(hit[k][2], tot[2])))
