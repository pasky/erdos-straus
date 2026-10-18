"""O262: universality test of the zero law across the numerator ladder m = 4..24 (Type II lotteries).
Unit = (m, cell p mod lcm(840,4m), dyadic-pair bin): mu = cell mean count, n primes, z zeros.
Prints the exceptions per m and the pooled zero-rate as a function of mu (bins of mu), with the min count ratio."""
import math, numpy as np
P = np.load('/tmp/z32/primes.npy').astype(np.int64)
rows = []; summ = []
for m in range(4, 25):
    c = np.load(f'/tmp/z32/cnt_m{m}.npy').astype(np.int64)
    ok = (P > 3) & (m % P != 0); p, f = P[ok], c[ok]
    Z = p[f == 0]; summ.append((m, len(Z), int(Z.max()) if len(Z) else 0, int((Z > 10**6).sum())))
    C = math.lcm(840, 4*m); cell = p % C
    for k in range(10, 27):
        sel = (p >= 2**k) & (p < 2**(k+1))
        pp, ff, cc = p[sel], f[sel], cell[sel]
        order = np.argsort(cc, kind='stable'); cc, ff = cc[order], ff[order]
        b = np.flatnonzero(np.diff(cc)) + 1; starts = np.r_[0, b]; ends = np.r_[b, len(cc)]
        for s, e in zip(starts, ends):
            if e - s < 10: continue
            g = ff[s:e]; rows.append((m, k, g.mean(), e - s, int((g == 0).sum()), int((g <= 2).sum())))
for t in summ: print('m=%d exceptions=%d largest=%d beyond1e6=%d' % t)
R = np.array(rows, dtype=float)
edges = [0, 2, 4, 6, 8, 10, 12, 15, 20, 25, 30, 40, 50, 70, 100, 150, 1e9]
print('mu-bin  units  primes  zeros  rate  (<=2)-rate')
for lo, hi in zip(edges[:-1], edges[1:]):
    s = (R[:, 2] >= lo) & (R[:, 2] < hi)
    if not s.any(): continue
    n = R[s, 3].sum(); z = R[s, 4].sum(); z2 = R[s, 5].sum()
    print(f'[{lo:g},{hi:g}) {int(s.sum())} {int(n)} {int(z)} {z/n:.2e} {z2/n:.2e}')
np.save('/tmp/z32/units.npy', R)
