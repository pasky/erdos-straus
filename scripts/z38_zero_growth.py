"""z38_zero_growth.py: growth of the zero set of R* over odd non-square n <= K (all n, and by M_BM8 threshold c*L^2)."""
import sys, math
data = []
for l in open(sys.argv[1]):
    f = l.split(); n = int(f[0])
    if math.isqrt(n) ** 2 == n: continue
    data.append((n, int(f[1]), int(f[2]), float(f[4]), float(f[5])))
Ks = [10**4, 3*10**4, 10**5, 3*10**5, 10**6]
for thr in (0.0, 0.05, 0.08, 0.10):
    out = []
    for K in Ks:
        z = sum(1 for d in data if d[0] <= K and d[2] == 0 and d[4] >= thr * math.log(d[0]) ** 2)
        zp = sum(1 for d in data if d[0] <= K and d[2] == 0 and d[1] and d[4] >= thr * math.log(d[0]) ** 2)
        out.append(f"K={K:.0e}: {z} ({zp} prime)")
    print(f"M_BM8 >= {thr} L^2 :", '; '.join(out))
# per-decade share of zeros among n in (K/3, K] and local exponent
prev = None
for K in Ks:
    z = sum(1 for d in data if d[0] <= K and d[2] == 0)
    if prev: print(f"local exponent log(Z({K:.0e})/Z({prev[0]:.0e}))/log(K ratio) = {math.log(z/prev[1])/math.log(K/prev[0]):.3f}")
    prev = (K, z)
