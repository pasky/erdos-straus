#!/usr/bin/env python3
"""Independent referee check: direct divisor ratios, no manuscript code imports.
Run: ulimit -v 8000000; timeout 120s uv run --no-project reviews/z51-forcing-r1-astra-check.py
"""
from collections import Counter
from math import isqrt
from pathlib import Path

LO, HI = 10**6, 10**6 + 30000
prime = bytearray(b'\x01') * (HI + 1)
prime[:2] = b'\x00\x00'
for a in range(2, isqrt(HI) + 1):
    if prime[a]:
        start = a * a
        prime[start::a] = b'\x00' * ((HI - start) // a + 1)
qs = [q for q in range(3, 101, 4) if prime[q]]
trial = [s for s in range(2, isqrt((HI + 100) // 4) + 1) if prime[s]]
ps = [p for p in range(LO, HI + 1) if p % 8 == 1 and prime[p]]

def divisors(n):
    ds = [1]
    for s in trial:
        if s * s > n:
            break
        power, old = 1, ds[:]
        while n % s == 0:
            n //= s
            power *= s
            ds += [d * power for d in old]
    if n > 1:
        ds += [d * n for d in ds[:]]
    return ds

def ratios(ds, q):
    residues = {d % q for d in ds}
    assert 0 not in residues
    return {(a * pow(b, -1, q)) % q for a in residues for b in residues}

stored = {}
for line in Path('data/z51_forcing/win_1e6_perp.txt').read_text().splitlines():
    if line.startswith('#') or not line.strip():
        continue
    fields = line.split()
    p = int(fields[0])
    if LO <= p <= HI:
        assert p not in stored
        stored[p] = fields[4]
assert set(stored) == set(ps), ('prime coverage', set(stored) ^ set(ps))
counts, perq, mismatches = Counter(), {q: Counter() for q in qs}, []
for p in ps:
    for j, q in enumerate(qs):
        x = (p + q) // 4
        assert 4 * x == p + q
        ds = divisors(x)
        r2 = ratios(ds, q)
        rf = ratios(ds + [p * d for d in ds], q)
        forced = pow(q, (p - 1) // 2, p) == p - 1
        assert forced == (pow(x, (q - 1) // 2, q) == q - 1)
        ok2, okf = q - 1 in r2, q - 1 in rf
        assert not ok2 or okf
        actual = ('S' if ok2 else 'f' if okf else 'F') if forced else ('u' if ok2 else '.')
        if actual != stored[p][j]:
            mismatches.append((p, q, stored[p][j], actual))
        counts[actual] += 1
        perq[q][actual] += 1
        counts['full_success'] += okf
        counts['unforced_full_success'] += okf and not forced
print(f'interval=[{LO},{HI}], primes_1mod8={len(ps)}, windows={len(ps)*len(qs)}')
print('q=', qs)
print('pattern_counts=', {c: counts[c] for c in 'SfFu.'})
print('full_success=', counts['full_success'], 'unforced_full_success=', counts['unforced_full_success'])
print('mismatches=', len(mismatches), mismatches[:10])
print('q forced typeII_success full_success unforced typeII_success')
for q, c in perq.items():
    print(q, c['S']+c['f']+c['F'], c['S'], c['S']+c['f'], c['u']+c['.'], c['u'])
assert not mismatches
