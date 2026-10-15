"""R256 from-scratch: least Type II window m0(p) and Type-II-free non-squares.

Type II for n (ET): 4/n = 1/x + 1/y + 1/z, gcd(x, n) = 1, n | y, n | z.  With y = nY, z = nZ and m = 4x - n:
m/x = 1/Y + 1/Z  <=>  (mY - x)(mZ - x) = x^2  <=>  exists d | x^2, d = -x (mod m)  [gcd(x, m) = gcd(x, n) = 1].
Usage:  review_r256_m0.py brute  |  m0 N  |  free N
"""
import sys
from math import gcd, isqrt


def spf_sieve(N):
    s = list(range(N + 1))
    for i in range(2, isqrt(N) + 1):
        if s[i] == i:
            for j in range(i*i, N + 1, i):
                if s[j] == j:
                    s[j] = i
    return s


def factor(x, spf):
    f = {}
    while x > 1:
        q = spf[x]
        f[q] = f.get(q, 0) + 1
        x //= q
    return f


def window_fires(x, m, spf):
    """exists d | x^2 with d = -x mod m"""
    if m == 1:
        return True
    target = (-x) % m
    res = {1 % m}
    for q, e in factor(x, spf).items():
        pw = [pow(q, k, m) for k in range(2*e + 1)]
        res = {(r*w) % m for r in res for w in pw}
        if len(res) == m:
            break
    return target in res


def typeII_brute(n):
    """all Type II solutions by direct enumeration (small n); returns set of windows m"""
    ms = set()
    for x in range(n//4 + 1, n//2 + 1):
        if gcd(x, n) != 1:
            continue
        m = 4*x - n
        # m/x = 1/Y + 1/Z, Y <= Z: x/m < Y <= 2x/m
        for Y in range(x//m + 1, 2*x//m + 1):
            t = m*Y - x
            if t > 0 and (x*Y) % t == 0:
                ms.add(m)
                break
    return ms


def m0(p, spf):
    m = 3
    while True:
        x = (p + m)//4
        if window_fires(x, m, spf):
            return m
        m += 4


def primes_upto(N):
    s = bytearray([1])*(N + 1); s[0] = s[1] = 0
    for i in range(2, isqrt(N) + 1):
        if s[i]:
            s[i*i::i] = bytearray(len(s[i*i::i]))
    return [i for i in range(N + 1) if s[i]]


if __name__ == '__main__':
    mode = sys.argv[1]
    if mode == 'brute':
        spf = spf_sieve(10**5)
        bad = 0
        for p in primes_upto(3000):
            if p % 4 != 1:
                continue
            ms = typeII_brute(p)
            if min(ms) != m0(p, spf):
                bad += 1; print('MISMATCH', p, min(ms), m0(p, spf))
        for n in range(5, 3000, 4):
            ms = typeII_brute(n)
            fast = any(window_fires((n + m)//4, m, spf) for m in range(3, n + 1, 4) if gcd((n + m)//4, n) == 1)
            if bool(ms) != fast:
                bad += 1; print('MISMATCH-n', n, sorted(ms)[:3], fast)
        print('brute check mismatches:', bad)
    elif mode == 'm0':
        N = int(sys.argv[2])
        spf = spf_sieve(N//4 + 2000)
        hard = {1, 121, 169, 289, 361, 529}
        hist, rec, offbad, cnt = {}, [], 0, 0
        best = 0
        for p in primes_upto(N):
            if p % 4 != 1:
                continue
            cnt += 1
            m = m0(p, spf)
            if p <= 10**6:
                hist[m] = hist.get(m, 0) + 1
            if (p % 840) not in hard and m not in (3, 7):
                offbad += 1; print('OFF-CLASS m0>=11', p, m)
            if m > best:
                best = m; rec.append((p, m))
        print('N', N, 'primes=1(4):', cnt, 'off-class violations:', offbad)
        print('records:', rec)
        print('hist<=1e6:', sorted(hist.items()))
    elif mode == 'free':
        N = int(sys.argv[2])
        spf = spf_sieve(N)
        out = []
        for n in range(5, N + 1, 4):
            r = isqrt(n)
            if r*r == n:
                continue
            ok = False
            for m in range(3, n + 1, 4):   # x = (n+m)/4 <= n/2  <=>  m <= n
                x = (n + m)//4
                if gcd(x, n) == 1 and window_fires(x, m, spf):
                    ok = True; break
            if not ok:
                out.append(n)
        print('non-square n=1(4) <=', N, 'with f_II=0:', len(out))
        print(out)
