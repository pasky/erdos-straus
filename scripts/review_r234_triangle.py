"""R234 spot-check of z9_triangle_shapes: triangle (cyclic plumbing) classes [[a,e,e],[e,b,e],[e,e,c]], e = +-1, det p."""
import sys, math
from review_r234_lib import *

lo, hi = int(sys.argv[1]), int(sys.argv[2])
cnt = dict(primes=0, has_tri_neg=0, no_tri_at_all=[], tri_not_path_any=0, tri_neg_not_path=0, decoupled=[])
for p in primes_1mod4(lo, hi):
    cnt['primes'] += 1
    tri = {}
    for a in range(1, int(round(p ** (1 / 3))) + 4):
        for b in range(a, math.isqrt(p + 2 + 3 * (math.isqrt(p) + 6)) + 3):
            if a * b <= 1:
                continue
            for e in (1, -1):
                num = p + a + b - 2 * e
                if num % (a * b - 1):
                    continue
                c = num // (a * b - 1)
                if c < b:
                    continue
                G = [[a, e, e], [e, b, e], [e, e, c]]
                assert det3(G) == p
                tri[canon(G)] = aniso_at_p(G, p)
    paths = {canon(path_gram(w)) for w in words(p) if aniso_at_p(path_gram(w), p)}
    neg = {k for k, s in tri.items() if s}
    if not tri:
        cnt['no_tri_at_all'].append(p)
    cnt['has_tri_neg'] += bool(neg)
    cnt['tri_not_path_any'] += any(k not in paths for k in tri)
    cnt['tri_neg_not_path'] += any(k not in paths for k in neg)
    if neg and not (neg & paths):
        cnt['decoupled'].append(p)
print({k: (v if not isinstance(v, list) else (len(v), v[:8])) for k, v in cnt.items()})
