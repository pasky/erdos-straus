"""Delta review driver; no lane code imported. Run compiled checker sequentially.
Usage: ulimit -v 6000000; timeout 1800 uv run python scripts/z68_xrev_sign2_check.py /tmp/z68_sign2_graph
The largest graph has <1e6 vertices; only one graph is retained at a time.
"""
import math
import re
import subprocess
import sys

REF = "83d90a3664e4d2cb9e461cb61d2ab56ea797d336"
KEYS = "S1Rmin S1Rminp S2Rmin S2Rminp S2D S3anyRmin S3anyD".split()


def counts(text):
    out = {}
    for line in text.splitlines():
        if " COUNTS " in line:
            row = {k: int(v) for k, v in re.findall(r"(\w+)=(-?\d+)", line)}
            assert row["n"] not in out
            out[row["n"]] = row
    return out


def prime(n):
    return n >= 2 and all(n % d for d in range(2, math.isqrt(n) + 1))


def report(label, rows):
    print(label, "N=", len(rows), {k: sum(r[k] for r in rows) for k in KEYS}, flush=True)


def main():
    texts = [subprocess.check_output(
        ["git", "show", f"{REF}:data/z68/sign/{name}.txt"], text=True)
        for name in ("graph_p1e5", "graph_controls", "graph_sample1e6")]
    full, controls, near = map(counts, texts)
    assert sorted(full) == [p for p in range(17, 100001, 8) if prime(p)]
    report("ALL STORED PRIME ROWS (aggregation, not graph replay)", list(full.values()))
    assert [sum(r[k] for r in full.values()) for k in KEYS] == [987,987,2138,2139,2139,1870,2141]
    sample = set(p for p in full if p <= 1000)
    for lo, hi in [(1000,10000),(10000,30000),(30000,60000),(60000,100000)]:
        band = sorted(p for p in full if lo < p <= hi)
        sample.update(band[round(i*(len(band)-1)/11)] for i in range(12))
        report(f"STORED BAND ({lo},{hi}]", [full[p] for p in band])
    sample.update([1249,2521,8641,14401,20521,21841])
    sample.update(p for p,r in full.items() if r["S2Rmin"] != r["S2Rminp"])
    near_primes = sorted(p for p in near if p > 900000)
    assert len(near_primes) == 30
    assert [p for p in range(near_primes[0],near_primes[-1]+1,8) if prime(p)] == near_primes
    assert sum(near[p]["S3anyD"] for p in near_primes) == 30
    assert sum(near[p]["S3anyRmin"] for p in near_primes) == 28
    sample.update([near_primes[0],near_primes[-1],589681])
    expected = full | controls | near
    sample.update(controls)
    result = subprocess.check_output([sys.argv[1], *map(str, sorted(sample))], text=True, timeout=1700)
    actual = counts(result)
    for n, row in actual.items():
        assert row == expected[n], (n, row, expected[n])
    # Compare traversal components and Dijkstra heights with archived lane records.
    raw = "\n".join(texts)
    checks = {}
    for line in result.splitlines():
        if " CHECK " not in line:
            continue
        r = {k: int(v) for k,v in re.findall(r"(\w+)=(-?\d+)",line)}
        n=r["n"]; checks[n]=r
        lane = re.search(rf"^n={n} giant=([^ ]+) giant\+=([^ ]+)",raw,re.M)
        assert lane
        for k,v in zip(["giant","giantp"],lane.groups()):
            assert abs(r[k]/actual[n]["V"]-float(v)) <= 0.00005001
        lane = re.search(rf"^n={n} V=\d+ E=\d+ comps=(\d+) comps\+=(\d+) L3=(\d+) goodL3=(\d+)",raw,re.M)
        assert tuple(map(int,lane.groups())) == (r["comps"],r["compsp"],r["L3"],r["goodL3"])
        lane = re.search(rf"^n={n} minimax-height.*?E (-?\d+) E\+ (-?\d+).*?E (-?\d+) E\+ (-?\d+)",raw,re.M)
        assert tuple(map(int,lane.groups())) == tuple(r[k] for k in ["h1","h1p","h2","h2p"])
    assert checks[409]["goodL3"]==8 and checks[409]["h2"]==-1
    assert checks[105]["L3"]==0
    assert checks[21841]["size1"]==checks[21841]["giant"]==15104
    assert (checks[21841]["h2"],checks[21841]["h2p"],checks[21841]["end1"])==(6,8,22)
    assert actual[21841]["S3n"]==1014 and actual[21841]["S3D"]==2
    squares = [n for n in controls if math.isqrt(n)**2==n]
    assert len(squares)==36
    assert all(checks[n]["goodL3"]==0 and actual[n]["S1good"]==0 and actual[n]["S2A"]==-1 for n in squares)
    report("INDEPENDENT SUBSAMPLE p<=1e5", [actual[n] for n in sorted(actual) if n in full])
    for lo,hi in [(0,1000),(1000,10000),(10000,30000),(30000,60000),(60000,100000)]:
        report(f"INDEPENDENT BAND ({lo},{hi}]",[actual[n] for n in sorted(actual) if n in full and lo<n<=hi])
    print(result, end="")
    print("PASS",len(actual),"graphs;",len(squares),"squares;",sum(r["moves"] for r in actual.values()),
          "rebuilt generating moves; all exact COUNTS, giant sizes, component counts and minimax heights agree.")


if __name__ == "__main__":
    main()
