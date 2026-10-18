"""O262: extreme-value test.  Per dyadic bin and m: #primes, min f/L^3, the 1e-4 and 1e-3 quantiles of f/L^3,
and the argmin prime.  A floor (min ratio not decreasing while #primes grows x2 per bin) is the signature of
a bounded-below local factor; a drifting-down min is the signature of an unbounded lower tail."""
import math, numpy as np
P = np.load('/tmp/z32/primes.npy').astype(np.int64)
for m in (4, 5, 6, 8, 12, 16, 24):
    c = np.load(f'/tmp/z32/cnt_m{m}.npy').astype(np.int64); ok = (P > 3) & (m % P != 0); p, f = P[ok], c[ok]
    r = f/np.log(p.astype(float))**3; out = []
    for k in range(14, 27):
        s = (p >= 2**k) & (p < 2**(k+1)); rr = r[s]; i = np.argmin(rr)
        out.append(f'{k}:{rr.min():.4f}/{np.quantile(rr,1e-4):.4f}/{np.quantile(rr,1e-3):.4f}/{np.median(rr):.3f}(p={p[s][i]})')
    print(f'm={m}: ' + '  '.join(out))
