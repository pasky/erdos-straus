# review_r236_misc.py — R236 from-scratch side checks for SIGN_FIELDS §1.
# (a) non-trivial offsets k <= 300 (Lemma 1.1); (b) n_s mod 840 vs Mordell's hard classes; (c) integer square points
# 4^l + k = s^2 (l >= 0) and 1 + k 4^a = s^2 (a >= 1); (d) non-D certificate classes contain no square residue
# (T1 consistency); (e) independent ES solutions for s <= 10 for all 13 offsets.
import json, glob, math
import sympy as sp
from review_r236_cert import es_small

HARD = {1, 121, 169, 289, 361, 529}
ks = [k for k in range(1, 301, 2) if k % 8 == 1 and (1 + k) % 3 == 1]
print('(a) nontrivial k:', ks, len(ks))
for k in ks:
    res = sorted({(4 ** s + k) % 840 for s in range(2, 14)})
    hard = sorted(s % 6 for s in range(2, 8) if (4 ** s + k) % 840 in HARD)
    print('(b) k=%d n mod 840: %s; hard s mod 6: %s' % (k, res, hard))
for k in ks:
    pts = [(l, 4 ** l + k) for l in range(0, 60) if sp.ntheory.primetest.is_square(4 ** l + k)]
    neg = [(a, 1 + k * 4 ** a) for a in range(1, 60) if sp.ntheory.primetest.is_square(1 + k * 4 ** a)]
    print('(c) k=%d square points l>=0: %s ; l<0: %s' % (k, pts, neg))
for f in sorted(glob.glob('data/z8/*.json')):
    C = json.load(open(f))
    for cl in C['classes']:
        if cl['fam'] == 'D':
            continue
        M, r = cl['M'], cl['r']
        # r is a square mod M (odd part, and mod 2-power) iff some s with s^2 ≡ r (M); exhaustive over s mod M
        sq = any((s * s - r) % M == 0 for s in range(M))
        assert not sq, (f, M, r)
print('(d) no non-D class is a square class mod M: OK')
for k in ks:
    out = []
    for s in range(0, 11):
        n = 4 ** s + k
        sol = es_small(n)
        assert sol is not None, (k, s, n)
        out.append(s)
    print('(e) k=%d: ES solution found independently for s = 0..10' % k)
