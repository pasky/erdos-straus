# z54 HCKILL: line-4 quadratic confinement families with p = 1 (mod 8).
# Line 4 confined identically  <=>  (a, delta) ~ (U^2 - W^2, 16 W^2 - U^2)/15 up to rational squares, and then
#   4a (p + 4)  = y^2 + (2u)^2   with delta + 16 a = 4 u^2,
#   a (4p + 1)  = y^2 + w^2      with delta + a = w^2,      where 4a p = y^2 + delta.
# For each small (U, W): list the classes y mod 8*4a giving integral p = 1 (8), and report the reduced polynomial
#   P(t) = p(y0 + M t) (M = 8*4a/gcd...), its content and fixed prime divisors (Bunyakovsky admissibility).
# Usage: uv run --with sympy python z54_hckill_fam4.py UMAX
import sys, math
from sympy import factorint, Poly, symbols, gcd as sgcd
UMAX = int(sys.argv[1])
t = symbols('t')
out = []
for U in range(2, UMAX+1):
    for W in range(U//4+1, U):
        if math.gcd(U, W) != 1: continue
        A0, B0 = U*U - W*W, 16*W*W - U*U
        if A0 <= 0 or B0 <= 0: continue
        g = math.gcd(A0, B0); s = (3 if g % 3 else 1)*(5 if g % 5 else 1)
        a, de = s*s*A0//15, s*s*B0//15
        for p_, e_ in factorint(math.gcd(a, de)).items():
            while a % (p_*p_) == 0 and de % (p_*p_) == 0: a//=p_*p_; de//=p_*p_
        if (-de) % 4 not in (0, 1): continue   # not a discriminant: no integral p
        # u, w
        uu2 = (de + 16*a); ww2 = de + a
        u = math.isqrt(uu2//4); w = math.isqrt(ww2)
        assert 4*u*u == uu2 and w*w == ww2, (U, W, a, de)
        M = 32*a
        ys = [y for y in range(M) if (y*y + de) % (4*a) == 0 and ((y*y + de)//(4*a)) % 8 == 1]
        if not ys: continue
        # bad classes: l = 3 mod 4 dividing u or w must not divide y  (else l | p+4 or 4p+1 possible)
        bad = sorted({l for l in list(factorint(u).keys()) + list(factorint(w).keys()) if l % 4 == 3})
        out.append((a, de, U, W, u, w, ys[:4], len(ys), bad))
out.sort()
for r in out[:25]:
    a, de, U, W, u, w, ys, ny, bad = r
    y0 = ys[0]; P = Poly(((y0 + 32*a*t)**2 + de)/(4*a), t)
    co = [int(c) for c in P.all_coeffs()]
    cont = math.gcd(*co)
    # fixed prime divisors: primes q <= deg+... for quadratics only q = 2 can be fixed beyond content; check q <= 3
    fixed = [q for q in (2, 3) if all(sum(c*(tt**(len(co)-1-i)) for i, c in enumerate(co)) % q == 0 for tt in range(q))]
    print(f"a={a} delta={de} (U,W)=({U},{W}) u={u} w={w}  #y-classes mod 32a with p=1(8): {ny}, e.g. y0={ys}  "
          f"P(t)=p(y0+32a t)={co} content={cont} fixed2/3={fixed} avoid y=0 mod {bad}")
