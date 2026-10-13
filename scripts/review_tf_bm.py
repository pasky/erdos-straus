"""R194 from-scratch verification of the TES Brauer-Manin certificates (TES_FINITE Thm 3.1).

Uses only review_tf_zomega (own Z[w] arithmetic). For a certificate (n, P0=(x,y), q, P1=(x,y,z)):
 1. z0 := 2 n x y / (9 x y - n (w y + w^2 x)) (so P0 lies on U), check the equation for P0 and P1;
 2. T(P0) = {q} exactly: x, y 2-primary; z0 integral at every prime except q, and z0 ≡ 1 mod 2 at (2);
 3. P1 is q-integral with x y z != 0;
 4. local invariants at q (tame, q ∤ 6) of alpha_zeta = (-u1/u3, -u2/u3)_zeta, u = (x/w, y/w^2, z/2),
    zeta = w (cubic) and zeta = -1 (quadratic), via the tame symbol
    (-1)^{v(a)v(b)} a^{v(b)} / b^{v(a)} mod q raised to (Nq - 1)/m, coincide for P0 and P1.
Convention-independent: only equality of the residue-symbol values at the same place is used.
"""
import sys
from review_tf_zomega import (mul, add, sub, conj, norm, divexact, is2primary, factor_O, W, W2, TWO, ONE)


def frac_reduce(num, den):
    return num, den


def val(x, P):
    v = 0
    while True:
        t = divexact(x, P)
        if t is None:
            return v, x
        x, v = t, v + 1


def vfrac(num, den, P):
    a, _ = val(num, P); b, _ = val(den, P)
    return a - b


def tes_eq(n, x, y, znum, zden):
    # 9 x y z = n (w y z + w^2 x z + 2 x y), with z = znum/zden: multiply by zden
    lhs = mul((9, 0), mul(mul(x, y), znum))
    rhs = mul(n, add(add(mul(W, mul(y, znum)), mul(W2, mul(x, znum))), mul(TWO, mul(mul(x, y), zden))))
    return lhs == rhs


def bad_places(x, y, znum, zden):
    """Primes where (x,y,z) is not in W_v. x, y in O assumed."""
    bad = set()
    _, fd = factor_O(zden)
    for P in fd:
        if vfrac(znum, zden, P) < 0:
            bad.add(P)
    two = (2, 0)
    if not (is2primary(x) and is2primary(y)):
        bad.add(two)
    if two not in bad:
        # z ≡ 1 mod 2 at (2): v_2(znum - zden) - v_2(zden) >= 1
        if vfrac(sub(znum, zden), zden, two) < 1:
            bad.add(two)
    return bad


class ResField:
    def __init__(self, q):
        self.q = q
        p = norm(q)
        self.p = p
        a, b = q
        assert b % p != 0  # split prime of prime norm
        self.r = (-a * pow(b, -1, p)) % p     # image of w: a + b r ≡ 0
        assert (self.r * self.r + self.r + 1) % p == 0

    def red(self, x):
        return (x[0] + x[1] * self.r) % self.p


def tame(numa, dena, numb, denb, F):
    """tame symbol of (a, b) at q, a = numa/dena, b = numb/denb, as element of F_p^*."""
    q = F.q
    va, na1 = val(numa, q); va2, da1 = val(dena, q)
    vb, nb1 = val(numb, q); vb2, db1 = val(denb, q)
    v_a = va - va2; v_b = vb - vb2
    ua = F.red(na1) * pow(F.red(da1), -1, F.p) % F.p     # unit part of a mod q
    ub = F.red(nb1) * pow(F.red(db1), -1, F.p) % F.p
    # (-1)^{v_a v_b} a^{v_b} / b^{v_a}: unit parts (the q-power parts cancel exactly in the tame symbol)
    t = pow(ua, v_b, F.p) * pow(ub, -v_a, F.p) % F.p
    if (v_a * v_b) % 2:
        t = (-t) % F.p
    return t


def invariants(x, y, znum, zden, F):
    """(cubic symbol, quadratic symbol) of the tame symbols of alpha_w, alpha_{-1} at q.
    u1 = x/w = x w^2, u2 = y/w^2 = y w, u3 = z/2.  a = -u1/u3 = -2 x w^2 zden / znum, b = -2 y w zden / znum."""
    na = mul((-2, 0), mul(mul(x, W2), zden)); da = znum
    nb = mul((-2, 0), mul(mul(y, W), zden)); db = znum
    t = tame(na, da, nb, db, F)
    p = F.p
    c3 = pow(t, (p - 1) // 3, p)
    c2 = pow(t, (p - 1) // 2, p)
    # express c3 as power of the image of w
    w = F.r
    j = [1, w, w * w % p].index(c3)
    k = 0 if c2 == 1 else 1
    assert c2 in (1, p - 1)
    return j, k


def certify(n, x0, y0, q, x1, y1, z1num, z1den, stated_z0=None):
    znum = mul(mul((2, 0), n), mul(x0, y0))
    zden = sub(mul((9, 0), mul(x0, y0)), mul(n, add(mul(W, y0), mul(W2, x0))))
    assert zden != (0, 0)
    if stated_z0 is not None:
        sn, sd = stated_z0
        assert mul(znum, sd) == mul(sn, zden), "stated z0 differs"
    assert tes_eq(n, x0, y0, znum, zden)
    T = bad_places(x0, y0, znum, zden)
    # identify q up to associates
    Tq = [P for P in T if divexact(P, q) is not None and norm(P) == norm(q)]
    assert len(T) == 1 and len(Tq) == 1, ("T(P0) =", T)
    assert tes_eq(n, x1, y1, z1num, z1den), "P1 not on U"
    assert z1num != (0, 0) and x1 != (0, 0) and y1 != (0, 0)
    assert vfrac(z1num, z1den, q) >= 0, "P1 not q-integral"
    F = ResField(q)
    i0 = invariants(x0, y0, znum, zden, F)
    i1 = invariants(x1, y1, z1num, z1den, F)
    T1 = bad_places(x1, y1, z1num, z1den)
    return T, i0, i1, sorted(norm(P) for P in T1)


CERTS = {
    # n: (x0, y0, q, x1, y1, z1num, z1den, stated z0)
    7: ((-1, 2), (-11, -12), (-9, -8), (431, -27), (-7, -14), (-7, -12), (182, -560), (-1042, 152), ((-406, -588), (54, 916))),
    103: ((11, 2), (-7, -14), (5, 4), (49, -33), (-7, -14), (-11, -12), (-2282, 896), (-858, 548), ((630, -672), (326, -428))),
    151: ((-9, -14), (-7, -14), (1, 0), (132, 13), (-7, -14), (-7, -12), (2534, 3472), (-1194, 136), ((-266, 56), (-238, -264))),
    211: ((-1, 14), (-7, -14), (-7, -8), (232, -5), (-7, -14), (-11, -12), (-1778, -4648), (-702, 680), ((-1050, -3024), (-454, 484))),
    26893: ((179, 36), (-7, -14), (-13, -6), (527, -121), (-7, -14), (-9, -6), (-13566, 22512), (134, 220), ((-7574, 40544), (242, 1296))),
}

if __name__ == "__main__":
    for N, c in CERTS.items():
        n, x0, y0, q, x1, y1, zn, zd, sz = c
        assert norm(n) == N and is2primary(n)
        T, i0, i1, T1 = certify(n, x0, y0, q, x1, y1, zn, zd, sz)
        ok = i0 == i1
        print(f"N={N}: T(P0)={sorted(T)} Nq={norm(q)}  (cubic exp, quad) P0={i0} P1={i1}  equal={ok}  bad norms of P1={T1}")
        assert ok
    print("all certificates verified")


def parse_author_log(path):
    """Read certificate DATA (only data) printed by the author's tf_bm.py and return CERTS-style dict."""
    import re, ast
    out = {}
    cur = None
    for line in open(path):
        m = re.match(r"== n = (-?\d+)\+(-?\d+)w, N = (\d+)", line.strip())
        if m:
            cur = [(int(m.group(1)), int(m.group(2))), int(m.group(3))]
            continue
        if line.startswith("base point"):
            pt = ast.literal_eval(line.split("=", 1)[1].split("bad set")[0].strip())
            cur.append(pt)
        elif "replace" in line:
            q = ast.literal_eval(line.split("at ", 1)[1].split(":")[0].strip())
            P1 = ast.literal_eval(line.split("from point", 1)[1].strip())
            n, N, P0 = cur
            out[N] = (n, P0[0], P0[1], q, P1[0], P1[1], P1[2][0], P1[2][1], P0[2])
    return out


if __name__ == "__main__" and len(sys.argv) > 1:
    C2 = parse_author_log(sys.argv[1])
    for N, c in sorted(C2.items()):
        n, x0, y0, q, x1, y1, zn, zd, sz = c
        assert norm(n) == N and is2primary(n)
        T, i0, i1, T1 = certify(n, x0, y0, q, x1, y1, zn, zd, sz)
        print(f"N={N}: Nq={norm(q)} P0={i0} P1={i1} equal={i0 == i1}")
        assert i0 == i1
    print(len(C2), "logged certificates verified")
