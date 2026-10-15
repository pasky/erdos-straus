"""review_zl_r1.py -- R231 round 2, FROM SCRATCH re-check of the §6 certificate (STERILE_LOWER Thm 6.3); does not import zl_r1/zl_r0.
For each certified cell j (r in [2^{j/32}, 2^{(j+1)/32})):
   S <= 2 (maxPQ_j + 2 #{ad <= Y} + engQ_j) / 2^{j/32}  +  sum_{K>=3 odd} 2 D_P(r^K) r^{-(K+1)/2}  +  sum_{k>=3 odd} 2 D_Q(r^k) r^{-k}
with the deeper terms from certified tables (min over covering cells, exact endpoints, 40-digit mpmath, rigorous geometric remainder)
and tails from review_zl_tail.py dumps.  Sweep cell lines are checked to have the exact integer endpoints ceil(2^{j/32}) (or +1 at an
even start, the sweep runs over odd n) and ceil(2^{(j+1)/32}) computed exactly here; a cell whose endpoints do not match is an ERROR,
not silently skipped.  #{ad <= Y} computed by brute force.
Usage: review_zl_r1.py SWEEPFILE A Y ENGFILE|none jmin [K3TABLES]   (K3TABLES=l2 adds the zl_box K=3/K=5 tables)"""
import sys, os, json
from fractions import Fraction as Fr
from mpmath import mp, mpf, exp
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import review_zl_combine as RC
from review_zl_combine import table, cover, agg, tailval, w2, LN2, PAD
mp.dps = 40

def ceil_pow(j):          # least integer n with n^32 >= 2^j, i.e. n >= 2^{j/32}, exact
    n = max(1, int(2 ** (j / 32)) - 2)
    while n ** 32 < 2 ** j: n += 1
    return n

def deeper(b, bh, P, Q, tP, tQ):
    LP, LQ = Fr(800), Fr(100); S = mpf(0); parts = {}
    for (kind, tabs, tl, Lt) in (("P", P, tP, LP), ("Q", Q, tQ, LQ)):
        last = None
        for K in range(3, 4001, 2):
            lo, hi = K * b, K * bh
            wl = 1 - b * (K + 1) / 2 if kind == "P" else 1 - b * K
            v = mpf(0)
            if lo < Lt:
                t = cover(tabs, lo, min(hi, Lt))
                if t is None: raise SystemExit(f"GAP {kind} K={K} [{float(lo)},{float(hi)})")
                v = t * w2(wl)
            if hi > Lt: v = max(v, tailval(tl, hi) * w2(wl))
            S += v; parts[(kind, K)] = v
            if lo >= Lt:
                last = K
                if v < mpf(10) ** -30: break
        else: raise SystemExit("cutoff not reached")
        Kl = last; rem = mpf(0)
        bb, bbh = mpf(b.numerator) / b.denominator, mpf(bh.numerator) / bh.denominator
        for (c, e, p) in tl:
            ee = mpf(e.numerator) / e.denominator
            if kind == "P":
                rho = exp((2 * ee * bbh - bb) * LN2) * (mpf(Kl + 2) / Kl) ** p
                t0 = 2 * c * exp((Kl * ee * bbh - bb * (Kl + 1) / 2) * LN2) * (Kl * bbh * LN2) ** p
            else:
                rho = exp((2 * ee * bbh - 2 * bb) * LN2) * (mpf(Kl + 2) / Kl) ** p
                t0 = 2 * c * exp((Kl * ee * bbh - bb * Kl) * LN2) * (Kl * bbh * LN2) ** p
            if not rho < mpf(95) / 100: raise SystemExit("remainder ratio")   # geometric remainder t0*rho/(1-rho), rigorous for any rho < 1
            rem += t0 * rho / (1 - rho)
        S += rem * PAD
    return S, parts

def main():
    sf, A, Y, ef, jmin = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), sys.argv[4], int(sys.argv[5])
    l2 = len(sys.argv) > 6 and sys.argv[6] == "l2"
    P = [table("data/zl/P_q32_k3.txt", 32), table("data/se/P_q4.txt", 4), table("data/se/P_q1.txt", 1),
         table("data/zl/P_q1_hi.txt", 1, jmax=799)]
    if l2: P += [table("data/zl/P_q32_k3_l2.txt", 32), table("data/zl/P_q32_k5_l2.txt", 32)]
    Q = [table("data/se/Q_q4.txt", 4)]
    if os.environ.get("MYK3"):     # independent: reviewer's own K=3 table + SE's reviewed tables only (no author k3/k5 tables)
        P = [table(os.environ["MYK3"], 32), table("data/se/P_q4.txt", 4), table("data/se/P_q1.txt", 1),
             table("data/zl/P_q1_hi.txt", 1, jmax=799)]
        print("MYK3: K=3 cells from", os.environ["MYK3"], "; K>=5 from SE tables / P_q1_hi")
    tP = agg(json.load(open("data/zl_review/tailP800_new.json")), Fr(1, 2), mpf(800) * LN2)
    tQ = agg(json.load(open("data/zl_review/tailQ100_new.json")), Fr(1), mpf(100) * LN2)
    ADY = 2 * sum(Y // a for a in range(1, Y + 1))
    eng = None
    if ef != "none":
        hdr = open(ef).readline()
        if f"ACUT={A}" not in hdr: raise SystemExit("engine header mismatch")
        eng = {int(l.split()[0]): mpf(l.split()[1]) for l in open(ef) if l[0].isdigit()}
    cells = {}
    for line in open(sf):
        f = line.split()
        if f and f[0] == "C": cells[int(f[1])] = tuple(int(x) for x in f[2:])
    X1 = max(v[1] for v in cells.values())
    if ef == "none" and not A > (X1 + 1) // 2: raise SystemExit("'none' needs every a < A swept: A > (X1+1)/2")
    worst = mpf(0); fails = 0; ok = []
    for j in sorted(cells):
        if j < jmin: continue
        lo, hi, mp_, mq, ms, cnt = cells[j]
        rlo, rhi = ceil_pow(j), ceil_pow(j + 1)
        if hi != rhi and hi == X1: continue                      # the sweep's last (partial) cell beyond the range end
        if not (hi == rhi and (lo == rlo or (lo == rlo + 1 and rlo % 2 == 0))):
            raise SystemExit(f"cell {j}: endpoints {lo},{hi} != exact {rlo},{rhi}")
        if max(mp_, mq) >= 65535: raise SystemExit(f"cell {j}: saturated")
        if eng is not None and j not in eng: raise SystemExit(f"missing engine row {j}")
        b = Fr(j, 32); bh = Fr(j + 1, 32)
        L1 = 2 * (ms + ADY + (eng[j] * (1 + mpf(10) ** -9) if eng else 0)) * w2(-b)
        Sd, parts = deeper(b, bh, P, Q, tP, tQ)
        S = (L1 + Sd) * PAD
        lim = mpf(1) / 2 - w2(-(b + 1))
        top = sorted(parts.items(), key=lambda kv: -kv[1])[:2]
        print(f"j={j} maxPQ={ms} L1={mp.nstr(L1, 6)} deeper={mp.nstr(Sd, 6)} S={mp.nstr(S, 8)} {'ok' if S < lim else 'FAIL'} top {[(k, mp.nstr(v, 4)) for k, v in top]}", flush=True)
        if not S < lim: fails += 1
        worst = max(worst, S); ok.append(j)
    if ok != list(range(min(ok), max(ok) + 1)): raise SystemExit(f"non-contiguous cells {ok}")
    print(f"{sf}: cells {min(ok)}..{max(ok)} ({len(ok)}), max S {mp.nstr(worst, 8)}, failures {fails}")
    sys.exit(1 if fails else 0)

main()
