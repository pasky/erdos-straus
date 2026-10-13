"""bsA_wu: for the chain lattice G(v,t,u) (odd det n), characteristic (Wu) vector w, w.w mod 8;
test whether Jacobi (A/n) is a function of (n mod 8, w.w mod 8)  [van der Blij / Rokhlin reading]."""
import itertools
from collections import defaultdict
from sympy import jacobi_symbol
tab = defaultdict(set)
for v, t, u in itertools.product(range(2, 34), repeat=3):
    n = t*u*v - u - v
    if n % 2 == 0: continue
    G = [[v, -1, 0], [-1, t, -1], [0, -1, u]]
    for eps in itertools.product((0, 1), repeat=3):
        if all(sum(G[j][i]*eps[i] for i in range(3)) % 2 == G[j][j] % 2 for j in range(3)): break
    ww = sum(eps[i]*G[i][j]*eps[j] for i in range(3) for j in range(3))
    tab[(n % 8, ww % 8)].add(jacobi_symbol(t*u - 1, n))
amb = {k: v for k, v in tab.items() if len(v) > 1}
print("cells (n mod 8, w.w mod 8) -> Jacobi values:", dict(sorted(tab.items())))
print("ambiguous cells:", amb)
