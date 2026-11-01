"""Summarise z53_forestclass_forest output lines: per root set, the primes at which no root of the set lies in a
bichromatic component (full component / depth<=1 / depth<=2), the max rank of the first hit, and the max first-hit
root.  Only n ≡ 1 (mod 8) and n ≡ 5 (mod 8) are reported separately.
Usage: uv run python scripts/z53_forestclass_summarize.py FILE [maxlist]
"""
import sys
from collections import defaultdict

SETS = ["ALL", "SM", "SP", "NR", "SMN", "SQ"]


def parse(line):
    d = {}
    toks = line.split()
    i = 0
    while i < len(toks):
        k, v = toks[i].split("=", 1)
        if k in SETS:
            cnt, hit, h1, h2 = map(int, v.split("/"))
            f = toks[i + 1].split("=")[1]
            f100 = toks[i + 2].split("=")[1]
            fa, fr = map(int, f.split("@"))
            ga, gr = map(int, f100.split("@"))
            d[k] = dict(cnt=cnt, hit=hit, h1=h1, h2=h2, fa=fa, fr=fr, ga=ga, gr=gr)
            i += 3
        else:
            d[k] = int(v)
            i += 1
    return d


def main():
    fn = sys.argv[1]
    maxlist = int(sys.argv[2]) if len(sys.argv) > 2 else 30
    stats = defaultdict(lambda: defaultdict(list))
    tot = defaultdict(int)
    maxr = defaultdict(lambda: (0, 0, 0))
    for line in open(fn):
        if not line.startswith("n="):
            continue
        d = parse(line)
        n = d["n"]
        cls = "1mod8" if n % 8 == 1 else ("5mod8" if n % 8 == 5 else "other")
        tot[cls] += 1
        for s in SETS:
            r = d[s]
            if r["cnt"] == 0:
                stats[cls][s + ":empty"].append(n)
                continue
            if r["hit"] == 0:
                stats[cls][s + ":full"].append(n)
            if r["h1"] == 0:
                stats[cls][s + ":d1"].append(n)
            if r["h2"] == 0:
                stats[cls][s + ":d2"].append(n)
            if r["hit"] and r["fr"] > maxr[(cls, s)][0]:
                maxr[(cls, s)] = (r["fr"], r["fa"], n)
    for cls in sorted(tot):
        print(f"## class {cls}: {tot[cls]} n")
        for s in SETS:
            row = []
            for kind in ("full", "d2", "d1", "empty"):
                L = stats[cls].get(s + ":" + kind, [])
                row.append(f"{kind}-fail={len(L)}")
            print(f"  {s}: " + " ".join(row) + f"  maxrank(first hit)={maxr[(cls, s)]}")
            L = stats[cls].get(s + ":full", [])
            if L:
                print(f"     full-fail list (first {maxlist}): {L[:maxlist]}")


if __name__ == "__main__":
    main()
