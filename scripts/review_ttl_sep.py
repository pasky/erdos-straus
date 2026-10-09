"""R111 from-scratch checks: Lemma 2.1 (distance formula), Lemma 2.2 (separation), and the
invariance group of the Type I forms (Sec 6 'Parity').  Exact integer arithmetic.

F_d = {[A,B,C]: B^2-4AC=-4d, A>0, B = 0 mod 2d, C = 0 mod d}.
Type I subset: [f, 4ad, de] with ef - 4a^2 d = 1.
cosh dist(z_Q,z_Q') - 1 = disc(Q-Q')/(2|D|) claimed; we check against the direct formula.
"""
import math, itertools, sys
from fractions import Fraction as Fr

def forms_Fd(d, Amax, Bwin):
    """all Q in F_d with A <= Amax and |B| <= Bwin (B = 0 mod 2d)."""
    out = []
    for A in range(1, Amax + 1):
        for B in range(-Bwin - (Bwin % (2*d)), Bwin + 1, 2 * d):
            if B % (2*d):
                continue
            num = B * B + 4 * d
            if num % (4 * A):
                continue
            C = num // (4 * A)
            if C % d == 0:
                out.append((A, B, C))
    return out

def cosh_direct(Q, R, d):
    # z = (-B + i sqrt(4d))/(2A); cosh = 1 + |z-w|^2/(2 Im z Im w), exact via rationals in sqrt
    A, B, C = Q; A2, B2, C2 = R
    # |z-w|^2 = ((-B/2A)+(B2/2A2))^2 + 4d (1/(2A)-1/(2A2))^2 ; Im z Im w = 4d/(4 A A2)
    dx = Fr(-B, 2*A) + Fr(B2, 2*A2)
    dy2 = 4*d*(Fr(1, 2*A) - Fr(1, 2*A2))**2
    return 1 + (dx*dx + dy2) / (2 * Fr(4*d, 4*A*A2))

def disc_diff(Q, R):
    a, b, c = (Q[0]-R[0], Q[1]-R[1], Q[2]-R[2])
    return b*b - 4*a*c

def main(dmax=40, Amax=60):
    worst = None
    hist = {}
    for d in range(1, dmax + 1):
        F = forms_Fd(d, Amax, 2 * d * Amax)
        for Q, R in itertools.combinations(F, 2):
            ch = cosh_direct(Q, R, d)
            dd = disc_diff(Q, R)
            assert ch - 1 == Fr(dd, 8 * d), (d, Q, R)      # Lemma 2.1 with |D| = 4d
            assert dd % (4 * d) == 0, (d, Q, R)            # 4d | disc(Q-Q')
            assert ch >= Fr(3, 2)
            hist[ch] = hist.get(ch, 0) + 1
            if worst is None or ch < worst[0]:
                worst = (ch, d, Q, R)
    print("Lemma 2.1 identity and 4d|disc(Q-Q') verified for all pairs, d<=%d, A<=%d" % (dmax, Amax))
    print("min cosh over F_d pairs:", worst)
    print("smallest cosh values:", sorted(hist)[:5])
    # which d attain cosh = 3/2 ?
    att = sorted({dd for dd in range(1, dmax+1)
                  for Q, R in itertools.combinations(forms_Fd(dd, Amax, 2*dd*Amax), 2)
                  if cosh_direct(Q, R, dd) == Fr(3, 2)})
    print("d attaining cosh=3/2 within window:", att[:20])
    # same restricted to Type I forms (B = 0 mod 4d)
    w1 = None
    for d in range(1, dmax+1):
        F = [Q for Q in forms_Fd(d, Amax, 2*d*Amax) if Q[1] % (4*d) == 0]
        for Q, R in itertools.combinations(F, 2):
            ch = cosh_direct(Q, R, d)
            if w1 is None or ch < w1[0]:
                w1 = (ch, d, Q, R)
    print("min cosh over Type I pairs:", w1)

def act(Q, g):
    """Q o g : (X,Y) -> Q(pX+tY, rX+sY), g = (p,t,r,s)."""
    A, B, C = Q; p, t, r, s = g
    A2 = A*p*p + B*p*r + C*r*r
    B2 = 2*A*p*t + B*(p*s + t*r) + 2*C*r*s
    C2 = A*t*t + B*t*s + C*s*s
    return (A2, B2, C2)

def is_typeI(Q, d):
    A, B, C = Q
    return A > 0 and B % (4*d) == 0 and C % d == 0 and C > 0

def group_check(dmax=30):
    """z-side: Q o g for g in Gamma^0(2d) cap Gamma_0(2) (t = 0 mod 2d, r = 0 mod 2) preserves Type I
    forms; and the R1 counterexample d=2, g=[[1,0],[2,1]] (z-side lower-left 2: this is the w-side
    image of Gamma_0(d) cap Gamma(2) failing)."""
    import random
    random.seed(1)
    bad = 0
    for d in range(1, dmax+1):
        F = [Q for Q in forms_Fd(d, 40, 2*d*40) if Q[1] % (4*d) == 0]
        for _ in range(200):
            # random element with t = 0 mod 2d, r = 0 mod 2
            while True:
                t = 2*d*random.randint(-3, 3); r = 2*random.randint(-5, 5)
                p = random.randint(-9, 9)
                if p == 0: continue
                # solve ps - tr = 1 for s
                if (1 + t*r) % p == 0:
                    s = (1 + t*r)//p; break
            for Q in F[:20]:
                Q2 = act(Q, (p, t, r, s))
                if not is_typeI(Q2, d):
                    bad += 1
    print("Gamma^0(2d) cap Gamma_0(2) (z-side) invariance failures:", bad)
    # w-side Gamma_0(d) cap Gamma(2) element [[1,0],[2d? ]] -> z-side conj by diag(d,1)
    # w = z/d ; g_w = [[p,t],[r,s]] corresponds to g_z = [[p, d t],[r/d, s]]
    # Gamma_0(d)cap Gamma(2) w-side, d=2: g_w=[[1,0],[2,1]]?  r=2 = 0 mod d=2, = 0 mod 2: in group.
    gz = (1, 0, 1, 1)   # r/d = 1
    Q = (1, 8, 18)      # f=1, a=1, d=2, e=9: ef-4a^2d = 9-8 = 1
    print("d=2: [1,8,18] o g_z =", act(Q, gz), " (R1 claims B=44 for the w-side element [[1,0],[2,1]])")

if __name__ == "__main__":
    main(int(sys.argv[1]) if len(sys.argv) > 1 else 30, 40)
    group_check()
