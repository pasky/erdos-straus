"""Z1064: CRT covering radius / largest gaps for the simultaneous exclusions relevant to ES.
Exclusion family: for a modulus set S subset of {8,3,5,7} the excluded residues are E_S = { n : n mod q in A_q for all q in S }
with A_8={1}, A_3={1}, A_5={1,4}, A_7={1,2,4} (squares / hard classes; E_{8,3,5,7} = Mordell hard set M mod 840).
Parameter ranges: n = 4k+1 (primes p = 1 mod 4 are the only relevant ones).  For each S:
  - density of E_S among n = 1 mod 4 classes;
  - maximal run of consecutive k (n=4k+1 consecutive in the progression) lying in E_S (cyclic, period lcm);
  - covering radius R_S = max over k of the distance (in k) to the nearest k with 4k+1 NOT in E_S (search distance).
Output: data/z52b/pass2/NC0/sub/Z1064_gaps.json
Run: uv run --with numpy python scripts/z52d_p2_NC0_Z1064.py
"""
import numpy as np, json, os, itertools
from math import lcm
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
A = {8: {1}, 3: {1}, 5: {1, 4}, 7: {1, 2, 4}}
def period(S):
    return lcm(*[q for q in S], 1) if S else 1
out = {}
for r in range(1, 5):
    for S in itertools.combinations([8, 3, 5, 7], r):
        P = lcm(*S) * 4 // (1 if 4 % 1 == 0 else 1)  # period in k: n=4k+1 mod lcm(S) => k mod lcm(S)
        per = lcm(*S)  # n mod per determines membership; k runs over Z/per (since 4 is invertible mod odd q; mod 8 handled via n mod 8)
        # build membership of n = 4k+1 for k in 0..L-1 with L = lcm(S) * 2 (safe for mod 8 component)
        L = lcm(*S) * 2
        ks = np.arange(L, dtype=np.int64); n = 4 * ks + 1
        bad = np.ones(L, dtype=bool)
        for q in S:
            bad &= np.isin(n % q, list(A[q]))
        frac = float(bad.mean())
        # maximal cyclic run of bad k
        if bad.all():
            maxrun = None; radius = None
        else:
            # cyclic run length
            arr = np.concatenate([bad, bad]); best = 0; cur = 0
            for x in arr:
                cur = cur + 1 if x else 0; best = max(best, cur)
            maxrun = int(min(best, L))
            # covering radius: max over k of distance to nearest good k (cyclic)
            good = np.where(~bad)[0]
            d = np.full(L, L, dtype=np.int64)
            for g in good:
                dist = np.minimum(np.abs(ks - g), L - np.abs(ks - g))
                d = np.minimum(d, dist)
            radius = int(d.max())
        out['S=' + ','.join(map(str, S))] = dict(period_k=L, bad_density=round(frac, 6), max_bad_run_k=maxrun, covering_radius_k=radius,
                                                 bad_classes_mod_lcm=int(bad.sum()))
for kk, v in out.items(): print(kk, v)
json.dump(out, open(ROOT + '/data/z52b/pass2/NC0/sub/Z1064_gaps.json', 'w'), indent=1)
