"""Failure sets of restricted-ES variants (columns of z52b_fingerprint_variants.c) at primes ≤ 1e5 and all n ≤ 3000; OEIS lookups."""
import numpy as np, json, sys, os
sys.path.insert(0, os.path.dirname(__file__))
from z52b_fingerprint_oeis import lookup
names = ['0 even', '1 even', '2 even', '3 even (all even)', 'primitive gcd=1', 'x,y | z', 'x | y', 'isosceles x=y or y=z',
         'all squarefree', 'z <= n^2', 'z <= n^1.5', 'some power of 2', 'x or y prime', 'some coprime pair', 'no denominator div by 3', 'some denominator div by 4']
A = np.loadtxt('data/z52b/raw/var_pr_1e5.txt', dtype=np.int64); B = np.loadtxt('data/z52b/raw/var_all_3000.txt', dtype=np.int64)
out = {}
for i, nm in enumerate(names):
    c = 2 + i
    fp = A[A[:, c] == 0, 0]; fa = B[B[:, c] == 0, 0]
    p1 = A[(A[:, 0] % 4 == 1)]
    frac = float((p1[:, c] > 0).mean())
    lastp = int(fp.max()) if len(fp) else None
    ratio = float(np.mean(p1[p1[:, 0] > 1000, c] / p1[p1[:, 0] > 1000, 1]))
    rec = dict(n_fail_primes=int(len(fp)), last_fail_prime=lastp, fail_primes_head=fp[:30].tolist(), fail_primes_tail=fp[-10:].tolist(),
               n_fail_all3000=int(len(fa)), fail_all_head=fa[:30].tolist(), frac_p1mod4_ok=frac, mean_share_of_U=ratio)
    if 4 <= len(fp) and len(fp) < 5000:
        rec['oeis_primes'] = lookup(fp[:20].tolist())
    seqp = A[:, c]
    rec['oeis_counts_primes'] = lookup(seqp[:20].tolist())
    out[nm] = rec
    print(nm, '| #fail primes', len(fp), 'last', lastp, '| head', fp[:15].tolist(), '| all-n fails', len(fa), fa[:12].tolist(), '| share', round(ratio, 3),
          '| oeis', [h[0] for h in rec.get('oeis_primes', [])][:2], [h[0] for h in rec['oeis_counts_primes']][:2], flush=True)
json.dump(out, open('data/z52b/variants.json', 'w'), indent=1)
