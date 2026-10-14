"""review_fs2_char2.py (R218, from scratch): FF_STERILE_PUSH §4 char-2 claim. For q = 2, 4, k = 2, c in F_q^*,
family (E; 0, g'; 2, g') with g' = T + c, E = 1 + T g'. Takes random monic P with P ≡ 1 + cT (mod T^2) [the c-slice]
and P ≡ 1 (mod g'E) [x ≡ 1 at the primes of g'E, as at a slice point], checks validity: T^2 | P + E, g' | X,
E | s = g' + X/g', lc(s) = lc(E), and the identity T^2/P = 1/X + 1/Y + 1/Z (Y = κPX/a, Z = κPX/b, κ = s/E).
Also checks that k = 2m families E = 1 + T^m g' (g' ≡ h mod T^m) are valid when P ≡ 1 + T^m h (mod T^{2m}).
usage: uv run --with python-flint python scripts/review_fs2_char2.py"""
import random
import flint
random.seed(5)
for q in (2, 4):
    ctx = flint.fq_default_ctx(2, 1 if q == 2 else 2, var='w')
    R = flint.fq_default_poly_ctx(ctx)
    els = [ctx(0), ctx(1)] + ([ctx.gen(), ctx.gen() + 1] if q == 4 else [])
    T = R([0, 1]); one = R([1])
    def rnd(d):
        return R([random.choice(els) for _ in range(d)] + [ctx(1)])
    ok = 0
    for m in (1, 2, 3):
        A = T**(2 * m)
        for trial in range(60):
            h = R([random.choice(els[1:])] + [random.choice(els) for _ in range(m - 1)])   # unit mod T^m
            # g' monic, g' ≡ h (mod T^m), T ∤ g'
            gp = h + T**m * rnd(random.randint(0, 2)) if True else None
            if gp.degree() < m: gp = h + T**m * rnd(0)
            lc = gp.coeffs()[-1]; gp = gp * lc**-1
            # renormalise to keep g' ≡ h mod T^m: if lc != 1 we skip (monic needed)
            if (gp - h) % T**m != 0 or gp.coeffs()[0] == 0:
                continue
            E = one + T**m * gp
            M = A * gp * E
            # CRT: P ≡ 1 + T^m h (mod A), P ≡ 1 (mod g'E); g'E coprime to T
            u = one + T**m * h
            ge = gp * E
            # P = 1 + ge * t, need ge*t ≡ T^m h mod A
            inv = None
            # inverse of ge mod A by extended gcd
            g, s_, t_ = ge.xgcd(A)
            inv = s_ * g.coeffs()[0]**-1
            t0 = (T**m * h * inv) % A
            P0 = one + ge * t0
            P = P0 + M * rnd(random.randint(2, 5))        # monic, large degree
            assert (P - u) % A == 0 and (P - one) % ge == 0
            X, rem = divmod(P + E, A); assert rem == 0
            assert X % gp == 0
            s = gp + X // gp
            kappa, rem = divmod(s, E); assert rem == 0 and s != 0
            assert s.coeffs()[-1] == E.coeffs()[-1]
            # identity A/P = 1/X + a/(kappa P X) + b/(kappa P X) with a = g', b = X/g'
            a, b = gp, X // gp
            assert A * X * kappa == P * kappa + a + b   # multiply A/P = 1/X + (a+b)/(kappa P X) by kappa P X
            ok += 1
    print(f"q={q}: {ok} random (m, g', P) instances valid, 0 failures")
