"""Stratified enrichment of class-group membership for lying in a bichromatic component.
Input: strat files of z53_forestclass_forest (-s): rows chi amod8 inSM inSP log2bucket count nonisolated inBichrom.
For each size-bucket range and each membership flag F in {SM, SP}, compares rate(F=1) with rate(F=0) inside strata
(chi, a mod 8, other flag, bucket) and reports the Mantel–Haenszel-type pooled ratio
  RR = Σ_s x1_s n0_s/N_s / Σ_s x0_s n1_s/N_s  (x = #inBichrom (or #nonisolated), n = #roots)
plus raw rates.  Only n ≡ 1 (mod 8) censuses should be fed (the census files are p ≡ 1 mod 8 above 1e7; the 1e7 file
mixes p ≡ 5 (8), where a ≡ 0 (8) is never in SP and the edge {1,2} dominates).
Usage: uv run python scripts/z53_forestclass_enrich.py FILE...
"""
import sys
from collections import defaultdict

rows = defaultdict(lambda: [0, 0, 0])
for fn in sys.argv[1:]:
    for line in open(fn):
        if line.startswith("#"):
            continue
        c, m, sm, sp, b, n, ni, bi = map(int, line.split())
        r = rows[(c, m, sm, sp, b)]
        r[0] += n
        r[1] += ni
        r[2] += bi

BR = [(4, 6), (7, 9), (10, 12), (13, 15), (16, 18), (19, 21), (22, 24)]
for flag in ("SM", "SP"):
    print(f"## membership flag {flag} (strata: chi, a mod 8, other flag, log2 bucket)")
    for lo, hi in BR:
        for which, idx in (("nonisolated", 1), ("bichromComp", 2)):
            num = den = 0.0
            n1 = x1 = n0 = x0 = 0
            strata = defaultdict(lambda: [[0, 0], [0, 0]])
            for (c, m, sm, sp, b), r in rows.items():
                if not (lo <= b <= hi):
                    continue
                f = sm if flag == "SM" else sp
                o = sp if flag == "SM" else sm
                s = strata[(c, m, o, b)]
                s[f][0] += r[0]
                s[f][1] += r[idx]
            for key, ((nn0, xx0), (nn1, xx1)) in strata.items():
                N = nn0 + nn1
                if nn0 == 0 or nn1 == 0:
                    continue
                num += xx1 * nn0 / N
                den += xx0 * nn1 / N
                n1 += nn1; x1 += xx1; n0 += nn0; x0 += xx0
            rr = num / den if den else float("nan")
            r1 = x1 / n1 if n1 else float("nan")
            r0 = x0 / n0 if n0 else float("nan")
            print(f"  a in [2^{lo},2^{hi+1}) {which:12s}: rate(in)={r1:.5f} (n={n1}, x={x1})  rate(out)={r0:.5f} "
                  f"(n={n0})  MH ratio={rr:.3f}")
