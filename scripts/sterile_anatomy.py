"""Anatomy of dumped sterile components (from sterile_survey.py --dump output).

uv run python scripts/sterile_anatomy.py FILE.jsonl [minsize]

For each dumped component: the denominator shared by most vertices (the hub),
its kind -- p-free anchor with a=x-t, Type I p-divisible bucket with
h=(m+t)/p, or Type II label -- the hub coverage, the number of Type I/II
vertices, and the number of vertices off the hub.  Finite description only.
"""
import json, sys
from collections import Counter


def kind(p, z):
    t = (p - 1) // 4
    if z % p:
        return f"x a={z - t}" if 1 <= z <= 2 * t else f"free {'neg' if z < 0 else 'big'}"
    m = z // p
    if (4 * m - 1) % p == 0:
        return f"I h={(m + t) // p}"
    return "II"


def analyze(p, comp):
    comp = [tuple(map(int, v)) for v in comp]
    deg = Counter(z for v in comp for z in set(v))
    hub, d = deg.most_common(1)[0]
    types = Counter(sum(z % p == 0 for z in v) for v in comp)
    shared = sorted(((c, kind(p, z)) for z, c in deg.items() if c > 1), reverse=True)
    return dict(p=p, size=len(comp), hub=kind(p, hub), hubdeg=d, typeI=types[1], typeII=types[2],
                shared=shared[:8])


if __name__ == "__main__":
    minsize = int(sys.argv[2]) if len(sys.argv) > 2 else 20
    out = []
    for line in (__import__("gzip").open(sys.argv[1], "rt") if sys.argv[1].endswith(".gz") else open(sys.argv[1])):
        r = json.loads(line)
        for C in r.get("dumped", []):
            if len(C) >= minsize:
                out.append(analyze(r["p"], C))
    for a in sorted(out, key=lambda a: -a["size"]):
        print(json.dumps(a))
    hk = Counter(a["hub"].split()[0] + (" a<=0" if a["hub"].startswith("x a=-") or a["hub"] == "x a=0" else "") for a in out)
    print("hub kinds:", dict(hk))
