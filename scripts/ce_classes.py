"""Enumerate isometry classes of positive classical ternary lattices of det n (canonical forms) and split by
anisotropy at p (genus G^-: C0 in B_{p,inf}). Also detect path-shaped classes (words)."""
from itertools import product
from math import isqrt
from cf_lib import ternary_aniso, words, jacobi


def det3(G):
    (a, f, e), (_, b, d), (_, _, c) = G
    return a * (b * c - d * d) - f * (f * c - d * e) + e * (f * d - b * e)


def Qv(G, x):
    return sum(G[i][j] * x[i] * x[j] for i in range(3) for j in range(3))


def Bv(G, x, y):
    return sum(G[i][j] * x[i] * y[j] for i in range(3) for j in range(3))


def short_vectors(G, bound):
    # brute force box using a crude bound: |x_i| <= sqrt(bound * adj_ii / det)
    n = det3(G)
    adj = [[G[1][1] * G[2][2] - G[1][2] ** 2, 0, 0], [0, G[0][0] * G[2][2] - G[0][2] ** 2, 0],
           [0, 0, G[0][0] * G[1][1] - G[0][1] ** 2]]
    R = [isqrt(bound * adj[i][i] // n) + 1 for i in range(3)]
    out = []
    for x in product(*[range(-r, r + 1) for r in R]):
        if any(x):
            q = Qv(G, x)
            if q <= bound:
                out.append((q, x))
    out.sort()
    return out


def canon(G):
    """Canonical Gram: lexicographically minimal (Q1,Q2,Q3,B12,B13,B23) over bases."""
    c = max(G[i][i] for i in range(3))
    sv = short_vectors(G, c)
    best = None
    for i1, (q1, x1) in enumerate(sv):
        if best and q1 > best[0]:
            break
        for (q2, x2) in sv:
            if best and (q1, q2) > best[:2]:
                break
            if q2 < q1:
                continue
            cr = (x1[1] * x2[2] - x1[2] * x2[1], x1[2] * x2[0] - x1[0] * x2[2], x1[0] * x2[1] - x1[1] * x2[0])
            if not any(cr):
                continue
            for (q3, x3) in sv:
                if best and (q1, q2, q3) > best[:3]:
                    break
                if q3 < q2:
                    continue
                d = cr[0] * x3[0] + cr[1] * x3[1] + cr[2] * x3[2]
                if abs(d) != 1:
                    continue
                # sign normalisations of x2, x3: choose to minimise off-diagonal tuple
                b12, b13, b23 = Bv(G, x1, x2), Bv(G, x1, x3), Bv(G, x2, x3)
                for s2, s3 in product((1, -1), repeat=2):
                    key = (q1, q2, q3, s2 * b12, s3 * b13, s2 * s3 * b23)
                    if best is None or key < best:
                        best = key
    return best


def classes(n):
    seen = {}
    amax = int(round((2 * n) ** (1 / 3))) + 1
    for a in range(1, amax + 1):
        for b in range(a, 2 * n + 1):
            if a * b > 2 * n * 2:
                break
            for f in range(-(a // 2), a // 2 + 1):
                m = a * b - f * f
                if m <= 0:
                    continue
                for e in range(-(a // 2), a // 2 + 1):
                    for d in range(-(b // 2), b // 2 + 1):
                        # det = c*m - (a d^2 - 2 f d e + b e^2)
                        r = a * d * d - 2 * f * d * e + b * e * e
                        if (n + r) % m:
                            continue
                        c = (n + r) // m
                        if c < b:
                            continue
                        G = [[a, f, e], [f, b, d], [e, d, c]]
                        k = canon(G)
                        if k not in seen:
                            seen[k] = G
    return seen


def gram_of(k):
    q1, q2, q3, b12, b13, b23 = k
    return [[q1, b12, b13], [b12, q2, b23], [b13, b23, q3]]


def aniso_at(G, p):
    d1 = G[0][0]
    m2 = G[0][0] * G[1][1] - G[0][1] ** 2
    n = det3(G)
    return ternary_aniso([d1, d1 * m2, m2 * n], p)


if __name__ == '__main__':
    import sys
    p = int(sys.argv[1])
    cl = classes(p)
    minus = [k for k in cl if aniso_at(gram_of(k), p)]
    paths = {}
    for w in words(p):
        t, u, v = w
        k = canon([[v, -1, 0], [-1, t, -1], [0, -1, u]])
        paths.setdefault(k, []).append(w)
    print('p', p, 'classes', len(cl), 'G-', len(minus), 'G+', len(cl) - len(minus))
    for k in sorted(minus):
        print('  ', k, 'PATH' if k in paths else '', paths.get(k, ''))
