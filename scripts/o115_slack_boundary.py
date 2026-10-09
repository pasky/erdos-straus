"""O115 diagnostic: locate candidates admitted by the 1e-9 safety slack of typei6_vsearch.c (author engine of
POINTWISE_TYPEI6 Comp 4.1) but rejected by the exact test of review_typei6_vsearch.c (R99).

Exact test (both engines' size condition, Lemma 3.1(b)):  c' P1 (64 c_o^4 d^8 - T^4) < u^2 c_o M T^4,
c_o = 7^a c', M = c_o d^2 + T, T = 2^{L-4}, u = 7^b; a, d, c' odd, 7 !| c', P1 | M.
Author admits P1 <= ratio*(1+1e-9), ratio = u^2 c_o M T^4 / (c' (64 c_o^4 d^8 - T^4)).
For each (a, d) and each odd P1 <= P1MAX the exact boundary in c' is found by bisection (the defect
is decreasing in c' once positive); the few c' just past it are tested for slack admission and P1 | M.
Restricted to P1 <= P1MAX (diagnostic only; not a completeness statement).
Usage: o115_slack_boundary.py L b [P1MAX]"""
import sys
from fractions import Fraction

L, b = int(sys.argv[1]), int(sys.argv[2])
P1MAX = int(sys.argv[3]) if len(sys.argv) > 3 else 99
T = 2 ** (L - 4); u2 = 7 ** (2 * b); T4 = T ** 4
SL = Fraction(10 ** 9, 10 ** 9 + 1)  # ratio >= 1/(1+1e-9)  <=>  P1 <= ratio*(1+1e-9) at the boundary


def lhs_rhs(p7a, cp, d, P1):
    co = p7a * cp; M = co * d * d + T
    return P1 * cp * (64 * co ** 4 * d ** 8 - T4), u2 * co * M * T4, M


def exact_ok(p7a, cp, d, P1):
    l, r, _ = lhs_rhs(p7a, cp, d, P1)
    return l < r


hits = []
a = 1
while exact_ok(7 ** a, 1, 1, 1):
    p7a = 7 ** a; d = 1
    while exact_ok(p7a, 1, d, 1):
        for P1 in range(1, P1MAX + 1, 2):
            if not exact_ok(p7a, 1, d, P1):
                break
            lo, hi = 1, 3  # largest odd-agnostic integer c' with exact_ok
            while exact_ok(p7a, hi, d, P1) or 64 * (p7a * hi) ** 4 * d ** 8 <= T4:
                lo, hi = hi, hi * 2
            while hi - lo > 1:
                mid = (lo + hi) // 2
                if exact_ok(p7a, mid, d, P1) or 64 * (p7a * mid) ** 4 * d ** 8 <= T4:
                    lo = mid
                else:
                    hi = mid
            for cp in range(hi, hi + 8):
                if cp % 2 == 0 or cp % 7 == 0:
                    continue
                l, r, M = lhs_rhs(p7a, cp, d, P1)
                if l < r or l <= 0:
                    continue
                if Fraction(r, l) >= SL and M % P1 == 0:
                    hits.append((a, cp, d, P1, float(1 - Fraction(r, l))))
        d += 2
    a += 2
print(f"L={L} b={b} P1<={P1MAX}: slack-only candidates {len(hits)}")
for h in hits:
    print("  a=%d c'=%d delta=%d P1=%d relative violation %.3g" % h)
