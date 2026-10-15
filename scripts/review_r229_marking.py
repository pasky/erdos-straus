# R229 from-scratch checks of z1_marking_isometry (Lemma 1, Prop 2, Prop 3) and z1_small_prime_pigeonhole.
# Own isometry canonical form for positive ternary lattices (lex-min Gram over greedy-minimal bases).
import sys, math
from itertools import product
from math import gcd
from collections import defaultdict

def words(n):
    out = []
    for t in range(1, n + 3):
        for u in range(1, n + 3):
            A = t * u - 1
            if A <= 0: continue
            if (n + u) % A == 0:
                v = (n + u) // A
                if v >= 1: out.append((t, u, v))
    return out

def gram(w):
    t, u, v = w
    return [[v, -1, 0], [-1, t, -1], [0, -1, u]]

def Q(G, x): return sum(G[i][j] * x[i] * x[j] for i in range(3) for j in range(3))
def B(G, x, y): return sum(G[i][j] * x[i] * y[j] for i in range(3) for j in range(3))

def short_vectors(G, bound):
    # all nonzero x with Q(x) <= bound (Fincke-Pohst via LDL^T over floats, then exact filter)
    import numpy as np
    M = np.array(G, dtype=float)
    L = np.linalg.cholesky(M)  # M = L L^T ; Q(x) = |L^T x|^2
    R = L.T  # upper triangular
    res = []
    def rec(i, x, partial):
        if i < 0:
            if any(x): 
                xx = tuple(x)
                if Q(G, xx) <= bound: res.append(xx)
            return
        # contribution of row i: (R[i,i] x_i + sum_{j>i} R[i,j] x_j)^2
        c = sum(R[i, j] * x[j] for j in range(i + 1, 3))
        rem = bound - partial + 1e-9
        if rem < 0: return
        r = math.sqrt(rem) / R[i, i]
        lo = math.ceil(-r - c / R[i, i] - 1e-9); hi = math.floor(r - c / R[i, i] + 1e-9)
        for xi in range(lo, hi + 1):
            x[i] = xi
            rec(i - 1, x, partial + (R[i, i] * xi + c) ** 2)
        x[i] = 0
    rec(2, [0, 0, 0], 0.0)
    return res

def det3(a, b, c):
    return (a[0] * (b[1] * c[2] - b[2] * c[1]) - a[1] * (b[0] * c[2] - b[2] * c[0]) + a[2] * (b[0] * c[1] - b[1] * c[0]))

def canon(G):
    # lex-min over bases (x,y,z) of (Qx,Qy,Qz,Bxy,Bxz,Byz) with Qx<=Qy<=Qz; minimal Gram is reached by vectors of
    # norm <= lambda_3 (successive-minima basis exists in dim 3); we search all vectors with norm <= max diag of a
    # basis achieving the successive minima, which is <= max(G_ii) bound -> use bound = max diag of G (safe superset).
    bound = max(G[i][i] for i in range(3))
    S = short_vectors(G, bound)
    S.sort(key=lambda x: Q(G, x))
    best = None
    # lex-min: Qx minimal first
    for x in S:
        qx = Q(G, x)
        if best and qx > best[0]: break
        for y in S:
            qy = Q(G, y)
            if qy < qx: continue
            if best and (qx, qy) > tuple(best[:2]): break
            for z in S:
                qz = Q(G, z)
                if qz < qy: continue
                if best and (qx, qy, qz) > tuple(best[:3]): break
                if abs(det3(x, y, z)) != 1: continue
                tup = (qx, qy, qz, B(G, x, y), B(G, x, z), B(G, y, z))
                if best is None or tup < best: best = tup
    return best

def P(w):
    t, u, v = w
    return (t, u, v, t * u - 1, t * v - 1)

def inS(w, M): return any(x % M == 0 for x in P(w))

if __name__ == "__main__":
    NMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 150
    # Lemma 1: norm-one triples isometric (via canon) -- n+1 = ab
    bad = 0; cnt = 0
    for n in range(1, NMAX, 2):
        for a in range(1, n + 2):
            if (n + 1) % a: continue
            b = (n + 1) // a
            ws = [(1, a + 1, b + 1), (a + 1, 1, b), (b + 1, 1, a)]
            assert all(t * u * v - u - v == n for t, u, v in ws)
            target = canon([[1, 0, 0], [0, b, -1], [0, -1, a]])
            cnt += 1
            if any(canon(gram(w)) != target for w in ws): bad += 1
    print("Lemma 1 norm-one triples:", cnt, "checked, failures", bad)
    # Prop 2 construction check for M <= 60
    badP2 = 0
    for M in range(2, 61):
        units = [x for x in range(M) if gcd(x, M) == 1 and x not in (1, M - 1)]
        if not units: continue
        x = units[0]; xinv = pow(x, -1, M)
        found = 0
        for a in range(1, 40 * M):
            if (a + 1) % M != x % M: continue
            if M % 2 == 1 and a % 2: continue
            b = xinv if xinv > 0 else M
            n = a * b - 1
            w1, w2 = (1, a + 1, b + 1), (a + 1, 1, b)
            if n % 2 == 0 or gcd(n, M) != 1 or inS(w1, M) or not inS(w2, M): badP2 += 1
            found += 1
            if found > 3: break
    print("Prop 2 construction, M<=60 with phi(M)>2: failures", badP2)
    # mixed isometry classes per M, n coprime to M, odd n < NMAX
    mixed = defaultdict(int); classes = 0; multi = 0; interior_bad = 0
    for n in range(3, NMAX, 2):
        cls = defaultdict(list)
        for w in words(n): cls[canon(gram(w))].append(w)
        classes += len(cls)
        for c, ws in cls.items():
            if len(ws) > 1: multi += 1
            inter = [w for w in ws if min(w) >= 2]
            if len({tuple(w) for w in inter} | {w[::-1] for w in inter}) > 2 and len(inter) > 1:
                # interior words up to reversal (t,u,v)->(t,v,u)
                reps = {min(w, (w[0], w[2], w[1])) for w in inter}
                if len(reps) > 1: interior_bad += 1
            for M in range(2, 31):
                if gcd(n, M) != 1: continue
                s = {inS(w, M) for w in ws}
                if len(s) > 1: mixed[M] += 1
    print(f"odd n<{NMAX}: {classes} path classes, multi-marked {multi}, interior non-unique {interior_bad}")
    print("M with mixed classes (n coprime to M):", dict(sorted(mixed.items())))
    print("M<=30 never mixed:", [M for M in range(2, 31) if mixed[M] == 0])
