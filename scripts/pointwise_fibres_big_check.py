"""Checks for pointwise_fibres_big (finite, exact comparisons).

PYTHONPATH=scripts uv run --with python-flint python scripts/pointwise_fibres_big_check.py

1. Every denominator bucket of the complete graph (pointwise_incidence) at
   several p equals BigFibreOracle.fibre, both with the C interval scan and
   with the scan disabled (forcing the pruned Type I divisor method).
2. Components: for primes up to ~2e6 the lazy BFS from each vertex of every
   sterile component found by the complete C++ enumerator exhausts exactly
   that component (same vertex count), and FOUND from a positive-containing one.
"""
import json, random, subprocess
from pointwise_incidence import incidence_solutions
from pointwise_refactor import denominator_buckets, components
from pointwise_fibres import explore
from pointwise_fibres_big import BigFibreOracle

for p in (13, 73, 97, 1009, 6089, 10477, 30637, 297049):
    V = incidence_solutions(p)
    B = denominator_buckets(V)
    for sb in (300_000_000, 1):
        O = BigFibreOracle(p, scan_budget=sb)
        for z, idx in B.items():
            assert O.fibre(z) == {V[i] for i in idx}, (p, z, sb)
    # unused labels near the hubs are empty
    O = BigFibreOracle(p, scan_budget=1)
    t = (p - 1) // 4
    for h in range(-30, 31):
        z = p * (p * h - t)
        assert O.fibre(z) == {V[i] for i in B.get(z, [])}
print("bucket equality OK")

subprocess.run(["g++", "-std=c++17", "-O3", "-fopenmp", "-march=native",
                "scripts/signed_components.cpp", "-o", "/tmp/signed_components_chk"], check=True)
random.seed(2)
for p in (30637, 663557, 1094629, 1999957):
    out = subprocess.run(["/tmp/signed_components_chk", str(p), "--threads", "4", "--dump", "4"],
                         capture_output=True, text=True, check=True).stdout.splitlines()
    comps = []
    for line in out[1:]:
        f = line.split()
        if f[0] == "C":
            comps.append([])
        else:
            comps[-1].append(tuple(map(int, f[1:])))
    O = BigFibreOracle(p, scan_budget=1)
    for C in comps:
        r = explore(O, random.choice(C), max_vertices=10**5)
        assert r.status == "STERILE" and r.visited == len(C), (p, len(C), r.status, r.visited)
    print(p, "sterile comps re-exhausted:", sorted(len(C) for C in comps))
print("OK")
