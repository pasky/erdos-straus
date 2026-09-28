"""Cross-check scripts/signed_components.cpp against the Python enumerator.

PYTHONPATH=scripts uv run python scripts/signed_components_check.py [NPRIMES]

For sampled primes p<=300000 compare: vertex count, positive count, seed
component size/positives and the full sterile-size histogram with the
independent complete enumerator pointwise_incidence.incidence_solutions.
Then, for every dumped non-seed sterile component, verify each vertex
exactly and re-exhaust the component with the lazy exact BFS
(pointwise_fibres.explore) from its first vertex: it must return STERILE with
the same vertex count.  Finite checks only.
"""
import json, random, subprocess, sys
from collections import Counter
from sympy import primerange
from pointwise_incidence import incidence_solutions
from pointwise_refactor import components, seed
from pointwise_fibres import FibreOracle, explore, checked_vertex

BIN = "/tmp/signed_components"


def build():
    subprocess.run(["g++", "-std=c++17", "-O3", "-fopenmp", "-march=native",
                    "scripts/signed_components.cpp", "-o", BIN], check=True)


def run(p, dump=None, threads=4):
    cmd = [BIN, str(p), "--threads", str(threads)]
    if dump is not None:
        cmd += ["--dump", str(dump)]
    out = subprocess.run(cmd, check=True, capture_output=True, text=True).stdout.splitlines()
    summary = json.loads(out[0])
    comps, cur = [], None
    for line in out[1:]:
        f = line.split()
        if f[0] == "C":
            cur = []
            comps.append(cur)
        else:
            cur.append(tuple(int(v) for v in f[1:]))
    return summary, comps


def python_summary(p):
    V = incidence_solutions(p)
    s = seed(p)
    hist, seedsize, seedpos = Counter(), None, None
    for C in components(V):
        pos = sum(v[0] > 0 for v in C)
        if s in C:
            seedsize, seedpos = len(C), pos
        elif pos == 0:
            hist[len(C)] += 1
    return len(V), sum(v[0] > 0 for v in V), seedsize, seedpos, hist


def check_dumped(p, comps):
    oracle = FibreOracle(p)
    for C in comps:
        for v in C:
            checked_vertex(p, v)
            assert v[0] < 0
        r = explore(oracle, C[0], max_vertices=10**6)
        assert r.status == "STERILE" and r.visited == len(C), (p, r.status, r.visited, len(C))


if __name__ == "__main__":
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 40
    build()
    ps = [p for p in primerange(5, 300000) if p % 4 == 1]
    random.seed(1)
    sample = sorted(set(random.sample(ps, n) + [1009, 10477, 30637, 297049]))
    for p in sample:
        S, comps = run(p, dump=1)
        nV, npos, ss, sp, hist = python_summary(p)
        assert (S["V"], S["pos"], S["seedsize"], S["seedpos"]) == (nV, npos, ss, sp), (p, S)
        assert {int(k): v for k, v in S["sterile_hist"].items()} == dict(hist), p
        assert sorted(len(C) for C in comps) == sorted(hist.elements())
        check_dumped(p, comps)
    print(f"OK: {len(sample)} primes agree with the Python enumerator; dumped sterile components re-exhausted")
