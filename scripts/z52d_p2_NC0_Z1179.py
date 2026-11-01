#!/usr/bin/env python3
"""Z1179 (CEGIS-style identity synthesis, first step).

Template language: P_i(n) = (a n^2 + b n + c)/d with a,b,c in [-3,3], d in {1,2,4}.
Candidate: a pair (P1,P2); P3 is forced by 4/n = 1/P1 + 1/P2 + 1/P3, i.e.
  P3 = n P1 P2 / (4 P1 P2 - n (P1 + P2)),
accepted only if the division is exact and the quotient is again a template polynomial.
This is the 'verifier' step: exact polynomial arithmetic (Fractions), no sampling.
Counterexample step: an accepted identity is only a rational-function identity; its
integrality domain is then tested on n = 24k+1 (the residue class of the item) and n = 3 mod 4.
"""
import itertools, json, sys
from fractions import Fraction as F

def pmul(a, b):
    r = [F(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            r[i + j] += x * y
    return r

def padd(a, b):
    n = max(len(a), len(b))
    a = a + [F(0)] * (n - len(a)); b = b + [F(0)] * (n - len(b))
    return [x + y for x, y in zip(a, b)]

def trim(a):
    a = list(a)
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a

def pdivmod(num, den):
    num = trim(num); den = trim(den)
    if len(num) < len(den):
        return [F(0)], num
    q = [F(0)] * (len(num) - len(den) + 1)
    r = list(num)
    while len(r) >= len(den) and any(x != 0 for x in r):
        c = r[-1] / den[-1]; k = len(r) - len(den)
        q[k] = c
        for i, y in enumerate(den):
            r[i + k] -= c * y
        r = r[:-1]
    r = trim(r) if r else [F(0)]
    return trim(q), r

def is_zero(a):
    return all(x == 0 for x in a)

# template set: coefficients (c, b, a) for c + b n + a n^2 (ascending order)
templates = []
seen = set()
for a, b, c, d in itertools.product(range(-3, 4), range(-3, 4), range(-3, 4), [1, 2, 4]):
    poly = [F(c, d), F(b, d), F(a, d)]
    if all(x == 0 for x in poly):
        continue
    key = tuple(poly)
    if key in seen:
        continue
    seen.add(key)
    templates.append(poly)

def evalp(p, n):
    return sum(c * n ** i for i, c in enumerate(p))

def in_template_set(q):
    # each coefficient must be k/d with d in {1,2,4} and |k| <= 3
    for c in trim(q):
        if not any((c * d).denominator == 1 and abs(c * d) <= 3 for d in (1, 2, 4)):
            return False
    return True

# n factor: polynomial n = [0,1]
N = [F(0), F(1)]
found = []
n_checked = 0
sols = []
for i in range(len(templates)):
    P1 = templates[i]
    if is_zero(P1):
        continue
    for j in range(i, len(templates)):
        P2 = templates[j]
        if is_zero(P2):
            continue
        n_checked += 1
        num = pmul(N, pmul(P1, P2))
        den = padd(pmul([F(4)], pmul(P1, P2)), [-x for x in pmul(N, padd(P1, P2))])
        if is_zero(trim(den)):
            continue
        q, r = pdivmod(num, den)
        if not is_zero(r):
            continue
        q = trim(q)
        if len(q) > 3:
            continue
        q = q + [F(0)] * (3 - len(q))
        if not in_template_set(q):
            continue
        # verify exactly on 9 points (degree of identity <= 6)
        ok = True
        for nn in range(2, 11):
            lhs = F(4, nn)
            if any(evalp(t, nn) == 0 for t in (P1, P2, q)):
                ok = False; break
            rhs = 1 / F(evalp(P1, nn)) + 1 / F(evalp(P2, nn)) + 1 / F(evalp(q, nn))
            if lhs != rhs:
                ok = False; break
        if ok:
            sols.append((P1, P2, q))

def fmt(p):
    return "(" + " + ".join(f"{c}*n^{i}" for i, c in enumerate(p) if c != 0) + ")"

# integrality domain on n in class: all three P_i integers, positive
def domain(P, mod):
    ok = []
    for n in range(2, mod):
        vals = [evalp(p, n) for p in P]
        if all(v.denominator == 1 and v > 0 for v in vals):
            ok.append(n)
    return ok

out = []
for P1, P2, P3 in sols:
    dom = [n for n in range(2, 400) if all(evalp(p, n).denominator == 1 and evalp(p, n) > 0 for p in (P1, P2, P3))]
    out.append({"P": [[str(c) for c in P1], [str(c) for c in P2], [str(c) for c in P3]],
                "text": [fmt(P1), fmt(P2), fmt(P3)],
                "integral_positive_n_below_400": dom[:40],
                "n_in_1mod24": [n for n in dom if n % 24 == 1][:10]})

# drop degenerate identities: a P_i proportional to n (then 1/P_i = c/n) or two P_i with
# P_i + P_j == 0 (their reciprocals cancel), or P_i constant
def degenerate(P):
    Ps = [[F(x) for x in p] for p in P]
    for p in Ps:
        if trim(p)[0] == 0 and len(trim(p)) == 2:
            return True          # c*n
        if len(trim(p)) == 1:
            return True          # constant
    for i in range(3):
        for j in range(i + 1, 3):
            if all(x == 0 for x in padd(Ps[i], Ps[j])):
                return True
    return False
nontriv = [o for o in out if not degenerate(o["P"])]
print("nontrivial raw:", len(nontriv))
uniq = {}
for o in nontriv:
    key = tuple(sorted(o["text"]))
    uniq.setdefault(key, o)
res = list(uniq.values())
print(f"templates={len(templates)} pairs_checked={n_checked} exact_identities_raw={len(sols)} nontrivial_unique={len(res)}")
for o in res[:40]:
    print(o["text"], "| integral n<400 (first):", o["integral_positive_n_below_400"][:12], "| n≡1 mod 24:", o["n_in_1mod24"][:5])
json.dump({"templates": len(templates), "pairs_checked": n_checked, "raw": len(sols), "nontrivial_unique": len(res), "identities": res},
          open("data/z52b/pass2/NC0/sub/Z1179_cegis.json", "w"), indent=1)
