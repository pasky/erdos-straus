"""z9 (O233) library: canonical forms of positive ternary integer Grams, the supersingular 2-isogeny graph
modulo Frobenius on the lattice side (vertices = Gross forms of maximal orders of B_{p,inf}, stored as even
Hessian Grams of det 2p; edges = classes of G^-_p, classical det-p lattices anisotropic at p), path words and
their pointers.  Integer arithmetic for all lattice data; the short-vector / coset search windows in coset_min use floating-point bounds (with slack)."""
from math import isqrt, gcd
from itertools import product


def det3(G):
    return (G[0][0] * (G[1][1] * G[2][2] - G[1][2] ** 2) - G[0][1] * (G[0][1] * G[2][2] - G[1][2] * G[0][2])
            + G[0][2] * (G[0][1] * G[1][2] - G[1][1] * G[0][2]))


def Q(G, x):
    return sum(G[i][j] * x[i] * x[j] for i in range(3) for j in range(3))


def B(G, x, y):
    return sum(G[i][j] * x[i] * y[j] for i in range(3) for j in range(3))


def gram_of(G, vs):
    return tuple(tuple(B(G, a, b) for b in vs) for a in vs)


def cross(a, b):
    return (a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0])


def dot(a, b):
    return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]


def lin(cs, vs):
    return tuple(sum(c * v[i] for c, v in zip(cs, vs)) for i in range(3))


def greedy_reduce(G):
    """Return basis (rows, in original coords) of a greedily reduced basis (pairwise Gauss + sort, iterate)."""
    bas = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
    changed = True
    while changed:
        changed = False
        bas.sort(key=lambda x: Q(G, x))
        for i in range(3):
            for j in range(3):
                if i == j:
                    continue
                qi = Q(G, bas[i])
                bij = B(G, bas[i], bas[j])
                # reduce bas[j] by bas[i]
                r = round(bij / qi) if qi else 0
                if r and Q(G, bas[i]) <= Q(G, bas[j]):
                    nb = tuple(bas[j][k] - r * bas[i][k] for k in range(3))
                    if Q(G, nb) < Q(G, bas[j]):
                        bas[j] = nb
                        changed = True
        # try x3 +- x1 +- x2 style
        for e1, e2 in product((-1, 0, 1), repeat=2):
            nb = tuple(bas[2][k] + e1 * bas[0][k] + e2 * bas[1][k] for k in range(3))
            if Q(G, nb) < Q(G, bas[2]):
                bas[2] = nb
                changed = True
    bas.sort(key=lambda x: Q(G, x))
    return bas


def vectors_upto(G, bound):
    """All nonzero x (up to sign: first nonzero coord > 0) with Q(x) <= bound, via reduced basis and box."""
    bas = greedy_reduce(G)
    Gr = gram_of(G, bas)
    d = det3(Gr)
    adj = [Gr[1][1] * Gr[2][2] - Gr[1][2] ** 2, Gr[0][0] * Gr[2][2] - Gr[0][2] ** 2, Gr[0][0] * Gr[1][1] - Gr[0][1] ** 2]
    R = [isqrt(bound * adj[i] // d) + 1 for i in range(3)]
    out = []
    for c in product(*[range(-r, r + 1) for r in R]):
        if not any(c):
            continue
        fnz = next(x for x in c if x)
        if fnz < 0:
            continue
        q = Q(Gr, c)
        if q <= bound:
            out.append((q, lin(c, bas)))
    out.sort()
    return out


def coset_min(G, x1, x2, b):
    """Minimal-norm vectors in b + Z x1 + Z x2 (list), and the min."""
    g11, g12, g22 = B(G, x1, x1), B(G, x1, x2), B(G, x2, x2)
    h1, h2 = B(G, b, x1), B(G, b, x2)
    D = g11 * g22 - g12 * g12
    # real minimiser of Q(b + a x1 + c x2)
    a0 = (-h1 * g22 + h2 * g12) / D
    c0 = (-h2 * g11 + h1 * g12) / D
    best = None
    cand = []
    ra, rc = round(a0), round(c0)
    q0 = Q(G, lin((1, ra, rc), (b, x1, x2)))
    qb0 = Q(G, b) - (h1 * h1 * g22 - 2 * h1 * h2 * g12 + h2 * h2 * g11) / D  # real min
    slack = q0 - qb0
    Ra = isqrt(int(slack * g22 / D) + 1) + 1
    Rc = isqrt(int(slack * g11 / D) + 1) + 1
    for a in range(int(a0) - Ra - 1, int(a0) + Ra + 2):
        for c in range(int(c0) - Rc - 1, int(c0) + Rc + 2):
            y = lin((1, a, c), (b, x1, x2))
            q = Q(G, y)
            if best is None or q < best:
                best, cand = q, [y]
            elif q == best:
                cand.append(y)
    return best, cand


def canon(G):
    """Complete isometry invariant of a positive ternary integer Gram: lexmin Gram (Q1,Q2,Q3,B12,B13,B23) over the
    intrinsic set of bases (x1,x2,x3) with Q(x1)=lam1, Q(x2)=lam2, <x1,x2> primitive, x3 of minimal norm among
    vectors completing (x1,x2) to a basis (overall minimal), all sign changes."""
    bas = greedy_reduce(G)
    q2 = Q(G, bas[1])
    vs = vectors_upto(G, q2)
    lam1 = vs[0][0]
    S1 = [x for q, x in vs if q == lam1]
    # lam2: min norm of a vector independent of some x1 in S1 (= second successive minimum)
    lam2 = None
    for q, y in vs:
        if any(any(cross(x, y)) for x in S1):
            lam2 = q
            break
    S2 = [y for q, y in vs if q == lam2]
    pairs = []
    for x1 in S1:
        for x2 in S2:
            cr = cross(x1, x2)
            if not any(cr):
                continue
            g = gcd(gcd(abs(cr[0]), abs(cr[1])), abs(cr[2]))
            if g != 1:
                continue
            pairs.append((x1, x2, cr))
    trip = []
    lam3 = None
    for x1, x2, cr in pairs:
        # b with dot(cr, b) = 1 (cr primitive)
        b = solve_dot1(cr)
        m, cand = coset_min(G, x1, x2, b)
        if lam3 is None or m < lam3:
            lam3, trip = m, [(x1, x2, y) for y in cand]
        elif m == lam3:
            trip += [(x1, x2, y) for y in cand]
    best = None
    for x1, x2, x3 in trip:
        g = gram_of(G, (x1, x2, x3))
        for s2, s3 in product((1, -1), repeat=2):
            key = (g[0][0], g[1][1], g[2][2], s2 * g[0][1], s3 * g[0][2], s2 * s3 * g[1][2])
            if best is None or key < best:
                best = key
    return best


def key_to_gram(k):
    a, b, c, f, e, d = k
    return ((a, f, e), (f, b, d), (e, d, c))


def solve_dot1(c):
    """Integer vector b with c.b = 1, c primitive."""
    # extended gcd chain
    def eg(a, b):
        if b == 0:
            return (a, 1, 0) if a >= 0 else (-a, -1, 0)
        g, x, y = eg(b, a % b)
        return g, y, x - (a // b) * y
    g1, x1, y1 = eg(c[0], c[1])
    g2, x2, y2 = eg(g1, c[2])
    assert g2 == 1
    return (x2 * x1, x2 * y1, y2)


# ---------- words ----------
def words(p):
    """All (t,u,v) >= 1 with t u v - u - v = p."""
    out = []
    for t in range(1, p + 3):
        N = t * p + 1
        A = t - 1 if t > 1 else 1
        # A = t u - 1 >= t - 1; enumerate A = -1 mod t up to sqrt(N), take both orders
        if t == 1:
            A = 1
            step = 1
        else:
            A = t - 1
            step = t
        r = isqrt(N)
        while A <= r:
            if A > 0 and N % A == 0:
                As = N // A
                if (As + 1) % t == 0:
                    u, v = (A + 1) // t, (As + 1) // t
                    if u >= 1 and v >= 1:
                        out.append((t, u, v))
                        if u != v:
                            out.append((t, v, u))
            A += step
    return out


def path_gram(w):
    t, u, v = w
    return ((v, -1, 0), (-1, t, -1), (0, -1, u))


def jacobi(a, n):
    a %= n
    r = 1
    while a:
        while a % 2 == 0:
            a //= 2
            if n % 8 in (3, 5):
                r = -r
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3:
            r = -r
        a %= n
    return r if n == 1 else 0


def chi(w, p):
    t, u, v = w
    return jacobi(-(t * u - 1), p)


# ---------- edges <-> vertices ----------
def iso_classes_mod4(G):
    """Classes x mod 2 (nonzero) with Q(x) = 0 mod 4 for classical odd-det G."""
    return [x for x in product((0, 1), repeat=3) if any(x) and Q(G, x) % 4 == 0]


def overlattice_hessian(G, x):
    """L + Z x/2 for x in L with Q(x) = 0 (4): returns Hessian Gram (= 2 * half Gram) of L+, integer even,
    det 2p.  Basis: complete x (primitive mod 2) ... use basis {x/2, b2, b3}."""
    # find unimodular basis with first vector x (x primitive since x mod 2 nonzero and entries in {0,1})
    cols = complete_basis(x)
    Gb = gram_of(G, cols)  # Gram in basis (x, b2, b3)
    # scale first vector by 1/2: half Gram H with H00 = Q(x)/4, H0i = B(x,bi)/2, Hij = Gij
    # Hessian = 2H : entries 2H -> integer
    a = Gb[0][0] // 2  # 2*Q(x)/4
    H = ((Gb[0][0] // 2, Gb[0][1], Gb[0][2]), (Gb[0][1], 2 * Gb[1][1], 2 * Gb[1][2]),
         (Gb[0][2], 2 * Gb[1][2], 2 * Gb[2][2]))
    return H


def complete_basis(x):
    """Unimodular basis with first vector x (x primitive)."""
    x = tuple(x)
    for b2 in product((-1, 0, 1), repeat=3):
        for b3 in product((-1, 0, 1), repeat=3):
            if abs(dot(cross(x, b2), b3)) == 1:
                return (x, b2, b3)
    raise ValueError


def sublattices_hessian(H):
    """Edges at a vertex: H even Hessian Gram (det 2p). Half Gram F = H/2.  Classical index-2 sublattices
    L (B = H/2 integral on L).  Returns list of classical Grams (det p) of the 3 sublattices."""
    out = []
    # functional phi mod 2 (nonzero); L = ker phi; need H(x,y) even for x,y in L
    for phi in product((0, 1), repeat=3):
        if not any(phi):
            continue
        # basis of ker phi mod 2 lifted to Z: L = {x : phi.x = 0 mod 2}
        basis = kernel_basis(phi)
        Hb = gram_of(H, basis)
        if all(Hb[i][j] % 2 == 0 for i in range(3) for j in range(3)):
            out.append(tuple(tuple(Hb[i][j] // 2 for j in range(3)) for i in range(3)))
    return out


def kernel_basis(phi):
    i = phi.index(1)
    basis = []
    e = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
    for j in range(3):
        if j == i:
            basis.append(tuple(2 * c for c in e[j]))
        elif phi[j] == 1:
            basis.append(tuple(e[j][k] + e[i][k] for k in range(3)))
        else:
            basis.append(e[j])
    return basis


def pentagon_vectors(w):
    """The five pentagon vectors of L_w (coords) with their entries: e1(v), e2(t), e3(u), f(A), f*(A*)."""
    t, u, v = w
    A, As = t * u - 1, t * v - 1
    return [((1, 0, 0), v), ((0, 1, 0), t), ((0, 0, 1), u), ((A, u, 1), A), ((1, v, As), As)]
