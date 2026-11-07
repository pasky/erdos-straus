#!/usr/bin/env python3
"""z62 INVERSE: consistency check of Lemma 2 / Cor 3 on the census files: at u, C in {1,2,3,6} no slice is 'S'
(starved) or 'Q' (non-real kill); for primes p = 1 (24) failing u-slices u = 1, 2 and failing C-slice C = 1 are 'B'."""
import sys, collections
bad = collections.Counter(); seen = collections.Counter()
for fn in sys.argv[1:]:
    for l in open(fn):
        if l.startswith('#'): continue
        n, tag, us, cs = l.split()[:4]; n = int(n)
        for k in (1, 2, 3, 6):
            for fam, s, lim in (('u', us, (n + 1) // 3), ('C', cs, (n + 3) // 4)):
                if k > lim: continue
                seen[(fam, k)] += 1
                if s[k - 1] in 'SQ': bad[('SQ', fam, k, tag)] += 1
        if n % 24 == 1 and tag != 'Q':
            for fam, s, ks in (('u', us, (1, 2)), ('C', cs, (1,))):
                for k in ks:
                    if s[k - 1] not in 'hB': bad[('notB', fam, k, tag, n % 24)] += 1
print('slices checked', dict(seen)); print('violations', dict(bad))
