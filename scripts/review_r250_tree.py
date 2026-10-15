"""review_r250_tree.py (R250, from scratch): the q = 3 (or any odd q), A = T^2, c-slice ball tree with Case A, Case B, I4.
Complete enumerations (proofs of completeness in reviews/ff-inversion-review.md §3):
 Case A (g = 1 gives the maximal balls): on a c-slice E is monic, v_T(E+1) = 1, T^alpha || a1, T not| b1, deg b1 <= alpha-1,
   F := (a1+b1)/E monic of degree <= alpha-1-deg b1, and a1'(K b1 F - T^alpha) = F + b1 with K := (E+1)/(a1' b1).
   So loop alpha, b1, F, monic divisors a1' of F + b1, K = ((F+b1)/a1' + T^alpha)/(b1 F) must be a polynomial.
 I4: the same data (deg a1 > deg b1 automatically), ball u == -1/E mod T^{2+alpha}; each re-checked against the definition
   A a b | e P + 1 at the slice point (T^{2+alpha} | u e + 1, (ab)' | e + 1).
 Case B: E = L'w - 1, E' = L'C - 1, L' = g'm', m'wC = T^s + v, w + C = g'v, T || w, T || C (pure algebra from EE' = D and
   E == E' == -1 mod L'); deg v <= max(a,b) < a + b, so v = (-T^s) mod wC. Loop ordered (w, C) with a + b <= s <= SMAX.
   Largest ball of a tuple: j = ceil((s-2)/2), centre -E mod T^{2+j}.
Every ball is re-verified from the definitions (Case A: E | a1+b1, E == -1 mod (a1b1)', lc; Case B: E | 1 + T^s L'g', monic
cofactor, E == -1 mod L', g' | L'). Survivors per depth with and without I4.
usage: review_r250_tree.py q DMAX"""
import sys, itertools
from review_r250_gf import Field

q, DMAX = int(sys.argv[1]), int(sys.argv[2]); k = 2
F = Field(q); T = (0, 1)


def key(p, m):  # residue mod T^m as tuple of m coefficients
    p = F.mod(p, F.Tpow(m)); return tuple(p) + (0,) * (m - len(p))


# ---------- Case A ----------
caseA = []
for al in range(1, DMAX - k + 1):
    Ta = F.Tpow(al)
    for db in range(0, al):
        for b1 in F.monics(db):
            if b1[0] == 0:
                continue
            for dF in range(0, al - db):
                for Fp in F.monics(dF):
                    sF = F.add(Fp, b1)
                    if not sF:
                        continue
                    for a1p in F.monic_divisors(sF):
                        if a1p[0] == 0:
                            continue
                        Kn, r = F.divmod(F.add(F.exact(sF, a1p), Ta), F.mul(b1, Fp))
                        if r or not Kn:
                            continue
                        E = F.sub(F.mul(Kn, F.mul(a1p, b1)), (1,))
                        a1 = F.mul(Ta, a1p)
                        # verify from the definition
                        if not E or E[-1] != 1 or F.deg(E) < 1:
                            continue
                        if F.vT(F.add(E, (1,))) != 1:
                            continue  # not on a c-slice
                        assert F.mul(E, Fp) == F.add(a1, b1)
                        if len(F.gcd(a1, b1)) != 1:
                            continue  # non-primitive; its reduced datum (a1/h, b1/h, E) is enumerated separately
                        assert not F.mod(F.add(E, (1,)), F.mul(a1p, b1))
                        assert F.deg(a1) > F.deg(b1)
                        caseA.append((al, a1, b1, E))
caseA = sorted(set(caseA))
ballsA = {(key(F.neg(E), k + al), ('A', a1, b1, E)) for (al, a1, b1, E) in caseA}
ballsI4 = set()
for (al, a1, b1, E) in caseA:
    m = k + al
    cen = key(F.neg(F.inv_mod(E, F.Tpow(m))), m)
    # I4 definition at slice point x_u, u = cen: T^{k+v_T(ab)} | u e + 1 and (ab)' | e + 1
    assert key(F.add(F.mul(cen, E), (1,)), m) == (0,) * m
    assert not F.mod(F.add(E, (1,)), F.mul(F.tfree(a1), b1)) and F.divides(E, F.add(a1, b1))
    ballsI4.add((cen, ('I4', a1, b1, E)))

# ---------- Case B ----------
SMAX = k + 2 * (DMAX - k)
def ws(a):  # monic w of degree a with T || w
    for w1 in F.monics(a - 1):
        if w1[0] != 0:
            yield F.mul(T, w1)
ballsB = set()
for t in range(2, SMAX + 1):
    for a in range(1, t):
        b = t - a
        for w in ws(a):
            for C in ws(b):
                wC = F.mul(w, C); wpC = F.add(w, C)
                vs = F.mod(F.neg(F.Tpow(t)), wC)
                for s in range(t, SMAX + 1):
                    if s > t:
                        vs = F.mod(F.mul(T, vs), wC)
                    v = vs
                    if not v or F.vT(v) < 2:
                        continue
                    gq, r = F.divmod(wpC, v)
                    if r or not gq or gq[-1] != 1 or gq[0] == 0:
                        continue
                    gp = gq; mp = F.exact(F.add(F.Tpow(s), v), wC)
                    if mp[-1] != 1 or mp[0] == 0:
                        continue
                    Lp = F.mul(gp, mp); E = F.sub(F.mul(Lp, w), (1,)); Ep = F.sub(F.mul(Lp, C), (1,))
                    Dp = F.add((1,), F.mul(F.Tpow(s), F.mul(Lp, gp)))
                    assert F.mul(E, Ep) == Dp and E[-1] == 1 and Ep[-1] == 1
                    j = (s - k + 1) // 2
                    if k + j > DMAX:
                        continue
                    ballsB.add((key(F.neg(E), k + j), ('B', s, w, C, gp, mp)))


def ball_set(bs):
    return {b for (b, _) in bs}


def contains(big, small):  # balls as residue tuples (big has smaller or equal length)
    return len(big) <= len(small) and small[:len(big)] == big


def survivors(balls, c, d):
    cnt = 0
    for tail in itertools.product(range(q), repeat=d - 2):
        u = (1, c) + tail
        if not any(contains(b, u) for b in balls if len(b) <= d):
            cnt += 1
    return cnt


A_, B_, I_ = ball_set(ballsA), ball_set(ballsB), ball_set(ballsI4)
inv = lambda b: key(F.inv_mod(b, F.Tpow(len(b))), len(b))
print("q=%d k=2 c-slices, ball depth <= %d" % (q, DMAX))
print("Case A data %d, balls %d; I4 balls %d; Case B balls %d; |A cap B| = %d" % (len(caseA), len(A_), len(I_), len(B_), len(A_ & B_)))
for name, S in [('A', A_), ('B', B_), ('I4', I_), ('A+B', A_ | B_), ('A+B+I4', A_ | B_ | I_)]:
    print("  %-7s balls %4d, without inverse ball: %d" % (name, len(S), sum(1 for b in S if inv(b) not in S)))
print("  A balls inside a Case B ball: %d/%d; I4 balls inside a Case B ball: %d/%d"
      % (sum(any(contains(x, b) for x in B_) for b in A_), len(A_), sum(any(contains(x, b) for x in B_) for b in I_), len(I_)))
for c in range(1, q):
    s1 = [survivors(A_ | B_, c, d) for d in range(3, DMAX + 1)]
    s2 = [survivors(A_ | B_ | I_, c, d) for d in range(3, DMAX + 1)]
    xs = (1, c) + (0,) * (DMAX - 2)
    print("  c=%d survivors d3..d%d  A+B: %s  A+B+I4: %s  x*_c alive: %s" % (c, DMAX, s1, s2, not any(contains(b, xs) for b in A_ | B_ | I_)))
