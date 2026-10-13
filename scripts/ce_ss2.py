"""Points (E, C) of X_0(2) at supersingular E over F_{p^2} (p = 1 mod 12, so j != 0, 1728), with the Atkin-Lehner w_2
(Velu) and Frobenius; count orbits of <Frob, w_2> = isomorphism classes of Eichler orders of level 2 in B_{p,inf}
(Deuring), to compare with the class number of the ternary genus G^-_p (Thm 2.1)."""
import sys
from ce_ss import F2, is_ss_Fp, phi2


def inv(F, x):
    p = F.p
    nrm = (x[0] * x[0] - F.nr * x[1] * x[1]) % p
    ni = pow(nrm, -1, p)
    return ((x[0] * ni) % p, (-x[1] * ni) % p)


def canon_AB(F, j):
    k = F.mul(j, inv(F, F.add((1728 % F.p, 0), F.sc(-1, j))))
    return F.sc(3, k), F.sc(2, k)


def jinv(F, a, b):
    a3 = F.mul(F.mul(a, a), a)
    num = F.sc(4 * 1728, a3)
    den = F.add(F.sc(4, a3), F.sc(27, F.mul(b, b)))
    return F.mul(num, inv(F, den))


def run(p):
    F = F2(p)
    elems = [(a, b) for a in range(p) for b in range(p)]
    j0 = (next(j for j in range(1, p) if j != 1728 % p and is_ss_Fp(j, p)), 0)
    verts, todo = {j0}, [j0]
    while todo:
        j = todo.pop()
        for y in elems:
            if phi2(F, j, y) == (0, 0) and y not in verts:
                verts.add(y); todo.append(y)
    cub = {}
    for j in verts:
        A, B = canon_AB(F, j)
        roots = [x for x in elems if F.add(F.add(F.mul(F.mul(x, x), x), F.mul(A, x)), B) == (0, 0)]
        assert len(roots) == 3, (j, roots)
        cub[j] = (A, B, roots)
    pts = [(j, x) for j in verts for x in cub[j][2]]
    def w2(P):
        j, x0 = P
        A, B, roots = cub[j]
        t = F.add(F.sc(3, F.mul(x0, x0)), A)
        w = F.mul(x0, t)
        a2, b2 = F.add(A, F.sc(-5, t)), F.add(B, F.sc(-7, w))
        x1 = next(r for r in roots if r != x0)
        xi = F.add(x1, F.mul(t, inv(F, F.add(x1, F.sc(-1, x0)))))
        j2 = jinv(F, a2, b2)
        A2, B2, roots2 = cub[j2]
        mu2 = F.mul(F.mul(a2, B2), inv(F, F.mul(b2, A2)))
        xn = F.mul(mu2, xi)
        assert xn in roots2
        return (j2, xn)
    def frob(P):
        return (F.frob(P[0]), F.frob(P[1]))
    seen, orbits = set(), 0
    for P in pts:
        if P in seen:
            continue
        orbits += 1
        st = [P]
        while st:
            q = st.pop()
            if q in seen:
                continue
            seen.add(q)
            st += [frob(q), w2(q)]
    return len(verts), len(pts), orbits


if __name__ == '__main__':
    for p in map(int, sys.argv[1:]):
        print('p', p, '#ss, #X0(2)ss, orbits:', run(p))
