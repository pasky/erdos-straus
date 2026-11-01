"""Independent NONCRTSMOOTH data audit; run via uv with timeout/ulimit.
Usage: uv run python SCRIPT /tmp/xrev_NONCRTSMOOTH
Requires census_{p24,test,nearsq,s1e7}.csv produced by the independent C++ engine.
"""
import csv
import math
from pathlib import Path
import statistics
import sys

root = Path(sys.argv[1])
data = root / "data/z53/noncrtsmooth"


def rows(path):
    with path.open() as f:
        return [{k: int(v) for k, v in row.items()} for row in csv.DictReader(f)]


sieve = bytearray(b"\1") * 1_000_000
sieve[0:2] = b"\0\0"
for a in range(2, math.isqrt(len(sieve) - 1) + 1):
    if sieve[a]:
        sieve[a*a::a] = b"\0" * ((len(sieve) - 1 - a*a) // a + 1)
expected = [p for p in range(1, len(sieve), 24) if sieve[p]]
assert [r["n"] for r in rows(root / "census_p24.csv")] == expected
print(f"Independent prime sieve: complete {len(expected)}-prime p24 census")

for name in ("p24", "test", "nearsq", "s1e7"):
    actual = rows(root / f"census_{name}.csv")
    assert actual == rows(data / f"lot_{name}.csv")
    pos = [r for r in actual if r["R"]]
    no_prime = [r["n"] for r in pos if not r["Rp"]]
    print(name, "rows", len(actual), "R=0", len(actual)-len(pos),
          "no-prime", len(no_prime), "max", max(no_prime, default=0),
          "no-both-prime", sum(not r["Rbp"] for r in pos),
          "no-both-smooth", sum(not r["Rs25"] for r in pos)/len(pos),
          "bestPM/log", statistics.mean(r["bestPM"]/math.log(r["n"]) for r in actual),
          "bestM<=6", statistics.mean(1 <= r["bestM"] <= 6 for r in actual),
          "PM2-empty", statistics.mean(not r["PM2"] for r in actual))
    if name == "p24":
        by_n = {r["n"]: r for r in actual}
        seen = []
        for path in sorted((data / "v2").glob("p24_*.csv")):
            for row in rows(path):
                assert all(by_n[row["n"]][k] == v for k, v in row.items())
                seen.append(row["n"])
        assert sorted(seen) == expected
        print("Engine 2 archival coverage: complete, no duplicates or mismatches")

# Recompute fixed-q counts by solving for B, without integer factorisation.
fixed = rows(data / "fixedq.csv")
for row in fixed:
    p, q = row["p"], row["q"]
    counts = []
    for j in range(1, q + 1):
        count = 0
        for u in range(1, math.isqrt(j*p // (q-2)) + 1):
            B, rem = divmod(j*p+u, q*u-1)
            if rem == 0 and B >= u:
                count += 1 if B == u else 2
        counts.append(count)
    jmin = next(j for j, count in enumerate(counts, 1) if count)
    assert (jmin, sum(counts[:q//4]), sum(counts)) == (row["jmin"], row["N_q4"], row["N_q"])
    x, y = q-1, q*pow(q-1, -1, p)-1
    k, rem = divmod(x*y-1, q*p)
    assert rem == 0 and 1 <= k <= q-2 and jmin <= q-2 and row["trivial_ok"] == 1
print(f"Independent fixed-q enumeration: all {len(fixed)} rows exact")
for q in sorted({r["q"] for r in fixed}):
    near = [r for r in fixed if r["q"] == q and 10**6 < r["p"] < 2*10**6]
    print("q", q, "near primes", len(near), "mean k/q", statistics.mean(r["jmin"]/q for r in near))

# Finite demonstration of the analytical counterexample when the q range is omitted.
ps = [p for p in range(3, 101) if sieve[p]]
Q = 2 + 2*math.prod(ps)
assert Q % 4 == 0
for p in ps:
    k = (Q-2)//p
    assert (Q-1)**2 == 1 + k*Q*p
print("Unrestricted-q counterexample: q=2+2*product(odd primes<=100), x=y=q-1")
