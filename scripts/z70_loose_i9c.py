# z70 LOOSE I9, review fixes: (a) stratum sizes and same-population means; (b) the amended (nearest) decoy and the
# two-sided decoy compared on the SAME subset (Q-primes where both a lower and an upper admissible decoy exist).
import sys, json, math
sys.path.insert(0, 'scripts')
from z70_loose_i9 import badq, yword
from z70_loose_i9b import side
rows = json.load(open('data/z70/loose/i9_rows.json'))
for name, R in rows.items():
    ms = [len(r['ctl']) for r in R]; ret = [r for r in R if r['ctl']]
    hq = sum(r['Q'] for r in ret) / len(ret)
    cq = sum(sum(c['Q'] for c in r['ctl']) / len(r['ctl']) for r in ret) / len(ret)
    print(f"{name}: strata={len(R)} retained={len(ret)} control counts (sorted)={sorted(ms)}; retained hard Q={hq:.3f}, "
          f"stratum-weighted control Q={cq:.3f}, Delta={hq-cq:+.4f}")
pool = [c for r in rows['noprime231'] for c in r['ctl'] if c['Q']]
a = []; excl = []
for c in pool:
    X, Y, bq = badq(c['p']); q = bq[0]
    lo = side(c['p'], q, X, -1); hi = side(c['p'], q, X, +1)
    if lo is None or hi is None: excl.append(c); continue
    a.append((c['Yq'], c['Yd2'], (yword(c['p'], lo) + yword(c['p'], hi)) / 2))
n = len(a)
for lab, k in (('nearest (amended) decoy', 1), ('two-sided decoy', 2)):
    d = [x[0] - x[k] for x in a]; m = sum(d) / n; sd = math.sqrt(sum((t - m) ** 2 for t in d) / (n - 1) / n)
    print(f"noprime controls, same subset n={n}: Y(q)={sum(x[0] for x in a)/n:.4f} vs {lab} {sum(x[k] for x in a)/n:.4f}: diff={m:+.4f} z={m/sd:+.2f}")
print(f"all Q-controls: {len(pool)}, Y(q) = {sum(c['Yq'] for c in pool) / len(pool):.4f}")
print(f"excluded from the two-sided subset (second-review fix: this population was mis-specified in the first version): "
      f"{len(excl)} Q-primes; Y(q) = {sum(c['Yq'] for c in excl) / len(excl):.4f}; nearest decoy Y = {sum(c['Yd2'] for c in excl) / len(excl):.4f}")
