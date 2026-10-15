"""z1 (O224): the pentagon in the Fano plane P(L/2L). For each cell (t,u,v) mod 4 (n odd), list the 7 nonzero classes
of L/2L, q(x) = Q(x) mod 4, the pentagon classes e1,e2,e3,p f1 = A e1+u e2+e3, p f3 = e1+v e2+A* e3 (mod 2).
Also count classes mod 2^j L with Q = 0 mod 2^{j+1} (depth-j classes) and how often a pentagon vector is one of them."""
from itertools import product
def Q(t,u,v,x):
    a,b,c = x
    return v*a*a + t*b*b + u*c*c - 2*a*b - 2*b*c
res = {}
for t,u,v in product(range(1,9), repeat=3):
    n = t*u*v-u-v
    if n % 2 == 0: continue
    A, As = t*u-1, t*v-1
    pent = [(1,0,0),(0,1,0),(0,0,1),(A%2,u%2,1),(1,v%2,As%2)]
    pent = [tuple(x) for x in pent]
    cls = [x for x in product(range(2),repeat=3) if any(x)]
    iso = [x for x in cls if Q(t,u,v,x) % 4 == 0]
    distinct = len(set(pent))
    nonp = [x for x in cls if x not in pent]
    key = (len(iso), distinct, len(set(iso) & set(pent)), tuple(Q(t,u,v,x) % 4 for x in nonp))
    res[key] = res.get(key, 0) + 1
for k, c in sorted(res.items()): print('iso', k[0], 'distinct pentagon classes', k[1], 'iso&pent', k[2], 'q on non-pentagon', k[3], ':', c)
