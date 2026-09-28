"""Validate the depth<=3 classification (scripts/depth3.py) against a brute layered BFS.

uv run python scripts/depth3_validate.py LO HI [--step K] [--jobs N]

For each prime p=1 mod 4 in [LO,HI] (every K-th one), compute with the exact
FibreOracle of pointwise_fibres.py:
  L1 = seed neighbours, L2 = nonpositive neighbours of L1 outside L1+seed,
  X1 = members of L1 having a positive neighbour,
  X2 = members of L2 having a positive neighbour,
and compare with the families (9), (A), (B) of depth3.py, which must produce
exactly X1 (via h) and exactly X2 (as the middle vertices of A/B paths).
Also checks the structural lemmas: L1 is nonpositive, L2 members off the
(A)/(B) shapes have no positive neighbour.
"""
from __future__ import annotations

import argparse
import json
import sys
from multiprocessing import Pool

from sympy import primerange

from depth3 import Depth3
from pointwise_fibres import FibreOracle
from pointwise_refactor import seed


def brute(p):
    O = FibreOracle(p, max_divisors=10**7, max_fibre=10**7)
    t = (p - 1) // 4
    S = tuple(seed(p))
    L1 = set(O.fibre(t)) - {S}
    assert all(v[0] < 0 for v in L1)
    pos = lambda z: {w for w in O.fibre(z) if w[0] > 0}
    Pos2 = set().union(*[pos(z) for v in L1 for z in v])
    L2 = set()
    for v in L1:
        for z in v:
            if z == t:
                continue
            for w in O.fibre(z):
                if w[0] < 0 and w not in L1 and w != S:
                    L2.add(w)
    Pos3 = set().union(*[pos(z) for v in L2 for z in v]) - Pos2
    return O, Pos2, Pos3, len(L1), len(L2)


def check(p):
    O, Pos2, Pos3, n1, n2 = brute(p)
    pos = lambda z: {w for w in O.fibre(z) if w[0] > 0}
    D = Depth3(p)
    r9 = D.crit9(all_hits=True)
    rA = D.famA(all_hits=True)
    rB = D.famB(all_hits=True)
    # family sets, using the oracle for the final fibres
    t = D.t
    F2 = set()
    for h in D.T2:
        F2 |= pos(p * (p * h - t))
    F3 = set()
    mids = [tuple(hh["path"][1]) for hh in rA + rB]
    # recompute all A/B middles independent of productivity
    allmid = set()
    for c in D.T2:
        M = p * c + t
        for d in __import__("depth3").sq_divisors(D.F(M)):
            if (d + c) % (4 * c + 1) == 0:
                a = (d + c) // (4 * c + 1)
                if (t + a) % p:
                    allmid.add(tuple(sorted((t + a, -p * M, (t + a) * M // d))))
    for dd in D.T2:
        for delta in (dd, -dd):
            if delta in (t, -t):
                continue
            V1 = tuple(sorted((t, p * (delta - t), p * (t * t // delta - t))))
            for mm in (delta - t, t * t // delta - t):
                for V2 in D.type2_fibre(mm):
                    if V2 != V1:
                        allmid.add(V2)
    for V2 in allmid:
        for z in V2:
            F3 |= pos(z)
    F3 -= Pos2
    prodok = all(bool(D.productive(z)) == bool(pos(z)) for V2 in allmid for z in V2 if z > 0 and z % p)
    fastok = (bool(r9) == bool(Pos2)) and (bool(rA or rB) == bool(Pos3))
    ok = (F2 == Pos2) and (F3 == Pos3) and prodok and fastok
    return {"p": p, "ok": ok, "L1": n1, "L2": n2, "Pos2": len(Pos2), "Pos3": len(Pos3),
            "A": len(rA), "B": len(rB), "prodok": prodok, "fastok": fastok,
            "diff": [sorted(map(str, F2 ^ Pos2)), sorted(map(str, F3 ^ Pos3))] if not ok else None}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("lo", type=int)
    ap.add_argument("hi", type=int)
    ap.add_argument("--step", type=int, default=1)
    ap.add_argument("--jobs", type=int, default=8)
    a = ap.parse_args()
    ps = [q for q in primerange(max(a.lo, 13), a.hi) if q % 4 == 1][:: a.step]
    bad = 0
    tot = {"A": 0, "B": 0, "d3": 0}
    with Pool(a.jobs) as pool:
        for r in pool.imap_unordered(check, ps, chunksize=2):
            tot["A"] += r["A"] > 0
            tot["B"] += r["B"] > 0
            tot["d3"] += r["Pos2"] == 0
            if not r["ok"]:
                bad += 1
                print(json.dumps(r), flush=True)
    print("checked", len(ps), "mismatches", bad, "primes with A-hits", tot["A"], "with B-hits", tot["B"], "dist>2:", tot["d3"])


if __name__ == "__main__":
    main()
