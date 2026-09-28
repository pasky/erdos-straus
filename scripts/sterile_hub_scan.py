"""Natural sterile hubs at random large p (exact lazy search; finite evidence).

PYTHONPATH=scripts uv run --with python-flint python scripts/sterile_hub_scan.py LO HI N [--K 200] [--jobs 16]

For N random primes p=1 mod 4 in [LO,HI), start the exact lazy BFS
(pointwise_fibres_big) from every vertex-bearing negative-quadrant hub:
anchors x=t-k (1<=k<=K) and Type I buckets h=-c (1<=c<=K).  Report, per p,
the largest component found STERILE (fully exhausted) and its hub.  Since
large sterile components for random p are hub-dominated (SIZE_CONJECTURE.md
§2), this estimates the natural max sterile size far beyond 2^31, but it is a
lower bound for the true maximum, not a complete census.
"""
import argparse, json, random, signal, time
from multiprocessing import Pool

import flint

from pointwise_fibres import IncompleteSearch, explore
from pointwise_fibres_big import BigFibreOracle


class Timeout(Exception):
    pass


def _alarm(*_):
    raise Timeout()


def job(args):
    p, K, timeout, maxv = args
    signal.signal(signal.SIGALRM, _alarm)
    signal.alarm(timeout)
    t = (p - 1) // 4
    O = BigFibreOracle(p)
    best, found, sterile, unknown, done_starts = None, 0, 0, 0, set()
    t0 = time.time()
    try:
        hubs = [("a", -k, t - k) for k in range(1, K + 1)] + [("h", -c, p * (p * -c - t)) for c in range(1, K + 1)]
        for kind, val, z in hubs:
            try:
                F = O.fibre(z)
                if not F:
                    continue
                v0 = min(F)
                if v0 in done_starts:
                    continue
                r = explore(O, v0, max_vertices=maxv)
            except IncompleteSearch:
                unknown += 1
                continue
            if r.status == "STERILE":
                sterile += 1
                if best is None or r.visited > best[0]:
                    best = (r.visited, kind, val)
            else:
                found += 1
    except Timeout:
        unknown += 1
    finally:
        signal.alarm(0)
    return dict(p=p, best=best, sterile_hubs=sterile, exiting_hubs=found, unknown=unknown,
                secs=round(time.time() - t0, 1))


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("lo", type=int)
    ap.add_argument("hi", type=int)
    ap.add_argument("n", type=int)
    ap.add_argument("--K", type=int, default=200)
    ap.add_argument("--jobs", type=int, default=16)
    ap.add_argument("--timeout", type=int, default=3600)
    ap.add_argument("--maxv", type=int, default=200000)
    ap.add_argument("--seed", type=int, default=1)
    ap.add_argument("--from-file", default=None, help="take primes from a sterile_survey jsonl (validation)")
    a = ap.parse_args()
    rng = random.Random(a.seed)
    ps = set()
    if a.from_file:
        ps = {json.loads(l)["p"] for l in open(a.from_file)}
        ps = set(sorted(ps)[: a.n])
    while len(ps) < a.n:
        q = rng.randrange(a.lo, a.hi) | 1
        q -= (q - 1) % 4
        while flint.fmpz(q).is_prime() != 1:
            q += 4
        ps.add(q)
    with Pool(a.jobs) as pool:
        for r in pool.imap_unordered(job, [(p, a.K, a.timeout, a.maxv) for p in sorted(ps)]):
            print(json.dumps(r), flush=True)
