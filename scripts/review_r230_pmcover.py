"""R230 from scratch: which primes h = 3 (mod 4) have Type II class sets {-4 c^2 d mod h : c d | (h+1)/4} covering all
quadratic non-residues mod h (the classes are always QNRs: check that too).  Also tau_3(K) < 2K-1 tail check and
the constant C3 = prod_p max_a (a+1)/p^(a/3) with tau(n) <= C3 n^(1/3)."""
import sys
from sympy import primerange, divisors, legendre_symbol, divisor_count

H = int(sys.argv[1]) if len(sys.argv) > 1 else 20000
cover = []
for h in primerange(3, H + 1):
    if h % 4 != 3: continue
    K = (h + 1)//4
    cls = set()
    for m in divisors(K):
        for c in divisors(m):
            d = m // c
            r = (-4*c*c*d) % h
            assert r != 0 and legendre_symbol(r, h) == -1, (h, c, d)
            cls.add(r)
    if len(cls) == (h - 1)//2:
        cover.append(h)
print(f"h <= {H}: covering h = {cover}; all classes QNR")

# C3
C3 = 1.0
for p in primerange(2, 100):
    C3 *= max(1.0, max((a + 1)/p**(a/3) for a in range(1, 40)))
print(f"C3 = {C3:.4f}; tau3(K) <= (C3 K^(1/3))^2 < 2K-1 for K > {((C3**2)/2)**3:.0f}")
# tau3 <= tau^2 tail check up to K for which bound kicks in
bad = [K for K in range(1, int(((C3**2)/2)**3) + 2) if sum(divisor_count(m) for m in divisors(K)) >= 2*K - 1]
print("K with tau3(K) >= 2K-1:", bad)
