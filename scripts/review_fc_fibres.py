"""Hostile review of FORMAL_CLOSURE.md: independent recomputation of formal fibres.

uv run --with python-flint --with sympy python scripts/review_fc_fibres.py [--n 240] [--jobs 6] [--all]

For a non-dead formal denominator Z = c*prod(g/C_g)^e (over S):
  N = 4Z - P;  r/s = N/(P Z) reduced in Q(X);
  s = c_s * prod (g/C_g)^alpha_g  (entry polys only),  r = c_r * prod (h/C_h)^beta_h,
  with c_r, c_s coprime integers (q-independent scaling; any common integer scaling of
  (r(q), s(q)) gives the same fibre since (r y - s)(r w - s) = s^2 for every such pair).
  At admissible q the divisors of s(q)^2 are D = +-d prod r_g^j, d | c_s^2, 0<=j<=2 alpha.
  Candidate (y, w) = ((D+s)/r, (s^2/D+s)/r), D != -s, accepted iff both are integral:
    (A) h^beta | D+s in Q[X]  (resp. s^2/D+s)  for every h in r;
    (B) c_r | (D+s)(q)  evaluated at q0  (the certificate's class), and we check that
        q0 mod ell^E_ell suffices: v_ell(c_r) + v_ell(den(D+s)) <= E_ell for every ell|c_r,
        for every candidate that passes (A) (accepted or rejected by (B)).
  Additionally: every prime of c_r is in Lambda; every factor h of r has
  v_ell(h(q0)) < E_ell (so r_h = h(q)/C_h is Lambda-free); y, w factor over S with
  integral constants.
Pinning: if r has a nonconstant factor h0, (A) forces d*E(theta) = -s(theta) at a root
theta of h0, i.e. the constant of D is determined by its monomial; otherwise all
divisors d of c_s^2 are enumerated.
"""
from __future__ import annotations

import argparse
import itertools
import json
import random
import sys
import time
from collections import Counter, defaultdict
from fractions import Fraction
from math import gcd, prod
from multiprocessing import Pool

import flint
from sympy import divisors, factorint

sys.path.insert(0, __file__.rsplit("/", 1)[0])
from review_fc_common import PKEY, XKEY, Model, canon_formal, canon_vertex, load, vval

M = None
SKEYS = None


def fq(x):
    return flint.fmpq_poly([x]) if not isinstance(x, flint.fmpq_poly) else x


def normkey(g):
    """primitive, lc>0 fmpz_poly -> key"""
    return tuple(int(a) for a in g.coeffs())


def to_formal(poly_q):
    """fmpq_poly -> formal integer over S, or raise."""
    num, den = poly_q.numer(), int(poly_q.denom())
    cont, fac = num.factor()
    const = Fraction(int(cont), den)
    ex = []
    for h, e in fac:
        if h.coeffs()[-1] < 0:
            h = -h
            if e % 2:
                const = -const
        key = normkey(h)
        if key not in SKEYS:
            raise ValueError(("factor not in S", key))
        const *= M.Cof(key) ** e
        ex.append((key, e))
    if const.denominator != 1:
        raise ValueError(("nonintegral constant", const))
    return canon_formal((const.numerator, ex))


def fibre(Z):
    """Return (set of canonical vertices, info dict)."""
    info = {}
    c, ex = Z
    P = flint.fmpq_poly([1, 24])
    Zp = M.formal_poly(Z)
    N = 4 * Zp - P
    # exponents of PZ
    ePZ = defaultdict(int)
    for k, e in ex:
        ePZ[k] += e
    ePZ[PKEY] += 1
    # cancel common factors
    Nn = N
    cs_q = Fraction(int(c))
    alpha = {}
    for k, e in ePZ.items():
        g = flint.fmpq_poly(list(k))
        mcount = 0
        while mcount < e:
            qq, rr = divmod(Nn, g)
            if rr != 0:
                break
            Nn = qq
            mcount += 1
        cs_q /= M.Cof(k) ** mcount
        if e - mcount > 0:
            alpha[k] = e - mcount
    # r = Nn = kappa * prod h^beta
    num, den = Nn.numer(), int(Nn.denom())
    cont, fac = num.factor()
    kappa = Fraction(int(cont), den)
    rfac = []
    for h, b in fac:
        if h.coeffs()[-1] < 0:
            h = -h
            if b % 2:
                kappa = -kappa
        key = normkey(h)
        Ch, ok = M.lam_part(h)
        if not ok:
            info["aux_precision_fail"] = info.get("aux_precision_fail", 0) + 1
        info.setdefault("aux_not_in_S", 0)
        if key not in SKEYS:
            info["aux_not_in_S"] += 1
        rfac.append((h, key, b, Ch))
        kappa *= Ch ** b
    a, b_ = kappa, cs_q
    L = a.denominator * b_.denominator // gcd(a.denominator, b_.denominator)
    A, B = int(a * L), int(b_ * L)
    g0 = gcd(A, B)
    c_r, c_s = A // g0, B // g0
    if c_s < 0:
        c_r, c_s = -c_r, -c_s
    # r_poly and s_poly (as fmpq_polys)
    s_formal = (c_s, tuple(sorted(alpha.items())))
    s_poly = M.formal_poly(s_formal)
    r_poly = flint.fmpq_poly([c_r])
    for h, key, b, Ch in rfac:
        r_poly *= (flint.fmpq_poly(h) / Ch) ** b
    assert r_poly * Zp * P == s_poly * N, "r/s != N/(PZ)"
    # c_r primes
    cr_abs = abs(c_r)
    for ell in M.lam:
        if cr_abs % ell == 0:
            while cr_abs % ell == 0:
                cr_abs //= ell
    info["c_r_outside_lambda"] = cr_abs
    info["c_r"] = c_r
    info["c_s"] = c_s
    crl = {ell: vval(c_r, ell) for ell in M.lam if c_r % ell == 0}
    # values at q0 mod |c_r|
    mod = abs(c_r)
    Rv = {}
    for k in alpha:
        Rv[k] = (int(flint.fmpz_poly(list(k))(M.q0)) // M.Cof(k)) % mod if mod > 1 else 0
    s_val = (c_s * prod(pow(Rv[k], e, mod) for k, e in alpha.items())) % mod if mod > 1 else 0

    keys = sorted(alpha)
    Gpoly = {k: flint.fmpq_poly(list(k)) / M.Cof(k) for k in keys}
    nonconst = [(h, b) for h, key, b, Ch in rfac if h.degree() >= 1]
    hpows = [flint.fmpq_poly(h) ** b for h, key, b, Ch in rfac if h.degree() >= 1]
    h0 = flint.fmpq_poly(nonconst[0][0]) if nonconst else None
    cs2 = c_s * c_s
    s_mod = s_poly % h0 if h0 is not None else None
    dlist = None
    if h0 is None:
        dlist = divisors(abs(cs2))
    ranges = [range(2 * alpha[k] + 1) for k in keys]
    accepted = {}
    n_mono = 0
    n_A = 0
    need_prec = 0
    prec_fail = []

    def testA(Dp):
        T = Dp + s_poly
        for hp in hpows:
            if T % hp != 0:
                return None
        return T

    for js in itertools.product(*ranges):
        n_mono += 1
        Ep = flint.fmpq_poly([1])
        for k, j in zip(keys, js):
            if j:
                Ep *= Gpoly[k] ** j
        if h0 is not None:
            em = Ep % h0
            # lambda*em == -s_mod
            if h0.degree() == 1:
                lamb = -s_mod[0] / em[0]
            else:
                if em[1] != 0:
                    lamb = -s_mod[1] / em[1]
                else:
                    lamb = -s_mod[0] / em[0]
                if lamb * em != -s_mod:
                    continue
            lamb = Fraction(int(lamb.p), int(lamb.q))
            if lamb.denominator != 1 or lamb == 0 or cs2 % lamb.numerator != 0:
                continue
            consts = [lamb.numerator]
        else:
            consts = [s * d for d in dlist for s in (1, -1)]
        for lam_ in consts:
            if lam_ == -c_s and all(j == alpha[k] for k, j in zip(keys, js)):
                continue  # D = -s
            Dp = Ep * lam_
            T = testA(Dp)
            if T is None:
                continue
            n_A += 1
            # precision for (B)
            dT = int(T.denom())
            for ell, v in crl.items():
                need = v + vval(dT, ell)
                need_prec = max(need_prec, need)
                if need > M.E[ell]:
                    prec_fail.append((ell, need, M.E[ell]))
            if mod > 1:
                Dv = (lam_ * prod(pow(Rv[k], j, mod) for k, j in zip(keys, js))) % mod
                if (Dv + s_val) % mod != 0:
                    continue
            accepted[(lam_, js)] = T
    info["monomials"] = n_mono
    info["passA"] = n_A
    info["accepted_D"] = len(accepted)
    info["prec_fail"] = prec_fail[:5]
    info["n_prec_fail"] = len(prec_fail)
    # build vertices: need both D and s^2/D accepted
    verts = set()
    errors = []
    for (lam_, js), T in accepted.items():
        comp = (cs2 // lam_, tuple(2 * alpha[k] - j for k, j in zip(keys, js)))
        if comp not in accepted:
            continue
        T2 = accepted[comp]
        try:
            y = to_formal(T / r_poly)
            w = to_formal(T2 / r_poly)
        except ValueError as e:
            errors.append(str(e)[:200])
            continue
        verts.add(canon_vertex([canon_formal(Z), y, w]))
    info["errors"] = errors[:5]
    info["n_errors"] = len(errors)
    info["unpaired"] = sum(1 for (l, js) in accepted
                           if (cs2 // l, tuple(2 * alpha[k] - j for k, j in zip(keys, js))) not in accepted)
    return verts, info


def init(cert):
    global M, SKEYS
    M = Model(cert)
    for coeffs, Cg, *_ in cert["S"]:
        M.C[tuple(int(a) for a in coeffs)] = int(Cg)   # verified equal in review_fc_global.py
    SKEYS = set(M.poly)


def work(args):
    Z, expected = args
    t = time.time()
    try:
        verts, info = fibre(Z)
    except Exception as e:  # report, do not hide
        return dict(Z=str(Z), exception=repr(e)[:300])
    info["Z"] = str(Z)
    info["n_mine"] = len(verts)
    info["n_cert"] = len(expected)
    info["equal"] = verts == expected
    info["missing_in_cert"] = [str(v) for v in list(verts - expected)[:3]]
    info["extra_in_cert"] = [str(v) for v in list(expected - verts)[:3]]
    info["time"] = round(time.time() - t, 2)
    return info


_cert = None


def _pinit():
    init(_cert)


def main():
    global _cert
    ap = argparse.ArgumentParser()
    ap.add_argument("--n", type=int, default=240)
    ap.add_argument("--jobs", type=int, default=6)
    ap.add_argument("--seed", type=int, default=20260926)
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--out", default="reviews/review_fc_fibres.json")
    a = ap.parse_args()
    cert, clo, lamf = load()
    _cert = cert
    init(cert)
    V = [canon_vertex(v) for v in cert["vertices"]]
    occ = defaultdict(set)
    for v in V:
        for F in v:
            occ[F].add(v)

    def classify(F):
        c, ex = F
        if any(k == PKEY for k, e in ex):
            return "pdiv"
        if c < 0:
            return "dead"
        Zp = M.formal_poly(F)
        d = Zp.degree()
        if d >= 2 or (d == 1 and (Zp[1] > 12 or (Zp[1] == 12 and Zp[0] > 0))):
            return "dead"
        return "anchor"

    cls = {Z: classify(Z) for Z in occ}
    nondead = [Z for Z in occ if cls[Z] != "dead"]
    if a.all:
        sample = nondead
    else:
        rng = random.Random(a.seed)
        by = defaultdict(list)
        for Z in nondead:
            by[cls[Z]].append(Z)
        sample = set()
        # seed's neighbours: the denominators of the seed, t=6X and -pt = -6XP
        for Z in [(6, ((XKEY, 1),)), (-6, tuple(sorted(((XKEY, 1), (PKEY, 1))))),
                  (-12, tuple(sorted(((XKEY, 1), (PKEY, 1)))))]:
            Zc = canon_formal(Z)
            if Zc in occ:
                sample.add(Zc)
        # largest fibres
        big = sorted(nondead, key=lambda Z: -len(occ[Z]))[:25]
        sample.update(big)
        # stratified random
        for kind, frac in (("pdiv", 0.55), ("anchor", 0.45)):
            sample.update(rng.sample(by[kind], int(a.n * frac)))
        sample = sorted(sample, key=lambda Z: -len(occ[Z]))
    print("sample", len(sample), Counter(cls[Z] for Z in sample), flush=True)
    res = []
    t0 = time.time()
    with Pool(a.jobs, initializer=_pinit) as pool:
        for i, r in enumerate(pool.imap_unordered(work, [(Z, occ[Z]) for Z in sample])):
            r["kind"] = cls.get(eval(r["Z"]), "?") if "Z" in r else "?"
            res.append(r)
            if not r.get("equal", False) or r.get("n_prec_fail") or r.get("c_r_outside_lambda", 1) != 1 \
                    or r.get("aux_precision_fail") or r.get("n_errors") or r.get("aux_not_in_S"):
                print("PROBLEM", json.dumps(r)[:1500], flush=True)
            if i % 20 == 0:
                print(i, round(time.time() - t0), r.get("n_mine"), r.get("time"), flush=True)
    summary = dict(
        n=len(res),
        kinds=dict(Counter(r["kind"] for r in res)),
        equal=sum(1 for r in res if r.get("equal")),
        exceptions=sum(1 for r in res if "exception" in r),
        prec_fail=sum(1 for r in res if r.get("n_prec_fail")),
        c_r_outside=sum(1 for r in res if r.get("c_r_outside_lambda", 1) != 1),
        aux_precision_fail=sum(1 for r in res if r.get("aux_precision_fail")),
        aux_not_in_S=sum(1 for r in res if r.get("aux_not_in_S")),
        errors=sum(1 for r in res if r.get("n_errors")),
        vertices_compared=sum(r.get("n_cert", 0) for r in res),
        max_fibre=max(r.get("n_cert", 0) for r in res),
        passA_total=sum(r.get("passA", 0) for r in res),
        monomials_total=sum(r.get("monomials", 0) for r in res),
        time=round(time.time() - t0),
    )
    print(json.dumps(summary))
    json.dump(dict(summary=summary, results=res), open(a.out, "w"), indent=0)


if __name__ == "__main__":
    main()
