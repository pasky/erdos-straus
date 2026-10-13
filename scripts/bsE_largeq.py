"""bsE_largeq.py (O178): explicit evaluation of the union bound of DEPTH_ASPECT Thm 2.5.
Upper bound for the relative covered mass of a c-slice (A = T^2) by all Case B (Lemma 2.2, pattern-wise min of the
four reconstruction bounds with crude divisor multiplicities 2^n, 3^n) and all Case A (Lemma 2.4) families.
Prints, for q = 3^r, the bound; the theorem needs bound < 1.  Sums are truncated at SMAX with a geometric tail check.
usage: uv run python scripts/bsE_largeq.py [SMAX]"""
import sys
from math import ceil, log, exp
L2, L3 = log(2), log(3)

def caseB(q, s):
    lq = log(q)
    tot = 0.0
    for a in range(1, s):
        for b in range(a, s - a + 1):
            z = s - a - b
            for y in range(0, b + 1):
                for t in range(2, b - y + 1):
                    B1 = L2 + (t - 2) * lq + s * L3
                    B2 = (y + z) * lq + (y + z) * L2 + (s + 2 * y + z) * L2
                    B3 = (a - 1 + y) * lq + (s + y) * L2
                    B4 = (a - 1 + z) * lq + max(s, z + 2 * a) * L2
                    tot += (1 if a == b else 2) * exp(min(B1, B2, B3, B4) + (1 - ceil(s / 2)) * lq)
    return tot

def caseA(q, al):
    lq = log(q)
    tot = 0.0
    for be in range(0, al):
        for ka in range(1, al - be + 1):
            f = al - be - ka
            for lam in range(0, max(f, be) + 1):
                if f >= be:
                    c = min(log(24) + f * lq + al * L3, L2 + (be + ka - 1) * lq + 3 * al * L2)
                else:
                    c = min(log(24) + (be - lam) * lq + al * L3, log(4) + (lam + al - be - 1) * lq)
                tot += exp(c + ka * L2 - al * lq)
    return tot

def tails(q, SMAX):
    """crude analytic tails beyond SMAX: Case B: (s+1)^4 patterns (x2 for a>b) * 2*16^s * q^(-s/10-1/5);
    Case A: (al+1)^3 patterns * 24*8^al * 2^al * q^(-(al+1)/2).  Geometric sums (valid when ratio < 1)."""
    lq = log(q)
    rB = exp(log(16) - lq / 10); rA = exp(log(16) - lq / 2)
    if rB >= 1 or rA >= 1:
        return float("inf")
    def tail(r, n0, deg):  # sum_{n>n0} (n+1)^deg r^n  <= (n0+2)^deg r^(n0+1) / (1 - r*((n0+3)/(n0+2))^deg)
        rr = r * ((n0 + 3) / (n0 + 2)) ** deg
        return float("inf") if rr >= 1 else (n0 + 2) ** deg * r ** (n0 + 1) / (1 - rr)
    return 4 * exp(-lq / 5) * tail(rB, SMAX, 4) + 24 * exp(-lq / 2) * tail(rA, SMAX, 3)

if __name__ == "__main__":
    SMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 60
    for r in range(1, 80):
        q = 3.0 ** r
        sb = sum(caseB(q, s) for s in range(3, SMAX + 1))
        sa = sum(caseA(q, al) for al in range(1, SMAX + 1))
        tl = tails(q, SMAX)
        print("q=3^%d  caseB(s<=%d) %.3e  caseA %.3e  tails %.3e  total %.3e" % (r, SMAX, sb, sa, tl, sb + sa + tl))
        if sb + sa + tl < 1:
            break
