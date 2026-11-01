"""Z1060: visits of quadratic recurrences n_k = a k^2 + b k + c (mod 840) to the Mordell hard set M (the classes where
the identity census does not cover ES): M = {1,121,169,289,361,529} mod 840 (repo: AMPLIFY_EXCEPTION.md (K2), y4_mordell_witness.md).
Exact structure: M = A8 x A3 x A5 x A7 with A8={1}, A3={1}, A5={1,4} (squares mod 5), A7={1,2,4} (squares mod 7) (CRT product set),
so for k uniform mod 840 the visit density is delta(f) = prod_q N_q(f)/q, N_q(f) = #{k mod q : f(k) mod q in A_q}.
Checks: (1) brute-force density over k mod 840 for random quadratics vs the product formula; (2) exact per-prime achievable
values; (3) which quadratics are trapped (delta = 1), and the minimum over NON-constant quadratics.
Output: data/z52b/pass2/NC0/sub/Z1060_visits.json.
Run: ulimit -v 4000000; uv run --with numpy python scripts/z52d_p2_NC0_Z1060.py
"""
import numpy as np, json, os, itertools, random
from fractions import Fraction as Fr
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
M840 = {1, 121, 169, 289, 361, 529}
A = {8: {1}, 3: {1}, 5: {1, 4}, 7: {1, 2, 4}}
# check the product description of M
prod = {r for r in range(840) if all((r % q) in A[q] for q in A)}
assert prod == M840, (sorted(prod), sorted(M840))
k840 = np.arange(840, dtype=np.int64)
def delta_brute(a, b, c):
    v = (a * k840 * k840 + b * k840 + c) % 840
    return float(np.mean([int(x) in M840 for x in v]))
def N_q(a, b, c, q):
    k = np.arange(q, dtype=np.int64); v = (a * k * k + b * k + c) % q
    return sum(1 for x in v if int(x) in A[q])
def delta_prod(a, b, c):
    d = Fr(1)
    for q in A:
        d *= Fr(N_q(a, b, c, q), q)
    return float(d)
random.seed(1)
val = []
for _ in range(3000):
    a, b, c = (random.randrange(840) for _ in range(3))
    val.append((delta_brute(a, b, c), delta_prod(a, b, c)))
mism = sum(1 for x, y in val if abs(x - y) > 1e-12)
out = {'product_structure_checked': True, 'brute_vs_product_mismatches_of_3000': mism}
# per-prime achievable N_q/q values over all (a,b,c) mod q (components are independent by CRT)
per = {}
for q in A:
    vals = set()
    for a, b, c in itertools.product(range(q), repeat=3):
        vals.add(Fr(N_q(a, b, c, q), q))
    per[q] = sorted(vals)
out['achievable_Nq_over_q'] = {str(q): [str(x) for x in per[q]] for q in per}
# exact minimum/maximum of delta over all quadratics mod 840 (product over components)
out['min_delta_over_all_quadratics'] = str(min(per[8][0] * per[3][0] * per[5][0] * per[7][0] for _ in [0]))
out['max_delta'] = str(max(per[8][-1] * per[3][-1] * per[5][-1] * per[7][-1] for _ in [0]))
# non-constant quadratics trapped in M? (delta = 1 requires N_q = q for all q)
trapped = []
for a, b, c in itertools.product(range(3), range(3), range(3)):
    pass
def trapped_mod(q):
    return [(a, b, c) for a, b, c in itertools.product(range(q), repeat=3) if N_q(a, b, c, q) == q]
for q in A:
    T = trapped_mod(q)
    out[f'trapped_mod_{q}_count'] = len(T)
    out[f'trapped_mod_{q}_nonconstant_count'] = sum(1 for (a, b, c) in T if (a % q, b % q) != (0, 0))
# example: k^2+2 avoids M entirely (never 1 mod 3)
out['delta_k2_plus_2'] = delta_brute(1, 0, 2)
out['example_k2_plus_2_mod3_values'] = sorted({(k * k + 2) % 3 for k in range(3)})
json.dump(out, open(ROOT + '/data/z52b/pass2/NC0/sub/Z1060_visits.json', 'w'), indent=1)
print(json.dumps({k: v for k, v in out.items() if k != 'achievable_Nq_over_q'}, indent=1))
print({q: v[:6] for q, v in out['achievable_Nq_over_q'].items()})
