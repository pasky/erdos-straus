#!/usr/bin/env python3
"""z62 INVERSE: evaluate the pre-registered kill test: conditional shares among failing slices (st|f, B|f)
near-zeros (tag A) vs controls (tag B), bands [17-64], [65-256], u and C families; bootstrap SE over integers.
Usage: z62_inverse_killtest.py slicefile tagA tagB"""
import sys, random
fn, ta, tb = sys.argv[1:4]
bands = [(17, 64), (65, 256)]
data = {ta: [], tb: []}
for l in open(fn):
    if l.startswith('#'): continue
    n, tag, us, cs = l.split()[:4]
    if tag in data: data[tag].append((int(n), us, cs))
def stats(rows, fam, a, b):
    st = bm = fl = 0
    for n, us, cs in rows:
        s = us if fam == 'u' else cs
        lim = (n + 1) // 3 if fam == 'u' else (n + 3) // 4
        seg = s[a - 1:min(b, lim)]
        fl += sum(ch != 'h' for ch in seg); st += sum(ch in 'BTQ' for ch in seg); bm += seg.count('B')
    return st / fl, bm / fl
random.seed(1)
killed = True
for fam in 'uC':
    for a, b in bands:
        sa, ba = stats(data[ta], fam, a, b); sb, bb = stats(data[tb], fam, a, b)
        bs = []
        for _ in range(300):
            ra = [random.choice(data[ta]) for _ in data[ta]]; rb = [random.choice(data[tb]) for _ in data[tb]]
            x = stats(ra, fam, a, b); y = stats(rb, fam, a, b); bs.append((x[0] - y[0], x[1] - y[1]))
        se1 = (sum(d[0] ** 2 for d in bs) / len(bs) - (sum(d[0] for d in bs) / len(bs)) ** 2) ** .5
        se2 = (sum(d[1] ** 2 for d in bs) / len(bs) - (sum(d[1] for d in bs) / len(bs)) ** 2) ** .5
        ok = abs(sa - sb) <= 0.05 and abs(ba - bb) <= 0.05
        killed &= ok
        print(f'{fam} [{a}-{b}] st|f {ta} {sa:.3f} {tb} {sb:.3f} d {sa-sb:+.3f} (se {se1:.3f}) | B|f {ba:.3f} {bb:.3f} d {ba-bb:+.3f} (se {se2:.3f}) | within 0.05: {ok}')
print('KILL criterion met (all within 0.05):', killed)
