"""R89: check of POINTWISE_TYPEI4 Lemma 3.6 (L=7 tower).  (1) symbolic: (3.1) with m = rho j - lam u <=> (3.2),
the quadratic, the resultant constant C, and the j=1 reductions; (2) brute force over generic integers:
all (u, j, m, A, rho) with u in [1,Umax], A in {1,7,49}, gcd(j,u)=1, j odd < 4u, m odd, m j A < 8u, satisfying (3.1)
(rho integer >= 1) -- check lam integer, even, lam <= 4j + j^2/u, (3.2), the explicit bounds and the quadratic
(7^e := u/A as a rational).  Here u need not be a power of 7 (so lam = 0 is not excluded and is only reported)."""
import sys
from fractions import Fraction as Fr
from math import gcd
import sympy as sp
u, j, m, A, rho, lam = sp.symbols('u j m A rho lam')
eq31 = rho * ((4*u - j)**2 - 2*m*j*A*u) - m*(4*u + j)
eq32 = u*(16*rho + 4*lam) - j*(12*rho + 2*A*rho*m - lam)
sub = {m: rho*j - lam*u}
print("(3.1)|_{m=rho j - lam u} - u*(3.2)|_{m=...} =", sp.expand(eq31.subs(sub) + u*eq32.subs(sub)))
E = sp.symbols('E')  # 7^e, with A*E = u
quad = (2*j*m - 16*E)*lam*u**2 + (2*j*m**2 - 16*E*m + 8*E*lam*j)*u + E*(12*j*m - lam*j**2)
# quad should equal j*E*(3.2) after rho = (m + lam u)/j and A = u/E
q2 = sp.expand(j*E*eq32.subs({rho: (m + lam*u)/j, A: u/E}))
print("quad - (-j E (3.2)) =", sp.simplify(quad + q2), "| quad - (+...) =", sp.simplify(quad - q2))
A1 = 2*A*lam*j + 16
Nn = 2*A*j**2*rho**2 + 12*j*rho - lam*j
Dd = A1*rho + 4*lam
C = -lam*j*(4*A**2*lam**2*j**2 + 128*A*lam*j + 1024)
r = sp.rem(sp.expand(A1**2*Nn - C), sp.expand(Dd), rho)
print("A1^2 Nn - C mod Dd (in rho) =", sp.simplify(r))
print("u*Dd - Nn under m=rho j - lam u vs (3.2):", sp.expand((u*Dd - Nn) + eq32.subs(m, rho*j - lam*u)))
for lv in (2, 4):
    e = sp.expand(eq32.subs({j: 1, lam: lv, rho: m + lv*u}))
    print("j=1, lam=%d:" % lv, sp.factor(e))
Umax = int(sys.argv[1]) if len(sys.argv) > 1 else 400
cnt = bad = lam0 = 0
for uu in range(1, Umax + 1):
    for AA in (7, 343):
        for jj in range(1, 4*uu, 2):
            if gcd(jj, uu) != 1: continue
            mm = 1
            while mm * jj * AA < 8*uu:
                den = (4*uu - jj)**2 - 2*mm*jj*AA*uu
                num = mm*(4*uu + jj)
                if den > 0 and num % den == 0:
                    rr = num // den; cnt += 1
                    ok = (rr*jj - mm) % uu == 0
                    L_ = (rr*jj - mm) // uu
                    ok &= L_ % 2 == 0 and L_ >= 0 and Fr(L_) <= 4*jj + Fr(jj*jj, uu)
                    ok &= uu*(16*rr + 4*L_) == jj*(12*rr + 2*AA*rr*mm - L_)
                    if L_ == 0: lam0 += 1
                    else:
                        ok &= rr < 2*AA*L_**2*jj**2 + 64*L_*jj + Fr(512, AA)
                        ok &= Fr(uu, AA) < 2*L_*jj**3 + 10*jj**2 + 37*jj
                        EE = Fr(uu, AA)
                        qv = (2*jj*mm - 16*EE)*L_*uu**2 + (2*jj*mm**2 - 16*EE*mm + 8*EE*L_*jj)*uu + EE*(12*jj*mm - L_*jj*jj)
                        ok &= qv == 0 and 2*jj*mm != 16*EE
                    if not ok:
                        bad += 1; print("BAD", uu, AA, jj, mm, rr, L_)
                mm += 2
print("brute: solutions of (3.1)", cnt, "lam=0 cases", lam0, "failures", bad)
