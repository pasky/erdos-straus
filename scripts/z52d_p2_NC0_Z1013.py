"""Z1013: rational reconstruction of ES ratios. For each prime p = 1 (mod 4) <= PMAX, take ALL solutions x<=y<=z of
4/p = 1/x+1/y+1/z (scripts/z52d_p2_NC0_Z1013.c), reduce the ratios y/z, x/z, x/y, and record the height
H = max(|num|,|den|).  Rational reconstruction of a ratio from its residue mod M succeeds iff M > 2 H^2 (standard bound),
so M*(solution) = 2H^2+1 is the modulus a CRT/lifting search needs.  Reports per p: min/median/max of H and the scaling
exponent of H vs p (log-log fit).  Also checks the enumeration against U(p) in data/z52b/raw/f4_all_30000.txt.
Run: ./z52d_p2_NC0_Z1013 PMAX > /tmp/z52d_big/G2/z1013_sols.txt; uv run --with numpy python scripts/z52d_p2_NC0_Z1013.py
"""
import numpy as np, json, os, math, collections
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PMAX = 3000
rows = collections.defaultdict(list)
for line in open('/tmp/z52d_big/G2/z1013_sols.txt'):
    n, x, y, z = map(int, line.split()); rows[n].append((x, y, z))
F = np.loadtxt(ROOT + '/data/z52b/raw/f4_all_30000.txt', dtype=np.int64)
U = {int(r[0]): int(r[1]) for r in F}
def H(a, b):
    g = math.gcd(a, b); return max(a // g, b // g)
summ = []; mism = []
for p in sorted(rows):
    if p > PMAX: continue
    sols = rows[p]
    if p in U and U[p] != len(sols): mism.append((p, U[p], len(sols)))
    Hyz = [H(y, z) for (x, y, z) in sols]
    Hxz = [H(x, z) for (x, y, z) in sols]
    Hxy = [H(x, y) for (x, y, z) in sols]
    summ.append(dict(p=p, U=len(sols), minH_yz=min(Hyz), medH_yz=float(np.median(Hyz)), maxH_yz=max(Hyz),
                     maxH_xz=max(Hxz), maxH_xy=max(Hxy), max_modulus_needed_yz=2 * max(Hyz) ** 2 + 1))
ps = np.array([s['p'] for s in summ], float)
def slope(v):
    return float(np.polyfit(np.log(ps), np.log(np.array(v, float)), 1)[0])
out = dict(n_primes=len(summ), U_enumeration_mismatches=mism[:10], n_mismatch=len(mism),
           slope_logH_vs_logp={'minH_yz': slope([s['minH_yz'] for s in summ]), 'medH_yz': slope([s['medH_yz'] for s in summ]),
                               'maxH_yz': slope([s['maxH_yz'] for s in summ]), 'maxH_xz': slope([s['maxH_xz'] for s in summ]),
                               'maxH_xy': slope([s['maxH_xy'] for s in summ])},
           )
# fraction of ALL solutions whose y/z reconstructs from modulus p^2 (M = p^2 > 2H^2 <=> H < p/sqrt2) and from p^4
tot = 0; ok2 = 0; ok4 = 0; okp = 0
for p in rows:
    if p > PMAX: continue
    for (x, y, z) in rows[p]:
        h = H(y, z); tot += 1
        ok2 += (2 * h * h < p * p); ok4 += (2 * h * h < p ** 4); okp += (2 * h * h < p)
out['fraction_solutions_reconstructible_by_modulus_p4'] = round(ok4 / tot, 4)
out['fraction_reconstructible_by_modulus_p2'] = round(ok2 / tot, 4)
out['fraction_reconstructible_by_modulus_p'] = round(okp / tot, 4)
out['n_solutions_total'] = tot
out['examples'] = summ[-5:]
json.dump(out, open(ROOT + '/data/z52b/pass2/NC0/sub/Z1013_reconstruction.json', 'w'), indent=1)
print(json.dumps({k: v for k, v in out.items() if k != 'examples'}, indent=1))
print(summ[-3:])
