"""Z0342: 4/p = 1/x+1/y+1/z with x,y,z in Z[sqrt2], x and its conjugate x' both >= 1 (real and conjugate embedding),
bounded by x<=B (real embedding) and x'<=B. Exact arithmetic: 1/(a+b r2) = (a-b r2)/(a^2-2b^2).
Reports: which primes p<=PMAX admit such a triple; how many triples use a non-rational element; sanity on Z-solutions."""
import sys, json, math
from fractions import Fraction as F
from itertools import combinations_with_replacement as cwr
B = int(sys.argv[1]) if len(sys.argv) > 1 else 30
PMAX = int(sys.argv[2]) if len(sys.argv) > 2 else 300
S = []
r2 = math.sqrt(2)
for b in range(-B, B + 1):
    for a in range(-2 * B, 2 * B + 1):
        x = a + b * r2; xc = a - b * r2
        if 1 <= x <= B and 1 - 1e-12 <= xc <= B:
            N = a * a - 2 * b * b
            if N == 0: continue
            S.append((x, a, b, N))
import os
if os.environ.get('ZONLY'): S = [e for e in S if e[2] == 0]
S.sort()
print('elements', len(S))
def is_prime(n): return n > 1 and all(n % q for q in range(2, int(n**0.5) + 1))
targets = {p: F(4, p) for p in range(5, PMAX + 1) if p % 4 == 1 and is_prime(p)}
hit = {}
# two-term sums cache: value -> (x,y) list; then check 4/p - 1/z
pairs = {}
for i, (xv, a1, b1, N1) in enumerate(S):
    for j in range(i, len(S)):
        xw, a2, b2, N2 = S[j]
        # rational test on sum of two: coefficient of sqrt2 must be cancelled by z; keep exact as pair
        s_rat = F(a1, N1) + F(a2, N2); s_irr = F(b1, N1) + F(b2, N2)
        pairs.setdefault((s_rat, s_irr), (i, j))
for p, t in targets.items():
    found = None
    for k, (xv, a, b, N) in enumerate(S):
        rem_rat = t - F(a, N); rem_irr = F(b, N)
        key = (rem_rat, rem_irr)
        if key in pairs:
            i, j = pairs[key]
            found = (S[i][1:3], S[j][1:3], (a, b))
            break
    if found: hit[p] = found
ok = sorted(hit); miss = [p for p in targets if p not in hit]
irr = [p for p in ok if any(e[1] != 0 for e in hit[p])]
res = dict(B=B, PMAX=PMAX, n_primes=len(targets), n_with_Z2_triple=len(ok), n_with_genuinely_irrational_triple=len(irr), missing_irr_example=[p for p in ok if p not in irr][:5], missing=miss[:40], n_missing=len(miss),
           example=(ok[0], hit[ok[0]]) if ok else None)
print(json.dumps(res, default=str, indent=1))
json.dump(res, open(f'data/z52b/pass1/U04/zsqrt2_B{B}_P{PMAX}' + ('_Zonly' if os.environ.get('ZONLY') else '') + '.json', 'w'), default=str, indent=1)
