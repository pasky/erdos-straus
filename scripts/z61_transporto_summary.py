#!/usr/bin/env python3
"""Summarise data/z61/transporto/r1_census.jsonl -> data/z61/transporto/r1_summary.txt (falsifier table numbers)."""
import json, collections, os
ROOT = os.path.join(os.path.dirname(__file__), "..")
R = [json.loads(l) for l in open(os.path.join(ROOT, "data/z61/transporto/r1_census.jsonl"))]

def r1hit(n):  # an r_f = 1 hit: f = 7 (8), f | n+1  (universal sink: r-1 = 0 lies in every fibre)
    return any((n + 1) % f == 0 for f in range(7, n + 2, 8))

out = []
by = collections.defaultdict(list)
for r in R:
    by[r["set"]].append(r)
out.append("set  N  valid  valid_without_r1hit  nH=0  nE=0  stranded[min,max]  forced[min,max]  first_invalid")
for s, L in by.items():
    v = [r for r in L if r["valid"]]
    vw = [r["n"] for r in v if not r1hit(r["n"])]
    inval = sorted(r["n"] for r in L if not r["valid"])
    out.append(f"{s} {len(L)} {len(v)} {vw} {sum(r['nH']==0 for r in L)} {sum(r['nE']==0 for r in L)} "
               f"[{min(r['stranded'] for r in L)},{max(r['stranded'] for r in L)}] "
               f"[{min(r['forced'] for r in L)},{max(r['forced'] for r in L)}] {inval[:1]}")
P = by["P"]
c = collections.Counter((r["n"] % 4, r1hit(r["n"]), r["valid"]) for r in P)
out.append("primes <= PMAX by (n mod 4, has r=1 hit, R1 valid): " + str(sorted(c.items())))
out.append("odd squares valid: " + str([r["n"] for r in by["SQ"] if r["valid"]]))
for s in ("SQ", "Z7"):
    for r in by[s][:4] if s == "SQ" else by[s]:
        out.append(f"  {s} n={r['n']} nE={r['nE']} tokens={r['tokens']} own-exit={r['tok_exit_own']} "
                   f"sink-routed={r['sink_routed']} stranded={r['stranded']} forced={r['forced']} ({r['forced_primes']} primes)")
txt = "\n".join(out) + "\n"
open(os.path.join(ROOT, "data/z61/transporto/r1_summary.txt"), "w").write(txt)
print(txt)

# foreign-flux screen (scripts/z61_transporto_foreign.py)
fp = os.path.join(ROOT, "data/z61/transporto/foreign.jsonl")
if os.path.exists(fp):
    F = {}
    for l in open(fp):
        r = json.loads(l)
        F[r["n"]] = r
    def isprime(n):
        return n > 1 and all(n % q for q in range(2, int(n ** 0.5) + 1))
    Pn = sorted(n for n in F if isprime(n) and n <= 20000)
    cov = [n for n in Pn if F[n]["nUncovered"] == 0]
    lines = [f"foreign screen: primes 13..20000: {len(Pn)}; forced primes all carried by hit columns at {len(cov)}: {cov}",
             "  max nF/nsink sample: " + str([(n, F[n]['nF'], F[n]['nUncovered'], F[n]['nsink']) for n in Pn[-3:]])]
    for n in (169, 289, 361, 529, 105, 409, 2521, 9601, 102001):
        r = F[n]
        lines.append(f"  n={n} sinks={r['nsink']} forced_primes={r['nF']} uncovered={r['nUncovered']} top={r['uncovered_top'][-4:]}")
    t2 = "\n".join(lines) + "\n"
    open(os.path.join(ROOT, "data/z61/transporto/r1_summary.txt"), "a").write(t2)
    print(t2)
