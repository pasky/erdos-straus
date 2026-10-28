"""z48 forestconn: build the adversarial prime list for list mode (primes > 10^7 mainly)."""
import csv, gzip, math
from sympy import isprime, nextprime

rows = []
for fn in ("data/z46_forest_h4/census.csv.gz", "data/z46_forest_h4/qnr.csv.gz", "data/z46_forest_h4/hunt.csv.gz"):
    with gzip.open(fn, "rt") as f:
        for r in csv.DictReader(f):
            if r["H"]:
                rows.append((r["family"], int(r["p"]), int(r["H"]), int(r["r"])))
seen = set()
out = []
def add(tag, p):
    if p in seen or p % 24 != 1 or not isprime(p):
        return
    seen.add(p); out.append((tag, p))
big = [r for r in rows if r[1] > 10**7]
for fam, p, H, r in sorted(big, key=lambda x: -x[2] / math.log(x[1]) ** 2)[:60]:
    add("topH4ratio", p)
for fam, p, H, r in sorted(big, key=lambda x: -x[3])[:60]:
    add("larger", p)
for fam, p, H, r in sorted(big, key=lambda x: -x[2] / x[3])[:30]:
    add("topH4overr", p)
for p in (25862761, 837476641, 109878088321, 3667646782801, 1002125860849, 130679098667329, 641335046555449):
    add("named", p)
# near-squares p = m^2 + k, p == 1 mod 24; 40 primes per (scale, k)
for scale in (10**8, 10**10, 10**12, 10**14):
    m0 = math.isqrt(scale)
    for k in (1, -3, -8, 24, -24, 48, -48):
        got = 0; m = m0
        while got < 40:
            p = m * m + k
            if p % 24 == 1 and isprime(p):
                add(f"nsq{k:+d}", p); got += 1
            m += 1
# consecutive samples
for scale in (10**9, 10**12):
    p = scale; got = 0
    while got < 3000:
        p = nextprime(p)
        if p % 24 == 1:
            add(f"consec{int(math.log10(scale))}", p); got += 1
for tag, p in out:
    print(tag, p)
