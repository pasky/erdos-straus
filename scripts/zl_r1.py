"""zl_r1.py -- O228 (STERILE_LOWER.md §6). Certificate of (S) on r-ranges [2^{j/32}, 2^{(j+1)/32}) covered by a joint level-1
sweep (zl_sweep.c).  For such a range the level-1 terms (P at K = 1, Q at k = 1) are bounded by
   2 * ( maxPQ_j + 2 * #{(a,d): a d <= Y} + engQ_A(j) ) / 2^{j/32}
where maxPQ_j = max over primes r in the range of (#P-data of r) + (#Q-data of r with a < A, ad > Y)   [zl_sweep, exact],
2 * #{ad <= Y} bounds the Q-data with ad <= Y (<= 2 per (a, d): M17C Lemma 2.1(iv)), and engQ_A(j) is the zl_boxa bound
(ACUT = A) for the Q-data with a >= A on the N-cell j.  All deeper terms (K >= 3, k >= 3, tails) exactly as zl_r0.py.
Usage: python3 zl_r1.py SWEEPFILE A Y ENGFILE [SWEEPFILE A Y ENGFILE ...]   (fails closed; exit 1 on any failure)."""
import sys, math, os
sys.path.insert(0, __file__.rsplit('/', 1)[0])
os.environ.setdefault("SE_W", "40")
import zl_r0
from zl_r0 import load, table_max, agg, tailw, DZ
import zl_tail as se_tail

def Dsum(Y):                                   # #{(a,d) : a d <= Y} exactly
    s = 0; a = 1
    while a <= Y:
        q = Y // a; a2 = Y // q; s += q * (a2 - a + 1); a = a2 + 1
    return s

def deeper(P, Q, tP, tQ, b, bh, LP, LQ):
    S = 0.0
    for K in range(3, 100001, 2):
        lo, hi = K * b, K * bh; wl = 1 - b * (K + 1) / 2
        v1 = table_max(P, lo, min(hi, LP)) if lo < LP else 0.0
        if v1 is None: sys.exit(f"missing P table {lo} {hi}")
        term = v1 * 2 ** wl if lo < LP else 0.0
        if hi > LP: term = max(term, tailw(tP, hi, wl))
        S += term
        if lo >= LP and term < 1e-30: break
    else: sys.exit("P series did not reach the cutoff")
    for k in range(3, 100001, 2):
        lo, hi = k * b, k * bh; wl = 1 - b * k
        v1 = table_max(Q, lo, min(hi, LQ)) if lo < LQ else 0.0
        if v1 is None: sys.exit(f"missing Q table {lo} {hi}")
        term = v1 * 2 ** wl if lo < LQ else 0.0
        if hi > LQ: term = max(term, tailw(tQ, hi, wl))
        S += term
        if lo >= LQ and term < 1e-30: break
    else: sys.exit("Q series did not reach the cutoff")
    return S

def main():
    P1 = load('P_q1.txt', 1); P1.update({k: v for k, v in load('P_q1_hi.txt', 1, DZ).items() if k not in P1})
    P = [load('P_q32.txt', 32, DZ), load('P_q4.txt', 4), P1]
    Q = [load('Q_q32.txt', 32, DZ), load('Q_q4.txt', 4)]
    LP, LQ = 800.0, 100.0
    tP, wP, _, _ = se_tail.tailP(32, LP); tQ, wQ, _, _ = se_tail.tailQ(16, LQ)
    tP, tQ = agg(tP), agg(tQ)
    LPn, LQn = LP * math.log(2), LQ * math.log(2)
    if not (all(e < 0.5 and p <= (0.5 - e) * LPn for (c, e, p) in tP) and all(e < 1 and p <= (1 - e) * LQn for (c, e, p) in tQ)):
        sys.exit("tail terms not decreasing relative to the weights")
    args = sys.argv[1:]; bad = 0; worst = (0, None); done = []
    for i in range(0, len(args), 4):
        sf, A, Y, ef = args[i], int(args[i + 1]), int(args[i + 2]), args[i + 3]
        ADY = 2 * Dsum(Y)
        eng = {}
        if ef == 'none':
            # all rows a < A swept: a Q-datum of F has a <= acd <= (F+1)/2 (M17D Lemma 2.2(ii)), so none has a >= A if A > (X1+1)/2
            X1s = max(int(l.split()[3]) for l in open(sf) if l.startswith('C '))
            if not A > (X1s + 1) // 2 + 1: sys.exit("ENGFILE none needs A > (X1+1)/2 + 1")
            eng = None
        else:
            for line in open(ef):
                f = line.split()
                if f and f[0].isdigit(): eng[int(f[0])] = float(f[1]) * (1 + 1e-9)
            hdr = open(ef).readline()
            if f"ACUT={A}" not in hdr: sys.exit(f"{ef}: header lacks ACUT={A}: {hdr}")
        for line in open(sf):
            f = line.split()
            if not f or f[0] != 'C': continue
            j, lo, hi, mp, mq, ms, cnt = int(f[1]), int(f[2]), int(f[3]), int(f[4]), int(f[5]), int(f[6]), int(f[7])
            b = j / 32; rlo, rhi = math.ceil(2 ** b), math.ceil(2 ** ((j + 1) / 32))
            if not (hi == rhi and (lo == rlo or (lo == rlo + 1 and rlo % 2 == 0))): continue   # partial cell: not certified here (sweep starts at odd X0)
            if ms >= 131070 or mp == 65535 or mq == 65535: bad += 1; print(f"FAIL j={j}: counter overflow"); continue
            if eng is not None and j not in eng: sys.exit(f"missing engine row j={j}")
            ej = 0.0 if eng is None else eng[j]
            L1 = 2 * (ms + ADY + ej) / 2 ** b
            S = (L1 + deeper(P, Q, tP, tQ, b, b + 1 / 32, LP, LQ)) * (1 + 1e-6) + 1e-20
            lim = 0.5 - 2 ** (-b - 1)
            ok = S < lim
            print(f"j={j} b={b:.5f} primes={cnt} maxPQ={ms} ADY={ADY} engQ={ej:.4e} L1={L1:.5f} S={S:.6f} {'ok' if ok else 'FAIL'}")
            if not ok: bad += 1
            if S > worst[0]: worst = (S, b)
            done.append(j)
    print(f"cells certified: {len(done)} (j = {min(done) if done else None}..{max(done) if done else None}); max S = {worst[0]:.6f}; failures {bad}")
    sys.exit(1 if bad else 0)

if __name__ == '__main__':
    main()
