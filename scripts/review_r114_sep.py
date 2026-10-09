"""R114 from-scratch checks for paper/es-typei-heegner-note.tex.

(1) Lemma 2.2: distinct Q,Q' in F_d = {[A,B,C]: B^2-4AC=-4d, A>0, 2d|B, d|C}
    have cosh dist(z_Q,z_Q') >= 3/2.  Computed from the points themselves
    (not via Lemma 2.1): z = (-B + 2i sqrt d)/(2A), Im z = sqrt(d)/A, and
    cosh dist - 1 = |z-w|^2/(2 Im z Im w), all exact in Q.
    Also checks Lemma 2.1's formula disc(Q-Q')/(2|D|) on the same pairs,
    sharpness of 3/2 and the Type I subset minimum.
(2) Lemma 2.2-adjacent: invariance of F_d^I (4d | B) under Gamma^0(2d) cap Gamma_0(2)
    (z-side), and of q | cB-A under the z-matrices of Gamma_0(2d) cap Gamma(2q).
(3) Section 6 densities g_{c,d}(l) and the kappa_c deviation by brute force over F_l^3.
(4) Lemma 6.3: #{(t:s) in P^1(Z/d): Q0(t,s)=0 mod d} <= r(d) for reduced primitive Q0.
(5) Lemma 1.1 identity sum_{j,k<=L} min(1/j,1/k) = sum_h (2h-1)/h.
Memory: tiny (d<=60, A<=60).
"""
from fractions import Fraction as Fr
from math import gcd, isqrt
import itertools, random, sys


def forms_Fd(d, Amax, Bmax):
    out = []
    for A in range(1, Amax + 1):
        for B in range(-Bmax, Bmax + 1):
            if B % (2 * d):
                continue
            num = B * B + 4 * d
            if num % (4 * A):
                continue
            C = num // (4 * A)
            if C % d:
                continue
            out.append((A, B, C))
    return out


def cosh_minus_1(Q, R, d):
    A, B, _ = Q
    A2, B2, _ = R
    dx = Fr(-B, 2 * A) - Fr(-B2, 2 * A2)
    # (Im z - Im w)^2 = d (1/A - 1/A2)^2 ; Im z Im w = d/(A A2)
    num = dx * dx + d * (Fr(1, A) - Fr(1, A2)) ** 2
    return num / (2 * Fr(d, A * A2))


def disc(Q):
    A, B, C = Q
    return B * B - 4 * A * C


def check_separation(dmax=60, Amax=60):
    worst = Fr(10**9)
    sharp = []
    typei_min = Fr(10**9)
    npairs = 0
    for d in range(1, dmax + 1):
        F = forms_Fd(d, Amax, 2 * d * Amax)
        for Q, R in itertools.combinations(F, 2):
            v = cosh_minus_1(Q, R, d)
            npairs += 1
            diff = tuple(x - y for x, y in zip(Q, R))
            assert v == Fr(disc(diff), 8 * d), (d, Q, R)  # Lemma 2.1 with |D|=4d
            if v < worst:
                worst = v
            if v == Fr(1, 2):
                sharp.append(d)
            if Q[1] % (4 * d) == 0 and R[1] % (4 * d) == 0:
                typei_min = min(typei_min, v)
    return npairs, worst, sorted(set(sharp)), typei_min


def rand_sl2(mod_conds, rng, tries=10000):
    # random SL2(Z) matrices satisfying predicate mod_conds
    for _ in range(tries):
        p, t = rng.randint(-30, 30), rng.randint(-30, 30)
        if gcd(p, t) != 1:
            continue
        # find r,s with ps - tr = 1
        g, x, y = egcd(p, -t)  # p*x + (-t)*y = 1 -> s=x, r=y
        s, r = x, y
        k = rng.randint(-5, 5)
        s, r = s + k * t, r + k * p
        if p * s - t * r != 1:
            continue
        if mod_conds(p, t, r, s):
            return p, t, r, s
    return None


def egcd(a, b):
    if b == 0:
        return (a, 1, 0) if a >= 0 else (-a, -1, 0)
    g, x, y = egcd(b, a % b)
    return g, y, x - (a // b) * y


def act(Q, g):
    # Q o gamma, gamma = [[p,t],[r,s]] : Q(pX+tY, rX+sY)
    A, B, C = Q
    p, t, r, s = g
    A2 = A * p * p + B * p * r + C * r * r
    B2 = 2 * A * p * t + B * (p * s + t * r) + 2 * C * r * s
    C2 = A * t * t + B * t * s + C * s * s
    return A2, B2, C2


def check_groups(rng):
    bad1 = bad2 = 0
    n = 0
    for d in range(1, 31):
        FI = [Q for Q in forms_Fd(d, 40, 8 * d * 40) if Q[1] % (4 * d) == 0]
        # z-side group Gamma^0(2d) cap Gamma_0(2): 2d | t, 2 | r
        for _ in range(40):
            g = rand_sl2(lambda p, t, r, s: t % (2 * d) == 0 and r % 2 == 0, rng)
            if g is None:
                continue
            for Q in FI[:20]:
                Q2 = act(Q, g)
                n += 1
                if not (Q2[1] % (4 * d) == 0 and Q2[2] % d == 0 and disc(Q2) == -4 * d):
                    bad1 += 1
        # sieve: w-side Gamma_0(2d) cap Gamma(2q); z-matrix [[p, d t],[r/d, s]]
        for q in (3, 5, 7, 15, 21):
            if gcd(q, d) != 1:
                continue
            for _ in range(10):
                g = rand_sl2(lambda p, t, r, s: r % (2 * d * q) == 0 and t % (2 * q) == 0
                             and (p - 1) % (2 * q) == 0 and (s - 1) % (2 * q) == 0, rng)
                if g is None:
                    continue
                p, t, r, s = g
                gz = (p, d * t, r // d, s)
                for Q in FI[:20]:
                    Q2 = act(Q, gz)
                    for c in (1, 2, 3):
                        if (c * Q[1] - Q[0] - (c * Q2[1] - Q2[0])) % q:
                            bad2 += 1
    return n, bad1, bad2


def legendre(a, l):
    a %= l
    if a == 0:
        return 0
    return 1 if pow(a, (l - 1) // 2, l) == 1 else -1


def check_density():
    rows = []
    for l in (3, 5, 7, 11, 13):
        for d in range(1, 30):
            if d % l == 0:
                continue
            chi = legendre(-d, l)
            quad = [(A, B, C) for A in range(l) for B in range(l) for C in range(l)
                    if (B * B - 4 * A * C + 4 * d) % l == 0]
            assert len(quad) == l * l + chi * l
            for c in (1, l):
                sat = sum(1 for (A, B, C) in quad if (c * B - A) % l == 0)
                g = Fr(sat, len(quad))
                pred = Fr(l - 1, l * l + chi * l) if c % l else Fr(1 + chi, l + chi)
                assert g == pred, (l, d, c, g, pred)
                sl2 = l * (l * l - 1)
                rows.append((l, chi, c % l == 0, g * sl2))
                # bound used in Thm 6.2 proof
                lim = l * l if c % l else 2 * l * l
                assert g * sl2 <= lim
    # the deviation: l | c, chi = 1 gives 2 l (l-1) > l^2
    dev = sorted({(l, int(v)) for (l, chi, lc, v) in rows if lc and chi == 1})
    return dev


def r_of(d):
    r, m, p = 1, d, 2
    while p * p <= m:
        k = 0
        while m % p == 0:
            m //= p
            k += 1
        r *= p ** (k // 2)
        p += 1
    return r


def P1(d):
    pts = set()
    for t in range(d):
        for s in range(d):
            if gcd(gcd(t, s), d) != 1:
                continue
            # canonical rep: smallest (t*u, s*u) over units u
            rep = min(((t * u) % d, (s * u) % d) for u in range(1, d + 1) if gcd(u, d) == 1)
            pts.add(rep)
    return pts


def check_L63(dmax=80):
    worst = 0
    for d in range(1, dmax + 1):
        pts = P1(d) if d > 1 else {(0, 0)}
        # reduced primitive forms of disc -4d
        for A in range(1, isqrt(4 * d // 3) + 2):
            for B in range(-A, A + 1, 1):
                if B % 2:
                    continue
                num = B * B + 4 * d
                if num % (4 * A):
                    continue
                C = num // (4 * A)
                if C < A or gcd(gcd(A, B), C) != 1:
                    continue
                cnt = sum(1 for (t, s) in pts if (A * t * t + B * t * s + C * s * s) % d == 0)
                worst = max(worst, Fr(cnt, r_of(d)))
                assert cnt <= r_of(d), (d, A, B, C, cnt)
    return worst


def check_L11(L=200):
    for n in range(1, L + 1):
        lhs = sum(Fr(1, max(j, k)) for j in range(1, n + 1) for k in range(1, n + 1))
        rhs = sum(Fr(2 * h - 1, h) for h in range(1, n + 1))
        assert lhs == rhs and rhs <= 2 * n
    return True


if __name__ == "__main__":
    rng = random.Random(114)
    npairs, worst, sharp, tmin = check_separation()
    print(f"[L2.2] pairs={npairs} min(cosh-1)={worst}  -> min cosh = {1+worst}")
    print(f"[L2.2] d attaining cosh=3/2 (sharp): {sharp[:20]}")
    print(f"[L2.2] Type I subset (4d|B): min cosh = {1+tmin}")
    print(f"[L2.1] formula cosh-1 = disc(Q-Q')/(8d) verified on all pairs")
    n, b1, b2 = check_groups(rng)
    print(f"[groups] tested {n}: parity failures={b1}, sieve-functional failures={b2}")
    dev = check_density()
    print(f"[sec6] densities g_(c,d) verified; l|c & chi=1 gives |SL2|g = 2l(l-1): {dev}")
    print(f"[L6.3] max P1-root count / r(d) over reduced primitive forms, d<=80: {check_L63()}")
    print(f"[L1.1] identity and <=2L verified up to L=200: {check_L11()}")
