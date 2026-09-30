"""How close do actual seed components come to the formal one? (FORMAL_CLOSURE.md §5, EVIDENCE)

uv run --with python-flint python scripts/formal2_realq.py LAMFILE DUMP.json.gz [--mod-bound 13] [--n 5]
    [--lo 1e9] [--hi 1e11] [--depth 6]

Choose actual primes q with p=24q+1 prime and q = qt (the certificate's model point) modulo
2^a 3^b 5^c ... (all primes <= mod-bound, powers ell^k with ell^k <= 10^4 roughly).  Evaluate
every formal vertex at q; the integral ones form F(q) (genuine vertices of the graph of p).
Run an exact layered BFS from the seed (scripts/pointwise_fibres.py oracle) and report,
per layer, how many actual vertices lie in F(q), the first positive vertex, and for the
escape path which vertices are formal and which g in S have a composite value r_g(q) at the
shared denominator where the path leaves F(q).
"""
from __future__ import annotations

import argparse
import gzip
import json
import random
import sys
from fractions import Fraction
from math import prod

sys.set_int_max_str_digits(0)
sys.path.insert(0, __file__.rsplit("/", 1)[0])
import formal2  # noqa: E402
from pointwise_fibres import FibreOracle, IncompleteSearch  # noqa: E402
from pointwise_refactor import seed  # noqa: E402
from sympy import isprime, primerange  # noqa: E402


def ev(key, q):
    return sum(a * q**i for i, a in enumerate(key))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("lamfile")
    ap.add_argument("dump")
    ap.add_argument("--mod-bound", type=int, default=13)
    ap.add_argument("--n", type=int, default=5)
    ap.add_argument("--lo", type=float, default=1e9)
    ap.add_argument("--hi", type=float, default=1e11)
    ap.add_argument("--depth", type=int, default=5)
    ap.add_argument("--seed", type=int, default=7)
    ap.add_argument("--budget", type=int, default=200000)
    ap.add_argument("--power-cap", type=int, default=100)
    ap.add_argument("--only-deep", action="store_true", help="print only q with no positive vertex at distance <=2")
    a = ap.parse_args()
    LF = json.load(open(a.lamfile))
    st = json.load(gzip.open(a.dump, "rt"))
    res = {int(l): tuple(v) for l, v in LF["residues"].items()}
    qt = formal2.build_qt(res, LF.get("seed", 1))
    C = {tuple(k): c for k, c, _, _ in st["S"]}
    V = [[(z[0], [(tuple(k), e) for k, e in z[1]]) for z in v] for v in st["vertices"]]
    mods = []
    for ell in primerange(2, a.mod_bound + 1):
        k = 1
        while ell ** (k + 1) <= a.power_cap:
            k += 1
        mods.append(ell**k)
    Mq = prod(mods)
    rng = random.Random(a.seed)
    out = []
    tries = 0
    while len(out) < a.n and tries < 10**7:
        tries += 1
        q = qt % Mq + Mq * rng.randrange(int(a.lo) // Mq + 1, int(a.hi) // Mq + 1)
        if not (isprime(q) and isprime(24 * q + 1)):
            continue
        p = 24 * q + 1
        # formal vertices integral at q
        gval = {}

        def val(z):
            c, ex = z
            x = Fraction(c)
            for k, e in ex:
                if k not in gval:
                    gval[k] = Fraction(ev(k, q), C[k])
                x *= gval[k] ** e
            return x

        Fq = {}
        for v in V:
            vals = [val(z) for z in v]
            if all(x.denominator == 1 and x != 0 for x in vals):
                Fq[tuple(sorted(int(x) for x in vals))] = v
        O = FibreOracle(p, max_divisors=10**6, max_fibre=10**6, factor_limit=10**6)
        root = tuple(sorted(seed(p)))
        prev = {root: None}
        layer = [root]
        rows = []
        first_pos = None
        status = "ok"
        try:
            for d in range(1, a.depth + 1):
                nxt = []
                for vtx in layer:
                    for z in set(vtx):
                        for w in O.fibre(z):
                            if w not in prev:
                                prev[w] = (vtx, z)
                                nxt.append(w)
                                if len(prev) > a.budget:
                                    raise IncompleteSearch("budget")
                pos = [w for w in nxt if w[0] > 0]
                rows.append({"d": d, "size": len(nxt), "in_F": sum(1 for w in nxt if w in Fq),
                             "nonpos_not_in_F": sum(1 for w in nxt if w not in Fq and w[0] < 0),
                             "positive": len(pos)})
                if pos and first_pos is None:
                    first_pos = pos[0]
                    break
                layer = nxt
        except IncompleteSearch as e:
            status = "incomplete:" + str(e)
        info = {"q": q, "p": p, "formal_integral_at_q": len(Fq), "layers": rows, "status": status}
        if first_pos is not None:
            path, w = [], first_pos
            while w is not None:
                path.append(w)
                w = prev[w][0] if prev[w] else None
            path = path[::-1]
            info["escape_path_in_F"] = [x in Fq for x in path]
            # where the path leaves F(q): the shared denominator and its composite r_g(q)
            for i in range(1, len(path)):
                if path[i] not in Fq and path[i - 1] in Fq:
                    zval = prev[path[i]][1]
                    fv = Fq[path[i - 1]]
                    for zf in fv:
                        if val(zf) == zval:
                            comp = []
                            for k, e in zf[1]:
                                rg = Fraction(ev(k, q), C[k])
                                if rg.denominator != 1 or not isprime(int(rg)):
                                    comp.append([list(k), str(rg) if rg < 10**40 else "big"])
                            info["leave_at"] = {"step": i, "z": zval, "formal_z": [zf[0], [[list(k), e] for k, e in zf[1]]],
                                                "composite_r_g": comp}
                            break
                    break
        if a.only_deep and len(rows) >= 2 and rows[1]["positive"]:
            continue
        print(json.dumps(info), flush=True)
        out.append(info)


if __name__ == "__main__":
    main()
