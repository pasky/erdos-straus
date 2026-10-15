"""review_zl_combine.py -- R231, FROM SCRATCH combiner for STERILE_LOWER Thm 2.1 (does not import zl_r0.py / se_r0.py).
Checks  S(r) = sum_{k odd} 2 D_Q(r^k) r^{-k} + sum_{K odd} 2 D_P(r^K) r^{-(K+1)/2}  <  (r-1)/(2r)
for every r in [2^B0, infinity) (r-cells [2^b, 2^{b+1/32}) below 2^34, [2^b, 2^{b+1/4}) above, up to 2^800).
Arithmetic: all cell endpoints exact (Fractions of bits); every real quantity computed with mpmath at 40 digits and inflated by a
relative 1e-30 (upper bounds) -- error of each op < 1e-38, so these are rigorous upper bounds.
Tables: certified se_box/zl_box rows "j F": D(N) <= F for N in [2^{j/q}, 2^{(j+1)/q}).  For each N-range the combiner walks the
range and, at each point, takes the SMALLEST value among the table cells containing it (any covering cell is a valid bound).
Tails (json lists of (c,e,p), from review_zl_tail.py on SE's reviewed se_tail.py): valid for N >= 2^LP (P) / 2^LQ (Q).
Terms are aggregated by (p, e rounded UP to 1e-6, e<0 -> 0), admissibility re-checked after aggregation; tail evaluated at the TOP
of each N-range (nondecreasing in N), weight at the BOTTOM r = 2^b. The K-series is summed until K reaches KMAX in the tail
regime, then the remainder is bounded by an explicit geometric series (ratio bound per term, decreasing in K).
For r >= 2^800: all N are in the tails and each weighted term is decreasing in r (admissibility), so S(r) <= bound of the last cell.
Usage: review_zl_combine.py B0bits_num/32 VARIANT TAILP   VARIANT in {se, l2}; TAILP json for P tail.  Exit 1 on any failure."""
import sys, json, os
from fractions import Fraction as Fr
from mpmath import mp, mpf, log, exp
mp.dps = 40
PAD = 1 + mpf(10) ** -30
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def table(path, q, jmax=None):
    T = {}
    with open(os.path.join(ROOT, path)) as fh:
        for line in fh:
            if line.startswith("#") or not line.strip(): continue
            f = line.split(); j = int(f[0]); v = mpf(f[1])
            if j in T or not (v >= 0): raise SystemExit(f"bad row {path}: {line}")
            if jmax is not None and j > jmax: continue
            T[j] = v
    return (q, T)

def cover(tabs, lo, hi):
    """max over [lo, hi) (bits, Fractions) of min over covering cells; None if a gap exists."""
    x = lo; best = mpf(0)
    while x < hi:
        cands = []
        for (q, T) in tabs:
            j = (x * q).numerator // (x * q).denominator     # floor(x q), exact
            if j in T: cands.append((T[j], Fr(j + 1, q)))
        if not cands: return None
        v, end = min(cands, key=lambda t: t[0])
        # the chosen cell covers [x, end); the smaller-valued one is a valid bound on that piece
        best = max(best, v); x = end
    return best

def agg(terms, h, L0):
    A = {}
    for (c, e, p) in terms:
        e2 = max(Fr(0), Fr(-(-Fr(e) * 10**5 // 1), 10**5))       # ceil to 1e-5 grid, cap at 0
        A[(e2, p)] = A.get((e2, p), mpf(0)) + mpf(c)
    out = [(c * PAD, e, p) for (e, p), c in A.items()]
    for (c, e, p) in out:
        if not (e < h and p <= (mpf((h - e).numerator) / (h - e).denominator) * L0): raise SystemExit("aggregated tail term not admissible")
    return out

LN2 = log(2)
def tailval(terms, bits):
    """sum c N^e (ln N)^p at N = 2^bits (bits Fraction)."""
    L = mpf(bits.numerator) / bits.denominator * LN2
    return sum(c * exp(mpf(e.numerator) / e.denominator * L) * L ** p for (c, e, p) in terms) * PAD

def w2(bits):  # 2^{bits} (bits Fraction), upper bound
    return exp(mpf(bits.numerator) / bits.denominator * LN2) * PAD

def main():
    B0 = Fr(sys.argv[1]); variant = sys.argv[2]; tailP = sys.argv[3]
    LP, LQ, Bfine, Bmax = Fr(800), Fr(100), Fr(34), Fr(800)
    if len(sys.argv) > 4: Bmax = Fr(sys.argv[4]); print("NOTE: partial run up to", float(Bmax), "-- not a certificate")
    P = [table("data/zl/P_q32.txt", 32), table("data/se/P_q4.txt", 4), table("data/se/P_q1.txt", 1),
         table("data/zl/P_q1_hi.txt", 1, jmax=799)]
    Q = [table("data/zl/Q_q32.txt", 32), table("data/se/Q_q4.txt", 4)]
    if variant == "l2":
        P.append(table("data/zl/P_q32_l2.txt", 32)); Q.append(table("data/zl/Q_q32_l2.txt", 32))
    tP = agg(json.load(open(os.path.join(ROOT, tailP))), Fr(1, 2), mpf(800) * LN2)
    tQ = agg(json.load(open(os.path.join(ROOT, "data/zl_review/tailQ100_new.json"))), Fr(1), mpf(100) * LN2)
    print(f"tail groups: P {len(tP)}, Q {len(tQ)}; max e P {float(max(t[1] for t in tP)):.6f} Q {float(max(t[1] for t in tQ)):.6f}")
    b = B0; worst = (mpf(0), None); fails = 0; KMAX = 4001
    while b <= Bmax:
        st = Fr(1, 32) if b < Bfine else Fr(1, 4)
        bh = b + st
        S = mpf(0); parts = {}
        for (kind, tabs, tl, Lt, h) in (("P", P, tP, LP, None), ("Q", Q, tQ, LQ, None)):
            last = None
            for K in range(1, KMAX + 1, 2):
                lo, hi = K * b, K * bh
                wl = 1 - b * (K + 1) / 2 if kind == "P" else 1 - b * K     # log2 of the weight bound at r = 2^b
                v = mpf(0)
                if lo < Lt:
                    t = cover(tabs, lo, min(hi, Lt))
                    if t is None: print("GAP", kind, K, float(lo), float(hi)); sys.exit(1)
                    v = t * w2(wl)
                if hi > Lt:
                    v = max(v, tailval(tl, hi) * w2(wl))
                S += v; parts[(kind, K)] = v
                if lo >= Lt:
                    last = (K, hi)
                    if v < mpf(10) ** -30: break
            else:
                print("series cutoff not reached", kind, float(b)); sys.exit(1)
            # remainder K > KMAX (all in tails): per-term ratio of successive odd K at the top/bottom bounds
            Kl, _ = last
            rem = mpf(0)
            for (c, e, p) in tl:
                ee = mpf(e.numerator) / e.denominator
                if kind == "P":   # term(K) <= 2c 2^{K bh e} (K bh ln2)^p 2^{-b(K+1)/2}
                    rho = exp((2 * ee * mpf(bh.numerator) / bh.denominator - mpf(b.numerator) / b.denominator) * LN2) * (mpf(Kl + 2) / Kl) ** p
                    t0 = 2 * c * exp((Kl * ee * mpf(bh.numerator) / bh.denominator - mpf(b.numerator) / b.denominator * (Kl + 1) / 2) * LN2) * (Kl * mpf(bh.numerator) / bh.denominator * LN2) ** p
                else:
                    rho = exp((2 * ee * mpf(bh.numerator) / bh.denominator - 2 * mpf(b.numerator) / b.denominator) * LN2) * (mpf(Kl + 2) / Kl) ** p
                    t0 = 2 * c * exp((Kl * ee * mpf(bh.numerator) / bh.denominator - mpf(b.numerator) / b.denominator * Kl) * LN2) * (Kl * mpf(bh.numerator) / bh.denominator * LN2) ** p
                if not rho < mpf(1) / 2: print("remainder ratio too large", kind, float(b)); sys.exit(1)
                rem += t0 * rho / (1 - rho)
            S += rem * PAD
        lim = mpf(1) / 2 - exp(-(mpf(b.numerator) / b.denominator + 1) * LN2)
        S *= PAD
        if not S < lim: fails += 1; print(f"FAIL b={float(b):.5f} S={mp.nstr(S, 8)}")
        if S > worst[0]: worst = (S, b, parts)
        if os.environ.get("VERBOSE") or b == B0:
            top = sorted(parts.items(), key=lambda kv: -kv[1])[:4]
            print(f"b={float(b):.5f} S={mp.nstr(S, 8)} lim={mp.nstr(lim, 10)} top:", [(k, mp.nstr(v, 5)) for k, v in top])
        b += st
    print(f"B0={float(B0)} variant={variant} tail={tailP}: max S = {mp.nstr(worst[0], 8)} at b = {float(worst[1])}; failures {fails}")
    sys.exit(1 if fails else 0)

if __name__ == "__main__":
    main()
