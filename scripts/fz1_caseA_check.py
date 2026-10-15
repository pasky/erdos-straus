"""fz1_caseA_check.py (O220): every Case A route of fz1_caseA.py, separately, against exact unfiltered k = 1 Case A counts
(fz1_caseA_enum q AMAX 0 0 output; constant-E patterns lam = be = ka = 0 skipped). usage: fz1_caseA_check.py q file"""
import sys, fz1_caseA as M
from math import factorial
q = int(sys.argv[1]); Ns = lambda d: 1 if d <= 0 else q**d - q**(d - 1)
EXACT = {}
for l in open(sys.argv[2]):
    f = l.split(); EXACT[tuple(map(int, f[1:5]))] = int(f[5])
src = open(M.__file__).read()
# rebuild the per-pattern route list by running run() with an EX hook that records min(B) is not enough; recompute B here
import re
ns = {}
code = src[src.index("    @lru_cache(None)\n    def cop"):src.index("    tot = Fr(0)")]
exec("from functools import lru_cache\nfrom math import comb\ndef mk(q):\n" + code + "    return clsr\n", ns)
clsr = ns['mk'](q); viol = 0; n = 0
for (al, la, be, ka), c in EXACT.items():
    if la + be + ka == 0: continue
    f = al - be - ka; ze = max(f, be) - la
    B = [2 * Ns(la) * Ns(be) * Ns(ka), 4 * Ns(la) * Ns(ka) * Ns(f),
         4 * Ns(be) * Ns(ka) * clsr(max(al, 2 * be + ka), la + be + ka, be + ka, 1),
         2 * Ns(la) * Ns(be) * clsr(al + la, la + be + ka, la + be, 1),
         2 * (q - 1) * q**ze * (factorial(al) // (factorial(be) * factorial(ka) * factorial(f))),
         4 * (q - 1) * q**ze * Ns(la) * Ns(ka)]
    n += 1
    for i, b in enumerate(B):
        if c > b: viol += 1; print('VIOL', al, la, be, ka, c, 'route', i, b)
print(f'q={q}: patterns {n}, route violations {viol}')
