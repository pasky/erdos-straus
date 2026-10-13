"""R194 sanity check of review_tf_bm symbols: on complete TES solution sets at primes pi, the cubic
invariant of alpha_w at pi must be constant and non-zero (TWISTED_T1 Thm 3.2(a): order-3 T1), the quadratic one
may vary. Detects a symbol implementation that is identically trivial."""
from review_tf_zomega import solve_tes, canon_factor_prime, primes_upto, norm
from review_tf_bm import ResField, invariants
from collections import Counter
for N, pi in primes_upto(1100, inert_too=False):
    if N not in (307, 439, 601, 1009):
        continue
    S = solve_tes(pi, canon_factor_prime(pi))
    F = ResField(pi)
    c = Counter(invariants(x, y, z, (1, 0), F) for (x, y, z) in S)
    print(N, len(S), dict(c))
