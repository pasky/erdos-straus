"""z38_zero_law.py: empirical P(R*=0 | main term M) for odd non-square n in [lo, hi] vs the swap-Poisson prediction exp(-M/2)
(R* is even; R*/2 ~ Poisson(M/2)).  M = M_BM (col 4) or M_BM8 (col 5)."""
import sys, math
f, lo, hi, col = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])
bins = {}
for l in open(f):
    x = l.split(); n = int(x[0])
    if not (lo <= n <= hi) or math.isqrt(n) ** 2 == n: continue
    M = float(x[col]); b = int(M // 2) * 2
    t = bins.setdefault(b, [0, 0, 0.0, 0]); t[0] += 1; t[1] += (x[2] == '0'); t[2] += math.exp(-M / 2); t[3] += (x[1] == '1' and x[2] == '0')
print(f"n in [{lo},{hi}], M = col {col}: bin  N  zeros(primes)  predicted exp(-M/2)  ratio")
for b in sorted(bins):
    N, z, pr, zp = bins[b]
    if N >= 50: print(f"[{b},{b+2}) {N} {z}({zp}) {pr:.1f} {z/pr if pr > 0 else float('nan'):.2f}")
