"""z5_sqpm_prime.py — prime-modulus words for SQ_± (CAP_GROWING §3).

A word (t,u,v) of X_n (tuv − u − v = n, tuv ≠ 0) with A = tu − 1 = ±l, l prime: then l | n + u, u | l+1 (A = l)
or u | l−1 (A = −l, signed), and for n ≡ 1 (mod 4) χ = (−A/n) = (n/l) = (−u/l). So n fires at prime l iff
n ≡ −u (mod l) for some u ∈ ±div(l+1) ∪ ±div(l−1) with (−u/l) = −1 (and n + u ≠ 0).
Marks all such n ≤ N (n ≡ 1 mod 8) by residue-class sieving over primes l ≤ N + max|u|, then reports the
non-squares with no prime-modulus word, the class sum Σ ω(l)/l, and the odd-square control.
usage: z5_sqpm_prime.py N
"""
import sys, math
import numpy as np
from sympy import primerange, divisors, legendre_symbol

def main():
    N = int(sys.argv[1])
    fired = np.zeros(N + 1, dtype=bool)
    Ssum = 0.0
    for l in primerange(3, 2 * N + 3):
        us = set()
        for m in (l + 1, l - 1):
            for d in divisors(m):
                us.add(d); us.add(-d)
        cls = set()
        for u in us:
            if legendre_symbol((-u) % l, l) == -1:
                cls.add((-u) % l)
        if l <= N: Ssum += len(cls) / l
        for c in cls:
            # n ≡ c (mod l); need n + u != 0 automatically for n > 0 unless u = -n; harmless (n=l-... tiny)
            start = c if c > 0 else l
            fired[start::l] = True
    bad = [n for n in range(9, N + 1, 8) if not fired[n] and math.isqrt(n) ** 2 != n]
    sq = [n for n in range(9, N + 1, 8) if fired[n] and math.isqrt(n) ** 2 == n]
    print(f"N={N} sum_l omega/l (l<=N) = {Ssum:.2f}  (log N = {math.log(N):.2f})")
    print(f"non-squares n≡1(8) without prime-modulus word: {len(bad)}; first: {bad[:30]}")
    print(f"odd squares n≡1(8) marked (must be 0 by T1): {len(sq)}")

if __name__ == "__main__":
    main()
