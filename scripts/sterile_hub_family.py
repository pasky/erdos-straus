"""Adversarial 'dead hub' family for the size conjecture (finite, certified checks).

PYTHONPATH=scripts uv run --with python-flint python scripts/sterile_hub_family.py \
    --k 2 --r 7 --count 40 --pmin 19 --pool 40 --jobs 16 > out.jsonl

Construction: M=4k+1; x = product of r distinct primes q = 1 (mod M) drawn
at random from the first `pool` such primes >= pmin (optionally with
exponents); p = 4(x+k)+1 must be prime, and k must not divide t^2 (else x
lies in the -pt hub fibre of the seed).  Then the fibre of x consists of
exactly (tau(x^2)-1)/2 nonpositive Type II vertices (SIZE_CONJECTURE.md,
Lemma B).  For each such p we run the exact lazy BFS of
pointwise_fibres_big from the hub fibre: STERILE means the entire component
was exhausted and has no positive vertex.  Each JSON line records the verdict.
"""
import argparse, json, math, random, signal, sys, time
from multiprocessing import Pool

import flint
from sympy import primerange

from pointwise_fibres import IncompleteSearch
from pointwise_fibres_big import hub_component


class Timeout(Exception):
    pass


def _alarm(*_):
    raise Timeout()


def job(args):
    p, x, k, qs, timeout, maxv, seedsize = args
    signal.signal(signal.SIGALRM, _alarm)
    signal.alarm(timeout)
    t0 = time.time()
    out = dict(p=p, x=x, k=k, primes=qs, tau=math.prod(2 * e + 1 for e in qs.values()))
    try:
        r = hub_component(p, x, max_vertices=maxv)
        out.update(status=r["status"], visited=r.get("visited"), hubfibre=r.get("hubfibre"),
                   pathlen=(len(r["path"]) - 1) if r.get("path") else None)
        if seedsize and out["status"] == "STERILE":
            from pointwise_fibres_big import BigFibreOracle, exhaust_component
            from pointwise_refactor import seed
            S, pos = exhaust_component(BigFibreOracle(p), seed(p))
            out.update(seedcomp=len(S), seedpos=pos)
    except IncompleteSearch as e:
        out.update(status=out.get("status", "UNKNOWN"), reason=str(e))
    except Timeout:
        out.update(status="TIMEOUT")
    finally:
        signal.alarm(0)
    out["secs"] = round(time.time() - t0, 1)
    return out


def candidates(k, r, count, pmin, pool, expmax, rng, pmax, guard=0, mod4=0, tprime=False):
    M = 4 * k + 1
    Q = [q for q in primerange(pmin, 10**6) if q % M == 1 and (not mod4 or q % 4 == mod4)][:pool]
    G = [q for q in primerange(guard, 2 * guard) if q % M == 1 and q % 4 == 3] if guard else []
    seen, out, tries = set(), [], 0
    while len(out) < count and tries < 10**6:
        tries += 1
        qs = sorted(rng.sample(Q, r))
        exps = {q: rng.randint(1, expmax) for q in qs}
        if G:
            exps[rng.choice(G)] = 1
        x = math.prod(q**e for q, e in exps.items())
        t = x + k
        p = 4 * t + 1
        if x in seen or p >= pmax or (t * t) % k == 0 or flint.fmpz(p).is_prime() != 1:
            continue
        if tprime and math.prod(2 * int(e) + 1 for _, e in flint.fmpz(t).factor()) > tprime:
            continue
        seen.add(x)
        out.append((p, x, k, exps))
    return out


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--k", type=int, default=2)
    ap.add_argument("--r", type=int, default=5)
    ap.add_argument("--count", type=int, default=20)
    ap.add_argument("--pmin", type=int, default=3)
    ap.add_argument("--pool", type=int, default=30)
    ap.add_argument("--expmax", type=int, default=1)
    ap.add_argument("--pmax", type=int, default=2**61)
    ap.add_argument("--guard", type=int, default=0,
                    help="add one prime q0=1 mod M, 3 mod 4 in [G,2G) (use with --mod4 1): "
                         "then every descent divisor d=x/w, w|x, w=1 mod 4, has d>=q0")
    ap.add_argument("--mod4", type=int, default=0)
    ap.add_argument("--tprime", type=int, default=0, help="require tau(t^2) <= this (sparse seed hubs)")
    ap.add_argument("--seedsize", action="store_true", help="also exhaust the seed component")
    ap.add_argument("--jobs", type=int, default=16)
    ap.add_argument("--timeout", type=int, default=1800)
    ap.add_argument("--maxv", type=int, default=10**6)
    ap.add_argument("--seed", type=int, default=0)
    a = ap.parse_args()
    rng = random.Random(a.seed)
    C = candidates(a.k, a.r, a.count, a.pmin, a.pool, a.expmax, rng, a.pmax, a.guard, a.mod4, a.tprime)
    with Pool(a.jobs) as pool:
        for res in pool.imap_unordered(job, [(p, x, k, e, a.timeout, a.maxv, a.seedsize) for p, x, k, e in C]):
            res["primes"] = {str(q): e for q, e in res["primes"].items()}
            print(json.dumps(res), flush=True)
