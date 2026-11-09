"""NL7 Corollary 3.6: search for a quartic norm curve P(t) = N_{Q(zeta_8)/Q}(t + alpha), alpha = x*zeta + y*i + z*zeta^3
(trace 0, so P = t^4 + c2 t^2 + c1 t + c0 is monic and depressed) that satisfies (IRR) and (LC).
  c2 = 4xz + 2y^2,  c1 = 4y(z^2 - x^2),  c0 = (2xz - y^2)^2 + (z^2 - x^2)^2.
(IRR-a)  P + mu irreducible for all integers mu >= 1:  a factorisation (t^2+ut+v)(t^2-ut+w) over Z needs u | c1,
         v = (c2 + u^2 - c1/u)/2, w = (c2 + u^2 + c1/u)/2 integers and mu = v*w - c0 >= 1   (finite check).
(IRR-b)  mu P + 1 irreducible for all mu >= 1:  reducibility forces coprime r, s != 0 with
         H(r,s) = C(r^2, s^2) a positive divisor of 4 c1^2,  C(R,S) = R^3 + 2 c2 R^2 S + (c2^2 - 4 c0) R S^2 - c1^2 S^3.
         C(R,S) = h is solved for every h | 4 c1^2 by PARI's thue (thueinit flag 1: unconditional) when C is
         irreducible; solutions with R, S positive perfect squares would be the exceptions.
(LC)     for every prime l <= 61 and every l | disc(P): some t with P(t) a nonzero square mod l (l odd), P(t) = 1 mod 8
         (l = 2).  (For l >= 17, l not dividing 2*disc, existence is automatic by Hasse-Weil, Prop 3.4 Step 3.)
Also a brute-force cross-check: factor P + mu and mu*P + 1 over Q for 1 <= mu <= MU.
"""
import sys
from math import isqrt, gcd
from sympy import symbols, Poly, factor_list, divisors, primerange, discriminant, factorint
from cypari import pari

t = symbols('t')
MU = 400

def is_square(n):
    return n >= 0 and isqrt(n) ** 2 == n

def check(x, y, z, verbose=False):
    c2, c1, c0 = 4*x*z + 2*y*y, 4*y*(z*z - x*x), (2*x*z - y*y)**2 + (z*z - x*x)**2
    if c1 == 0:
        return None
    P = Poly(t**4 + c2*t**2 + c1*t + c0, t)
    if not P.is_irreducible:
        return None
    # (IRR-a)
    bad_a = []
    for u in divisors(abs(c1)):
        for su in (u, -u):
            num_v, num_w = c2 + su*su - c1 // su, c2 + su*su + c1 // su
            if num_v % 2 == 0 and num_w % 2 == 0:
                v, w = num_v // 2, num_w // 2
                mu = v * w - c0
                if mu >= 1:
                    bad_a.append((mu, su, v, w))
    if bad_a:
        return ('IRR-a fails', (c2, c1, c0), sorted(set(b[0] for b in bad_a)))
    # (IRR-b)
    C = f"x^3 + {2*c2}*x^2 + {c2*c2 - 4*c0}*x - {c1*c1}"
    if not pari(f"polisirreducible({C})"):
        return ('C reducible (skipped)', (c2, c1, c0), None)
    th = pari(f"thueinit({C}, 1)")
    bad_b = []
    for h in divisors(4 * c1 * c1):
        for sol in pari.thue(th, h):
            R, S = int(sol[0]), int(sol[1])
            if R > 0 and S > 0 and is_square(R) and is_square(S):
                bad_b.append((h, R, S))
    if bad_b:
        return ('IRR-b fails', (c2, c1, c0), bad_b)
    # (LC)
    disc = int(discriminant(P.as_expr(), t))
    lc_primes = sorted(set(list(primerange(3, 62)) + [q for q in factorint(abs(disc)) if q > 2]))
    f = lambda n: n**4 + c2*n*n + c1*n + c0
    if not any(f(r) % 8 == 1 for r in range(8)):
        return ('LC fails at 2', (c2, c1, c0), None)
    r2 = [r for r in range(8) if f(r) % 8 == 1]
    lcw = {2: r2[0]}
    for l in lc_primes:
        ok = [r for r in range(l) if f(r) % l != 0 and pow(f(r) % l, (l - 1) // 2, l) == 1]
        if not ok:
            return (f'LC fails at {l}', (c2, c1, c0), None)
        lcw[l] = ok[0]
    # brute-force cross-check of (IRR) for small mu
    for mu in range(1, MU + 1):
        for Q in (P.as_expr() + mu, mu * P.as_expr() + 1):
            fl = factor_list(Q, t)[1]
            assert len(fl) == 1 and fl[0][1] == 1, (x, y, z, mu)
    return ('OK', (c2, c1, c0), {'disc': disc, 'r_l': lcw})

if __name__ == '__main__':
    B = int(sys.argv[1]) if len(sys.argv) > 1 else 4
    found = 0
    for x in range(-B, B + 1):
        for y in range(1, B + 1):
            for z in range(0, B + 1):
                if gcd(gcd(x, y), z) != 1:
                    continue
                res = check(x, y, z)
                if res is None:
                    continue
                if res[0] == 'OK':
                    found += 1
                    c2, c1, c0 = res[1]
                    print(f"OK  alpha = {x}*zeta + {y}*i + {z}*zeta^3 : P = t^4 + {c2} t^2 + {c1} t + {c0}; disc = {res[2]['disc']}; LC witnesses r_l: {res[2]['r_l']}")
                    if found >= 6:
                        sys.exit(0)
                elif B <= 2:
                    print(res[0], (x, y, z), res[1], res[2])
