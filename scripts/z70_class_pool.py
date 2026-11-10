# pool the aggregate Z of several z70_class_{null,psf} output files: Z = sum(excess)/sqrt(sum var), var recovered as (excess/Z)^2
import sys, re, math
stats = {}
for fn in sys.argv[1:]:
    last = [l for l in open(fn) if l.startswith('#') and 'Z_' in l][-1]
    for s, z, o, nu in re.findall(r"Z_(\w+) = ([+-]?[\d.na]+) \(obs ([\d.]+), null ([\d.]+)\)", last):
        z = float(z); ex = float(o) - float(nu)
        if math.isnan(z) or z == 0: continue
        a = stats.setdefault(s, [0.0, 0.0]); a[0] += ex; a[1] += (ex / z) ** 2
print(' '.join(sys.argv[1:]))
print('; '.join(f"Z_{s} = {a[0]/math.sqrt(a[1]):+.2f}" for s, a in stats.items() if a[1] > 0))
