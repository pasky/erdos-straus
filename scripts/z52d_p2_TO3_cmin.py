"""Fix round TO3 (Z0775, Z0853, Z0761 support): C_min(p) = min{C : some R-word has t = 4C} for primes 1 mod 4 up to 1e8
(from the binary minwords dump /tmp/z52/big/minwords1e8.bin, same logic as scripts/z52b_fingerprint_minwords.c).
Z0853: empirical P(C_min > c) vs the independence product prod_{C<=c}(1-P(E_C)), with E_C(p) = [4Cp+1 has a divisor
= -1 mod 4C] (= existence of an R-word with t=4C, see the item) computed on primes <= 2e5. Writes cmin_results.json"""
import json, math
import numpy as np
from sympy import divisors
N = 10**8
MW = np.memmap('/tmp/z52/big/minwords1e8.bin', dtype=np.uint32, mode='r', shape=(N + 1, 3))
sieve = np.ones(N + 1, dtype=bool); sieve[:2] = False
for i in range(2, int(N ** .5) + 1):
    if sieve[i]: sieve[i * i::i] = False
P1 = np.nonzero(sieve)[0]; P1 = P1[P1 % 4 == 1]
cm = np.asarray(MW[P1, 0]).astype(np.int64)
out = {'n_primes_1mod4_le1e8': int(len(P1)), 'n_no_word': int((cm == 0).sum()),
       'cmin_hist_head': {int(k): int(v) for k, v in zip(*np.unique(cm[cm > 0], return_counts=True)) if k <= 12}}
mx = {}
for X in [10**3, 10**4, 10**5, 10**6, 10**7, 10**8]:
    s = P1 <= X
    mx[X] = dict(max=int(cm[s].max()), argmax=int(P1[s][np.argmax(cm[s])]), frac_cmin_gt3=round(float((cm[s] > 3).mean()), 5))
out['max_cmin_by_X'] = mx
# Z0853 independence test on primes <= 2e5
ps = [int(q) for q in P1 if q <= 200000]
pc = dict(zip([int(q) for q in P1], cm.tolist()))
E = np.zeros((len(ps), 20), dtype=bool)
for i, p in enumerate(ps):
    for C in range(1, 21):
        n = 4 * C * p + 1
        E[i, C - 1] = any(d % (4 * C) == 4 * C - 1 for d in divisors(n))
PE = E.mean(axis=0)
cms = np.array([pc[p] for p in ps])
tail = {}
for c in range(1, 21):
    emp = float((cms > c).mean())
    ind = float(np.prod(1 - PE[:c]))
    tail[c] = dict(emp_P_Cmin_gt_c=round(emp, 5), indep_prod=round(ind, 5))
out['Z0853_tail_vs_independence_p<=2e5'] = tail
out['Z0853_P_E_C'] = {C: round(float(PE[C - 1]), 4) for C in range(1, 21)}
# check: E_C(p) agrees with Cmin (min C with E_C true) on these primes
minC = np.array([next((C for C in range(1, 21) if E[i, C - 1]), 0) for i in range(len(ps))])
out['check_Cmin_vs_E_C_agreement_fraction'] = round(float((minC == np.minimum(cms, 21)).mean()), 4)
out['check_agreement_note'] = 'compares min{C<=20: E_C} with C_min (C_min > 20 counted as 21 -> excluded from equality if any)'
json.dump(out, open('data/z52b/pass2/TO3/cmin_results.json', 'w'), indent=1)
for k, v in out.items(): print(k, str(v)[:600])
