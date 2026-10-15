"""R259 from-scratch symbolic checks of the rearrangements used in NORMFORM_CUBIC Thms 1.1', 1.2', 3.1.
All quantities are treated as free symbols (P, E, A1, ... independent), so each check is an identity in
a free polynomial ring; the case hypotheses (e.g. 4abd = 1) are imposed by substitution.
Run: uv run --with sympy python scripts/review_r259_identities.py
"""
from sympy import symbols, expand, simplify, Rational

P, E, A, B, C, D, A1, a, b, d, k, G, kap, kp, EA, EB = symbols('P E A B C D A1 a b d k G kappa kappa2 EA EB')

def zero(x, msg):
    assert simplify(expand(x)) == 0, (msg, simplify(expand(x)))
    print('ok:', msg)

typeI = lambda A, B, C, D: 4*A*B*C*D - (P*(A + B) + C)
typeII = lambda A, B, C, D: 4*A*B*C*D - (A + B + C*P)

# ---- Thm 1.1' (b2): A = (P+E)/(4BD), C*E = A+B  =>  E(4BDC - 1) = P + 4B^2 D
Ab = (P + E)/(4*B*D); Cb = (Ab + B)/E
zero(typeII(Ab, B, Cb, D), "1.1'(b2) the family A=(P+E)/(4BD), C=(A+B)/E satisfies Type II")
zero(E*(4*B*D*Cb - 1) - (P + 4*B**2*D), "1.1'(b2) E(4BDC-1) = P + 4B^2 D")
# (b1): C(4ABD - P) = A + B
zero(typeII(A, B, C, D) - (C*(4*A*B*D - P) - (A + B)), "1.1' C(4ABD-P) = A+B form of Type II")

# ---- Thm 1.2' (c1)
# B of degree k: B = (P+E)/(4CD), A*E = PB + C  => E(4CD A - P) = P^2 + 4C^2 D
Bb = (P + E)/(4*C*D); Ab = (P*Bb + C)/E
zero(typeI(Ab, Bb, C, D), "1.2'(c1,B) family satisfies Type I")
zero(E*(4*C*D*Ab - P) - (P**2 + 4*C**2*D), "1.2'(c1,B) E(4CDA-P) = P^2 + 4C^2D")
# C of degree k: C = P/(4BD) + E;  Type I  <=>  E(4BD A - 1) = kappa P, kappa = B + 1/(4BD)
Cc = P/(4*B*D) + E
zero(typeI(A, B, Cc, D) - (E*(4*B*D*A - 1) - (B + 1/(4*B*D))*P), "1.2'(c1,C) Type I == E(4BDA-1) - kappa P")
# D of degree k: D = P/(4BC) + E; Type I <=> 4BC A E = PB + C
Dd = P/(4*B*C) + E
zero(typeI(A, B, C, Dd) - (4*B*C*A*E - (P*B + C)), "1.2'(c1,D) Type I == 4BCAE - (PB + C)")
# (c2) mu = k: A = kap P + EA, B = kp P + EB
Aa = kap*P + EA; Ba = kp*P + EB
expr = expand(typeI(Aa, Ba, C, D))
G2 = (4*C*D*kap - 1)*EB + (4*C*D*kp - 1)*EA
zero(expr - ((4*C*D*kap*kp - kap - kp)*P**2 + P*G2 - (C - 4*C*D*EA*EB)), "1.2'(c2,mu=k) expansion P^2 coeff, P*G, rest")

# ---- Thm 3.1
zero(typeI(A, B, C, D) - (C*(4*A*B*D - 1) - P*(A + B)), "3.1 C(4ABD-1) = P(A+B) form")
# degenerate family: B=b, D=-1/(4b^2), C=-bP, A arbitrary
zero(typeI(A, b, -b*P, -1/(4*b**2)), "3.1 degenerate family is a Type I solution")
# (e0) lambda: A + b = lam (4 b d A - 1) with 4 lam b d = 1 forces lam = -b
lam = symbols('lam')
# identity in A: coefficient of A: 1 = 4 lam b d ; constant: b = -lam
print('ok: (e0) coefficient comparison A+b = lam(4bdA-1): A-coeff 1 = 4 lam b d, const b = -lam  =>  d = -1/(4b^2) (by hand)')
# (e1)(i): A = a + P A1, B=b, D=d, 4abd=1:  4ABD - 1 = P * A1/a
dd = 1/(4*a*b)
zero(4*(a + P*A1)*b*dd - 1 - P*A1/a, "3.1(e1)(i) H = A1/a")
# (i) a+b=0: C = (A+B)/H = a(a+b+P A1)/A1 = aP when b=-a
zero(((a + (-a) + P*A1)/(A1/a)) - a*P, "3.1(e1)(i) a+b=0 gives C = aP = -bP")
# (ii): B = b + kap P, D = d (4abd=1): H = 4d(a kap + B A1)
Bii = b + kap*P
zero((4*(a + P*A1)*Bii*dd - 1) - P*4*dd*(a*kap + Bii*A1), "3.1(e1)(ii) H = 4d(a kappa + B A1)")
Hii = 4*dd*(a*kap + Bii*A1)
zero(((a + P*A1) + Bii - G*Hii) - (-(A1*(4*dd*G*Bii - P) - (a + Bii - 4*dd*G*a*kap))), "3.1(e1)(ii) A+B=GH <=> A1(4dGB-P) = a+B-4dGa kappa")
# (iii): B = b, D = d + kap P: H = 4b(a kap + A1 D)
Diii = dd + kap*P
zero((4*(a + P*A1)*b*Diii - 1) - P*4*b*(a*kap + A1*Diii), "3.1(e1)(iii) H = 4b(a kappa + A1 D)")
Hiii = 4*b*(a*kap + A1*Diii)
zero(((a + P*A1) + b - G*Hiii) - (-(A1*(4*b*G*Diii - P) - (a + b - 4*b*G*a*kap))), "3.1(e1)(iii) A+B=GH <=> A1(4bGD-P) = a+b-4bGa kappa")
print('all identities verified')
