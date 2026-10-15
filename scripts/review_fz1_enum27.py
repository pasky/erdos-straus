"""review_fz1_enum27.py (R226): independent exact enumeration of the k = 1 Case B tuples (B^{k=1}) over F_q (q = p^r),
per pattern (s; a, z, y, t) with a <= b (a = b: both orders), with total and slice-filtered (E(0) not in F_3) counts.
Uses python-flint (FLINT factorisation over F_q); written from the text of FF_STERILE_SMALL §6/§7, not from fz1_enum.c.
Sweeps for each s (union of found tuples, every tuple verified against the definition):
  V : every v (deg t <= t0, lc(v) = lc(w + C) in {1, 2} as g' is monic, v(0) != 0): all ordered (w, C) of monic divisors with wC | T^s + v;
  R2: every (m', g') with deg m' + deg g' <= D: monic E | 1 + T^s m'g'^2 with E == -1 mod m'g'  -> w = (E+1)/L', C = (g'T^s+w)/E;
  R3: every (w, g') with deg w + deg g' <= D:  monic E | g'T^s + w with E == -1 mod g'w -> L' = (E+1)/w, m' = L'/g', C;
  R4: every (m', w) with deg m' + deg w <= D:  monic E | T^s + m'w^2 with E == -1 mod m'w -> g' = (E+1)/(m'w), C.
Completeness for a <= b: t = s - (a + y + z) (y + t = b, Lemma 7.1(i), re-derived in the review), so t > t0 gives
sigma = a + y + z <= s - t0 - 1 and min(y + z, a + y, a + z) <= floor(2 sigma / 3) <= D := floor(2 (s - t0 - 1) / 3).
The identities used (EE' = 1 + T^s L'g', EC = g'T^s + w, Ev = T^s + m'w^2) are re-derived in the review.
usage: review_fz1_enum27.py p r s t0 [outfile]   (D computed; prints per-pattern lines "s a z y t count count_filtered")"""
import sys, itertools, time
import flint

def main():
    p, r, s, t0 = map(int, sys.argv[1:5]); out = sys.argv[5] if len(sys.argv) > 5 else None
    D = max(0, (2 * (s - t0 - 1)) // 3)
    F = flint.fq_default_ctx(p, r); R = flint.fq_default_poly_ctx(F)
    q = p ** r
    g = F.gen()
    elems = [F(0)] + sorted({g ** i for i in range(q - 1)}, key=str) if r > 1 else [F(i) for i in range(q)]
    elems = list(dict.fromkeys(elems)); assert len(elems) == q
    nonzero = [e for e in elems if e != 0]
    F3 = {F(1), F(p - 1)} if p == 3 else None
    T = R([0, 1]); Ts = T ** s; one = R([1])
    def monics(d):
        if d == 0: yield one; return
        for low in itertools.product(elems, repeat=d - 1):
            for c0 in nonzero: yield R([c0, *low, 1])
    def divisors(P):
        c, fac = P.factor()
        divs = [(one, 0)]
        for f, e in fac:
            df = f.degree(); new = []
            for d0, dd in divs:
                x = d0
                for k in range(e + 1):
                    new.append((x, dd + k * df)); x = x * f
            divs = new
        return divs
    found = {}
    def key(*polys): return tuple(tuple(int(str(c)) if r == 1 else str(c) for c in P.coeffs()) for P in polys)
    def verify(m, gg, w, C, src):
        # definition check
        for P in (m, gg, w, C):
            if P == 0 or P.leading_coefficient() != 1 or P.coeffs()[0] == 0: return
        v = m * w * C - Ts
        if v == 0 or v.coeffs()[0] == 0: return
        if w + C != gg * v: return
        a, b = w.degree(), C.degree()
        if a > b: return
        k = key(m, gg, w, C)
        if k in found: return
        L = m * gg; E = L * w - 1
        filt = F3 is not None and E.coeffs()[0] not in F3
        found[k] = (s, a, m.degree(), gg.degree(), v.degree(), filt, src)
    t_start = time.time(); nfac = 0
    # ---- sweep V ----
    for t in range(0, t0 + 1):
        if t == 0:
            vs = (R([c]) for c in nonzero)
        else:
            vs = (R([c0, *low, lc]) for lc in (F(1), F(2 % p)) for low in itertools.product(elems, repeat=t - 1) for c0 in nonzero)
        for v in vs:
            P = Ts + v
            if P.degree() != s: continue
            nfac += 1
            divs = [d for d, _ in divisors(P)]
            for w in divs:
                Pw = P // w
                for C in divisors(Pw):
                    C = C[0]
                    m = Pw // C
                    sm = w + C
                    if sm % v != 0: continue
                    gg = sm // v
                    if gg.leading_coefficient() != 1: continue
                    verify(m, gg, w, C, 'V')
    # ---- sweeps R2, R3, R4 ----
    for d1 in range(D + 1):
        for d2 in range(D + 1 - d1):
            for X in monics(d1):
                for Y in monics(d2):
                    # R2: (m', g') = (X, Y)
                    L = X * Y; P = one + Ts * X * Y * Y; nfac += 1
                    for E, de in divisors(P):
                        if de < L.degree(): continue
                        if (E + 1) % L != 0: continue
                        w = (E + 1) // L
                        num = Y * Ts + w
                        if num % E != 0: continue
                        verify(X, Y, w, num // E, 'R2')
                    # R3: (w, g') = (X, Y)
                    w, gg = X, Y; P = gg * Ts + w; M = gg * w; nfac += 1
                    for E, de in divisors(P):
                        if de < 1 or (E + 1) % M != 0: continue
                        L = (E + 1) // w
                        if L % gg != 0: continue
                        verify(L // gg, gg, w, P // E, 'R3')
                    # R4: (m', w) = (X, Y)
                    m, w = X, Y; P = Ts + m * w * w; M = m * w; nfac += 1
                    for E, de in divisors(P):
                        if de < 1 or (E + 1) % M != 0: continue
                        gg = (E + 1) // M
                        num = gg * Ts + w
                        if num % E != 0: continue
                        verify(m, gg, w, num // E, 'R4')
    counts = {}
    for k, (s_, a, z, y, t, filt, src) in found.items():
        c = counts.setdefault((s_, a, z, y, t), [0, 0]); c[0] += 1; c[1] += filt
    tot = sum(c[0] for c in counts.values()); totf = sum(c[1] for c in counts.values())
    print(f"q={q} s={s} t0={t0} D={D}: factorisations {nfac}, tuples(a<=b) {tot}, filtered (E(0) not in F_3) {totf}, "
          f"time {time.time() - t_start:.0f}s", flush=True)
    if out:
        with open(out, 'w') as fo:
            for k in sorted(counts): fo.write("%d %d %d %d %d %d %d\n" % (*k, *counts[k]))

main()
