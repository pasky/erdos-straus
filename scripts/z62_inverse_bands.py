#!/usr/bin/env python3
"""z62 INVERSE: band statistics of slice codes per tag. Usage: z62_inverse_bands.py slicefile [minN]"""
import sys, collections
fn = sys.argv[1]; minN = int(sys.argv[2]) if len(sys.argv) > 2 else 0
bands = [(1, 4), (5, 16), (17, 64), (65, 256)]
acc = collections.defaultdict(lambda: collections.Counter())
cnt = collections.Counter()
for l in open(fn):
    if l.startswith('#'): continue
    n, tag, us, cs = l.split()[:4]; n = int(n)
    if n < minN: continue
    cnt[tag] += 1
    for fam, s, lim in (('u', us, (n + 1) // 3), ('C', cs, (n + 3) // 4)):
        for (a, b) in bands:
            for k in range(a, min(b, lim) + 1):
                acc[(tag, fam, a)][s[k - 1]] += 1
print('counts', dict(cnt))
for fam in 'uC':
    print(f'== {fam}-slices: per band, fractions h / B / T / Q / S ; structured share (B+T+Q)/(fail)')
    for tag in 'ZGEKcnt':
        row = []
        for (a, b) in bands:
            c = acc[(tag, fam, a)]; tot = sum(c.values())
            if not tot: row.append('   -   '); continue
            fail = tot - c['h']; st = c['B'] + c['T'] + c['Q']
            row.append(f"[{a}-{b}] h{c['h']/tot:.2f} B{c['B']/tot:.2f} T{c['T']/tot:.2f} Q{c['Q']/tot:.2f} S{c['S']/tot:.2f} st|f{st/max(fail,1):.2f}")
        print(tag, ' | '.join(row))
