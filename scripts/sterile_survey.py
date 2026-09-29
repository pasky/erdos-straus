"""Survey of sterile (positive-free, non-seed) component sizes via signed_components.cpp.

PYTHONPATH=scripts uv run python scripts/sterile_survey.py LO HI [--sample N] [--jobs 16] [--dump S] > out.jsonl

Runs the exact complete enumerator on every prime p=1 mod 4 in [LO,HI)
(or on N random ones), one single-threaded process per prime.  Each JSON
line is the C++ summary; with --dump S the vertices of every sterile
component of size >= S are attached as decimal strings.  Finite evidence.
"""
import argparse, json, random, subprocess, sys
from multiprocessing import Pool
from sympy import isprime, nextprime

BIN = "/tmp/signed_components"  # build: see signed_components.cpp header


def job(args):
    p, dump = args
    cmd = [BIN, str(p), "--threads", "1"]
    if dump:
        cmd += ["--dump", str(dump)]
    out = subprocess.run(cmd, check=True, capture_output=True, text=True).stdout.splitlines()
    S = json.loads(out[0])
    comps = []
    for line in out[1:]:
        f = line.split()
        if f[0] == "C":
            comps.append([])
        else:
            comps[-1].append(f[1:])
    if comps:
        S["dumped"] = comps
    return S


def primes_in(lo, hi):
    p = nextprime(lo - 1)
    while p < hi:
        if p % 4 == 1:
            yield p
        p = nextprime(p)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("lo", type=int)
    ap.add_argument("hi", type=int)
    ap.add_argument("--sample", type=int, default=0)
    ap.add_argument("--jobs", type=int, default=16)
    ap.add_argument("--dump", type=int, default=0)
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--skip", default=None, help="jsonl file of already-done primes")
    a = ap.parse_args()
    if a.sample:
        rng = random.Random(a.seed)
        ps = set()
        while len(ps) < a.sample:
            n = rng.randrange(a.lo, a.hi)
            n -= (n - 1) % 4
            while not isprime(n):
                n += 4
            if n < a.hi:
                ps.add(n)
        ps = sorted(ps)
    else:
        ps = list(primes_in(a.lo, a.hi))
    if a.skip:
        done = {json.loads(l)["p"] for l in open(a.skip)}
        ps = [p for p in ps if p not in done]
    with Pool(a.jobs) as pool:
        for r in pool.imap_unordered(job, [(p, a.dump) for p in ps], chunksize=4):
            print(json.dumps(r), flush=True)
