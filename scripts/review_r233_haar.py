"""R233: Prop 5.1 from scratch. For k = 2..7, count (t,u,v) mod 2^k with tuv - u - v = p (mod 2^k) for every odd
class p, and the share of 'five-slice' points (4 | t, u, v, A = tu-1 or B = tv-1)."""
import numpy as np

for k in range(2, 8):
    q = 1 << k
    r = np.arange(q, dtype=np.int64)
    t, u, v = np.meshgrid(r, r, r, indexing='ij')
    f = (t * u * v - u - v) % q
    five = (t % 4 == 0) | (u % 4 == 0) | (v % 4 == 0) | ((t * u - 1) % 4 == 0) | ((t * v - 1) % 4 == 0)
    tot = np.bincount(f.ravel(), minlength=q)
    fv = np.bincount(f.ravel(), weights=five.ravel(), minlength=q)
    out = {}
    for p in range(1, q, 2):
        out.setdefault(p % 4, set()).add((int(tot[p]), fv[p] / tot[p]))
    print(k, "p=1(4):", out[1], " p=3(4):", out[3], " expected 5*4^(k-1) =", 5 * 4 ** (k - 1))
