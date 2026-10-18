"""O262: one-constant crossover predictor across the ladder.  For each m: q_m = 1e-3 quantile of f/L^3 in the top
bin [2^26, 2^27) and median ratio; last exception p_last (from all primes 3 < p <= 1e8, p ∤ m);
c0_m := q_m * (ln p_last)^3 (the 'crossover count'); a single c0 then predicts p_last = exp((c0/q_m)^(1/3))."""
import math, numpy as np
P = np.load('/tmp/z32/primes.npy').astype(np.int64)
rows = []
for m in range(4, 25):
    c = np.load(f'/tmp/z32/cnt_m{m}.npy').astype(np.int64); ok = (P > 3) & (m % P != 0); p, f = P[ok], c[ok]
    s = p >= 2**26; r = f[s]/np.log(p[s].astype(float))**3; q = np.quantile(r, 1e-3); med = np.median(r)
    Z = p[f == 0]; pl = int(Z.max()) if len(Z) else 0
    c0 = q*math.log(pl)**3 if pl else float('nan'); rows.append((m, q, med, pl, len(Z), c0))
    print(f'm={m:2d} q1e-3={q:.5f} median={med:.4f} #exc={len(Z):5d} last={pl:9d} c0={c0:.2f}')
c0s = [r[5] for r in rows if r[3] and r[3] < 5e7]
g = math.exp(np.mean(np.log(c0s))); print(f'geometric-mean c0 over m with last exception < 5e7: {g:.2f}  range {min(c0s):.2f}..{max(c0s):.2f}')
for m, q, med, pl, n, c0 in rows:
    print(f'  m={m}: predicted last exception ~ exp(({g:.2f}/q)^(1/3)) = {math.exp((g/q)**(1/3)):.3g}   (observed {pl})')
