"""Independent (Opus R3 reviewer) replay of notes/z80/PROTH_CORE.md Theorem 13 (§9): cover-22..30.json.
No repository script imported; pure stdlib (own Jacobi, own divisor/Moebius code).
 (A) per-row rule check on the whole class s = j mod P (s >= 64), at the row's own test modulus:
     periodicity (odd part: 2^P = 1; dyadic part <= 2^64), then the rule from first principles:
     M = Mordell classes typed by hand; D = q | n plus own direct triple for q; II/K = divisibility
     conditions of the explicit triples; W = word + ACTUAL Jacobi symbol (A/n) on a representative
     (sign is a function of n mod 8A since A = 1 mod 4 is NOT assumed: we use n mod 4A*? -> see below).
     X rows: different arithmetic from the repo: A mod H via AGGREGATED exponents of B_i=1+2^i
     (i = a*b mod h) instead of Moebius products on 2^(a+4h) mod 16H, and A mod 16 = c separately.
 (B) coverage by a chunked recursive bytearray sieve (child chunks of size <= CH built from whole
     prime powers of period/b), different from the repo's prime-by-prime residue tree with the
     55440 base sieve; every uncovered leaf would be reported.
 (C) brute box 513 <= s <= SMAX (repo box is 64..512): for EVERY s and EVERY non-X row whose class
     contains s, build the actual ES triple on the actual integer n (W via the five explicit
     Dedekind slices) and verify 4xyz = n(xy+yz+zx); plus s < 64 from z78 small.json re-verified.
 (D) the X-row core lemma on actual integers at small analogue parameters (h-part stripping incl.).
Run: ulimit -v 6000000; timeout 1800 uv run --offline --no-project python -B opus_r3_cover.py [SMAX]
"""
import json, sys, random, itertools
from math import gcd, lcm, isqrt, prod
from pathlib import Path
R = Path(__file__).resolve().parents[1] / 'proth'
SMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 1100
BAD840 = {1, 121, 169, 289, 361, 529}

def factor(n):
    f = {}; p = 2
    while p * p <= n:
        while n % p == 0: f[p] = f.get(p, 0) + 1; n //= p
        p += 1 if p == 2 else 2
    if n > 1: f[n] = f.get(n, 0) + 1
    return f

def divisors(n):
    ds = [1]
    for p, e in factor(n).items(): ds = [d * p ** i for d in ds for i in range(e + 1)]
    return sorted(ds)

def mu(n):
    f = factor(n); return 0 if any(e > 1 for e in f.values()) else (-1) ** len(f)

def jacobi(a, n):
    assert n > 0 and n % 2; a %= n; r = 1
    while a:
        while a % 2 == 0:
            a //= 2
            if n % 8 in (3, 5): r = -r
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3: r = -r
        a %= n
    return r if n == 1 else 0

def tri(n, x, y, z):
    assert min(x, y, z) > 0 and 4 * x * y * z == n * (x * y + y * z + z * x), (n, x, y, z)

def direct(q):
    for x in range(q // 4 + 1, 4 * q + 8):
        a, b = 4 * x - q, q * x; g = gcd(a, b); a //= g; b //= g
        for y in range(b // a + 1, 2 * b // a + 1):
            r = a * y - b
            if r > 0 and (b * y) % r == 0: return x, y, b * y // r
    raise ValueError(q)

def modulus(r):
    P, j, t, *z = r
    if t == 'M': return 840
    if t in ('D', 'II'): return z[0]
    if t == 'W': return 8 * z[0]
    if t == 'K':
        f, K, D, E = z; return 4 * f * K if (D[2] or E[2]) else 4 * lcm(f, K)
    raise ValueError(t)

# ---------- explicit triples on actual n ----------
def triple_actual(r, n):
    P, j, t, *z = r
    if t == 'M':
        assert n % 840 not in BAD840; return None        # Mordell + scaling (no explicit triple)
    if t == 'D':
        q = z[0]; assert n % q == 0; x, y, w = direct(q); c = n // q; return c * x, c * y, c * w
    if t == 'II':
        f, a, b = z; assert (f + 1) % (4 * a * b) == 0 and (b * n + a) % f == 0
        d = (f + 1) // (4 * a * b); bp = (b * n + a) // f
        return a * bp * d, a * b * d * n, bp * b * d * n
    if t == 'W':
        A, u = z; tt, r0 = divmod(A + 1, u); v, r1 = divmod(n + u, A); assert r0 == r1 == 0 and tt >= 2 and u >= 2 and v >= 2
        assert n == tt * u * v - u - v and n % 4 == 1 and jacobi(A, n) == -1
        if (tt * v - 1) % 4 == 0: D = (tt * v - 1) // 4; return A * D * n, u * D, A * u * D
        if (tt * u - 1) % 4 == 0: Ap = tt * v - 1; D = (tt * u - 1) // 4; return Ap * D * n, v * D, Ap * v * D
        if tt % 4 == 0: T = tt // 4; return T * u * v, T * v * n, T * u * n
        if u % 4 == 0: w = u // 4; f = tt * v - 1; return w * f, tt * n * w, tt * n * w * f
        if v % 4 == 0: w = v // 4; f = tt * u - 1; return w * f, tt * n * w, tt * n * w * f
        raise AssertionError('W row with no slice')
    if t == 'K':
        f, K0, Dd, Ee = z; assert f % 4 == 3 and (n + f) % (4 * K0) == 0
        K = (n + f) // 4
        def val(V):
            d, i, b = V; assert K0 % d == 0 and i in (0, 1) and b in (0, 1); return d * n ** i * (K // K0) ** b
        D, E = val(Dd), val(Ee); assert (D + E) % f == 0 and (n * K) % D == 0 and (n * K) % E == 0
        w = (D + E) // f; return K, n * K // D * w, n * K // E * w
    raise ValueError(t)

# ---------- (A) rule on the whole class, modulo the test modulus ----------
def rule_mod(r, k):
    P, j, t, *z = r; M = modulus(r); M2 = M & -M; Mo = M // M2
    Mk = Mo // gcd(Mo, k)                                # k(2^P-1) = 0 mod Mo  <=>  2^P = 1 mod Mo/(k,Mo)
    assert M2 <= 2 ** 64 and pow(2, P, Mk) == 1 % Mk
    s0 = j + P * max(0, -(-(64 - j) // P))
    nr = (k * pow(2, s0, M) + 1) % M                    # n mod M, the same for every s = j mod P, s >= 64
    if t == 'M': assert nr % 840 not in BAD840
    elif t == 'D': q = z[0]; assert q >= 2 and nr % q == 0; tri(q, *direct(q))
    elif t == 'II':
        f, a, b = z; assert min(f, a, b) > 0 and (f + 1) % (4 * a * b) == 0 and (b * nr + a) % f == 0
    elif t == 'W':
        A, u = z; tt, r0 = divmod(A + 1, u); assert r0 == 0 and tt >= 2 and u >= 2 and (nr + u) % A == 0
        assert (k << 64) + 1 + u >= 2 * A                 # v >= 2 already at s = 64
        # Jacobi (A/n) for n = nr mod 8A, n = 1 mod 8: by reciprocity it equals (n mod A / A) * sign(A,n)
        # and sign depends only on A mod 4, n mod 4; evaluate on a genuine positive representative n'
        # in the same class mod 8A (n' = nr + 8A*?), which has the same symbol.
        rep = nr if nr % 2 else nr + M
        assert rep % 8 == 1 and jacobi(A, rep) == -1
        v8 = ((rep + u) // A) % 4                         # v mod 4 is fixed on the class (8A | M)
        assert any(c % 4 == 0 for c in (tt, u, v8, A, tt * v8 - 1))
    elif t == 'K':
        f, K0, Dd, Ee = z; assert f % 4 == 3 and K0 > 0 and (nr + f) % (4 * K0) == 0
        Kq = ((nr + f) // (4 * K0)) % f                   # K/K0 mod f, valid since 4K0f | M when used
        def val(V):
            d, i, b = V; assert d > 0 and K0 % d == 0; return d * nr ** i * Kq ** b
        assert (val(Dd) + val(Ee)) % f == 0
    else: raise ValueError(t)

def x_row(r, m):
    P, j, t, e, W = r; h = 2 * m - 1; H = 2 ** h - 1; k = 4 ** m - 1
    assert t == 'X' and j == 0 and e % 2 == 1 and P % (4 * e) == 0
    assert sorted(int(a) for a in W) == [a for a in range(1, h) if gcd(a, h) == 1]
    De = set(divisors(e)); Bi = [(1 + pow(2, i, H)) % H for i in range(h)]
    for a, (c, I) in W.items():
        a = int(a); assert c > 0 and k % c == 0 and len(set(I)) == len(I) and set(I) <= De
        assert c % 16 == (14 * H - 1) % 16              # A = c mod 16 since Phi_{2d}(0)=1, 16 | X
        E = [0] * h
        for d in I:
            for b in divisors(d): E[a * b % h] += mu(d // b)
        A = c % H
        for i, x in enumerate(E):
            if x: A = A * pow(Bi[i], x, H) % H
        assert A == H - 1                                 # 7u-1 = 14H-1 = -1 mod H
    return len(W)

# ---------- (B) coverage ----------
def coverage(rows, L, CH=4096):
    F = factor(L); stats = {'nodes': 0, 'leaves': 0}
    def chunk(b):
        rem = L // b; c = 1
        for p in sorted(F):
            while rem % p == 0 and c * p <= CH: c *= p; rem //= p
        if c == 1:                                       # a single prime > CH: take it
            c = min(p for p in F if rem % p == 0)
        return c
    def node(a, b, R):
        stats['nodes'] += 1
        c = chunk(b); bb = b * c; cov = bytearray(c); nxt = []
        for P, jj in R:
            g = gcd(P, b); assert (jj - a) % g == 0
            if bb % P == 0:
                st = P // g; t0 = (jj - a) // g * pow(b // g, -1, st) % st
                cov[t0::st] = b'\1' * len(range(t0, c, st))
            else: nxt.append((P, jj))
        for t in range(c):
            if cov[t]: continue
            s = a + b * t
            Rn = [(P, jj) for P, jj in nxt if (jj - s) % gcd(P, bb) == 0]
            assert Rn, ('UNCOVERED', s, bb)
            assert bb < L
            node(s, bb, Rn)
    node(0, 1, [(r[0], r[1]) for r in rows])
    return stats['nodes']

# ---------- (D) X lemma on actual integers, small analogues ----------
def x_lemma_small():
    rng = random.Random(3); hits = 0
    for m in range(3, 9):
        h = 2 * m - 1; k = 4 ** m - 1; u = k - 1; H = 2 ** h - 1; hp = [p for p in factor(h)]
        for e in (3, 5, 9, 15, 21, 45):
            De = divisors(e); ck = divisors(k)
            for mult in (1, 3, 5, h, h * h, 3 * h, 7):
                s = 4 * e * mult
                r_ = s // e
                for p in hp:
                    while r_ % p == 0: r_ //= p
                if gcd(r_, h) != 1: continue
                X = 2 ** r_
                phi = {}
                for d in De:   # actual integer Phi_{2d}(X) by exact division
                    v = X ** d + 1
                    for dd in De:
                        if dd < d and d % dd == 0: v //= phi[dd]
                    phi[d] = v
                n = k * 2 ** s + 1
                for _ in range(300):
                    c = rng.choice(ck); I = [d for d in De if rng.random() < 0.5]
                    A = c * prod(phi[d] for d in I)
                    if (A - (7 * u - 1)) % (8 * u): continue
                    assert (n + u) % A == 0
                    tt = (A + 1) // u; v = (n + u) // A; assert tt % 8 == 7 and v % 8 == 7 and n == tt * u * v - u - v
                    D = (tt * v - 1) // 4; tri(n, A * D * n, u * D, A * u * D); hits += 1
    return hits

def main():
    # small s from z78 data, re-verified
    S = json.loads((R.parents[1] / 'z78/proth/small.json').read_text())
    for m in range(22, 31):
        for s, (x, y, z) in enumerate(S[m - 1]): tri((4 ** m - 1) * 2 ** s + 1, x, y, z)
    print('(0) s<64 triples for m=22..30 re-verified:', 9 * 64)
    print('(D) X core lemma on actual integers (small analogues):', x_lemma_small(), 'instances')
    for m in range(22, 31):
        c = json.loads((R / f'cover-{m}.json').read_text()); k = 4 ** m - 1; L = c['period']
        assert c['m'] == m and c['left'] == [] and all(L % r[0] == 0 and 0 <= r[1] < r[0] for r in c['rows'])
        nx = 0
        for r in c['rows']:
            if r[2] == 'X': nx += x_row(r, m)
            else: rule_mod(r, k)
        nodes = coverage(c['rows'], L)
        fixed = [r for r in c['rows'] if r[2] != 'X']; cnt = 0; ex = 0
        for s in range(513, SMAX + 1):
            n = (k << s) + 1; hit = False
            for r in fixed:
                if s % r[0] == r[1]:
                    T = triple_actual(r, n); hit = True; cnt += 1
                    if T: tri(n, *T); ex += 1
            assert hit or any(s % r[0] == r[1] for r in c['rows']), (m, s)
            assert hit, ('only X at small s?', m, s)
        xs = [(r[0], r[3]) for r in c['rows'] if r[2] == 'X']
        print(f'm={m} period={L} rows={len(c["rows"])} X(P,e)={xs} X-sources={nx} cover-nodes={nodes} '
              f'box 513..{SMAX}: {cnt} rule firings, {ex} explicit triples OK', flush=True)

if __name__ == '__main__':
    main()
