"""O252 numerics: statistics of K at the least cap-0 window (CAP_DOWN Lemma 1.1 slice, delta_p = 0, cap 0).

For every prime p = 1 (mod 4), p <= N, scan windows m = 3 (mod 4), gcd(m, p) = 1, m <= M (all m, prime or not):
K = (p+m)/4, cap 0 at m  <=>  -1 = d1/d2 (mod m) for divisors d1, d2 | K  <=>  P cap (-P) != {} with P = {d mod m : d | K}.
Records at the least cap-0 window m0(p): m0, primality, forced-ness (m prime, (m/p) = -1), K, P+(K), Omega(K), omega(K),
u = log K / log P+(K), tau(K^2), certificate (exponent vector delta = v(d1) - v(d2)), max |delta|, support size, largest
prime used, budget share sum|delta| / Omega(K).
Baseline: the same K-statistics at ALL scanned windows m <= m0 (failures) and success rate binned by tau(K^2)/m,
separately forced / unforced prime windows and composite windows.
Every VER-th certificate is rebuilt as an ES solution and checked with exact rationals (Type II: p | y, p | z).
usage: z24_least_window.py N M VER [outfile] [hard]   (hard: only Mordell-hard p mod 840 in {1,121,169,289,361,529})
"""
import sys
from fractions import Fraction
from math import gcd, isqrt, log
from collections import defaultdict

N, M, VER = map(int, sys.argv[1:4]); HARD = len(sys.argv) > 5 and sys.argv[5] == 'hard'
HARDC = {1, 121, 169, 289, 361, 529}
LIM = (N + M) // 4 + 2
spf = list(range(LIM + 1))
for i in range(2, isqrt(LIM) + 1):
    if spf[i] == i:
        for j in range(i * i, LIM + 1, i):
            if spf[j] == j:
                spf[j] = i
# primes up to N via sieve (bytearray)
isp = bytearray([1]) * (N + 1); isp[0] = isp[1] = 0
for i in range(2, isqrt(N) + 1):
    if isp[i]:
        isp[i * i::i] = bytearray(len(range(i * i, N + 1, i)))
smallp = [i for i in range(2, M + 1) if isp[i]] if M <= N else None


def isprime_small(m):
    return m >= 2 and spf[m] == m if m <= LIM else all(m % r for r in range(2, isqrt(m) + 1))


def fac(k):
    f = {}
    while k > 1:
        s = spf[k]; f[s] = f.get(s, 0) + 1; k //= s
    return f


def jacobi(a, n):
    a %= n; r = 1
    while a:
        while a % 2 == 0:
            a //= 2
            if n % 8 in (3, 5):
                r = -r
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3:
            r = -r
        a %= n
    return r if n == 1 else 0


def divisors_mod(fs, m):
    """dict residue -> exponent tuple (one divisor per residue)."""
    R = {1 % m: ()}
    for s, b in fs.items():
        R2 = dict(R)
        sm = s % m
        for r, vec in R.items():
            x = r
            for c in range(1, b + 1):
                x = x * sm % m
                if x not in R2:
                    R2[x] = vec + ((s, c),)
        R = R2
    return R


def cap0(fs, m):
    R = divisors_mod(fs, m)
    for r, v1 in R.items():
        t = (-r) % m
        if t in R:
            return v1, R[t]
    return None


def verify(p, m, K, v1, v2):
    d1 = 1; d2 = 1
    for s, c in v1:
        d1 *= s ** c
    for s, c in v2:
        d2 *= s ** c
    assert (d1 + d2) % m == 0
    # Lemma 1.1 with d = K*d1/d2 (exponents c_s = b_s + delta_s in [0, 2 b_s])
    g = gcd(d1, d2); d1 //= g; d2 //= g
    assert K % d2 == 0
    d = K // d2 * d1
    assert (K + d) % m == 0
    A = (K + d) // m
    x, y, z = K, p * A, Fraction(p * K * A, d)
    assert Fraction(4, p) == Fraction(1, x) + Fraction(1, y) + 1 / z
    assert z.denominator == 1 and y % p == 0 and z.numerator % p == 0


out = open(sys.argv[4], 'w') if len(sys.argv) > 4 else sys.stdout
recs = []
fail_m0 = 0
# baseline: windows tried (m <= m0); bins of log2(tau(K^2)/m)
bins = defaultdict(lambda: [0, 0])
perm = defaultdict(lambda: [0, 0])
hiF = []     # (kind, bin) -> [tries, successes]
kstat_win = defaultdict(float); kstat_all = defaultdict(float); nwin = 0; nall = 0
cnt = 0; nver = 0
for p in range(5, N + 1, 4):
    if not isp[p] or (HARD and p % 840 not in HARDC):
        continue
    cnt += 1
    found = None
    for m in range(3, M + 1, 4):
        if gcd(m, p) != 1:
            continue
        K = (p + m) // 4
        fs = fac(K)
        t2 = 1
        for b in fs.values():
            t2 *= 2 * b + 1
        Pp = max(fs)
        Om = sum(fs.values())
        ispr = isprime_small(m)
        kind = ('F' if jacobi(m, p) == -1 else 'U') if ispr else 'C'
        c = cap0(fs, m)
        bn = int(log(t2 / m, 2) // 1)
        bins[(kind, bn)][0] += 1
        perm[(m, kind)][0] += 1
        u = log(K) / log(Pp) if K > 1 else 0
        nall += 1; kstat_all['Om'] += Om; kstat_all['om'] += len(fs); kstat_all['u'] += u; kstat_all['lt2'] += log(t2)
        if c is None and kind == 'F' and bn >= 1 and len(hiF) < 40:
            hiF.append((p, m, K, dict(fs), round(t2 / m, 1), sorted(set(pow(s, (m - 1) // 2, m) and (s % m) for s in fs))))
        if c is not None:
            bins[(kind, bn)][1] += 1
            perm[(m, kind)][1] += 1
            v1, v2 = c
            nwin += 1; kstat_win['Om'] += Om; kstat_win['om'] += len(fs); kstat_win['u'] += u; kstat_win['lt2'] += log(t2)
            delta = defaultdict(int)
            for s, cc in v1:
                delta[s] += cc
            for s, cc in v2:
                delta[s] -= cc
            supp = {s: dd for s, dd in delta.items() if dd}
            found = (m, ispr, kind, K, Pp, Om, len(fs), u, t2, supp,
                     max([abs(x) for x in supp.values()] or [0]), max(supp or [1]),
                     sum(abs(x) for x in supp.values()) / Om)
            if VER and cnt % VER == 0:
                verify(p, m, K, v1, v2); nver += 1
            break
    if found is None:
        fail_m0 += 1; recs.append((p, None)); continue
    recs.append((p, found))

print('N', N, 'M', M, 'primes p=1(4):', cnt, 'verified exactly:', nver, 'no cap-0 window <= M:', fail_m0, file=out)
ok = [(p, f) for p, f in recs if f]
m0s = sorted(ok, key=lambda t: -t[1][0])
print('largest least cap-0 windows (p, m0, kind, K, P+, Omega, u, tau(K^2), delta):', file=out)
for p, f in m0s[:12]:
    print('  ', p, f[0], f[2], f[3], f[4], f[5], round(f[7], 2), f[8], dict(f[9]), file=out)
hist = defaultdict(int)
for p, f in ok:
    hist[f[0]] += 1
print('m0 histogram:', dict(sorted(hist.items())), file=out)
kh = defaultdict(int)
for p, f in ok:
    kh[f[2]] += 1
print('kind of least cap-0 window (F forced prime, U unforced prime, C composite):', dict(kh), file=out)
least_smooth = sorted(ok, key=lambda t: -(t[1][4] / t[1][3]))[:10]
print('least smooth K at m0 (largest P+(K)/K): (p, m0, K, P+, Omega, delta)', file=out)
for p, f in least_smooth:
    print('  ', p, f[0], f[3], f[4], f[5], dict(f[9]), file=out)
nprimeK = sum(1 for p, f in ok if f[4] == f[3])
print('K prime at m0:', nprimeK, file=out)
for key in ('Om', 'om', 'u', 'lt2'):
    print('mean %s: at successful windows %.3f, at all scanned windows %.3f' % (key, kstat_win[key] / max(nwin, 1), kstat_all[key] / max(nall, 1)), file=out)
mx = defaultdict(int); sz = defaultdict(int); share = []
for p, f in ok:
    mx[f[10]] += 1; sz[len(f[9])] += 1; share.append(f[12])
print('max |delta| histogram:', dict(sorted(mx.items())), file=out)
print('support size histogram:', dict(sorted(sz.items())), file=out)
print('mean budget share sum|delta|/Omega(K): %.3f' % (sum(share) / len(share)), file=out)
lp = defaultdict(int)
for p, f in ok:
    q = f[11]
    lp['<=7' if q <= 7 else '<=31' if q <= 31 else '<=1000' if q <= 1000 else '>1000'] += 1
print('largest prime used in certificate:', dict(lp), file=out)
print('success rate by kind and floor(log2(tau(K^2)/m)): kind bin tries succ rate', file=out)
for k in sorted(bins):
    t, s = bins[k]
    if t >= 50:
        print('  ', k[0], k[1], t, s, round(s / t, 3), file=out)
print('per-window success (m, kind, tries, succ, rate) for m <= 103 (tries counted only up to m0):', file=out)
for k in sorted(perm):
    t, sc = perm[k]
    if k[0] <= 103 and t >= 30:
        print('  ', k[0], k[1], t, sc, round(sc / t, 3), file=out)
print('forced-window FAILURES with tau(K^2)/m >= 2 (p, m, K, fac, ratio, residues of primes of K):', file=out)
for t in hiF:
    print('  ', t, file=out)
# T1 control: odd squares a^2 <= min(N, 10^6): no window m <= 200 with cap 0 (Lemma 1.1 slice) -- proved (CAP_DOWN sec. 3)
sqhit = 0; sqn = 0
for a in range(3, isqrt(min(N, 10**6)) + 1, 2):
    n = a * a; sqn += 1
    for m in range(3, 201, 4):
        if gcd(m, n) != 1 or (n + m) % 4:
            continue
        K = (n + m) // 4
        if gcd(K, n) != 1:
            continue
        if cap0(fac(K), m) is not None:
            sqhit += 1
print('T1 control: odd squares a^2 <= min(N,1e6):', sqn, ' (square, window) pairs with cap 0 at m <= 200:', sqhit, '(must be 0)', file=out)
