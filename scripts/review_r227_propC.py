"""R227 from-scratch check of Prop C(a,b) for general M (not only M in {4, 8, 12}).
F_M = Q(alpha), alpha = sqrt(p)*(z - 1/z), alpha^2 = p(theta^2 - 4), theta = z + 1/z.
f = Res_theta(Psi_M(theta), (x - k theta)^2 - p(theta^2 - 4)) = char. poly of beta = alpha + k theta (irreducible => F_M = Q(beta)).
Check: h (prime, h not dividing disc(f) M p) splits completely in F_M  <=>  Frob_h in {1, g}
       <=>  (h = 1 mod M and (p/h) = 1)  or  (h = -1 mod M and (p/h) = -1).
Also checks irreducibility of f (so F_M has degree phi(M)) and total negativity of alpha^2 numerically.
usage: uv run --with sympy python scripts/review_r227_propC.py
"""
from sympy import symbols, resultant, Poly, cos, pi, totient, primerange, legendre_symbol as L, minimal_polynomial
from sympy import discriminant, factor_list, Rational, gcd as sgcd

x, th = symbols("x th")
bad = checks = 0
for M in (5, 7, 9, 15, 16, 20, 24):
    psi = Poly(minimal_polynomial(2 * cos(2 * pi / M), th), th)
    for p in (5, 13, 17, 29, 37, 41):
        if M % p == 0:
            continue
        # primitive element beta = alpha + k*theta of F_M = Q(theta)(alpha) (alpha alone may generate a subfield, e.g. M = 16)
        for k in (1, 2, 3, 5):
            f = Poly(resultant(psi.as_expr(), (x - k * th) ** 2 - p * (th ** 2 - 4), th), x)
            assert f.degree() == totient(M)
            fl = factor_list(f.as_expr())
            if len(fl[1]) == 1 and fl[1][0][1] == 1:
                break
        else:
            raise AssertionError((M, p))
        D = int(discriminant(f.as_expr(), x))
        co = [int(c) for c in f.all_coeffs()]
        for h in primerange(3, 1500):
            if D % h == 0 or (M * p) % h == 0:
                continue
            roots = 0
            for r in range(h):
                val = 0
                for c in co:
                    val = (val * r + c) % h
                roots += (val == 0)
            split = roots == f.degree()
            pred = (h % M == 1 and L(p % h, h) == 1) or (h % M == M - 1 and L(p % h, h) == -1)
            checks += 1
            bad += split != pred
print("Prop C(b) general-M checks", checks, "mismatches", bad)
