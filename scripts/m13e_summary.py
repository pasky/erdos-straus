"""m13e_summary.py — totals over run dirs: levels, ES solutions, distinct boxes, hits per tested point.
usage: m13e_summary.py rundir [rundir...]"""
import glob, pickle, sys
lev, nsol, boxes, hits = [], 0, set(), {}
for d in sys.argv[1:]:
    for fn in glob.glob(d + '/inv_*.pkl'):
        D = pickle.load(open(fn, 'rb')); lev.append(D['N']); nsol += D['nsol']; boxes |= set(D['boxes'])
        for p, h in D['hits'].items():
            hits.setdefault(p, set()).update((t[0], t[1], t[2], t[3]) for t in h)
print(f'levels {len(lev)} (max N {max(lev)}), ES solutions {nsol}, distinct boxes {len(boxes)}')
for p, h in hits.items():
    print(f' point ({p[0]},{p[1]}): distinct hit data {len(h)}', sorted(h)[:4])
