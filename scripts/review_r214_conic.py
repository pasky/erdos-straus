"""R214 from-scratch check of TWO_FIBRES Prop A2 / y1_hurwitz_lift H4.

For p prime:
  (a) orbits of O(Z^3) (signed permutations, projectively S4) on the conic C(F_p): x^2+y^2+z^2 = 0;
  (b) isometry classes of the lattices L_l = ({x in Z^3 : x = lambda*l mod p}, |x|^2/p), one per orbit;
  (c) the full set of isometry classes of positive classical ternary lattices of det p isotropic at p
      (enumerated independently from Minkowski-type bounds abc <= 2 det, 2|f|<=a, ...).
Claims checked: every class in (c) is some L_l (onto), (b) subset of (c), and #orbits vs #classes.
Canonical form: lexicographically minimal Gram over all bases realising the successive minima (exact for rank 3).
"""
import itertools, math, sys
from fractions import Fraction
import numpy as np

def det3(G):
    return (G[0][0]*(G[1][1]*G[2][2]-G[1][2]*G[2][1]) - G[0][1]*(G[1][0]*G[2][2]-G[1][2]*G[2][0])
            + G[0][2]*(G[1][0]*G[2][1]-G[1][1]*G[2][0]))

def inv_diag(G):
    d = det3(G)
    c00 = G[1][1]*G[2][2]-G[1][2]**2
    c11 = G[0][0]*G[2][2]-G[0][2]**2
    c22 = G[0][0]*G[1][1]-G[0][1]**2
    return [Fraction(c00, d), Fraction(c11, d), Fraction(c22, d)]

def Q(G, x):
    return sum(G[i][j]*x[i]*x[j] for i in range(3) for j in range(3))

def short_vectors(G, N):
    """all nonzero x with Q(x) <= N (box from exact bound |x_i| <= sqrt(N * (G^-1)_ii))."""
    iv = inv_diag(G)
    B = [int(math.isqrt(int(N*iv[i]))) + 1 for i in range(3)]
    out = []
    for x in itertools.product(*[range(-b, b+1) for b in B]):
        if any(x):
            q = Q(G, x)
            if q <= N:
                out.append((q, x))
    out.sort()
    return out

def rank(vs):
    return np.linalg.matrix_rank(np.array(vs, dtype=float))

def canon(G):
    # successive minima: bound N = max diagonal works (diagonal vectors are independent)
    N = max(G[i][i] for i in range(3))
    sv = short_vectors(G, N)
    lam = []; chosen = []
    for q, x in sv:
        if rank(chosen + [x]) > len(chosen):
            chosen.append(x); lam.append(q)
            if len(chosen) == 3: break
    by = {q: [x for qq, x in sv if qq == q] for q in set(lam)}
    best = None
    for v1 in by[lam[0]]:
        for v2 in by[lam[1]]:
            for v3 in by[lam[2]]:
                M = [v1, v2, v3]
                d = round(np.linalg.det(np.array(M, dtype=float)))
                if abs(d) != 1: continue
                H = tuple(tuple(sum(G[a][b]*M[i][a]*M[j][b] for a in range(3) for b in range(3)) for j in range(3)) for i in range(3))
                key = (H[0][0], H[1][1], H[2][2], H[0][1], H[0][2], H[1][2])
                if best is None or key < best: best = key
    return best

def isotropic_at_p(G, p):
    r = np.arange(p)
    X, Y, Z = np.meshgrid(r, r, r, indexing='ij')
    q = (G[0][0]*X*X + G[1][1]*Y*Y + G[2][2]*Z*Z + 2*G[0][1]*X*Y + 2*G[0][2]*X*Z + 2*G[1][2]*Y*Z) % p
    return int((q == 0).sum()) > p

def genus_plus(p):
    seen = set()
    for a in range(1, 2*p+1):
        for b in range(a, 2*p//a + 1):
            for c in range(b, 2*p//(a*b) + 1):
                for f in range(-(a//2), a//2+1):
                    for e in range(-(a//2), a//2+1):
                        for d in range(-(b//2), b//2+1):
                            G = [[a, f, e], [f, b, d], [e, d, c]]
                            if det3(G) != p: continue
                            if a*b - f*f <= 0: continue
                            k = canon(G)
                            if k in seen: continue
                            seen.add(k)
    plus = {k for k in seen if isotropic_at_p(key2G(k), p)}
    return seen, plus

def key2G(k):
    a, b, c, f, e, d = k
    return [[a, f, e], [f, b, d], [e, d, c]]

def conic_orbits(p):
    pts = set()
    for x in range(p):
        for y in range(p):
            for z in range(p):
                if (x, y, z) == (0, 0, 0): continue
                if (x*x+y*y+z*z) % p: continue
                # normalise projectively: first nonzero coord = 1
                i = next(i for i, c in enumerate((x, y, z)) if c)
                inv = pow((x, y, z)[i], -1, p)
                pts.add(tuple((c*inv) % p for c in (x, y, z)))
    def norm(v):
        i = next(i for i, c in enumerate(v) if c % p)
        inv = pow(v[i], -1, p)
        return tuple((c*inv) % p for c in v)
    group = []
    for perm in itertools.permutations(range(3)):
        for sg in itertools.product((1, -1), repeat=3):
            group.append((perm, sg))
    orbits = []; left = set(pts)
    while left:
        v = left.pop(); orb = {v}
        for perm, sg in group:
            w = norm(tuple(sg[i]*v[perm[i]] for i in range(3)))
            orb.add(w)
        left -= orb; orbits.append(sorted(orb))
    return pts, orbits

def L_of(l, p):
    # M = pZ^3 + Z*l, l normalised so that its first nonzero coordinate is 1: basis {l} + p*e_j (j != that index)
    i0 = next(i for i, c in enumerate(l) if c)
    B = [list(l)] + [[p if k == j else 0 for k in range(3)] for j in range(3) if j != i0]
    G = [[sum(B[i][k]*B[j][k] for k in range(3)) for j in range(3)] for i in range(3)]
    assert all(G[i][j] % p == 0 for i in range(3) for j in range(3))
    G = [[G[i][j]//p for j in range(3)] for i in range(3)]
    assert det3(G) == p, det3(G)
    return G

if __name__ == '__main__':
    primes = [int(a) for a in sys.argv[1:]] or [5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    for p in primes:
        pts, orbits = conic_orbits(p)
        imgs = [canon(L_of(o[0], p)) for o in orbits]
        allc, plus = genus_plus(p)
        img = set(imgs)
        print(f"p={p} conic pts={len(pts)} orbits={len(orbits)} orbit sizes={sorted(len(o) for o in orbits)} "
              f"image classes={len(img)} genus+ classes={len(plus)} (all det-p classes={len(allc)}) "
              f"image==genus+: {img == plus}", flush=True)
