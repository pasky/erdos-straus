"""y2_f4_walks: Farey-complex (Short–Van Son–Zabolotskii) reading of the ES sign.

For a word (b_1..b_r) (HJ / negative continued fraction, letters >= 1) with N = K(b) > 0, build the Farey path
V_1=(0,-1), V_2=(1,0), V_{i+1} = b_{i-1} V_i - V_{i-1}, ending at V_{r+2} = (N, A).  Reduce mod n (vertices of
F_n = unimodular pairs mod n up to +-1).  If det(V_{r+2}, V_1) = -N is a unit +-1 mod n, the path closes to a
closed walk of length r+2 in F_n.  Test SVZ "strong contractibility" (spur removal + triangle shortcut, cyclic)
and compare with the Jacobi symbol (A/N).

usage: y2_f4_walks.py NMAX RMAX [n=4]
"""
import sys
from functools import lru_cache
from math import gcd

n_mod = 4


def canon(v):
    a, b = v[0] % n_mod, v[1] % n_mod
    m = ((-a) % n_mod, (-b) % n_mod)
    return min((a, b), m)


def det(u, v):
    return (u[0] * v[1] - u[1] * v[0]) % n_mod


def adj(u, v):
    return det(u, v) in (1, n_mod - 1) and u != v


def rot_canon(w):
    k = len(w)
    if k == 0:
        return ()
    rs = [w[i:] + w[:i] for i in range(k)]
    rs += [tuple(reversed(x)) for x in rs]
    return min(rs)


@lru_cache(maxsize=None)
def strongly_contractible(w):
    k = len(w)
    if k <= 1:
        return True
    if k == 2:  # u,v,u : a spur pair
        return True
    for i in range(k):
        a, b, c = w[i - 1], w[i], w[(i + 1) % k]
        if a == c:  # spur <a,b,a> -> <a>
            nw = [w[j] for j in range(k) if j != i and j != (i + 1) % k]
            # remove b and the second a (keep one a)
            if strongly_contractible(rot_canon(tuple(nw))):
                return True
        elif adj(a, c):  # triangle a,b,c -> a,c
            nw = tuple(w[j] for j in range(k) if j != i)
            if strongly_contractible(rot_canon(nw)):
                return True
    return False


def jacobi(a, n):
    a %= n
    res = 1
    while a:
        while a % 2 == 0:
            a //= 2
            if n % 8 in (3, 5):
                res = -res
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3:
            res = -res
        a %= n
    return res if n == 1 else 0


def words(nmax, rmax):
    """all words with letters >=1 and 0 < K <= nmax, length 1..rmax, via DFS on (K_prev, K_cur)."""
    # path vectors: track (V_prev, V_cur); N = first coord of V_cur
    out = []

    def rec(prev, cur, word):
        if len(word) >= 1 and cur[0] > 0:
            out.append((tuple(word), cur))
        if len(word) == rmax:
            return
        b = 1
        while True:  # cur[0] > 0 always (positive prefixes only)
            nxt = (b * cur[0] - prev[0], b * cur[1] - prev[1])
            if nxt[0] > nmax:
                break
            if nxt[0] > 0:
                rec(cur, nxt, word + [b])
            b += 1
    # start: V1=(0,-1), V2=(1,0); first letter b1 gives V3=(b1, 1)
    for b1 in range(1, nmax + 1):
        rec((1, 0), (b1, 1), [b1])
    return out


if __name__ == "__main__":
    nmax = int(sys.argv[1]); rmax = int(sys.argv[2])
    if len(sys.argv) > 3:
        n_mod = int(sys.argv[3])
    V1 = (0, -1); V2 = (1, 0)
    stats = {}
    bad = 0
    for word, last in words(nmax, rmax):
        N, A = last
        if gcd(N, 2) != 1 or N < 3:
            continue
        # rebuild path
        path = [V1, V2]
        for b in word:
            p, c = path[-2], path[-1]
            path.append((b * c[0] - p[0], b * c[1] - p[1]))
        assert path[-1] == last
        w = rot_canon(tuple(canon(v) for v in path))
        sc = strongly_contractible(w)
        J = jacobi(A % N, N)
        key = (len(word), N % 4, sc, J)
        stats[key] = stats.get(key, 0) + 1
    for k in sorted(stats):
        print(k, stats[k])


def all_closed_walks(L):
    """enumerate all closed walks of length L on F_n (n = n_mod); return counts (total, strongly contractible)."""
    verts = sorted({canon((a, b)) for a in range(n_mod) for b in range(n_mod) if gcd(gcd(a, b), n_mod) == 1})
    tot = sc = 0

    def rec(w):
        nonlocal tot, sc
        if len(w) == L:
            if adj(w[-1], w[0]):
                tot += 1
                sc += strongly_contractible(rot_canon(tuple(w)))
            return
        for v in verts:
            if adj(w[-1], v):
                rec(w + [v])
    for v in verts:
        rec([v])
    return len(verts), tot, sc
