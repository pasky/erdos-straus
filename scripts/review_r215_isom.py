# R215 — from-scratch ℤ-isometry test of ternary path forms Q_w (Gram [[v,-1,0],[-1,t,-1],[0,-1,u]]) and search
# for pairs of words of the same prime n with isometric Q_w but different S_M membership.
# Isometry search: columns of U are short vectors of G1 with prescribed norms/inner products (box bound from G1^{-1}).
import sys, itertools
from fractions import Fraction as F
from math import isqrt

def gram(t, u, v): return [[v, -1, 0], [-1, t, -1], [0, -1, u]]
def det3(G):
    return (G[0][0]*(G[1][1]*G[2][2]-G[1][2]*G[2][1]) - G[0][1]*(G[1][0]*G[2][2]-G[1][2]*G[2][0])
            + G[0][2]*(G[1][0]*G[2][1]-G[1][1]*G[2][0]))
def inv_diag(G):
    D = det3(G)
    m = lambda i, j: G[i][j]
    c00 = m(1,1)*m(2,2)-m(1,2)*m(2,1); c11 = m(0,0)*m(2,2)-m(0,2)*m(2,0); c22 = m(0,0)*m(1,1)-m(0,1)*m(1,0)
    return [F(c00, D), F(c11, D), F(c22, D)]
def q(G, x, y): return sum(x[i]*G[i][j]*y[j] for i in range(3) for j in range(3))
def short(G, N):
    idg = inv_diag(G)
    B = [isqrt(int(N*idg[i])) + 1 for i in range(3)]
    out = {}
    for x in itertools.product(*[range(-b, b+1) for b in B]):
        n = q(G, x, x)
        if 0 < n <= N: out.setdefault(n, []).append(x)
    return out
def isometric(G1, G2):
    if det3(G1) != det3(G2): return None
    S = short(G1, max(G2[i][i] for i in range(3)))
    for x in S.get(G2[0][0], []):
        for y in S.get(G2[1][1], []):
            if q(G1, x, y) != G2[0][1]: continue
            for z in S.get(G2[2][2], []):
                if q(G1, x, z) != G2[0][2] or q(G1, y, z) != G2[1][2]: continue
                U = [[x[i], y[i], z[i]] for i in range(3)]
                if abs(det3(U)) == 1: return U
    return None
def words(n):
    out = []
    for t in range(1, n+2):
        for u in range(1, n+2):
            # t u v - u - v = n  ->  v (tu - 1) = n + u
            A = t*u - 1
            if A <= 0: continue
            if (n + u) % A: continue
            v = (n + u)//A
            if v >= 1: out.append((t, u, v))
    return out
def inS(M, w):
    t, u, v = w
    return any(x % M == 0 for x in (t*u-1, t*v-1, t, u, v))

if __name__ == "__main__":
    G1, G2 = gram(1, 2, 7), gram(2, 1, 6)
    U = isometric(G1, G2)
    print("n=5: (1,2,7) in S7:", inS(7, (1, 2, 7)), " (2,1,6) in S7:", inS(7, (2, 1, 6)), " isometry U =", U)
    if U:
        UT = [list(r) for r in zip(*U)]
        P = [[sum(UT[i][k]*G1[k][l]*U[l][j] for k in range(3) for l in range(3)) for j in range(3)] for i in range(3)]
        print("  U^T G1 U =", P, "== G2:", P == G2)
    NMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 40
    import sympy
    for M in (4, 5, 7, 8, 11):
        mixed = 0; ex = None
        for n in sympy.primerange(3, NMAX+1):
            W = words(n)
            assert all(t*u*v-u-v == n for t, u, v in W)
            # group by isometry (greedy representatives)
            reps = []
            for w in W:
                G = gram(*w)
                for r in reps:
                    if isometric(gram(*r[0]), G) is not None:
                        r.append(w); break
                else: reps.append([w])
            for r in reps:
                s = {inS(M, w) for w in r}
                if len(s) == 2:
                    mixed += 1
                    if ex is None: ex = (n, [w for w in r if inS(M, w)][0], [w for w in r if not inS(M, w)][0])
        print(f"M={M}: primes n<={NMAX}: mixed isometry classes {mixed}; first example {ex}")
