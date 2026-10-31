#!/usr/bin/env python3
"""z52b pass1 U06 — Z2006 / Z2879: Frobenius number of 3-generated semigroups vs ES words n = tuv-u-v.
Frobenius F(S) = largest integer not in <gens> (brute force, gcd must be 1).
Z2006: S = <tu, tv, u+v> with 4 | t. Question: does F(S) equal tuv-u-v (ES word value)?
Z2879: scan a,b,c <= 50 for F(<a,b,c>) = tuv-u-v for some t,u,v >= 2 (any families)."""
import math, json
def frob(gens):
    g = math.gcd(*gens)
    if g != 1: return None
    gens = sorted(set(x for x in gens if x > 0))
    lim = gens[0] * gens[-1] + 2 * max(gens) + 10
    rep = bytearray(lim + 1); rep[0] = 1
    for x in range(1, lim + 1):
        rep[x] = any(x >= a and rep[x - a] for a in gens)
    # largest non-representable
    for x in range(lim, -1, -1):
        if not rep[x]: return x
    return -1
res = {"z2006": [], "z2879_matches": []}
hits = tot = 0
for t in range(2, 13):
    for u in range(2, 13):
        for v in range(2, 13):
            if math.gcd(u, v) != 1: continue
            F = frob([t * u, t * v, u + v])
            if F is None: continue
            tot += 1
            if F == t * u * v - u - v:
                hits += 1
                res["z2006"].append((t, u, v))
print("Z2006: <tu,tv,u+v> with gcd=1: total", tot, "F = tuv-u-v:", hits, res["z2006"][:10])
# Z2879: which three-generator Frobenius numbers equal some tuv-u-v (t,u,v>=2)?
targets = {}
for t in range(2, 30):
    for u in range(2, 30):
        for v in range(2, 30):
            targets.setdefault(t * u * v - u - v, []).append((t, u, v))
found = 0; examples = []
for a in range(3, 51):
    for b in range(a + 1, 51):
        for c in range(b + 1, 51):
            F = frob([a, b, c])
            if F is not None and F in targets and F > 0 and found < 10000:
                found += 1
                if len(examples) < 8: examples.append(((a, b, c), F, targets[F][0]))
print("Z2879: triples a<b<c<=50 with F(<a,b,c>) equal to some tuv-u-v (value<=~2e4): ", found, examples)
json.dump({"tot": tot, "hits": hits, "z2006_hits": res["z2006"][:50], "z2879_found": found, "z2879_examples": examples},
          open("data/z52b/pass1/U06/frob_z2006_z2879.json", "w"), indent=0)
