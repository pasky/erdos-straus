# Summarise lot_*.csv (z53_noncrtsmooth_lottery output), the second-engine files v2/*.csv, and fixedq.csv.
# Usage: uv run --with pandas python scripts/z53_noncrtsmooth_summary.py > data/z53/noncrtsmooth/summary.txt
import glob
import pandas as pd, numpy as np
D = 'data/z53/noncrtsmooth/'
for f in ['test', 'p24', 'nearsq', 's1e7']:
    d = pd.read_csv(D + f'lot_{f}.csv'); d['L'] = np.log(d.n)
    pos = d[d.R > 0]
    print(f'== {f}: {len(d)} n in [{d.n.min()}, {d.n.max()}]; R=0 at {(d.R==0).sum()}')
    e = (d.R > 0) & (d.Rp == 0)
    print(f'  "x or y prime" empty while R>0: {e.sum()} [n>1e5: {(e&(d.n>1e5)).sum()}, n>5e5: {(e&(d.n>5e5)).sum()}]'
          + (f'; largest {d.n[e].max()}' if e.any() else ''))
    b = (d.R > 0) & (d.Rbp == 0)
    print(f'  "x and y both prime" empty while R>0: {b.sum()} of {len(pos)} ({b.sum()/max(1,len(pos)):.3f})')
    print(f'  mean R/L^2={np.mean(d.R/d.L**2):.3f}; unordered means /L: either-prime {np.mean(d.Rp/2/d.L):.3f}, both-prime {np.mean(d.Rbp/2/d.L):.4f}')
    q = d[d.n > 5e5]
    if len(q):
        for c in ['Rp', 'Rbp']:
            v = q[c] / 2
            print(f'  n>5e5 unordered {c}/2: mean {v.mean():.2f}, var/mean {v.var()/max(1e-9,v.mean()):.3f}')
    for c in ['Rs50', 'Rs33', 'Rs25', 'Re33', 'Re25']:
        print(f'  {c}: share of R={d[c].sum()/max(1,d.R.sum()):.4f}; frac of R>0 primes with {c}=0: {(pos[c]==0).mean():.4f}')
    print(f'  M chosen per p to maximise |P_M(p)|: mean |P_M|={d.bestPM.mean():.2f}, mean |P_M|/L={np.mean(d.bestPM/d.L):.3f}, max |P_M|/L={np.max(d.bestPM/d.L):.3f}; argmax M counts {d.bestM.value_counts().head(6).to_dict()}; share of argmax in 1..6: {d.bestM.isin([1,2,3,4,5,6]).mean():.3f}')
    print('  P_M nonempty fraction (M fixed): ' + ', '.join(f'M={m}: {(d["PM%d"%m]>0).mean():.3f}' for m in [1,2,6,12,60]))
    print(f'  Cmin: median {d.Cmin[d.Cmin>0].median()}, max {d.Cmin.max()}')
    v2 = sorted(glob.glob(D + f'v2/{f}_*.csv'))
    if v2:
        w = pd.concat([pd.read_csv(x) for x in v2]).merge(d[['n','R','Rp','Rbp']], on='n', suffixes=('_v2',''))
        mism = ((w.R != w.R_v2) | (w.Rp != w.Rp_v2) | (w.Rbp != w.Rbp_v2)).sum()
        print(f'  second engine (PARI divisor form): {len(w)} of {len(d)} n compared (R, Rp, Rbp): mismatches {mism}')
d = pd.read_csv(D + 'fixedq.csv'); d['L'] = np.log(d.p)
print('== fixedq: kappa(p,q) = least cofactor at class modulus q; N_q = # ordered witnesses (kappa<=q, x)')
print('  CRT witness has cofactor in [1, q-2] and jmin <= q-2 in all rows:', bool(d.trivial_ok.all()), len(d))
fails = {409,577,5569,9601,23929,83449,102001,329617,712321,8813281}
for name, sub in [('all 29 primes', d), ('19 primes near 1e6', d[~d.p.isin(fails)]), ('10 (★)-failures', d[d.p.isin(fails)])]:
    g = sub.groupby('q').agg(jmin_mean=('jmin','mean'), jmin_max=('jmin','max'), Nq=('N_q','mean'), L=('L','mean'))
    g['jmin_mean/q'] = g.jmin_mean / g.index; g['Nq/L'] = g.Nq / g.L
    print(' --', name); print(g.round(3).to_string())
