"""Iteration helper for formal2.py (FORMAL_CLOSURE.md §2).

  init     --qt-from DUMP | --B B --seed s   -> lam file (residues of qt mod ell^k, ell<=B)
  explicit DUMP_A OUT.txt                    -> r-primes failing the counting certificate
  analyze  DUMP_B LAMFILE NEWLAMFILE         -> residue choices; obstacles appended to LAM

Obstacles are primes ell outside LAM at which no admissible residue exists in the
generic model:
  (a) C3: every residue mod ell is a root of some g in S (fixed prime divisor);
  (b) r-primes: every residue is a root of some g in S or activates a fragile candidate.
Such an ell is added to LAM with a residue rho (24 rho+1 a nonzero square mod ell,
rho != 0), minimising (#g in S with g(rho)=0, #fragile candidates activated).
"""
import gzip
import json
import random
import sys

import numpy as np
import flint
sys.set_int_max_str_digits(0)
from sympy import primerange


def kfor(ell):
    k = 1
    while ell**k < 2**64:
        k += 1
    return k


def roots(coeffs, ell):
    c = [a % ell for a in coeffs]
    while c and c[-1] == 0:
        c.pop()
    if len(c) <= 1:
        return []
    if len(c) == 2:
        return [(-c[0] * pow(c[1], -1, ell)) % ell]
    return [int(r) for r, _ in flint.nmod_poly(c, ell).roots()]


def vpow(a, e, ell):
    r = np.ones_like(a)
    b = a % ell
    while e:
        if e & 1:
            r = (r * b) % ell
        b = (b * b) % ell
        e >>= 1
    return r


def scount(S, ell):
    """cnt[x] = number of g in S with g(x) = 0 mod ell (vectorised for deg <= 2)"""
    cnt = np.zeros(ell, dtype=np.int64)
    lin = [k for k in S if len(k) == 2]
    quad = [k for k in S if len(k) == 3]
    for k in S:
        if len(k) > 3:
            for r in roots(k, ell):
                cnt[r] += 1
    if lin:
        a0 = np.array([k[0] % ell for k in lin], dtype=np.int64)
        a1 = np.array([k[1] % ell for k in lin], dtype=np.int64)
        ok = a1 != 0
        rt = (-a0[ok] % ell) * vpow(a1[ok], ell - 2, ell) % ell
        np.add.at(cnt, rt, 1)
    if quad:
        a0 = np.array([k[0] % ell for k in quad], dtype=np.int64)
        a1 = np.array([k[1] % ell for k in quad], dtype=np.int64)
        a2 = np.array([k[2] % ell for k in quad], dtype=np.int64)
        deg1 = (a2 == 0) & (a1 != 0)
        if deg1.any():
            rt = (-a0[deg1] % ell) * vpow(a1[deg1], ell - 2, ell) % ell
            np.add.at(cnt, rt, 1)
        q = a2 != 0
        a0, a1, a2 = a0[q], a1[q], a2[q]
        if ell == 2:
            for x in range(2):
                np.add.at(cnt, np.full(int(((a2 * x * x + a1 * x + a0) % 2 == 0).sum()), x), 1)
        else:
            sqt = np.full(ell, -1, dtype=np.int64)
            xs = np.arange((ell + 1) // 2, dtype=np.int64)
            sqt[(xs * xs) % ell] = xs
            disc = (a1 * a1 % ell - 4 * (a0 * a2 % ell)) % ell
            sr = sqt[disc]
            has = sr >= 0
            inv2a = vpow((2 * a2[has]) % ell, ell - 2, ell)
            r1 = ((-a1[has] + sr[has]) % ell) * inv2a % ell
            r2 = ((-a1[has] - sr[has]) % ell) * inv2a % ell
            np.add.at(cnt, r1, 1)
            dz = sr[has] != 0
            np.add.at(cnt, r2[dz], 1)
    return cnt


def qrmask(ell):
    x = np.arange(ell, dtype=np.int64)
    v = (24 * x + 1) % ell
    sq = np.zeros(ell, dtype=bool)
    sq[(x * x) % ell] = True
    m = sq[v] & (v != 0) & (x != 0)
    return m


def cmd_init(argv):
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("out")
    ap.add_argument("--qt-from")
    ap.add_argument("--B", type=int, default=1500)
    ap.add_argument("--seed", type=int, default=1)
    a = ap.parse_args(argv)
    if a.qt_from:
        st = json.load(gzip.open(a.qt_from, "rt"))
        qt = int(st["qt"])
        B = st["B"]
    else:
        sys.path.insert(0, __file__.rsplit("/", 1)[0])
        import formal2
        qt = formal2.model_point(a.B, a.seed)
        B = a.B
    res = {str(l): [qt % l**kfor(l), kfor(l)] for l in primerange(2, B + 1)}
    json.dump({"residues": res, "seed": a.seed, "base_B": B, "added": []}, open(a.out, "w"))


def cmd_explicit(argv):
    st = json.load(gzip.open(argv[0], "rt"))
    sdeg = sum(len(k) - 1 for k, C, a, e in st["S"])
    lam = set(st["lam"])
    bad = sorted(int(l) for l, b in st["budget"].items() if int(l) not in lam and b + sdeg >= int(l) - 1)
    open(argv[1], "w").write(" ".join(map(str, bad)))
    print(json.dumps({"explicit": len(bad), "max": bad[-1] if bad else None, "sum_deg": sdeg}))


def cmd_analyze(argv):
    st = json.load(gzip.open(argv[0], "rt"))
    LF = json.load(open(argv[1]))
    S = [k for k, C, a, e in st["S"]]
    sdeg = sum(len(k) - 1 for k in S)
    lam = set(st["lam"])
    explicit = set(st["explicit"])
    budget = {int(l): b for l, b in st["budget"].items()}
    frag = {int(l): {int(x): c for x, c in d.items()} for l, d in st["fragile"].items()}
    rp = set(st["rprimes"]) - lam
    need_explicit, rho, obstacles = [], {}, []
    rng = random.Random(len(lam))
    for ell in sorted(rp):
        if ell not in explicit:
            if budget.get(ell, 0) + sdeg >= ell - 1:
                need_explicit.append(ell)
            continue
        cnt = scount(S, ell)
        fc = np.zeros(ell, dtype=np.int64)
        for x, c in frag.get(ell, {}).items():
            fc[x] += c
        free = np.flatnonzero((cnt == 0) & (fc == 0))
        if len(free):
            rho[ell] = int(free[0])
            continue
        m = qrmask(ell)
        cost = cnt * 10**6 + fc
        cost[~m] = 1 << 62
        x = int(np.argmin(cost))
        obstacles.append({"ell": ell, "rho": x, "S_roots": int(cnt[x]), "frag": int(fc[x]), "why": "r"})
    for ell in primerange(2, sdeg + 2):
        ell = int(ell)
        if ell in lam or ell in rp:
            continue
        cnt = scount(S, ell)
        if (cnt == 0).any():
            continue
        m = qrmask(ell)
        cost = cnt.copy()
        cost[~m] = 1 << 62
        x = int(np.argmin(cost))
        obstacles.append({"ell": ell, "rho": x, "S_roots": int(cnt[x]), "frag": 0, "why": "C3"})
    summary = {"S": len(S), "sum_deg": sdeg, "vertices": len(st["vertices"]), "rprimes_outside": len(rp),
               "explicit_ok": len(rho), "need_explicit": need_explicit[:20], "n_need_explicit": len(need_explicit),
               "obstacles": len(obstacles),
               "obst_list": [(o["ell"], o["S_roots"], o["frag"], o["why"]) for o in obstacles][:60],
               "positive": sum(1 for v in st["vertices"] if all(z[0] > 0 for z in v))}
    print(json.dumps(summary))
    if len(argv) > 2:
        for o in obstacles:
            ell, k = o["ell"], kfor(o["ell"])
            LF["residues"][str(ell)] = [o["rho"] + ell * rng.randrange(ell ** (k - 1)), k]
            LF["added"].append(o)
        LF["generic_rho"] = {str(l): r for l, r in rho.items()}
        json.dump(LF, open(argv[2], "w"))


def cmd_finalize(argv):
    """all r-primes become model primes: explicit ones get the generic rho found by analyze
    (stored in the NEW lam file), the others a random residue avoiding the roots of S."""
    st = json.load(gzip.open(argv[0], "rt"))
    LF = json.load(open(argv[1]))
    S = [k for k, C, a, e in st["S"]]
    lam = set(int(l) for l in LF["residues"])
    rng = random.Random(12345)
    gr = {int(l): r for l, r in LF.get("generic_rho", {}).items()}
    nnew = 0
    for ell in sorted(set(st["rprimes"]) - lam):
        if ell in gr:
            rho = gr[ell]
        else:
            while True:
                rho = rng.randrange(1, ell)
                if all(sum(a * pow(rho, i, ell) for i, a in enumerate(k)) % ell for k in S):
                    break
        LF["residues"][str(ell)] = [rho, 1]
        nnew += 1
    LF["finalized_from"] = argv[0]
    json.dump(LF, open(argv[2], "w"))
    print(json.dumps({"added_model_primes": nnew, "lam": len(LF["residues"])}))


if __name__ == "__main__":
    {"init": cmd_init, "explicit": cmd_explicit, "analyze": cmd_analyze, "finalize": cmd_finalize}[sys.argv[1]](sys.argv[2:])
