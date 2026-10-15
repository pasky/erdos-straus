"""O237 goal 4: best Lemma-1.1 cap over windows m <= M (CAP_DOWN Lemma 1.1, Type II at x, any m = 3 (mod 4)).

cap(m) = min e such that -1 = prod_{s | K} s^{delta_s} (mod m), K = (n+m)/4, b_s = v_s(K), with
  delta_s in [-b_s, b_s]  (all s, including 2),   or   delta_s in {b_s+2, ..., b_s+2e} (odd s only).
(D = K * prod s^delta_s is the divisor d of Lemma 1.1.)  cap 0 is a Type II ES solution.
For each n: best cap over m <= M, least m with cap 0, least m with cap <= 1.  Every VER-th n: the best solution is
rebuilt and checked with exact rationals against Def 1.1.
usage: z13_window_caps.py N M EMAX VER [primes|all]
"""
import sys
from fractions import Fraction
from math import gcd, isqrt
from sympy import isprime, factorint

N, M, EMAX, VER = map(int, sys.argv[1:5]); MODE = sys.argv[5] if len(sys.argv) > 5 else 'primes'
LIM = (N + M) // 4 + 2
spf = list(range(LIM + 1))
for i in range(2, isqrt(LIM) + 1):
    if spf[i] == i:
        for j in range(i * i, LIM + 1, i):
            if spf[j] == j:
                spf[j] = i


def fac(k):
    f = {}
    while k > 1:
        s = spf[k]; f[s] = f.get(s, 0) + 1; k //= s
    return f


def cap_at(n, m, emax):
    K = (n + m) // 4
    if gcd(K, n) != 1:
        return None
    fs = fac(K)
    for e in range(emax + 1):
        R = {1: ()}
        for s, b in fs.items():
            D = list(range(-b, b + 1))
            if s != 2:
                D += list(range(b + 2, b + 2 * e + 1, 2))
            sm = s % m
            if sm == 0:
                continue
            P = [(pow(sm, dd, m) if dd >= 0 else pow(pow(sm, -1, m), -dd, m), dd) for dd in D]
            R2 = {}
            for r, vec in R.items():
                for pv, dd in P:
                    rr = r * pv % m
                    if rr not in R2:
                        R2[rr] = vec + ((s, dd),)
            R = R2
        if (m - 1) % m in R or (m == 1):
            return e, K, R[(m - 1) % m]
    return None


def verify(n, m, K, vec, e):
    d = K
    num, den = 1, 1
    for s, dd in vec:
        if dd >= 0:
            num *= s ** dd
        else:
            den *= s ** (-dd)
    assert (K * num) % den == 0
    d = K * num // den
    assert (K + d) % m == 0
    A = (K + d) // m
    x, y, z = K, n * A, Fraction(n * K * A, d)
    assert Fraction(4, n) == Fraction(1, x) + Fraction(1, y) + 1 / z
    D = z.denominator; r = isqrt(D); assert r * r == D and r % 2 == 1
    for l, v in factorint(r).items():
        assert n % l and y % l == 0 and v <= e


hist = {}; m0max = (0, 0); m1max = (0, 0); worst = []; cnt = 0; nver = 0; sqw = 0
for n in range(5, N + 1, 4):
    if MODE == 'primes' and not isprime(n):
        continue
    r = isqrt(n)
    if r * r == n:
        for m in range(3, min(M, 400) + 1, 4):
            if gcd(m, n) == 1 and cap_at(n, m, 3) is not None:
                sqw += 1
        continue
    if MODE == 'all' and any(l % 4 == 3 for l in factorint(n)):
        continue
    cnt += 1
    best = None; m0 = m1 = None
    for m in range(3, M + 1, 4):
        if gcd(m, n) != 1:
            continue
        lim = EMAX if best is None else best[0] - 1
        if lim < 0:
            break
        c = cap_at(n, m, lim)
        if c is not None:
            best = (c[0], m, c[1], c[2])
            if c[0] <= 1 and m1 is None:
                m1 = m
            if c[0] == 0:
                m0 = m
    if best is None:
        hist['>' + str(EMAX)] = hist.get('>' + str(EMAX), 0) + 1; worst.append(n); continue
    hist[best[0]] = hist.get(best[0], 0) + 1
    if best[0] >= 1:
        worst.append((n, best[0], best[1]))
    if m0 is not None and m0 > m0max[0]:
        m0max = (m0, n)
    if m1 is not None and m1 > m1max[0]:
        m1max = (m1, n)
    if VER and cnt % VER == 0:
        verify(n, best[1], best[2], best[3], best[0]); nver += 1
print('N', N, 'M', M, 'mode', MODE, 'count', cnt, 'verified', nver)
print('best-cap histogram:', dict(sorted(hist.items(), key=lambda t: str(t[0]))))
print('max least cap-0 window:', m0max, ' max least cap<=1 window:', m1max)
print('n with best cap >= 1 (n, cap, window):', worst[:40], '... total', len(worst))
print('odd squares with a Lemma-1.1 window m <= 400, cap <= 3 (T1: must be 0):', sqw)
