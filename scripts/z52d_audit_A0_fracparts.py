"""z52d audit A0, item Z1739: fractional parts {(p+u)/m}, m = 4uC−1, over the trial set 𝓡 = {(u,C): m ≤ p+u} (PARITY_AUDIT
Lemma 2.1). Compare the empirical law for primes p ≡ 1 (24) with random odd n ≡ 1 (24) of the same size, and with the
'Farey/divisor-problem' law of {N/m} for m uniform on [1,N]: P(frac ≤ t) = Σ_k t/(k(k+t)) (= ψ(1+t)+γ).
Reports Kolmogorov distance to that law, the bin-mass near 0 (fraction < 1/50), and the exact-zero count (= R(p)).
Usage: uv run --with numpy --with scipy python scripts/z52d_audit_A0_fracparts.py"""
import numpy as np
from scipy.special import digamma
def fracs(n):
    out = []
    u = 1
    while 3 * u - 1 <= n:  # C = 1 needs 4u-1 <= n+u
        Cmax = (n + u + 1) // (4 * u)
        C = np.arange(1, Cmax + 1, dtype=np.int64); m = 4 * u * C - 1; m = m[m <= n + u]
        out.append(((n + u) % m) / m)
        u += 1
    return np.concatenate(out)
def law(t): return digamma(1 + t) + np.euler_gamma
rng = np.random.default_rng(0)
def isprime(n): return n > 1 and all(n % d for d in range(2, int(n**0.5) + 1))
P = [p for p in range(10**6 + 1, 10**6 + 20000, 24) if isprime(p)][:6]
Nn = [n for n in rng.integers(10**6 // 24, (10**6 + 20000) // 24, 40) * 24 + 1 if not isprime(n)][:6]
for lab, ns in [('prime', P), ('composite', Nn)]:
    for n in ns:
        f = np.sort(fracs(n)); k = len(f)
        ks = np.max(np.abs(np.arange(1, k + 1) / k - law(f)))
        print(f"{lab:9s} n={n} |R|={k} zeros(R)={int((f == 0).sum())} KS-dist-to-divisor-law={ks:.5f} "
              f"(1/sqrt|R|={1/np.sqrt(k):.5f}) mass<0.02: {np.mean(f < 0.02):.5f} vs law {law(0.02):.5f}")
