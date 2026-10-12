"""Small independent arithmetic checks for O157's technique-transfer triage.

Run: ulimit -v 4000000; timeout 600 env PYTHONPATH=scripts \
    OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 uv run python scripts/triage_tech.py
Only standard-library, bounded loops; no dense arrays or external factoring.
"""
from math import gcd, isqrt


def prime(n):
    return n >= 2 and all(n % d for d in range(2, isqrt(n) + 1))


def factors(n):
    out = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            out[d] = out.get(d, 0) + 1
            n //= d
        d += 1
    if n > 1:
        out[n] = 1
    return out


def witnesses(n):
    # B >= 1 implies (4AC-1) <= n+A, hence A <= (n+1)/3.
    return [(a, (n + a) // (4 * a * c - 1), c)
            for a in range(1, (n + 1) // 3 + 1)
            for c in range(1, (n + a + 1) // (4 * a) + 1)
            if (n + a) % (4 * a * c - 1) == 0]


for n in range(2, 151):
    triples = witnesses(n)
    ab = [(a, b) for a in range(1, (n + 1) // 3 + 1)
          for b in range(1, (n + 1) // 3 + 1)
          if (n + a + b) % (4 * a * b) == 0]
    assert sorted((a, b) for a, b, c in triples) == ab
    for a in range(1, (n + 1) // 3 + 1):
        for c in range(1, (n + a + 1) // (4 * a) + 1):
            q = 4 * a * c - 1
            assert ((n + a) % q == 0) == ((4 * c * n + 1) % q == 0)
    if isqrt(n) ** 2 == n and n % 2:
        assert not triples
print('Dual forms agree for 2 <= n <= 150; odd squares have no witnesses.')

p = 73
example = next((a, b, c) for a, b, c in witnesses(p)
               if (p + b) % (4 * a) != 0)
print('False common-frame congruence counterexample p=73, (A,B,C)=', example)

# Bounded exponent products need not equal the subgroup they generate.
for p in range(73, 2000, 24):
    if not prime(p):
        continue
    found = False
    for e in range(3, min(p, 120), 4):
        n = (p + e) // 4
        if gcd(n, e) != 1:
            continue
        fs = factors(n)
        products = {1}
        group = {1}
        for ell, v in fs.items():
            products = {a * pow(ell, t, e) % e
                        for a in products for t in range(-v, v + 1)}
            powers, x = {1}, ell % e
            while x != 1:
                powers.add(x)
                x = x * ell % e
            group = {a * b % e for a in group for b in powers}
        if e - 1 in group and e - 1 not in products:
            print('Subgroup counterexample:', 'p=', p, 'e=', e, 'N=', n,
                  'factors=', fs, 'bounded products=', sorted(products))
            found = True
            break
    if found:
        break
else:
    raise AssertionError('No subgroup counterexample in the prescribed range')

for d in range(2, 73):
    if pow((-d) % 73, 36, 73) == 1 and not any(
        (u := isqrt(73 - d * v * v)) ** 2 + d * v * v == 73
        for v in range(isqrt(73 // d) + 1)
    ):
        print('Representation-seed counterexample: p=73, d=', d,
              '; (-d/p)=1 but p != u^2+d*v^2.')
        break

# Independent complete small smoothness coverage, including q > N.
N = 1000
ps = [p for p in range(73, N + 1, 24) if prime(p)]
for beta in (None, 0.5, 0.4, 0.3, 0.25, 0.2):
    misses = 0
    for p in ps:
        good = any(beta is None or max(factors(4 * a * c - 1)) <= N ** beta
                   for a, b, c in witnesses(p))
        misses += not good
    print('Exact small coverage:', N, 'primes=', len(ps), 'beta=', beta,
          'uncovered=', misses)
