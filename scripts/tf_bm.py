"""O194 TES_FINITE §3: local invariants of the BL Brauer classes alpha_w (order 3) and alpha_{-1} (order 2) on
K-rational points of the TES surface 9/n = w/x + w^2/y + 2/z (K = Q(w)), and a search for an adelic INTEGRAL
point (x_i in O_v, x_i = 1 mod 2 at v = 2) orthogonal to Br U = Br K + <alpha_w, alpha_{-1}>  (BL Prop 2.6/Thm 1.7).

alpha_zeta(u) = (-u1/u3, -u2/u3)_zeta, u = (x/w, y/w^2, z/2).  Tame invariants from the tame symbol
(-1)^{v(a)v(b)} a^{v(b)} b^{-v(a)} mod P raised to (N P - 1)/m, read as zeta^j; the single wild place (lambda for
m = 3, (2) for m = 2) by Hilbert reciprocity (complex place: Br C = 0).  Own code (does not import tw_eis.py).
"""
import sys
import itertools
from fractions import Fraction
import tf_core as C

LAM = (1, -1)


def val(x, P):
    v = 0
    while True:
        q = C.div(x, P)
        if q is None:
            return v, x
        x, v = q, v + 1


class Res:
    """residue field O/P with power map; P a prime element (split, inert, lambda)."""
    def __init__(self, P):
        self.P = P
        self.q = C.norm(P)
        if P == LAM:
            self.kind, self.p = 'lam', 3
        elif P[1] == 0:
            self.kind, self.p = 'inert', abs(P[0])
        else:
            self.kind, self.p = 'split', self.q
            a, b = P
            self.r = (-a * pow(b, -1, self.p)) % self.p
            assert (self.r * self.r + self.r + 1) % self.p == 0

    def red(self, x):
        a, b = x
        if self.kind == 'lam':
            return (a + b) % 3
        if self.kind == 'split':
            return (a + b * self.r) % self.p
        return (a % self.p, b % self.p)

    def mul(self, s, t):
        if self.kind == 'inert':
            p = self.p
            u = C.mul(s, t)
            return (u[0] % p, u[1] % p)
        return s * t % self.p

    def pw(self, s, e):
        if self.kind != 'inert':
            return pow(s, e, self.p)
        r, base = (1, 0), s
        while e:
            if e & 1:
                r = self.mul(r, base)
            base = self.mul(base, base); e >>= 1
        return r

    def inv(self, s):
        return self.pw(s, self.q - 2)

    def log_root(self, s, m):
        """s in mu_m(residue field): return j with s = zeta^j, zeta = w (m = 3) or -1 (m = 2)."""
        one = self.red((1, 0)); z = self.red((0, 1) if m == 3 else (-1, 0))
        t = one
        for j in range(m):
            if t == s:
                return j
            t = self.mul(t, z)
        raise ValueError((s, m))


_RES = {}


def res(P):
    if P not in _RES:
        _RES[P] = Res(P)
    return _RES[P]


def tame(a, b, P, m):
    """a, b = (num, den) pairs of O-elements; local invariant in Z/m at the tame prime P."""
    R = res(P)
    va1, a1 = val(a[0], P); va2, a2 = val(a[1], P)
    vb1, b1 = val(b[0], P); vb2, b2 = val(b[1], P)
    va, vb = va1 - va2, vb1 - vb2
    s = R.red((1, 0)) if (va * vb) % 2 == 0 else R.red((-1, 0))
    au = R.mul(R.red(a1), R.inv(R.red(a2)))
    bu = R.mul(R.red(b1), R.inv(R.red(b2)))
    s = R.mul(s, R.pw(au, vb % (R.q - 1)))
    s = R.mul(s, R.pw(bu, (-va) % (R.q - 1)))
    return R.log_root(R.pw(s, (R.q - 1) // m), m)


def primes_of(*els):
    ps = set()
    for x in els:
        ps |= set(C.factor(x).keys())
    return ps


def point_from_xy(n, x, y):
    """z = 2/(9/n - w/x - w^2/y) as (num, den) in O; None if undefined."""
    # 9/n - w/x - w^2/y = (9xy - w n y - w^2 n x)/(n x y)
    num = C.sub(C.sub(C.mul(C.NINE, C.mul(x, y)), C.mul(C.W, C.mul(n, y))), C.mul(C.W2, C.mul(n, x)))
    if num == (0, 0):
        return None
    return (C.mul(C.TWO, C.mul(n, C.mul(x, y))), num)  # z = zn/zd


def invariants(n, x, y, z):
    """x, y in O; z = (zn, zd). Returns dict place -> (inv alpha_w in Z/3, inv alpha_{-1} in Z/2)."""
    zn, zd = z
    # a = -u1/u3 = -(x/w)/(z/2) = -2 x zd / (w zn) ; b = -2 y zd / (w^2 zn)
    a = (C.mul((-2, 0), C.mul(x, zd)), C.mul(C.W, zn))
    b = (C.mul((-2, 0), C.mul(y, zd)), C.mul(C.W2, zn))
    ps = primes_of(a[0], a[1], b[0], b[1]) | {(2, 0), LAM}
    out = {}
    for P in ps:
        i3 = None if P == LAM else tame(a, b, P, 3)
        i2 = None if P == (2, 0) else tame(a, b, P, 2)
        out[P] = [i3, i2]
    out[LAM][0] = (-sum(v[0] for P, v in out.items() if P != LAM)) % 3
    out[(2, 0)][1] = (-sum(v[1] for P, v in out.items() if P != (2, 0))) % 2
    return out


def bad_places(n, x, y, z):
    """places where the point is not in the integral model (x, y in O already): v(z) < 0, or at 2 not = 1 mod 2."""
    zn, zd = z
    bad = set()
    for P in primes_of(zd):
        if val(zd, P)[0] > val(zn, P)[0]:
            bad.add(P)
    # at 2: z must be a 2-unit = 1 mod 2  (x, y are chosen 2-primary)
    v2n, zn2 = val(zn, (2, 0)); v2d, zd2 = val(zd, (2, 0))
    if v2n != v2d or not C.two_primary(C.mul(zn2, C.conj(zd2))):
        bad.add((2, 0))
    return bad


def bm_search(n, R=150, verbose=True):
    """Find base point P0 (bad set T) and replacements good at each v in T so that the adelic integral point is
    orthogonal to alpha_w and alpha_{-1}.  Returns a certificate list or None."""
    els = [x for x in C.disk(R) if C.two_primary(x)]
    pts = []
    for x in els:
        for y in els:
            z = point_from_xy(n, x, y)
            if z is None:
                continue
            pts.append((x, y, z, bad_places(n, x, y, z)))
    pts.sort(key=lambda t: len(t[3]))
    good_vals = {}  # place -> {(i3, i2): witness point}

    def local(P, pt):
        x, y, z, _ = pt
        inv = invariants(n, x, y, z)
        return tuple(inv[P]) if P in inv else (0, 0)

    def achievable(P):
        if P not in good_vals:
            d = {}
            for pt in pts:
                if P not in pt[3]:
                    v = local(P, pt)
                    if v not in d:
                        d[v] = pt
                    if len(d) == 6:
                        break
            good_vals[P] = d
        return good_vals[P]

    for pt in pts:
        T = sorted(pt[3])
        if len(T) > 2:
            break
        base = [local(P, pt) for P in T]
        opts = [list(achievable(P).items()) for P in T]
        for choice in itertools.product(*opts):
            d3 = sum(c[0][0] - b[0] for c, b in zip(choice, base)) % 3
            d2 = sum(c[0][1] - b[1] for c, b in zip(choice, base)) % 2
            if d3 == 0 and d2 == 0:
                cert = (pt[:3], [(P, c[1][:3], c[0], b) for P, c, b in zip(T, choice, base)])
                if verbose:
                    print("base point x, y, z =", pt[:3], " bad set T =", T)
                    for P, w, newv, oldv in cert[1]:
                        print(f"   at {P}: replace (inv_w, inv_-1) {oldv} by {newv} from point {w}")
                return cert
    if verbose:
        print("no certificate found; achievable local sets:", {P: sorted(d) for P, d in good_vals.items()})
    return None


if __name__ == '__main__':
    args = list(map(int, sys.argv[1:]))
    for a, b in zip(args[::2], args[1::2]):
        print(f"== n = {a}+{b}w, N = {C.norm((a, b))}")
        bm_search((a, b))
