"""zl_r0.py -- O228 (STERILE_LOWER.md §2): se_r0.py with (i) zl_tail.py value-selected tails at LP = 800 bits (P), LQ = 100 (Q),
(ii) extra certified tables data/zl/{P_q1_hi (2^600..2^800), P_q32, Q_q32 (2^24..2^34, 1/32-octave cells)}, (iii) r-ranges of width
2^{1/32} below 2^Bfine.  Usage: python3 zl_r0.py B0 [Bmax [Bfine]].
Based on se_r0.py -- O219 (STERILE_EXPLICIT.md §3.4). Combine the certified tables of se_box.c and the tails of se_tail.py
into the measure criterion
   S(r) = sum_{k odd} 2 D_Q(r^k) r^{-k} + sum_{K odd} 2 D_P(r^K) r^{-(K+1)/2}  <  (r-1)/(2r)
for every prime r >= 2^B0.  r is treated in ranges [2^b, 2^{b+1/4}), b = B0, B0+1/4, ..., < 2^Bmax; for r >= 2^Bmax all
N = r^K lie in the tail range and every term is decreasing in r (checked), so S(r) <= S(2^Bmax-range).
Tables: lines "j F ..." meaning D(N) <= F for all N in [2^{j/q}, 2^{(j+1)/q}).
Tails: se_tail.py term lists (c, e, p): D(N) <= sum c N^e (ln N)^p for N >= 2^{L0}.
Usage: python3 se_r0.py B0 [Bmax]      (fails closed: exit 1 if any range violates the criterion or a table is missing)."""
import sys, math
sys.path.insert(0, __file__.rsplit('/', 1)[0])
import os; os.environ.setdefault("SE_W", "40")
import zl_tail as se_tail
D = __file__.rsplit('/', 2)[0] + '/data/se/'
DZ = __file__.rsplit('/', 2)[0] + '/data/zl/'

def load(fn, q, base=None):
    T = {}
    for line in open((base or D) + fn):
        f = line.split()
        if len(f) >= 2 and f[0].lstrip('-').isdigit():
            j, v = int(f[0]), float(f[1])
            if not (math.isfinite(v) and v >= 0) or j in T: sys.exit(f"bad/duplicate table row {fn}: {line.strip()}")
            T[j] = (v * (1 + 1e-9), q)
    return T

def table_max(tabs, lo_bits, hi_bits):
    """max of certified F over quarter/full-octave cells covering [lo_bits, hi_bits); None if not fully covered."""
    best = 0.0
    x = lo_bits
    while x < hi_bits - 1e-12:
        got = None
        for T in tabs:                                   # prefer the finest table that has the cell
            q = next(iter(T.values()))[1]
            j = math.floor(x * q + 1e-12)
            if j in T: got = (T[j][0], (j + 1) / q); break
        if got is None: return None
        best = max(best, got[0]); x = got[1]
    return best

def agg(terms):
    """merge terms with equal p, rounding e UP to a 1e-6 grid (valid: N^e increases with e for N >= 1)."""
    A = {}
    for (c, e, p) in terms:
        # negative exponents are capped at 0 (c N^e <= c for N >= 1), so every merged term is nondecreasing in N
        k = (max(0.0, math.ceil(e * 1e6) / 1e6), p); A[k] = A.get(k, 0.0) + c
    return [(c, e, p) for (e, p), c in A.items()]
def tailw(terms, bits, wlog2):
    """sum_t c N^e (ln N)^p * 2^{wlog2} at N = 2^bits, computed in log space."""
    L = bits * math.log(2)
    return sum(math.exp(math.log(c) + e * L + p * math.log(L) + wlog2 * math.log(2)) for (c, e, p) in terms)

def main():
    verbose = bool(__import__('os').environ.get('ZL_VERBOSE'))
    B0 = float(sys.argv[1]); Bmax = float(sys.argv[2]) if len(sys.argv) > 2 else 800.0
    if not (B0 <= Bmax and Bmax >= 800.0): sys.exit("need B0 <= Bmax and Bmax >= 800 (all N in the tails beyond Bmax)")
    P1 = load('P_q1.txt', 1)
    P1.update({k: v for k, v in load('P_q1_hi.txt', 1, DZ).items() if k not in P1})
    P = [load('P_q32.txt', 32, DZ), load('P_q4.txt', 4), P1]
    Q = [load('Q_q32.txt', 32, DZ), load('Q_q4.txt', 4)]
    if __import__('os').environ.get('ZL_L2'):              # zl_box (l2-Minkowski, Lemma 2.1) tables take precedence where present
        P.insert(0, load('P_q32_l2.txt', 32, DZ)); Q.insert(0, load('Q_q32_l2.txt', 32, DZ))
    LP, LQ = 800.0, 100.0                                  # tail thresholds (bits)
    Bfine = float(sys.argv[3]) if len(sys.argv) > 3 else 34.0
    tP, wP, _, _ = se_tail.tailP(32, LP); tQ, wQ, _, _ = se_tail.tailQ(16, LQ)
    tP, tQ = agg(tP), agg(tQ)
    if not (wP < 0.5 and wQ < 1.0): sys.exit("tail exponents too large")
    LPn, LQn = LP * math.log(2), LQ * math.log(2)
    if not (all(e < 0.5 and p <= (0.5 - e) * LPn for (c, e, p) in tP) and all(e < 1 and p <= (1 - e) * LQn for (c, e, p) in tQ)):
        sys.exit("tail terms not decreasing relative to the weights")
    worst = (0, None); b = B0; bad = 0
    while b <= Bmax + 1e-9:
        step = 1 / 32 if b < Bfine - 1e-9 else 0.25
        bh = b + step
        S = 0.0
        for K in range(1, 100001, 2):                    # P part
            lo, hi = K * b, K * bh
            wl = 1 - b * (K + 1) / 2                     # log2 of 2 * r^{-(K+1)/2}
            v1 = table_max(P, lo, min(hi, LP)) if lo < LP else 0.0
            if v1 is None: print("missing P table", lo, hi); sys.exit(1)
            term = v1 * 2 ** wl if lo < LP else 0.0
            if hi > LP: term = max(term, tailw(tP, hi, wl))   # terms increasing in N: top of the range
            S += term
            if not math.isfinite(term): sys.exit("non-finite P term")
            if lo >= LP and term < 1e-30: break
        else: sys.exit("P series did not reach the cutoff")
        for k in range(1, 100001, 2):                    # Q part
            lo, hi = k * b, k * bh
            wl = 1 - b * k
            v1 = table_max(Q, lo, min(hi, LQ)) if lo < LQ else 0.0
            if v1 is None: print("missing Q table", lo, hi); sys.exit(1)
            term = v1 * 2 ** wl if lo < LQ else 0.0
            if hi > LQ: term = max(term, tailw(tQ, hi, wl))
            S += term
            if not math.isfinite(term): sys.exit("non-finite Q term")
            if lo >= LQ and term < 1e-30: break
        else: sys.exit("Q series did not reach the cutoff")
        S = S * (1 + 1e-6) + 1e-20                     # 1e-20: geometric remainder after the break
        lim = 0.5 - 2 ** (-b - 1)                         # (r-1)/(2r) for r >= 2^b
        if not (S < lim): bad += 1; print(f"FAIL b={b:.2f} S={S:.6f}")
        if verbose: print(f"b={b:.5f} S={S:.6f} lim={lim:.6f}")
        if S > worst[0]: worst = (S, b)
        b += step
    print(f"B0={B0} Bmax={Bmax}: max S = {worst[0]:.6f} at b = {worst[1]}; failures {bad}")
    sys.exit(1 if bad else 0)

if __name__ == '__main__':
    main()
