"""Z1118: nerve of parametrisation charts (G4, NC0).
Charts = repo residue-certificate families (Type I/II, see z52d_p2_NC0_lib.py), restricted to
primes p = 1 mod 4 up to 10^6. Five explicit families; the nerve records which families share a
certificate prime. Also: duplicate charts (identical covered sets on p=1 mod 4)."""
import sys, itertools, json
sys.path.insert(0, "scripts")
import numpy as np
from z52d_p2_NC0_lib import primes_upto, families, covered_mask

ps = primes_upto(10**6)
ps = ps[(ps % 4 == 1) & (ps > 5)]
fams = {f["name"]: f for f in families(60)}
chart_names = ["I(1,2)", "I(2,2)", "I(1,5)", "II(1,5)", "I(2,3)"]
C = {n: covered_mask(fams[n], ps) for n in chart_names}
k = len(chart_names)
print(f"primes = 1 mod 4, p<=1e6: {len(ps)}")
for n in chart_names:
    print(f"  chart {n:8s} s={fams[n]['s']:3d} m={fams[n]['m']:4d} |R|={len(fams[n]['R'])} density={C[n].mean():.4f}")

# duplicate charts
dups = []
names_all = list(fams)
sets = {}
for n in names_all:
    c = covered_mask(fams[n], ps)
    key = c.tobytes()
    sets.setdefault(key, []).append(n)
dup_groups = [v for v in sets.values() if len(v) > 1]
print("duplicate-chart groups among all s<=60 families:", len(dup_groups))
for g in dup_groups[:8]:
    print("  ", g)
print("I(1,2) == II(1,2) on p=1 mod 4:", np.array_equal(covered_mask(fams["I(1,2)"], ps), covered_mask(fams["II(1,2)"], ps)))

# nerve of the 5 charts
nerve = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
simplex_counts = {}
for r in range(1, k + 1):
    for sub in itertools.combinations(chart_names, r):
        cnt = int(np.logical_and.reduce([C[n] for n in sub]).sum())
        simplex_counts["+".join(sub)] = cnt
        if cnt > 0:
            nerve[r] += 1
print("nonempty simplices by size:", nerve, "max possible:", {r: len(list(itertools.combinations(range(k), r))) for r in range(1, k + 1)})
N = len(ps)
print("pairwise: observed vs independent (product of densities), ratio")
pair_out = {}
for a, b in itertools.combinations(chart_names, 2):
    obs = simplex_counts[f"{a}+{b}"] / N
    ind = C[a].mean() * C[b].mean()
    pair_out[f"{a}&{b}"] = (obs, ind)
    print(f"  {a:8s} & {b:8s}: obs {obs:.4f}  indep {ind:.4f}  ratio {obs/ind if ind else float('nan'):.3f}")
core = simplex_counts["+".join(chart_names)]
print("primes covered by all 5 charts (core):", core, "of", N)
print("primes covered by no chart among the 5:", int((~np.logical_or.reduce([C[n] for n in chart_names])).sum()))
json.dump({"simplex_counts": simplex_counts, "N": N, "dup_groups": dup_groups[:20]},
          open("data/z52b/pass2/NC0/sub/Z1118_nerve.json", "w"), indent=0)
