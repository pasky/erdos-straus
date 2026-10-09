"""R99 from-scratch check of POINTWISE_TYPEI6 Lemma 1.1, Lemma 1.3, Lemma 3.1 identity, Prop 2.1 algebra,
Remark 1.2 numbers.  Approach: free symbols (cp, s=7^a, delta, P1, X, u); T is ELIMINATED via the Pell
relation 16 P X^2 - Q u^2 = 1, so every identity that holds 'on solutions' must become a rational identity.
"""
import sympy as sp

cp, s, de, P1, X, u = sp.symbols('cp s delta P1 X u', positive=True)
co = s*cp
# Pell: 16 cp P1 X^2 - s*(M/P1)*u^2 = 1, M = co de^2 + T  ->  solve for T
T = sp.together(P1*(16*cp*P1*X**2 - 1)/(s*u**2) - co*de**2)
M = co*de**2 + T
P = cp*P1
Q = s*M/P1
d = co*M
assert sp.simplify(16*P*X**2 - Q*u**2 - 1) == 0
assert sp.simplify(P*Q - d) == 0
m = cp*de**2
g = 4*P1*X - s*u*de
y = cp*g*de
j = T*u/2 - y
rho = (T*u/2 + j)/P1
lam = (rho*j - m)/u
sig = 8*s*m*j + 4*T*j - T**2*u
mu = 8*co*de**2 + 4*T
kap = 8*s*lam
z = lambda e: sp.simplify(sp.together(e)) == 0
# Lemma 1.1
assert z(8*j - mu*u + 32*cp*de*P1*X), "1.1(a)"
assert z(4*j**2 - u*sig - 4*m*P1), "1.1(b)"
assert z(sig - (4*lam*P1 - 2*T*j)), "1.1(c)"
# quadratic form / discriminant claim in (b)
J, U = sp.symbols('J U')
qf = 4*J**2 - mu*J*U + T**2*U**2
assert z(sp.expand(qf.subs({J: j, U: u})) - (4*j**2 - u*sig))
assert z(sp.discriminant(qf, J).subs(U, 1) - 64*de**2*d), "disc"
# Lemma 1.3
expr13 = (2*s*T*(T*rho + 2*lam)*u**2 - (8*s*T*rho**2*P1 + kap*rho*P1 + 4*T**2)*u
          + P1*(8*s*rho**3*P1 + 6*T*rho - 4*lam))
assert z(expr13), "1.3"
# also Delta identity sigma = Delta - 2Tj (TYPEI5 notation)
Delta = 8*j*s*m + 6*T*j - T**2*u
assert z(sig - (Delta - 2*T*j))
print("symbolic Lemma 1.1(a)(b)(c), discriminant, Lemma 1.3: OK")

# Lemma 1.1(d) and Lemma 3.1 identity contain sqrt(P), sqrt(Q); check them with an independent
# algebraic approach: work in Q(sqrtP, sqrtQ) with sqrtP, sqrtQ symbols, reducing sqrtP^2=P, sqrtQ^2=Q.
sP, sQ = sp.symbols('sP sQ', positive=True)
sd = sP*sQ
zeta = 4*X*sP + u*sQ
zinv = 4*X*sP - u*sQ   # = 1/zeta on solutions
theta = (T/2)*(sd - co*de)/(sd + co*de)
def red(e):
    e = sp.together(e)
    num, den = sp.fraction(e)
    num = sp.expand(num)
    num = sp.Poly(num, sP, sQ)
    # reduce exponents
    out = 0
    for (a1, b1), cf in num.terms():
        out += cf * (P**(a1//2)) * (Q**(b1//2)) * sP**(a1 % 2) * sQ**(b1 % 2)
    return sp.together(out)/den
# rationalise: multiply theta numerator/denominator: (sd-coδ)/(sd+coδ) = (sd-coδ)^2/(d - co^2δ^2)
theta_r = (T/2)*(sd - co*de)**2/(d - co**2*de**2)
assert z(sp.simplify(red((d - co**2*de**2)) - co*T))
jd = u*theta_r - de*sP*zinv          # 1/zeta = zinv
assert z(red(jd - j)), "1.1(d)"
sig31 = 4*u*theta_r**2 - mu*de*sP*zinv
assert z(red(sig31 - sig)), "3.1 identity"
print("Lemma 1.1(d), Lemma 3.1 sigma identity (algebraic, sqrt reduced): OK")

# Prop 2.1 algebra
c0, Tt, dd = sp.symbols('c_o T delta', positive=True)
dpoly = c0**2*dd**2 + c0*Tt
r = sp.symbols('r')
eta_n = (c0*dd)**2 - dpoly
assert sp.expand(eta_n + c0*Tt) == 0
# eps_* = eta^2/(c_o T) = (2 c_o delta^2 + T + 2 delta sqrt d)/T
x_eps = (c0**2*dd**2 + dpoly)/(c0*Tt); y_eps = 2*c0*dd/(c0*Tt)
assert sp.simplify(x_eps - (2*c0*dd**2 + Tt)/Tt) == 0 and sp.simplify(y_eps - 2*dd/Tt) == 0
assert sp.simplify(x_eps**2 - dpoly*y_eps**2 - 1) == 0
# xi = delta c_o + T/(2 delta) + sqrt d ; N(xi) = T^2/(4 delta^2); 2 delta xi / T = eps_*
xi_x = dd*c0 + Tt/(2*dd)
assert sp.simplify(xi_x**2 - dpoly - Tt**2/(4*dd**2)) == 0
assert sp.simplify(2*dd*xi_x/Tt - x_eps) == 0 and sp.simplify(2*dd/Tt - y_eps) == 0
# Schinzel parameters along delta = delta0 + N t
t, N, d0 = sp.symbols('t N delta0')
f = sp.expand(dpoly.subs(dd, d0 + N*t))
A2 = f.coeff(t, 2); B = f.coeff(t, 1); C = f.coeff(t, 0)
assert sp.simplify(A2 - (c0*N)**2) == 0
assert sp.simplify(B - 2*c0**2*d0*N) == 0
assert sp.simplify(B**2 - 4*A2*C + 4*c0**3*Tt*N**2) == 0
print("Prop 2.1 algebra (eps_*, xi, Schinzel coefficients): OK")

# Remark 1.2: L=13, b=1, (c',g,delta,P1,X)=(79,19,1,1,17), a=1
from math import gcd
L, a, b = 13, 1, 1
Tn = 2**(L-4); un = 7**b; cpn, gn, dn, P1n, Xn = 79, 19, 1, 1, 17
con = 7**a*cpn; Mn = con*dn**2 + Tn
assert gn == 4*P1n*Xn - 7**a*un*dn
Q1n = Mn//P1n; Pn = cpn*P1n; Qn = 7**a*Q1n
assert 16*Pn*Xn**2 - Qn*un**2 == 1
yn = cpn*gn*dn; jn = Tn*un//2 - yn; mn = cpn*dn**2
rn = (Tn*un//2 + jn)//P1n; assert (Tn*un//2 + jn) % P1n == 0
assert (rn*jn - mn) % un == 0; ln = (rn*jn - mn)//un
sn = 8*7**a*mn*jn + 4*Tn*jn - Tn**2*un
print("Remark 1.2: j, lambda, sigma =", jn, ln, sn, "; j^2 > m P1:", jn**2 > mn*P1n)
# reconstruct certificate (TYPEI4 Prop 1.2 converse): A = 2 Q u^2 + 1, n = c_o k_o, k_o = X u
An = 2*Qn*un**2 + 1; ko = Xn*un; nn = con*ko
F = An - 8*nn*dn; e = An + 8*nn*dn
print("F, e =", F, e)
assert F*e == 1 + 2**(L+2)*cpn*7**(a+2*b)*Xn**2
assert F % 16 == 7
# near-miss conditions F = -1 mod c'k', F = 1 mod 7^{a+b}
assert (F + 1) % (cpn*Xn) == 0 and (F - 1) % 7**(a+b) == 0
v2 = lambda x: (x & -x).bit_length() - 1
print("v2(F+9), v2(e+9) =", v2(F+9), v2(e+9), "; need >= t >= 2+ceil(L/2) =", 2 + (L+1)//2)
# certificate at x_w for w = -F mod 2^t, all splits alpha+2gamma=L
for gam in range(0, L//2 + 1):
    al = L - 2*gam; tt = 2 + al + gam
    w = (-F) % 2**tt
    assert w % 16 == 9
    print(f"  alpha={al} gamma={gam} t={tt}: certificate at w={w} (w mod 16 = {w%16}); at w=9: {(F+9) % 2**tt == 0 or (e+9) % 2**tt == 0}")
