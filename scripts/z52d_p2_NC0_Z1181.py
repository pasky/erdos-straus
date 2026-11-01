#!/usr/bin/env python3
"""Z1181: equality-saturation-lite over 3-term unit-fraction forms for 4/n.

Not a full e-graph library: a closure over two rewrite rules on unit-fraction denominators,
which are polynomials in n with rational coefficients (exact Fractions):
  R1:  1/d = 1/(d+1) + 1/(d(d+1))        (verified identity, any d != 0, -1)
  R2:  1/d = 1/(2d) + 1/(2d)
Seeds (verified 2-term identities for 4/n, each checked symbolically in the script):
  A:  4/n = 1/((n+1)/4) + 1/(n(n+1)/4)
  B:  4/n = 1/((n+2)/4) + 1/(n(n+2)/8)
Forms are 3-term multisets reached from a seed by one rewrite of one denominator (R1 or R2),
and from those by one further rewrite of one denominator that keeps 3 terms (R1 with
we keep only sets of size 3). Equal forms are merged by their
polynomial triple. Scoring (the 'extraction' step): the integrality domain of the triple,
i.e. the residues n mod 840 at which all three denominators are integers and positive for
large n. Result: which residue classes (mod 4, mod 8, mod 24) any extracted form covers.
"""
import itertools, json
from fractions import Fraction as F

# polynomial = tuple of Fractions, ascending powers of n
def padd(a, b):
    m = max(len(a), len(b))
    a = list(a) + [F(0)] * (m - len(a)); b = list(b) + [F(0)] * (m - len(b))
    return tuple(x + y for x, y in zip(a, b))

def pmul(a, b):
    r = [F(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            r[i + j] += x * y
    return tuple(r)

def pscale(c, a):
    return tuple(c * x for x in a)

def norm(a):
    a = list(a)
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return tuple(a)

def ev(p, n):
    return sum(c * n ** i for i, c in enumerate(p))

N = (F(0), F(1))
ONE = (F(1),)

def R1(d):
    return [padd(d, ONE), pmul(d, padd(d, ONE))]

def R2(d):
    return [pscale(F(1, 2), d), pscale(F(1, 2), d)]

def check_identity(terms):
    """terms: list of denominators; verify 4/n = sum 1/d exactly at 12 sample points"""
    for n in range(3, 15):
        lhs = F(4, n)
        rhs = sum(F(1) / ev(d, n) for d in terms)
        if lhs != rhs:
            return False
    return True

seeds = {
    "A": [padd(pscale(F(1, 4), N), pscale(F(1, 4), ONE)), pscale(F(1, 4), pmul(N, padd(N, ONE)))],
    "B": [pscale(F(1, 4), padd(N, (F(2),))), pscale(F(1, 8), pmul(N, padd(N, (F(2),))))],
}
for k, s in seeds.items():
    assert check_identity(s), k

forms = {}
def add_form(terms, origin):
    key = tuple(sorted(norm(t) for t in terms))
    if key not in forms:
        forms[key] = origin
    return key

for name, s in seeds.items():
    for i, d in enumerate(s):
        for rule, fn in (("R1", R1), ("R2", R2)):
            new = s[:i] + s[i + 1:] + fn(d)
            if len(new) != 3 or not check_identity(new):
                continue
            add_form(new, f"{name}+{rule}@{i}")
# depth 2: rewrite a 3-term form by R1/R2 on one denominator (giving 4 terms), then merge two
# equal denominators (1/d+1/d = 1/(d/2)) back to 3 terms; only identity-checked triples are kept
base = list(forms.keys())
for key in base:
    for i, d in enumerate(key):
        for fn in (R1, R2):
            new4 = list(key[:i]) + list(key[i + 1:]) + fn(d)
            # merge a pair of terms that are equal (1/d+1/d = 1/(d/2)) -> reduces count to 3
            for a, b in itertools.combinations(range(len(new4)), 2):
                if norm(new4[a]) == norm(new4[b]):
                    red = [new4[k] for k in range(len(new4)) if k not in (a, b)] + [pscale(F(1, 2), new4[a])]
                    if len(red) == 3 and check_identity(red):
                        add_form(red, f"{key}->merge")

def integral_mod(triple, L):
    """residues n mod L at which every denominator is an integer (for n = r + kL, k large),
    checked on representatives in [L, 2L) to avoid small-n artefacts. Positivity assumed for n>=L."""
    ok = []
    for r in range(L):
        n = r + 2 * L
        good = True
        for d in triple:
            v = ev(d, n)
            if v.denominator != 1 or v <= 0:
                good = False; break
        if good:
            ok.append(r)
    return ok

L = 840
rows = []
cover = {"mod4": set(), "mod8": set(), "mod24": set()}
for key, origin in forms.items():
    res = integral_mod(key, L)
    rows.append({"origin": origin, "terms": ["(" + " + ".join(f"{c}*n^{i}" for i, c in enumerate(d) if c != 0) + ")" for d in key],
                 "integral_residues_mod_840": len(res), "sample": res[:12]})
    for r in res:
        cover["mod4"].add(r % 4); cover["mod8"].add(r % 8); cover["mod24"].add(r % 24)

print("forms (distinct 3-term triples):", len(forms))
print("forms with nonempty integrality domain:", sum(1 for r in rows if r["integral_residues_mod_840"]))
print("residues mod 4 covered by some form:", sorted(cover["mod4"]))
print("residues mod 8 covered:", sorted(cover["mod8"]))
print("residues mod 24 covered (count):", len(cover["mod24"]), sorted(cover["mod24"]))
# explicit check of n = 1 mod 4 classes
ok1 = {}
for key, origin in forms.items():
    for r in integral_mod(key, L):
        if r % 4 == 1:
            ok1.setdefault(origin, []).append(r)
print("forms integral on some n = 1 mod 4 residue:", len(ok1))
json.dump({"n_forms": len(forms), "rows": rows, "covered_mod4": sorted(cover["mod4"]),
           "covered_mod8": sorted(cover["mod8"]), "covered_mod24": sorted(cover["mod24"]),
           "mod4_1_hits": {k: v[:10] for k, v in ok1.items()}},
          open("data/z52b/pass2/NC0/sub/Z1181_egraph.json", "w"), indent=0)
