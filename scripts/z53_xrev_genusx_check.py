"""Independent GENUSX audit; no third-party dependencies.
Run with a bounded shell, e.g. ulimit -v 2097152; ulimit -t 300;
timeout 280s uv run --no-project scripts/z53_xrev_genusx_check.py /tmp/xrev_GENUSX
The extracted memo engine must be compiled as ROOT/engine first. Child processes
inherit the memory/CPU limits and each has a wall-clock timeout. Arrays are at
most O(54000) for the independent density check; engine E uses O(sqrt(n)+U1).
"""
import csv
import math
import statistics as st
import subprocess
import sys
from collections import defaultdict
from pathlib import Path

root = Path(sys.argv[1])
data = root / "data/z53/genusx"


def load(name):
    with (data / name).open() as stream:
        first = stream.readline()
        stream.seek(0)
        if first.startswith("tag\t"):
            return list(csv.DictReader(stream, delimiter="\t"))
        # random.tsv is headerless and uses the original, pre-ladder schema.
        fields = "tag n logn R G E1 C4 CU0 CBM REST Mhat Mdirect Mcls shell hits l2bad fullbad U0 U1 Y X".split()
        return [row for row in csv.DictReader(stream, fieldnames=fields, delimiter="\t") if row["tag"] != "tag"]


def num(row, key):
    return float(row[key])


def engine(row, mode="E"):
    args = [str(root / "engine"), mode] + [row[k] for k in ("n", "U0", "U1", "Y", "X")]
    result = subprocess.run(args, capture_output=True, text=True, check=True, timeout=100)
    return dict(item.split("=") for item in result.stdout.split())


# Recompute statistics independently, without importing the original statistics code.
groups = defaultdict(list)
allrows = []
for name in ("random_small.tsv", "random.tsv", "nearsq.tsv", "controls.tsv", "hard.tsv",
             "validate_direct.tsv", "validate_direct_1e10.tsv"):
    rows = load(name)
    allrows.extend(rows)
    if name in ("random_small.tsv", "random.tsv", "nearsq.tsv"):
        for row in rows:
            groups[row["tag"]].append(row)
for tag, rows in groups.items():
    R, G, M = ([num(row, key) for row in rows] for key in ("R", "G", "Mhat"))
    v = st.pvariance([r - m for r, m in zip(R, M)])
    vg = st.pvariance([g - m for g, m in zip(G, M)])
    vrg = st.pvariance([r - g for r, g in zip(R, G)])
    print(tag, "N", len(rows), "G/M", round(st.mean(g/m for g, m in zip(G, M)), 6),
          "variance shares", round(vg/v, 6), round(vrg/v, 6),
          "swap-Poisson", round(vrg/(2*st.mean(G)), 6),
          "zero excess", round(st.mean(r == 0 for r in R)/st.mean(math.exp(-m/2) for m in M), 6),
          flush=True)
print("saved records", len(allrows), "shell", sum(int(r["shell"]) for r in allrows), flush=True)

# Rerun every saved E-mode row, deduplicating identical windows only.
unique = {tuple(row[k] for k in ("n", "U0", "U1", "Y", "X")): row for row in allrows}
for row in unique.values():
    got = engine(row)
    for key in ("R", "G", "E1", "C4", "CU0", "CBM", "REST", "G4", "G6", "G12", "G120", "shell", "hits"):
        if key not in row:
            continue
        assert abs(float(got[key]) - num(row, key)) < 1.1e-6, (row["n"], key, got[key], row[key])
    assert got["lemma2_bad"] == got["fullbad"] == "0"
    assert row["l2bad"] == row["fullbad"] == "0"
print("engine reruns passed", len(unique), flush=True)

squares = [r for r in allrows if math.isqrt(int(r["n"]))**2 == int(r["n"])]
for row in squares:
    assert num(row, "R") == num(row, "G") == 0
    assert abs(num(row, "E1") + num(row, "CBM")) < 1.1e-6
    assert abs(num(row, "C4") + num(row, "CU0")) < 1.1e-6
print("square records", len(squares), "shell", sum(int(r["shell"]) for r in squares),
      "mean E1/log²n", st.mean(num(r, "E1")/math.log(int(r["n"]))**2 for r in squares), flush=True)
square = next(r for r in squares if r["n"] == "100020001")
square_direct = engine(square, "D")
assert float(square_direct["M"]) == float(square_direct["Mcls"]) == 0
print("square direct M=Mcls=0", square["n"], flush=True)

# Repeat all saved direct-density runs, including the square, not the expensive class-number driver.
for row in allrows:
    if math.isfinite(num(row, "Mdirect")):
        got = engine(row, "D")
        assert abs(float(got["M"]) - num(row, "Mdirect")) < 1.1e-6
        assert abs(float(got["Mcls"]) - num(row, "Mcls")) < 1.1e-6
        print("direct", row["n"], "M", got["M"], "Mcls", got["Mcls"], flush=True)

# Independent density/count implementation: enumerate all pairs, testing pa as a
# unit square modulo 8 and every odd prime, rather than using the level-divisor formulas.
row = next(r for r in allrows if r["n"] == "100000049" and math.isfinite(num(r, "Mdirect")))
n, u0, u1, y, x = (int(row[k]) for k in ("n", "U0", "U1", "Y", "X"))
spf = list(range(x + 1))
for prime in range(2, math.isqrt(x) + 1):
    if spf[prime] == prime:
        for j in range(prime*prime, x+1, prime):
            if spf[j] == j:
                spf[j] = prime


def squarefree_factors(value):
    factors = []
    while value > 1:
        prime = spf[value]
        value //= prime
        if value % prime == 0:
            return None
        factors.append(prime)
    return factors


ws = []
for w in range(y + 1, x + 1):
    if w % 2 == 0 or math.gcd(w, n) != 1:
        continue
    factors = squarefree_factors(w)
    if factors is not None:
        ws.append((w, factors, 2**len(factors)/math.prod(prime-1 for prime in factors)))
M, MC, GG = [], [], []
RR = 0
for u in range(u0 + 1, u1 + 1):
    if u % 4 != 1 or math.gcd(u, n) != 1:
        continue
    up = squarefree_factors(u)
    if up is None:
        continue
    gu = 2**len(up)/math.prod(prime-1 for prime in up)
    for w, wp, rho in ws:
        if math.gcd(u, w) != 1:
            continue
        a = -(u+2*w)
        pa = n*a
        agen = pa % 8 == 1 and all(pow(pa % prime, (prime-1)//2, prime) == 1 for prime in up)
        bgen = all(pow(pa % prime, (prime-1)//2, prime) == 1 for prime in wp)
        ac = (n-a) % (8*u) == 0
        bc = (n-a) % w == 0
        RR += 2*int(ac and bc)
        if agen and bc:
            GG.append(2*gu)
        if bgen:
            if agen:
                M.append(2*gu*rho)
            if ac:
                MC.append(2*rho)
assert RR == int(float(row["R"]))
for value, key in ((math.fsum(GG), "G"), (math.fsum(M), "Mdirect"), (math.fsum(MC), "Mcls")):
    assert abs(value-num(row, key)) < 1e-6, (key, value, row[key])
print("independent raw CRT", n, "R", RR, "G", math.fsum(GG), "M", math.fsum(M), "Mcls", math.fsum(MC), flush=True)

hard = [r for r in load("hard.tsv") if r["tag"] == "STARZERO" and num(r, "Mhat") > 0.5]
print("informative STARZERO", len(hard), "G/M>=0.84", sum(num(r, "G")/num(r, "Mhat") >= .84 for r in hard),
      "ratios", [(r["n"], round(num(r, "G")/num(r, "Mhat"), 9)) for r in hard], flush=True)
for name in ("ladder_small.tsv", "ladder_large.tsv"):
    laddergroups = defaultdict(list)
    for r in load(name):
        laddergroups[r["tag"]].append(r)
    for tag, rows in laddergroups.items():
        base = st.pvariance(num(r, "R")-num(r, "Mhat") for r in rows)
        shares = [st.pvariance(num(r, key)-num(r, "Mhat") for r in rows)/base for key in ("G", "G4", "G6", "G12", "G120")]
        print("ladder", tag, [round(v, 6) for v in shares], flush=True)
print("PASS", flush=True)
