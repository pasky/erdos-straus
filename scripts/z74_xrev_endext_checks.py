"""Cross-lab (Opus) review checks for the z72-z74 ENDEXT lane notes:
LOGIC_FOUR_SQUARE_AUDIT, LOGIC_LAG_END_MULTIPLE, LOGIC_LAGRANGE_END_TEST,
LOGIC_BCM_HULL_AND_ODD, LOGIC_ODD_COMPLETION_AUDIT, LOGIC_ODD_QUATERNION_LIFT.

All checks are small finite sanity checks of the algebraic identities and
algorithms the notes rely on, run over D = Z as a test base ring.
 A. -1 is not a sum of two squares in Q_2 (no primitive zero of x^2+y^2+z^2 mod 4/8).
 B. Both hyperbolic-pair recipes (LAG_END_MULTIPLE, LAGRANGE_END_TEST §1) over Z/l^k.
 C. Quaternion splittings over Z/m: explicit I,J (ODD_QUATERNION_LIFT) and the
    semilinear model w -> c w + d conj(w) (ODD_COMPLETION_AUDIT §1); det = Q4.
 D. SL2(D) -> SL2(D/m) lifting by the Bezout column procedure (D = Z).
 E. Unit-norm quaternion lift along a divisibility chain with *incompatible*
    splittings at each level (ODD_COMPLETION §1).
 F. Idempotent lift along the same chain under (L) (ODD_COMPLETION §2), and
    Q(e + a(1-e)) = a.
 G. Five-square identity a = ((a+1)/2)^2 + sum (h_i (a-1)/2)^2.
 H. Semilocal torsor trick c = w / conj(w), w = h + c conj(h) (ODD_COMPLETION §3).
 I. Norm repair by 1 + delta/2 along standard powers.
 J. Odd-quotient local step (BCM_HULL_AND_ODD): -1 = a^2+b^2 mod q from a
    nonzero four-square zero, via N(z/w) = -1.
 K. Sorted ES bounds (x<=3n/4, y<=2nx, z<=nxy) on all solutions, n<=60.
Run: ulimit -v 6000000; timeout 1800 uv run --offline --no-project python scripts/z74_xrev_endext_checks.py
"""
import itertools, math, random

random.seed(74)


def inv(a, m):
    return pow(a % m, -1, m)


def checkA():
    for k in (2, 3):
        M = 1 << k
        for x, y, z in itertools.product(range(M), repeat=3):
            if (x | y | z) & 1 and (x * x + y * y + z * z) % M == 0:
                raise AssertionError((k, x, y, z))
    # integral case: x^2+y^2 = -1 mod 4 impossible
    assert all((x * x + y * y + 1) % 4 for x in range(4) for y in range(4))
    return "x^2+y^2+z^2 has no primitive zero mod 4 or 8, so -1 is not x^2+y^2 in Q_2"


def Q(v, m):
    return sum(x * x for x in v) % m


def dot(u, v, m):
    return sum(a * b for a, b in zip(u, v)) % m


def isotropic_lift(l, k):
    """primitive isotropic vector of Q4 mod l^k from a four-square rep of l (Hensel)."""
    for v in itertools.product(range(int(math.isqrt(l)) + 1), repeat=4):
        if sum(x * x for x in v) == l:
            break
    M = l ** k
    v = list(v)
    j = next(i for i in range(4) if v[i] % l)
    for _ in range(k + 1):  # Newton on coordinate j
        f = Q(v, M)
        v[j] = (v[j] - f * inv(2 * v[j], M)) % M
    assert Q(v, M) == 0 and v[j] % l
    return v, j


def checkB():
    n = 0
    for l in (3, 5, 7, 11, 13, 29, 101):
        for k in (1, 2, 3):
            M = l ** k
            v, j = isotropic_lift(l, k)
            # recipe 1 (LAG_END_MULTIPLE): 2 v.w = 1, w' = w - Q(w) v ; Q(w' + a v) = a
            w = [0] * 4
            w[j] = inv(2 * v[j], M)
            wp = [(w[i] - Q(w, M) * v[i]) % M for i in range(4)]
            assert Q(wp, M) == 0 and (2 * dot(v, wp, M)) % M == 1
            # recipe 2 (LAGRANGE_END_TEST): u.b = 1, b' = b - (b.b) u / 2 ; Q(u + (a/2) b') = a
            b = [0] * 4
            b[j] = inv(v[j], M)
            bp = [(b[i] - Q(b, M) * v[i] * inv(2, M)) % M for i in range(4)]
            assert Q(bp, M) == 0 and dot(v, bp, M) == 1
            for _ in range(200):
                a = random.randrange(M)
                assert Q([(wp[i] + a * v[i]) % M for i in range(4)], M) == a
                h = a * inv(2, M) % M
                assert Q([(v[i] + h * bp[i]) % M for i in range(4)], M) == a
                n += 2
    return f"both hyperbolic recipes represent every residue ({n} trials, l^k up to 101^3)"


def mat_mul(A, B, m):
    return [[sum(A[i][t] * B[t][j] for t in range(2)) % m for j in range(2)] for i in range(2)]


def det(A, m):
    return (A[0][0] * A[1][1] - A[0][1] * A[1][0]) % m


def prime_powers(m):
    out, p = [], 2
    while m > 1:
        if m % p == 0:
            q = 1
            while m % p == 0:
                m //= p
                q *= p
            out.append(q)
        p += 1
    return out


def two_sq_minus1(m, rnd=False):
    """a^2+b^2 = -1 mod m, by brute force at each prime power and CRT (random choice if rnd)."""
    pe = prime_powers(m)
    parts = []
    for q in pe:
        sols = [(a, b) for a in range(q) for b in range(q) if (a * a + b * b + 1) % q == 0]
        assert sols, (m, q)
        parts.append(random.choice(sols) if rnd else sols[0])
    return (crt([x[0] for x in parts], pe), crt([x[1] for x in parts], pe))


def splitting(m, ab):
    a, b = ab
    I = [[0, m - 1], [1, 0]]
    J = [[a % m, b % m], [b % m, (-a) % m]]
    IJ = mat_mul(I, J, m)
    E = [[1, 0], [0, 1]]
    return E, I, J, IJ


def quat_to_mat(x, S, m):
    return [[sum(x[t] * S[t][i][j] for t in range(4)) % m for j in range(2)] for i in range(2)]


def solve4(S, Mtx, m):
    """coordinates of matrix Mtx in basis S over Z/m (brute-force free of division issues:
    use the explicit inverse since 1,I,J,IJ is a basis when 2 is a unit)."""
    # x0 + x1 I + x2 J + x3 IJ ; recover by traces: tr(X)=2x0, tr(X I^-1)..., use 2-invertibility
    i2 = inv(2, m)
    def tr(A):
        return (A[0][0] + A[1][1]) % m
    E, I, J, IJ = S
    # basis elements square to scalars 1,-1,-1,-1 and pairwise anticommute (except E)
    x0 = tr(Mtx) * i2 % m
    x1 = (-tr(mat_mul(Mtx, I, m))) * i2 % m
    x2 = (-tr(mat_mul(Mtx, J, m))) * i2 % m
    x3 = (-tr(mat_mul(Mtx, IJ, m))) * i2 % m
    return [x0, x1, x2, x3]


ODD_M = [5, 13, 25, 65, 9, 45, 117, 325, 221, 3 * 5 * 13]


def checkC():
    n = 0
    for m in ODD_M:
        S = splitting(m, two_sq_minus1(m, rnd=True))
        E, I, J, IJ = S
        neg = [[m - 1, 0], [0, m - 1]]
        assert mat_mul(I, I, m) == neg and mat_mul(J, J, m) == neg
        JI = mat_mul(J, I, m)
        assert all((IJ[i][j] + JI[i][j]) % m == 0 for i in range(2) for j in range(2))
        for _ in range(300):
            x = [random.randrange(m) for _ in range(4)]
            X = quat_to_mat(x, S, m)
            assert det(X, m) == Q(x, m)
            assert solve4(S, X, m) == x  # basis (span all of M2)
            n += 1
        # semilinear model on C = R[i] (basis 1,i): w -> c w + d conj(w)
        a, b = two_sq_minus1(m, rnd=True)  # b = a + b i with N(b) = a^2+b^2 = -1
        for _ in range(200):
            c = (random.randrange(m), random.randrange(m))
            d = (random.randrange(m), random.randrange(m))
            # matrix of w -> c w + d wbar in basis (1, i)
            def app(w):
                cw = ((c[0] * w[0] - c[1] * w[1]) % m, (c[0] * w[1] + c[1] * w[0]) % m)
                wb = (w[0], (-w[1]) % m)
                dw = ((d[0] * wb[0] - d[1] * wb[1]) % m, (d[0] * wb[1] + d[1] * wb[0]) % m)
                return ((cw[0] + dw[0]) % m, (cw[1] + dw[1]) % m)
            c1, ci = app((1, 0)), app((0, 1))
            A = [[c1[0], ci[0]], [c1[1], ci[1]]]
            Nc = (c[0] ** 2 + c[1] ** 2) % m
            Nd = (d[0] ** 2 + d[1] ** 2) % m
            assert det(A, m) == (Nc - Nd) % m
            n += 1
        # j: w -> bb * wbar squares to -1
        def jmap(w):
            wb = (w[0], (-w[1]) % m)
            return ((a * wb[0] - b * wb[1]) % m, (a * wb[1] + b * wb[0]) % m)
        for w in [(1, 0), (0, 1), (2, 3)]:
            jj = jmap(jmap(w))
            assert jj == ((-w[0]) % m, (-w[1]) % m)
    return f"splittings: I^2=J^2=-1, IJ=-JI, basis, det = Q4; semilinear det = N(c)-N(d) ({n} trials)"


def egcd(a, b):
    if b == 0:
        return (a, 1, 0) if a >= 0 else (-a, -1, 0)
    g, x, y = egcd(b, a % b)
    return g, y, x - (a // b) * y


def lift_sl2(Abar, m):
    """Lift Abar in SL2(Z/m) to SL2(Z) by the note's column procedure."""
    a, b = Abar[0][0] % m, Abar[1][0] % m  # first column lifts
    if a == 0 and b == 0:
        raise AssertionError("non-unimodular column")
    g, x, y = egcd(a, b)  # x a + y b = g
    ap, bp = a // g, b // g
    # gamma = [[x, y], [-bp, ap]] in SL2(Z), gamma (a,b)^T = (g,0)^T
    # replace (g,0) by (g,m) (unimodular since (g,m)=1), undo: gamma^-1 (g,m)
    assert math.gcd(g, m) == 1
    gi = [[ap, -y], [bp, x]]  # inverse of gamma
    u = gi[0][0] * g + gi[0][1] * m
    v = gi[1][0] * g + gi[1][1] * m
    gg, p, q = egcd(u, v)  # p u + q v = 1
    assert gg == 1
    L = [[u, -q], [v, p]]  # det = u p + v q = 1
    # correct second column mod m by a multiple of the first
    # want L[:,1] + lam * L[:,0] == Abar[:,1] mod m ; in basis of L: coeffs
    t0 = (Abar[0][1] - L[0][1]) % m
    t1 = (Abar[1][1] - L[1][1]) % m
    # solve [u v]^T lam = (t0,t1) using L^-1 = [[p, q], [-v, u]]
    lam = (p * t0 + q * t1) % m
    rest = (-v * t0 + u * t1) % m
    assert rest == 0, "discrepancy not a multiple of the first column"
    L = [[u, -q + lam * u], [v, p + lam * v]]
    assert L[0][0] * L[1][1] - L[0][1] * L[1][0] == 1
    assert all((L[i][j] - Abar[i][j]) % m == 0 for i in range(2) for j in range(2))
    return L


def rand_sl2(m):
    while True:
        a, b, c = (random.randrange(m) for _ in range(3))
        if math.gcd(a, m) == 1:
            d = (1 + b * c) * inv(a, m) % m
            A = [[a, b], [c, d]]
            # randomize via a unipotent to get non-unit corner sometimes
            U = [[1, 0], [random.randrange(m), 1]]
            A = mat_mul(U, A, m)
            assert det(A, m) == 1
            return A


def checkD():
    n = 0
    for m in ODD_M + [2, 4, 12, 360, 840, 1001]:
        for _ in range(300):
            lift_sl2(rand_sl2(m), m)
            n += 1
    return f"SL2(Z)->SL2(Z/m) lifting procedure succeeds ({n} random matrices)"


CHAIN = [5, 65, 65 * 9, 65 * 9 * 17, 65 * 9 * 17 * 25]


def red(A, m):
    return [[x % m for x in row] for row in A]


def checkE():
    """unit-norm lift along CHAIN with an independent random splitting at each level."""
    for trial in range(20):
        s_int = random.choice([-1, 2, 3, 7, -11]) if trial else -1
        q_prev, m_prev = None, None
        for m in CHAIN:
            if math.gcd(s_int, m) != 1:
                break
            S = splitting(m, two_sq_minus1(m, rnd=True))
            s = s_int % m
            if q_prev is None:
                q = solve4(S, [[s, 0], [0, 1]], m)
            else:
                Sbar = [red(X, m_prev) for X in S]
                Mbar = quat_to_mat(q_prev, Sbar, m_prev)  # old quaternion in reduced coords
                assert det(Mbar, m_prev) == s % m_prev
                T = mat_mul(Mbar, [[inv(s, m_prev), 0], [0, 1]], m_prev)
                L = red(lift_sl2(T, m_prev), m)
                Mn = mat_mul(L, [[s, 0], [0, 1]], m)
                q = solve4(S, Mn, m)
                assert [x % m_prev for x in q] == q_prev
            assert Q(q, m) == s
            q_prev, m_prev = q, m
    return f"unit-norm quaternions lift coherently along {CHAIN} with incompatible splittings"


def image_generator(P, m):
    """a vector generating the image of idempotent matrix P over Z/m (brute force)."""
    for x in itertools.product(range(m), repeat=2):
        v = (sum(P[0][j] * x[j] for j in range(2)) % m, sum(P[1][j] * x[j] for j in range(2)) % m)
        # generator iff its content is a unit (free rank one image)
        if math.gcd(math.gcd(v[0], v[1]), m) == 1:
            return v
    raise AssertionError("image not free")


def checkF():
    chain = CHAIN[:4]
    e_prev, m_prev = None, None
    for m in chain:
        S = splitting(m, two_sq_minus1(m, rnd=True))
        E11 = [[1, 0], [0, 0]]
        if e_prev is None:
            e = solve4(S, E11, m)
        else:
            Sbar = [red(X, m_prev) for X in S]
            P = quat_to_mat(e_prev, Sbar, m_prev)
            assert mat_mul(P, P, m_prev) == P
            Pc = [[(1 - P[0][0]) % m_prev, (-P[0][1]) % m_prev], [(-P[1][0]) % m_prev, (1 - P[1][1]) % m_prev]]
            v1, v2 = image_generator(P, m_prev), image_generator(Pc, m_prev)
            g = [[v1[0], v2[0]], [v1[1], v2[1]]]
            dg = det(g, m_prev)
            assert math.gcd(dg, m_prev) == 1
            di = inv(dg, m_prev)
            g = [[v1[0], v2[0] * di % m_prev], [v1[1], v2[1] * di % m_prev]]
            assert det(g, m_prev) == 1
            # check g E11 g^-1 = P
            gi = [[g[1][1], (-g[0][1]) % m_prev], [(-g[1][0]) % m_prev, g[0][0]]]
            assert mat_mul(mat_mul(g, E11, m_prev), gi, m_prev) == P
            G = red(lift_sl2(g, m_prev), m)
            Gi = [[G[1][1], (-G[0][1]) % m], [(-G[1][0]) % m, G[0][0]]]
            e = solve4(S, mat_mul(mat_mul(G, E11, m), Gi, m), m)
            assert [x % m_prev for x in e] == e_prev
        # Q(e + a(1-e)) = a for all a
        one = [1, 0, 0, 0]
        for a in random.sample(range(m), min(m, 300)):
            v = [(e[i] + a * (one[i] - e[i])) % m for i in range(4)]
            assert Q(v, m) == a
        e_prev, m_prev = e, m
    return f"idempotent lifts coherently along {chain}; Q(e+a(1-e))=a at every level"


def checkG():
    for m in ODD_M:
        h = two_sq_minus1(m)  # -1 = h0^2 + h1^2 (two of the four h_i, rest 0)
        i2 = inv(2, m)
        for a in range(m):
            p = (a + 1) * i2 % m
            r = (a - 1) * i2 % m
            assert (p * p + (h[0] * r) ** 2 + (h[1] * r) ** 2) % m == a
    return "five-square identity verified for every residue of each test modulus"


def gmul(x, y, m):
    return ((x[0] * y[0] - x[1] * y[1]) % m, (x[0] * y[1] + x[1] * y[0]) % m)


def gconj(x, m):
    return (x[0] % m, (-x[1]) % m)


def gnorm(x, m):
    return (x[0] * x[0] + x[1] * x[1]) % m


def gunit(x, m):
    return math.gcd(gnorm(x, m), m) == 1


def crt(rs, ms):
    x, M = 0, 1
    for r, mm in zip(rs, ms):
        t = ((r - x) * inv(M, mm)) % mm
        x, M = x + M * t, M * mm
    return x % M


def checkH():
    n = 0
    for m in [5, 13, 65, 9 * 5, 25 * 13, 3 * 7 * 5]:  # include 3, 7: field case for Z[i]
        fac = [p for p in range(2, m + 1) if m % p == 0 and all(p % d for d in range(2, p))]
        pe = [p ** max(k for k in range(1, 10) if m % p ** k == 0) for p in fac]
        T = [(a, b) for a in range(m) for b in range(m) if gnorm((a, b), m) == 1]
        for c in random.sample(T, min(len(T), 400)):
            # choose h prime-by-prime: 1 unless c = -1 mod p, then i
            hs = []
            for p in fac:
                hs.append((0, 1) if (c[0] + 1) % p == 0 and c[1] % p == 0 else (1, 0))
            h = (crt([x[0] for x in hs], pe), crt([x[1] for x in hs], pe))
            w = tuple((a + b) % m for a, b in zip(h, gmul(c, gconj(h, m), m)))
            assert gunit(w, m), (m, c, h, w)
            assert gmul(c, gconj(w, m), m) == w
            n += 1
    return f"semilocal torsor: w = h + c conj(h) is a unit with c conj(w) = w ({n} cases, incl. inert primes)"


def checkI():
    for m in (3, 5, 7, 13):
        for j in (1, 2, 3):
            M2 = m ** (2 * j)
            for _ in range(100):
                beta = (random.randrange(M2), random.randrange(M2))
                delta = (gnorm(beta, M2) + 1) % M2
                if delta % (m ** j):
                    # force norm = -1 + delta with delta in (m^j): rescale search
                    continue
                f = (1 + delta * inv(2, M2)) % M2
                nb = (beta[0] * f % M2, beta[1] * f % M2)
                assert gnorm(nb, M2) == M2 - 1
    # constructive version: start from a norm -1 element mod m^j and repair to m^(2j)
    for m in (5, 13, 3 * 0 + 9):
        a, b = two_sq_minus1(m)
        mod = m
        beta = (a, b)
        for _ in range(3):
            M2 = mod * mod
            delta = (gnorm(beta, M2) + 1) % M2
            assert delta % mod == 0
            f = (1 + delta * inv(2, M2)) % M2
            beta = (beta[0] * f % M2, beta[1] * f % M2)
            assert gnorm(beta, M2) == M2 - 1
            mod = M2
    return "1 + delta/2 repairs norm -1 from m^j to m^(2j)"


def checkJ():
    cnt = 0
    for q in range(3, 400, 2):
        if any(q % d == 0 for d in range(3, int(q ** 0.5) + 1, 2)):
            continue
        rep = next(v for v in itertools.product(range(int(math.isqrt(q)) + 1), repeat=4)
                   if sum(x * x for x in v) == q)
        z, w = (rep[0] % q, rep[1] % q), (rep[2] % q, rep[3] % q)
        assert (gnorm(z, q) + gnorm(w, q)) % q == 0 and (z != (0, 0) or w != (0, 0))
        if pow(q - 1, (q - 1) // 2, q) == 1:
            r = next(x for x in range(q) if (x * x + 1) % q == 0)
            ab = (r, 0)
        else:
            assert z != (0, 0) and w != (0, 0)
            wi = gconj(w, q)
            nw = inv(gnorm(w, q), q)
            zw = gmul(z, (wi[0] * nw % q, wi[1] * nw % q), q)
            ab = zw
        assert (gnorm(ab, q) + 1) % q == 0
        cnt += 1
    return f"-1 = a^2+b^2 mod q obtained from the four-square zero for all {cnt} odd primes q<400"


def checkK():
    cnt = 0
    for n in range(2, 61):
        for x in range(1, n + 1):
            for y in range(x, 2 * n * x + 1):
                num = n * x * y
                den = 4 * x * y - n * (x + y)
                if den > 0 and num % den == 0:
                    z = num // den
                    if z >= y:
                        assert 4 * x <= 3 * n and y <= 2 * n * x and z <= n * x * y
                        cnt += 1
    return f"sorted ES bounds hold on {cnt} solutions, n<=60"


if __name__ == "__main__":
    for f in (checkA, checkB, checkC, checkD, checkE, checkF, checkG, checkH, checkI, checkJ, checkK):
        print(f.__name__, "OK:", f())
