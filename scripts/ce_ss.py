"""Supersingular X_0(2) points over F_{p^2} modulo <Frobenius, w_2>, for comparison with the class number of G^-_p."""
import sys


def phi2_coeffs(j, p):
    # Phi_2(j, Y) as polynomial in Y: coefficients [c0, c1, c2, c3] (elements of F_{p^2} as pairs)
    return None


class F2:
    def __init__(self, p):
        self.p = p
        self.nr = next(a for a in range(2, p) if pow(a, (p - 1) // 2, p) == p - 1)

    def mul(self, x, y):
        p = self.p
        return ((x[0] * y[0] + self.nr * x[1] * y[1]) % p, (x[0] * y[1] + x[1] * y[0]) % p)

    def add(self, x, y):
        return ((x[0] + y[0]) % self.p, (x[1] + y[1]) % self.p)

    def sc(self, c, x):
        return ((c * x[0]) % self.p, (c * x[1]) % self.p)

    def frob(self, x):
        return (x[0], (-x[1]) % self.p)


def phi2(F, X, Y):
    m, a, s = F.mul, F.add, F.sc
    X2, Y2 = m(X, X), m(Y, Y)
    terms = [m(X2, X), m(Y2, Y), s(-1, m(X2, Y2)), s(1488, a(m(X2, Y), m(X, Y2))), s(-162000, a(X2, Y2)),
             s(40773375, m(X, Y)), s(8748000000, a(X, Y)), ((-157464000000000) % F.p, 0)]
    r = (0, 0)
    for tm in terms:
        r = a(r, tm)
    return r


def is_ss_Fp(j, p):
    if j in (0, 1728 % p):
        return None
    k = (j * pow((1728 - j) % p, -1, p)) % p
    A, B = (3 * k) % p, (2 * k) % p
    s = 0
    for x in range(p):
        r = (x * x * x + A * x + B) % p
        s += 0 if r == 0 else (1 if pow(r, (p - 1) // 2, p) == 1 else -1)
    return s == 0  # #E = p + 1 + s


def ss_x02(p):
    F = F2(p)
    j0 = next(j for j in range(1, p) if j != 1728 % p and is_ss_Fp(j, p))
    elems = [(a, b) for a in range(p) for b in range(p)]
    verts, edges, todo = {(j0, 0)}, [], [(j0, 0)]
    while todo:
        j = todo.pop()
        # roots of Phi2(j, Y) with multiplicity: brute force + multiplicity via finite differences is messy;
        # instead count roots and assume simple unless fewer than 3 found (then flag)
        roots = [y for y in elems if phi2(F, j, y) == (0, 0)]
        edges.append((j, roots))
        for y in roots:
            if y not in verts:
                verts.add(y)
                todo.append(y)
    return F, verts, edges


if __name__ == '__main__':
    p = int(sys.argv[1])
    F, verts, edges = ss_x02(p)
    pts = set()
    flag = 0
    for j, roots in edges:
        if len(roots) < 3:
            flag += 1
        for y in roots:
            pts.add((j, y))
    # orbits under frob and swap
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
            st += [(F.frob(q[0]), F.frob(q[1])), (q[1], q[0])]
    print('p', p, '#ss', len(verts), 'X0(2)ss pts(distinct)', len(pts), 'orbits', orbits, 'verts w/ repeated roots', flag)
