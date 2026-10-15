"""review_fz1_caseA.py (R226): k = 1 Case A on the slices u0 not in {-1, -2} (FF_STERILE_SMALL Lemma 7.2).
(1) naive exact enumeration over F_q (small q) of Case A data (a1', b1, K) -> E = a1'b1K - 1, alpha >= 1, from the
    Case A conditions (DEPTH_ASPECT §2.2 with k = 1): a1 = T^alpha a1', T not dividing a1' b1, gcd(a1, b1) = 1,
    E | a1 + b1, E == -1 mod a1'b1 (K := (E+1)/(a1'b1)), T not dividing E, lc(E) in {1, lc(a1 + b1)} (lc(s) of the
    equal-type sums; distinct types give 1), slice u0 = -E(0) not in {-1, -2}.  Enumeration bound: deg E = lam + be + ka
    <= deg(a1 + b1) = max(alpha + lam, be); every (lam, be, ka) with be + ka <= alpha, lam <= alpha is enumerated and
    patterns outside are shown empty by checking be > alpha + lam never occurs within a larger box (BOX).
    Every datum is tested for the claims of Lemma 7.2(a): z := (F + b1)/a1' is a nonzero polynomial with T not dividing
    it, f = alpha - be - ka >= 0, lam <= max(f, be), deg z <= zeta, route (ix) E | 1 + T^alpha a1'^2 K,
    (A0)-(A4), lc(E) = lc(K).
(2) per-route check of the six route formulas of the author's fz1_caseA.py (transcribed) and of R226's own routes.
(3) R226's own Case A mass for q = 3^r (exact rationals): routes (i), (ii), (v), (vi) only (re-derived in the review),
    alpha <= AMAX, plus the Lemma 7.2(b) tail.
usage: review_fz1_caseA.py enum q AMAX [loose]   |   review_fz1_caseA.py mass r AMAX"""
import sys, itertools, math
from fractions import Fraction as Fr
sys.path.insert(0, 'scripts')

def enum(q, AMAX, loose=False):
    from review_fz1_ff import GF
    F = GF(q)
    bad_u = {F.neg[1], F.neg[F.add[1][1]]}
    mon = lambda d: list(F.polys(d, monic=True, Tfree=True))
    counts = {}; fails = []; outside = 0
    for al in range(1, AMAX + 1):
        Ta = F.T(al)
        for la in range(0, al + 2):                      # lam up to alpha + 1 (claim: lam <= alpha)
            for be in range(0, al + la + 2):           # box larger than needed: be up to alpha + lam + 1
                for ka in range(0, al + 1):
                    if la + be + ka > al + la + 1: continue
                    for a1p in mon(la):
                        a1 = F.pmul(Ta, a1p)
                        for b1 in mon(be):
                            if F.deg(F.pgcd(a1, b1)) > 0: continue
                            S = F.padd(a1, b1)
                            for lcK in (1, F.add[1][1]):
                                for K in F.polys(ka, monic=False, Tfree=True):
                                    if K[-1] != lcK: continue
                                    E = F.psub(F.pmul(F.pmul(a1p, b1), K), F.const(1))
                                    if not E or E[0] == 0: continue
                                    if F.deg(E) < 1: continue            # constant E: u0 in {-1,-2} (Prop 6.1)
                                    if not loose and F.lc(E) not in (1, F.lc(S)): continue
                                    Fq, rem = F.pdivmod(S, E)
                                    if rem: continue
                                    u0 = F.neg[E[0]]
                                    if (u0 in bad_u) if not loose else (u0 == 1): continue   # loose: only T not dividing K
                                    f = F.deg(Fq)
                                    if be > al + la or f != al - be - ka:
                                        outside += 1; fails.append(('pattern', al, la, be, ka, f)); continue
                                    # Lemma 7.2(a) checks
                                    zz, r2 = F.pdivmod(F.padd(Fq, b1), a1p)
                                    zeta = max(f, be) - la
                                    ok = [r2 == (), bool(zz), bool(zz) and zz[0] != 0, la <= max(f, be),
                                          bool(zz) and F.deg(zz) <= zeta, F.lc(E) == F.lc(K)]
                                    ix = F.padd(F.const(1), F.pmul(Ta, F.pmul(F.pmul(a1p, a1p), K)))
                                    ok.append(F.pdivides(E, ix))
                                    ok.append(F.pmul(F.pmul(b1, K), Fq) == F.padd(Ta, zz))                  # (A3)
                                    ok.append(F.pmul(zz, E) == F.padd(Ta, F.pmul(F.pmul(b1, b1), K)))      # (A2)
                                    ok.append(F.pmul(b1, F.psub(F.pmul(F.pmul(a1p, K), Fq), F.const(1))) == F.padd(F.pmul(Ta, a1p), Fq))  # (A4)
                                    if not all(ok): fails.append(('claim', al, la, be, ka, ok))
                                    c = counts.setdefault((al, la, be, ka), 0); counts[(al, la, be, ka)] = c + 1
    return counts, fails, outside

def author_routes(q, al, la, be, ka):
    """transcription of the six bounds of fz1_caseA.py (B list), with its clsr/cls/cop"""
    from math import comb, factorial
    Ns = lambda d: 1 if d <= 0 else q**d - q**(d - 1)
    def cop(n, d, rho):
        X = d - rho; best = None
        for m in range(1, 61):
            for k in range(0, 201 - m):
                if n * m * (m + 1) + X * (m * (m + 1) + 2 * k * m + k * (k + 1)) < 2 * (m + k + 1) * m * d:
                    if best is None or m + k < best: best = m + k
                    break
        return best
    def cls(n, d, rho, both):
        if d < rho or (both and n - d < rho): return 1
        c = [comb(n, d)]
        if 3 * rho > n: c.append(2)
        x = cop(n, d, rho) if rho >= 1 else None
        if x: c.append(x)
        if both and rho >= 1:
            x = cop(n, n - d, rho)
            if x: c.append(x)
        return min(c)
    def clsr(n, d, rho, both):
        best = comb(n, d)
        for j in range(0, max(0, d - rho + 1) + 1):
            if q**j >= best: break
            best = min(best, q**j * cls(n, d, rho + j, both))
        return best
    f = al - be - ka; ze = max(f, be) - la
    return [2 * Ns(la) * Ns(be) * Ns(ka), 4 * Ns(la) * Ns(ka) * Ns(f),
            4 * Ns(be) * Ns(ka) * clsr(max(al, 2 * be + ka), la + be + ka, be + ka, 1),
            2 * Ns(la) * Ns(be) * clsr(al + la, la + be + ka, la + be, 1),
            2 * (q - 1) * q**ze * (factorial(al) // (factorial(be) * factorial(ka) * factorial(f))),
            4 * (q - 1) * q**ze * Ns(la) * Ns(ka)]

def own_routes(q, al, la, be, ka):
    """R226 routes: (i) (a1', b1, K): 2 N(la) N(be) N(ka); (ii) (a1', K, F) -> b1 by (A4): 2*2 N(la) N(ka) N(f);
    (v) z (T-free, deg <= zeta: (q-1) q^zeta), then (b1, K, F) ordered factorisation of T^alpha + z with lc(K) in {1,2}:
    2 multinomial; (vi) (a1', z, K): b1, F roots of X^2 - a1'z X + (T^alpha + z)/K: 2 * (q-1) q^zeta * N(la) * 2 N(ka)."""
    N = lambda d: 1 if d <= 0 else q**d - q**(d - 1)
    f = al - be - ka; ze = max(f, be) - la
    mult = math.factorial(al) // (math.factorial(be) * math.factorial(ka) * math.factorial(f))
    return [2 * N(la) * N(be) * N(ka), 4 * N(la) * N(ka) * N(f), 2 * (q - 1) * q**ze * mult, 4 * (q - 1) * q**ze * N(la) * N(ka)]

def mass(r, AMAX):
    q = 3**r; tot = Fr(0)
    for al in range(1, AMAX + 1):
        acc = 0
        for be in range(0, al + 1):
            for ka in range(0, al - be + 1):
                f = al - be - ka
                for la in range(0, max(f, be) + 1):
                    acc += min(own_routes(q, al, la, be, ka))
        tot += Fr(acc, q**al)
    a0 = AMAX + 1
    rho = ((a0 + 2) / (a0 + 1))**3 * math.sqrt(3 / q)
    tail = (a0 + 1)**3 * math.sqrt(8) * q**((1 - a0) / 2) * 3**(a0 / 2) / (1 - rho) * 1.000001
    return tot, tail

if __name__ == '__main__':
    if sys.argv[1] == 'enum':
        q, AMAX = int(sys.argv[2]), int(sys.argv[3])
        counts, fails, outside = enum(q, AMAX, loose=len(sys.argv) > 4)
        if len(sys.argv) > 4: print('LOOSE mode: all slices with u0 != 1 (T not dividing K), lc(E) in {1,2} only')
        print(f"q={q} alpha<={AMAX}: data on slices u0 not in {{-1,-2}}: {sum(counts.values())}; per alpha: "
              + str({a: sum(c for k, c in counts.items() if k[0] == a) for a in range(1, AMAX + 1)}))
        print(f"  Lemma 7.2(a) claim failures: {len(fails)} (outside the pattern range: {outside})", fails[:5])
        va = vo = 0; wa = [0.0] * 6; wo = [0.0] * 4
        for (al, la, be, ka), c in counts.items():
            A = author_routes(q, al, la, be, ka); O = own_routes(q, al, la, be, ka)
            for i, x in enumerate(A):
                if c > x: va += 1; print("  AUTHOR ROUTE VIOLATION", i, (al, la, be, ka), c, x)
                wa[i] = max(wa[i], c / x)
            for i, x in enumerate(O):
                if c > x: vo += 1; print("  OWN ROUTE VIOLATION", i, (al, la, be, ka), c, x)
                wo[i] = max(wo[i], c / x)
        print(f"  author routes (i)-(vi) violations {va}, max count/bound {[round(x, 3) for x in wa]}; own routes violations {vo}, max {[round(x, 3) for x in wo]}")
        sys.exit(1 if fails or va or vo else 0)
    else:
        r, AMAX = int(sys.argv[2]), int(sys.argv[3])
        tot, tail = mass(r, AMAX)
        print(f"r={r} q={3**r}: own Case A mass alpha<={AMAX} <= {float(tot) * (1 + 1e-12):.10e}, tail <= {tail:.3e}")
