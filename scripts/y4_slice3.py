"""O212 (BRAINSTORM/y4_catalogue): where do the failures of M/p sit relative to the least e-slices?
Type II slices need e = -p (mod M), Type I slices e = -p^{-1} (mod M). e in {1, 3}: (Z/e)^* = {+-1}, so the
slice event "-1 in Sigma_e(N)" is just "Sigma_e(N) nontrivial". Count failing primes (census files) by
(e0_II, e0_I) = least positive representatives.
Usage: PYTHONPATH=scripts uv run python scripts/y4_slice3.py"""
from collections import Counter
from y4_t1_numerators import fails
for M in range(5, 25):
    fl = fails(M)
    if not fl:
        continue
    c = Counter()
    ex = []
    for p in fl:
        e2 = (-p) % M
        e1 = (-pow(p, -1, M)) % M
        small = e2 in (1, 3) or e1 in (1, 3)
        c[small] += 1
        if small:
            ex.append((p, e2, e1))
    print(M, 'failures', len(fl), 'with a slice e<=3:', c[True], ex[:8])

# which M have an e in {1,3} slice (Type I or II) in EVERY unit class?
from math import gcd
full = []
for M in range(3, 200):
    cov = set()
    for r in range(1, M):
        if gcd(r, M) != 1:
            continue
        e2, e1 = (-r) % M, (-pow(r, -1, M)) % M
        if e2 in (1, 3) or e1 in (1, 3):
            cov.add(r)
    units = sum(1 for r in range(1, M) if gcd(r, M) == 1)
    if len(cov) == units:
        full.append(M)
print('M in [3,200) with an e<=3 slice in every unit class:', full)

# ES at p = 1 (mod 12): both e = 3 slices (Type II N=(p+3)/4, Type I N=(3p+1)/4) fail iff all prime factors = 1 mod 3
from sympy import primerange, primefactors
for X in (10**4, 10**5, 10**6):
    ps = [p for p in primerange(13, X) if p % 12 == 1]
    both = [p for p in ps if all(q % 3 == 1 for q in primefactors((p + 3) // 4))
            and all(q % 3 == 1 for q in primefactors((3 * p + 1) // 4))]
    print(f'p=1 mod 12 below {X}: {len(ps)}, both e=3 slices empty: {len(both)} ({len(both)/len(ps):.3f})', both[:6])
