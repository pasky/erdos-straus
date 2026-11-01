"""Does class-group membership (SM: -p square mod a) still matter after conditioning on the genus count?
Input: *.genus files of z53_forestclass_forest (-s FILE writes FILE.genus): rows
  chi amod8 inSM log2bucket genusbucket count nonisolated inBichromComp
genusbucket 0: no divisor of p+a in the coset (-p)G_a^2 (then a is isolated, Lemma G); else
1 + clamp(floor(2 log2 mu) + 20) with mu = g * [G:G^2] / phi(a) the genus-layer expected number of neighbours.
Reports (1) the sanity check "genusbucket 0 ⇒ isolated", (2) the share of genus-obstructed vertices in/out of SM,
(3) MH ratios for SM membership with strata (chi, a mod 8, size) [genus-blind] and (chi, a mod 8, size, genusbucket)
[genus-conditioned].
Usage: uv run python scripts/z53_forestclass_genusenrich.py FILE.genus ...
"""
import sys
from collections import defaultdict

rows = defaultdict(lambda: [0, 0, 0])
for fn in sys.argv[1:]:
    for line in open(fn):
        if line.startswith("#"):
            continue
        c, m, sm, b, g, n, ni, bi = map(int, line.split())
        r = rows[(c, m, sm, b, g)]
        r[0] += n; r[1] += ni; r[2] += bi

z = [0, 0, 0]
obs = {0: [0, 0], 1: [0, 0]}
for (c, m, sm, b, g), r in rows.items():
    if b < 2:
        continue
    obs[sm][1] += r[0]
    if g == 0:
        obs[sm][0] += r[0]
        for i in range(3):
            z[i] += r[i]
print(f"genus-obstructed vertices (a>=4): {z[0]}, of which non-isolated {z[1]} (Lemma G predicts 0)")
for sm in (1, 0):
    print(f"  inSM={sm}: share genus-obstructed = {obs[sm][0]}/{obs[sm][1]} = {obs[sm][0]/max(1,obs[sm][1]):.4f}")

BR = [(4, 6), (7, 9), (10, 12), (13, 15), (16, 18), (19, 21), (22, 24)]
for lo, hi in BR:
    for which, idx in (("nonisolated", 1), ("bichromComp", 2)):
        out = []
        for cond in ("blind", "genus", "genus>0"):
            strata = defaultdict(lambda: [[0, 0], [0, 0]])
            for (c, m, sm, b, g), r in rows.items():
                if not (lo <= b <= hi):
                    continue
                if cond == "genus>0" and g == 0:
                    continue
                key = (c, m, b) if cond == "blind" else (c, m, b, g)
                s = strata[key]
                s[sm][0] += r[0]
                s[sm][1] += r[idx]
            num = den = 0.0
            for (n0, x0), (n1, x1) in strata.values():
                N = n0 + n1
                if n0 and n1:
                    num += x1 * n0 / N
                    den += x0 * n1 / N
            out.append(f"{cond}: {num/den if den else float('nan'):.3f}")
        print(f"a in [2^{lo},2^{hi+1}) {which:12s} SM MH ratio  " + "  ".join(out))
