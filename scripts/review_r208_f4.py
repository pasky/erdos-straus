"""R208 from-scratch: strong contractibility (SVZ arXiv:2312.12953 §1, def before Thm 1.6) of closed walks in F_4.

F_4: vertices = primitive vectors of (Z/4)^2 modulo ±1, edges det = ±1 mod 4; triangular faces = mutually adjacent
triples (checked below to be exactly the images of Farey triangles {u, v, u±v}).
Moves: spur removal <v,u,v> -> <v>; triangle shortcut <u,v,w> -> <u,w> for mutually adjacent u,v,w.
Two readings: 'based' (moves at interior positions of the based closed walk) and 'cyclic' (any position).
Also: map each positive formal word's pentagon V1..V5 (LENGTH_THREE Prop 1.1) to F_4 and record spur <-> 4 | q_i.
"""
import sys
from functools import lru_cache
from itertools import product

n = 4
def norm(v):
    a, b = v[0] % n, v[1] % n
    w = ((-a) % n, (-b) % n)
    return min((a, b), w)

V = sorted({norm(v) for v in product(range(n), repeat=2) if (v[0] % 2 or v[1] % 2)})
idx = {v: i for i, v in enumerate(V)}
def det(u, v):
    return (u[0] * v[1] - u[1] * v[0]) % n
adj = [[det(V[i], V[j]) in (1, n - 1) for j in range(len(V))] for i in range(len(V))]
tri = {frozenset((i, j, k)) for i in range(6) for j in range(6) for k in range(6)
       if adj[i][j] and adj[j][k] and adj[i][k]}
farey = set()
for i in range(6):
    for j in range(6):
        if adj[i][j]:
            u, v = V[i], V[j]
            for sg in (1, -1):
                w = norm((u[0] + sg * v[0], u[1] + sg * v[1]))
                farey.add(frozenset((i, j, idx[w])))
print("F4: vertices", len(V), "edges", sum(map(sum, adj)) // 2, "triangles", len(tri), "Farey faces", len(farey),
      "equal", tri == farey)


@lru_cache(maxsize=None)
def sc(w, cyclic):
    """w: tuple v0..v_{L-1} (closed: v_L = v0). Returns True if reducible to a point."""
    L = len(w)
    if L == 0 or L == 1:
        return True  # length-1 loop impossible (no self-loops); L==0 is a point
    positions = range(L) if cyclic else range(1, L)
    for i in positions:
        a, b, c = w[(i - 1) % L], w[i], w[(i + 1) % L]
        if a == c and L >= 2:
            # remove w[i] and w[i+1] (spur a,b,a -> a)
            if cyclic:
                ww = tuple(w[j] for j in range(L) if j not in (i, (i + 1) % L))
            else:
                if i + 1 == L:  # w[L] = v0 = w[i-1]: path becomes v0..w[i-1](=v0)
                    ww = w[:i - 1]
                else:
                    ww = w[:i] + w[i + 2:]
            if sc(ww, cyclic):
                return True
        elif a != c and adj[a][c]:
            ww = tuple(w[j] for j in range(L) if j != i)
            if sc(ww, cyclic):
                return True
    return False


def walks(L):
    for start in range(6):
        def rec(path):
            if len(path) == L:
                if adj[path[-1]][path[0]]:
                    yield tuple(path)
                return
            for j in range(6):
                if adj[path[-1]][j]:
                    yield from rec(path + [j])
        yield from rec([start])


for L in range(3, 8):
    W = list(walks(L))
    print("L", L, "closed walks", len(W), "strongly contractible: based", sum(sc(w, False) for w in W),
          "cyclic", sum(sc(w, True) for w in W))

# word-level dictionary check
X = int(sys.argv[1]) if len(sys.argv) > 1 else 400
bad = 0; cnt = 0
for c in range(1, X + 3):
    for m in range(1, X + 3):
        for s in range(1, X + 3):
            N = m * c * s - c - s
            if N > X:
                break
            if N <= 0 or N % 2 == 0:
                continue
            h, hp = c * m - 1, m * s - 1
            Vs = [(0, -1), (1, 0), (c, 1), (h, m), (N, hp)]
            q = (hp, c, m, s, h)
            ids = [idx[norm(v)] for v in Vs]
            cnt += 1
            for i in range(5):
                a, b = ids[i - 1], ids[(i + 1) % 5]
                spur = a == b
                anti = (a != b) and not adj[a][b]
                if spur != (q[i] % 4 == 0) or anti != (q[i] % 4 == 2):
                    bad += 1
            assert all(adj[ids[i]][ids[(i + 1) % 5]] for i in range(5))
print("words N<=", X, cnt, "spur/antipode dictionary failures", bad)
