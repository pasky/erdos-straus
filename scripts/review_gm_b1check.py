"""R201: brute-force cross-check of the complete B = 1 criterion in review_gm_least.b1_pairs, and of the
bound A <= 3(n+1)/2, g <= 2n(n+1) (GROWING_MUTE Prop 3.1) on the B = 1 slice, for all odd n <= NMAX.
Brute force: every even A <= 2n + 4 (a priori bound from A(4 lam kap - n) = 2(lam+kap)), every divisor g of
nA^2 + 1 with g = -1 (mod 2A).
Usage: PYTHONPATH=scripts uv run --with sympy python scripts/review_gm_b1check.py NMAX
"""
import sys
from review_gm_least import b1_pairs, divs


def brute(n):
    out = set()
    for A in range(2, 2 * n + 5, 2):
        for g in divs(n * A * A + 1):
            if (g + 1) % (2 * A) == 0:
                out.add(((g + 1) // (2 * A), A, g))
    return out


NMAX = int(sys.argv[1])
worstA = worstg = 0
for n in range(3, NMAX + 1, 2):
    b = brute(n)
    fast = {(lam, A, 2 * lam * A - 1) for lam, kap, A in b1_pairs(n)}
    assert b == fast, (n, b ^ fast)
    for lam, A, g in b:
        worstA = max(worstA, A / (3 * (n + 1) / 2))
        worstg = max(worstg, g / (2 * n * (n + 1)))
print(f'odd n <= {NMAX}: brute == complete criterion; max A/(3(n+1)/2) = {worstA:.4f}, max g/(2n(n+1)) = {worstg:.4f}')
