"""R170: from-scratch check of the Kronecker-Hurwitz relation quoted in GROWING_IDENTITIES §3."""
from fractions import Fraction
from math import isqrt
from review_gi_trace import h_w, divisors


def H(D):  # Hurwitz class number H(D), D >= 0
    if D == 0:
        return Fraction(-1, 12)
    if D % 4 in (1, 2):
        return Fraction(0)
    return sum((h_w(-D // (f * f)) for f in range(1, isqrt(D) + 1)
                if D % (f * f) == 0 and (D // (f * f)) % 4 in (0, 3)), Fraction(0))


bad = 0
for N in range(1, 400):
    lhs = sum(H(4 * N - t * t) for t in range(-isqrt(4 * N), isqrt(4 * N) + 1))
    rhs = 2 * sum(divisors(N)) - sum(min(d, N // d) for d in divisors(N))
    bad += lhs != rhs
print("KH: sum_t H(4N-t^2) = 2 sigma(N) - sum_{d|N} min(d,N/d), N<400: failures", bad)
