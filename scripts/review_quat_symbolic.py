"""R130: symbolic checks with an explicit quaternion multiplication (own implementation).
Algebra (alpha,beta): basis 1,i,j,k, i^2=alpha, j^2=beta, k=ij=-ji.
1. Lemma 1.2: realise u, v (u^2=-d, v^2=-m, uv+vu=1) inside (-d, -d(4dm-1)) as u=i, v=(j-u)/(2d);
   check relations, Gram det of trd(x_i x_j) on (1,u,v,uv), closure (vu = 1-uv).
2. Lemma 3.1: (2a i + j)(2b i - j) = -(4abd-p) - 2(a+b)k in (-d,-p); norms.
3. §2 isogeny-form lattice Gram [a,1,bd] (+) [b,-1,ad]: discriminants and determinant.
"""
import sympy as sp

d, m, a, b, p, c, e = sp.symbols('d m a b p c e')


class Q:
    def __init__(s, al, be, x):
        s.al, s.be, s.x = al, be, [sp.sympify(t) for t in x]

    def __mul__(s, o):
        al, be = s.al, s.be
        a0, a1, a2, a3 = s.x
        b0, b1, b2, b3 = o.x
        # i^2=al, j^2=be, k^2=-al*be, ij=k, ji=-k, ik=al j, ki=-al j, jk=-be i, kj=be i
        r0 = a0*b0 + al*a1*b1 + be*a2*b2 - al*be*a3*b3
        r1 = a0*b1 + a1*b0 - be*a2*b3 + be*a3*b2
        r2 = a0*b2 + a2*b0 + al*a1*b3 - al*a3*b1
        r3 = a0*b3 + a3*b0 + a1*b2 - a2*b1
        return Q(al, be, [sp.expand(t) for t in (r0, r1, r2, r3)])

    def __add__(s, o):
        return Q(s.al, s.be, [sp.expand(x + y) for x, y in zip(s.x, o.x)])

    def sc(s, t):
        return Q(s.al, s.be, [sp.expand(t * x) for x in s.x])

    def trd(s):
        return sp.simplify(2 * s.x[0])

    def nrd(s):
        al, be = s.al, s.be
        x0, x1, x2, x3 = s.x
        return sp.expand(x0**2 - al*x1**2 - be*x2**2 + al*be*x3**2)


def lemma12():
    al, be = -d, -d*(4*d*m - 1)
    one = Q(al, be, [1, 0, 0, 0])
    u = Q(al, be, [0, 1, 0, 0])
    v = Q(al, be, [0, -1/(2*d), 1/(2*d), 0])
    rel = [sp.simplify((u*u).x[0] + d), sp.simplify((v*v).x[0] + m), [sp.simplify(t) for t in (u*v + v*u).x]]
    print("u^2+d, v^2+m, uv+vu:", rel)
    B = [one, u, v, u*v]
    G = sp.Matrix(4, 4, lambda r, s: sp.simplify((B[r]*B[s]).trd()))
    print("Gram trd(x_i x_j):", G.tolist())
    print("det:", sp.factor(G.det()))
    # closure: all products of basis elements in Z-span: check v*u = 1 - u*v and products listed
    vu = v*u
    print("vu - (1-uv):", [sp.simplify(x) for x in (vu + u*v + one.sc(-1)).x])


def lemma31():
    al, be = -d, -p
    i = Q(al, be, [0, 1, 0, 0]); j = Q(al, be, [0, 0, 1, 0]); k = Q(al, be, [0, 0, 0, 1])
    lhs = (i.sc(2*a) + j) * (i.sc(2*b) + j.sc(-1))
    print("Lemma 3.1 product:", lhs.x, " expected:", [-(4*a*b*d - p), 0, 0, -2*(a+b)])
    print("N(2ai+j) =", (i.sc(2*a)+j).nrd(), " N(1+2ck) =", (Q(al, be, [1, 0, 0, 2*c])).nrd())


def isog():
    # Gram of degree form on (phi1, phi2, u phi1, u phi2): (x,y)-pairing = (deg(x+y)-deg x-deg y)/2
    G = sp.Matrix([[a, 0, 0, sp.Rational(1, 2)], [0, b, -sp.Rational(1, 2), 0],
                   [0, -sp.Rational(1, 2), a*d, 0], [sp.Rational(1, 2), 0, 0, b*d]])
    print("isogeny lattice det:", sp.factor(G.det()), " (claimed (pe/4)^2 with pe=4abd-1)")


if __name__ == "__main__":
    lemma12(); lemma31(); isog()
