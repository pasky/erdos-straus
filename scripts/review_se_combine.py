"""R222: from-scratch recombination of the measure criterion (S) of STERILE_EXPLICIT §3.4 (independent of se_r0.py).
Inputs (treated as data): the author's tables data/se/{P_q4,P_q1,Q_q4}.txt and the tail monomial lists of se_tail.py
(dumped to /tmp/r222/tails.json; their derivation is audited separately in the review).
For each r-range [2^b, 2^{b+1/4}), b = 32, 32.25, ..., 600:
  S_hat(b) = sum_{K odd} 2 * 2^{-b(K+1)/2} * Dmax_P(K) + sum_{k odd} 2 * 2^{-bk} * Dmax_Q(k),
Dmax = max over table cells meeting the N-range [2^{Kb}, 2^{K(b+1/4)}) (cells located with exact rational arithmetic) and,
where the range reaches the tail (>= 2^600 P, >= 2^100 Q), the per-monomial maximum of c N^e (ln N)^p over the range
(handles negative e exactly: endpoints and the interior critical point). Series truncated with an explicit geometric
remainder bound (ratio of successive odd-index terms computed from the monomials, checked to be < 1 and decreasing).
Uses mpmath (60 digits).  Usage: uv run --with mpmath python scripts/review_se_combine.py [b_lo b_hi]"""
import sys, json, math
from fractions import Fraction as Fr
import mpmath as mp
mp.mp.dps = 60
def M(x): return mp.mpf(x.numerator) / x.denominator if isinstance(x, Fr) else mp.mpf(x)

def load(fn):
    T = {}
    for line in open('data/se/' + fn):
        f = line.split()
        if f and f[0].isdigit():
            j = int(f[0]); assert j not in T; v = mp.mpf(f[1]); assert v >= 0 and mp.isfinite(v); T[j] = v
    return T
P4, P1, Q4 = load('P_q4.txt'), load('P_q1.txt'), load('Q_q4.txt')
TL = json.load(open('/tmp/r222/tails.json'))
TP = [(mp.mpf(c), mp.mpf(e), int(p)) for c, e, p in TL['P']]
TQ = [(mp.mpf(c), mp.mpf(e), int(p)) for c, e, p in TL['Q']]
LP, LQ = Fr(600), Fr(100)

def tabmax(tabs, lo, hi):
    """max over cells meeting [lo, hi) bits; tabs = [(q, T)], finest first; error if uncovered."""
    best = mp.mpf(0); x = lo
    while x < hi:
        for (q, T) in tabs:
            j = math.floor(x * q)
            if j in T: best = max(best, T[j]); x = Fr(j + 1, q); break
        else: raise SystemExit(f"uncovered N-range at {float(x)} bits")
    return best

import numpy as np
def _arr(terms):
    g = {}
    for c, e, p in terms: g[(float(e), p)] = g.get((float(e), p), 0.0) + float(c)
    k = list(g)
    return np.array([g[x] for x in k]), np.array([x[0] for x in k]), np.array([float(x[1]) for x in k])
ARR = {}
def tailmax(terms, lo, hi, wlog2=0):
    """sum over monomials of max_{N in [2^lo, 2^hi]} c N^e (ln N)^p (each maximised separately); float64 in log space,
    inflated by 1e-9 relative (all logs here are < 1e4, double error ~1e-12 relative)."""
    key = id(terms)
    if key not in ARR: ARR[key] = _arr(terms)
    c, e, p = ARR[key]
    L0, L1 = float(lo) * math.log(2), float(hi) * math.log(2)
    lf = lambda L: np.log(c) + e * L + p * np.log(L)
    best = np.maximum(lf(L0), lf(L1))
    with np.errstate(divide='ignore', invalid='ignore'):
        Lc = np.where((e < 0) & (p > 0), -p / np.where(e < 0, e, -1.0), -1.0)
    inside = (Lc > L0) & (Lc < L1)
    if inside.any(): best = np.where(inside, np.maximum(best, lf(np.where(inside, Lc, L0))), best)
    return mp.mpf(float(np.exp(best + float(wlog2) * math.log(2)).sum())) * (1 + mp.mpf('1e-9'))   # weighted

def S_of(b):
    bh = b + Fr(1, 4); S = mp.mpf(0); parts = {}
    for mode in 'PQ':
        terms, Lt = (TP, LP) if mode == 'P' else (TQ, LQ)
        tabs = [(4, P4), (1, P1)] if mode == 'P' else [(4, Q4)]
        prev = None; K = 1
        while True:
            lo, hi = K * b, K * bh
            wlog2 = 1 - b * (K + 1) / 2 if mode == 'P' else 1 - b * K
            t = mp.mpf(0)
            if lo < Lt: t = tabmax(tabs, lo, min(hi, Lt)) * mp.mpf(2) ** M(wlog2)
            if hi > Lt: t = max(t, tailmax(terms, max(lo, Lt), hi, wlog2))
            S += t; parts[(mode, K)] = t
            if lo >= Lt and K >= 3:
                # ratio bound for all later odd indices: each monomial's weighted max at K+2 over its value at K
                # (all later ranges are in the tail; monomial-wise ratio, taken as max over monomials and K' >= K)
                h = mp.mpf(1) / 2 if mode == 'P' else mp.mpf(1)
                if id(terms) not in ARR: ARR[id(terms)] = _arr(terms)
                _, ea, pa = ARR[id(terms)]
                rho = mp.mpf(float(np.max(2.0 ** (2 * (np.maximum(ea, 0) * float(bh) - float(h) * float(b))) * ((K + 2) / K) ** pa))) * (1 + mp.mpf('1e-9'))
                if rho < mp.mpf('0.9') and t < mp.mpf('1e-40'):
                    S += t * rho / (1 - rho); break
            K += 2
            if K > 20001: raise SystemExit("no convergence")
    return S, parts

if __name__ == '__main__':
    blo = Fr(sys.argv[1]) if len(sys.argv) > 1 else Fr(32); bhi = Fr(sys.argv[2]) if len(sys.argv) > 2 else Fr(600)
    b = blo; worst = (mp.mpf(0), None); fails = 0; n = 0
    while b <= bhi:
        S, parts = S_of(b); n += 1
        lim = mp.mpf(1) / 2 - mp.mpf(2) ** (-M(b) - 1)
        if not S < lim: fails += 1; print("FAIL", float(b), mp.nstr(S, 8))
        if S > worst[0]: worst = (S, b, parts)
        b += Fr(1, 4)
    S, bw, parts = worst
    top = sorted(parts.items(), key=lambda kv: -kv[1])[:6]
    print(f"ranges {n}, failures {fails}, max S_hat = {mp.nstr(S, 8)} at b = {float(bw)}; top terms:",
          ", ".join(f"{m}{K}:{mp.nstr(v, 4)}" for (m, K), v in top))
