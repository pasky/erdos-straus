"""R27 small from-scratch checks: Prop 6.1 brute force; Thm 4.3 constants
(unit-square chi^2 values, (1-x)^-2 <= 1+4x, reduction uniformity);
Thm 3.1 pi(N) <= 1.25 N/log N threshold."""
import math, random
from sympy import primerange, nextprime, primepi

# ---- Prop 6.1: nu = sum_{p<=N, p in A} 1[n = p mod q], q prime in (N,2N]
random.seed(7)
bad = 0
for N in range(2, 1500):
    primes = list(primerange(2, N + 1))
    q = nextprime(N)
    assert q <= 2 * N
    for trial in range(3):
        A = [p for p in primes if random.random() < 0.5]
        Aset = set(A)
        nu = lambda m: sum(1 for p in A if (m - p) % q == 0)
        vals = {p: nu(p) for p in primes}
        ok = all(vals[p] == (1 if p in Aset else 0) for p in primes)
        ok &= sum(vals.values()) == len(A)
        # nu >= 0 everywhere trivially (nonneg coefficients); E nu = |A|/q
        bad += not ok
print("Prop 6.1 brute force N<1500, 3 random A each: failures =", bad)
print("  note E_U nu = |A|/q, so N*E_U nu = N|A|/q in [|A|/2, |A|): mean*N is NOT the count;"
      " the 'exact' value is sum over primes of nu, which needs the location of primes.")

# ---- Thm 4.3: unit squares mod p^v, chi^2 of uniform-on-squares vs uniform
def unit_squares(m):
    return sorted({(x * x) % m for x in range(m) if math.gcd(x, m) == 1})
for p, vmax in ((2, 7), (3, 5), (5, 4), (7, 3), (11, 2)):
    for v in range(1, vmax + 1):
        m = p ** v
        S = unit_squares(m)
        chi2 = m / len(S) - 1
        claim = (p + 1) / (p - 1) if p > 2 else None
        # reduction from p^vmax onto p^v uniform?
        big = p ** vmax
        Sb = unit_squares(big)
        cnt = {}
        for s in Sb: cnt[s % m] = cnt.get(s % m, 0) + 1
        uniform = set(cnt) == set(S) and len(set(cnt.values())) == 1
        print(f"  p^v={m}: #unit squares={len(S)} chi2={chi2:.4f} claim={claim} reduction uniform={uniform}")
        assert uniform and (claim is None or abs(chi2 - claim) < 1e-12) and chi2 <= 7
xs = [i / 10000 * 0.25 for i in range(10001)]
print("(1-x)^-2 <= 1+4x on [0,1/4]:", all((1 - x) ** -2 <= 1 + 4 * x + 1e-15 for x in xs))

# ---- Thm 3.1: N/(4A log N) >= pi(N)/(5A)  <=>  pi(N) <= 1.25 N / log N
last = None
for N in range(3, 200000, 1):
    if primepi(N) > 1.25 * N / math.log(N): last = N
print("last N < 2e5 with pi(N) > 1.25N/log N:", last)
