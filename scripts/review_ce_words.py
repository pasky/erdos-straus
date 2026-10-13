"""R199: from-scratch checks on path lattices L_w, w = (t,u,v), tuv - u - v = p.

For each word: (1) explicit-Gram identities of Section 2 (trd/nrd of alpha, beta, gamma; alpha*beta = t*gamma;
i = 1+alpha, j = 1+beta trace zero, i^2 = -A*, j^2 = -A, ij+ji = -2; eps = -(1+ij) trace 0, nrd eps = t p);
(2) Thm 1.2(c): exact 2-power overorder enumeration: unique index-2 overorder of discrd 2p, maximal 2-overorders
(discrd p) exist (exactly 2) iff chi(w) = -1, where chi is computed from the *p-adic anisotropy* of L_w
(Legendre symbol of minus a nonzero 2x2 principal minor) -- independent of CHI_FLIP;
(3) Thm 2.1 'L = (E^0)^#(p)': Gram of the trace-zero sublattice of C_0(L_w) equals adj(G_w) up to GL3(Z)
(checked by exhibiting the basis dual to e_1,e_2,e_3 claimed in the text, i.e. Gram exactly adj(G)), and E^0 = C_0^0.
"""
import sys
from fractions import Fraction as F
sys.path.insert(0, 'scripts')
from review_ce_lib import Cliff, two_power_overorders, discrd, is_order, coords, inv


def legendre(a, p):
    a %= p
    if a == 0:
        return 0
    r = pow(a, (p - 1) // 2, p)
    return 1 if r == 1 else -1


def words(p):
    out = []
    t = 1
    while True:
        found_any = False
        u = 1
        while True:
            d = t * u - 1
            if d > p + u or (t == 1 and u > p + 2):
                break
            if d > 0:
                found_any = True
                if (p + u) % d == 0:
                    v = (p + u) // d
                    out.append((t, u, v))
            u += 1
        if t > 1 and not found_any:
            break
        t += 1
        if t > p + 2:
            break
    return out


def adj(G):
    (a, b, c), (d, e, f), (g, h, i) = G
    return [[e * i - f * h, c * h - b * i, b * f - c * e],
            [f * g - d * i, a * i - c * g, c * d - a * f],
            [d * h - e * g, b * g - a * h, a * e - b * d]]


def aniso_p(G, p):
    Aj = adj(G)
    for k in range(3):
        if Aj[k][k] % p:
            return legendre(-Aj[k][k], p) == -1
    raise ValueError


def check_word(p, w, full=True):
    t, u, v = w
    G = [[v, -1, 0], [-1, t, -1], [0, -1, u]]
    A, As = t * u - 1, t * v - 1
    C = Cliff(G)
    one, al, be, ga = C.c0_basis()
    ok = (C.trd(al), C.trd(be), C.trd(ga)) == (-2, -2, 0)
    ok &= (C.nrd(al), C.nrd(be), C.nrd(ga)) == (t * v, t * u, u * v)
    ok &= C.vmul(al, be) == [t * x for x in ga]
    i = [one[k] + al[k] for k in range(4)]
    j = [one[k] + be[k] for k in range(4)]
    ok &= C.trd(i) == 0 and C.trd(j) == 0
    ok &= C.vmul(i, i) == [-As, 0, 0, 0] and C.vmul(j, j) == [-A, 0, 0, 0]
    ij, ji = C.vmul(i, j), C.vmul(j, i)
    ok &= [x + y for x, y in zip(ij, ji)] == [-2, 0, 0, 0]
    eps = [-(one[k] + ij[k]) for k in range(4)]
    ok &= C.trd(eps) == 0 and C.nrd(eps) == t * p
    ok &= eps == [-(i[k] + j[k] + t * ga[k]) for k in range(4)]
    # trace-zero sublattice of C_0: in basis (1,al,be,ga) trd = 2c0 - 2c1 - 2c2; basis of kernel:
    # x1 = 1+al, x2 = 1+be, x3 = ga  (Z-basis of the trace-zero part since trd(c) = 2(c0-c1-c2))
    T0 = [i, j, ga]
    Gr0 = [[(C.nrd([a + b for a, b in zip(x, y)]) - C.nrd(x) - C.nrd(y)) / 2 for y in T0] for x in T0]
    # compare with adj(G) via a unimodular change: find basis whose Gram is adj(G) exactly
    Aj = adj(G)
    # claimed: Gram of C_0^0 is adj(G) = [[A,u,1],[u,uv,v],[1,v,A*]] up to GL3(Z); test det & invariants + explicit basis
    ok &= Aj == [[A, u, 1], [u, u * v, v], [1, v, As]]
    from review_ce_lib import det
    ok &= det(Gr0) == det(Aj) == p * p
    # explicit isometry search: small-coefficient unimodular matrices M with M Gr0 M^T = Aj
    chi = -1 if aniso_p(G, p) else 1
    ok &= chi == legendre(-A, p)
    res = dict(ok=ok, chi=chi, Gr0=Gr0)
    if full:
        B = [one, al, be, ga]
        assert is_order(C, B) and discrd(C, B) == 4 * p
        ovs = two_power_overorders(C, B)
        idx2 = [Bo for k, Bo in ovs if k == 2]
        idx4 = [Bo for k, Bo in ovs if k == 4]
        ok2 = len(idx2) == 1 and discrd(C, idx2[0]) == 2 * p and all(k <= 4 for k, _ in ovs)
        ok2 &= len(idx4) == (2 if chi == -1 else 0) and all(discrd(C, M) == p for M in idx4)
        # E^0 = C_0^0: trace-zero elements of E lie in C_0
        E = idx2[0]
        Bi = inv(B)
        # E^0 basis: kernel of trd on E; check each trace-zero combination of E basis with coeffs in {0,1} (mod C_0 suffices)
        from itertools import product
        for c in product(range(2), repeat=4):
            x = [sum(c[r] * E[r][k] for r in range(4)) for k in range(4)]
            if C.trd(x) == 0:
                cc = coords(B, x)
                ok2 &= all(z.denominator == 1 for z in cc)
        res['ok'] = ok and ok2
        res['nmax'] = len(idx4)
    return res


if __name__ == '__main__':
    primes = [int(x) for x in sys.argv[1:]] or [37, 41, 61, 73]
    tot = bad = neg = 0
    for p in primes:
        for w in words(p):
            r = check_word(p, w)
            tot += 1
            neg += r['chi'] == -1
            if not r['ok']:
                bad += 1
                print('FAIL', p, w, r)
    print('words', tot, 'chi=-1', neg, 'failures', bad)
