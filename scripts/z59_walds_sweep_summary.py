#!/usr/bin/env python3
"""z59 WALDS: summarise data/z59/walds/halfint_sweep_*.txt -> one line per level L.
Usage: python3 scripts/z59_walds_sweep_summary.py data/z59/walds/halfint_sweep_A.txt data/z59/walds/halfint_sweep_B.txt
"""
import re, sys
from collections import defaultdict

runs = []
for fn in sys.argv[1:]:
    cur = None
    for line in open(fn):
        m = re.match(r"L=(\d+) N=(\d+) D=(-?\d+) (?:space=\d+ )?dim=(\d+) B=(\d+) l0=(\d+) #T1-conditions=(\d+) rank\(cond\)=(\d+) dimK=(\d+)", line)
        if m:
            cur = dict(L=int(m[1]), D=int(m[3]), dim=int(m[4]), B=int(m[5]), l0=int(m[6]), rc=int(m[8]), dK=int(m[9]), ranks={})
            runs.append(cur)
            continue
        m = re.match(r"\s+rank of K on (\S+) \(n<=B, (\d+) indices\) = (\d+)", line)
        if m and cur is not None:
            cur["ranks"][m[1]] = (int(m[3]), int(m[2]))
by = defaultdict(list)
for r in runs:
    by[r["L"]].append(r)
print("L | #psi | dim M_{3/2} (range) | B | rank T1-rows l0=0 / l0=11 (range) | max rank of K on C1 (l0=0 / l0=11) | #C1 indices | #Mordell indices")
tot = bad = 0
for L in sorted(by):
    rs = by[L]
    a = [r for r in rs if r["l0"] == 0]
    b = [r for r in rs if r["l0"] == 11]
    tot += len(rs)
    bad += sum(1 for r in rs if any(v[0] for v in r["ranks"].values()))
    dims = sorted({r["dim"] for r in rs})
    f = lambda xs: f"{min(xs)}-{max(xs)}" if xs else "-"
    print(f"{L} | {len(a)} | {f(dims)} | {rs[0]['B']} | {f([r['rc'] for r in a])} / {f([r['rc'] for r in b])} | "
          f"{max((r['ranks'].get('C1', (0, 0))[0] for r in a), default='-')} / {max((r['ranks'].get('C1', (0, 0))[0] for r in b), default='-')} | "
          f"{rs[0]['ranks'].get('C1', (0, 0))[1]} | {rs[0]['ranks'].get('Mordell-classes', (0, 0))[1]}")
print(f"# runs: {tot}; runs with a non-zero rank on any C1 subset: {bad}")
