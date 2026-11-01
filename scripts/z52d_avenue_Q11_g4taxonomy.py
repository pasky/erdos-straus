"""z52d avenue Q11 (Z1444/Z1512/Z1596/Z1600/Z1608/Z1561): gate-G4 taxonomy at levels t = 4C for (★).
For primes p ≡ 1 (4), 1000 < p ≤ PMAX, and C = 1, 2, ...: D_C = subset products (with multiplicity) of the prime
factors of N = 4Cp+1 in G = (ℤ/4C)^×. Level C 'wins' iff −1 ∈ D_C (⟺ N has a divisor ≡ −1 mod 4C).
Reports: (a) least winning C and whether D_{C*} = G there ('covering regime') ; (b) for failures with C ≤ CMAX:
subgroup-type (−1 ∉ ⟨factors⟩) vs multiplicity poverty, split by ω; (c) for failures with ω ≥ 6: is D a union of cosets
of a non-trivial subgroup (non-trivial stabiliser)?  Run: timeout 60 python3 scripts/z52d_avenue_Q11_g4taxonomy.py"""
from math import gcd
from collections import Counter
PMAX, CMAX = 20000, 30
def factor(n):
    f = {}; d = 2
    while d * d <= n:
        while n % d == 0: f[d] = f.get(d, 0) + 1; n //= d
        d += 1
    if n > 1: f[n] = f.get(n, 0) + 1
    return f
def subset_products(f, m):
    S = {1}
    for q, e in f.items():
        r = q % m; new = set(S); x = 1
        for _ in range(e):
            x = x * r % m; new |= {s * x % m for s in S}
        S = new
    return S
def gen_subgroup(rs, m):
    H = {1}; frontier = [1]
    while frontier:
        h = frontier.pop()
        for r in rs:
            y = h * r % m
            if y not in H: H.add(y); frontier.append(y)
    return H
isprime = lambda n: n > 1 and all(n % d for d in range(2, int(n ** .5) + 1))
ps = [p for p in range(1001, PMAX, 4) if isprime(p)]
least = Counter(); cover_at_least = 0; fail_kind = Counter(); stab = Counter()
for p in ps:
    found = False
    for C in range(1, 301):
        m = 4 * C; f = factor(m * p + 1); D = subset_products(f, m)
        phi = m
        for q in factor(m): phi = phi // q * (q - 1)
        win = (m - 1) in D
        if win and not found:
            found = True; least[C] += 1; cover_at_least += (len(D) == phi)
        if C <= CMAX and not win:
            om = len(f); H = gen_subgroup([q % m for q in f], m)
            fail_kind[('subgroup' if (m - 1) not in H else 'poverty', min(om, 6))] += 1
            if om >= 6:
                st = [h for h in range(2, m) if gcd(h, m) == 1 and {h * d % m for d in D} == D]
                stab['nontrivial' if st else 'trivial'] += 1
        if found and C >= CMAX: break
    if not found: least['none<=300'] += 1
n = len(ps)
print(f'{n} primes ≡ 1 (4) in (1000, {PMAX}); least winning C: {sorted(least.items(), key=str)}')
print(f'D_C* = whole group at the least winning level: {cover_at_least}/{n}')
for om in range(1, 7):
    a, b = fail_kind[('subgroup', om)], fail_kind[('poverty', om)]
    if a + b: print(f'failures C ≤ {CMAX}, ω = {om}{"+" if om == 6 else ""}: subgroup-type {a}, multiplicity-poverty {b} ({b / (a + b):.0%})')
print('failures with ω ≥ 6, stabiliser of D:', dict(stab))
