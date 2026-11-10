# z70 GEN — list every (p, d) with G_d(p) = empty and its r4, r8 (registered item-2 list).  usage: python3 scripts/z70_gen_empty.py FILE...
import sys, json
rows = []
for f in sys.argv[1:]:
    for l in open(f):
        r = json.loads(l)
        if 'skipped' in r or r['G'] > 0: continue
        rows.append((r['d'], r['n'], r['n'] % 840, r['r4'], r['r8'], r['cyc']))
print('# d p p%840 r4 r8 cyc   (all (p, d) with G_d(p) empty in the input files)')
for x in sorted(rows): print(*x)
