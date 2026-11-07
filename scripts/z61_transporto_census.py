#!/usr/bin/env python3
"""z61 TRANSPORTO census: rule R1 on the mandatory falsifier sets. Writes data/z61/transporto/r1_census.jsonl.

Sets: SQ odd squares 9..2025 + 97^2, 101^2, 113^2; Z7 (8 composite U7-zeros); RC first 60 R-zero composites
(data/z58/screens/composite_zeros_le8e6.txt); P all odd primes <= PMAX; STAR, GSTAR (<=1e7), AHALF (U7 A-half
zero primes), LATE prime 2031121; U8 (hitset restricted to U^(8) targets) at the U^(8)-zero primes <= 2e5.
"""
import sys, json, os, time
sys.path.insert(0, os.path.dirname(__file__))
from z61_transporto_r1 import spf_sieve, ledger

ROOT = os.path.join(os.path.dirname(__file__), "..")
OUT = os.path.join(ROOT, "data/z61/transporto/r1_census.jsonl")
PMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 20000

def read_nums(path, maxn=None, col=0, tag=None):
    out = []
    for line in open(os.path.join(ROOT, path)):
        if line.startswith("#") or not line.strip():
            continue
        t = line.split()
        if tag is not None and t[0] != tag:
            continue
        v = int(t[col])
        if maxn is None or v <= maxn:
            out.append(v)
    return out

def primes_upto(N, spf):
    return [p for p in range(3, N + 1, 2) if spf[p] == p]

def main():
    sets = {}
    sets["SQ"] = [m * m for m in range(3, 46, 2)] + [97 ** 2, 101 ** 2, 113 ** 2]
    sets["Z7"] = [105, 1465, 3865, 4545, 10305, 12145, 39361, 67425]
    sets["RC"] = read_nums("data/z58/screens/composite_zeros_le8e6.txt")[:60]
    sets["STAR"] = read_nums("data/z58/screens/star_prime_zeros.txt")
    sets["GSTAR"] = read_nums("data/z58/screens/gstar_zeros.txt", maxn=10 ** 7)
    sets["AHALF"] = read_nums("data/z60/lopez/u7half_tgt2_primes_1e8.txt", col=1, tag="ZERO")
    sets["LATE"] = [2031121]
    u8 = read_nums("data/z59/conv2/union_K8_primes_1e8.txt", col=1, tag="ZERO", maxn=200000)
    big = max(max(v) for v in sets.values())
    spf = spf_sieve(2 * big + 2)
    sets["P"] = primes_upto(PMAX, spf)
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    t0 = time.time()
    with open(OUT, "w") as fo:
        for name, ns in sets.items():
            for n in ns:
                r = ledger(n, spf, "u7")
                r["set"] = name
                fo.write(json.dumps(r) + "\n")
        for n in u8:
            r = ledger(n, spf, "u8")
            r["set"] = "U8"
            fo.write(json.dumps(r) + "\n")
    print("done", round(time.time() - t0, 1), "s", file=sys.stderr)

if __name__ == "__main__":
    main()
