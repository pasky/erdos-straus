"""Independent re-checks for the z74 Opus cross-review of lane Z72PHASE.

Written from scratch for the review (no import of the authors' scripts).
Run from the repository root, one section at a time or all:

  ulimit -v 6000000; timeout 1800 uv run --offline --no-project --with sympy --with numpy \
      python scripts/z74_xrev_z72phase_checks.py [section ...]

Sections: group, z72, phase43, extremal, mix, tail, orbit, census, composite, probe.
Large integers are factored with GNU coreutils `factor` (deterministic output, each factorisation is re-multiplied).
"""
import json
import random
import subprocess
import sys
from fractions import Fraction as Fr
from functools import lru_cache
from itertools import combinations, product
from math import gcd, isqrt, lcm, prod
from pathlib import Path

from sympy import factorint, isprime, legendre_symbol, jacobi_symbol, nextprime, primerange, sqrt_mod
from sympy.ntheory.modular import crt

ROOT = Path(__file__).resolve().parents[1]
TAIL = ROOT / 'data/z72/counter_tail'
OK = []


def ok(msg):
    OK.append(msg)
    print('  OK', msg, flush=True)


# ---------------------------------------------------------------- factoring
_FCACHE = {}


def gfactor_many(ns):
    """Factor many positive integers with GNU factor; returns {n: {p: e}} and re-multiplies."""
    todo = sorted({n for n in ns if n > 1 and n not in _FCACHE})
    for i in range(0, len(todo), 2000):
        chunk = todo[i:i + 2000]
        out = subprocess.run(['factor'], input='\n'.join(map(str, chunk)), capture_output=True,
                             text=True, check=True).stdout
        for line in out.splitlines():
            n, fs = line.split(':')
            n = int(n)
            d = {}
            for f in fs.split():
                d[int(f)] = d.get(int(f), 0) + 1
            assert prod(p ** e for p, e in d.items()) == n
            _FCACHE[n] = d
    res = {}
    for n in ns:
        res[n] = {} if n == 1 else _FCACHE[n]
    return res


def fac(n):
    if n < 10 ** 12:
        return factorint(n)
    return gfactor_many([n])[n]


def divisors_from(f):
    ds = [1]
    for p, e in f.items():
        ds = [d * p ** k for d in ds for k in range(e + 1)]
    return ds


def omega(n):
    return len(fac(n))


def support2_certs(K, c, f=None):
    """All Type II certificates (A,B) at shift c with coprime AB | K, c | A+B, omega(AB) <= 2 (unordered)."""
    f = f if f is not None else fac(K)
    ps = sorted(f)
    out = []
    for q in ps:
        for i in range(1, f[q] + 1):
            if (1 + q ** i) % c == 0:
                out.append((1, q ** i))
    for q, r in combinations(ps, 2):
        for i in range(1, f[q] + 1):
            for j in range(1, f[r] + 1):
                A, B = q ** i, r ** j
                if (1 + A * B) % c == 0:
                    out.append((1, A * B))
                if (A + B) % c == 0:
                    out.append((A, B))
    return out


def all_certs(K, c, f=None):
    """All coprime unordered (A,B), AB | K, c | A+B (unrestricted support)."""
    f = f if f is not None else fac(K)
    ps = sorted(f)
    out = []
    for signs in product((0, 1, 2), repeat=len(ps)):  # 0: absent, 1: in A, 2: in B
        for exps in product(*[range(1, f[p] + 1) for p in ps]):
            A = prod(p ** e for p, e, s in zip(ps, exps, signs) if s == 1)
            B = prod(p ** e for p, e, s in zip(ps, exps, signs) if s == 2)
            if A <= B and (A + B) % c == 0:
                out.append((A, B))
        # exponents of absent primes are irrelevant; dedupe below
    return sorted(set(out))


def pocklington(N):
    """Pocklington-Lehmer primality proof for N > 2^64 (below 2^64 SymPy's isprime is deterministic).
    Uses a fully factored part F of N-1 with F^2 > N; each prime of F is itself proved recursively."""
    if N < 2 ** 64:
        return isprime(N)
    f = fac(N - 1)
    F, used = 1, []
    for q in sorted(f, reverse=True):
        F *= q ** f[q]
        used.append(q)
        if F * F > N:
            break
    assert F * F > N, 'N-1 not factored far enough'
    for q in used:
        assert pocklington(q)
        for a in range(2, 200):
            if pow(a, N - 1, N) != 1:
                return False
            if gcd(pow(a, (N - 1) // q, N) - 1, N) == 1:
                break
        else:
            raise AssertionError('no Pocklington witness')
    return True


def es_ok(n, xs):
    return all(x > 0 for x in xs) and sum(Fr(1, x) for x in xs) == Fr(4, n)


def triple_from(n, c, A, B):
    K = (n + c) // 4
    assert (n + c) % 4 == 0 and K % (A * B) == 0 and (A + B) % c == 0
    D, E = K // (A * B), (A + B) // c
    t = (K, n * A * D * E, n * B * D * E)
    assert es_ok(n, t)
    return t


def direct_completion(n, x, fx=None, fn=None, want=False):
    """Does 4/n - 1/x = 1/y + 1/z have a positive solution?  Exact test via divisors of v^2 (residue sets)."""
    u, v = 4 * x - n, n * x
    if u <= 0:
        return False
    g = gcd(u, v)
    u, v = u // g, v // g
    if u == 1:
        return True
    fv = {}
    for f in (fx or fac(x), fn or fac(n)):
        for p, e in f.items():
            fv[p] = fv.get(p, 0) + e
    fv = {p: e for p, e in fv.items() if v % p == 0}
    for p in list(fv):
        e = 0
        w = v
        while w % p == 0:
            w //= p
            e += 1
        fv[p] = e
    assert prod(p ** e for p, e in fv.items()) == v
    target = (-v) % u
    # residues of divisors of v^2 modulo u (all primes of v are units mod u since gcd(u,v)=1)
    S = {1 % u}
    for p, e in fv.items():
        pw = [pow(p, k, u) for k in range(2 * e + 1)]
        S = {(s * w) % u for s in S for w in pw}
    hit = target in S
    if hit and want:
        return True
    return hit


# ---------------------------------------------------------------- group criterion (Z72 + Z73 composite)
def dist(x, m):
    x %= m
    return min(x, m - x)


def sec_group():
    print('[group] cyclic criterion of Z72_PAIR_PHASE (full a,b range)')
    cases = fires = eqmiss = 0
    for c in [3, 7, 11, 19, 23, 31, 43, 47, 59, 67, 71, 79, 83]:
        m = c - 1
        for a in range(m):
            for b in range(m):
                for v in range(1, 6):
                    for w in range(1, 6):
                        V, W = v + 1, w + 1
                        Tm = min(V * dist(j * a, m) + W * dist(j * b, m) for j in range(1, m, 2))
                        box = {(i * a + k * b) % m for i in range(-v, v + 1) for k in range(-w, w + 1)}
                        hit = (m // 2) in box
                        cases += 1
                        if Tm > m or (Tm == m and (v % 2 or w % 2)):
                            fires += 1
                            assert hit, (c, a, b, v, w)
                        if Tm == m:
                            oa, ob = m // gcd(a, m), m // gcd(b, m)
                            cond = (oa == 2 * V and ob == 2 * W and gcd(V, W) == 1)
                            assert (not hit) == cond, (c, a, b, v, w)
                            eqmiss += (not hit)
                        if cond_rect(a, b, m, V, W):
                            assert Tm == m and not hit
    ok(f'cyclic criterion: {cases} boxes, {fires} fire (all hit), {eqmiss} equality misses = exactly the order/coprimality cases')
    # sharpness example
    m, a, b, v, w = 30, 5, 3, 2, 4
    Tm = min(3 * dist(j * a, m) + 5 * dist(j * b, m) for j in range(1, m, 2))
    box = {(i * a + k * b) % m for i in range(-v, v + 1) for k in range(-w, w + 1)}
    assert Tm == m and 15 not in box
    ok('sharpness example c=31,(a,b)=(5,3),(v,w)=(2,4): T=1 and miss')

    print('[group] general finite abelian criterion of Z73_COMPOSITE_PHASE (G = Z/m1 x Z/m2)')
    cases = fires = eqmiss = 0
    for m1, m2 in [(2, 2), (2, 4), (4, 4), (2, 6), (2, 8), (4, 6), (6, 6), (2, 12), (4, 8)]:
        L = lcm(m1, m2)
        G = [(x, y) for x in range(m1) for y in range(m2)]
        add = lambda g, h: ((g[0] + h[0]) % m1, (g[1] + h[1]) % m2)
        mul = lambda k, g: ((k * g[0]) % m1, (k * g[1]) % m2)
        chars = [(j1, j2) for j1 in range(m1) for j2 in range(m2)]
        th = lambda ch, g: (ch[0] * g[0] * (L // m1) + ch[1] * g[1] * (L // m2)) % L
        squares = {mul(2, g) for g in G}
        for t in [g for g in G if g != (0, 0) and mul(2, g) == (0, 0)]:
            odd = [ch for ch in chars if th(ch, t) == L // 2]
            for q in G:
                for r in G:
                    for v in range(1, 5):
                        for w in range(1, 5):
                            V, W = v + 1, w + 1
                            TL = min(V * dist(th(ch, q), L) + W * dist(th(ch, r), L) for ch in odd)
                            hit = any(((i * q[0] + k * r[0]) % m1, (i * q[1] + k * r[1]) % m2) == t
                                      for i in range(-v, v + 1) for k in range(-w, w + 1))
                            cases += 1
                            if TL > L:
                                fires += 1
                                assert hit
                            if TL == L:
                                tset = {(0, 0), t}
                                inj = all(((i * q[0] + k * r[0]) % m1, (i * q[1] + k * r[1]) % m2) not in tset
                                          for i in range(V) for k in range(W) if (i, k) != (0, 0))
                                cond = mul(V, q) == t and mul(W, r) == t and inj
                                assert (not hit) == cond, (m1, m2, t, q, r, v, w)
                                if not hit:
                                    eqmiss += 1
                                    if t not in squares:
                                        assert V % 2 == 1 and W % 2 == 1
    ok(f'abelian criterion: {cases} cases, {fires} with T>1 (all hit), {eqmiss} equality misses = exactly the stated '
       f'q^V=r^W=t / direct-product cases; non-square t forces V,W odd')


def cond_rect(a, b, m, V, W):
    return (m // gcd(a, m) == 2 * V and m // gcd(b, m) == 2 * W and gcd(V, W) == 1)


# ---------------------------------------------------------------- Z72_PAIR_PHASE
def sec_z72():
    print('[z72] 1009 example, 1201 table, partial forcing, by-p sample of the support sieve')
    n, c, K = 1009, 11, 255
    assert n % 840 == 169 and (n + c) // 4 == K
    assert triple_from(n, c, 17, 5) == (255, 102918, 30270)
    m = 10
    lg = {pow(2, i, 11): i for i in range(10)}
    a, b = lg[5], lg[17 % 11]
    assert (a, b) == (4, 9) and min(2 * dist(j * a, m) + 2 * dist(j * b, m) for j in range(1, m, 2)) == m
    ok('1009: logs (4,9), T=1, triple (255,102918,30270)')
    p = 1201
    rows = {}
    for c in range(3, (p + 4) // 3 + 1, 4):
        K = (p + c) // 4
        cs = all_certs(K, c)
        if cs:
            rows[c] = min((omega(A * B), A, B) for A, B in cs)
    assert rows == {23: (3, 6, 17), 31: (3, 1, 154), 39: (2, 1, 155), 47: (3, 8, 39)}, rows
    assert triple_from(1201, 39, 1, 155) == (310, 9608, 1489240)
    ok('1201: successful shifts {23:3, 31:3, 39:2, 47:3} (min omega), no prime shift with support <= 2')
    # partial forcing identity
    cnt = 0
    for p in primerange(5, 200000):
        if p % 8 == 5:
            triple_from(p, 3, 1, 2)
            cnt += 1
        elif p % 8 == 1:
            h = (p + 1) // 2
            rs = [r for r in fac(h) if r % 4 == 3]
            for r in rs:
                triple_from(p, 2 * r + 1, 1, 2 * r)
                cnt += 1
    ok(f'partial forcing (5 mod 8: c=3; 1 mod 8: r | (p+1)/2, r=3 mod 4) gives valid triples ({cnt} checks)')
    # prime count p = 1 mod 4 up to 5e8 (independent numpy sieve of odd numbers)
    import numpy as np
    N = 500_000_000
    s = np.ones(N // 2 + 1, dtype=np.bool_)  # s[i] <-> 2i+1
    s[0] = False
    for i in range(1, (isqrt(N) - 1) // 2 + 1):
        if s[i]:
            pp = 2 * i + 1
            s[pp * pp // 2::pp] = False
    idx = np.nonzero(s)[0]
    primes = 2 * idx + 1
    n1 = int(np.count_nonzero(primes % 4 == 1))
    assert n1 == 13176808, n1
    n1b = int(np.count_nonzero((primes % 4 == 1) & (primes <= 50_000_000)))
    assert n1b == 1500452, n1b
    ok('prime counts: 13,176,808 primes 1 mod 4 <= 5e8; 1,500,452 <= 5e7')
    # by-p sample at the top of the range and a random sample (search by p, then c, factoring K)
    top = [int(q) for q in primes[-40000:] if q % 4 == 1]
    rng = random.Random(74)
    one = primes[primes % 4 == 1]
    samp = top + [int(one[rng.randrange(len(one))]) for _ in range(20000)]
    mord = [int(q) for q in primes[-3_000_000:] if q % 840 in (1, 121, 169, 289, 361, 529)]
    samp += mord
    del s, idx, primes, one
    worst = (0, 0)
    for p in samp:
        c = 3
        while True:
            K = (p + c) // 4
            if support2_certs(K, c):
                break
            c += 4
            assert 3 * c <= p + 4
        A, B = support2_certs((p + c) // 4, c)[0]
        triple_from(p, c, A, B)
        worst = max(worst, (c, p))
    ok(f'by-p support<=2 search: {len(samp)} primes (top 2*10^4 below 5e8, 2*10^4 random, {len(mord)} Mordell-class '
       f'near 5e8): all certified, latest first shift c={worst[0]} at p={worst[1]}')


# ---------------------------------------------------------------- PHASE43
def sec_phase43():
    print('[phase43] paired rows at c=43')
    rows = [(12395549472601, 222158389, False), (349219296721, 6258859, True)]
    lg = {pow(3, i, 43): i for i in range(42)}
    def sl(x):
        e = lg[x % 43]
        return e if e <= 21 else e - 42
    assert [sl(13), sl(29), sl(37)] == [-10, -1, 7]
    for n, q, expect in rows:
        x = 13 * 29 * 37 * q
        assert isprime(n) and isprime(q) and n == 4 * x - 43 and n % 840 == 1
        assert [pow(n, (c - 1) // 2, c) == 1 for c in (3, 7, 11, 19, 23, 31)] == [True] * 6
        assert pow(n, 21, 43) == 42
        assert sl(q) == (-7 if not expect else 7)
        costs = [dist(10 * j, 42) + dist(j, 42) + 2 * dist(7 * j, 42) for j in range(1, 22, 2)]
        assert costs == [25, 57, 27, 35, 57, 41, 31, 75, 33, 53, 63]
        gens = [13, 29, 37, q]
        R = {1}
        for g in gens:
            gi = pow(g, -1, 43)
            R = {(r * s) % 43 for r in R for s in (gi, 1, g)}
        assert set(range(1, 43)) - R == {4, 11, 14, 40, 42}
        H = n * x
        res = direct_completion(n, x, fx={13: 1, 29: 1, 37: 1, q: 1}, fn={n: 1})
        assert res == expect
        if not expect:
            assert H % 43 == 13
            S = {1}
            for p_ in (13, 29, 37, q, n):
                S = {(s * pow(p_, k, 43)) % 43 for s in S for k in range(3)}
            assert set(range(1, 43)) - S == {30} and (-H) % 43 == 30
    ok('both rows: primes, 1 mod 840, Euler signs, logs (-10,-1,7,-+7), cost list, missing ratio set {4,11,14,40,42}')
    ok('negative row: divisor classes of H^2 miss exactly 30 = -H; positive row completes (direct test)')
    n = rows[0][0]
    for c in range(3, 44, 4):
        x = (n + c) // 4
        assert not direct_completion(n, x), c
    x = (n + 47) // 4
    t = (3098887368162, 817782487148702189502978, 1344434408867368729822288659)
    assert t[0] == x and es_ok(n, t)
    ok('negative row: no completion at any c=3,7,...,43 (composites included); c=47 triple verified')
    n, q = rows[0][0], rows[0][1]
    x = 13 * 29 * 37 * q
    nd = 0
    for d in divisors_from({13: 2, 29: 2, 37: 2, q: 2, n: 2}):
        if 4 * d <= n:
            continue  # 1/d > 4/n leaves a negative remainder: d cannot be a denominator
        fd = dict(factorint(d)) if d < 10 ** 12 else {pp: e for pp, e in ((13, 0), (29, 0), (37, 0), (q, 0), (n, 0))}
        if d >= 10 ** 12:
            w = d
            for pp in (13, 29, 37, q, n):
                while w % pp == 0:
                    w //= pp
                    fd[pp] += 1
            assert w == 1
            fd = {pp: e for pp, e in fd.items() if e}
        fd_n = {n: 1}
        if 4 * d == n:
            continue
        assert not direct_completion(n, d, fx=fd, fn=fd_n), d
        nd += 1
    ok(f'negative row: none of the {nd} admissible divisors d of H^2 is a denominator of any ES triple for 4/n')
    # positive-row identity family
    for a in [2, 41, 45, 84, 29 * 6258859]:
        if a % 43 not in (2, 41):
            continue
        nn = 1924 * a - 43
        xx = 481 * a
        y = 481 * (nn * a + 1) // 43
        assert 481 * (nn * a + 1) % 43 == 0 and es_ok(nn, (xx, y, nn * a * y))
    ok('positive-row identity x=481a, y=481(na+1)/43, z=nay verified on samples')


# ---------------------------------------------------------------- EXTREMAL_ES
def band(n, h, strict, cap=10 ** 7):
    """All sorted triples with |4/n - sum| < h (strict) or <= h, h a positive Fraction; asserts finiteness."""
    hn, hd = h.numerator, h.denominator
    out = []
    xlo = max(1, (n * hd) // (4 * hd + hn * n))
    assert 4 * hd > hn * n
    xhi = (3 * n * hd) // (4 * hd - hn * n) + 1
    for x in range(xlo, xhi + 1):
        A, B = 4 * x - n, n * x  # r1 = A/B
        if A * hd + hn * B <= 0:
            continue
        assert A * hd > hn * B, ('infinite y fibre', n, x)
        ylo = max(x, (B * hd) // (A * hd + hn * B))
        yhi = (2 * B * hd) // (A * hd - hn * B) + 1
        for y in range(ylo, yhi + 1):
            s, t = A * y - B, B * y  # r2 = s/t
            if s * hd + hn * t <= 0:
                continue
            assert s * hd > hn * t, ('infinite z fibre', n, x, y)
            zlo = max(y, (t * hd) // (s * hd + hn * t))
            zhi = (t * hd) // (s * hd - hn * t) + 1
            for z in range(zlo, zhi + 1):
                num = abs(s * z - t)  # error = num/(t z)
                lhs, rhs = num * hd, hn * t * z
                if lhs < rhs or (not strict and lhs == rhs):
                    out.append((x, y, z, Fr(num, t * z)))
                    assert len(out) < cap
    return out


def components(verts):
    par = {}
    def find(a):
        while par.setdefault(a, a) != a:
            par[a] = par[par[a]]
            a = par[a]
        return a
    for v in verts:
        for d in set(v[:3]):
            ra, rb = find(('v', v[:3])), find(('d', d))
            if ra != rb:
                par[ra] = rb
    return find


def sec_extremal():
    print('[extremal] section 1 optimum, 73 bottleneck, small n, gates')
    def no_two_term(n):
        return all(p % 4 == 1 for p in fac(n))
    tested = []
    for n in [25, 73, 97, 193, 241, 313, 337, 409, 433, 457, 577, 601, 625, 673, 1105, 2521]:
        assert n % 24 == 1 and no_two_term(n)
        X = (n + 3) // 4
        B0 = n * X
        Y = (B0 + 2) // 3
        T = B0 * Y
        Z = (T + 1) // 2
        e0 = Fr(1, T * Z)
        assert Fr(4, n) - Fr(1, X) - Fr(1, Y) - Fr(1, Z) == e0
        vs = band(n, e0, strict=False)
        nonex = [v for v in vs if v[3] != 0]
        assert [v[:3] for v in nonex] == [(X, Y, Z)], (n, nonex[:5])
        assert all(Z not in v[:3] for v in vs if v[3] == 0)
        tested.append(n)
    ok(f'closest nonexact triple = (X,Y,Z) uniquely, and no exact triple contains Z, for n in {tested}')
    # gates
    def gateX(n):
        X = (n + 3) // 4
        return any(q % 3 == 2 for q in fac(n * X))
    def gateY(n):
        X = (n + 3) // 4
        Y = (n * X + 2) // 3
        M = 4 * Y - n
        assert M * X - n * Y == 2 and M == (n * n + 8) // 3
        f = dict(fac(n))
        for q, e in fac(Y).items():
            f[q] = f.get(q, 0) + e
        S = {1}
        for q, e in f.items():
            S = {(s * pow(q, k, M)) % M for s in S for k in range(2 * e + 1)}
        return 2 in S
    got = {n: (gateX(n), gateY(n)) for n in (25, 73, 409, 577, 2521)}
    assert got == {25: (True, gateY(25)), 73: (False, False), 409: (False, False), 577: (True, False),
                   2521: (False, False)}, got
    assert isprime(463) and isprime(530251) and isprime(631)
    p = 10156800001
    X = (p + 3) // 4
    assert isprime(p) and p % 24 == 1 and fac(X) == {13: 1, 199: 1, 981523: 1} and not gateX(p)
    ok(f'gates (X,Y): 73 {got[73]}, 409 {got[409]}, 577 {got[577]}, 2521 {got[2521]}; 25 X-gate open; '
       f'10156800001 X-gate closed')
    # brute-force the gate criteria against the band (one-move repair exists iff a gate opens)
    for n in (73, 97, 193, 241, 313, 337, 409, 433):
        X = (n + 3) // 4
        Y = (n * X + 2) // 3
        hasX = any(q % 3 == 2 for q in fac(n * X))
        # direct: exact triple containing X / Y
        dX = direct_completion_two(n, X)
        dY = direct_completion_two(n, Y)
        assert (dX, dY) == (hasX, gateY(n)), n
    ok('gate criteria agree with direct exact-completion tests at 8 primes 1 mod 24')
    # n = 73 bottleneck
    n = 73
    H = 44913834
    e0 = Fr(1, 206198539471)
    path = [(19, 463, 321091), (19, 514, 4599), (20, 351, 514), (20, 210, 30660)]
    errs = [abs(Fr(4, n) - sum(Fr(1, d) for d in t)) for t in path]
    assert errs == [e0, Fr(1, H), Fr(1, 131702220), 0]
    assert all(set(a) & set(b) for a, b in zip(path, path[1:]))
    vs = band(n, Fr(1, H), strict=True)
    find = components(vs)
    assert any(v[:3] == path[0] for v in vs) and not any(v[:3] == path[1] for v in vs)
    root = find(('v', path[0]))
    comp = [v for v in vs if find(('v', v[:3])) == root]
    assert len(vs) == 6939 and len(comp) == 6296 and all(v[3] != 0 for v in comp)
    assert sum(v[3] == 0 for v in vs) > 0  # exact triples exist in the band, just not in this component
    assert Fr(1, H) / e0 == Fr(148665133, 32382)
    ok(f'73: strict band E<1/{H} has {len(vs)} vertices; extremum component ({len(comp)} vertices) has no exact triple; '
       f'displayed path attains max 1/{H}: bottleneck exact')
    # small n < 73 with no two-term split
    surv = [n for n in range(2, 73) if n % 2 and all(p % 4 == 1 for p in fac(n))]
    surv = [n for n in surv if n > 1]
    assert surv == [5, 13, 17, 25, 29, 37, 41, 53, 61, 65]
    for n in surv:
        # greedy strict underapproximation
        r, ds = Fr(4, n), []
        for _ in range(3):
            d = int(1 / r) + 1
            ds.append(d)
            r -= Fr(1, d)
        g = r
        assert g > 0
        vs = band(n, g, strict=False)
        nz = sorted(v[3] for v in vs if v[3] != 0)
        best = [v for v in vs if v[3] == nz[0]]
        assert len(best) == 1
        exact = [v for v in vs if v[3] == 0]
        assert any(set(best[0][:3]) & set(e[:3]) for e in exact), n
    ok(f'every n in {surv}: unique closest nonexact triple, one move from an exact triple')
    # D-energy statements
    def dgraph(n, h):
        vs = []
        for x in range(n // 4 + 1, (3 * n + h) // 4 + 1):
            A, B = 4 * x - n, n * x
            for y in range(x, (2 * B + h) // A + 1):
                s = A * y - B
                if s <= 0:
                    continue
                By = B * y
                for z in range(max(y, (By - h) // s - 1), (By + h) // s + 2):
                    D = s * z - By
                    if abs(D) <= h and z >= y:
                        assert D == 4 * x * y * z - n * (x * y + y * z + z * x)
                        vs.append((x, y, z, D))
        return vs
    trapped_first = None
    for n in range(2, 18):
        vs = dgraph(n, 1)
        find = components(vs)
        compex = {find(('v', v[:3])) for v in vs if v[3] == 0}
        tr = [v for v in vs if find(('v', v[:3])) not in compex]
        if tr and trapped_first is None:
            trapped_first = (n, sorted(v[:4] for v in tr))
    assert trapped_first == (17, [(7, 11, 654, -1), (7, 11, 655, 1)]), trapped_first
    for h, trapped in ((2, True), (3, False)):
        vs = dgraph(17, h)
        find = components(vs)
        compex = {find(('v', v[:3])) for v in vs if v[3] == 0}
        assert (find(('v', (7, 11, 655))) not in compex) == trapped
    ok('D-energy: first trapped |D|<=1 component is at n=17: {(7,11,654),(7,11,655)}; trapped at cap 2, escapes at cap 3')


def direct_completion_two(n, x):
    return direct_completion(n, x)


# ---------------------------------------------------------------- mixproof
def reduce_form(a, b, c):
    while True:
        if a > c:
            a, b, c = c, -b, a
        if -a < b <= a:
            if a == c and b < 0:
                b = -b
            return a, b, c
        k = (a - b) // (2 * a)
        b, c = b + 2 * k * a, a * k * k + b * k + c


def menu(p, d, Qmax=200):
    plus, minus = [], []
    for q in primerange(3, Qmax):
        if jacobi_symbol(-d * p % q, q) != 1:
            continue
        (minus if jacobi_symbol(-d % q, q) == -1 else plus).append(q)
        if len(plus) >= 3 and len(minus) >= 3:
            break
    plus, minus = plus[:3], minus[:3]
    W = []
    prs = sorted(plus + minus)
    for k in (1, 2, 3):
        for S in combinations(prs, k):
            for es in product((1, 2), repeat=k):
                if sum(e for q, e in zip(S, es) if q in minus) % 2 == 0:
                    continue
                mods = [q ** e for q, e in zip(S, es)]
                rootlists = [sorted({x % m for x in range(m) if (x * x + d * p) % m == 0}) for m in mods]
                for rs in product(*rootlists):
                    r, N = crt(mods, rs)
                    W.append((int(N), int(r)))
    return prs, plus, minus, W


def sec_mix():
    print('[mix] d=2 frozen-menu exclusion; d=1 identities at 409, 9601, large p')
    p0 = 9601
    prs, plus, minus, W = menu(p0, 2)
    norms = {N for N, r in W}
    assert prs == [3, 11, 13, 17, 23, 29] and (len(W), len(norms), max(norms)) == (710, 103, 5783557)
    # the menu only depends on p mod q^2 for q <= 29 (and p mod 840 for the excluded small primes)
    M = 840 * prod(q * q for q in primerange(3, 30))
    for N in norms:
        assert M % N == 0
    bad = [(N, a) for N in norms if N % 8 == 7 for a in divisors_from(factorint((N + 1) // 8))
           if (p0 + 8 * a * a) % N == 0]
    assert bad == []
    ok('d=2 menu at 9601: primes [3,11,13,17,23,29], 710 signed words, 103 norms, max 5783557; certificate: no '
       'N=7 mod 8 norm has a | (N+1)/8 with N | p+8a^2')
    # SR + FR' product bound at the threshold
    Nmax = 5783557
    P = 2 * Nmax ** 2 + 1
    m = isqrt(2 * (2 * P + (P + 8) // 7)) + 1
    assert Nmax * m < 2 * P
    # an actual prime in the progression, and the good A=31 solution there; menu unchanged there
    x0, L = crt([M, 31], [p0, (-8) % 31])
    x0, L = int(x0), int(L)
    p = x0 + L * ((P - x0) // L + 1)
    while not isprime(p):
        p += L
    assert p > P and p % M == p0 % M and (p + 8) % 31 == 0 and pocklington(p)
    prs2, _, _, W2 = menu(p, 2)
    assert prs2 == prs and sorted(W2) == sorted(W)
    e = (p + 8) // 31
    b = (p + e) // 8
    a, c = 1, 4
    assert (p + e) % 8 == 0 and 8 * a * b == p + e and c * e == a + b and 8 * a * c - 1 == 31
    assert es_ok(p, (2 * b, 8 * p, 8 * b * p))
    # membership test brute force on the actual large p: no word is the A-ideal (or conjugate) of a solution
    for N in {N for N, r in W2 if N % 8 == 7}:
        for a_ in divisors_from(factorint((N + 1) // 8)):
            assert (p + 8 * a_ * a_) % N != 0
    ok(f'prime p={p} in the cell: same menu, A=31 solution good (triple verified), no menu word good')
    # d = 1 at 409
    p = 409
    prs, plus, minus, W = menu(p, 1)
    assert 5 in prs and 7 in prs and any(N == 35 for N, r in W)
    H = (p + 35) // 4
    ds = [a for a in range(1, H + 1) if H % a == 0]
    assert [a for a in ds if (4 * a * a + p) % 5 == 0] == [3, 37]
    assert [a for a in ds if (4 * a * a + p) % 7 == 0] == [1, 111]
    assert [a for a in ds if (4 * a * a + p) % 35 == 0] == []
    ok('409: divisor sets {3,37} mod 5, {1,111} mod 7, empty mod 35')
    # d = 1 at 9601: ranking and good set
    p = 9601
    prs, plus, minus, W = menu(p, 1)
    f = {reduce_form(N, 2 * r, (r * r + p) // N) for N, r in W}
    ranked = sorted(f, key=lambda t: (Fr(abs(t[1]), t[0]), t))
    good = set()
    amax = isqrt((p + (p + 4) // 3) // 4)
    for a in range(1, amax + 1):
        Na = p + 4 * a * a
        for A in [A for A in range(1, Na + 1) if Na % A == 0] if Na < 10 ** 6 else []:
            if (A + 1) % (4 * a) == 0:
                e = Na // A
                b = (p + e) // (4 * a)
                c = (A + 1) // (4 * a)
                assert 4 * a * b == p + e and c * e == a + b
                good.add(reduce_form(A, 4 * a, e))
                good.add(reduce_form(A, -4 * a, e))
    top4 = ranked[:4]
    assert {t[0] for t in top4} == {62, 59} and good == {reduce_form(23, 12, 419), reduce_form(23, -12, 419),
                                                         reduce_form(31, 6, 310), reduce_form(31, -6, 310)}
    assert good.isdisjoint(top4) and Fr(abs(ranked[3][1]), ranked[3][0]) < Fr(abs(ranked[4][1]), ranked[4][0])
    ok(f'9601 (d=1): top four ranked menu classes {top4}; good set {sorted(good)}; disjoint; no tie at cutoff')
    # large p mixed hit
    p = 15322362791157241
    assert isprime(p) and p % 840 == 1
    a, b, c, e = 311, 12317016130314, 2335, 5274953375
    N = 17 ** 2 * 19 * 23 ** 2
    assert 4 * a * b == p + e and c * e == a + b and 4 * a * c - 1 == N and (p + e) % 4 == 0
    assert es_ok(p, (a * b, a * c * p, b * c * p))
    prs, plus, minus, W = menu(p, 1)
    assert (N, 622) in W or (N, (-622) % N) in W
    f = {reduce_form(Nn, 2 * r, (r * r + p) // Nn) for Nn, r in W}
    ranked = sorted(f, key=lambda t: (Fr(abs(t[1]), t[0]), t))
    assert reduce_form(N, 4 * a, e) in ranked[:4] or reduce_form(N, -4 * a, e) in ranked[:4]
    ok(f'p={p}: word N=17^2*19*23^2 root 622 (=2a) is top-four and good; menu primes {prs}')


# ---------------------------------------------------------------- counter tail (README, ROUND2)
def first_support2_shift(p, cmax=4000):
    c = 3
    Ks = [(p + cc) // 4 for cc in range(3, cmax, 4)]
    F = gfactor_many(Ks)
    while True:
        K = (p + c) // 4
        cs = support2_certs(K, c, F[K])
        if cs:
            return c, cs
        c += 4


def sec_tail():
    print('[tail] counter_tail README late rows, CSV identities, ROUND2 shift-15 criterion')
    L = 4 * lcm(*range(1, 26))
    assert L == 107084577600
    late = [(2019030344657726401, 79), (2650016366384587201, 83), (5091403384022155201, 111),
            (3127054922239248001, 127)]
    for p, c0 in late:
        assert isprime(p) and isprime((p + 1) // 2) and (p - 1) % L == 0
        k = (p - 1) // L
        for t in (1, 2, 3):
            assert (L * k) % (4 * t) == 0 and isprime(1 + L * k // (4 * t))
        c, cs = first_support2_shift(p, 200)
        assert c == c0, (p, c)
        A, B = cs[0]
        triple_from(p, c, A, B)
        # shifts 3,7,11 have no certificate at all (unrestricted)
        for cc in (3, 7, 11):
            assert all_certs((p + cc) // 4, cc) == []
    p = 3127054922239248001
    assert (1, 39276714758833) in first_support2_shift(p, 200)[1]
    pc, cc = 2170275209960457601, 87
    assert isprime(pc) and isprime((pc + 1) // 2) and first_support2_shift(pc, 200)[0] == cc
    ok('late targets 79,83,111,127 and late L-control 87 recomputed (by p, GNU factor); 3,7,11 blocked unrestricted')
    # every CSV triple is a positive ES solution
    nrows = 0
    rows, ABs = [], []
    for name in ('pilot.csv', 'cluster.csv', 'progression_controls.csv'):
        lines = (TAIL / name).read_text().splitlines()
        hdr = lines[0].split(',')
        for ln in lines[1:]:
            rec = dict(zip(hdr, ln.split(',')))
            p = int(rec['p'])
            xs = (int(rec['x']), int(rec['y']), int(rec['z']))
            assert es_ok(p, xs)
            A_, B_, c_ = int(rec['A']), int(rec['B']), int(rec['first_c'])
            assert triple_from(p, c_, A_, B_) == xs  # the recorded A,B,c generate the recorded triple
            ABs.append(int(rec['A']) * int(rec['B']))
            rows.append((name, rec['arm'], p, int(rec['first_c'])))
            nrows += 1
    assert nrows == 512 * 2 + 2048 * 2 + 2048
    FA = gfactor_many(ABs)
    assert all(len(FA[k]) <= 2 for k in ABs)
    ok(f'{nrows} CSV rows: literal triples are ES solutions generated by the recorded (A,B,first_c); omega(AB)<=2')
    # random sample of first shifts recomputed
    rng = random.Random(7)
    samp = rng.sample(rows, 300)
    for name, arm, p, c0 in samp:
        assert first_support2_shift(p, c0 + 4)[0] == c0, (name, p, c0)
    ok('300 random CSV rows: first support<=2 shift recomputed independently, all agree')
    # quantile table for the cluster
    def q(xs, f):
        xs = sorted(xs)
        return xs[max(0, -(-len(xs) * f // 100) - 1)]
    for (nm, arm), want in {(('cluster.csv', 'target')): (15, 27, 47, 127),
                            (('cluster.csv', 'control')): (3, 11, 19, 31),
                            (('progression_controls.csv', 'L-control')): (3, 15, 31, 87),
                            (('pilot.csv', 'target')): (3, 11, 23, 43),
                            (('pilot.csv', 'control')): (3, 11, 19, 51)}.items():
        xs = [c for n_, a_, p, c in rows if n_ == nm and a_ == arm]
        got = (q(xs, 50), q(xs, 90), q(xs, 99), max(xs))
        assert got == want, (nm, arm, got)
    ok('quantile table (median/90/99/max) reproduced from CSVs')
    # ROUND2: shift-15 criterion on all c15 rows
    lines = (TAIL / 'c15.csv').read_text().splitlines()
    hdr = lines[0].split(',')
    recs = [dict(zip(hdr, ln.split(','))) for ln in lines[1:]]
    assert len(recs) == 2048
    Qs = [(int(r['p']) + 15) // 16 for r in recs]
    F = gfactor_many(Qs)
    nb = ncomp = 0
    for r, Qv in zip(recs, Qs):
        p = int(r['p'])
        assert p % 16 == 1 and isprime(p) and isprime((p + 1) // 2)
        crit = all(qq % 15 in (1, 2, 4, 8) for qq in F[Qv])
        assert crit == bool(int(r['blocked15']))
        K = (p + 15) // 4
        fK = dict(F[Qv]); fK[2] = fK.get(2, 0) + 2
        has15 = bool(support2_certs(K, 15, fK))
        assert has15 == (not crit)
        if crit:
            nb += 1
            ncomp += not isprime(Qv)
            assert int(r['first_c']) > 15
        xs = (int(r['x']), int(r['y']), int(r['z']))
        assert es_ok(p, xs)
    assert (nb, ncomp) == (823, 540)
    blk = [int(r['first_c']) for r in recs if int(r['blocked15'])]
    assert sorted(blk)[len(blk) // 2] == 23 and max(blk) == 119
    ok('c15.csv: criterion (all primes of Q in <2> mod 15) <=> no support<=2 certificate at 15, for all 2048 rows; '
       '823 blocked (540 composite Q), median 23, max 119')


# ---------------------------------------------------------------- orbits (ROUND2/ROUND3)
def pair_moves(x, y, F):
    """All unordered positive (x',y') with 1/x'+1/y' = 1/x+1/y."""
    num, den = x + y, x * y
    g = gcd(num, den)
    u, v = num // g, den // g
    fv = {}
    for d in (x, y):
        for p, e in F[d].items():
            fv[p] = 0
    for p in list(fv):
        e, w = 0, v
        while w % p == 0:
            w //= p
            e += 1
        if e:
            fv[p] = e
        else:
            del fv[p]
    assert prod(p ** e for p, e in fv.items()) == v
    out = set()
    for d in divisors_from({p: 2 * e for p, e in fv.items()}):
        if d <= v and (d + v) % u == 0:
            e2 = v * v // d
            assert (e2 + v) % u == 0
            out.add(((v + d) // u, (v + e2) // u))
    return u, out


def closure(states, p):
    """Independent closure + connectivity + layer audit of a listed component."""
    S = {tuple(sorted(s)) for s in states}
    dens = {d for s in S for d in s}
    F = gfactor_many(sorted(dens))
    adj = {s: set() for s in S}
    for s in S:
        assert sum(Fr(1, d) for d in s) == Fr(4, p)
        for i, j in combinations(range(4), 2):
            u, mv = pair_moves(s[i], s[j], F)
            assert u != 1, ('mergeable', s)
            rest = [s[k] for k in range(4) if k not in (i, j)]
            for a, b in mv:
                t = tuple(sorted(rest + [a, b]))
                assert t in S, ('escape', s, t)
                if t != s:
                    adj[s].add(t)
    edges = sum(len(v) for v in adj.values()) // 2
    return S, adj, edges


def bfs_layers(adj, root):
    seen = {root: 0}
    fr = [root]
    layers = [1]
    while fr:
        nxt = []
        for s in fr:
            for t in adj[s]:
                if t not in seen:
                    seen[t] = seen[s] + 1
                    nxt.append(t)
        if nxt:
            layers.append(len(nxt))
        fr = nxt
    return seen, layers


def read_closed(name):
    lines = (TAIL / name).read_text().splitlines()
    return [tuple(int(v) for v in ln.split(',')[1:]) for ln in lines[1:]]


def sec_orbit():
    print('[orbit] closed components 14281 (O), 101641 (O,T), 1009 (T); paths; fixed-K obstruction')
    specs = [('closed14281.csv', 14281, 'O', 92, 641, [1, 1, 1, 17, 52, 20]),
             ('closed101641O.csv', 101641, 'O', 20, 47, [1, 1, 1, 5, 4, 8]),
             ('closed101641T.csv', 101641, 'T', 65, 306, [1, 13, 11, 26, 7, 5, 1, 1]),
             ('closed1009T.csv', 1009, 'T', 6, None, [1, 4, 1])]
    comps = {}
    for name, p, seed, nv, ne, lay in specs:
        S, adj, edges = closure(read_closed(name), p)
        root = (p, p, p, p) if seed == 'O' else tuple(sorted((p, (p + 2) // 3, p * ((p + 2) // 3), p * ((p + 2) // 3))))
        assert root in S
        seen, layers = bfs_layers(adj, root)
        assert len(seen) == len(S) == nv and layers == lay, (name, len(S), layers)
        if ne is not None:
            assert edges == ne, (name, edges)
        comps[name] = S
        ev = sorted({seen[s_] for s_ in S if any(d % 2 == 0 for d in s_)})
        want_ev = {'closed14281.csv': [5], 'closed101641O.csv': [5], 'closed1009T.csv': []}.get(name)
        if want_ev is not None:
            assert ev == want_ev, (name, ev)
        else:
            assert ev[0] == 2
    assert not (comps['closed101641O.csv'] & comps['closed101641T.csv'])
    try:  # negative control: dropping a vertex must make the list non-closed
        closure(read_closed('closed14281.csv')[:-1], 14281)
        raise RuntimeError('negative control did not fail')
    except AssertionError:
        pass
    ok('all four listed components are closed under every pair replacement (own divisor generator), have no '
       'mergeable pair, are connected from their seed with the stated vertex/edge/layer counts; 101641 O,T disjoint')
    # pretrap paths
    P = json.loads((TAIL / 'pretrap_paths.json').read_text())
    mord = [p for p in primerange(2, 101641) if p % 840 in (1, 121, 169, 289, 361, 529)]
    assert sorted(int(k) for k in P) == mord and len(mord) == 277

    def check_path(p, path, starts):
        assert tuple(sorted(path[0])) in starts
        for s, t in zip(path, path[1:]):
            assert sum(Fr(1, d) for d in t) == Fr(4, p)
            ms, mt = list(s), list(t)
            common = 0
            for d in list(ms):
                if d in mt:
                    mt.remove(d)
                    common += 1
            assert common >= 2
        last = path[-1]
        merges = [(i, j) for i, j in combinations(range(4), 2)
                  if (Fr(1, last[i]) + Fr(1, last[j])).numerator == 1]
        assert merges
        i, j = merges[0]
        m = (Fr(1, last[i]) + Fr(1, last[j])).denominator
        tri = [last[k] for k in range(4) if k not in (i, j)] + [m]
        assert es_ok(p, tri)
        return tri
    for k, path in P.items():
        p = int(k)
        b = (p + 2) // 3
        starts = {(p, p, p, p), tuple(sorted((p, b, p * b, p * b)))}
        check_path(p, path, starts)
    ok('pretrap_paths.json: exactly the 277 Mordell-class primes < 101641, each path valid (two kept denominators, '
       'exact sums) from O or T to a merge giving an ES triple')
    Nn = json.loads((TAIL / 'nested_paths.json').read_text())
    assert sorted(Nn) == ['1009', '101641', '14281'] and all(len(v) >= 2 for v in Nn.values())
    for k, path in Nn.items():
        p = int(k)
        h = (p + 1) // 2
        a = (h + 1) // 2
        q = p * a
        b2 = (q + 2) // 3
        tri = check_path(p, path, {tuple(sorted((a, b2, q * b2, q * b2)))})
        if p == 101641:
            assert sorted(tri) == [25434, 27214380, 307344088620]
    ok('nested_paths.json: 1009, 14281, 101641 paths valid from the nested seed; 101641 gives (25434,27214380,307344088620)')
    # universal seed moves
    for p in mord[:40]:
        h = (p + 1) // 2
        a = (h + 1) // 2
        seq = [(p, p, p, p), (h, p * h, p, p), (h, h, p * h, p * h), (h, h, p * a, p * h * a),
               (a, h * a, p * a, p * h * a), (a, p * a, p * a, p * a)]
        for s in seq:
            assert sum(Fr(1, d) for d in s) == Fr(4, p)
        for s1, s2 in zip(seq, seq[1:]):
            m2 = list(s2)
            for d in s1:
                if d in m2:
                    m2.remove(d)
            assert len(m2) == 2  # exactly one pair replaced
    ok('universal seed (a,pa,pa,pa) reached from O by the five displayed moves (40 primes)')


# ---------------------------------------------------------------- Z73_COMPOSITE_PHASE
def chars_mod(c):
    """Characters of (Z/c)* as functions g -> angle (Fraction mod 1), via CRT over prime powers (odd c)."""
    f = factorint(c)
    comps = []
    for p, e in f.items():
        m = p ** e
        g = int(__import__('sympy').primitive_root(m))
        phi = m // p * (p - 1)
        lg = {pow(g, i, m): i for i in range(phi)}
        comps.append((m, phi, lg))
    def gen():
        for js in product(*[range(phi) for m, phi, lg in comps]):
            def th(x, js=js):
                return sum(Fr(j * lg[x % m], phi) for j, (m, phi, lg) in zip(js, comps)) % 1
            yield th
    return gen


def fdist(x):
    x %= 1
    return min(x, 1 - x)


def sec_composite():
    print('[composite] 1201 at c=39; p=3117161329 at c=715; s=2 construction instance')
    p, c, q, r = 1201, 39, 5, 31
    K = (p + c) // 4
    assert K == 310 and K % (q * r) == 0
    T = min(2 * fdist(th(q)) + 2 * fdist(th(r)) for th in chars_mod(c)() if th(c - 1) == Fr(1, 2))
    assert T == 1 and pow(5, 2, 39) != 38 and (q * r) % c == c - 1
    ok('1201, c=39, q=5, r=31: joint score T=1 exactly, 5^2 != -1, hit A=1,B=155')
    p, c = 3117161329, 715
    K = (p + c) // 4
    assert isprime(p) and p % 840 in (1, 121, 169, 289, 361, 529) and K == 2729 * 285559
    assert isprime(2729) and isprime(285559)
    sg = lambda x: tuple(x % m for m in (5, 11, 13))
    assert sg(2729) == (4, 1, 12) and sg(285559) == (4, 10, 1) and sg(p) == (4, 7, 9)
    assert jacobi_symbol(p, c) == -1
    assert all_certs(K, c) == []
    H = p * K
    hits = [d for d in divisors_from({p: 2, 2729: 2, 285559: 2}) if (d + H) % c == 0]
    assert hits == [] and not direct_completion(p, K, fx={2729: 1, 285559: 1}, fn={p: 1})
    t = (779290335, 221553301293526860, 68016863497112746020)
    assert es_ok(p, t) and 4 * t[0] - p == 11
    T = min(2 * fdist(th(2729)) + 2 * fdist(th(285559)) for th in chars_mod(c)() if th(c - 1) == Fr(1, 2))
    assert T == 0
    # pairwise feasibility of the three sign constraints
    for drop in range(3):
        sols = [(i, j) for i in (0, 1) for j in (0, 1)
                if all(((i * (m in (5, 13))) + j * (m in (5, 11))) % 2 == 1
                       for k, m in enumerate((5, 11, 13)) if k != drop)]
        assert sols
    ok('3117161329 (Mordell class), c=715: no Type II at K, none of the 27 divisors of (pK)^2 completes, joint T=0, '
       'every two components feasible; c=11 triple verified')
    # explicit instance of the s=2 prime construction
    l1 = 211
    l0, l2 = [x for x in range(841, 10 ** 5, 840) if isprime(x)][:2]
    assert l1 % 105 == 1 and l1 % 8 == 3 and l0 % 840 == 1 and l2 % 840 == 1 and l0 > 17
    c = l0 * l1 * l2
    def find_q(conds, extra=None, start=3):
        mods = [m for m, r in conds]
        res = [r for m, r in conds]
        x, Lm = crt(mods, res)
        x, Lm = int(x), int(Lm)
        while True:
            if isprime(x) and (extra is None or extra(x)):
                return x
            x += Lm
    q1 = find_q([(2, 1), (105, 1), (l0, l0 - 1), (l1, l1 - 1), (l2, 1)])
    target = ((1 + c) * pow(4, -1, 105)) % 105
    q2 = find_q([(2, 1), (105, target), (l0, l0 - 1), (l1, 1), (l2, l2 - 1)],
                extra=lambda q: isprime(4 * q1 * q - c) and q != q1)
    n = 4 * q1 * q2 - c
    assert pocklington(n)  # n > 2^64: proved prime (the direct test below assumes n prime)
    K = q1 * q2
    assert n % 840 == 1 and jacobi_symbol(n, c) == -1 and n % l0 == 4
    assert all_certs(K, c, {q1: 1, q2: 1}) == []
    assert not direct_completion(n, K, fx={q1: 1, q2: 1}, fn={n: 1})
    for sub in ([l0, l1], [l0, l2], [l1, l2]):
        cc = prod(sub)
        assert any((q1 ** i * q2 ** j + 0) % cc == cc - 1 for i in (0, 1) for j in (0, 1))
    ok(f's=2 instance: l=({l0},{l1},{l2}), q=({q1},{q2}), prime n={n} = 1 mod 840, (n/c)=-1: no triple contains '
       f'x=K, while every proper subset of components is solvable')


# ---------------------------------------------------------------- Z73_PROBE_FORCING
def A1_cert(p, c_lim=None):
    """All A=1 certificates (B, c) with B | (p+c)/4, c | 1+B, c=3 mod 4."""
    out = []
    for c in range(3, (p + 4) // 3 + 1, 4):
        K = (p + c) // 4
        for B in divisors_from(fac(K)):
            if (1 + B) % c == 0:
                out.append((B, c))
    return out


def sec_probe():
    print('[probe] Z73_PROBE_FORCING')
    # section 1 facts
    assert isprime(37) and isprime(293) and fac((17 + 1) // 2) == {3: 2} and fac(21) == {3: 1, 7: 1}
    assert fac(4 * 1201 + 1) == {5: 1, 31: 2} and isprime(601)
    # incompatibility lemma, brute force
    cnt = 0
    for p in primerange(3, 30000):
        if p % 8 != 1:
            continue
        for r in fac(4 * p + 1):
            if r <= 3:
                continue
            for c in divisors_from(fac(2 * r + 1)):
                if c % 4 == 3 and (p + c) % (8 * r) == 0:
                    raise AssertionError((p, r, c))
            cnt += 1
    ok(f'A=1,B=2r with prime r>3, r | 4p+1: never a certificate (brute force, {cnt} (p,r) pairs, p<30000)')
    # E=2 compression
    for p in primerange(3, 60000):
        if p % 8 != 1:
            continue
        f = fac(2 * p + 1)
        crit = any(q % 8 in (5, 7) for q in f)
        Bs = [B for B in divisors_from(f) if B % 8 == 5]
        assert bool(Bs) == crit
        if Bs:
            assert min(sum(factorint(B).values()) for B in Bs) <= 2
            B = min(Bs)
            t = (2 * p + 1) // B
            assert t % 8 == 7
            D, c = (t + 1) // 8, (B + 1) // 2
            assert p + c == 4 * B * D
    ok('E=2 line: certificate <=> 2p+1 has a prime 5 or 7 mod 8, then Omega(B)<=2 (p<60000, p=1 mod 8)')
    # 193 first without A=1 certificate
    first = next(p for p in primerange(3, 2000) if p % 8 == 1 and not A1_cert(p))
    assert first == 193 and len(range(3, (193 + 4) // 3 + 1, 4)) == 16
    triple_from(193, 15, 2, 13)
    ok('193 is the first prime 1 mod 8 with no A=1 certificate (16 shifts 3..63); A=2,B=13,c=15 works')
    # sharp theorem on s = 15 mod 16 (composite s included)
    nchk = nfail = 0
    for s in range(15, 40000, 16):
        fs = factorint(s)
        f5 = {q: 2 * e for q, e in fs.items()}
        f5[5] = 2 * fs.get(5, 0) + 1
        Bs = [B for B in divisors_from(f5) if B % 16 == 11]
        assert Bs
        mo = min(len(factorint(B)) for B in Bs)
        crit_fail = all(q % 16 in (1, 5, 7, 9) for q in fs) and 5 not in fs and \
            all(fs[q] == 1 for q in fs if q % 16 == 5)
        assert mo <= 3 and (mo > 2) == crit_fail, (s, mo)
        # second family identities and E=5 criterion
        U, V = (5 * s - 1) // 2, (5 * s + 1) // 4
        p = (5 * s * s - 1) // 4
        D = (s + 1) // 16
        assert 5 * p + 1 == 2 * U * V and p + 4 * D == s * V and U % 20 == 17 and V % 20 == 19
        fUV = factorint(U * V)
        small5 = any(((2 * b + 1) % 5 == 0) and ((U * V // b) % 20 == 19)
                     for q, e in fUV.items() for j in range(1, e + 1) for b in [q ** j])
        crit5 = any(pow(q, j, 20) == 17 for q, e in fUV.items() for j in range(1, e + 1))
        assert small5 == crit5
        nchk += 1
        nfail += crit_fail
    ok(f'sharp support theorem (E=4) and E=5 prime-power criterion verified on all {nchk} s=15 mod 16 below 40000 '
       f'({nfail} support-3 cases)')
    # table rows
    for s, p, e4min, e5, Bs_min in [(31, 1201, 2, False, None), (959, 1149601, 3, True, [4795]),
                                    (2911, 10592401, 3, False, [14555])]:
        assert (5 * s * s - 1) // 4 == p and isprime(p)
        f5 = {q: 2 * e for q, e in factorint(s).items()}
        f5[5] = 2 * factorint(s).get(5, 0) + 1
        Bs = sorted(B for B in divisors_from(f5) if B % 16 == 11)
        assert min(len(factorint(B)) for B in Bs) == e4min
        if Bs_min:
            assert Bs == Bs_min  # the only E=4 certificate
        U, V = (5 * s - 1) // 2, (5 * s + 1) // 4
        fUV = factorint(U * V)
        assert any(pow(q, j, 20) == 17 for q, e in fUV.items() for j in range(1, e + 1)) == e5
    triple_from(1149601, 7, 1, 34)
    assert (1149601 + 7) // 4 // 34 == 8453
    # s = 2911 extras
    p = 10592401
    assert fac((p + 1) // 2) == {109: 1, 48589: 1} and not any(q % 8 in (5, 7) for q in fac(2 * p + 1))
    assert not any(q % 8 == 5 for q in fac(p + 2))
    triple_from(p, 23, 19, 27)
    assert jacobi_symbol(p, 7) == 1 and jacobi_symbol(p, 15) == 1
    # s = 4319
    p = 23317201
    assert isprime(p) and isprime((p + 1) // 2) and fac(4319) == {7: 1, 617: 1} and fac(10797) == {3: 1, 59: 1, 61: 1}
    assert isprime(5399)
    neg = [q for q in (7, 617, 3, 59, 61, 5399) if legendre_symbol(q, p) == -1]
    assert neg == [7, 59, 5399]
    triple_from(p, 7, 1, 62)
    neg2911 = [q for q in (41, 71, 19, 383, 3, 1213) if legendre_symbol(q, 10592401) == -1]
    assert 19 in neg2911 and 383 not in neg2911 and 71 in neg2911

    def q_in_support2(p, q):
        """Is there a support<=2 certificate with q | AB?  Enumerate k=AB=q^i m, omega<=2, c = -p mod 4k."""
        kmax = (p + 1) // 3
        qi = q
        while qi <= kmax:
            for mpart in [1] + [r ** j for r in primerange(2, kmax // qi + 1) if r != q
                                for j in range(1, 64) if qi * r ** j <= kmax]:
                k = qi * mpart
                c = (-p) % (4 * k)
                if c == 0 or c > k + 1:
                    continue
                splits = [(1, k)] + ([(qi, mpart)] if mpart > 1 else [])
                if any((A + B) % c == 0 for A, B in splits):
                    return True
            qi *= q
        return False
    for q in (7, 59, 5399):
        assert not q_in_support2(23317201, q), q
    assert not q_in_support2(10592401, 383) and q_in_support2(10592401, 19)
    ok('table rows; s=2911 (19 usable, 383 in no support-2 AB, signs +1 at 7,15); s=4319: negative primes 7,59,5399 '
       'occur in no support<=2 AB; B=62,c=7 works')
    # section 5 lemma brute force
    cs = [c for c in range(7, 200, 8) if gcd(c, 2) == 1]
    from sympy import totient, n_order
    cs = [c for c in cs if n_order(2, c) * 2 == totient(c)]
    nhyp = 0
    for p in primerange(3, 300000):
        if p % 8 != 1:
            continue
        for c in cs:
            if gcd(p, c) != 1 or jacobi_symbol(p, c) != -1:
                continue
            K = (p + c) // 4
            h = n_order(2, c)
            v2 = (K & -K).bit_length() - 1
            if v2 < h // 2:
                continue
            nhyp += 1
            assert support2_certs(K, c), (p, c)
    ok(f'section 5 lemma: every (p<3e5, c in {cs}) meeting the hypotheses has a support<=2 certificate at c ({nhyp} cases)')
    for s in range(15, 200000, 16):
        if s % 7 == 0:
            p = (5 * s * s - 1) // 4
            if isprime(p):
                assert support2_certs((p + 7) // 4, 7)
    ok('every prime of the quadratic family with 7 | s (s < 2e5) has support<=2 at shift 7')


def sec_census():
    print('[census] own BFS from O=(p,p,p,p) for the 53 Mordell-class primes < 20000 (four_orbit.csv)')
    rows = {}
    lines = (TAIL / 'four_orbit.csv').read_text().splitlines()
    hdr = lines[0].split(',')
    for ln in lines[1:]:
        r = dict(zip(hdr, ln.split(',')))
        rows[int(r['p'])] = r
    mord = [p for p in primerange(2, 20000) if p % 840 in (1, 121, 169, 289, 361, 529)]
    assert sorted(rows) == mord and len(mord) == 53
    F = {}
    def fz(d):
        if d not in F:
            F[d] = dict(factorint(d)) if d < 10 ** 15 else dict(fac(d))
        return F[d]
    def mergeable(s):
        return any((a * b) % (a + b) == 0 for a, b in combinations(s, 2))
    res = {}
    for p in mord:
        root = (p, p, p, p)
        seen = {root}
        layer = [root]
        depth = 0
        found = None
        while layer and depth <= 16 and len(seen) < 40000:
            if any(mergeable(s) for s in layer):
                found = depth
                break
            nxt = []
            for s in layer:
                for i, j in combinations(range(4), 2):
                    Fd = {s[i]: fz(s[i]), s[j]: fz(s[j])}
                    u, mv = pair_moves(s[i], s[j], Fd)
                    rest = [s[k] for k in range(4) if k not in (i, j)]
                    for a, b in mv:
                        t = tuple(sorted(rest + [a, b]))
                        if t not in seen:
                            assert sum(Fr(1, d) for d in t) == Fr(4, p)
                            seen.add(t)
                            nxt.append(t)
            layer = nxt
            depth += 1
        res[p] = found if found is not None else ('closed' if not layer else 'cap')
    for p in mord:
        r = rows[p]
        if r['status'] == 'hit':
            assert res[p] == int(r['first_merge']), (p, res[p], r)
        else:
            assert r['status'] == 'closed' and res[p] == 'closed', (p, res[p], r)
    assert [p for p in mord if res[p] == 'closed'] == [14281]
    ok('own BFS from O reproduces four_orbit.csv: 52 primes merge at the stated first-merge depth, 14281 closed')


SECTIONS = {'census': sec_census, 'group': sec_group, 'z72': sec_z72, 'phase43': sec_phase43, 'extremal': sec_extremal, 'mix': sec_mix,
            'tail': sec_tail, 'orbit': sec_orbit, 'composite': sec_composite, 'probe': sec_probe}

if __name__ == '__main__':
    names = sys.argv[1:] or list(SECTIONS)
    for nm in names:
        SECTIONS[nm]()
    print(f'ALL OK ({len(OK)} checks)')
