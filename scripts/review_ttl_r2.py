"""R111 round 2, from-scratch checks.
(1) e-cusp main term of (b2)/(b5): N(q) = #{(a,e): A<=a<2A, E<=e<2E, e | 4a^2d+1, q | 4acd - f}, f = (4a^2d+1)/e,
    with E <= 4A (lambda = A/(qE) possibly > 1) vs g_{c,d}(q) N(1).
(2) Lemma 8.3(c): T(D,F) := D^{-1} sum_{d~D} g(d) sum_{f~F} rho_d(f)/phi(f) stays bounded, F from 1 to >> D.
"""
import sys, math
from sympy import legendre_symbol, divisors, totient, factorint
from sympy.ntheory import sqrt_mod

def g_cd(l, c, d):
    chi = legendre_symbol((-d) % l, l)
    return (1 + chi)/(l + chi) if c % l == 0 else (l - 1)/(l*l + chi*l)

def ecusp(A, d, E, cs=(1, 3), qs=(3, 5, 7, 11, 13, 17)):
    pairs = []
    for a in range(A, 2*A):
        M = 4*a*a*d + 1
        for e in divisors(M):
            if E <= e < 2*E:
                pairs.append((a, e, M//e))
    n1 = len(pairs)
    out = [f"d={d} A={A} E={E} (A/E={A/E:.2f}) N(1)={n1}"]
    for c in cs:
        row = []
        for q in qs:
            if (2*d) % q == 0: continue
            nq = sum(1 for (a, e, f) in pairs if (4*a*c*d - f) % q == 0)
            pred = g_cd(q, c, d)*n1
            row.append(f"q={q}:{(nq-pred)/math.sqrt(pred+1):+.1f}sd")
        out.append(f"  c={c}: " + " ".join(row))
    print("\n".join(out))

def rho(d, f):
    r = 1
    for p, k in factorint(f).items():
        if p == 2 or d % p == 0: return 0
        r *= 1 + legendre_symbol((-d) % p, p)
    return r

def lemma83c(D, F):
    s = 0.0
    phis = {f: int(totient(f)) for f in range(F, 2*F)}
    for d in range(D, 2*D):
        gd = d/int(totient(d))
        s += gd*sum(rho(d, f)/phis[f] for f in range(F, 2*F))
    return s/D

if __name__ == "__main__":
    for (A, d, E) in [(20000, 101, 5000), (20000, 101, 40000), (20000, 1009, 2000), (20000, 1009, 60000)]:
        ecusp(A, d, E)
    for D in [50, 400]:
        print(f"Lemma 8.3(c) D={D}: " + " ".join(f"F={F}:{lemma83c(D, F):.3f}" for F in [1, 4, 30, 300, 3000]))
