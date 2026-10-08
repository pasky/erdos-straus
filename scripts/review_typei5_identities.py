# R92 from-scratch sympy check of TYPEI5 Lemma 3.2 (H), (Lin), Prop 3.3 algebra.
from sympy import cancel, symbols, expand, simplify, factor, together, numer, Rational
rho, lam, u, j, T, W, s, sig, om, Dl = symbols('rho lambda u j T W s sigma omega Delta')
# W = 7^a ; m = rho j - lambda u ; y = T u/2 - j ; z = T u/2 + j ; mP1 = y^2 - 2 W m u j
m = rho*j - lam*u
y = T*u/2 - j
lhs = rho*(y**2 - 2*W*m*u*j) - m*(T*u/2 + j)          # = 0  (rho * mP1 = m * rho P1)
Delta = 8*j*W*m + 6*T*j - T**2*u
H = rho*Delta - 2*lam*(T*u + 2*j)
# lhs should equal (u/4 or so) * H  up to a factor
print("lhs / H =", simplify(lhs / H))
# (Lin): from (H) m = lam[u(2Tj - D) + 4j^2]/D ; plug into D = 8 j W m + 6Tj - T^2 u
kap = 8*W*lam
mD = lam*(u*(2*T*j - Dl) + 4*j**2)/Dl
eq = numer(together(8*j*W*mD + 6*T*j - T**2*u - Dl))
Lin = u*(kap*j*(2*T*j - Dl) - Dl*T**2) - (Dl*(Dl - 6*T*j) - 4*kap*j**3)
print("Lin consistency (should be const*Lin):", simplify(eq / Lin))
# consistency check that m from (H) really is rho j - lam u
rhoH = 2*lam*(T*u + 2*j)/Dl
print("m formula:", simplify(rhoH*j - lam*u - mD))
# (iii): g = 2T^3 - s kap, N(j) = 4 kap j^3 + (2Tj - s)(4Tj + s); R = g^3 N(sT^2/g)
k = symbols('kappa')
g = 2*T**3 - s*k
N = lambda jj: 4*k*jj**3 + (2*T*jj - s)*(4*T*jj + s)
R = expand(g**3 * N(s*T**2/g))
print("R - k s^3 (4T^3 - s k)^2 =", cancel(R - k*s**3*(4*T**3 - s*k)**2))
print("R - [4 k s^3 T^6 + g s^3 k (4T^3+g)] =", cancel(R - (4*k*s**3*T**6 + g*s**3*k*(4*T**3 + g))))
# (iii) Lin with Delta = 2Tj - s gives u*(g j - s T^2) = N(j) ?
L3 = Lin.subs({Dl: 2*T*j - s, W: k/(8*lam)})
print("(iii) Lin + u(gj - sT^2) - N(j)... :", expand(-L3 - (u*(g*j - s*T**2) - N(j))))
# g^3 N(j) - R divisible by (g j - s T^2) as polynomial with integer coeffs?
from sympy import div, Poly
q, r = div(Poly(expand(g**3*N(j) - R), j), Poly(g*j - s*T**2, j))
print("remainder:", r, " quotient integral coeffs:", q)
# (v): Delta = 2Tj + sigma ; identity  kap j om sig = (2Tj+sig)[(2Tj - sig)^2 - om T^2] with u sig = 4j^2 - om
L5 = Lin.subs({Dl: 2*T*j + sig, W: k/(8*lam)})
L5u = expand(L5.subs(u, (4*j**2 - om)/sig) * sig)
print("(v) identity:", expand(L5u + (k*j*om*sig - (2*T*j + sig)*((2*T*j - sig)**2 - om*T**2))), "or", expand(L5u - (k*j*om*sig - (2*T*j + sig)*((2*T*j - sig)**2 - om*T**2))))
# (v) divisibility constant: s -> -sigma
gp = 2*T**3 + sig*k
Rv = expand(R.subs(s, -sig))
print("(v) R(-sigma) + k sig^3 (4T^3 + sig k)^2 =", cancel(Rv + k*sig**3*(4*T**3 + sig*k)**2))
print("author's (v) const - k sig^3 (4T^3+sig k)^2 =", expand(4*k*sig**3*T**6 + gp*sig**3*k*(4*T**3 + 2*T**3 + sig*k) - k*sig**3*(4*T**3 + sig*k)**2))
# (iv): Delta = 2Tj
L4 = expand(Lin.subs({Dl: 2*T*j, W: k/(8*lam)}))
print("(iv):", factor(L4))
# (ii): lam<0: kap = -K1, Delta = -x  : u (K x - E) = x^2 + 6Tjx + 4K1 j^3, K = T^2 - K1 j, E = 2K1 T j^2
x, K1 = symbols('x K1')
L2 = expand(Lin.subs({Dl: -x, W: -K1/(8*lam)}))
print("(ii):", expand(L2 - (u*((T**2 - K1*j)*x - 2*K1*T*j**2) - (x**2 + 6*T*j*x + 4*K1*j**3))))
