"""R223 (hostile review #2 of STERILE_EXPLICIT.md): FROM-SCRATCH all-N tail bound for D_P(N), N >= N0 = 2^600,
with EXACT rational exponents and interval-rounded constants, and its contribution to (S) for r in [2^32, 2^32.25).
Boxes a in [N^al, N^{al+u}), c in [N^ga, N^{ga+u}), d in [N^de, N^{de+u}), u = 1/M, capped by a^2 d <= N/2, acd < N.
Every route bound is a list of monomials (c, e, p) meaning c N^e (ln N)^p, c an upper-rounded Fraction, e a Fraction.
Class-divisor counts: Lemma 1.3 / Cor 1.4 with J = ceil(N^kappa); (Cop) is verified as a linear function of L = ln N
(slope <= 0 exactly in rationals, value < 0 at L0 with interval logs), using X_J <= max(1, c1 N^{x1-xs-kappa}/cs).
Usage: PYTHONPATH=scripts uv run python scripts/review_se2_tail.py [M=32] [W=40]"""
import sys, math
from fractions import Fraction as Fr
from mpmath import iv, mp
iv.dps = 40; mp.dps = 40

def fr(x):
    x = mp.mpf(x); m, e = x.man, x.exp
    if x < 0: m = -m
    return Fr(m) * (Fr(2) ** e)
def ivf(x):
    x = Fr(x); return iv.mpf(x.numerator) / iv.mpf(x.denominator)
def lnU(x): return fr(iv.log(ivf(x)).b)
def lnD(x): return fr(iv.log(ivf(x)).a)

L0bits = 600
L0lo = fr((iv.mpf(L0bits) * iv.log(iv.mpf(2))).a); L0hi = fr((iv.mpf(L0bits) * iv.log(iv.mpf(2))).b)

def isprime(p):
    return p >= 2 and all(p % q for q in range(2, int(p ** 0.5) + 1))
def logC(eta, k):                       # log of sup_n tau_k(n)/n^eta (upper), concavity break
    s = Fr(0)
    for p in range(2, int(k ** (1 / float(eta))) + 2):
        if not isprime(p): continue
        best = Fr(0); prev = None; j = 0
        while True:
            j += 1
            v = lnU(math.comb(j + k - 1, k - 1)) - Fr(eta) * j * lnD(p)
            best = max(best, v)
            if prev is not None and v < prev: break
            prev = v
        s += best
    return s
def expU(x): return fr(iv.exp(ivf(x)).b)

def val(T, L):     # float evaluation, for choosing routes only
    return sum(float(c) * math.exp(float(e) * L) * L ** p for (c, e, p) in T)
def mx(T): return max(e for (c, e, p) in T)
def key(T): return (mx(T), val(T, float(L0lo)))
def mul(S, T): return [(c1 * c2, e1 + e2, p1 + p2) for (c1, e1, p1) in S for (c2, e2, p2) in T]

W = 40
LNW = {w: lnU(w) for w in range(2, 200)}
def cop(cn, xn, cs, xs, c0, x0, c1, x1):
    """#divisors of an integer n <= cn N^xn, in a unit class mod s >= cs N^xs, in [D0, D1], D0 >= c0 N^x0, D1 <= c1 N^x1."""
    best = [(c1 / cs, x1 - xs, 0), (Fr(1), Fr(0), 0)] if x1 > xs else [(c1 / cs + 1, Fr(0), 0)]
    lcn, lc0, lc1s = lnU(cn), lnD(c0), lnU(c1 / cs)
    fl = float; L0f = fl(L0lo)
    cands = []
    for w in range(2, W + 1):                                   # float pre-screen
        ww = w * (w - 1) // 2
        for m in range(1, w + 1):
            A = m * (m + 1) // 2
            g0, g1 = w * math.log(w) + A * fl(lcn) - m * w * fl(lc0), A * fl(xn) - m * w * fl(x0)
            if g1 > 1e-12 or g0 + g1 * L0f > -1e-9: continue
            kap = max(0.0, fl(x1 - xs) + g1 / ww, fl(x1 - xs) + (g0 + ww * fl(lc1s)) / (ww * L0f) + g1 / ww)
            T = [(Fr(w - 1), kap, 0), (Fr(w - 1), 0.0, 0)]
            cands.append((key(T), w, m))
    cands.sort()
    for (kk, w, m) in cands:                                   # exact verification of the best surviving candidate
        if kk >= key(best): break
        ww = w * (w - 1) // 2; A = m * (m + 1) // 2
        g0, g1 = w * LNW[w] + A * lcn - m * w * lc0, A * xn - m * w * x0
        if g1 > 0 or not (g0 + g1 * L0lo < 0): continue
        k1 = x1 - xs + g1 / ww
        k2 = x1 - xs + (g0 + ww * lc1s) / (ww * L0lo) + g1 / ww
        kap = Fr(math.ceil(max(Fr(0), k1, k2) * 10 ** 7) + 1, 10 ** 7)
        slope = g1 + ww * (x1 - xs - kap)
        if not (slope <= 0 and g0 + ww * lc1s + slope * L0lo < 0): continue
        T = [(Fr(w - 1), kap, 0), (Fr(w - 1), Fr(0), 0)]
        if key(T) < key(best): best = T
        break
    return best

def tailP(M):
    u = Fr(1, M)
    lc3 = logC(Fr(3, 10), 3); C3 = expU(lc3)
    etaw = Fr(1, 10)                     # 2^omega(e) <= Cw e^{1/10}, Cw = prod_{p < 1024} 2/p^{1/10}
    lcw = sum((lnU(2) - etaw * lnD(p) for p in range(2, 1024) if isprime(p)), Fr(0)); Cw = expU(lcw)
    SA = [(1 / L0lo + u, Fr(0), 1)]      # sum_{a in box} 1/a <= 1 + u L <= (1/L0 + u) L
    terms = []; worst = Fr(0); nbox = 0; used = {}
    for ia in range(M + 1):
        for idd in range(M + 1):
            for ic in range(M + 1):
                al, de, ga = ia * u, idd * u, ic * u
                if 2 * al + de > 1 or al + ga + de > 1: continue      # empty: a^2 d <= N/2, acd < N
                nbox += 1
                alp = min(al + u, (1 - de) / 2); dep = min(de + u, 1 - 2 * al); gap = min(ga + u, 1 - al - de)
                sg = al + ga + de; sgp = min(alp + gap + dep, Fr(1))
                nA, nC, nD = [(Fr(1), alp, 0)], [(Fr(1), gap, 0)], [(Fr(1), dep, 0)]
                pe = [(Fr(1, 4), 1 - sg, 0)]
                R = {}
                R['H'] = mul(mul(nA, nC), nD)
                R['A'] = mul(mul(pe, SA), SA) + mul(nA, nD)
                fw = (Fr(3), sg, Fr(4), sgp)
                R['C'] = mul(mul(nA, nD), cop(Fr(3), Fr(1), Fr(4), al + de, *fw))
                R['D'] = mul(mul(nC, nD), cop(Fr(5), 1 + 2 * gap + dep, Fr(4), ga + de, *fw))
                R['E'] = mul(mul(nA, nC), cop(Fr(2), 1 + gap, Fr(4), al + ga, *fw))
                es = (Fr(1, 4), 1 - sgp)                                # e > N^{1-sg+}/4
                bw = (Fr(1, 4), 1 - alp - dep, Fr(1, 2), 1 - al - de)   # b-window
                pF = mul(pe, SA) + nA
                R['F'] = mul(pF, min(cop(Fr(1, 2), 1 - al, *es, *bw), cop(Fr(1, 2), 1 - al, *es, Fr(1), de, Fr(1), dep), key=key))
                pG = mul(pe, SA) + nD
                om = [(Cw, etaw * (1 - sg), 0)]
                R['G'] = mul(mul(pG, om), min(cop(Fr(1, 2), 1 - de, *es, Fr(1), al, Fr(1), alp), cop(Fr(1, 2), 1 - de, *es, *bw), key=key))
                R['tau3'] = mul(pe + [(Fr(1), Fr(0), 0)], [(C3 * expU(-Fr(3, 10) * lnD(2)), Fr(3, 10), 0)])
                R['I'] = mul(nC, pF)
                k = min(R, key=lambda t: key(R[t]))
                used[k] = used.get(k, 0) + 1
                terms += R[k]; worst = max(worst, mx(R[k]))
    return terms, worst, nbox, used

def contribution(terms, b=Fr(32), db=Fr(1, 4), Kmin=19, Kmax=4001):
    """sum_{K odd >= Kmin} max_{N in [2^{Kb}, 2^{K(b+db)}]} bound(N) * 2 r^{-(K+1)/2}, r >= 2^b (terms increasing in N)."""
    tot = mp.mpf(0); ln2 = mp.log(2)
    for K in range(Kmin, Kmax + 1, 2):
        Lt = K * (b + db) * ln2
        t = sum(mp.mpf(c.numerator) / c.denominator * mp.e ** (mp.mpf(e.numerator) / e.denominator * Lt) * Lt ** p
                for (c, e, p) in terms) * mp.mpf(2) ** (1 - b * (K + 1) / 2)
        tot += t
        if t < mp.mpf(10) ** -40: break
    return tot, K, t

if __name__ == '__main__':
    M = int(sys.argv[1]) if len(sys.argv) > 1 else 32
    if len(sys.argv) > 2: W = int(sys.argv[2])
    terms, worst, nbox, used = tailP(M)
    ok = all(e >= 0 and p >= 0 for (c, e, p) in terms) and all(e < Fr(1, 2) and p <= (Fr(1, 2) - e) * L0lo for (c, e, p) in terms)
    G = sum(float(c) * math.exp(float(e - Fr(1, 2)) * float(L0hi)) * float(L0hi) ** p for (c, e, p) in terms)
    print(f"M={M} W={W} boxes {nbox} terms {len(terms)} max exponent {float(worst):.5f} monotone/decreasing {ok} "
          f"G=D_P(N0)/sqrt(N0) bound {G:.4e} routes {used}")
    tot, K, t = contribution(terms)
    print(f"P-tail contribution to S for r in [2^32, 2^32.25): {mp.nstr(tot, 8)} (summed to K={K}, last term {mp.nstr(t, 3)})")
