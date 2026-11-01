# z52d pass2 NC1 fix round 3: Z1479 quartic character of witnesses (d^{(p-1)/4} ∈ {±1,±i}), Z1438 Type-I counts over d ≤ 30,
# Z1409 energy landscape with B = 128 for small primes.
import numpy as np, math, json
from collections import defaultdict, Counter
from sympy import primerange, divisors
out = {}
W0 = defaultdict(list)
for line in open('/tmp/wit_1e6.txt'):
    p, C, d = map(int, line.split()); W0[p].append((C, d))
W = dict(W0)
allp = [p for p in primerange(5, 10**6) if p % 4 == 1]
# Z1479: quartic character of every witness d (all C ≤ 50): label by value of d^((p-1)/4) ∈ {1, -1, i, -i}; i = the root with i^2=-1
lab = Counter(); per_prime_kinds = Counter(); pr_with = 0
for p in allp:
    if not W.get(p): continue
    pr_with += 1
    ivals = set()
    for C, d in W[p]:
        v = pow(d % p, (p-1)//4, p)
        if v == 1: lab['1'] += 1
        elif v == p-1: lab['-1'] += 1
        else:
            ivals.add(v)   # the actual root of unity value (i or -i)
            lab['±i'] += 1
    per_prime_kinds[len(ivals)] += 1
    if len(ivals)==1: lab['primes_all_witnesses_same_quartic_value'] += 1
out['Z1479_quartic'] = {'primes_with_witness': pr_with, 'min_root_of_unity_value_example': None, 'witness_label_counts (value of d^((p-1)/4))': dict(lab),
    'primes by number of distinct values of d^((p-1)/4) among witnesses': dict(per_prime_kinds),
    'interpretation': 'every witness is a quadratic non-residue (Lemma B) so d^((p-1)/4) ∈ {±i}; the quartic character of d is the only remaining invariant'}
# Z1438: Type I (d≥1): f | p²+4c²d, f ≡ -p (mod 4cd); fraction of primes with a solution for some c ≤ 20, d ≤ 30 ; also which d needed
P3 = [p for p in primerange(5, 3000) if p % 4 == 1][:300]
hit_d1 = 0; hit_any = 0; dstat = Counter()
for p in P3:
    found = None
    for c in range(1, 21):
        for dd in range(1, 31):
            N = p*p+4*c*c*dd; mod = 4*c*dd
            for f in divisors(N):
                if f % mod == (-p) % mod:
                    found = (c, dd, f); break
            if found: break
        if found: break
    if found:
        hit_any += 1; dstat[found[1]] += 1
        if found[1] == 1: hit_d1 += 1
out['Z1438_typeI'] = {'primes': len(P3), 'frac_with_TypeI_solution_c<=20,d<=30': round(hit_any/len(P3), 3),
    'frac_with_d=1_only': round(hit_d1/len(P3), 3), 'smallest_d_found_histogram(top)': dstat.most_common(6)}
# Z1409 energy landscape, B = 128
land = {}
for p in [13, 17, 29, 37, 41]:
    B = 128; r = np.arange(1, B+1)
    X, Y, Z = np.meshgrid(r, r, r, indexing='ij')
    E = (4*X*Y*Z - p*(X*Y+Y*Z+Z*X)).astype(np.int64)**2
    zeros = int((E == 0).sum())
    vals_ = np.unique(E); nz = vals_[vals_ > 0]
    land[p] = {'zero_energy_states_x,y,z<=128': zeros, 'gap_first_nonzero_energy': int(nz[0]) if len(nz) else None,
               'min_nonzero_energy_states': int((E == nz[0]).sum()) if len(nz) else None}
out['Z1409_landscape_B128'] = land
print(json.dumps(out, indent=1, default=str))
