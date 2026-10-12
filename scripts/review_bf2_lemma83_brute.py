"""R163 from-scratch brute force of Lemma 8.3 (POINTWISE_BINARYFORM §8).

Enumerates ALL solutions 4/n = 1/x+1/y+1/z (x<=y<=z), for n = lam^2 w^2 <= NMAX
(lam odd prime, w odd >= 1; every decomposition of n is tested), via
  x in (n/4, 3n/4],  1/y+1/z = a/b  <=>  (a y - b)(a z - b) = b^2,
then tests every ordered permutation against the hypotheses of (a)-(e).
Independent of scripts/bf2_*.py.
Usage: PYTHONPATH=scripts uv run python scripts/review_bf2_lemma83_brute.py NMAX
"""
import sys
from math import gcd
from itertools import permutations


def spf_table(N):
    s = list(range(N + 1))
    for i in range(2, int(N ** 0.5) + 1):
        if s[i] == i:
            for j in range(i * i, N + 1, i):
                if s[j] == j:
                    s[j] = i
    return s


def factor(m, spf):
    f = {}
    while m > 1:
        p = spf[m]
        while m % p == 0:
            m //= p
            f[p] = f.get(p, 0) + 1
    return f


def legendre(a, p):
    a %= p
    if a == 0:
        return 0
    return 1 if pow(a, (p - 1) // 2, p) == 1 else -1


def solutions(n, spf):
    fn = factor(n, spf)
    out = []
    for x in range(n // 4 + 1, 3 * n // 4 + 1):
        a, b = 4 * x - n, n * x
        if a <= 0:
            continue
        g = gcd(a, b)
        a, b = a // g, b // g
        # b = n*x/g ; factor b^2 from factors of n and x
        fb = dict(fn)
        for p, e in factor(x, spf).items():
            fb[p] = fb.get(p, 0) + e
        for p, e in factor(g, spf).items():
            fb[p] -= e
        divs = [1]
        for p, e in fb.items():
            if e == 0:
                continue
            divs = [d * p ** k for d in divs for k in range(2 * e + 1)]
        bb = b * b
        for d in divs:
            if d > b or (d + b) % a:
                continue
            y = (d + b) // a
            e2 = bb // d
            if (e2 + b) % a:
                continue
            z = (e2 + b) // a
            if y < x:
                continue
            out.append((x, y, z))
    return out


def main():
    NMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 6000
    spf = spf_table(3 * NMAX)
    primes = [p for p in range(3, int(NMAX ** 0.5) + 1) if spf[p] == p]
    cnt = dict(a=0, b=0, c=0, d=0, e=0, viol=0, sols=0, ns=0)
    for lam in primes:
        w = 1
        while lam * lam * w * w <= NMAX:
            n = lam * lam * w * w
            S = solutions(n, spf)
            # sanity: each is a solution
            for (x, y, z) in S:
                assert 4 * x * y * z == n * (x * y + y * z + z * x)
            cnt['ns'] += 1
            cnt['sols'] += len(S)
            for s in S:
                for (x, y, z) in set(permutations(s)):
                    yz = y * z
                    # (a)
                    if x % n == 0 and y % lam == 0 and (y // lam) % lam and z % lam == 0 \
                            and (z // lam) % lam and gcd(w, yz) == 1:
                        cnt['a'] += 1
                        val = -(x // n) * (y // lam) * (z // lam)
                        if legendre(val, lam) != -1:
                            cnt['viol'] += 1
                            print('VIOL a', n, lam, w, (x, y, z))
                    # (b) (y,z ordering irrelevant)
                    if y % n == 0 and z % n == 0 and x % lam == 0 and (x // lam) % lam \
                            and gcd(w, x) == 1:
                        cnt['b'] += 1
                        if legendre(1 - 4 * (y // n), lam) != -1:
                            cnt['viol'] += 1
                            print('VIOL b', n, lam, w, (x, y, z))
                        if legendre(1 - 4 * (z // n), lam) != -1:
                            cnt['viol'] += 1
                            print('VIOL b(z)', n, lam, w, (x, y, z))
                    if x % n == 0 and y % (lam * lam) == 0 and z % (lam * lam) == 0 \
                            and gcd(w, yz) == 1:
                        cnt['c'] += 1
                        print('VIOL c', n, lam, w, (x, y, z))
                    if y % n == 0 and z % n == 0 and x % (lam * lam) == 0 and gcd(w, x) == 1:
                        cnt['d'] += 1
                        print('VIOL d', n, lam, w, (x, y, z))
                    if (x % n == 0 and gcd(n, yz) == 1) or \
                            (y % n == 0 and z % n == 0 and gcd(n, x) == 1):
                        cnt['e'] += 1
                        print('VIOL e', n, lam, w, (x, y, z))
            w += 2
    print('NMAX', NMAX, cnt)


if __name__ == '__main__':
    main()
