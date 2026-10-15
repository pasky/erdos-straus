"""R228: symbolic check of NEAR_SQUARE_EXIST §5.1 (3-parameter Type I (1,0,1), Lambda = 1 families) and of the
converse ("every such family has this form"), plus a numeric spot check that the resulting triples solve 4/n."""
from sympy import symbols, simplify, expand, rem, Poly, Rational, factor, together, solve
m, x, al, la, j, de, kap = symbols('m x alpha lambda j delta kappa')
n = m**2 - j
nx = x**2 - j
c = -al * nx
a = la * (m - x) + al
d = (m - x) / (4 * c * la) - 1 / (4 * al**2)
f = expand(4 * a * c * d - n)
kappa = al / la + la * nx / al - 2 * x
print("f - kappa(m-x) =", simplify(f - kappa * (m - x)))
for name, P in (("n a + c", n * a + c), ("4 a^2 d + 1", 4 * a**2 * d + 1)):
    print(name, "at m = x:", simplify(P.subs(m, x)), "; remainder mod (m-x):", simplify(rem(together(P).as_numer_denom()[0], m - x, m)))
# converse: a linear, c constant, d linear, f = 4acd - n linear with root x
cc = symbols('c')
a2 = la * (m - x) + al
d2 = de * (m - x) + symbols('d0')
f2 = expand(4 * a2 * cc * d2 - n)
sol = solve([Poly(f2, m).coeff_monomial(m**2), (4 * a2**2 * d2 + 1).subs(m, x), (n * a2 + cc).subs(m, x)], [de, symbols('d0'), cc], dict=True)
print("converse solutions:", sol)
for s in sol:
    print("  f2(x) =", simplify(f2.subs(s).subs(m, x)), "; d matches:", simplify(d2.subs(s) - d))
