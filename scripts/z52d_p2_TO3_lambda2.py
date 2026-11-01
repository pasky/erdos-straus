"""Fix round TO3 (Z0840): lambda(p) = min{ r(p/A) : (A/p) = -1 } (DEDEKIND_ES Cor 4.6), r = HJ length (scripts/bsA_hjlen.py).
(1) brute-force check of the Cor 4.6 criterion lambda(p)=2 <=> (p+1)/2 has a prime factor = 3 mod 4, for primes p = 1 mod 8, p <= 3000;
(2) for all primes p = 1 mod 8 <= 2e5 (base table U): cross-tab of lambda in {2,3} against U/log^2 p and U/log^3 p quantiles.
Writes data/z52b/pass2/TO3/lambda2_results.json"""
import csv, json, math, sys
import numpy as np
from sympy import primerange, factorint
sys.path.insert(0, 'scripts')
from bsA_hjlen import hj_len
out = {}
def lam_brute(p):
    best = None
    for A in range(1, p):
        if pow(A, (p - 1) // 2, p) != p - 1: continue      # (A/p) = -1
        r = hj_len(p, A)
        if best is None or r < best: best = r
    return best
def crit2(p):
    m = (p + 1) // 2
    return any(q % 4 == 3 for q in factorint(m))
chk = []
for p in primerange(17, 3001):
    if p % 8 != 1: continue
    lb = lam_brute(p)
    chk.append((p, lb, 2 if crit2(p) else 3))
bad = [c for c in chk if c[1] != c[2]]
out['Z0840_criterion_check_p1mod8_le3000'] = dict(n=len(chk), mismatches=bad[:10], n_mismatch=len(bad),
                                                 lambda2_count=sum(1 for c in chk if c[1] == 2), lambda3_count=sum(1 for c in chk if c[1] == 3))
rows = list(csv.DictReader(open('data/z52b/pass2/TO3/base_primes_2e5.tsv'), delimiter='\t'))
U = {int(r['p']): float(r['U']) for r in rows}
ps = [p for p in U if p % 8 == 1 and p > 1000]
lam = {p: (2 if crit2(p) else 3) for p in ps}
for name, f in [('U_over_log2', lambda p: U[p] / math.log(p) ** 2), ('U_over_log3', lambda p: U[p] / math.log(p) ** 3)]:
    v2 = [f(p) for p in ps if lam[p] == 2]; v3 = [f(p) for p in ps if lam[p] == 3]
    out[f'Z0840_{name}_lambda2'] = dict(n=len(v2), median=round(float(np.median(v2)), 4), mean=round(float(np.mean(v2)), 4), min=round(float(min(v2)), 4))
    out[f'Z0840_{name}_lambda3'] = dict(n=len(v3), median=round(float(np.median(v3)), 4), mean=round(float(np.mean(v3)), 4), min=round(float(min(v3)), 4))
hard = sorted(ps, key=lambda p: U[p] / math.log(p) ** 3)[:30]
out['Z0840_hardest30_lambda'] = {'lambda2': sum(1 for p in hard if lam[p] == 2), 'lambda3': sum(1 for p in hard if lam[p] == 3)}
out['Z0840_hardest10'] = [(p, lam[p]) for p in hard[:10]]
json.dump(out, open('data/z52b/pass2/TO3/lambda2_results.json', 'w'), indent=1)
print(json.dumps(out, indent=1)[:2500])
