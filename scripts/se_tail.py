"""se_tail.py -- O219 (STERILE_EXPLICIT.md §3.3). Normalised-box tail: for ALL N >= N0 = 2^L0bits,
D_P(N) <= sum_t c_t N^{e_t} (ln N)^{p_t}  (mode P)  resp.  D_Q(F) <= same (mode Q),
with every route bound of Table 2 written as a list of terms (c, e, p) valid for all N >= N0 (worst-case box corners;
Coppersmith conditions (Cop) checked as linear functions of L = ln N: slope <= 0 and value < 0 at L0).
Boxes: a in [N^{x_a}, N^{x_a+u}) etc., u = 1/M.  Prints the term list summary and
  G = sum_t c_t N0^{e_t - h} L0^{p_t}   (h = 1/2 for P, 1 for Q),
which bounds D/N^h for every N >= N0 provided every term is decreasing there (checked: e_t < h, p_t <= (h - e_t) L0).
Usage: python3 se_tail.py P|Q M L0bits.   Fails (exit 1) if some box has no route with all exponents < h.
Floating point: all exponents/constants are rounded upward by 1e-9 (the conditions are checked with margin 1e-9)."""
import sys, math
EPS = 1e-9
def lC(eta, kk, pmax=10**6):
    s = 0.0
    p = 2
    sieve = bytearray([1]) * (int(kk ** (1 / eta)) + 2)
    for p in range(2, len(sieve)):
        if not sieve[p]: continue
        for q in range(p * p, len(sieve), p): sieve[q] = 0
        best, lb, k = 0.0, 0.0, 0
        while True:
            k += 1
            lb += math.log(k + kk - 1) - math.log(k)
            v = lb - eta * k * math.log(p)
            best = max(best, v)
            if v < best - 1 and k > 4: break
        s += best
    return s + 1e-9

def mul(T1, T2):
    return [(c1 * c2, e1 + e2, p1 + p2) for (c1, e1, p1) in T1 for (c2, e2, p2) in T2]
def add(*Ts):
    out = []
    for T in Ts: out += T
    return out
def maxe(T): return max(e for (c, e, p) in T)
def val(T, L): return sum(c * math.exp(e * L) * L ** p for (c, e, p) in T)

def cop(L0, cn, xn, cs, xs, c0, x0, c1, x1, W=int(__import__("os").environ.get("SE_W", "24")), kgrid=None):
    """divisors of n <= cn N^xn in a unit class mod s >= cs N^xs in [D0, D1], D0 >= c0 N^x0, D1 <= c1 N^x1."""
    best = [(c1 / cs, x1 - xs, 0), (1.0, 0.0, 0)]          # trivial: window/s + 1
    if x1 - xs <= 0: best = [(c1 / cs + 1, 0.0, 0)]
    for w in range(2, W + 1):
        for m in range(1, w + 1):
            s0 = m * (m + 1) / 2 * xn - m * w * x0
            g0 = w * math.log(w) + m * (m + 1) / 2 * (math.log(cn) + xn * L0) - m * w * (math.log(c0) + x0 * L0)
            if s0 > -EPS or g0 > -EPS * (1 + abs(g0)): continue
            ww = w * (w - 1) / 2
            k1 = x1 - xs + s0 / ww
            k2 = x1 - xs + math.log(c1 / cs) / L0 + g0 / (ww * L0)
            kap = max(0.0, k1, k2) + 1e-7
            T = [(w - 1.0, kap, 0), (w - 1.0, 0.0, 0)]
            if (maxe(T), val(T, L0)) < (maxe(best), val(best, L0)): best = T
    return best

def tailP(M, L0bits, eta3=0.3):
    u = 1.0 / M; L0 = L0bits * math.log(2)
    lc3 = lC(eta3, 3)
    etaw = 0.1; lcw = 0.0                      # 2^omega(e) <= prod_{p < 2^{1/etaw}} (2 p^{-etaw}) * e^etaw
    for p in range(2, 2 ** 10 + 1):
        if all(p % q for q in range(2, int(p ** 0.5) + 1)) and 2 > p ** etaw: lcw += math.log(2) - etaw * math.log(p)
    lcw += 1e-9
    LA = lambda: [(1.0 / L0 + u, 0.0, 1)]          # 1/A + u ln N <= (1/L0 + u) ln N
    terms = []; worst = -1; nbox = 0
    for ia in range(M + 1):
        for id_ in range(M + 1):
            for ic in range(M + 1):
                xa, xd, xc = ia * u, id_ * u, ic * u
                if 2 * xa + xd > 1 + EPS or xa + xc + xd > 1 + EPS: continue
                nbox += 1
                s3 = xa + xc + xd
                # capped upper exponents: a <= sqrt(N/(2d)), acd <= N, d <= N/(2a^2)
                xa_ = min(xa + u, (1 - xd) / 2); xd_ = min(xd + u, 1 - 2 * xa); xc_ = min(xc + u, 1 - xa - xd)
                s3_ = min(xa_ + xc_ + xd_, 1.0)
                nA, nC, nD = [(1.0, xa_, 0)], [(1.0, xc_, 0)], [(1.0, xd_, 0)]
                pe = [(0.25, 1 - s3, 0)]
                R = {}
                R['H'] = mul(mul(nA, nC), nD)
                R['A'] = add(mul(mul(pe, LA()), LA()), mul(nA, nD))
                fw = (3.0, s3, 4.0, s3_)               # f-window: D0 >= 3 N^s3, D1 <= 4 N^{s3_}
                R['C'] = mul(mul(nA, nD), cop(L0, 3.0, 1.0, 4.0, xa + xd, *fw))
                R['D'] = mul(mul(nC, nD), cop(L0, 5.0, 1 + 2 * xc_ + xd_, 4.0, xc + xd, *fw))
                R['E'] = mul(mul(nA, nC), cop(L0, 2.0, 1 + xc_, 4.0, xa + xc, *fw))
                pairF = add(mul(pe, LA()), nA)
                E0 = (0.25, 1 - s3_)
                if E0[1] >= 0:
                    cb = cop(L0, 0.5, 1 - xa, E0[0], E0[1], 0.25, 1 - xa_ - xd_, 0.5, 1 - xa - xd)
                    cd = cop(L0, 0.5, 1 - xa, E0[0], E0[1], 1.0, xd, 1.0, xd_)
                    R['F'] = mul(pairF, min(cb, cd, key=lambda T: (maxe(T), val(T, L0))))
                    pairG = add(mul(pe, LA()), nD)
                    om = [(math.exp(lcw) * 1.0, etaw * (1 - s3), 0)]   # 2^omega(e) <= C_w e^etaw, e <= N^{1-s3}
                    ca = cop(L0, 0.5, 1 - xd, E0[0], E0[1], 1.0, xa, 1.0, xa_)
                    cb2 = cop(L0, 0.5, 1 - xd, E0[0], E0[1], 0.25, 1 - xa_ - xd_, 0.5, 1 - xa - xd)
                    R['G'] = mul(mul(pairG, om), min(ca, cb2, key=lambda T: (maxe(T), val(T, L0))))
                R['tau3'] = mul(add(pe, [(1.0, 0.0, 0)]), [(math.exp(lc3) * 0.5 ** eta3, eta3, 0)])
                R['I'] = mul(nC, pairF)
                k = min(R, key=lambda k: (maxe(R[k]), val(R[k], L0)))
                terms += R[k]; worst = max(worst, maxe(R[k]))
    return terms, worst, nbox, L0

def tailQ(M, L0bits):
    u = 1.0 / M; L0 = L0bits * math.log(2)
    terms = []; worst = -1; nbox = 0
    for ic in range(M + 1):
        for id_ in range(M + 1):
            for ip in range(M + 1):
                xc, xd, xp = ic * u, id_ * u, ip * u
                if xc + xd > 1 + EPS or xp > 1 + EPS: continue
                nbox += 1
                xa1 = 1 + u - xc - xd; xa0 = 1 - xc - xd - 2 * u
                nA = [(0.5, xa1, 0), (1.0, 0.0, 0)]
                nC, nD = [(1.0, xc + u, 0)], [(1.0, xd + u, 0)]
                fw = (1.0, xp, 1.0, xp + u)
                R = {}
                R['AD'] = mul([(2.0, 0, 0)], mul(nA, nD))
                R['AC'] = mul(mul(nA, nC), cop(L0, 1.0, 2 + u - xc - xd, 1.0, xa0 + xc, *fw))
                R['CD'] = mul(mul(nC, nD), cop(L0, 5.0, 2.0, 4.0, xc + xd, *fw))
                # fac: pairs (f,a), 4a | f+F: (Phi N^u/4)(1/a0 + ln(a1/a0)) + nA ; then c- or d-class mod f
                la = [((1 + math.log(8)) / L0 + 3 * u, 0.0, 1)]   # sum_{a0<=a<=a1} 1/a <= 1 + ln 8 + 3u ln N (a >= 1)
                pa = add(mul([(0.25, xp + u, 0)], la), nA)
                cc = [(1.0, xc + u - xp, 0), (1.0, 0.0, 0)]; dd = [(1.0, xd + u - xp, 0), (1.0, 0.0, 0)]
                R['fac'] = mul(pa, min(cc, dd, key=lambda T: (maxe(T), val(T, L0))))
                pc = add(mul([(0.25, xp + u, 0)], [(1.0 / L0 + u, 0.0, 1)]), nC)
                R['fca'] = mul(pc, [(0.5, xa1 - xp, 0), (1.0, 0.0, 0)])
                k = min(R, key=lambda k: (maxe(R[k]), val(R[k], L0)))
                terms += R[k]; worst = max(worst, maxe(R[k]))
    return terms, worst, nbox, L0

if __name__ == '__main__':
    mode, M, L0bits = sys.argv[1], int(sys.argv[2]), float(sys.argv[3])
    h = 0.5 if mode == 'P' else 1.0
    terms, worst, nbox, L0 = (tailP if mode == 'P' else tailQ)(M, L0bits)
    ok = all(e < h - EPS and p <= (h - e) * L0 for (c, e, p) in terms)
    G = sum(c * math.exp((e - h) * L0) * L0 ** p for (c, e, p) in terms) * (1 + 1e-6)
    print(f"mode {mode} M {M} L0bits {L0bits} boxes {nbox} terms {len(terms)} max-exponent {worst:.4f} decreasing {ok} G {G:.6e}")
    if not ok: sys.exit(1)
