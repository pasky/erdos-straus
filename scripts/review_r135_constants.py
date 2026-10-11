"""R135: numeric sanity of the (b2) constants in Thm 2.2 of LONGSHOT_PIGEONHOLE.md (from scratch)."""
from math import log
from sympy import primerange, divisor_count
# h = tau(n^2)^2 * mu at prime powers
assert all(divisor_count(2**(2*v))**2 - divisor_count(2**(2*v-2))**2 == 8*v for v in range(1, 30))
print("2-part sum:", 1 + sum(8*j*2**(-max(j-1, 0)) for j in range(1, 200)))
print("odd small-prime factor at l=3:", 1 + sum(8*v*3**(-(v-1)) for v in range(1, 200)), "= 1+8/(1-1/3)^2 =", 1+8/(1-1/3)**2)
P = 1.0; last = 3
for e in [10**k for k in range(2, 8)]:
    for l in primerange(last, e): P *= 1 + 8*l*l/(l-1)**3
    last = e
    print(f"e={e:>9}  prod_(3<=l<e)(1+8l^2/(l-1)^3)/(log e)^8 = {P/log(e)**8:.4f}")
