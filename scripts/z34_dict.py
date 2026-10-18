"""O264 goal 1: Type A (b = 1 line) vs Astra sources, via the slice residue c_g = -p^{-1} mod g.

Claims tested (HARD_PAIR.md §1):
 (A) Type A solutions (a,c,d) <-> slices g = 4cd-1 (g = 3 mod 4, gcd(g,p)=1) with c_g | h, h = (g+1)/4; c = c_g, d = h/c.
 (B) the Astra source at slice g exists  <=> c_g is a square unit mod g  (checked per prime factor of g).
 (C) an Astra source (q,m,s) is integral on arrival (x = sh/m^2 in Z) <=> m^2 | h <=> Type A with c = m^2.
Part 1 (all p = 1 (4) <= N): Type A by the pair form (B1_LINE Lemma 1.1), check identity, c == c_g, c | h,
   splitness of the slice, c perfect square; counts per p.
Part 2 (p <= N2): independent slice scan g <= 2p (c_g | h) must reproduce the Type A set exactly; independent
   Astra integral-source scan m <= sqrt((p+7)/12), divisors q | pm^2+1, q = -1 mod 4m^2, must equal the c-square subset.
usage: z34_dict.py N N2
"""
import sys
from math import isqrt, gcd
from fractions import Fraction

N, N2 = int(sys.argv[1]), int(sys.argv[2])
L = N + 2 * isqrt(N) + 10
spf = list(range(L + 1))
for i in range(2, isqrt(L) + 1):
    if spf[i] == i:
        for j in range(i * i, L + 1, i):
            if spf[j] == j:
                spf[j] = i


def fac(n):
    f = {}
    if n <= L:
        while n > 1:
            s = spf[n]; f[s] = f.get(s, 0) + 1; n //= s
        return f
    r = 2
    while r * r <= n:
        while n % r == 0:
            f[r] = f.get(r, 0) + 1; n //= r
        r += 1 if r == 2 else 2
    if n > 1:
        f[n] = f.get(n, 0) + 1
    return f


def divisors(f):
    ds = [1]
    for q, e in f.items():
        ds = [d * q ** k for d in ds for k in range(e + 1)]
    return ds


def is_sq_unit(c, g):
    """c a square unit mod g (g odd)."""
    if gcd(c, g) != 1:
        return False
    for q in fac(g):
        if pow(c % q, (q - 1) // 2, q) != 1:
            return False   # Hensel: odd q, unit square mod q lifts to q^e
    return True


def typeA(p):
    """all Type A solutions (a, c, d) via pairs {s,t}, st | p+s+t, 4 | st."""
    sols = set()
    for s in range(1, 2 + isqrt(p + 1)):
        for t in divisors(fac(p + s)):
            if t <= s or (s * t) % 4:
                continue
            if (p + s + t) % (s * t):
                continue
            D, g = (s, t) if s % 4 == 0 else (t, s)
            d = D // 4
            c = (p + s + t) // (s * t)
            w = 4 * c * d - 1
            assert (c * p + 1) % w == 0
            a = (c * p + 1) // w
            sols.add((a, c, d))
    return sols


isprime = lambda n: n > 1 and spf[n] == n
stats = dict(primes=0, sols=0, split=0, nonsplit=0, csq=0, fails=[], noint=[], c1=0)
for p in range(5, N + 1, 4):
    if not isprime(p):
        continue
    stats['primes'] += 1
    S = typeA(p)
    if not S:
        stats['fails'].append(p)
    nsq = 0
    for (a, c, d) in S:
        assert Fraction(1, a * d) + Fraction(1, a * c * d * p) + Fraction(1, c * d * p) == Fraction(4, p)
        g = 4 * c * d - 1; h = c * d
        assert gcd(g, p) == 1 and (-pow(p, -1, g)) % g == c and h % c == 0
        if is_sq_unit(c, g):
            stats['split'] += 1
        else:
            stats['nonsplit'] += 1
        r = isqrt(c)
        if r * r == c:
            nsq += 1
            q, m, s_ = g, r, a        # Astra source (q, m, s), integral
            assert q * s_ == p * m * m + 1 and h % (m * m) == 0
            assert Fraction(s_ * h, m * m) == a * d
    stats['sols'] += len(S); stats['csq'] += nsq
    if S and nsq == 0:
        stats['noint'].append(p)
    if p <= N2:
        # independent slice scan
        G = set()
        for g in range(3, 2 * p + 1, 4):
            if g % p == 0:
                continue
            h = (g + 1) // 4
            cg = (-pow(p, -1, g)) % g
            if h % cg == 0:
                G.add(g)
        assert G == {4 * c * d - 1 for (a, c, d) in S}, p
        assert len(G) == len(S), p
        # independent integral Astra sources
        I = set()
        for m in range(1, isqrt((p + 7) // 12) + 2):
            M2 = m * m
            for q in divisors(fac(p * M2 + 1)):
                if q % (4 * M2) == 4 * M2 - 1:
                    I.add((q, m))
        assert I == {(4 * c * d - 1, isqrt(c)) for (a, c, d) in S if isqrt(c) ** 2 == c}, p
print('N =', N, 'slice/int-source cross-check up to', N2, ': OK')
print('primes', stats['primes'], 'TypeA sols', stats['sols'], 'on split slices', stats['split'],
      'on non-split slices', stats['nonsplit'], 'with c a square (integral Astra sources)', stats['csq'])
print('Type A failures:', stats['fails'])
nI = stats['noint']
print('Type A holds but no integral Astra source:', len(nI), 'first', nI[:25])
