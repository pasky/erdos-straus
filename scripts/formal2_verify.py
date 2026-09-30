"""Independent verification of a fully-model formal closure certificate (FORMAL_CLOSURE.md §3).

uv run --with python-flint python scripts/formal2_verify.py LAMFILE DUMP.json.gz [--jobs 14] [--cert OUT.json.gz]

Checks, all exact:
 1. qt rebuilt from LAMFILE equals the dump's model point; LAM = the dump's LAM.
 2. S: every g primitive, lc>0, irreducible over Q; C_g = prod_{ell in LAM} ell^{v_ell(g(qt))}
    recomputed by trial division; E_ell := 1 + max v_ell(g(qt)) (and the fibre precision below).
 3. Every vertex: entries are formal integers over S with nonzero integer constants; the
    identity 1/a+1/b+1/c = 4/(24X+1) holds in Q(X); some entry has a negative constant.
    The seed (6X,-12XP,-12XP) is a vertex.
 4. Every denominator Z of every vertex is classified independently; for non-dead Z (p-divisible,
    or p-free with 0 < Z <= 12X eventually) the fibre is recomputed by the OLD sympy engine
    scripts/formal_closure.py (small primes := LAM, qt := model point) and must be contained in
    the vertex set, and every vertex containing Z must be in it.  Every prime of every c_r must
    lie in LAM (then all decisions are exact at q = qt mod prod ell^E_ell).
    Dead Z: negative, or degree >= 2, or degree 1 with Z > 12X eventually (WINDMILL Thm 7).
 5. H has no fixed prime divisor: for every prime ell outside LAM with ell <= sum deg S, some
    residue mod ell is a root of no g in S.
"""
from __future__ import annotations

import argparse
import gzip
import json
import sys
from fractions import Fraction
from math import prod
from multiprocessing import Pool

import flint

sys.set_int_max_str_digits(0)
sys.path.insert(0, __file__.rsplit("/", 1)[0])
import formal2  # noqa: E402  (only build_qt)
from formal2_iter import scount  # noqa: E402
from sympy import primerange  # noqa: E402

G = {}


def old_init(qt, lam):
    import formal_closure as fc
    G["F"] = fc.Formal(1500, 1, qt=qt, extra_small=[l for l in lam if l > 1500])
    G["fc"] = fc


def to_old(F, z):
    """new formal integer (keys low->high) -> old (keys high->low)"""
    fc = G["fc"]
    c, ex = z
    out = []
    for k, e in ex:
        ko = tuple(reversed(k))
        if ko not in F.primes:
            F.key(fc.Poly(list(ko), fc.X, domain=fc.ZZ))
        out.append((ko, e))
    return (c, tuple(sorted(out)))


def from_old(z):
    c, ex = z
    return (c, tuple(sorted((tuple(reversed(k)), e) for k, e in ex)))


def old_work(Z):
    F = G["F"]
    zo = to_old(F, Z)
    F.r_primes = set()
    F.flags = []
    out = F.fibre(zo)
    res = [tuple(sorted(from_old(z) for z in w)) for w in out]
    return Z, res, sorted(F.r_primes)


def canon(v):
    return tuple(sorted(v))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("lamfile")
    ap.add_argument("dump")
    ap.add_argument("--jobs", type=int, default=14)
    ap.add_argument("--cert", default=None)
    ap.add_argument("--skip-fibres", action="store_true")
    a = ap.parse_args()
    LF = json.load(open(a.lamfile))
    st = json.load(gzip.open(a.dump, "rt"))
    res = {int(l): tuple(v) for l, v in LF["residues"].items()}
    lam = sorted(res)
    qt = formal2.build_qt(res, LF.get("seed", 1))
    assert qt == int(st["qt"]), "model point mismatch"
    assert lam == sorted(st["lam"]), "LAM mismatch"
    report = {"LAM": len(lam), "maxLAM": lam[-1]}
    # ---- 2. S
    S = {}
    maxval = {}
    for key, C, isaux, isentry in st["S"]:
        key = tuple(key)
        g = flint.fmpz_poly(list(key))
        assert g.degree() >= 1 and g.content() == 1 and key[-1] > 0, key
        cont, facs = g.factor()
        assert len(facs) == 1 and facs[0][1] == 1, ("reducible", key)
        v = int(g(qt))
        assert v > 0
        CC = 1
        for ell in lam:
            k = 0
            while v % ell == 0:
                v //= ell
                k += 1
            if k:
                CC *= ell**k
                maxval[ell] = max(maxval.get(ell, 0), k)
        assert CC == C, ("C_g mismatch", key)
        S[key] = (g, C, v, bool(isaux), bool(isentry))
    sdeg = sum(len(k) - 1 for k in S)
    report.update(S=len(S), S_entry=sum(1 for x in S.values() if x[4]), sum_deg=sdeg,
                  sum_deg_entry=sum(len(k) - 1 for k, x in S.items() if x[4]),
                  max_deg=max(len(k) - 1 for k in S))
    P = (1, 24)
    X = (0, 1)
    assert P in S and X in S

    def polyq(z):
        c, ex = z
        num, den = flint.fmpz_poly([c]), 1
        for k, e in ex:
            num *= S[k][0] ** e
            den *= S[k][1] ** e
        return num, den

    # ---- 3. vertices
    V = set()
    for v in st["vertices"]:
        w = []
        for c, ex in v:
            assert isinstance(c, int) and c != 0
            ex = tuple(sorted((tuple(k), e) for k, e in ex))
            for k, e in ex:
                assert k in S and e > 0, "entry poly not in S"
            w.append((c, ex))
        w = canon(w)
        (n1, d1), (n2, d2), (n3, d3) = [polyq(z) for z in w]
        PX = flint.fmpz_poly([1, 24])
        # sum d_i/n_i = 4/P  <=>  P(d1 n2 n3 + d2 n1 n3 + d3 n1 n2) = 4 n1 n2 n3
        assert PX * (d1 * n2 * n3 + d2 * n1 * n3 + d3 * n1 * n2) == 4 * n1 * n2 * n3, w
        assert any(z[0] < 0 for z in w), ("positive formal vertex", w)
        V.add(w)
    seed = canon([(6, ((X, 1),)), (-12, tuple(sorted([(X, 1), (P, 1)]))), (-12, tuple(sorted([(X, 1), (P, 1)])))])
    assert seed in V
    report["vertices"] = len(V)
    # ---- 4. denominators
    byden = {}
    for w in V:
        for z in w:
            byden.setdefault(z, set()).add(w)

    def kind(z):
        c, ex = z
        if any(k == P for k, e in ex):
            return "pdiv"
        if c < 0:
            return "dead"
        d = sum((len(k) - 1) * e for k, e in ex)
        if d == 0:
            return "anchor"
        if d >= 2:
            return "dead"
        num, den = polyq(z)
        a1 = Fraction(int(num.coeffs()[1]), den)
        a0 = Fraction(int(num.coeffs()[0]), den)
        return "dead" if (a1 > 12 or (a1 == 12 and a0 > 0)) else "anchor"

    kinds = {z: kind(z) for z in byden}
    report["denominators"] = {k: sum(1 for x in kinds.values() if x == k) for k in ("pdiv", "anchor", "dead")}
    for z, kd in kinds.items():
        if kd == "dead":
            assert len(byden[z]) == 1, ("dead denominator in two formal vertices", z)
    todo = [z for z, kd in kinds.items() if kd != "dead"]
    if not a.skip_fibres:
        bad = 0
        rp = set()
        with Pool(a.jobs, initializer=old_init, initargs=(qt, lam)) as pool:
            for n, (Z, ws, rps) in enumerate(pool.imap_unordered(old_work, todo, chunksize=4)):
                rp.update(rps)
                fib = {canon(w) for w in ws}
                if not fib <= V or fib != byden[Z]:
                    bad += 1
                    print("FIBRE MISMATCH", Z, len(fib), len(byden[Z]), len(fib - V), file=sys.stderr)
                if n % 1000 == 0:
                    print("fibres", n, len(todo), file=sys.stderr, flush=True)
        report["fibres_checked"] = len(todo)
        report["fibre_mismatches"] = bad
        report["r_primes_outside_LAM"] = sorted(rp)[:20]
        assert bad == 0 and not rp
    # ---- 5. no fixed prime divisor
    lamset = set(lam)
    Sk = list(S)
    c3 = []
    for ell in primerange(2, sdeg + 2):
        ell = int(ell)
        if ell in lamset:
            continue
        if not (scount(Sk, ell) == 0).any():
            c3.append(ell)
    report["fixed_prime_divisors"] = c3
    assert not c3
    # ---- precision
    E = {ell: maxval.get(ell, 0) + 1 for ell in lam}
    for l, v in st["needE"].items():
        E[int(l)] = max(E[int(l)], v)
    report["E_max"] = max(E.values())
    report["log10_M"] = round(sum(e * __import__("math").log10(l) for l, e in E.items()), 1)
    report["OK"] = True
    print(json.dumps(report))
    if a.cert:
        cert = {"q0_mod": {str(l): [qt % l**E[l], E[l]] for l in lam},
                "S": [[list(k), x[1], x[3], x[4]] for k, x in sorted(S.items())],
                "vertices": [[[z[0], [[list(k), e] for k, e in z[1]]] for z in w] for w in sorted(V)],
                "report": report}
        with gzip.open(a.cert, "wt") as fh:
            json.dump(cert, fh)


if __name__ == "__main__":
    main()
