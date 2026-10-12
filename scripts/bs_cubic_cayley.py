"""O143 brainstorm: ES surface <-> Cayley cubic / Markoff k=4 / SU(2)-CM dictionary.

Checks (all tiny):
 (A) symbolic: Markoff-Cayley coordinates X,Y,Z of the symmetric Cayley form sum 1/y_i = 0.
 (B) symbolic: CM parametrisation y(x,y,x',y',D) solves sum 1/y_i = 0.
 (C) for every positive solution of 4/p (p prime < PMAX): image lies in the open compact
     component |X|,|Y|,|Z| < 2; the CM discriminant class D = sqf(p*u1*u2*u3) is p-free for
     Type I and divisible by p for Type II; Type I has (-D/p) = -1 (BL / GEOMETRY_ES Prop 5.1).
 (D) the Markoff Vieta move X -> YZ - X maps positive ES points to positive ES points
     (of a different n); prints a short orbit.
Run: PYTHONPATH=scripts uv run python scripts/bs_cubic_cayley.py
"""
from fractions import Fraction as Fr
from math import gcd
import sympy as sp
from geo_common import es_solutions

PMAX = 400


def symbolic():
    y0, y1, y2, y3 = sp.symbols('y0:4')
    e1 = y0 + y1 + y2 + y3
    e3 = y1*y2*y3 + y0*y2*y3 + y0*y1*y3 + y0*y1*y2
    X = 2*(y0 + y1 - y2 - y3)/e1
    Y = 2*(y0 - y1 + y2 - y3)/e1
    Z = 2*(y0 - y1 - y2 + y3)/e1
    q = sp.factor(sp.together(X**2 + Y**2 + Z**2 - X*Y*Z - 4))
    print("(A) X^2+Y^2+Z^2-XYZ-4 =", q)
    x, y, xp, yp, D = sp.symbols("x y xp yp D")
    Y0 = x*xp*(x*xp - D*y*yp)
    Y1 = D*x*yp*(x*yp + xp*y)
    Y2 = D*xp*y*(x*yp + xp*y)
    Y3 = -D*y*yp*(x*xp - D*y*yp)
    s = sp.simplify(1/Y0 + 1/Y1 + 1/Y2 + 1/Y3)
    print("(B) sum 1/y_i for CM parametrisation =", s)
    # X for the CM parametrisation equals 2cos(2A), tan A = y sqrt(D)/x
    Xp = sp.simplify((2*(Y0 + Y1 - Y2 - Y3)/(Y0 + Y1 + Y2 + Y3)) - 2*(x**2 - D*y**2)/(x**2 + D*y**2))
    print("(B') X - 2(x^2-Dy^2)/(x^2+Dy^2) =", Xp)


def sqf(m):
    m = abs(m)
    out = 1
    for q, e in sp.factorint(m).items():
        if e % 2:
            out *= q
    return out


def to_markoff(n, u):
    y = [Fr(4*u[0]), Fr(4*u[1]), Fr(4*u[2]), Fr(-n)]
    e1 = sum(y)
    X = 2*(y[0] + y[1] - y[2] - y[3])/e1
    Y = 2*(y[0] - y[1] + y[2] - y[3])/e1
    Z = 2*(y[0] - y[1] - y[2] + y[3])/e1
    return e1, X, Y, Z


def from_markoff(X, Y, Z):
    """Return (n, (u1,u2,u3)) positive ES point, or None if not in the positive tetrahedron."""
    y = [1 + (X + Y + Z)/2, 1 + (X - Y - Z)/2, 1 + (-X + Y - Z)/2, 1 + (-X - Y + Z)/2]
    den = 1
    for t in y:
        den = den*t.denominator//gcd(den, t.denominator)
    v = [int(t*den) for t in y]
    g = 0
    for t in v:
        g = gcd(g, t)
    v = [t//g for t in v]
    if sum(1 for t in v if t < 0) > 2:
        v = [-t for t in v]
    neg = [i for i, t in enumerate(v) if t < 0]
    if len(neg) != 1 or 0 in v:   # one negative coordinate = one of the 4 tetrahedron faces
        return None
    j = neg[0]
    pos = [t for i, t in enumerate(v) if i != j]
    lam = 4//gcd(4, gcd(pos[0], gcd(pos[1], pos[2])))
    return lam*(-v[j]), tuple(sorted(lam*t//4 for t in pos))


def check_primes():
    nsol = bad = 0
    for p in sp.primerange(5, PMAX):
        for u in es_solutions(p):
            nsol += 1
            e1, X, Y, Z = to_markoff(p, u)
            assert X**2 + Y**2 + Z**2 - X*Y*Z == 4
            ok = e1 > 0 and all(abs(t) < 2 for t in (X, Y, Z))
            k = sum(1 for t in u if t % p == 0)
            D = sqf(p*u[0]*u[1]*u[2])
            if k == 1:   # Type I
                ok &= (D % p != 0) and sp.jacobi_symbol((-D) % p, p) == -1
            elif k == 2:  # Type II
                ok &= (D % p == 0)
            else:
                ok = False
            back = from_markoff(X, Y, Z)
            ok &= back == (p, tuple(sorted(u)))
            bad += not ok
    print(f"(C) primes 5..{PMAX}: {nsol} positive solutions, failures = {bad}")


def vieta_orbit():
    p, u = 5, sorted(es_solutions(5)[0])
    e1, X, Y, Z = to_markoff(p, u)
    print("(D) start 4/5 =", u, " D =", sqf(5*u[0]*u[1]*u[2]))
    moves = [lambda X, Y, Z: (Y*Z - X, Y, Z), lambda X, Y, Z: (X, X*Z - Y, Z),
             lambda X, Y, Z: (X, Y, X*Y - Z)]
    pt = (X, Y, Z)
    for i, j in enumerate([0, 1, 2, 0, 1]):
        pt = moves[j](*pt)
        r = from_markoff(*pt)
        D = sqf(r[0]*r[1][0]*r[1][1]*r[1][2]) if r else None
        print(f"    move x{j+1}: |coords|<2: {all(abs(t) < 2 for t in pt)};  ES point:", r,
              " D=sqf(n*u1*u2*u3) =", D)


if __name__ == "__main__":
    symbolic()
    check_primes()
    vieta_orbit()
