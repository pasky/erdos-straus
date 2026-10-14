"""y1_z3_gram (O209): test whether s*G_w is the Gram matrix of three integer vectors in Z^3, G_w the path Gram
[[v,-1,0],[-1,t,-1],[0,-1,u]] of a word w=(t,u,v) of X_n.  Claims tested:
 (P) n prime: s=n realizable  <=>  chi(w)=+1.
 (S) n=m^2 odd square: s=1 realizable for every word (path lattices of square det are index-m sublattices of Z^3).
 (C) composite n: s=n realizable <=> Diff(T_w)={2} (all odd eps_l=+1)  [exploratory].
Usage: PYTHONPATH=scripts uv run python scripts/y1_z3_gram.py NMAX"""
import sys
from math import isqrt
from cf_lib import jacobi, words


def vecs(N):
    out = []
    R = isqrt(N)
    for x in range(-R, R + 1):
        for y in range(-R, R + 1):
            r = N - x * x - y * y
            if r < 0:
                continue
            z = isqrt(r)
            if z * z == r:
                out.append((x, y, z))
                if z:
                    out.append((x, y, -z))
    return out


def dot(a, b):
    return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]


def realizable(s, t, u, v):
    # b fixed up to O(Z^3): take b in a fundamental set: 0 <= b0 <= b1 <= b2
    B = [b for b in vecs(s * t) if 0 <= b[0] <= b[1] <= b[2]]
    VA, VC = vecs(s * v), vecs(s * u)
    for b in B:
        As = [a for a in VA if dot(a, b) == -s]
        if not As:
            continue
        Cs = [c for c in VC if dot(c, b) == -s]
        for a in As:
            for c in Cs:
                if dot(a, c) == 0:
                    return True
    return False


def odd_eps_ok(A, n):
    m, l, ok = n, 3, True
    while l * l <= m:
        if m % l == 0:
            e = 0
            while m % l == 0:
                m //= l
                e += 1
            if e % 2 and jacobi(-A % l, l) == -1:
                ok = False
        l += 2
    if m > 1 and jacobi(-A % m, m) == -1:
        ok = False
    return ok


def isprime(n):
    return n > 1 and all(n % d for d in range(2, isqrt(n) + 1))


if __name__ == '__main__':
    N = int(sys.argv[1])
    stat = {'P': [0, 0], 'S': [0, 0], 'C': [0, 0]}
    for n in range(3, N + 1, 2):
        sq = isqrt(n) ** 2 == n
        for (t, u, v) in words(n):
            A = t * u - 1
            if isprime(n):
                ok = realizable(n, t, u, v) == (jacobi(-A % n, n) == 1)
                key = 'P'
            elif sq:
                ok = realizable(1, t, u, v)
                key = 'S'
            else:
                ok = realizable(n, t, u, v) == odd_eps_ok(A, n)
                key = 'C'
            stat[key][0] += 1
            if not ok:
                stat[key][1] += 1
                if stat[key][1] <= 5:
                    print('FAIL', key, n, (t, u, v))
    print('N =', N, {k: f'{a} words, {b} failures' for k, (a, b) in stat.items()})
