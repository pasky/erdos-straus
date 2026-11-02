# z54 HCKILL: symbolic checks for the quadratic-family classification (Props F2-F4).
# (a, delta) = (U^2 - W^2, 16 W^2 - U^2)/15 is the general line-4-confined family (up to rational squares).
# For each x in C, the endpoint/level square-class forms are  E_x = delta + 4 a x,  L_x = x (x delta + 4 a).
import sympy as sp
U, W = sp.symbols('U W')
a = (U**2 - W**2)/15; de = (16*W**2 - U**2)/15
for x in [4, 7, 8, 12, 15, 16]:
    E = sp.factor(sp.expand(de + 4*a*x)); L = sp.factor(sp.expand(x*(x*de + 4*a)))
    print(f"x={x}: delta+4ax = {E} ;  x(x delta+4a) = {L}")
# branch points of the (Z/2)^4 cover for lines {7, 8}: roots of the four binary forms in t = U/W
t = sp.symbols('t')
forms = {'7e': 9*t**2-4, '7l': 36-t**2, '8e': 31*t**2-16, '8l': 31-t**2}
roots = {k: sp.solve(f, t) for k, f in forms.items()}
allr = [r for v in roots.values() for r in v]
print("roots:", roots); print("all 8 distinct:", len(set(allr)) == 8)
# no product of a nonempty subset of the forms is a square in C[t] (forms squarefree, pairwise coprime) -> irreducible cover
fs = list(forms.values())
print("pairwise gcd 1:", all(sp.gcd(fs[i], fs[j]) == 1 for i in range(4) for j in range(i+1, 4)))
# Riemann-Hurwitz for the degree-16 (Z/2)^4 cover of P^1 branched at 8 points, each with 8 preimages of index 2:
deg, br = 16, 8
g = (deg*(-2) + br*(deg//2)) // 2 + 1
print("genus of each {4,7,8}-curve:", g)
# genus of the {4,7} curve: (Z/2)^2 cover branched at 4 points
deg, br = 4, 4
print("genus of the {4,7} curve E7:", (deg*(-2) + br*(deg//2))//2 + 1)
