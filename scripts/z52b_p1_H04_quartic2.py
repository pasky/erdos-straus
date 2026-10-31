#!/usr/bin/env python3
"""Z1488 (full families, no sampling): zeros of R on n = k m^2 (n ≡ 1 mod 4, non-square, n>=1000) vs expected zeros from
controls: for each family member, control rate = zero rate of odd non-squares in the same class mod 840 within [n/2, 2n]."""
import numpy as np, math
R = np.fromfile('/tmp/h04_R.bin', dtype=np.uint16); N = len(R) - 1
sq = np.zeros(N + 1, bool); s = np.arange(1, math.isqrt(N) + 1); sq[s * s] = True
z = ((R == 0) & ~sq).astype(np.int64); ok = (~sq).astype(np.int64)
# cumulative counts per residue class mod 840
cz = {}; co = {}
for r in range(840):
    idx = np.arange(r, N + 1, 840); cz[r] = np.concatenate([[0], np.cumsum(z[idx])]); co[r] = np.concatenate([[0], np.cumsum(ok[idx])])
def rate(n):
    r = n % 840; a = (n // 2 - r) // 840 + 1; b = (min(2 * n, N) - r) // 840 + 1; a = max(a, 0)
    return (cz[r][b] - cz[r][a]) / max(co[r][b] - co[r][a], 1)
rows = []
for power in (2, 4):
    for k in range(2, 201):
        if math.isqrt(k) ** 2 == k: continue
        ns = [k * m ** power for m in range(1, int((N / k) ** (1 / power)) + 2) if 1000 <= k * m ** power <= N]
        ns = [n for n in ns if n % 4 == 1]
        if not ns: continue
        obs = int(sum(R[n] == 0 for n in ns)); exp = sum(rate(n) for n in ns)
        rows.append((k, power, len(ns), obs, exp, [n for n in ns if R[n] == 0][:6]))
tot_o = sum(r[3] for r in rows); tot_e = sum(r[4] for r in rows)
print(f"families: {len(rows)}  total zeros observed {tot_o}  expected(control) {tot_e:.1f}")
for r in sorted(rows, key=lambda r: -(r[3] - r[4]) / math.sqrt(r[4] + 0.5))[:15]:
    print(f"k={r[0]:3d} m^{r[1]} size={r[2]:5d} obs={r[3]:3d} exp={r[4]:6.2f} zeros={r[5]}")
