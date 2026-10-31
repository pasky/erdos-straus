"""Z0081: global Legendre-sign patterns of ES solutions (x,y,z) mod small l, vs local possibilities.
Uses esols() from z52b_p1_U02_lib (validated against f4 U-data for n<3000). Primes p = 1 mod 4 up to 3000 (and all p<=3000)."""
import sys, json, itertools
sys.path.insert(0, 'scripts')
from z52b_p1_U02_lib import esols
from sympy import primerange

def leg(a, l):
    a %= l
    if a == 0: return 0
    return 1 if pow(a, (l-1)//2, l) == 1 else -1

out = {}
P = [p for p in primerange(5, 3001)]
for l in (3, 5, 7):
    obs = {}
    tot = 0
    for p in P:
        for (x, y, z) in esols(p):
            if any(v % l == 0 for v in (x, y, z)): continue
            key = tuple(sorted([leg(x, l), leg(y, l), leg(z, l)]))  # unordered pattern (x<=y<=z is ordering, so sort for symmetry)
            obs[key] = obs.get(key, 0) + 1
            tot += 1
    # local: all triples (u,v,w) of nonzero residues mod l with some residue-level realization of
    # 4/p = 1/x+1/y+1/z modulo l for p not 0 mod l: 4uvw = p(uv+vw+wu) (mod l), with (uvw) units.
    allowed = set()
    for p in P:
        if p % l == 0: continue
        for u, v, w in itertools.product(range(1, l), repeat=3):
            if (4*u*v*w - p*(u*v+v*w+w*u)) % l == 0:
                allowed.add(tuple(sorted([leg(u, l), leg(v, l), leg(w, l)])))
    out[l] = {'observed_counts': {str(k): v for k, v in sorted(obs.items())},
              'locally_allowed_sorted_patterns': sorted(str(k) for k in allowed),
              'missing_globally': sorted(str(k) for k in allowed if k not in obs), 'total': tot}
    print(l, out[l]['observed_counts'], 'missing:', out[l]['missing_globally'])
json.dump(out, open('data/z52b/pass1/U02/Z0081_signs.json', 'w'), indent=1)
