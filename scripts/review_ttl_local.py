"""R111 from-scratch local checks.
(a) Lemma 6.1: SL2(F_l) acting on binary forms by Q o g is transitive on {B^2-4AC = -4d} (l odd, l∤d).
(b) g_{c,d}(l) formulas of Sec 6.
(c) g'_{c,a}(l) of Prop 7.1.
(d) Lemma 6.3: r(d) = #{(t:s) in P^1(Z/d): Q0(t,s) = 0 mod d} <= prod p^{floor(k/2)} (and the 4x for p=2)
    over all primitive forms of disc -4d.
"""
import math, itertools
from sympy import factorint, legendre_symbol

def sl2(l):
    return [(p, t, r, s) for p in range(l) for t in range(l) for r in range(l) for s in range(l)
            if (p*s - t*r) % l == 1]

def act(Q, g, m):
    A, B, C = Q; p, t, r, s = g
    return ((A*p*p + B*p*r + C*r*r) % m, (2*A*p*t + B*(p*s + t*r) + 2*C*r*s) % m,
            (A*t*t + B*t*s + C*s*s) % m)

def check_local(lmax=23):
    for l in [3, 5, 7, 11, 13, 17, 19, 23]:
        if l > lmax: break
        G = sl2(l)
        for d in range(1, 3*l):
            if d % l == 0: continue
            quad = [(A, B, C) for A in range(l) for B in range(l) for C in range(l)
                    if (B*B - 4*A*C + 4*d) % l == 0]
            chi = legendre_symbol((-d) % l, l)
            assert len(quad) == l*l + chi*l, (l, d)
            orb = {act(quad[0], g, l) for g in G}
            assert len(orb) == len(quad), ("not transitive", l, d)
            for c in range(0, l):
                num = sum(1 for (A, B, C) in quad if (c*B - A) % l == 0)
                g = num / len(quad)
                pred = (l - 1)/(l*l + chi*l) if c % l else (1 + chi)/(l + chi)
                assert abs(g - pred) < 1e-12, (l, d, c, g, pred)
    print("(a),(b) transitivity, |quadric| = l^2+chi*l, g_{c,d} formulas: OK for l<=%d" % lmax)
    for l in [3, 5, 7, 11, 13]:
        for a in range(1, 2*l):
            if a % l == 0: continue
            for c in range(0, l):
                num = sum(1 for e in range(l) for f in range(l) if (f*(c*e - a) - c) % l == 0)
                pred = (l - 1)/l**2 if c % l else 1/l
                assert abs(num/l**2 - pred) < 1e-12, (l, a, c)
    print("(c) g'_{c,a}(l) formula OK")

def prim_forms(D):
    """all primitive reduced positive definite forms of discriminant D<0 (one per SL2(Z)-class)."""
    out = []
    a = 1
    while 3*a*a <= -D:
        for b in range(-a+1, a+1):
            if (b*b - D) % (4*a): continue
            c = (b*b - D)//(4*a)
            if c < a: continue
            if b < 0 and (a == c): continue
            if math.gcd(math.gcd(a, abs(b)), c) != 1: continue
            out.append((a, b, c))
        a += 1
    return out

def P1(d):
    pts = set()
    for t in range(d):
        for s in range(d):
            if math.gcd(math.gcd(t, s), d) != 1: continue
            # normalise by units
            best = min(((u*t) % d, (u*s) % d) for u in range(1, d+1) if math.gcd(u, d) == 1)
            pts.add(best)
    return pts

def check_rd(dmax=150):
    worst = 0; worst2 = None
    for d in range(1, dmax+1):
        pts = P1(d)
        rb = 1
        for p, k in factorint(d).items():
            rb *= p**(k//2)
        for Q in prim_forms(-4*d):
            A, B, C = Q
            r = sum(1 for (t, s) in pts if (A*t*t + B*t*s + C*s*s) % d == 0)
            assert r <= 4*rb, (d, Q, r, rb)
            if r > rb:
                worst2 = (d, Q, r, rb)
            worst = max(worst, r/rb)
    print("(d) max r(d)/prod p^floor(k/2) over primitive forms, d<=%d: %s; case exceeding without the 4:" % (dmax, worst), worst2)

if __name__ == "__main__":
    check_local()
    check_rd()
