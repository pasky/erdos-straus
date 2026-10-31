"""z52d audit A0, item Z1139: 'density of states' near ES certificates.
For n and every pair x ≤ y with 4/n − 1/x − 1/y = a/b > 0 (reduced) and the third denominator ≥ y possible (b/a ≥ y),
record the reduced residual numerator a (a = 1 ⟺ an ES solution with z = b) and the raw numerator K = 4xy − n(x+y)
(gcd defect g = K/a). Histogram P(a = k), k ≤ 12, for primes p ≡ 1 (24) vs odd squares vs other n ≡ 1 (24).
Also the fraction of residuals a/b with a = 2 that are 2/b = 1/z + 1/z' with z' ≤ ... (a 4-term repair; for context only).
Usage: uv run --with numpy python scripts/z52d_audit_A0_dos.py"""
import numpy as np, math
def hist(n, kmax=12):
    H = np.zeros(kmax + 2, dtype=np.int64); tot = 0
    for x in range(n // 4 + 1, 3 * n // 4 + 1):
        e = 4 * x - n                        # 4/n − 1/x = e/(nx)
        ymax = (2 * n * x) // e              # y ≤ z  ⟺  e/(nx) ≤ 2/y
        y = np.arange(max(x, n * x // e + 1), ymax + 1, dtype=np.int64)
        K = e * y - n * x                    # e/(nx) − 1/y = K/(nxy)
        y = y[K > 0]; K = K[K > 0]
        den = n * x * y
        g = np.gcd(K, den); a = K // g
        tot += len(a)
        a = np.minimum(a, kmax + 1); H += np.bincount(a, minlength=kmax + 2)
    return H, tot
def isprime(n): return n > 1 and all(n % d for d in range(2, int(n**0.5) + 1))
groups = {'prime': [p for p in range(1201, 4000, 24) if isprime(p)][:8],
          'square': [m * m for m in range(35, 64, 2) if (m * m) % 24 == 1][:8],
          'other': [n for n in range(1201, 4000, 24) if not isprime(n) and math.isqrt(n) ** 2 != n][:8]}
for gname, ns in groups.items():
    Hs = np.zeros(14); T = 0
    for n in ns:
        H, tot = hist(n); Hs += H; T += tot
    P = Hs / T
    print(f"{gname:6s} n={ns} pairs={T}")
    print("   P(a=k)·10⁴, k=1..12:", " ".join(f"{1e4*P[k]:.2f}" for k in range(1, 13)), f"| a>12: {P[13]:.4f}")
    k = np.arange(2, 13); slope, icpt = np.polyfit(np.log(k), np.log(P[2:13]), 1)
    print(f"   power-law fit on k=2..12: P ≈ {math.exp(icpt):.4g}·k^{slope:.3f}; extrapolated k=1: {1e4*math.exp(icpt):.2f} vs observed {1e4*P[1]:.2f}")
