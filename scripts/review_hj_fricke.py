"""R174: from-scratch check of bsA_fricke_vieta F1 (and the gamma entries) and bsA_selling_sandpile D1/D2/D3 identities.
M(a) = [[a,-1],[1,0]].  For v,t,u in [2,12]: gamma = M(v)M(t)M(u) = [[n,-A*],[A,-t]]; Fricke cubic with boundary traces
(v,t,u,T), T = tr gamma; Selling conorms; G^{-1} diagonal entries A/n, A*/n; Smith form of G cyclic (gcd of 2x2 minors = 1)."""
import itertools
from math import gcd
def mul(X, Y): return [[X[0][0]*Y[0][0]+X[0][1]*Y[1][0], X[0][0]*Y[0][1]+X[0][1]*Y[1][1]],
                       [X[1][0]*Y[0][0]+X[1][1]*Y[1][0], X[1][0]*Y[0][1]+X[1][1]*Y[1][1]]]
M = lambda a: [[a, -1], [1, 0]]
tr = lambda X: X[0][0] + X[1][1]
bad = 0; cnt = 0
for v, t, u in itertools.product(range(2, 13), repeat=3):
    n = t*u*v - u - v; A = t*u - 1; As = t*v - 1
    g = mul(mul(M(v), M(t)), M(u)); cnt += 1
    if g != [[n, -As], [A, -t]]: bad += 1
    T = tr(g)
    if T != t*u*v - t - u - v: bad += 1
    x, y, z = tr(mul(M(v), M(t))), tr(mul(M(t), M(u))), tr(mul(M(v), M(u)))
    if (x, y, z) != (As - 1, A - 1, u*v - 2): bad += 1
    lhs = x*x + y*y + z*z + x*y*z
    rhs = (v*t + u*T)*x + (t*u + v*T)*y + (v*u + t*T)*z + 4 - v*v - t*t - u*u - T*T - v*t*u*T
    if lhs != rhs: bad += 1
    # Selling: Gram G, e0 = -(e1+e2+e3)
    G = [[v, -1, 0], [-1, t, -1], [0, -1, u]]
    e = [[1,0,0],[0,1,0],[0,0,1],[-1,-1,-1]]
    dot = lambda a, b: sum(a[i]*G[i][j]*b[j] for i in range(3) for j in range(3))
    conorm = {(i, j): -dot(e[i], e[j]) for i in range(4) for j in range(i+1, 4)}
    if conorm != {(0,1): 1, (1,2): 1, (0,2): 0, (0,3): v-1, (1,3): t-2, (2,3): u-1}: bad += 1
    # det = n, adjugate diagonal (1,1),(3,3) = A, A*; cyclic cokernel
    if (t*u - 1, t*v - 1) != (A, As): bad += 1
    minors = [G[r1][c1]*G[r2][c2] - G[r1][c2]*G[r2][c1] for r1, r2 in itertools.combinations(range(3), 2) for c1, c2 in itertools.combinations(range(3), 2)]
    g2 = 0
    for m_ in minors: g2 = gcd(g2, m_)
    if g2 != 1: bad += 1
print(cnt, "words v,t,u<=12;", bad, "failures (gamma, T, traces, Fricke cubic, Selling conorms, cyclic Smith form)")
