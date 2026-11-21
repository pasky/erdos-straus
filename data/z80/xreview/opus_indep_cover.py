"""Independent (Opus reviewer) replay of the z80 all-s Proth covers.
Written from the rule definitions in notes/z77/PROOF_S_WILD.md §2 and notes/z80/PROTH_CORE.md,
without importing any repository script.  Checks:
  (1) every fixed row's rule at its actual modulus, with own modulus derivation;
  (2) actual-integer ES triples (or word + sign data) at every s in [64, SMAX] hitting each row;
  (3) exhaustive coverage by an independent CRT split strategy (split by ALL remaining primes of
      the row with fewest missing prime factors) and, for periods <= 2e9, a direct bytearray;
  (4) X rows: own Phi evaluation via CRT x0 (x0=0 mod 16, x0=2^a mod H) and, with gmpy2,
      actual-integer masks A | n+u and ES triples at real exponents s=e*r for several unit sources.
Run: ulimit -v 6000000; uv run --offline --no-project --with gmpy2 --with cypari2 python -B opus_indep_cover.py
"""
import json, sys, math, random
from math import gcd, lcm, isqrt
from pathlib import Path
import gmpy2
from gmpy2 import mpz
R = Path(__file__).resolve().parents[1] / 'proth'
SMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 1500
UNITSQ = {a * a % 840 for a in range(840) if gcd(a, 840) == 1}
assert len(UNITSQ) == 6

def divisors(n):
    out = []
    i = 1
    while i * i <= n:
        if n % i == 0:
            out.append(i)
            if i * i != n: out.append(n // i)
        i += 1
    return sorted(out)

def mu(n):
    r, p = 1, 2
    while p * p <= n:
        if n % p == 0:
            n //= p
            if n % p == 0: return 0
            r = -r
        p += 1
    return -r if n > 1 else r

def es_ok(n, x, y, z):
    return x > 0 and y > 0 and z > 0 and 4 * x * y * z == n * (x * y + y * z + z * x)

from cypari2 import Pari
pari = Pari()
def small_triple(q):
    # own search with PARI factorisation: x>q/4, a=4x-q, b=qx; (a y-b)(a z-b)=b^2
    for x in range(q // 4 + 1, q // 4 + 200):
        a = 4 * x - q; b = q * x
        g = gcd(a, b); a //= g; b //= g
        for d in map(int, pari.divisors(b * b)):
            if d > b: break
            if (d + b) % a == 0 and (b * b // d + b) % a == 0:
                y = (d + b) // a; z = (b * b // d + b) // a
                if es_ok(q, x, y, z): return (x, y, z)
    raise ValueError(q)

def modulus(T, z):
    if T == 'M': return 840
    if T in ('D', 'II'): return z[0]
    if T == 'W': return 8 * z[0]
    if T == 'K':
        f, K0, D, E = z
        return 4 * f * K0 if (D[2] or E[2]) else 4 * lcm(f, K0)
    raise ValueError(T)

stats = {}
def rule_mod(T, z, n, M):
    """Rule check at residue n mod M (all quantities needed are determined mod M)."""
    if T == 'M':
        return n % 840 not in UNITSQ
    if T == 'D':
        return n % z[0] == 0 and z[0] >= 2
    if T == 'II':
        f, a, b = z
        return min(f, a, b) > 0 and (f + 1) % (4 * a * b) == 0 and (b * n + a) % f == 0
    if T == 'W':
        A, u = z
        if (A + 1) % u or (n + u) % A: return False
        t = (A + 1) // u; v8 = ((n + u) % (8 * A)) // A  # v mod 8
        return t >= 2 and u >= 2 and (n + t) * t * u * v8 % 8 == 0
    if T == 'K':
        f, K0, D, E = z
        if f % 4 != 3 or (n + f) % (4 * K0): return False
        y0 = (n + f) // (4 * K0)  # only needed mod f when used
        def val(V):
            d, i, b = V
            assert d > 0 and K0 % d == 0 and i in (0, 1) and b in (0, 1)
            return d * pow(n, i) * pow(y0, b)
        return (val(D) + val(E)) % f == 0

def rule_full(m, T, z, n, k):
    """Actual integer n: build ES triple (or W word data) and verify."""
    if T == 'M':
        assert n % 840 not in UNITSQ; return 'mordell'
    if T == 'D':
        q = z[0]; assert n % q == 0
        x, y, w = small_triple_cache(q); c = n // q
        assert es_ok(n, x * c, y * c, w * c); return 'triple'
    if T == 'II':
        f, a, b = z; d = (f + 1) // (4 * a * b)
        bp, r = divmod(b * n + a, f); assert r == 0
        assert es_ok(n, a * bp * d, a * b * d * n, bp * b * d * n); return 'triple'
    if T == 'W':
        A, u = z; t, r1 = divmod(A + 1, u); v, r2 = divmod(n + u, A)
        assert r1 == r2 == 0 and min(t, u, v) >= 2 and n == t * u * v - u - v
        assert (n + t) * t * u * v % 8 == 0 and n % 4 == 1 and isqrt(n) ** 2 != n
        E = t * v - 1
        if E % 4 == 0:
            D = E // 4; assert es_ok(n, A * D * n, u * D, A * u * D); return 'triple'
        Ap = E  # swapped roles u<->v
        if A % 4 == 0:
            D = A // 4; assert es_ok(n, Ap * D * n, v * D, Ap * v * D); return 'triple'
        return 'word-only'
    if T == 'K':
        f, K0, D, E = z; y = (n + f) // 4; assert (n + f) % (4 * K0) == 0
        y0 = y // K0
        def val(V):
            d, i, b = V; return d * n ** i * y0 ** b
        a, b = val(D), val(E); assert (a + b) % f == 0 and (n * y) % a == 0 and (n * y) % b == 0
        g = (a + b) // f
        assert es_ok(n, y, n * y // a * g, n * y // b * g); return 'triple'

_st = {}
def small_triple_cache(q):
    if q not in _st: _st[q] = small_triple(q)
    return _st[q]

def check_rows(m, rows):
    k = 4 ** m - 1; h = 2 * m - 1
    kinds = {}
    for row in rows:
        P, j, T, *z = row
        assert 0 <= j < P
        if T == 'X': continue
        M = modulus(T, z)
        # least s0>=64 in class
        s0 = j if j >= 64 else j + ((64 - j + P - 1) // P) * P
        nM = (k * pow(2, s0, M) + 1) % M
        # periodicity of n mod M on the class for s>=s0
        assert (k * pow(2, s0, M) * (pow(2, P, M) - 1)) % M == 0, (m, row)
        assert rule_mod(T, z, nM, M), (m, row)
        if T == 'W':
            A, u = z
            # v>=2 for all s>=64: n+u >= k*2^64+1+u >= 2A
            assert k * 2 ** 64 + 1 + u >= 2 * A
        if T == 'D' and z[0] < 10 ** 13:
            small_triple_cache(z[0])
        # actual integers in the box
        s = s0
        while s <= SMAX:
            n = k * 2 ** s + 1
            kd = rule_full(m, T, z, n, k); kinds[T + ':' + kd] = kinds.get(T + ':' + kd, 0) + 1
            s += P
    return kinds

def coverage_split(rows, H, base):
    """Independent exhaustive cover check: node (a mod b).  Rows compatible with node; if some row's
    P | b it covers.  Else pick compatible row with smallest P/gcd(P,b) and split into all residues
    mod lcm(b,P) at once."""
    rs = [(P, j) for P, j, *_ in rows]
    for P, j in rs: assert H % P == 0
    covered = bytearray(base)
    small = [(P, j) for P, j in rs if base % P == 0]
    for P, j in small:
        for x in range(j, base, P): covered[x] = 1
    rest = [(P, j) for P, j in rs if base % P]
    nodes = 0
    stack = [(a, base, rest) for a in range(base) if not covered[a]]
    while stack:
        a, b, R0 = stack.pop(); nodes += 1
        U = [(P, j) for P, j in R0 if (j - a) % gcd(P, b) == 0]
        assert U, ('uncovered', a, b)
        if any(b % P == 0 for P, j in U): continue
        P, j = min(U, key=lambda r: (r[0] // gcd(r[0], b), r[0]))
        L = lcm(b, P); assert H % L == 0
        step = L // b
        if step > 10 ** 6:
            # fall back to a single prime split
            q = smallest_prime(P // gcd(P, b)); L = b * q; step = q
        for t in range(step):
            stack.append((a + b * t, L, U))
    return nodes

def smallest_prime(n):
    p = 2
    while p * p <= n:
        if n % p == 0: return p
        p += 1
    return n

def coverage_bytes(rows, H):
    c = bytearray(H)
    for P, j, *_ in rows:
        c[j::P] = b'\1' * ((H - j + P - 1) // P)
    out = []; i = c.find(0)
    while i >= 0 and len(out) < 100:
        out.append(i); i = c.find(0, i + 1)
    return out

def phi2d_mod(x, d, M):
    # Phi_{2d}(x) for odd d, via Phi_d(-x) = prod_{b|d} ((-x)^b - 1)^{mu(d/b)} (sign fixed below)
    num, den = 1, 1
    for b in divisors(d):
        e = mu(d // b)
        if e == 0: continue
        term = (pow(-x, b, M) - 1) % M
        if e == 1: num = num * term % M
        else: den = den * term % M
    val = num * pow(den, -1, M) % M
    return (-val) % M if d == 1 else val  # Phi_2(x) = x+1 = -((-x)-1)

def check_X(m, row):
    P, j, T, e, W = row
    k = 4 ** m - 1; h = 2 * m - 1; H = 2 ** h - 1; u = k - 1; M = 8 * u
    assert u == 2 * H and j == 0 and P % (4 * e) == 0 and e % 2 == 1
    units = [a for a in range(1, h) if gcd(a, h) == 1]
    assert sorted(map(int, W)) == units
    divs_e = set(divisors(e))
    for a in units:
        c, I = W[str(a)]
        assert k % c == 0 and len(set(I)) == len(I) and set(I) <= divs_e
        # x0 = 0 mod 16, = 2^a mod H  (CRT)
        x0 = next(x for x in range(pow(2, a, H), 16 * H, H) if x % 16 == 0)
        A = c
        for d in I: A = A * phi2d_mod(x0, d, M) % M
        assert A == (7 * u - 1) % M, (m, a)
    return True

def check_X_actual(m, row, nsrc):
    P, j, T, e, W = row
    k = 4 ** m - 1; h = 2 * m - 1; u = k - 1
    hp = {p for p in range(3, h + 1, 2) if h % p == 0 and all(p % q for q in range(3, isqrt(p) + 1, 2))}
    units = [a for a in range(1, h) if gcd(a, h) == 1]
    done = []
    for a in units[:nsrc]:
        r = next(r for r in range(4, 10 * h, 4) if r % h == a)
        assert gcd(r, h) == 1
        for o in (1, min(hp)):
            s = e * r * o
            assert s % (4 * e) == 0
            X = mpz(2) ** r
            c, I = W[str(a)]
            A = mpz(c)
            for d in I:
                num = mpz(1); den = mpz(1)
                for b in divisors(d):
                    ee = mu(d // b)
                    if ee == 1: num *= X ** b + 1
                    elif ee == -1: den *= X ** b + 1
                q, rr = gmpy2.f_divmod(num, den); assert rr == 0
                A *= q
            n = mpz(k) * mpz(2) ** s + 1
            assert (n + u) % A == 0 and (A + 1) % u == 0
            t = (A + 1) // u; v = (n + u) // A
            assert t % 8 == 7 and v % 8 == 7 and n == t * u * v - u - v
            D = (t * v - 1) // 4; assert (t * v - 1) % 4 == 0
            x1, y1, z1 = A * D * n, u * D, A * u * D
            assert 4 * x1 * y1 * z1 == n * (x1 * y1 + y1 * z1 + z1 * x1)
            done.append((a, r, o, s))
    return done

if __name__ == '__main__':
    random.seed(1)
    ms = [11] + list(range(13, 22))
    for m in ms:
        c = json.loads((R / f'cover-{m}.json').read_text())
        rows = c['rows']; H = c['period']
        kinds = check_rows(m, rows)
        X = [r for r in rows if r[2] == 'X']
        for r in X: check_X(m, r)
        if m == 11:
            assert c['left'] == [0] and not X
            assert coverage_bytes(rows, H) == [0]
            cov = 'bytes: misses exactly [0]'
        else:
            assert c['left'] == []
            if H <= 2 * 10 ** 9:
                assert coverage_bytes(rows, H) == [], m
                cov = 'bytes: complete'
            else:
                nodes = coverage_split(rows, H, gcd(H, 720720))
                cov = f'split: complete ({nodes} nodes)'
        print(m, H, len(rows), kinds, cov, flush=True)
    # actual X instances
    for m in ms[1:]:
        c = json.loads((R / f'cover-{m}.json').read_text())
        X = [r for r in c['rows'] if r[2] == 'X'][0]
        nsrc = 99 if m <= 14 else 2
        if X[3] > 100000: nsrc = 1
        print('X actual', m, X[3], len(check_X_actual(m, X, nsrc)), 'instances', flush=True)
