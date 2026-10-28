"""z48 forestconn: tables from the scan CSVs (census to 1e7 = full forests; list runs = vertex cap).

usage: uv run python scripts/z48_forestconn_analyze.py census.csv.gz [list.csv.gz ...]
"""
import csv
import gzip
import math
import statistics as st
import sys
from collections import Counter

from sympy import factorint

CS = ["0.25", "0.5", "1", "2", "4", "8"]
RSTAR0 = [409, 577, 5569, 9601, 23929, 83449, 102001, 329617, 712321, 1134241, 1724209, 1726201, 5212561, 8813281]
NAMED = [193, 409, 577, 2521, 3361, 5569, 9601, 66529]


def load(fn):
    with gzip.open(fn, "rt") as f:
        rows = []
        for r in csv.DictReader(f):
            for k, v in r.items():
                if k != "tag":
                    r[k] = float(v) if k == "L2" else int(v)
            rows.append(r)
    return rows


def q3(p):
    """least prime q == 3 mod 4 dividing (p+1)/2, else 0 (root-1 depth-1 certificate)."""
    f = factorint((p + 1) // 2)
    c = [q for q in f if q % 4 == 3]
    return min(c) if c else 0


def pct(a, b):
    return f"{a}/{b} ({100.0 * a / b:.2f}%)" if b else f"{a}/0"


def census(rows):
    out = []
    P = print
    n = len(rows)
    P(f"## census: {n} primes p == 1 (mod 24), p <= {max(r['p'] for r in rows)}, full forests: {all(r['full'] for r in rows)}")
    P(f"edges {sum(r['edges'] for r in rows)}, bichromatic {sum(r['negedges'] for r in rows)}")
    # decades
    P("\n### A. by range: comp(1) / comp(r) / mechanism (full forest)")
    P("| range | primes | comp(1) monochromatic | comp(r) has no QR | r has a parent (H4=r) | root(r)=1 | rho*=1 | rho*=root(r) | H4>log²p |")
    P("|---|---:|---:|---:|---:|---:|---:|---:|---:|")
    edges = [0, 10**4, 10**5, 10**6, 3 * 10**6, 10**7 + 1]
    for lo, hi in zip(edges, edges[1:]):
        S = [r for r in rows if lo < r["p"] <= hi]
        m = len(S)
        if not m:
            continue
        P(f"| ({lo:.0e},{hi:.0e}] | {m} | {pct(sum(r['B1'] == 0 for r in S), m)} | {pct(sum(r['Br'] == 0 for r in S), m)} | "
          f"{pct(sum(r['rootr'] < r['r'] for r in S), m)} | {pct(sum(r['rootr'] == 1 for r in S), m)} | {pct(sum(r['rho'] == 1 for r in S), m)} | "
          f"{pct(sum(r['rho'] == r['rootr'] for r in S), m)} | {pct(sum(r['H4'] > r['L2'] for r in S), m)} |")
    both = [r for r in rows if r["B1"] == 0 and r["Br"] == 0]
    P(f"\ncomp(1) monochromatic AND comp(r) monochromatic (full forest): {pct(len(both), n)}; first: {[r['p'] for r in both[:12]]}")
    P(f"comp(1) monochromatic: first 20 = {[r['p'] for r in rows if r['B1'] == 0][:20]}")
    P(f"largest p with comp(1) monochromatic: {[r['p'] for r in rows if r['B1'] == 0][-5:]}")
    P(f"comp(1) monochromatic: c1size distribution {sorted(Counter(r['c1size'] for r in rows if r['B1'] == 0).items())[:25]}")
    P(f"comp(1) monochromatic: max c1size {max(r['c1size'] for r in rows if r['B1'] == 0)}")

    # B1 vs log^2
    P("\n### B. Thresholds V = c·log²p: fraction of primes with the property inside F_p|[1,V]")
    P("| c | H4 ≤ V (some comp. bichromatic) | comp(1) bichromatic | 1~r (root(r)=1, r ≤ V) | r ≤ V and comp(r) has QR ≤ V | mean #comp/V | mean ∣comp(1)∣ | mean largest | mean max depth | mean #isolated/V |")
    P("|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|")
    for c in CS:
        cc = float(c)
        S = [r for r in rows if r["ncomp" + c] > 0]
        m = len(S)
        V = lambda r: r["V" + c]
        P(f"| {c} | {pct(sum(r['nmix' + c] > 0 for r in S), m)} | {pct(sum(r['c1mix' + c] for r in S), m)} | "
          f"{pct(sum(r['rootr'] == 1 and r['r'] <= V(r) for r in S), m)} | {pct(sum(r['r'] <= V(r) and 0 < r['Br'] <= V(r) for r in S), m)} | "
          f"{st.mean(r['ncomp' + c] / V(r) for r in S):.3f} | {st.mean(r['c1size' + c] for r in S):.1f} | {st.mean(r['largest' + c] for r in S):.1f} | "
          f"{st.mean(r['maxdepth' + c] for r in S):.2f} | {st.mean(r['nsingle' + c] / V(r) for r in S):.3f} |")
    # by range at c=1
    P("\n### B'. c = 1 by range (fraction failing)")
    P("| range | primes | no bichromatic comp ≤ log²p | comp(1) mono ≤ log²p | comp(1) mono in FULL F_p | mean ∣comp(1)∩[1,log²p]∣ | mean #comp ≤ log²p / log²p |")
    P("|---|---:|---:|---:|---:|---:|---:|")
    for lo, hi in zip(edges, edges[1:]):
        S = [r for r in rows if lo < r["p"] <= hi]
        m = len(S)
        P(f"| ({lo:.0e},{hi:.0e}] | {m} | {pct(sum(r['nmix1'] == 0 for r in S), m)} | {pct(sum(r['c1mix1'] == 0 for r in S), m)} | {pct(sum(r['B1'] == 0 for r in S), m)} | "
          f"{st.mean(r['c1size1'] for r in S):.2f} | {st.mean(r['ncomp1'] / r['V1'] for r in S):.3f} |")

    # rho distribution
    P("\n### C. Root of the first bichromatic component (rho*) and its depth")
    cnt = Counter("1" if r["rho"] == 1 else ("root(r)=r" if r["rho"] == r["rootr"] == r["r"] else ("root(r)<r" if r["rho"] == r["rootr"] else "other")) for r in rows)
    P(f"rho* classes: {dict(cnt)}")
    P(f"rho* values (top 15): {Counter(r['rho'] for r in rows).most_common(15)}")
    P(f"depth of the H4 vertex: {sorted(Counter(r['depthH4'] for r in rows).items())}")
    P(f"H4 == r: {pct(sum(r['H4'] == r['r'] for r in rows), n)};  H4 vertex is QNR: n/a (edge bichromatic either way)")
    P(f"max depth in full forest: {sorted(Counter(r['maxdepth'] for r in rows).items())}")
    P(f"depth of r: {sorted(Counter(r['depthr'] for r in rows).items())}")

    # K vs H4
    P("\n### D. Smallest *complete* bichromatic component: K = min over bichromatic components of their max vertex")
    rat = [r["K"] / r["H4"] for r in rows]
    P(f"K == H4: {pct(sum(r['K'] == r['H4'] for r in rows), n)}; K/H4: median {st.median(rat):.2f}, mean {st.mean(rat):.2f}, max {max(rat):.1f}")
    rk = [r["K"] / r["L2"] for r in rows]
    P(f"K/log²p: median {st.median(rk):.2f}, 90% {sorted(rk)[int(0.9 * n)]:.2f}, 99% {sorted(rk)[int(0.99 * n)]:.2f}, max {max(rk):.2f} at p={max(rows, key=lambda r: r['K'] / r['L2'])['p']}")
    P(f"size of that component: {sorted(Counter(r['Ksize'] for r in rows).items())[:15]}")
    P(f"min size of a bichromatic component: {sorted(Counter(r['minmixsize'] for r in rows).items())[:10]}")
    P(f"number of bichromatic components in full F_p: mean {st.mean(r['nmixed'] for r in rows):.1f}, min {min(r['nmixed'] for r in rows)}, nmixed/log²p mean {st.mean(r['nmixed'] / r['L2'] for r in rows):.3f}")
    # B1 and Br normalized
    P("\n### E. Normalised heights (full forest)")
    for name, key in (("H4", "H4"), ("B1 (first QNR in comp(1))", "B1"), ("Br (least QR in comp(r))", "Br")):
        S = [r[key] / r["L2"] for r in rows if r[key] > 0]
        S.sort()
        P(f"{name}/log²p over {len(S)} primes where finite: median {st.median(S):.3f}, 90% {S[int(.9 * len(S))]:.3f}, 99% {S[int(.99 * len(S))]:.3f}, 99.9% {S[int(.999 * len(S))]:.3f}, max {S[-1]:.3f}")
    S = [(r["B1"] / r["L2"], r["p"]) for r in rows if r["B1"]]
    P(f"top B1/log²p: {sorted(S)[-8:]}")
    return rows


def hard_table(rows, title, plist):
    by = {r["p"]: r for r in rows}
    print(f"\n### {title}")
    print("| p | r | H4 | edge (u,H4,t) | rho* | B1 | root(r) | Br | ∣comp(1)∣ | ∣comp(r)∣ | #bichrom. comps | K | Ksize | maxdepth |")
    print("|---:|---:|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|")
    for p in plist:
        r = by.get(p)
        if not r:
            print(f"| {p} | (absent) |")
            continue
        print(f"| {p} | {r['r']} | {r['H4']} | ({r['H4u']},{r['H4']},{r['H4t']}) | {r['rho']} | {r['B1'] or '∅'} | {r['rootr']} | {r['Br'] or '∅'} | {r['c1size']} | {r['crsize']} | {r['nmixed']} | {r['K']} | {r['Ksize']} | {r['maxdepth']} |")


def hard_by_ratio(rows, c=1.0, limit=60):
    S = [r for r in rows if r["H4"] == 0 or r["H4"] > c * r["L2"]]
    print(f"\n### F. Primes with NO bichromatic component in F_p|[1,{c}·log²p]: {len(S)} of {len(rows)}")
    print("| p | H4 | H4/log²p | r | H4/r | q3((p+1)/2) | B1/log²p | root(r) | Br | p mod 5,7,11,13 | pattern |")
    print("|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|")
    feats = Counter()
    for r in sorted(S, key=lambda r: -r["H4"] / r["L2"] if r["H4"] else -1e9)[:limit]:
        p = r["p"]
        q = q3(p)
        pat = []
        if q == 0:
            pat.append("(p+1)/2 has no q≡3(4)")
        if r["rootr"] == r["r"]:
            pat.append("r is a root")
        if r["B1"] == 0:
            pat.append("comp(1) mono")
        print(f"| {p} | {r['H4']} | {r['H4'] / r['L2']:.3f} | {r['r']} | {r['H4'] / r['r']:.2f} | {q or '—'} | {r['B1'] / r['L2'] if r['B1'] else float('nan'):.2f} | {r['rootr']} | {r['Br'] or '∅'} | {p % 5},{p % 7},{p % 11},{p % 13} | {'; '.join(pat)} |")
    for r in S:
        feats["q3 absent" if q3(r["p"]) == 0 else "q3 present"] += 1
        feats["r root" if r["rootr"] == r["r"] else "r has parent"] += 1
        feats["comp1 mono(full)" if r["B1"] == 0 else "comp1 mixed(full)"] += 1
    print(f"feature counts over all {len(S)}: {dict(feats)}")
    return S


def list_summary(rows, title):
    print(f"\n## {title}: {len(rows)} primes, vertex cap N = {sorted(set(r['N'] for r in rows))[:3]}...")
    tags = sorted(set(r["tag"] for r in rows))
    print("| family | primes | max p | H4 ≤ log²p | comp(1) mixed ≤ log²p | comp(1) mixed ≤ N | root(r)=1 | r has parent | comp(r) has QR ≤ N | max H4/log²p | max B1/log²p (finite) |")
    print("|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|")
    for t in tags:
        S = [r for r in rows if r["tag"] == t]
        m = len(S)
        b1 = [r["B1"] / r["L2"] for r in S if r["B1"]]
        print(f"| {t} | {m} | {max(r['p'] for r in S):.3g} | {pct(sum(r['nmix1'] > 0 for r in S), m)} | {pct(sum(r['c1mix1'] for r in S), m)} | {pct(sum(r['B1'] > 0 for r in S), m)} | "
              f"{pct(sum(r['rootr'] == 1 for r in S), m)} | {pct(sum(0 < r['rootr'] < r['r'] for r in S), m)} | {pct(sum(r['Br'] > 0 for r in S), m)} | "
              f"{max(r['H4'] / r['L2'] for r in S):.3f} | {max(b1) if b1 else float('nan'):.2f} |")


if __name__ == "__main__" and sys.argv[-1] not in ("--edges", "--trend"):
    rows = census(load(sys.argv[1]))
    hard_table(rows, "G. Named hard primes (full forest)", NAMED)
    hard_table(rows, "G'. The 14 primes with R(p)=0 (full forest)", RSTAR0)
    hard_by_ratio(rows, 1.0)
    for fn in sys.argv[2:]:
        L = load(fn)
        list_summary(L, fn)
        hard_by_ratio(L, 1.0, limit=40)
        hard_table(L, "named/adversarial (vertex-capped)", [r["p"] for r in L if r["tag"] in ("named",)])


def h4_edge_classes(rows):
    """slot type and smaller endpoint of the minimal certificate edge; r-attachment by r."""
    print("\n### H. The minimal certificate edge (u, H4, t)")
    def stype(t, u, v):
        s = []
        if t % 4 == 0: s.append("4|t")
        if u % 4 == 0: s.append("4|u")
        if v % 4 == 0: s.append("4|v")
        if (t * u - 1) % 4 == 0: s.append("4|tu-1")
        if (t * v - 1) % 4 == 0: s.append("4|tv-1")
        return "+".join(s)
    c = Counter(stype(r["H4t"], r["H4u"], r["H4"]) for r in rows)
    print(f"slot types: {c.most_common()}")
    cu = Counter(r["H4u"] if r["H4u"] <= 6 else ">6" for r in rows)
    print(f"smaller endpoint u: {sorted(cu.items(), key=str)}")
    print(f"u in {{1,2,3,4,6}} (quadratic-layer star): {pct(sum(r['H4u'] in (1, 2, 3, 4, 6) for r in rows), len(rows))}")
    print("\n| r(p) | primes | r has parent (H4=r) | root(r)=1 | comp(1) mono (full) | comp(r) mono (full) | H4>0.5log²p |")
    print("|---:|---:|---:|---:|---:|---:|---:|")
    for rv in sorted(set(r["r"] for r in rows)):
        S = [r for r in rows if r["r"] == rv]
        m = len(S)
        print(f"| {rv} | {m} | {pct(sum(r['rootr'] < rv for r in S), m)} | {pct(sum(r['rootr'] == 1 for r in S), m)} | {pct(sum(r['B1'] == 0 for r in S), m)} | {pct(sum(r['Br'] == 0 for r in S), m)} | {pct(sum(r['H4'] > 0.5 * r['L2'] for r in S), m)} |")


if __name__ == "__main__" and len(sys.argv) > 1 and sys.argv[-1] == "--edges":
    h4_edge_classes(load(sys.argv[1]))


def trend(rows):
    """log-log fit of failure frequencies vs log p (EVIDENCE only; small range of log p)."""
    import numpy as np
    bins = np.logspace(4, 7, 10)
    feats = {
        "comp(1) mono in full F_p": lambda r: r["B1"] == 0,
        "comp(1) mono within log²p": lambda r: r["c1mix1"] == 0,
        "comp(r) mono in full F_p": lambda r: r["Br"] == 0,
        "comp(1),comp(r) both mono (full)": lambda r: r["B1"] == 0 and r["Br"] == 0,
        "H4 > 0.25 log²p": lambda r: r["H4"] > 0.25 * r["L2"],
        "H4 > 0.5 log²p": lambda r: r["H4"] > 0.5 * r["L2"],
    }
    print("\n### I. Trend of failure frequencies (bins geometric in p, 1e4..1e7)")
    print("| feature | frequencies per bin (low→high p) | fitted κ in freq ≈ C (log p)^-κ |")
    print("|---|---|---:|")
    for name, f in feats.items():
        xs, ys, fr = [], [], []
        for lo, hi in zip(bins, bins[1:]):
            S = [r for r in rows if lo < r["p"] <= hi]
            k = sum(f(r) for r in S)
            fr.append(f"{k / len(S):.4f}")
            if k:
                xs.append(np.log(np.mean([math.log(r["p"]) for r in S])))
                ys.append(np.log(k / len(S)))
        kappa = -np.polyfit(xs, ys, 1)[0] if len(xs) > 2 else float("nan")
        print(f"| {name} | {' '.join(fr)} | {kappa:.2f} |")


if __name__ == "__main__" and len(sys.argv) > 1 and sys.argv[-1] == "--trend":
    trend(load(sys.argv[1]))
