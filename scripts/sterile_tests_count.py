"""Count 'positive-capable' denominators ('tests') in sterile components.

A positive vertex has all denominators positive: its p-free ones exceed p/4
(anchors x=t+a, a>=1), its Type I p-divisible one has h>=1, its Type II ones
have non-residue labels.  A component is sterile iff every such denominator
it contains has an all-nonpositive fibre ('failed test').
uv run python scripts/sterile_tests_count.py FILE.jsonl|CERT.json.gz ...
"""
import gzip, json, sys
from collections import Counter


def tests(p, comp):
    t = (p - 1) // 4
    dens = {z for v in comp for z in v}
    anchors = [z - t for z in dens if z % p and t + 1 <= z <= 2 * t]
    hs = []
    for z in dens:
        if z % p == 0 and (4 * (z // p) - 1) % p == 0:
            h = (z // p + t) // p
            if h >= 1:
                hs.append(h)
    return sorted(anchors), sorted(hs)


if __name__ == "__main__":
    rows = []
    for fn in sys.argv[1:]:
        if fn.endswith(".gz"):
            c = json.load(gzip.open(fn, "rt"))
            p = int(c["p"])
            comp = [tuple(map(int, v)) for v in c["vertices"]]
            a, h = tests(p, comp)
            print(f"{fn}: p={p} size={len(comp)} tests={len(a)+len(h)} anchors(a>=1)={a[:20]} h>=1={h[:20]}")
        else:
            for line in open(fn):
                r = json.loads(line)
                for C in r.get("dumped", []):
                    comp = [tuple(map(int, v)) for v in C]
                    a, h = tests(r["p"], comp)
                    rows.append((len(a) + len(h), len(comp), r["p"], a, h))
    if rows:
        rows.sort(reverse=True)
        print("max tests in dumped sterile comps:")
        for T, n, p, a, h in rows[:15]:
            print(T, n, p, a[:10], h[:10])
        print("tests histogram", sorted(Counter(r[0] for r in rows).items()))
