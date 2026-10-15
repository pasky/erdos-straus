"""R232 round 2: FROM-SCRATCH combiner for (S) on the 1/32-octave r-cells j of STERILE_LOWER §6, with
  level 1 (K = k = 1):  2 * max_{r in cell} (P(r) + Q(r)) / 2^{j/32}, P, Q = EXACT counts of ALL level-1 data (no a- or
                        ad-split) from review_r232_l1count.c (R232_QA=1), cell membership exact (2^j <= r^32 < 2^{j+1});
  K = 3:                R232's own exact-arithmetic box tables (review_r232_box.py P 32 j [l2]) where present;
  K >= 5, k >= 3:       SE's reviewed tables data/se/{P_q4, P_q1, Q_q4}.txt (NOT the author's new k3/k5 tables);
  tails:                SE's reviewed se_tail (P from 2^600, Q from 2^100; TAIL=se) or the author's zl_tail (TAIL=zl, P from 2^800,
                        then rows 600..799 of the author's P_q1_hi are needed).
mpmath 40 digits; tables padded up 1e-9; fails closed.  Usage: review_r232_combine2.py COUNTS.gz K3TABLE se|zl jlo jhi"""
import sys, os, gzip
import mpmath as mp
mp.mp.dps = 40
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
counts, k3file, TAIL, jlo, jhi = sys.argv[1], sys.argv[2], sys.argv[3], int(sys.argv[4]), int(sys.argv[5])

def load(path, q, jmin=None, jmax=None):
    T = {}
    for line in open(path):
        f = line.split()
        if not f or not f[0].lstrip('-').isdigit() or f[1] == 'FAIL': continue
        j, v = int(f[0]), mp.mpf(f[1])
        if not (v >= 0 and mp.isfinite(v)) or j in T: sys.exit(f"bad/duplicate row {path} {j}")
        if (jmin is None or j >= jmin) and (jmax is None or j <= jmax): T[j] = v * (1 + mp.mpf(10) ** -9)
    return (q, T)

L1 = {}
for line in gzip.open(counts, 'rt'):
    r, p, q, qy = map(int, line.split())
    j = (r ** 32).bit_length() - 1
    L1[j] = max(L1.get(j, 0), p + q)
SE = ROOT + '/data/se/'
P3 = load(k3file, 32)
Ptabs = [load(SE + 'P_q4.txt', 4), load(SE + 'P_q1.txt', 1)]
if TAIL == 'zl': Ptabs.append(load(ROOT + '/data/zl/P_q1_hi.txt', 1, 600, 799))
Qtabs = [load(SE + 'Q_q4.txt', 4)]
LP = 800 if TAIL == 'zl' else 600; LQ = 100
sys.path.insert(0, HERE); os.environ.setdefault("SE_W", "40")
T = __import__('zl_tail' if TAIL == 'zl' else 'se_tail')
tP, _, _, _ = T.tailP(32, LP); tQ, _, _, _ = T.tailQ(16, LQ)

def rnd(terms, h, L0bits):
    out = {}; L0 = mp.mpf(L0bits) * mp.log(2)
    for (c, e, p) in terms:
        eu = mp.mpf(max(0.0, e)) + mp.mpf(10) ** -9
        if not (e < h - 1e-7 and 0 <= p <= (h - eu) * L0): sys.exit(f"tail term not admissible {(c, e, p)}")
        out[(eu, p)] = out.get((eu, p), 0) + mp.mpf(c) * (1 + mp.mpf(10) ** -12)
    return [(c, e, p) for (e, p), c in out.items()]
tP, tQ = rnd(tP, 0.5, LP), rnd(tQ, 1.0, LQ)
def tail_at(terms, bits):
    L = mp.mpf(bits) * mp.log(2); return sum(c * mp.exp(e * L) * L ** p for (c, e, p) in terms)
def tmax(tabs, lo, hi):
    best = mp.mpf(0); x = mp.mpf(lo)
    while x < hi:
        got = None
        for (q, Tb) in tabs:
            j = int(mp.floor(x * q))
            if j in Tb: got = (Tb[j], mp.mpf(j + 1) / q); break
        if got is None: return None
        best = max(best, got[0]); x = got[1]
    return best
def term(kind, K, b, bh):
    lo, hi = K * b, K * bh; L0 = LP if kind == 'P' else LQ
    tabs = ([P3] if (kind == 'P' and K == 3) else []) + (Ptabs if kind == 'P' else Qtabs)
    v = mp.mpf(0)
    if lo < L0:
        t = tmax(tabs, lo, min(hi, L0))
        if t is None: sys.exit(f"gap {kind} K={K} [{lo},{hi})")
        v = t
    if hi > L0: v = max(v, tail_at(tP if kind == 'P' else tQ, hi))
    return v

worst = (0, None); fails = 0
for j in range(jlo, jhi + 1):
    if j not in L1: sys.exit(f"no level-1 counts for cell {j}")
    b = mp.mpf(j) / 32; bh = mp.mpf(j + 1) / 32
    S = 2 * L1[j] * mp.mpf(2) ** (-b); parts = {'L1': S}
    for kind in ('P', 'Q'):
        K = 3; prev = None
        while True:
            w = 2 * mp.mpf(2) ** (-b * (K + 1) / 2) if kind == 'P' else 2 * mp.mpf(2) ** (-b * K)
            t = term(kind, K, b, bh) * w; S += t
            if K <= 5: parts[f"{kind}{K}"] = t
            L0 = LP if kind == 'P' else LQ
            if K * b >= L0 and prev is not None and t < mp.mpf(10) ** -40 and t < prev / 2: S += t; break
            prev = t; K += 2
            if K > 200001: sys.exit("no convergence")
    lim = (1 - mp.mpf(2) ** (-b)) / 2
    ok = S < lim
    if not ok: fails += 1
    print(f"j={j} maxPQ={L1[j]} S={float(S):.6f} " + ' '.join(f"{k}={float(v):.5f}" for k, v in parts.items()) + (' ok' if ok else ' FAIL'))
    if S > worst[0]: worst = (S, j)
print(f"cells {jlo}..{jhi} tail={TAIL}: max S = {float(worst[0]):.6f} at j = {worst[1]}; failures {fails}")
sys.exit(1 if fails else 0)
