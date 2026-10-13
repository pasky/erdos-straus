"""review_da_thm25.py (R178, from scratch): the union bound of DEPTH_ASPECT Thm 2.5.

Relative (to one c-slice, mass q^-2) covered mass, k = 2:
  Case B: sum_{s>=3} sum_{patterns} 16^s * q^{m(pattern)} * q^{1 - ceil(s/2)}
          patterns (a,b,z,y,t): a,b>=1, z=s-a-b>=0, y>=0, t>=2, y+t<=max(a,b);
          m = min(t-2, y+z, a'-1+y, a'-1+z) with a' = min(a,b)   (Lemma 2.2; B(s) <= 16^s since
          delta(n) <= 2^n, delta_3(n) <= 3^n)
  Case A: sum_{alpha>=1} sum_{(lam,beta,kap)} 4*6^alpha * q^{e} * q^{-alpha}
          beta>=0, kap>=1, f=alpha-beta-kap>=0, lam<=max(f,beta) (z != 0);
          e = min(f, alpha-f-1) if f>=beta else min(beta-lam, lam+alpha-beta-1)  (Lemma 2.4)
Positive terms summed in double precision from log-space values (relative error < 1e-9 overall; reported with 2
significant digits), plus a rigorous geometric tail beyond S (crude per-level bounds of the document).
usage: uv run python scripts/review_da_thm25.py
"""
import math


def caseB(lq, S):
    tot = 0.0
    for s in range(3, S + 1):
        base = s * math.log(16) + (1 - (s + 1) // 2) * lq
        for a in range(1, s):
            for b in range(1, s - a + 1):
                z = s - a - b; ap = min(a, b); mx = max(a, b)
                for t in range(2, mx + 1):
                    Y = mx - t                       # y = 0..Y
                    c1 = min(t - 2, ap - 1 + z); c2 = min(z, ap - 1)
                    # m(y) = min(c1, y + c2)
                    for y in range(0, Y + 1):
                        m = min(c1, y + c2)
                        tot += math.exp(base + m * lq)
                        if y + c2 >= c1:             # constant from here on
                            tot += (Y - y) * math.exp(base + c1 * lq)
                            break
    return tot


def caseA(lq, S):
    tot = 0.0
    for al in range(1, S + 1):
        base = math.log(4) + al * math.log(6) - al * lq
        for beta in range(0, al):
            for kap in range(1, al - beta + 1):
                f = al - beta - kap
                for lam in range(0, max(f, beta) + 1):
                    e = min(f, al - f - 1) if f >= beta else min(beta - lam, lam + al - beta - 1)
                    tot += math.exp(base + e * lq)
    return tot


def tail(lq, S):
    """s >= S: Case B per level <= (s+1)^4 16^s q^{-(s/10+1/5)}; Case A per level <= (a+1)^3 4 6^a q^{-(a+1)/2}.
    Consecutive-term ratio <= ((S+2)/(S+1))^k * base^1, so tail <= first/(1-r)."""
    rB = ((S + 2) / (S + 1)) ** 4 * 16 * math.exp(-lq / 10)
    rA = ((S + 2) / (S + 1)) ** 3 * 6 * math.exp(-lq / 2)
    if rB >= 1 or rA >= 1:
        return float("inf")
    fB = math.exp(4 * math.log(S + 1) + S * math.log(16) - (S / 10 + 0.2) * lq)
    fA = math.exp(3 * math.log(S + 1) + math.log(4) + S * math.log(6) - (S + 1) / 2 * lq)
    return fB / (1 - rB) + fA / (1 - rA)


def crude(lq, S=5000):
    """the document's closed form 4 sum_s (s+1)^4 (16 q^-1/10)^s q^-1/5 + 24 sum_a (a+1)^3 (16 q^-1/2)^a q^-1/2."""
    A = sum(4 * math.exp(4 * math.log(s + 1) + s * (math.log(16) - lq / 10)) for s in range(1, S)) * math.exp(-lq / 5)
    B = sum(24 * math.exp(3 * math.log(a + 1) + a * (math.log(16) - lq / 2)) for a in range(1, 400)) * math.exp(-lq / 2)
    return A + B


if __name__ == "__main__":
    import sys
    S = int(sys.argv[1]) if len(sys.argv) > 1 else 100
    for r in range(26, 35):
        lq = r * math.log(3)
        B, A, tl = caseB(lq, S), caseA(lq, S), tail(lq, S + 1)
        print("r=%d S=%d caseB=%.3e caseA=%.3e tail=%.3e TOTAL=%.3e" % (r, S, B, A, tl, A + B + tl), flush=True)
    for name, lq in (("3^34", 34 * math.log(3)), ("1.3e16", math.log(1.3e16)), ("1.2e16", math.log(1.2e16)), ("3^33", 33 * math.log(3))):
        print("crude closed form at q=%s: %.4f" % (name, crude(lq)), flush=True)
    # threshold of the crude form
    lo, hi = math.log(1e15), math.log(1e17)
    for _ in range(60):
        mid = (lo + hi) / 2
        if crude(mid) < 1: hi = mid
        else: lo = mid
    print("crude form < 1 iff q > %.4e" % math.exp(hi))
