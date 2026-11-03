#!/usr/bin/env python3
"""z54 HCWIN: per-line success law from the .lines files of z54_hcwin_lines.c.
Rows 'G type j bin lo2 count succ sumP1 sumPh' (m = g/|G_x^2|, genus-normalised; sumP1, sumPh = sums over the lines in
the bin of 1-exp(-m) and 1-exp(-m/2)) and 'T type j bin lo2 count succ' (m = tau/phi(x)).
For G rows the printed prediction is the bin AVERAGE of 1-exp(-m) (E) resp. 1-exp(-m/2) (L); for T rows the bin-centre
value 1-exp(-2^(lo2+1/4)).
Prints, per dyadic block j (x in [2^j, 2^{j+1})) and kind, success rate vs m against 1 - exp(-m), pooled over E/L.
Also the genus-confined share (rows 'C').
Usage: python3 z54_hcwin_perline.py file.lines [min_j]
"""
import sys, math
from collections import defaultdict

fn = sys.argv[1]
minj = int(sys.argv[2]) if len(sys.argv) > 2 else 4
data = defaultdict(lambda: [0, 0, 0.0, 0.0])
conf = []
for line in open(fn):
    if line.startswith('#'):
        continue
    a = line.split()
    if a[0] in ('G', 'T'):
        kind, ty, j, b, lo2, c, s = a[0], a[1], int(a[2]), int(a[3]), float(a[4]), int(a[5]), int(a[6])
        key = (kind, ty, j, lo2 if b > 0 else None)
        data[key][0] += c; data[key][1] += s
        if kind == 'G' and len(a) >= 9:
            data[key][2] += float(a[7]); data[key][3] += float(a[8])
    elif a[0] == 'C':
        conf.append(line.strip())
for kind in ('G', 'T'):
    print(f"--- kind {kind} ({'m = g/|G^2|; pred = bin mean of 1-e^-m (E), 1-e^-m/2 (L)' if kind=='G' else 'm = tau/phi; pred = 1-e^-m at bin centre'}): lo2:rate|pred(count)")
    for ty in ('E', 'L'):
        for j in range(minj, 13):
            keys = sorted([k for k in data if k[0] == kind and k[1] == ty and k[2] == j], key=lambda k: -99 if k[3] is None else k[3])
            if not keys:
                continue
            parts = []
            for k in keys:
                c, s, s1, sh = data[k]
                if c < 50:
                    continue
                if k[3] is None:
                    parts.append(f"m=0:{s/c:.3f}({c})")
                else:
                    if kind == 'G' and s1 > 0:
                        pred = (s1 if ty == 'E' else sh) / c
                    else:
                        pred = 1 - math.exp(-2 ** (k[3] + 0.25))
                    parts.append(f"{k[3]:+.1f}:{s/c:.3f}|{pred:.3f}({c})")
            print(f" {ty} j={j:2d}: " + "  ".join(parts))
print("--- genus-confined lines")
for c in conf:
    print(" ", c)
