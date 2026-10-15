"""review_r250_domination.py (R250, from scratch): brute-force check of FF_INVERSION_CHECK Lemmas 2.2-2.4 / Thm 2.5.
Enumerate all coprime monic (a1, b1) with deg <= D and every monic E | a1 + b1 (T-free, deg E >= 1, E == -1 mod (a1 b1)'),
i.e. every Case A datum with g = 1 (= every I4 datum (a, b, e) = (a1, b1, E) with gcd(a,b) = 1 when deg a1 != deg b1),
with ball depth k + alpha <= DMAX, alpha = v_T(a1 b1). Slice filter MODE:
  c   : centre -E on a c-slice (u == 1 + cT mod T^2, c != 0), k >= 2;
  k1  : k = 1, u0 = -E(0) not in F_3^*;
  all : every unit u.
For each datum: (i) the I4 ball (u == -1/E mod T^{k+alpha}) is the inverse of the Case A ball (Lemma 2.2, by definition);
(ii) if Lemma 2.3's hypotheses hold, build its Case B datum and check E | D, D monic, D/E monic, g' | L', T not| L',
E == -1 mod L', j <= alpha (ball containment), and the swapped datum E' = D/E (Lemma 2.4) has a ball containing the I4 ball;
(iii) END-TO-END (no use of FE3 Lemma 1.1): pick polynomials P in the Case A ball and P' in the I4 ball, == 1 modulo all
relevant T-free moduli, of large degree, and check that the Case A family, the Case B family of Lemma 2.3, the I4 family and
the swapped Case B family all produce actual monic solutions A/P = 1/X + 1/Y + 1/Z. With PRIME=1 the P are irreducible.
usage: review_r250_domination.py q k MODE D DMAX [PRIME]"""
import sys, random
from review_r250_gf import Field

q, k = int(sys.argv[1]), int(sys.argv[2]); MODE = sys.argv[3]; D, DMAX = int(sys.argv[4]), int(sys.argv[5])
PRIME = len(sys.argv) > 6 and sys.argv[6] == '1'
F = Field(q); A = F.Tpow(k); rnd = random.Random(250)
F3s = {x for x in F.prime_sub if x}


def on_slice(E):  # centre u0 = -E of the Case A ball (the I4 ball is its inverse; both slice families inversion-closed)
    if MODE == 'c':
        return F.vT(F.add(E, (1,))) == 1
    if MODE == 'k1':
        return F.NEG[E[0]] not in F3s
    return True


def verify_solution(X, Y, Z, P):
    assert all(t and t[-1] == 1 for t in (X, Y, Z)), "non-monic denominator"
    lhs = F.mul(A, F.mul(X, F.mul(Y, Z)))
    rhs = F.mul(P, F.add(F.mul(X, Y), F.add(F.mul(Y, Z), F.mul(Z, X))))
    assert lhs == rhs, "identity fails"


def linear_solution(E, ta, a0, tb, b0, P):
    """linear family (E; ta, a0; tb, b0) at P, straight from the FE 6.2 definition; returns None if not valid."""
    X, r = F.divmod(F.add(P, E), A)
    if r or not F.divides(a0, X) or not F.divides(b0, X):
        return None
    def term(t, c):
        return [c, F.mul(P, c), F.exact(X, c), F.exact(F.mul(P, X), c)][t]
    a, b = term(ta, a0), term(tb, b0)
    s = F.add(a, b)
    if not s or not F.divides(E, s) or s[-1] != E[-1]:
        return None
    kap = F.exact(s, E)
    PX = F.mul(P, X)
    Y, Z = F.exact(F.mul(kap, PX), a), F.exact(F.mul(kap, PX), b)
    verify_solution(X, Y, Z, P)
    return X, Y, Z


def i4_solution(a, b, e, P):
    num = F.add(F.mul(e, P), (1,)); Aab = F.mul(A, F.mul(a, b))
    d, r = F.divmod(num, Aab)
    if r:
        return None
    c = F.exact(F.add(a, b), e)
    sol = (F.mul(F.mul(a, F.mul(b, d)), P), F.mul(a, F.mul(c, d)), F.mul(b, F.mul(c, d)))
    verify_solution(*sol, P)
    return sol


def pick_P(centre_mod_T, depth, mod1):
    """P == centre mod T^depth, P == 1 mod mod1 (T-free), random lift, deg P >= deg(modulus) + 4."""
    Tm = F.Tpow(depth)
    r = F.crt(F.mod(centre_mod_T, Tm), Tm, (1,), mod1) if F.deg(mod1) > 0 else F.mod(centre_mod_T, Tm)
    W = F.mul(Tm, mod1); nW = F.deg(W)
    for _ in range(4000):
        t = tuple(rnd.randrange(q) for _ in range(4)) + (1,)
        P = F.add(r, F.mul(W, t))
        if not PRIME or F.irreducible(P):
            return P
    raise RuntimeError("no prime found")


def lcm(a, b):
    return F.exact(F.mul(a, b), F.gcd(a, b))


stats = dict(data=0, hyp=0, outside=0, ok23=0, ok24=0, e2e=0)
outside_examples = []
seen = set()
for da in range(D + 1):
    for db in range(D + 1):
        for a1 in F.monics(da):
            for b1 in F.monics(db):
                if (b1, a1) in seen:
                    continue
                seen.add((a1, b1))
                if len(F.gcd(a1, b1)) != 1:
                    continue
                al = F.vT(a1) + F.vT(b1)
                if k + al > DMAX:
                    continue
                s_ab = F.add(a1, b1)
                if not s_ab:
                    continue
                Lp = F.mul(F.tfree(a1), F.tfree(b1))
                if F.deg(Lp) > F.deg(s_ab):
                    continue  # E + 1 != 0 divisible by Lp forces deg E >= deg Lp, while deg E <= deg(a1 + b1)
                for E in F.monic_divisors(s_ab):
                    if F.deg(E) < 1 or E[0] == 0:
                        continue
                    if F.mod(F.add(E, (1,)), Lp) if F.deg(Lp) > 0 else ():
                        continue
                    if not on_slice(E):
                        continue
                    stats['data'] += 1
                    # orientation: aa carries T^alpha, bb T-free
                    aa, bb = (a1, b1) if F.vT(a1) >= F.vT(b1) else (b1, a1)
                    alpha = F.vT(aa)
                    v = F.vT(F.add(E, (1,)))
                    if not (alpha >= 1 and alpha + v >= k and v <= k + alpha):
                        stats['outside'] += 1
                        if len(outside_examples) < 4:
                            outside_examples.append((aa, bb, E, alpha, v))
                        continue
                    stats['hyp'] += 1
                    H = F.exact(F.add(E, (1,)), F.Tpow(v))
                    Lb, r = F.divmod(H, bb); assert not r, "b1 does not divide H"
                    gp = F.tfree(aa)
                    s = alpha + v; j = (s - k + 1) // 2; ga = (s - k) // 2
                    assert 0 <= ga <= j and k + j + ga == s
                    assert Lb[0] != 0 and Lb[-1] == 1 and F.divides(gp, Lb), "L' / g' conditions"
                    assert not F.mod(F.add(E, (1,)), Lb), "E != -1 mod L'"
                    Dp = F.add((1,), F.mul(F.Tpow(s), F.mul(Lb, gp)))
                    Ep, r = F.divmod(Dp, E); assert not r, "E does not divide D"
                    assert Dp[-1] == 1 and Ep[-1] == 1
                    assert j <= alpha, "Case B ball not containing Case A ball"
                    stats['ok23'] += 1
                    # Lemma 2.4: E' == 1/E mod T^{k+j} (so its ball -E' contains the I4 ball -1/E mod T^{k+alpha}), E' == -1 mod L'
                    Tkj = F.Tpow(k + j)
                    assert F.mod(F.mul(E, Ep), Tkj) == (1,) and not F.mod(F.add(Ep, (1,)), Lb)
                    stats['ok24'] += 1
                    # end-to-end
                    a0B, b0B = F.mul(F.Tpow(ga), gp), F.mul(F.Tpow(j), Lb)
                    m1 = lcm(lcm(Lp, Lb), lcm(E, Ep))
                    # Case A ball point: P == -E mod T^{k+alpha}
                    P = pick_P(F.neg(E), k + alpha, m1)
                    assert linear_solution(E, 0, a1, 0, b1, P) or linear_solution(E, 0, a1, 1, b1, P), "Case A family invalid"
                    assert linear_solution(E, 0, a0B, 2, b0B, P), "Lemma 2.3 Case B family invalid at Case A point"
                    if F.deg(a1) != F.deg(b1):
                        cen = F.neg(F.inv_mod(E, F.Tpow(k + alpha)))
                        P2 = pick_P(cen, k + alpha, m1)
                        assert i4_solution(a1, b1, E, P2), "I4 family invalid in its ball"
                        assert linear_solution(Ep, 0, a0B, 2, b0B, P2), "swapped Case B family invalid at I4 point"
                    stats['e2e'] += 1
print("q=%d k=%d mode=%s D=%d DMAX=%d prime=%s:" % (q, k, MODE, D, DMAX, PRIME), stats)
for ex in outside_examples:
    print("  outside hypotheses: a1=%s b1=%s E=%s alpha=%d v=%d" % ex)
