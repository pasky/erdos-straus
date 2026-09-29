"""Parallel driver for formal_closure.Formal (same model; DEPTH3 §6).

uv run python scripts/formal_closure_par.py --seed 1 --B 200 --rounds 6 --jobs 12 [--prune]
Per round prints the statistics of formal_closure.py plus the number of NEW ANCHORS.
Every vertex contains an anchor (positive p-free <= 2t), so once all anchors'
fibres are expanded the closure is stable iff a round yields no new anchor.
"""
from __future__ import annotations

import argparse
import json
from multiprocessing import Pool

from sympy import Poly, ZZ

import formal_closure as fc

G = {}


def init(B, seed, extra):
    G["F"] = fc.Formal(B, seed, extra_small=extra)


def register(F, z):
    for k, e in z[1]:
        if k not in F.primes:
            F.key(Poly(list(k), fc.X, domain=ZZ))


def work(z):
    F = G["F"]
    register(F, z)
    F.aux_keys, F.r_primes, F.flags, F.r_root_budget = set(), set(), [], {}
    out = F.fibre(z)
    return z, [tuple(w) for w in out], (sorted(F.aux_keys), sorted(F.r_primes), F.flags, F.r_root_budget)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--rounds", type=int, default=6)
    ap.add_argument("--B", type=int, default=200)
    ap.add_argument("--seed", type=int, default=1)
    ap.add_argument("--jobs", type=int, default=12)
    ap.add_argument("--prune", action="store_true")
    ap.add_argument("--extra-bound", type=int, default=10**5)
    ap.add_argument("--extra", default=None, help="previous dump: add its small_next primes to the small set")
    ap.add_argument("--dump", default=None, help="write the final formal component (json.gz)")
    a = ap.parse_args()
    extra = []
    if a.extra:
        import gzip as _gz
        prev = json.load(_gz.open(a.extra, "rt"))
        extra = sorted(set(prev.get("extra_small", [])) | {l for l in prev.get("r_primes", []) if l <= a.extra_bound})
    F = fc.Formal(a.B, a.seed, extra_small=extra)
    s0 = F.seed()
    V, done, frontier = {s0}, set(), [s0]
    anchors_prev = set()
    AUX = set()
    RP, FLAGS, RB = set(), [], {}
    with Pool(a.jobs, initializer=init, initargs=(a.B, a.seed, extra)) as pool:
        for rnd in range(1, a.rounds + 1):
            todo = []
            for v in frontier:
                for z in v:
                    if z in done:
                        continue
                    done.add(z)
                    register(F, z)
                    if a.prune and F.kind(z) == "dead":
                        continue
                    todo.append(z)
            new = []
            for z, ws, (aux, rp, fl, rb) in pool.imap_unordered(work, todo, chunksize=4):
                RP.update(rp)
                for l, b in rb.items():
                    RB[l] = RB.get(l, 0) + b
                FLAGS.extend(fl)
                for k in aux:
                    if k not in F.primes:
                        F.key(Poly(list(k), fc.X, domain=ZZ))
                    AUX.add(k)
                for w in ws:
                    for zz in w:
                        register(F, zz)
                    if w not in V:
                        V.add(w)
                        new.append(w)
            for w in new:
                assert any(F.kind(z) == "anchor" for z in w), ("no anchor", w)
                vals = fc.check_vertex(F, w)
                assert not all(x > 0 for x in vals), ("POSITIVE formal vertex", w)
            anchors = set(F.anchors(V))
            st = F.stats(V)
            st.pop("anchor_alphas", None)
            st.update(r_primes=len(RP), flags=len(FLAGS), round=rnd, expanded=len(todo), new=len(new), new_anchors=len(anchors - anchors_prev))
            anchors_prev = anchors
            print(json.dumps(st), flush=True)
            if not new:
                print("STABILIZED", flush=True)
                break
            frontier = new
    if a.dump:
        import gzip
        used = {k for v in V for z in v for k, e in z[1]} | AUX
        state = {"B": a.B, "seed": a.seed, "qt": str(F.qt), "stabilized": not new,
                 "primes": [[list(k), F.primes[k][1]] for k in sorted(used)],
                 "r_primes": sorted(RP), "flags": FLAGS,
                 "r_root_budget": {str(l): b for l, b in RB.items()},
                 "extra_small": sorted(int(l) for l in extra),
                 "small_next": sorted(set(int(l) for l in extra) | set(int(l) for l in RP)),
                 "aux_only": [list(k) for k in sorted(AUX - {k for v in V for z in v for k, e in z[1]})],
                 "vertices": [[[z[0], [[list(k), e] for k, e in z[1]]] for z in v] for v in V]}
        with gzip.open(a.dump, "wt") as fh:
            json.dump(state, fh)


if __name__ == "__main__":
    main()
