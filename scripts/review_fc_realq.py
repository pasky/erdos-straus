"""Hostile review of FORMAL_CLOSURE.md: test the LOGIC of §1.1 (not just the code)
against brute force at real q.

For a non-dead formal denominator Z, the fibre recipe of §1.1 claims: at any q in the
certificate's class at the primes that matter for THIS fibre (Lambda-primes of C_g for
g in P*Z, of c_r, c_s and of C_h for h | r), with r_g prime (g in s), distinct and
large, the actual fibre of z = Z(q) equals the set of values of the formal fibre.

We pick fibres whose s involves few polynomials, find such q (q = q0 mod M', the
s-polynomial values prime), compute the ACTUAL fibre by brute force over all divisors
of s(q)^2 (factorisation known: the prime values, and sympy for the constant), and
compare with the certificate's formal vertices containing Z evaluated at q.

Also: brute-force sanity check of SIGNED_REFACTOR §5 / WINDMILL Thm 7 at small p
(every p-free z outside [1,2t] lies in at most one signed vertex), |z| <= ZMAX.

uv run --with python-flint --with sympy python scripts/review_fc_realq.py
"""
from __future__ import annotations

import json
import random
import sys
import time
from collections import defaultdict
from fractions import Fraction
from math import gcd, prod

import flint
from sympy import divisors, factorint, isprime, primerange

sys.path.insert(0, __file__.rsplit("/", 1)[0])
import review_fc_fibres as RF
from review_fc_common import PKEY, XKEY, canon_vertex, load, vval


def actual_fibre(z, p, fac_pz):
    """all unordered (y, w) with 1/y+1/w = 4/p - 1/z, as sorted triples with z.
    fac_pz: dict prime->exp of |p*z|."""
    n, mm = 4 * z - p, p * z
    g = gcd(n, mm)
    r, s = n // g, mm // g
    if s < 0:
        r, s = -r, -s
    fs = {}
    ss = s
    for q_, e in fac_pz.items():
        k = vval(ss, q_)
        if k:
            fs[q_] = k
            ss //= q_ ** k
    assert ss == 1, "factorisation of s incomplete"
    # divisors of s^2
    divs = [1]
    for q_, e in fs.items():
        divs = [d * q_ ** i for d in divs for i in range(2 * e + 1)]
    out = set()
    s2 = s * s
    for d in divs:
        for D in (d, -d):
            if D == -s:
                continue
            if (D + s) % r or (s2 // D + s) % r:
                continue
            y, w = (D + s) // r, (s2 // D + s) // r
            out.add(tuple(sorted((z, y, w))))
    return out


def formal_value(F, q, Cof):
    c, ex = F
    v = Fraction(c)
    for k, e in ex:
        v *= Fraction(int(flint.fmpz_poly(list(k))(q)), Cof(k)) ** e
    return v


def main():
    random.seed(7)
    cert, clo, lamf = load()
    RF.init(cert)
    M = RF.M
    V = [canon_vertex(v) for v in cert["vertices"]]
    occ = defaultdict(set)
    for v in V:
        for F in v:
            occ[F].add(v)
    out = {"realq": [], "thm7": None}
    # candidate fibres: non-dead with few polys in P*Z
    cands = []
    for Z in occ:
        c, ex = Z
        keys = {k for k, e in ex} | {PKEY}
        pdiv = PKEY in {k for k, e in ex}
        if not pdiv:
            if c < 0:
                continue
            Zp = M.formal_poly(Z)
            d = Zp.degree()
            if d >= 2 or (d == 1 and (Zp[1] > 12 or (Zp[1] == 12 and Zp[0] > 0))):
                continue
        if len(keys) <= 3:
            cands.append(Z)
    random.shuffle(cands)
    print("candidate fibres", len(cands), flush=True)
    done = 0
    t0 = time.time()
    for Z in sorted(cands, key=lambda Z: -len(occ[Z]))[:15] + cands[:200]:
        if done >= 40 or time.time() - t0 > 2400:
            break
        verts, info = RF.fibre(Z)
        c, ex = Z
        relev = set()
        nums = [abs(info["c_r"]), abs(info["c_s"])] + [M.Cof(k) for k, e in ex] + [M.Cof(PKEY)]
        # C_h of factors of r: recompute r factors via N
        Zp = M.formal_poly(Z)
        N = 4 * Zp - flint.fmpq_poly([1, 24])
        cont, fac = N.numer().factor()
        for h, b in fac:
            nums.append(M.lam_part(h)[0])
        for x in nums:
            for ell in M.lam:
                if x % ell == 0:
                    relev.add(ell)
        Mp = prod(ell ** M.E[ell] for ell in relev)
        if Mp > 10 ** 45:
            continue
        q0p = M.q0 % Mp
        spolys = sorted({k for k, e in ex} | {PKEY})
        found = None
        for trial in range(300000):
            q = q0p + Mp * random.randrange(10 ** 6, 10 ** 9)
            vals = []
            ok = True
            for k in spolys:
                v = int(flint.fmpz_poly(list(k))(q))
                C = M.Cof(k)
                if v % C:
                    ok = False
                    break
                v //= C
                if v < 10 ** 6 or not isprime(v):
                    ok = False
                    break
                vals.append(v)
            if ok and len(set(vals)) == len(vals):
                found = (q, vals)
                break
        if not found:
            print("no q for", Z, flush=True)
            continue
        q, vals = found
        p = 24 * q + 1
        z = formal_value(Z, q, M.Cof)
        assert z.denominator == 1
        z = int(z)
        fac = dict(factorint(abs(c)))
        for k in spolys:
            pass
        for k, v in zip(spolys, vals):
            fac[v] = fac.get(v, 0)
        # |p*z| = p * |c| * prod r_g^e / prod ... ; build exactly
        fpz = defaultdict(int)
        for pr, e in factorint(abs(c)).items():
            fpz[pr] += e
        for k, e in ex:
            # g(q)/C_g = r_g is prime (k in spolys)
            fpz[vals[spolys.index(k)]] += e
        fpz[p] += 1
        # NB c*prod(g/C_g)^e: C_g already divided out
        assert prod(pr ** e for pr, e in fpz.items()) == abs(p * z)
        act = actual_fibre(z, p, fpz)
        form = set()
        nonint = 0
        for v in occ[Z]:
            vals3 = [formal_value(F, q, M.Cof) for F in v]
            if any(x.denominator != 1 for x in vals3):
                nonint += 1
            form.add(tuple(sorted(int(x) if x.denominator == 1 else x for x in vals3)))
        rec = dict(Z=str(Z), log10_Mp=len(str(Mp)), q_digits=len(str(q)), n_actual=len(act),
                   n_formal=len(form), equal=act == form, nonint=nonint, c_r=info["c_r"],
                   extra_actual=[str(x) for x in list(act - form)[:3]],
                   missing_actual=[str(x) for x in list(form - act)[:3]])
        print(json.dumps(rec)[:600], flush=True)
        out["realq"].append(rec)
        done += 1

    # ---- Theorem 7 / SR §5 brute force at small p
    PMAX, ZMAX = 400, 4000
    viol = []
    nb = 0
    for p in primerange(5, PMAX):
        if p % 4 != 1:
            continue
        t = (p - 1) // 4
        for z in list(range(-ZMAX, 0)) + list(range(2 * t + 1, ZMAX + 1)):
            if z % p == 0:
                continue
            fpz = factorint(abs(p * z))
            f = actual_fibre(z, p, fpz)
            nb += 1
            if len(f) > 1:
                viol.append((p, z, sorted(f)[:3]))
    out["thm7"] = dict(PMAX=PMAX, ZMAX=ZMAX, buckets=nb, violations=viol[:10], n_viol=len(viol))
    print("thm7", out["thm7"], flush=True)
    out["summary"] = dict(realq_fibres=len(out["realq"]),
                          realq_equal=sum(r["equal"] for r in out["realq"]),
                          realq_vertices=sum(r["n_actual"] for r in out["realq"]))
    print(out["summary"])
    json.dump(out, open("reviews/review_fc_realq.json", "w"), indent=1)


if __name__ == "__main__":
    main()
