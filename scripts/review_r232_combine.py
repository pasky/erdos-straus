"""R232: FROM-SCRATCH combiner for criterion (S) of STERILE_EXPLICIT §3.1:
   S(r) = sum_{k odd} 2 D_Q(r^k) r^{-k} + sum_{K odd} 2 D_P(r^K) r^{-(K+1)/2}  <  (r-1)/(2r)   for every prime r >= 2^B0.
r-ranges [2^b, 2^{b+h}), h = 1/32 for b < 34, 1/4 above, up to 2^800 (beyond: every term is in the tail and decreasing in r).
Each term: (max certified table value over the N-cells covering [K b, K (b+h)) bits) * (largest weight, at r = 2^b);
for N above the table range: a tail term list sum c N^e (ln N)^p evaluated at the TOP of the N-range (terms increasing in N).
Level-1 tables (K = k = 1, b < 34) are R232's own exact-arithmetic tables (review_r232_box.py); higher levels use SE's
reviewed tables (data/se) and the author's se_box table P_q1_hi; tails: TAIL=se (SE's reviewed se_tail, N0 = 2^600 (P),
2^100 (Q), SE's route rule) or TAIL=zl (author's zl_tail, value-selected, N0 = 2^800 (P), 2^100 (Q)).
Evaluation in mpmath (40 digits), every table value padded up by 1e-9 relative. Fails closed (exit 1) on any gap.
Usage: review_r232_combine.py B0 cube|l2 se|zl"""
import sys, os
import mpmath as mp
mp.mp.dps = 40
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
B0 = mp.mpf(sys.argv[1]); VAR = sys.argv[2]; TAIL = sys.argv[3]

def load(path, q, jmin=None, jmax=None):
    T = {}
    for line in open(path):
        f = line.split()
        if not f or not f[0].lstrip('-').isdigit(): continue
        if f[1] == 'FAIL': continue
        j, v = int(f[0]), mp.mpf(f[1])
        if not (v >= 0 and mp.isfinite(v)): sys.exit(f"bad row {path} {line}")
        if j in T: sys.exit(f"duplicate row {path} {j}")
        if (jmin is None or j >= jmin) and (jmax is None or j <= jmax): T[j] = v * (1 + mp.mpf(10) ** -9)
    return (q, T)

R = ROOT + '/data/review_r232/'
mine = {'P': [load(R + 'P_q32_cube.txt', 32)], 'Q': [load(R + 'Q_q32_cube.txt', 32)]}
if VAR == 'l2':
    mine = {'P': [load(R + 'P_q32_l2.txt', 32)] + mine['P'], 'Q': [load(R + 'Q_q32_l2.txt', 32)] + mine['Q']}
SE = ROOT + '/data/se/'
hiP = [load(SE + 'P_q4.txt', 4), load(SE + 'P_q1.txt', 1), load(ROOT + '/data/zl/P_q1_hi.txt', 1, 600, 799)]
hiQ = [load(SE + 'Q_q4.txt', 4)]
LP = 800 if TAIL == 'zl' else 600; LQ = 100
if TAIL == 'se':   # with the SE tail from 2^600, the 600..800 table rows are not needed (use them anyway where present? no: tail only)
    hiP = hiP[:2]

sys.path.insert(0, HERE); os.environ.setdefault("SE_W", "40")
if TAIL == 'zl':
    import zl_tail as T
else:
    import se_tail as T
tP, wP, _, _ = T.tailP(32, LP); tQ, wQ, _, _ = T.tailQ(16, LQ)

def check_and_round(terms, h, L0bits):
    out = {}
    L0 = mp.mpf(L0bits) * mp.log(2)
    for (c, e, p) in terms:
        e_up = mp.mpf(max(0.0, e)) + mp.mpf(10) ** -9         # round up; negative exponents capped at 0 (N >= 1)
        if not (e < h - 1e-7 and p >= 0 and p <= (h - e_up) * L0): sys.exit(f"tail term not admissible: {(c, e, p)}")
        k = (e_up, p); out[k] = out.get(k, 0) + mp.mpf(c) * (1 + mp.mpf(10) ** -12)
    return [(c, e, p) for (e, p), c in out.items()]
tP, tQ = check_and_round(tP, 0.5, LP), check_and_round(tQ, 1.0, LQ)

def tail_at(terms, bits):    # sum c N^e (ln N)^p at N = 2^bits
    L = mp.mpf(bits) * mp.log(2)
    return sum(c * mp.exp(e * L) * L ** p for (c, e, p) in terms)

def tmax(tabs, lo, hi):
    """max over table cells covering [lo, hi) (bits); None if a gap."""
    best = mp.mpf(0); x = mp.mpf(lo)
    while x < hi:
        got = None
        for (q, T) in tabs:
            j = int(mp.floor(x * q))
            if j in T: got = (T[j], mp.mpf(j + 1) / q); break
        if got is None: return None
        best = max(best, got[0]); x = got[1]
    return best

def term(kind, K, b, bh):
    """D-bound for N in [2^{K b}, 2^{K bh})  (kind P or Q)."""
    lo, hi = K * b, K * bh
    L0 = LP if kind == 'P' else LQ
    tabs = (mine[kind] if K == 1 else []) + (hiP if kind == 'P' else hiQ)
    v = mp.mpf(0)
    if lo < L0:
        t = tmax(tabs, lo, min(hi, L0))
        if t is None: sys.exit(f"gap in {kind} tables at K={K} bits [{lo}, {hi})")
        v = t
    if hi > L0: v = max(v, tail_at(tP if kind == 'P' else tQ, hi))
    return v

worst = (0, None); fails = 0; b = B0
while b <= 800:
    h = mp.mpf(1) / 32 if b < 34 else mp.mpf(1) / 4
    bh = b + h; S = mp.mpf(0); tops = {}
    for kind in ('Q', 'P'):
        K = 1; prev = None
        while True:
            w = 2 * mp.mpf(2) ** (-b * K) if kind == 'Q' else 2 * mp.mpf(2) ** (-b * (K + 1) / 2)
            t = term(kind, K, b, bh) * w
            S += t
            if K <= 3: tops[f"{kind}{K}"] = t
            L0 = LP if kind == 'P' else LQ
            if K * b >= L0 and prev is not None and t < mp.mpf(10) ** -40 and t < prev / 2:
                S += t; break                  # remainder <= t (ratio < 1/2 and the ratio of tail terms decreases in K)
            prev = t; K += 2
            if K > 200001: sys.exit("series did not converge")
    lim = (1 - mp.mpf(2) ** (-b)) / 2
    if not S < lim: fails += 1; print(f"FAIL b={float(b)} S={float(S):.6f}")
    if S > worst[0]: worst = (S, b, tops)
    b = bh
print(f"B0={float(B0)} var={VAR} tail={TAIL}: max S = {float(worst[0]):.6f} at b = {float(worst[1])}", {k: float(v) for k, v in worst[2].items()}, f"failures {fails}")
sys.exit(1 if fails else 0)
