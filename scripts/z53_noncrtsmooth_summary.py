# Summarise lot_*.csv (z53_noncrtsmooth_lottery output) and fixedq.csv. Usage: uv run --with pandas python ... > summary.txt
import pandas as pd, numpy as np
D = 'data/z53/noncrtsmooth/'
for f in ['test', 'p24', 'nearsq', 's1e7']:
    d = pd.read_csv(D + f'lot_{f}.csv'); d['L'] = np.log(d.n)
    pos = d[d.R > 0]
    print(f'== {f}: {len(d)} n in [{d.n.min()}, {d.n.max()}]; R=0 at {(d.R==0).sum()}')
    print(f'  R>0 but no prime x/y (Rp=0): {((d.R>0)&(d.Rp==0)).sum()}  [n>1e5: {((d.R>0)&(d.Rp==0)&(d.n>1e5)).sum()}, n>5e5: {((d.R>0)&(d.Rp==0)&(d.n>5e5)).sum()}]')
    print(f'  mean R/L^2={np.mean(d.R/d.L**2):.3f}  mean Rp/L={np.mean(d.Rp/d.L):.3f}  sum Rp/sum R={d.Rp.sum()/max(1,d.R.sum()):.3f}')
    for c in ['Rs50', 'Rs33', 'Rs25']:
        print(f'  {c}: share of R={d[c].sum()/max(1,d.R.sum()):.4f}; frac of R>0 primes with {c}=0: {(pos[c]==0).mean():.4f}')
    print(f'  best fixed M: mean |P_M|={d.bestPM.mean():.2f}, mean |P_M|/L={np.mean(d.bestPM/d.L):.3f}, max |P_M|/L={np.max(d.bestPM/d.L):.3f}; argmax M counts {d.bestM.value_counts().head(6).to_dict()}')
    print('  P_M nonempty fraction: ' + ', '.join(f'M={m}: {(d["PM%d"%m]>0).mean():.3f}' for m in [1,2,6,12,60]))
    print(f'  Cmin: median {d.Cmin[d.Cmin>0].median()}, max {d.Cmin.max()}')
if True:
    d = pd.read_csv(D + 'fixedq.csv'); d['L'] = np.log(d.p)
    print('== fixedq: j(p,q) = least height at class modulus q; N_q = #solutions with j<=q')
    print('  trivial CRT bound j<=q-2 verified in all rows:', bool(d.trivial_ok.all()))
    g = d.groupby('q').agg(jmin_mean=('jmin','mean'), jmin_max=('jmin','max'), Nq=('N_q','mean'), L=('L','mean'))
    g['jmin_mean/q'] = g.jmin_mean / g.index; g['Nq/L'] = g.Nq / g.L
    print(g.round(3).to_string())
