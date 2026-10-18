"""z38_zero_bins.py: P(R*=0) by M_BM8 bin, primes vs composites (non-squares), n in [lo, hi] from a z38_mbm mode-1 file."""
import sys, math
lo, hi = int(sys.argv[2]), int(sys.argv[3])
bins = {}
for l in open(sys.argv[1]):
    n, isp, R, M0, MB, M8 = l.split(); n = int(n)
    if not (lo <= n <= hi) or math.isqrt(n) ** 2 == n: continue
    key = (int(isp), int(n) % 8, min(int(float(M8) // 4) * 4, 24))
    t = bins.setdefault(key, [0, 0]); t[0] += 1; t[1] += (R == '0')
for isp in (1, 0):
    for c in (1, 3, 5, 7):
        row = [(k[2], v[1], v[0]) for k, v in sorted(bins.items()) if k[0] == isp and k[1] == c]
        print(('prime' if isp else 'comp '), f"n≡{c}(8):", ' '.join(f"[{b},{b+4}):{z}/{N}" for b, z, N in row))
