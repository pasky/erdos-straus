# Re-aggregate z70_class_nullfix.py per-n lines, excluding given n (review round 2: the §1.9 smoke-test primes 24001, 25169
# (d = 1) and 24481 (d = 2) must be excluded from the registered F1 outcome).  Usage: python3 reagg.py FILE n1 n2 ...
import sys, re, math
fn = sys.argv[1]; excl = set(int(x) for x in sys.argv[2:])
SS = ('K', 'C0', 'M', 'E', 'L1', 'L3', 'A2', 'Mx', 'Ex')
agg = {s: [0.0, 0.0] for s in SS}; m = 0; pw = {s: 0 for s in SS}
for l in open(fn):
    if not l.startswith('n=') or '(skipped)' in l: continue
    n = int(re.match(r'n=(\d+)', l).group(1))
    if n in excl: continue
    m += 1
    for s, o, mu, sd in re.findall(r' (\w+) (\d+) \(([\d.]+)±([\d.]+)\)', l):
        if s in agg: agg[s][0] += int(o) - float(mu); agg[s][1] += float(sd)**2; pw[s] += float(sd) > 0
print(f"{fn} excluding {sorted(excl)}: n {m}; " + '; '.join(f"Z_{s} = {agg[s][0]/math.sqrt(agg[s][1]):+.3f} (excess {agg[s][0]:+.3f}, var {agg[s][1]:.3f}, n_var>0 {pw[s]})" if agg[s][1] > 0 else f"Z_{s} = nan" for s in ('Mx', 'Ex', 'L1', 'L3', 'C0', 'A2')))
