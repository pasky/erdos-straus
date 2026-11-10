# pool the EXACT aggregate excess/variance lines of z70_class_nullfix.py outputs (review fix of z70_class_pool.py rounding)
import sys, re, math
acc = {}
for fn in sys.argv[1:]:
    line = [l for l in open(fn) if 'EXACT sums' in l][-1]
    for s, ex, var in re.findall(r"(\w+) excess ([+-][\d.]+) var ([\d.]+)", line):
        a = acc.setdefault(s, [0.0, 0.0]); a[0] += float(ex); a[1] += float(var)
print('; '.join(f"Z_{s} = {a[0]/math.sqrt(a[1]):+.2f}" if a[1] > 0 else f"Z_{s} = nan" for s, a in acc.items()))
