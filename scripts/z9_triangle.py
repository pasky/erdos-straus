"""Cyclic (triangle) plumbing classes in G^-_p versus path classes.
Triangle Gram [[a,e3,e2],[e3,b,e1],[e2,e1,c]], e_i = +-1, det = abc + 2 e1e2e3 - a - b - c = p.
For each p: #triangle classes in G^-_p, #path classes, #triangle classes that are also path classes.
Usage: z9_triangle.py lo hi"""
import sys
from sympy import isprime
from z9_lib import canon, words, chi, path_gram, iso_classes_mod4


def triangles(p):
    out = set()
    for s in (1, -1):  # s = e1 e2 e3 ; WLOG e = (-1,-1,-1) (s=-1) or (1,1,1)... signs up to basis sign changes
        e = -1 if s == -1 else 1
        # abc - a - b - c + 2s = p, a <= b <= c
        a = 1
        while a * a * a <= p + 3 * a + 10:
            b = a
            while a * b * b <= p + 3 * b + 10:
                den = a * b - 1
                if den > 0:
                    num = p + a + b - 2 * s
                    if num % den == 0:
                        c = num // den
                        if c >= b:
                            G = ((a, e, e), (e, b, e), (e, e, c))
                            from z9_lib import det3
                            if det3(G) == p and G[0][0] * G[1][1] > 1:
                                out.add(G)
                b += 1
            a += 1
    return out


lo, hi = int(sys.argv[1]), int(sys.argv[2])
tot = [0, 0, 0, 0]
for p in range(lo, hi + 1):
    if not isprime(p) or p % 4 != 1:
        continue
    tri = set()
    for G in triangles(p):
        # positive definite check via leading minors
        if G[0][0] > 0 and G[0][0] * G[1][1] - 1 > 0 and iso_classes_mod4(G):
            tri.add(canon(G))
    path = {canon(path_gram(w)) for w in words(p) if chi(w, p) == -1}
    both = tri & path
    tot[0] += 1
    tot[1] += len(tri) > 0
    tot[2] += len(tri - path) > 0
    tot[3] += len(tri) > 0 and not both
    if len(sys.argv) > 3:
        print(p, len(tri), len(path), len(both))
print("primes", tot[0], "with chi=-1 triangle class", tot[1], "with a non-path triangle class", tot[2],
      "with triangle classes but none path", tot[3])
