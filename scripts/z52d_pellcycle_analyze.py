r"""z52d PELLCYCLE: tables from census.jsonl.
Usage: uv run python scripts/z52d_pellcycle_analyze.py data/z52d/pellcycle/census.jsonl
"""
import json
import sys
from collections import defaultdict

rows = [json.loads(l) for l in open(sys.argv[1])]
fams = ["Z", "N", "D", "C24", "CD", "H"]
by = defaultdict(list)
for r in rows:
    by[r["fam"]].append(r)
    if r["fam"] in ("Z", "N"):
        by["ZN"].append(r)

print(f"{len(rows)} primes; families: " + ", ".join(f"{f}={len(by[f])}" for f in fams))
for R in ("R0", "R1", "R2", "R3"):
    print(f"\n### root set {R}")
    print("| family | #p | mean |R| | mean #roots≥8 | primes with a hit (depth 2) | primes with a hit (full comp.) | censored roots |"
          " per-root hit rate, roots≥8, full: cycle / size-matched random / size+colour-matched |"
          " same, depth 2 | P(any hit, full) for size-matched random root sets |")
    print("|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|")
    for f in ["ZN", "D", "C24", "CD", "H"]:
        L = by[f]
        if not L:
            continue
        n = len(L)
        nR = sum(r[R]["n"] for r in L) / n
        nb = sum(r[R]["nbig"] for r in L) / n
        a2 = sum(r[R]["any2"] for r in L)
        af = sum(r[R]["anyf"] for r in L)
        cen = sum(r[R]["cens"] for r in L)
        hb = sum(r[R]["hitf_big"] for r in L)
        hb2 = sum(r[R]["hit2_big"] for r in L)
        tb = sum(r[R]["nbig"] for r in L)
        bs = [sum(r[R]["base"][k][x] for r in L) for k in ("size", "sizecol") for x in ("hitf", "hit2", "tot")]
        anyb = sum(r[R]["base"]["size"]["anyf"] for r in L) / sum(r[R]["base"]["size"]["K"] for r in L)
        pct = lambda a, b: f"{100 * a / b:.2f}%" if b else "—"
        print(f"| {f} | {n} | {nR:.0f} | {nb:.0f} | {a2}/{n} | {af}/{n} | {cen} | "
              f"{pct(hb, tb)} / {pct(bs[0], bs[2])} / {pct(bs[3], bs[5])} | "
              f"{pct(hb2, tb)} / {pct(bs[1], bs[2])} / {pct(bs[4], bs[5])} | {anyb:.3f} |")

print("\n### primes where NO component meeting the root set has a bichromatic edge")
for R in ("R0", "R1", "R2", "R3"):
    fails = [(r["fam"], r["p"], r["periodS"]) for r in rows if not r[R]["anyf"]]
    print(f"* {R}: {len(fails)} — " + ", ".join(f"{p} ({f}, period {per})" for f, p, per in fails))
print("\n### test primes: hits in R3 (full component), small roots <8 hitting, period of sqrt(p)")
for r in sorted(rows, key=lambda r: r["p"]):
    if r["fam"] in ("Z", "N"):
        print(f"* {r['p']} ({r['fam']}): period {r['periodS']}/{r['periodW']}, |R0|={r['R0']['n']}, |R3|={r['R3']['n']}, "
              f"R0 hits {r['R0']['hitf']} (depth-2 {r['R0']['hit2']}), R3 hits {r['R3']['hitf']}, small-root hits {r['R3']['small_hitf']}, first hit roots {r['R3']['hits'][:8]}")

print("\n### paired per-prime difference (cycle per-root hit rate − baseline), roots ≥ 8, mean ± s.e. over primes")
import math as _m
print("| root set | family | #p | full: − size | full: − size+colour | depth 2: − size | depth 2: − size+colour |")
print("|---|---|---:|---:|---:|---:|---:|")
for R in ("R0", "R3"):
    for f in ["ZN", "D", "C24", "CD", "ALL"]:
        L = [r for r in rows if r["fam"] != "H"] if f == "ALL" else by[f]
        cells = []
        for key, b in (("hitf_big", "size"), ("hitf_big", "sizecol"), ("hit2_big", "size"), ("hit2_big", "sizecol")):
            bx = "hitf" if key == "hitf_big" else "hit2"
            ds = [r[R][key] / r[R]["nbig"] - r[R]["base"][b][bx] / r[R]["base"][b]["tot"]
                  for r in L if r[R]["nbig"] and r[R]["base"][b]["tot"]]
            mu = sum(ds) / len(ds)
            se = _m.sqrt(sum((d - mu) ** 2 for d in ds) / (len(ds) - 1) / len(ds))
            cells.append(f"{100 * mu:+.2f} ± {100 * se:.2f} pp")
        print(f"| {R} | {f} | {len(L)} | " + " | ".join(cells) + " |")
