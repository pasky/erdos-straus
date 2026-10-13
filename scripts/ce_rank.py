"""Goal 3: rank the classes of G^-_p by invariants and locate the path (certificate) classes.
inv1 = min(L) (= least t with an endomorphism eps, eps^2 = -tp, in End(E,C): 'Frobenius distance');
inv2 = min of E^0 = adj(G) (least norm of a trace-zero element of the Eichler order)."""
import sys
from ce_classes import classes, aniso_at, gram_of, canon, short_vectors, det3
from cf_lib import words


def adj(G):
    (a, f, e), (_, b, d), (_, _, c) = G
    return [[b * c - d * d, e * d - f * c, f * d - e * b], [e * d - f * c, a * c - e * e, f * e - a * d],
            [f * d - e * b, f * e - a * d, a * b - f * f]]


def minvec(G):
    c = min(G[i][i] for i in range(3))
    return short_vectors(G, c)[0][0]


if __name__ == '__main__':
  for p in map(int, sys.argv[1:]):
      cl = classes(p)
      minus = [k for k in cl if aniso_at(gram_of(k), p)]
      paths = set(canon([[v, -1, 0], [-1, t, -1], [0, -1, u]]) for (t, u, v) in words(p))
      rows = []
      for k in minus:
          G = gram_of(k)
          rows.append((k[0], minvec(adj(G)), k in paths))
      r1 = sorted(rows, key=lambda r: (r[0], r[1]))
      r2 = sorted(rows, key=lambda r: (r[1], r[0]))
      first1 = next((i for i, r in enumerate(r1) if r[2]), None)
      first2 = next((i for i, r in enumerate(r2) if r[2]), None)
      npath = sum(r[2] for r in rows)
      print(p, '|G-|', len(minus), 'path classes', npath, 'rank of first path class by min(L):', first1,
            'by min(E0):', first2, ' minL of paths', sorted(r[0] for r in rows if r[2])[:6])
