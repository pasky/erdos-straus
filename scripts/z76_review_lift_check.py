"""Hostile-review checks for notes/z76/PROOF_LIFT.md §§1-3 (scripts/z76_lift.py).  Run from repo root.
Brute force on small N = r^K: exact P-data, distinct oriented boxes, per-e compression, per-band moment bound,
per-dyadic-box large-e bounds, total boxes(B).  Random tests of the compression lemma, of tau((M/g)^2) <= M^{1/k}F(M),
of the short-interval sum (1), and of divcap against adversarial products V = lcm(u z_i - 1)."""
import sys, random
from math import gcd, isqrt, lcm
sys.path.insert(0, 'scripts')
from z76_lift import major, wheel, moment, divcap, boxes, rootup, ceildiv

def factor(n):
    f = {}; p = 2
    while p * p <= n:
        while n % p == 0: f[p] = f.get(p, 0) + 1; n //= p
        p += 1 if p == 2 else 2
    if n > 1: f[n] = f.get(n, 0) + 1
    return f

def divisors_from(f):
    ds = [1]
    for p, e in f.items(): ds = [d * p ** k for d in ds for k in range(e + 1)]
    return ds

def pdata(N, r):
    out = []
    a = 1
    while 2 * a * a <= N:
        d = 1
        while 2 * a * a * d <= N:
            V = N + 4 * a * a * d; u = 4 * a * d; c = 1
            while u * c - 1 <= V:
                f = u * c - 1
                if V % f == 0:
                    e = V // f; b = (N * c + a) // f
                    if (N * c + a) % f == 0 and a <= b and 4 * a * b * d == N + e and a + b == c * e and all(x % r for x in (a, b, c, d)):
                        out.append((a, b, c, d, e))
                c += 1
            d += 1
        a += 1
    return out

fails = 0
def check(cond, msg):
    global fails
    if not cond: fails += 1; print('FAIL', msg)

def band_bound(n, i):
    j = i + 1; m = (n + (1 << j)) // 4; H = ceildiv(1 << i, 4); arr = []
    for bits, cost in ((i // 2, 1), (i, 2)):
        G = wheel(bits)
        for k in range(3, 8):
            A, B, U = major(k, G); arr.append(cost * ceildiv(rootup(m, k) * (H * A + B), U))
    return min(arr)

def small_N(r, K):
    N = r ** K; W = r ** ((K + 1) // 2); B = (N - 1).bit_length()  # N <= 2^B
    D = pdata(N, r)
    boxes_all = set(); per_e = {}
    for (a, b, c, d, e) in D:
        f, f2 = 4 * a * c * d - 1, 4 * b * c * d - 1
        M = (N + e) // 4
        for (x, y, ff) in ((a, b, f), (b, a, f2)):
            ctr = (-ff) % W
            h = x * x * d
            check(ctr == (-h * pow(M, -1, W)) % W, f'centre N={N} {a,b,c,d,e}')
            check((M * M) % h == 0 and (h + M) % e == 0, f'h-class N={N}')
            boxes_all.add(ctr); per_e.setdefault(e, set()).add(ctr)
    # per-e compression and per-band
    band = {}
    for e, S in per_e.items():
        M = (N + e) // 4; fm = factor(M)
        hs = [h for h in divisors_from({p: 2 * v for p, v in fm.items()}) if (h + M) % e == 0]
        check(len(S) <= len(hs), f'compress N={N} e={e}')
        i = e.bit_length() - 1
        for bits, cost in ((i // 2, 1), (i, 2)):
            g = gcd(M, wheel(bits)); t = 1
            for p, v in factor(M // g).items(): t *= 2 * v + 1
            check(len(hs) <= cost * t, f'compress-bound N={N} e={e} g={g}')
        band[i] = band.get(i, 0) + len(S)
    for i, v in band.items(): check(v <= band_bound(1 << B, i), f'band N={N} i={i}')
    # large-e per dyadic box with j chosen by boxes(B)
    tot, j = boxes(B); n = 1 << B
    check(len(boxes_all) <= tot, f'total N={N}')
    cnt = {}
    for (a, b, c, d, e) in D:
        if e < (1 << j): continue
        key = (a.bit_length() - 1, d.bit_length() - 1, c.bit_length() - 1); cnt[key] = cnt.get(key, 0) + 1
    for (xa, yd, zc), v in cnt.items():
        s = xa + yd + zc
        check(s <= B - j - 1, f's-layer N={N}')
        bnd = min(1 << s, (1 << (xa + yd)) * divcap(B + 2, 2 + xa + yd, zc), (1 << (xa + zc)) * divcap(B + zc + 2, 2 + xa + zc, yd),
                  (1 << (zc + yd)) * divcap(B + 2 * zc + yd + 6, 2 + zc + yd, xa),
                  (1 << (xa + yd)) * (1 + (n // ((2 << s) - 1)) // (4 << (xa + yd))))
        check(v <= bnd, f'dyadic N={N} box={xa,yd,zc}')
    # per-pair checks (route A count, divcap per fixed pair) -- sharper than per box
    pairs = {}
    for (a, b, c, d, e) in D:
        if e < (1 << j): continue
        xa, yd, zc = a.bit_length() - 1, d.bit_length() - 1, c.bit_length() - 1
        for key in (('ad', a, d, xa, yd, zc), ('ac', a, c, xa, zc, yd), ('cd', c, d, zc, yd, xa)):
            pairs[key] = pairs.get(key, 0) + 1
    for (kind, p1, p2, x1, x2, z), v in pairs.items():
        mb = {'ad': B + 2, 'ac': B + x2 + 2, 'cd': B + 2 * x1 + x2 + 6}[kind]  # x2 = z_c for ac; (x1, x2) = (z_c, y_d) for cd
        check(v <= divcap(mb, 2 + x1 + x2, z), f'pair {kind} N={N} {p1,p2}')
    print(f'N={r}^{K}={N} B={B} data={len(D)} boxes={len(boxes_all)} bound={tot} j={j} ratio={tot/max(1,len(boxes_all)):.1f}', flush=True)

def random_tests(seed=1):
    rnd = random.Random(seed)
    # compression lemma on random highly composite M
    for _ in range(3000):
        M = 1
        for p in (2, 3, 5, 7, 11, 13, 17, 19, 23):
            M *= p ** rnd.choice((0, 0, 1, 1, 2, 3))
        M *= rnd.randrange(1, 50)
        e = rnd.randrange(1, 4000)
        if gcd(e, M) != 1: continue
        hs = [h for h in divisors_from({p: 2 * v for p, v in factor(M).items()}) if (h + M) % e == 0]
        for g in [x for x in divisors_from(factor(M)) if x <= e]:
            t = 1
            for p, v in factor(M // g).items(): t *= 2 * v + 1
            check(len(hs) <= 2 * t, f'rand-compress2 M={M} e={e} g={g}')
            if g * g <= e: check(len(hs) <= t, f'rand-compress1 M={M} e={e} g={g}')
    # short-interval sum (1) against exact tau sums on random intervals
    for _ in range(60):
        i = rnd.randrange(2, 14); H = ceildiv(1 << i, 4); M0 = rnd.randrange(1, 10 ** 7); m = M0 + H - 1
        for bits, cost in ((i // 2, 1), (i, 2)):
            G = wheel(bits)
            for k in range(3, 8):
                A, Bc, U = major(k, G)
                exact = 0
                for M in range(M0, M0 + H):
                    g = gcd(M, G); t = 1
                    for p, v in factor(M // g).items(): t *= 2 * v + 1
                    exact += t
                check(exact * U <= rootup(m, k) * (H * A + Bc), f'interval i={i} k={k} M0={M0}')
    # divcap against adversarial V = lcm of many u z - 1
    for _ in range(400):
        sb = rnd.randrange(2, 9); u = rnd.randrange(1 << sb, 1 << (sb + 1)); zb = rnd.randrange(1, 9)
        zs = rnd.sample(range(1 << zb, 1 << (zb + 1)), rnd.randrange(1, min(12, 1 << zb) + 1))
        V = 1
        for z in zs: V = lcm(V, u * z - 1)
        V *= rnd.randrange(1, 4)
        mb = V.bit_length()
        true = sum(1 for z in range(1 << zb, 1 << (zb + 1)) if V % (u * z - 1) == 0)
        check(true <= divcap(mb, sb, zb), f'divcap u={u} zb={zb} V={V} true={true} cap={divcap(mb,sb,zb)}')

if __name__ == "__main__" and len(sys.argv) == 1:
    random_tests()
    for r, K in ((3, 9), (5, 7), (7, 7), (11, 5), (13, 5), (3, 13), (17, 5), (101, 3), (19, 5)):
        small_N(r, K)
    print('fails', fails)
    sys.exit(1 if fails else 0)

# ---- realistic-scale band test (run with argument 'band'): exact compressed h-counts vs band bounds at N = r^3 ~ 2^60
def _isprime(n):
    if n < 2: return False
    for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if n % p == 0: return n == p
    d, s = n - 1, 0
    while d % 2 == 0: d //= 2; s += 1
    for a in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        x = pow(a, d, n)
        if x in (1, n - 1): continue
        for _ in range(s - 1):
            x = x * x % n
            if x == n - 1: break
        else: return False
    return True

def _rho(n):
    if n % 2 == 0: return 2
    for c in range(1, 100):
        x = y = 2; g = 1
        while g == 1:
            x = (x * x + c) % n; y = (y * y + c) % n; y = (y * y + c) % n; g = gcd(abs(x - y), n)
        if g != n: return g
    raise ValueError(n)

def factor_big(n, out=None):
    out = {} if out is None else out
    for p in range(2, 1000):
        while n % p == 0: out[p] = out.get(p, 0) + 1; n //= p
    stack = [n] if n > 1 else []
    while stack:
        m = stack.pop()
        if m == 1: continue
        if _isprime(m): out[m] = out.get(m, 0) + 1; continue
        g = _rho(m); stack += [g, m // g]
    return out

def band_test(r, K, imax):
    N = r ** K; B = (N - 1).bit_length()
    for i in range(imax + 1):
        tot = 0
        for e in range(1 << i, 1 << (i + 1)):
            if (N + e) % 4: continue
            M = (N + e) // 4
            if gcd(M, e) != 1 or M % r == 0: continue
            fm = factor_big(M)
            hs = sum(1 for h in divisors_from({p: 2 * v for p, v in fm.items()}) if (h + M) % e == 0)
            tot += hs
        bb = band_bound(1 << B, i)
        check(tot <= bb, f'bigband N={r}^{K} i={i}')
        print(f'  band r={r} K={K} B={B} i={i} exact_h={tot} bound={bb} ratio={bb/max(tot,1):.1f}', flush=True)

if __name__ == '__main__' and len(sys.argv) > 1 and sys.argv[1] == 'band':
    for r in (1000003, 1048573):
        band_test(r, 3, 9)
    print('fails', fails)
