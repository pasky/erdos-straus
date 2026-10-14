"""fz_enum_check.py (O220): compare fz_enum pattern counts with bsE_famcount print output (q prime).
usage: fz_enum_check.py famcount_print_file enum_output_file"""
import sys
from collections import Counter
fam = Counter()
for line in open(sys.argv[1]):
    if line.startswith('s=') and ' a=' in line:
        d = dict(kv.split('=') for kv in line.split()[:6])
        s, a, b, mu, y, t = (int(d[k]) for k in ('s', 'a', 'b', 'mu', 'y', 't'))
        if a <= b: fam[s, a, mu, y, t] += 1
en = {}; skipped = 0
for line in open(sys.argv[2]):
    f = line.split()
    if f[5] == 'SKIP': skipped += 1; continue
    en[tuple(map(int, f[:5]))] = int(f[5])
smax = max(k[0] for k in en)
bad = 0
for k in set(fam) | set(en):
    if k[0] > smax or k not in en: continue
    if fam.get(k, 0) != en[k]: bad += 1; print('MISMATCH', k, fam.get(k, 0), en[k])
print(f'patterns compared={len(en)} (skipped {skipped}) tuples={sum(en.values())} mismatches={bad}')
