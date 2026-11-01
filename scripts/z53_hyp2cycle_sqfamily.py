"""z53_hyp2cycle_sqfamily.py — Prop S family: for primes q = 1 (4), q >= 11, a in (q/2,q) with a^2 = -1 (q),
m = (q+1)(a-1)+1; prints m^2 (one per line) for the scan binary, and asserts the 2-cycle {q, q+1} directly."""
from sympy import primerange, sqrt_mod, integer_nthroot
import sys
Q = int(sys.argv[1]) if len(sys.argv) > 1 else 3000
for q in primerange(11, Q):
    if q % 4 != 1: continue
    a = [r for r in sqrt_mod(-1, q, all_roots=True) if q / 2 < r < q][0]
    m = (q + 1) * (a - 1) + 1
    n = m * m; U = integer_nthroot(n, 4)[0]
    assert m % 2 == 1 and U < q and q + 1 <= 2 * U and (n + 2 * q + 1) % (q * (q + 1)) == 0
    k = (n + 2 * q + 1) // (q * (q + 1)); assert k % 4 != 0
    print(n)
