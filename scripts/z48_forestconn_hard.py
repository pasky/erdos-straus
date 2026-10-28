"""z48 forestconn: characterise primes with H4 > c·log²p (no bichromatic component below c·log²p).

For each such prime list, for small roots u <= 12, the least certifying child of u
(v | p+u, v == -p mod u, v > u, opposite colour; sympy divisors + Legendre, independent of C),
normalised by log²p, plus r(p) mod 4 and whether r(p) attaches.
usage: uv run python scripts/z48_forestconn_hard.py c csv.gz [csv.gz ...]
"""
import csv, gzip, math, sys
from collections import Counter
from sympy import divisors, legendre_symbol

def least_cert_child(p, u):
    cu = legendre_symbol(u % p, p)
    best = 0
    for v in divisors(p + u):
        if v > u and (v + p) % u == 0 and v <= p + 2 and v % p:
            if legendre_symbol(v % p, p) == -cu:
                return v  # divisors are sorted
    return best

c = float(sys.argv[1])
rows = []
for fn in sys.argv[2:]:
    for r in csv.DictReader(gzip.open(fn, "rt")):
        if int(r["H4"]) > c * float(r["L2"]):
            rows.append(r)
seen = set()
US = range(1, 13)
print(f"primes with H4 > {c}·log²p: {len(rows)}")
print("| p | H4/L² | r | r mod 4 | r attaches | " + " | ".join(f"u={u}" for u in US) + " |")
print("|---:|---:|---:|---:|---:|" + "---:|" * len(US))
agg = Counter()
for r in sorted(rows, key=lambda r: int(r["p"])):
    p = int(r["p"])
    if p in seen:
        continue
    seen.add(p)
    L2 = float(r["L2"])
    cells = []
    for u in US:
        if legendre_symbol(u, p) == 0:
            cells.append("—"); continue
        v = least_cert_child(p, u)
        cells.append("∅" if not v else f"{v / L2:.2g}")
        if v and v <= L2: agg[f"star{u}<=L2"] += 1
    ra = int(r["rootr"]) < int(r["r"]) and int(r["rootr"]) > 0
    agg[f"r%4={int(r['r']) % 4}"] += 1
    agg["r attaches"] += ra
    print(f"| {p} | {int(r['H4']) / L2:.3f} | {r['r']} | {int(r['r']) % 4} | {'yes' if ra else 'no'} | " + " | ".join(cells) + " |")
print(f"\naggregate over {len(seen)} distinct primes: {dict(sorted(agg.items()))}")
