"""NL7 falsifier screens for Proposition SG and for the explicit rule-failure primes.
 * no number in data/z58/screens/* (the (*)-zero primes, G*-zero primes, R8-zero primes, composite (*)-zeros) and no
   member of Z7 is of the form 16 s^4 + 1 with s ≡ ±18 (mod 126)   [F3/F4 for Prop SG]
 * the 12 R8-zero primes and the 14 (*)-zero primes: U7 words exist (re-witnessed here by letter search), i.e. the
   obstruction theorems do not conflict with U7 at the screens   [F2/F4]
"""
import sys, re
sys.path.insert(0, 'scripts')
from z69_nl7_lib import *
from sympy import integer_nthroot

def nums(fn):
    out = []
    for line in open(fn):
        if line.startswith('#'): continue
        m = re.findall(r'\d+', line)
        if m: out.append(int(m[0]))
    return out

Z7 = [105, 1465, 3865, 4545, 10305, 12145, 39361, 67425]
files = ['star_prime_zeros.txt', 'gstar_zeros.txt', 'r8_zeros_1e10.txt', 'composite_zeros_le8e6.txt']
allnums = {f: nums('data/z58/screens/' + f) for f in files}
allnums['Z7'] = Z7
for f, ns in allnums.items():
    hit = []
    for n in ns:
        if (n - 1) % 16 == 0:
            s, exact = integer_nthroot((n - 1) // 16, 4)
            if exact and s % 126 in (18, 108):
                hit.append(n)
    print(f"{f}: {len(ns)} numbers, in the SG family: {hit}")
for f in ('star_prime_zeros.txt', 'r8_zeros_1e10.txt'):
    res = []
    for n in allnums[f]:
        m = None
        for L in range(1, 200):
            w = words_with_letter(n, L)
            if w:
                m = (L, w[0]); break
        res.append((n, m))
    assert all(m is not None for _, m in res)
    print(f"{f}: every one of the {len(res)} primes has a U7 word; least letters: {sorted(set(m[0] for _, m in res))}; e.g. {res[-1]}")
