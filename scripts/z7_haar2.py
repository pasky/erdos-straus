"""O231 §5: 2-adic Haar mass of the five-slice (certificate) set on X_p: tuv - u - v = p, for p mod 2^k.
Counts all (t,u,v) mod 2^k with tuv-u-v = p mod 2^k and the fraction with 4 | t,u,v,tu-1 or tv-1 (well defined mod 2^k, k>=2).
usage: z7_haar2.py k"""
import sys
k = int(sys.argv[1]); Q = 1 << k
for pr in range(1, 16, 2):
    if pr % 4 != 1: continue
    tot = cert = 0
    for t in range(Q):
        for u in range(Q):
            # solve v (t u - 1) = p + u mod Q
            a, b = (t * u - 1) % Q, (pr + u) % Q
            for v in range(Q):
                if (a * v - b) % Q: continue
                tot += 1
                if t % 4 == 0 or u % 4 == 0 or v % 4 == 0 or (t * u - 1) % 4 == 0 or (t * v - 1) % 4 == 0: cert += 1
    print(f"p = {pr} mod 16: solutions mod 2^{k}: {tot}, five-slice fraction {cert/tot:.4f}")
