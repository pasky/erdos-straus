# z52d P2 TO8 Z3175: F_p[T] (p prime: q in {3,5}) search for 4/P = 1/X+1/Y+1/Z with X,Y,Z nonzero polynomials, X monic (deg<=2n),
# P monic irreducible of degree n. Reduce to 2-term: (4X-P)/(PX)=A/B, need (cd+B) divisible by A and (B^2/d+B) divisible by A, c in F_p^*.
import itertools, sys
from sympy import symbols, Poly
T = symbols('T')
def monic_polys(p, deg):
    for coeffs in itertools.product(range(p), repeat=deg):
        yield Poly([1] + list(coeffs), T, modulus=p)
def irreducibles(p, n):
    out=[]
    for c in itertools.product(range(p), repeat=n):
        P = Poly([1]+list(c), T, modulus=p)
        if P.is_irreducible: out.append(P)
    return out
def two_term_ok(A, B, p):
    # exists nonzero Y,Z with A/B = 1/Y+1/Z ?  equivalently (AY-B)(AZ-B)=B^2
    if A.is_zero: return False
    fl = Poly(B, T, modulus=p).factor_list()[1]
    # enumerate monic divisors of B^2
    divs = [Poly(1, T, modulus=p)]
    for f, e in fl:
        new = []
        for d in divs:
            for k in range(2 * e + 1):
                new.append(d * f ** k)
        divs = new
    B2 = B * B
    for d0 in divs:
        for c in range(1, p):
            d = d0 * c
            e2 = (B2.quo(d)) if B2.rem(d).is_zero else None
            if e2 is None: continue
            y1 = d + B; z1 = e2 + B
            if y1.is_zero or z1.is_zero: continue
            if y1.rem(A).is_zero and z1.rem(A).is_zero:
                return True
    return False
def has_rep(P, p):
    n = P.degree()
    four = Poly(4, T, modulus=p)
    for dX in range(0, 2 * n + 1):
        for cX in monic_polys(p, dX) if dX > 0 else [Poly(1, T, modulus=p)]:
            num = four * cX - P          # (4X-P)/(P X)
            if num.is_zero: continue
            den = P * cX
            g = num.gcd(den)
            A = num.quo(g); B = den.quo(g)
            if two_term_ok(A, B, p): return True
    return False
for p, nmax in [(3, 4), (5, 3)]:
    fails = []
    for n in range(1, nmax + 1):
        for P in irreducibles(p, n):
            if not has_rep(P, p): fails.append(str(P.as_expr()))
    print(f"F_{p}[T]: monic irreducible P with deg<= {nmax}: no rep found (X monic deg<=2n): {fails}")
