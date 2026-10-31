"""z52d avenue P01 / Z1483: Type I hits at (c, d) require (d/p) = -1.

Lemma (PROVED, 3 lines): let p ≡ 1 (mod 4) be prime with gcd(p, cd) = 1. If f | p^2 + 4c^2 d and f ≡ -p (mod 4cd),
then f is coprime to 2cdp, -d is a square mod every prime factor of f, so
1 = (-d/f) = chi_{-4d}(f) = chi_{-4d}(-p) = -chi_{-4d}(p) = -(d/p).
The coprimality hypothesis is needed: (p, c, d, f) = (5, 1, 5, 15) is a degenerate hit with (d/p) = 0.
Hence d = 1 (and every square d) has NO Type I hits — Pass 1's 'surprise' is the BM/genus factor (1 - (d/p)),
the Type I analogue of M_BM's (1 - chi_{-4uB}(p)) (SYNTHESIS_SPARKS8 Lemma 4.1).
Check: 30 primes p ≡ 1 (4) just above 10^4, d ≤ 15, c ≤ 40 (so p ∤ cd).  Run: timeout 60 python3 scripts/z52d_avenue_typeI_dsign.py
"""
def isprime(m): return m > 1 and all(m % d for d in range(2, int(m ** .5) + 1))
def divisors(N):
    fac, m, q = {}, N, 2
    while q * q <= m:
        while m % q == 0: fac[q] = fac.get(q, 0) + 1; m //= q
        q += 1
    if m > 1: fac[m] = fac.get(m, 0) + 1
    ds = [1]
    for r, e in fac.items(): ds = [d * r ** i for d in ds for i in range(e + 1)]
    return ds
ps = [p for p in range(10001, 12000) if p % 4 == 1 and isprime(p)][:30]
viol, tot = 0, {}
for p in ps:
    for d in range(1, 16):
        leg = -1 if pow(d, (p - 1) // 2, p) == p - 1 else 1
        hits = sum(1 for c in range(1, 41) for f in divisors(p * p + 4 * c * c * d) if (f + p) % (4 * c * d) == 0)
        tot[(d, leg)] = tot.get((d, leg), 0) + hits
        viol += (leg == 1 and hits > 0)
print("violations (hits with (d/p) = +1):", viol)
assert viol == 0
print(sorted(tot.items()))
