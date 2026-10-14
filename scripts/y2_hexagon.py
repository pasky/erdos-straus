"""y2_hexagon: polygon size r+2 = 6 (HJ length 4) vs 5.

For odd N <= X: does some INTERIOR word (all letters >= 2) of HJ length r (r = 3 or 4) have a short diagonal
(quiddity lambda_{i-1,i+1}, i over all r+2 vertices) = 0 (mod 4)?  Each such vertex gives 4/N as r unit fractions
(vertex-fan identity).  Report failures, odd squares separately; and the mod-2 quiddity patterns (up to rotation and
reflection) with their sign statistics.
usage: y2_hexagon.py X r
"""
import sys
from collections import Counter, defaultdict
from math import isqrt


def jac(a, n):
    a %= n; res = 1
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


def det(u, v):
    return u[0] * v[1] - u[1] * v[0]


def gen(X, r):
    """interior words of length r with 0 < N <= X; yields (word, path)."""
    out = []

    def rec(path, word):
        if len(word) == r:
            out.append((tuple(word), list(path)))
            return
        p, c = path[-2], path[-1]
        b = 2
        while True:
            nxt = (b * c[0] - p[0], b * c[1] - p[1])
            # with letters >= 2 the first coordinates increase; final N >= nxt[0]
            if nxt[0] > X:
                break
            rec(path + [nxt], word + [b])
            b += 1
    rec([(0, -1), (1, 0)], [])
    return out


def canon_pattern(t):
    k = len(t)
    rs = [t[i:] + t[:i] for i in range(k)]
    rs += [tuple(reversed(x)) for x in rs]
    return min(rs)


def main(X, r):
    has = defaultdict(bool)
    pat = Counter()
    for word, path in gen(X, r):
        N, A = path[-1]
        if N % 2 == 0:
            continue
        n = len(path)
        q = [abs(det(path[i - 1], path[(i + 1) % n])) for i in range(n)]
        z = any(x % 4 == 0 for x in q)
        if z:
            has[N] = True
        P = canon_pattern(tuple(x % 2 for x in q))
        if N % 4 == 1:
            pat[(P, z, jac(A, N))] += 1
    sq_fail = [N for N in range(9, X + 1, 2) if isqrt(N) ** 2 == N and not has[N]]
    nsq_fail = [N for N in range(3, X + 1, 2) if isqrt(N) ** 2 != N and not has[N]]
    print(f"r={r}: odd N<= {X} without a zero-mod-4 interior word: non-squares {len(nsq_fail)} (largest {nsq_fail[-10:]});"
          f" odd squares {len(sq_fail)} (largest {sq_fail[-10:]})")
    print("N=1 mod 4 patterns (mod-2 quiddities up to D_n, has zero, Jacobi):")
    for k in sorted(pat):
        print("  ", k, pat[k])


if __name__ == "__main__":
    main(int(sys.argv[1]), int(sys.argv[2]))
