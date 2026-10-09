"""O109: tabulate 2-adic closeness of fibre certificates from typei4_lb outputs.
Input lines: L b a c' g delta P1 X F e.  Checks Lemma 1.1 (v_2(F+9) = 3 + v_2(E)) on every row (both
orientations) and prints per-(L,b) counts and max closeness vs t_min = 2 + ceil(L/2).
Usage: typei7_tab.py files..."""
import sys
from collections import defaultdict


def v2(x):
    x = abs(x)
    return (x & -x).bit_length() - 1


import re, os
rows = defaultdict(list)
# completion records of typei4_lb (stderr collected in log.txt next to the files); refuse incomplete cells
done = set()
for fn in sys.argv[1:]:
    lg = os.path.join(os.path.dirname(fn) or ".", "log.txt")
    done |= set(tuple(map(int, m)) for m in re.findall(r"L=(\d+) b=(\d+) solutions", open(lg).read()))
for fn in sys.argv[1:]:
    L0, b0 = map(int, re.findall(r"lb_(\d+)_(\d+)", fn)[0])
    if (L0, b0) not in done:
        sys.exit(f"incomplete or unrecorded run: {fn}")
nchk = 0
for fn in sys.argv[1:]:
    for line in open(fn):
        f = line.split()
        if len(f) != 10:
            continue
        L, b, a, cp, g, dl, P1, X, F, e = map(int, f)
        co, ko = 7**a * cp, 7**b * X
        n = co * ko
        N = 1 + (1 << (L + 2)) * co * ko * ko
        assert F * e == N and F % 16 == 7 and e % 16 == 7
        for (FF, ee) in ((F, e), (e, F)):
            nd = (ee - FF) // 16
            assert (ee - FF) % 16 == 0 and nd % 2 == 1
            E = 5 - 9 * nd - (1 << (L - 2)) * co * ko * ko
            assert v2(FF + 9) == 3 + v2(E)   # Lemma 1.1
            nchk += 1
        rows[(L, b)].append((max(v2(F + 9), v2(e + 9)), v2(F + 9), v2(e + 9), cp, g, dl, a, (min(F, e), max(F, e))))
tot = 0
print("L b  count  distinct-(N,F)  closeness-list  t_min  margin(t_min - max)")
for (L, b) in sorted(rows):
    r = rows[(L, b)]
    tmin = 2 + (L + 1) // 2
    tot += len(r)
    cl = sorted((x[0] for x in r), reverse=True)
    print(L, b, len(r), len({x[7] for x in r}), ",".join(map(str, cl)), tmin, tmin - cl[0], "HIT" if cl[0] >= tmin else "")
print("total certificates", tot, "distinct (F,e) pairs", len({x[7] for r in rows.values() for x in r}), "Lemma 1.1 checks", nchk, file=sys.stderr)
