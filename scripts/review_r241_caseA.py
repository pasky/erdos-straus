"""review_r241_caseA.py (R241) — FROM SCRATCH exhaustive k = 1 Case A data and the law of FF_ODD_ABSENCE Thm 1.4.
Data (a1', b1, K): a1', b1 monic, lc K in {1, 2}, T not dividing a1' b1 K, E = a1' b1 K - 1, E | T^alpha a1' + b1.
Route (proved here, independent of the author's routes): E (F b1 K - T^alpha) = T^alpha + b1^2 K, so E | T^alpha + b1^2 K;
and beta + kappa <= alpha always (deg E <= deg(T^alpha a1' + b1), the case beta > alpha + lambda is impossible).
So enumerate (b1, K) with beta + kappa <= alpha, factor T^alpha + b1^2 K, E = lc(K) * D for monic D, a1' = (E+1)/(b1 K).
Checks per datum: E(0)^{2 alpha} = 1 (if q = 3^r), and the unsimplified Lemma 1.1 form
  E(0)^alpha = (-1)^{t + t kappa + kappa(1+alpha) + t alpha} lam^{kappa + 2 beta - alpha} (lc K)^{alpha - t},
  z = (F + b1)/a1', t = deg z, lam = lc z.
Prints per-pattern counts 'A alpha lam(deg a1') be ka count_offF3 count_P8 count_all'.
usage: review_r241_caseA.py p r amax"""
import sys, itertools
import flint
p, r, amax = map(int, sys.argv[1:4])
q = p ** r
F = flint.fq_default_ctx(p, r, 'g'); R = flint.fq_default_poly_ctx(F)
g0 = F.gen()
ELS = []
for cs in itertools.product(range(p), repeat=r):
    e = F(0)
    for i, c in enumerate(cs):
        e += F(c) * g0 ** i
    ELS.append(e)
NZ = [e for e in ELS if e != 0]
T = R([0, 1]); ONE, TWO = F(1), F(2)
def polys(d, lc):
    if d == 0:
        yield R([lc]); return
    for cs in itertools.product(NZ, *([ELS] * (d - 1))):
        yield R(list(cs) + [lc])
def monic_divisors(P):
    _, facs = P.factor()
    out = [R([1])]
    for f, e in facs:
        f = f.monic(); new = []
        for d in out:
            pw = R([1])
            for k in range(e + 1):
                new.append(d * pw); pw *= f
        out = new
    return out
F3 = {str(ONE), str(TWO)} if p == 3 else {str(ONE), str(-ONE)}
fails = 0
for al in range(1, amax + 1):
    cnt = {}
    seen = set()
    Ta = T ** al
    for be in range(0, al + 1):
        for ka in range(0, al - be + 1):
            for b1 in polys(be, ONE):
                for lcK in ((ONE, TWO) if p != 2 else (ONE,)):
                    for K in polys(ka, lcK):
                        G = Ta + b1 * b1 * K
                        for D in monic_divisors(G):
                            E = lcK * D
                            a1p, rr = divmod(E + 1, b1 * K)
                            if rr != 0 or a1p == 0 or a1p.leading_coefficient() != 1 or a1p(F(0)) == 0:
                                continue
                            Fp, rr = divmod(Ta * a1p + b1, E)
                            if rr != 0:
                                continue
                            key = (str(a1p), str(b1), str(K))
                            if key in seen:
                                continue
                            seen.add(key)
                            E0 = E(F(0))
                            z, rr = divmod(Fp + b1, a1p)
                            assert rr == 0 and z != 0 and z(F(0)) != 0
                            assert b1 * K * Fp == Ta + z   # (A3)
                            t = z.degree(); lam = z.leading_coefficient(); la = a1p.degree()
                            ex = ka + 2 * be - al
                            sign = -1 if (t + t * ka + ka * (1 + al) + t * al) % 2 else 1
                            lamp = lam ** ex if ex >= 0 else (1 / lam) ** (-ex)
                            rhs = F(sign) * lamp * (lcK ** (al - t) if al >= t else (1 / lcK) ** (t - al))
                            ok1 = (E0 ** al == rhs)
                            ok2 = (E0 ** (2 * al) == 1) if p == 3 else True
                            if not (ok1 and ok2):
                                fails += 1; print('LAWFAIL', al, key, E0, ok1, ok2)
                            off = str(E0) not in F3
                            p8 = (E0 ** 4 == -ONE)
                            c = cnt.setdefault((al, la, be, ka), [0, 0, 0])
                            c[0] += off; c[1] += p8; c[2] += 1
    for k in sorted(cnt):
        print('A', *k, *cnt[k])
    print(f'# alpha={al} data={sum(c[2] for c in cnt.values())} offF3={sum(c[0] for c in cnt.values())} '
          f'P8={sum(c[1] for c in cnt.values())} fails={fails}', flush=True)
