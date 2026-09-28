"""Test for Chen-type congruences of component sizes (finite evidence only).
uv run python scripts/component_congruences.py FILE.jsonl ...
Reports residue distributions of seed-component size, total vertex count V
and sterile sizes modulo small m, and of seed size modulo tau(t^2)."""
import json, sys
from collections import Counter
from sympy import divisor_count

seed, V, ster, tau = [], [], Counter(), []
for fn in sys.argv[1:]:
    for line in open(fn):
        r = json.loads(line)
        p = r["p"]
        if p < 1000:
            continue
        seed.append(r["seedsize"]); V.append(r["V"])
        for s, c in r["sterile_hist"].items():
            ster[int(s)] += c
        if len(tau) < 20000:
            T = int(divisor_count(((p - 1) // 4) ** 2))
            tau.append((r["seedsize"] % T, T, r["V"] % T))
for m in (2, 3, 4, 5, 6, 8, 12):
    cs = Counter(s % m for s in seed); cv = Counter(v % m for v in V)
    cst = Counter()
    for s, c in ster.items():
        cst[s % m] += c
    print(f"mod {m}: seed {dict(sorted(cs.items()))}  V {dict(sorted(cv.items()))}  sterile {dict(sorted(cst.items()))}")
z = sum(1 for a, T, b in tau if a == 0)
print(f"seed size = 0 mod tau(t^2): {z}/{len(tau)}; expected if uniform ~ {sum(1/T for _,T,_ in tau):.0f}")
z = sum(1 for a, T, b in tau if b == 0)
print(f"V = 0 mod tau(t^2): {z}/{len(tau)}")
