"""O143 memo 3: the elliptic fibration of the ES surface by u1+u2+u3 = s.

In s-coordinates (S_i = 1/u_i) the fibre is C_N : (x+y+z)(xy+yz+zx) = N xyz with N = 4s/n
(= (sum u)(sum 1/u)).  Checks:
 (1) #C_N(F_q) = #E_N(F_q) for E_N : Y^2 = X(X^2 + (N^2-6N-3)X + 16N)  (Weierstrass model, from memory of
     Bremner-Guy-Nowakowski; here only checked by point counts), several N, q.
 (2) symbolic discriminant of E_N in N  ->  fibre types (I2 at N=0, I3 at N=1, I1 at N=9, I6 at infinity).
 (3) every positive ES point of 4/p (p < PMAX) is a NON-torsion point of C_N (nP != O for n <= 12, O = (1:-1:0)),
     so E_N(Q) has rank >= 1 at every N = 4(u1+u2+u3)/p coming from an ES solution.
Run: PYTHONPATH=scripts uv run python scripts/bs_cubic_elliptic.py
"""
from fractions import Fraction as Fr
from math import gcd
import sympy as sp
from geo_common import es_solutions

PMAX = 120


def count_CN(N, q):
    """projective points of (x+y+z)(xy+yz+zx) - N xyz over F_q (N given mod q)."""
    c = 0
    pts = [(1, y, z) for y in range(q) for z in range(q)] + [(0, 1, z) for z in range(q)] + [(0, 0, 1)]
    for x, y, z in pts:
        if ((x + y + z)*(x*y + y*z + z*x) - N*x*y*z) % q == 0:
            c += 1
    return c


def count_EN(N, q):
    a, b = (N*N - 6*N - 3) % q, (16*N) % q
    c = 1
    for X in range(q):
        r = (X*(X*X + a*X + b)) % q
        if r == 0:
            c += 1
        elif pow(r, (q - 1)//2, q) == 1:
            c += 2
    return c


def F(P, N):
    x, y, z = P
    return (x + y + z)*(x*y + y*z + z*x) - N*x*y*z


def grad(P, N):
    x, y, z = P
    s, e = x + y + z, x*y + y*z + z*x
    return (e + s*(y + z) - N*y*z, e + s*(x + z) - N*x*z, e + s*(x + y) - N*x*y)


def hess_q(P, Q, N):
    """Q^T H(P) Q / 2 via finite difference: F(P+tQ) = F(P) + t gradF(P).Q + t^2 * this + t^3 F(Q)."""
    # second-order coefficient from exact polynomial evaluation at t = 1, -1
    Pp = tuple(a + b for a, b in zip(P, Q)); Pm = tuple(a - b for a, b in zip(P, Q))
    return (F(Pp, N) + F(Pm, N))/2 - F(P, N)


def norm(P):
    P = [Fr(t) for t in P]
    den = 1
    for t in P:
        den = den*t.denominator//gcd(den, t.denominator)
    v = [int(t*den) for t in P]
    g = 0
    for t in v:
        g = gcd(g, t)
    v = [t//g for t in v]
    for t in v:
        if t != 0:
            if t < 0:
                v = [-s for s in v]
            break
    return tuple(v)


def third(P, Q, N):
    if norm(P) == norm(Q):
        g = grad(P, N)
        # a point on the tangent line, different from P
        cands = [(g[1], -g[0], 0), (g[2], 0, -g[0]), (0, g[2], -g[1])]
        for R in cands:
            if any(R) and norm(R) != norm(P):
                break
        fR, h = F(R, N), hess_q(P, R, N)
        if fR == 0:
            return norm(R) if h != 0 else norm(P)
        return norm(tuple(fR*a - h*b for a, b in zip(P, R)))
    a = sum(gi*qi for gi, qi in zip(grad(Q, N), P))  # D_P F(Q)
    b = sum(gi*qi for gi, qi in zip(grad(P, N), Q))  # D_Q F(P)
    if a == 0 and b == 0:
        return None
    return norm(tuple(a*x - b*y for x, y in zip(P, Q)))


def add(P, Q, O, N):
    return third(O, third(P, Q, N), N)


def main():
    bad = 0
    for N in [10, 13, 17, 25, 29, 100]:
        for q in [7, 11, 13, 19, 23, 29, 31]:
            if (N*(N - 1)*(N - 9)) % q == 0:
                continue
            if count_CN(N % q, q) != count_EN(N % q, q):
                bad += 1
    print("(1) point-count mismatches C_N vs E_N:", bad)
    n_ = sp.symbols('N')
    a, b = n_**2 - 6*n_ - 3, 16*n_
    print("(2) disc(E_N) =", sp.factor(16*b**2*(a**2 - 4*b)))
    O = (1, -1, 0)
    tot = tors = 0
    for p in sp.primerange(5, PMAX):
        for u in es_solutions(p):
            N = Fr(4*sum(u), p)
            P = norm((Fr(1, u[0]), Fr(1, u[1]), Fr(1, u[2])))
            assert F(P, N) == 0
            R = P
            tot += 1
            for k in range(2, 13):
                R = add(R, P, O, N)
                if R == norm(O):
                    tors += 1
                    break
    print(f"(3) ES points of 4/p, p<{PMAX}: {tot}; torsion among them: {tors}")


if __name__ == "__main__":
    main()
