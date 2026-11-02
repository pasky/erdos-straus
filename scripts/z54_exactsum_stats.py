# z54 EXACTSUM: summarise conductor profiles. Usage: python scripts/z54_exactsum_stats.py prof_*.tsv
# For each sample group: var(R-G) across n, and variance fractions var(bucket)/var(R-G) for
#   (A) relative conductor rho = log f/log u: merged rho<1/2 (A0+A1), [.5,.75) (A2), [.75,1) (A3), top f=u (Atop)
#   (B) block multiplicity m_f: m=1 (B1), merged m<=3 (B1+B2), merged m>=16 (B4+B5)
# (merged buckets: variance of the SUM, i.e. covariances included), the sum of the five separate B-bucket variances
# relative to var(R-G), the Poisson-type ratio var(R-G)/mean(R+G), and the triangle ratio
# mean(sum_u |t_u|)/mean(R+G) (ratio of aggregate means; rows with R+G=0 are not excluded since aggregate).
# Square groups: R=G=0 identically, only mean |bucket| and mean sum_f |D_f| are printed.
import sys, csv
import numpy as np
for path in sys.argv[1:]:
    rows = list(csv.DictReader(open(path), delimiter='\t'))
    tags = []
    for r in rows:
        if r['tag'] not in tags: tags.append(r['tag'])
    print('==', path)
    print('tag N meanR meanG var(R-G) var/mean(R+G) | rho<1/2 [.5,.75) [.75,1) top | m=1 m<=3 m>=16 | sumvarB/var | triangle_u')
    for t in tags:
        S = [r for r in rows if r['tag'] == t]
        g = lambda k: np.array([float(r[k]) for r in S])
        RG = g('RG'); R, G = g('R'), g('G')
        v = RG.var(ddof=1) if len(S) > 1 else float('nan')
        if not v > 0:
            ma = {k: np.mean(np.abs(g(k))) for k in ['A0', 'A1', 'A2', 'A3', 'Atop', 'B1', 'B2', 'B3', 'B4', 'B5']}
            print(f'{t} {len(S)} R=G=0 identically; mean|bucket| ' + ' '.join(f'{k}={x:.3f}' for k, x in ma.items()) +
                  f'; mean sum_f|D_f| = {g("sumAbsDf").mean():.3f}; mean shell3 = {g("shell3").mean():.1f}')
            continue
        fr = lambda arr: arr.var(ddof=1) / v
        A = [fr(g('A0') + g('A1')), fr(g('A2')), fr(g('A3')), fr(g('Atop'))]
        B = [fr(g('B1')), fr(g('B1') + g('B2')), fr(g('B4') + g('B5'))]
        sB = sum(fr(g(k)) for k in ['B1', 'B2', 'B3', 'B4', 'B5'])
        tri = g('sumAbsTu').mean() / (R + G).mean()
        print(f'{t} {len(S)} {R.mean():.3f} {G.mean():.3f} {v:.3f} {v/(R+G).mean():.3f} | ' + ' '.join(f'{x:.3f}' for x in A) +
              ' | ' + ' '.join(f'{x:.3f}' for x in B) + f' | {sB:.3f} | {tri:.3f}   (maxerr {g("maxerr").max():.2g})')
