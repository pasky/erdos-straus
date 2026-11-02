# z54 EXACTSUM: summarise conductor profiles. Usage: python scripts/z54_exactsum_stats.py prof_*.tsv
import sys, csv, math
import numpy as np
for path in sys.argv[1:]:
    rows = list(csv.DictReader(open(path), delimiter='\t'))
    tags = []
    for r in rows:
        if r['tag'] not in tags: tags.append(r['tag'])
    print('==', path)
    A = ['A0', 'A1', 'A2', 'A3', 'Atop']; B = ['B1', 'B2', 'B3', 'B4', 'B5']
    print('tag N meanR meanG var(R-G) | varfrac A[0,.25) [.25,.5) [.5,.75) [.75,1) top | varfrac B m=1 2-3 4-15 16-63 64+ | sumvarB/var | mean sumAbsDf/(R+G) mean sumAbsTu/(R+G) maxerr')
    for t in tags:
        S = [r for r in rows if r['tag'] == t]
        g = lambda k: np.array([float(r[k]) for r in S])
        RG = g('RG'); v = RG.var(ddof=1) if len(S) > 1 else float('nan')
        R, G = g('R'), g('G')
        fa = [g(k).var(ddof=1) / v if v > 0 else float('nan') for k in A]
        fb = [g(k).var(ddof=1) / v if v > 0 else float('nan') for k in B]
        ma = [np.mean(np.abs(g(k))) for k in A]; mb = [np.mean(np.abs(g(k))) for k in B]
        den = np.maximum(R + G, 1e-9)
        line = f'{t} {len(S)} {R.mean():.3f} {G.mean():.3f} {v:.3f} | ' + ' '.join(f'{x:.3f}' for x in fa) + ' | ' + ' '.join(f'{x:.3f}' for x in fb)
        line += f' | {sum(g(k).var(ddof=1) for k in B)/v if v>0 else float("nan"):.3f} | {np.mean(g("sumAbsDf")/den):.3f} {np.mean(g("sumAbsTu")/den):.3f} {g("maxerr").max():.2g}'
        print(line)
        if v == 0 or t in ('SQUARE',):
            print('   (mean |bucket|) A:', ' '.join(f'{x:.3f}' for x in ma), ' B:', ' '.join(f'{x:.3f}' for x in mb), ' mean sumAbsDf', f'{g("sumAbsDf").mean():.3f}', ' mean shell3', f'{g("shell3").mean():.1f}')
