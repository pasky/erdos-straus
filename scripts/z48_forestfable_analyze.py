#!/usr/bin/env python3
"""z48 forestfable — analysis of scan output (scripts/z48_forestfable_scan.c)."""
import gzip
import math
import sys
from collections import Counter

HARD = [193, 409, 577, 2521, 3361, 5569, 9601, 23929, 66529, 83449, 102001, 329617, 712321, 1134241,
        1724209, 1726201, 5212561, 8813281, 5101441, 59929, 4962049, 8803369, 9257329]


def load(path):
    op = gzip.open if path.endswith(".gz") else open
    with op(path, "rt") as f:
        hdr = f.readline().split()
        rows = []
        for line in f:
            vals = list(map(int, line.split()))
            rows.append(dict(zip(hdr, vals)))
    return rows


def main():
    path = sys.argv[1]
    modc = int(sys.argv[2]) if len(sys.argv) > 2 else 24
    rows = load(path)
    allrows = rows
    rows = [r for r in rows if r["p"] % modc == 1]
    n = len(rows)
    print(f"file {path}: {len(allrows)} primes p≡1(4); restricting to p≡1 (mod {modc}): {n} primes, max p = {rows[-1]['p']}")
    print(f"total edges {sum(r['W'] for r in allrows)}, bichromatic {sum(r['B'] for r in allrows)}, "
          f"viol_slot {sum(r['viol_slot'] for r in allrows)}, viol_classB {sum(r['viol_classB'] for r in allrows)}")
    print(f"primes with B=0 (ES5 failures): {sum(1 for r in allrows if r['B']==0)}")

    def fails(key):
        return [r["p"] for r in rows if not r[key]]

    print("\n== sub-line failure counts over p ≡ 1 (mod %d) ==" % modc)
    for key, desc in [("L0", "some bichromatic edge has an endpoint ≡ 0 (4)  [López line, both orientations]"),
                      ("L7", "... endpoint ≡ 7 (8)"),
                      ("L3", "... endpoint ≡ 3 (8)"),
                      ("Lodd", "... both endpoints odd"),
                      ("Lp1", "line u=1 (QNR divisor of p+1; λ=2)"), ("Lp2", "line u=2"), ("Lp3", "line u=3"),
                      ("Lp4", "line u=4"), ("Lp7", "line u=7 (children of 7 only)"), ("Lp15", "line u=15 (children only)"),
                      ("V7", "vertex 7 non-isolated (any orientation)"), ("V15", "vertex 15 non-isolated (any orientation)"),
                      ("Lt2", "level t=2"), ("Lt3", "level t=3"), ("Lt4", "level t=4 ((★) C=1)"), ("Lt7", "level t=7"),
                      ("Lt15", "level t=15"),
                      ("LprimeA", "some bichromatic edge has a prime numerator A or A*"),
                      ("Lleg", "Legendre level: some bichromatic edge at a level t = 4^a t', t' ≡ 7 (8)  [z1_legendre_levels]"),
                      ("Ltuv4", "some word has a coordinate t,u,v ≡ 0 (4)  [two-line union (★)∪López, SPARKS9 Cor 1.2]"),
                      ("LA7", "some bichromatic edge has a numerator A or A* ≡ 0 (4) or ≡ 7 (8)  [y5 P_h position]"),
                      ("c1bi", "component of 1 is bichromatic"),
                      ("maxbi", "largest component is bichromatic"),
                      ("bi_in_big", "some bichromatic edge lies in a component of size ≥ 3")]:
        f = fails(key)
        print(f"  {key:8s} fails {len(f):6d}/{n}  ({len(f)/n:.4f})  first: {f[:8]}   {desc}")
    # unions
    def union_fail(keys):
        return [r["p"] for r in rows if not any(r[k] for k in keys)]
    print("\n== unions ==")
    for keys in [("L0", "L7"), ("L0", "L7", "L3"), ("Lp1", "Lp2", "Lp3", "Lp4", "Lp7", "Lp15"),
                 ("Lt2", "Lt3", "Lt4", "Lt7", "Lt15"),
                 ("Lp1", "Lp2", "Lp3", "Lp4", "Lp7", "Lp15", "Lt2", "Lt3", "Lt4", "Lt7", "Lt15"),
                 ("Lp1", "Lp2", "Lp3", "Lp4", "V7", "V15"), ("Lp1", "Lp2", "Lp3", "Lp4", "V7", "V15", "Lt2", "Lt3", "Lt4", "Lt7", "Lt15"),
                 ("L0", "Lp1", "Lp2", "Lp3", "Lt2", "Lt3"), ("c1bi", "L0"), ("c1bi", "L0", "L7")]:
        f = union_fail(keys)
        print(f"  {'+'.join(keys):55s} fails {len(f):6d}  first: {f[:10]}")

    print("\n== sign-free family word counts (means over last 20% of primes; all words in these families are certificates) ==")
    tail0 = rows[int(0.8 * n):]
    for key, desc in [("n07", "endpoint ≡ 0 (4) or 7 (8)"), ("nleg", "Legendre level"), ("ntuv4", "coordinate ≡ 0 (4)"), ("nA7", "numerator ≡ 0 (4) or 7 (8)"), ("B", "all bichromatic"), ("W", "all words")]:
        m = sum(r[key] for r in tail0) / len(tail0)
        print(f"  mean {key:6s} = {m:7.2f}   (/log^2 p = {sum(r[key]/math.log(r['p'])**2 for r in tail0)/len(tail0):.3f})   {desc}")
    print("\n== v07min = least non-isolated vertex ≡ 0 (4) or 7 (8);  lmin = least prime numerator of a certificate edge ==")
    for key in ["v07min", "lmin"]:
        vals = [r[key] for r in rows]
        mx = max(rows, key=lambda r: r[key])
        print(f"  max {key} = {mx[key]} at p={mx['p']} (log p={math.log(mx['p']):.2f})")
        for X in [16, 32, 64, 128, 256, 1000, 10000, 100000]:
            c = sum(1 for v in vals if v > X)
            print(f"    P({key} > {X}) = {c/n:.6f}  ({c})")
    print("\n== extremes ==")
    for key in ["H4", "umin", "tmin", "Amin", "r"]:
        mx = max(rows, key=lambda r: r[key] / math.log(r["p"]) ** 2)
        print(f"  max {key}/log^2 p = {mx[key]/math.log(mx['p'])**2:.4f} at p={mx['p']} ({key}={mx[key]}, r={mx['r']}, H4={mx['H4']})")
    for key in ["umin", "tmin", "Amin", "H4"]:
        mx = max(rows, key=lambda r: r[key])
        print(f"  max {key} = {mx[key]} at p={mx['p']} (log p = {math.log(mx['p']):.2f})")
    mn = min(rows, key=lambda r: r["W"] / math.log(r["p"]) ** 2)
    print(f"  min W/log^2 p = {mn['W']/math.log(mn['p'])**2:.4f} at p={mn['p']} (W={mn['W']}, B={mn['B']})")
    mn = min(rows, key=lambda r: r["B"] / math.log(r["p"]) ** 2)
    print(f"  min B/log^2 p = {mn['B']/math.log(mn['p'])**2:.4f} at p={mn['p']} (W={mn['W']}, B={mn['B']})")
    mn = min((r for r in rows if r["p"] > 10**5), key=lambda r: r["B"])
    print(f"  min B over p>1e5: {mn['B']} at p={mn['p']} (W={mn['W']})")
    mn = min((r for r in rows if r["p"] > 10**5), key=lambda r: r["W"])
    print(f"  min W over p>1e5: {mn['W']} at p={mn['p']} (B={mn['B']})")

    print("\n== means (last 20% of primes) ==")
    tail = rows[int(0.8 * n):]
    L2 = [math.log(r["p"]) ** 2 for r in tail]
    for key in ["W", "B", "ncomp", "maxc", "c1size", "nbicomp", "nonisol"]:
        m = sum(r[key] for r in tail) / len(tail)
        print(f"  mean {key} = {m:.2f}  (/log^2 p: {sum(r[key]/l for r, l in zip(tail, L2))/len(tail):.3f})")
    print(f"  mean B/W = {sum(r['B']/r['W'] for r in tail)/len(tail):.3f}")
    print(f"  fraction maxc==c1size: {sum(1 for r in tail if r['maxc']==r['c1size'])/len(tail):.3f}")
    mono = Counter()
    for r in rows:
        mono["i"] += r["m_i"]; mono["ii"] += r["m_ii"]; mono["iii"] += r["m_iii"]
    tot = sum(r["W"] - r["B"] for r in rows)
    print(f"  monochromatic edges by Theorem B class: {dict(mono)}  total mono {tot}")

    print("\n== hard primes ==")
    byp = {r["p"]: r for r in allrows}
    print("  p        r   W   B   H4 umin tmin  Amin L0 L7 L3 Lodd ncomp maxc maxbi c1size c1bi nbicomp")
    for p in HARD:
        if p in byp:
            r = byp[p]
            print(f"  {p:8d} {r['r']:3d} {r['W']:3d} {r['B']:3d} {r['H4']:4d} {r['umin']:4d} {r['tmin']:4d} {r['Amin']:5d} "
                  f"{r['L0']:2d} {r['L7']:2d} {r['L3']:2d} {r['Lodd']:3d}  {r['ncomp']:4d} {r['maxc']:4d} {r['maxbi']:4d} {r['c1size']:5d} {r['c1bi']:3d} {r['nbicomp']:4d}")

    print("\n== distribution of umin (least smaller endpoint of a certificate edge) ==")
    c = Counter(r["umin"] for r in rows)
    acc = 0
    for k in sorted(c):
        acc += c[k]
        if k <= 16 or c[k] > n // 500:
            print(f"  umin={k:4d}: {c[k]:6d}  cum {acc/n:.4f}")
    print(f"  P(umin>16) = {sum(v for k,v in c.items() if k>16)/n:.4f}, P(umin>64) = {sum(v for k,v in c.items() if k>64)/n:.5f}, max umin = {max(c)}")
    print("\n== distribution of tmin ==")
    c = Counter(r["tmin"] for r in rows)
    acc = 0
    for k in sorted(c):
        acc += c[k]
        if k <= 16:
            print(f"  tmin={k:4d}: {c[k]:6d}  cum {acc/n:.4f}")
    print(f"  P(tmin>16) = {sum(v for k,v in c.items() if k>16)/n:.4f}, max tmin = {max(c)}")


if __name__ == "__main__":
    main()
