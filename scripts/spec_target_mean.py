"""O123 §3 EVIDENCE: mean per-target count lambda_{c,d}(p) = #{f | p^2+4c^2 d : f = -p (mod 4cd), f <= p}
over primes p in [X, 2X) with chi_{-4d}(-p) = +1, normalised by log p/(c d); and fraction of empty targets."""
import sys, math
from sympy import primerange, divisors
from sympy.functions.combinatorial.numbers import jacobi_symbol
X = int(sys.argv[1]); K = int(sys.argv[2])
ps = list(primerange(X, X + K))
print(f"primes in [{X},{X+K}): {len(ps)}")
for d in [2, 3, 5, 6, 7, 10]:
    for c in [1, 2, 3, 5]:
        tot = n = empty = 0
        for p in ps:
            q = 4 * c * d
            # chi_{-4d}(-p): use any odd positive r = -p mod 4d coprime to d -> Kronecker(-4d, r) = jacobi(-4d mod r, r)
            r = (-p) % (4 * d)
            while math.gcd(r, 2 * d) != 1 or r == 0: r += 4 * d  # (should not happen for p > d)
            if jacobi_symbol((-4 * d) % r, r) != 1: continue
            m = p * p + 4 * c * c * d
            k = sum(1 for f in divisors(m) if f <= p and (f + p) % q == 0)
            tot += k; n += 1; empty += (k == 0)
        L = math.log(X)
        print(f"d={d:2d} c={c}: allowed p={n:4d} mean={tot/n:6.3f} mean*cd/L={tot/n*c*d/L:6.3f} empty={empty/n:5.2f}")
