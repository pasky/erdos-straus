"""Independent, bounded checks for the z49 sexp cross-model review.
No imports from the author's implementation. Finite checks, not asymptotic evidence.
Run: ulimit -v 8000000; timeout 120s uv run --no-project scripts/z49_sexp_xreview.py
"""
from fractions import Fraction
from itertools import combinations
from math import gcd, lcm, log, prod


def factors(n):
    out = {}
    p = 2
    while p * p <= n:
        while n % p == 0:
            out[p] = out.get(p, 0) + 1
            n //= p
        p += 1
    if n > 1:
        out[n] = 1
    return out


def phi(n):
    for p in factors(n):
        n = n // p * (p - 1)
    return n


def divisors(n):
    ds = [1]
    for p, e in factors(n).items():
        ds = [d * p**i for d in ds for i in range(e + 1)]
    return ds


# New check beyond the author's decomposition tests: both extra CRT classes
# in the pair-sum proof, including nontrivial smooth parts and repeated atoms.
rough_primes = (11, 13, 17, 19, 23, 29, 31)
rough = [r for mask in range(1 << len(rough_primes))
         if (r := prod(p for i, p in enumerate(rough_primes) if mask >> i & 1)) <= 20000]
endpoints = sorted((s * r, s, r) for s in (1, 5, 7, 25, 35)
                   for r in rough if s * r <= 20000)
family = [(u, v, s, t, r, w)
          for u, s, r in endpoints if 30 <= u <= 600 and u % 4 == 3
          for v, t, w in endpoints if 1000 <= v <= 20000 and gcd(u, v) == 1]
print(f'pair-check allocation: {len(endpoints)} endpoints, {len(family)} events; pairs streamed')
checks = equal_sums = duplicates = mixed = 0
for z in (1, 2, 3, 4, 6, 8, 9, 11, 13, 17):
    live = [e for e in family if (z + e[0] + e[1]) % (e[2] * e[3]) == 0]
    delta = Fraction(0)
    for e, f in combinations(live, 2):
        u, v, s, t, r, w = e
        up, vp, sp, tp, rp, wp = f
        g, h, j, k = gcd(r, rp), gcd(w, wp), gcd(r, wp), gcd(w, rp)
        D = g * h * j * k
        if D == 1 or (u + v - up - vp) % D:
            continue
        a, b, c, d = r // (g*j), w // (h*k), rp // (g*k), wp // (h*j)
        assert all(gcd(x, y) == 1 for x, y in combinations((g, h, j, k), 2))
        assert lcm(r*w, rp*wp) == D*a*b*c*d
        assert (vp-v) % g == (vp-u) % k == (up-u) % h == (up-v) % j == 0
        assert gcd(h*j, tp) == gcd(g*k, sp) == 1
        # The c,d CRT constraints are reduced; coefficient inversions are valid.
        assert gcd(sp*g*k, h*j*tp) == gcd(tp*h*j, g*k*sp) == 1
        assert (z+u) % t == (z+v) % s == 0
        assert (z+up) % tp == (z+vp) % sp == 0
        if u+v == up+vp:
            equal_sums += 1
            assert u != up and h <= abs(u-up) and g*j*k <= u*up
        else:
            assert D <= abs(u+v-up-vp)
        duplicates += (r*w == rp*wp)
        mixed += (s*t*sp*tp > 1)
        delta += Fraction(1, phi(lcm(r*w, rp*wp)))
        checks += 1
    mu = sum((Fraction(1, phi(e[4]*e[5])) for e in live), Fraction(0))
    print(f'pair fibre z={z}: live={len(live)} mu={float(mu):.8f} Delta={float(delta):.8f}')
print(f'pair CRT assertions: {checks}; equal sums={equal_sums}; repeated atoms={duplicates}; smooth={mixed}')
assert checks and mixed

# The author's numerics do not compute FT. Enumerate it directly here and
# independently check its claimed domination of larger-endpoint harmonic loads.
H = 1000
for Y in (10, 30, 100):
    ps = [p for p in range(2, H+1) if factors(p) == {p: 1}]
    powers = {}
    for p in ps:
        if p > Y:
            break
        power = 1
        while power*p < Y:
            power *= p
        powers[p] = max(power, 8 if p == 2 else 1)
    Q = prod(powers.values())
    coords = [(p, powers.get(p, 1)*p) for p in ps if powers.get(p, 1)*p <= H]
    A = [gcd(a, Q) for a in range(H+1)]
    Bsets = [divisors(gcd(a+1, Q)) for a in range(H+1)]
    ft = {}
    long = {}
    for p, q in coords:
        first = tail = 0.0
        for a in range(1, H+1):
            if a % p == 0:
                continue
            for B in Bsets[a]:
                if p in powers and B % powers[p]:
                    continue
                AB = A[a]*B
                residue = ((a+1)//B * pow(A[a], -1, p)) % p
                low = (a+q+1+AB-1)//AB
                t = low + (residue-low) % p
                assert t > 0 and AB*t >= a+q+1
                assert (AB*t-a-1) % (B*p) == 0
                first += 1/(a*t)
                tail += log(2*H+1)/(a*p)
        ft[q], long[q] = first, tail
    actual = {q: 0.0 for _, q in coords}
    events = 0
    for v in range(2, H+1):
        B = A[v]
        for a in range(1, v):
            if gcd(a,v) != 1 or (a,v) in ((1,2),(2,3)):
                continue
            if (v+1) % A[a] or (a+1) % B:
                continue
            events += 1
            for p in factors(v):
                q = powers.get(p, 1)*p
                if v % q == 0:
                    actual[q] += A[a]*B/(a*v)
    for q in actual:
        assert actual[q] <= 2*(ft[q]+long[q])+1e-9
    worst = max(ft, key=lambda q: q*ft[q]/log(H)**2)
    ratio = max(actual[q]/(2*(ft[q]+long[q])) for q in actual)
    print(f'FT H={H} Y={Y}: {len(coords)} coordinates, {events} live edges; '
          f'max q*FT/L^2={worst*ft[worst]/log(H)**2:.8f} at q={worst}; '
          f'max actual/enlarged_bound={ratio:.8f}')

# At a prime cutoff the largest power strictly below Y is p^0=1.
# Exact enumeration catches the author's C checker's base-digit normalization.
Q = 2520  # Q(11)
residues = [1+Q*t for t in range(11) if gcd(1+Q*t, Q*11) == 1]
mean = Fraction(0)
positive = []
for v in range(2, 12):
    for a in range(1, v):
        if gcd(a,v) != 1 or (a,v) in ((1,2),(2,3)):
            continue
        hits = sum((n+a+v) % (a*v) == 0 for n in residues)
        if hits:
            positive.append((a,v,Fraction(hits,len(residues))))
            mean += Fraction(hits,len(residues))
assert mean == Fraction(1,2)
print(f'prime-cutoff exact CRT H=Y=11: S={mean}; live={positive}')

# Mandatory controls via the unique-smaller-neighbour enumeration.
hard = (193, 409, 577, 2521, 3361, 5569, 9601, 66529, 8813281)
for n in hard + tuple(m*m for m in range(3, 100, 2)):
    first = None
    odd_checked = 0
    for v in range(2, min(n, 10001)):
        a = (-n) % v
        if a == 0 or gcd(a*v, n) != 1 or (n+a+v) % (a*v):
            continue
        t = (n+a+v)//(a*v)
        cert = any(x % 4 == 0 for x in (a,v,t,t*a-1,t*v-1))
        if a % 2 and v % 2:
            assert cert == (a % 4 != 1 or v % 4 != 1)
            odd_checked += 1
        if n not in hard:
            assert not cert
        else:
            assert cert == (pow(a*v % n, (n-1)//2, n) == n-1)
        if cert and first is None:
            first = v
    if n in hard:
        print(f'control prime {n}: H4={first}, odd edges checked={odd_checked}')
print('49 odd-square controls: no coprime certificate edges')
for n in (17, 241):
    hits = 0
    for x in range((n+7)//8, 3*n//8+1):
        b, c = 8*x-n, n*x
        for y in range(max(x, c//b+1), 2*c//b+1):
            denom = b*y-c
            if c*y % denom == 0 and c*y//denom >= y:
                hits += 1
    assert hits == 0
    print(f'numerator-8 full three-term check n={n}: {hits} representations')
print('PASS: all independent finite assertions')
