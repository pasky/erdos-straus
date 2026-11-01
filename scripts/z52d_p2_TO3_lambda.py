"""Pass-2 TO3 (Z0839/Z0840): five-slice / length-3 status of primes p = 1 mod 8 <= N (same hit-array logic as
scripts/dk_lambda_big.py, which the repo uses for lambda(p)<=3), cross-tabulated with U(p) from the base table.
Classes: 'interior' (length-3 interior word hit), 'boundary' (no interior hit, (p+1)/2 has a prime = 3 mod 4), 'fail'.
Writes data/z52b/pass2/TO3/lambda_results.json"""
import csv, json, math
import numpy as np
from scipy.stats import spearmanr
N = 200000
hit = bytearray(N + 1)
t = 2
while 4 * t - 4 <= N:
    u = 2
    while 2 * (t * u - 1) - u <= N:
        A = t * u - 1; v = 2
        while (n := v * A - u) <= N:
            if A % 4 == 0 or (t * v - 1) % 4 == 0 or t % 4 == 0 or u % 4 == 0 or v % 4 == 0:
                hit[n] = 1
            v += 1
        u += 1
    t += 1
sieve = bytearray([1]) * (N + 2); sieve[0] = sieve[1] = 0
for i in range(2, math.isqrt(N + 1) + 1):
    if sieve[i]: sieve[i*i::i] = bytearray(len(sieve[i*i::i]))
def has3mod4(m):
    q = 3
    while q * q <= m:
        if m % q == 0:
            if q % 4 == 3: return True
            while m % q == 0: m //= q
        q += 2
    return m > 1 and m % 4 == 3
rows = list(csv.DictReader(open('data/z52b/pass2/TO3/base_primes_2e5.tsv'), delimiter='\t'))
U = {int(r['p']): float(r['U']) for r in rows}
cls = {}
for p in range(17, N + 1, 8):
    if not sieve[p]: continue
    if hit[p]: cls[p] = 'interior'
    elif has3mod4((p + 1) // 2): cls[p] = 'boundary'
    else: cls[p] = 'fail'
out = {'N': N, 'n_primes_1mod8': len(cls), 'counts': {c: sum(1 for v in cls.values() if v == c) for c in ('interior', 'boundary', 'fail')}}
for c in ('interior', 'boundary'):
    ps = [p for p, v in cls.items() if v == c and p > 1000]
    lu = np.array([math.log(U[p] / math.log(p) ** 2) for p in ps])
    out[f'median_logU_over_log2_{c}_p>1e3'] = round(float(np.median(lu)), 4)
    out[f'mean_U_over_log3_{c}_p>1e3'] = round(float(np.mean([U[p] / math.log(p) ** 3 for p in ps])), 4)
    out[f'n_{c}_p>1e3'] = len(ps)
# hardness of boundary-only primes
bp = [p for p, v in cls.items() if v == 'boundary']
out['boundary_only_primes_le2e5_first'] = bp[:15]
out['boundary_only_count'] = len(bp)
top = sorted(cls, key=lambda p: U[p] / math.log(p) ** 3)[:12]
out['hardest12_U_over_log3_class'] = [(p, cls[p]) for p in top]
json.dump(out, open('data/z52b/pass2/TO3/lambda_results.json', 'w'), indent=1)
print(json.dumps(out, indent=1))
