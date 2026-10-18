"""O262: lower-deviation test beyond the zero range.  For the ladder lotteries, pool primes by cell mean mu
(cell = p mod lcm(840,4m), dyadic bin) and report -log P(f <= theta*mu) for theta = 0.2, 0.3, 0.4, 0.5."""
import math, numpy as np
P = np.load('/tmp/z32/primes.npy').astype(np.int64)
TH = (0.2, 0.3, 0.4, 0.5); acc = {}
for m in (4, 5, 6, 8, 10, 12, 16, 20, 24):
    c = np.load(f'/tmp/z32/cnt_m{m}.npy').astype(np.int64); ok = (P > 3) & (m % P != 0); p, f = P[ok], c[ok]
    C = math.lcm(840, 4*m)
    for k in range(12, 27):
        sel = (p >= 2**k) & (p < 2**(k+1)); cc = p[sel] % C; ff = f[sel]
        o = np.argsort(cc, kind='stable'); cc, ff = cc[o], ff[o]
        b = np.flatnonzero(np.diff(cc)) + 1
        for s, e in zip(np.r_[0, b], np.r_[b, len(cc)]):
            if e - s < 30: continue
            g = ff[s:e]; mu = g.mean(); key = min(int(math.log(mu)/math.log(1.5)), 30)
            a = acc.setdefault(key, np.zeros(len(TH) + 2)); a[0] += e - s; a[1] += mu*(e - s)
            for i, t in enumerate(TH): a[2 + i] += (g <= t*mu).sum()
print('mu~   primes   ' + '  '.join(f'-lnP(f<={t}mu)' for t in TH) + '   [/mu^0.91 for theta=0.3]')
for key in sorted(acc):
    a = acc[key]; mu = a[1]/a[0]
    v = [(-math.log(a[2+i]/a[0]) if a[2+i] else float('inf')) for i in range(len(TH))]
    print(f'{mu:7.1f} {int(a[0]):9d}  ' + '  '.join(f'{x:8.2f}' for x in v) + f'   {v[1]/mu**0.91:.3f}')
