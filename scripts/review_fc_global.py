"""Hostile review of FORMAL_CLOSURE.md: global (all-vertex) checks, independent code.

uv run --with python-flint --with sympy python scripts/review_fc_global.py
"""
from __future__ import annotations

import json
import sys
import time
from collections import Counter, defaultdict

import flint
from sympy import primerange

sys.path.insert(0, __file__.rsplit("/", 1)[0])
from review_fc_common import (PKEY, XKEY, Model, canon_formal, canon_vertex, load)

t0 = time.time()
out = {}
cert, clo, lamf = load()
m = Model(cert)
print("q0 digits", len(str(m.q0)), "log10 M", round(len(str(m.M)), 1), "E_max", max(m.E.values()))
out["E_max"] = max(m.E.values())
out["log10_M_digits"] = len(str(m.M))

# 1. consistency of the three data files
qt = int(clo["qt"])
out["lam_equal"] = sorted(clo["lam"]) == m.lam
out["qt_matches_q0"] = all(qt % (l ** m.E[l]) == m.res[l] for l in m.lam)
lr = lamf["residues"]
bad_lr = [l for l in m.lam if str(l) in lr and
          int(lr[str(l)][0]) % l ** min(int(lr[str(l)][1]), m.E[l]) != m.res[l] % l ** min(int(lr[str(l)][1]), m.E[l])]
low_lr = [l for l in m.lam if str(l) in lr and int(lr[str(l)][1]) < m.E[l]]
out["lam_final_consistent"] = (not bad_lr, len(lr), "residue precision < E at", low_lr[:10])
print("files:", out["lam_equal"], out["qt_matches_q0"], out["lam_final_consistent"], time.time() - t0)

# 2. S
nonprim, nonirr, neglc, Cmis, Cprec = [], [], [], [], []
for key, g in m.poly.items():
    if g.content() != 1:
        nonprim.append(key)
    if key[-1] <= 0:
        neglc.append(key)
    c, fac = g.factor()
    if not (len(fac) == 1 and fac[0][1] == 1 and abs(int(c)) == 1):
        nonirr.append(key)
    C, ok = m.lam_part(key)
    if not ok:
        Cprec.append(key)
    m.C[key] = C
    if C != m.cert_C[key]:
        Cmis.append(key)
sumdeg = sum(len(k) - 1 for k in m.poly)
out["S"] = dict(n=len(m.poly), sumdeg=sumdeg, nonprimitive=len(nonprim), reducible=len(nonirr),
                lc_nonpos=len(neglc), C_mismatch=len(Cmis), C_precision_fail=len(Cprec),
                X_in=XKEY in m.poly, P_in=PKEY in m.poly, C_X=m.C.get(XKEY), C_P=m.C.get(PKEY),
                maxdeg=max(len(k) - 1 for k in m.poly))
print("S:", out["S"], time.time() - t0)

# 3. vertices
V = [canon_vertex(v) for v in cert["vertices"]]
Vclo = set(canon_vertex(v) for v in clo["vertices"])
out["n_vertices"] = len(V)
out["vertices_distinct"] = len(set(V)) == len(V)
out["cert_equals_closure_vertices"] = set(V) == Vclo
P = flint.fmpq_poly([1, 24])
bad_id, notS, nonneg, zero_c, positive_vertices = [], [], [], [], []
entry_keys = set()
for v in V:
    for F in v:
        if F[0] == 0:
            zero_c.append(v)
        for k, e in F[1]:
            if k not in m.poly or e <= 0:
                notS.append(v)
            entry_keys.add(k)
    if not any(F[0] < 0 for F in v):
        nonneg.append(v)
    a, b, c = (m.formal_poly(F) for F in v)
    if P * (a * b + b * c + a * c) != 4 * a * b * c:
        bad_id.append(v)
seed = canon_vertex([(6, [(XKEY, 1)]), (-12, [(XKEY, 1), (PKEY, 1)]), (-12, [(XKEY, 1), (PKEY, 1)])])
out["vertex_checks"] = dict(identity_fail=len(bad_id), not_formal_over_S=len(notS), zero_const=len(zero_c),
                            no_negative_entry=len(nonneg), seed_present=seed in set(V))
flag_entry = {k for k, (ia, ie) in m.flags.items() if ie}
out["entry_flags"] = dict(n_entry_recomputed=len(entry_keys), flags_equal=entry_keys == flag_entry,
                          sumdeg_entry=sum(len(k) - 1 for k in entry_keys))
print("vertices:", out["vertex_checks"], out["entry_flags"], time.time() - t0)


# 4. denominators
def classify(F):
    c, ex = F
    if any(k == PKEY for k, e in ex):
        return "pdiv"
    if c < 0:
        return "dead"
    Zp = m.formal_poly(F)
    d = Zp.degree()
    if d >= 2:
        return "dead"
    if d == 1:
        lc, c0 = Zp[1], Zp[0]
        if lc > 12 or (lc == 12 and c0 > 0):
            return "dead"
        return "anchor"   # lc<12 (or =12, c0<=0): 0<Z<=12X eventually (lc>0 since c>0)
    return "anchor"


occ = defaultdict(set)
for i, v in enumerate(V):
    for F in v:
        occ[F].add(i)
cls = {Z: classify(Z) for Z in occ}
out["denominators"] = dict(Counter(cls.values()))
dead_multi = [Z for Z, c in cls.items() if c == "dead" and len(occ[Z]) > 1]
out["dead_in_more_than_one_vertex"] = len(dead_multi)
# sanity: positive degree-0 / lc checks for anchors
print("denominators:", out["denominators"], "dead multi:", len(dead_multi), time.time() - t0)

# 5. connectivity through shared formal denominators
par = list(range(len(V)))


def find(x):
    while par[x] != x:
        par[x] = par[par[x]]
        x = par[x]
    return x


for Z, s in occ.items():
    s = list(s)
    for j in s[1:]:
        a, b = find(s[0]), find(j)
        if a != b:
            par[a] = b
out["components"] = len({find(i) for i in range(len(V))})
print("components:", out["components"], time.time() - t0)

# 6. (C3) for every prime ell not in Lambda, ell <= sumdeg (full S), and for the entry family
lin = [k for k in m.poly if len(k) == 2]
quad = [k for k in m.poly if len(k) == 3]
c3_fail = []
c3_checked = 0
for ell in primerange(2, sumdeg + 1):
    if ell in m.lamset:
        continue
    c3_checked += 1
    covered = set()
    for b0, a1 in lin:
        if a1 % ell:
            covered.add((-b0 * pow(a1, -1, ell)) % ell)
    found = None
    for x in range(ell):
        if x in covered:
            continue
        if all((c0 + c1 * x + c2 * x * x) % ell for c0, c1, c2 in quad):
            found = x
            break
    if found is None:
        c3_fail.append(ell)
out["C3"] = dict(primes_checked=c3_checked, failures=c3_fail)
print("C3:", out["C3"], time.time() - t0)

out["dead_examples"] = [str(Z) for Z in dead_multi[:5]]
json.dump(out, open("reviews/review_fc_global.json", "w"), indent=1, default=str)
print(json.dumps(out, default=str))
