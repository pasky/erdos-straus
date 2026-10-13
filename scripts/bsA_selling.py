"""bsA_selling: chain Gram G(v,t,u)=[[v,-1,0],[-1,t,-1],[0,-1,u]] is Selling-reduced with conorms
(v-1,t-2,u-1,1,0,1); Kirchhoff tree count of the 4-vertex multigraph = det = tuv-u-v; discriminant-form class
= Jacobi (A/n). Also: for general K4 multigraphs with prime tree number, distribution of pairing class."""
import itertools, sys
from sympy import Matrix, jacobi_symbol, isprime
def lap(w):  # w: dict edge->(weight) on K4, vertices 0..3; reduced Laplacian deleting vertex 0
    L = [[0]*4 for _ in range(4)]
    for (i, j), c in w.items():
        L[i][j] -= c; L[j][i] -= c; L[i][i] += c; L[j][j] += c
    return Matrix([r[1:] for r in L[1:]])
bad = 0; n_ok = 0
for v, t, u in itertools.product(range(2, 13), repeat=3):
    G = Matrix([[v, -1, 0], [-1, t, -1], [0, -1, u]])
    w = {(0, 1): v-1, (0, 2): t-2, (0, 3): u-1, (1, 2): 1, (2, 3): 1, (1, 3): 0}
    n = t*u*v - u - v
    if lap(w) != G or G.det() != n: bad += 1
    if n % 2 == 1:
        adj = G.adjugate()
        # e3* = G^{-1} e3 generates disc group when gcd(adj33, n)=1; q(e3*) = adj33/n
        if adj[2, 2] % n and jacobi_symbol(int(adj[2, 2]) % n, n) != jacobi_symbol(t*u-1, n): bad += 1
        n_ok += 1
print("chain checks (v,t,u<=12): failures", bad, "odd cases", n_ok)
# general K4 multigraphs, weights 0..W, prime tree number p = 1 mod 4: pairing class via a generator
W = int(sys.argv[1]) if len(sys.argv) > 1 else 4
from collections import Counter
cnt = Counter()
E = [(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]
for ws in itertools.product(range(W+1), repeat=6):
    G = lap(dict(zip(E, ws))); p = G.det()
    if p > 2 and isprime(p) and p % 4 == 1:
        adj = G.adjugate(); k = next(i for i in range(3) if adj[i, i] % p)
        cnt[jacobi_symbol(int(adj[k, k]) % p, p)] += 1
print("K4 multigraphs weights<=%d, prime tree number =1(4): pairing class counts" % W, dict(cnt))
