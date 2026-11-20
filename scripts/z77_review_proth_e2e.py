"""Usage: fixed N1023 N4095 | extra | x NC.
z77 hostile review: end-to-end replay of the Proth certificates at ACTUAL exponents.
Independent of z77_proth_verify.py: builds explicit ES triples (exact integer identity
4xyz = n(xy+yz+zx)) from each rule at the real n; X rows rebuilt from Moebius-product
cyclotomic values at the real x=2^r with an own subset search. M rows: Mordell list only.
"""
import json, random, sys
from math import gcd
from pathlib import Path
root = Path('data/z77/proth')

def ok(n, x, y, z):
    return min(x, y, z) > 0 and 4*x*y*z == n*(x*y + y*z + z*x)

def es_small(q):  # brute ES for small q
    for x in range(q//4 + 1, q + 1):
        num, den = 4*x - q, q*x
        if num <= 0: continue
        for y in range(max(x, den//num), 2*den//num + 2):
            a, b = num*y - den, den*y
            if a > 0 and b % a == 0: return (x, y, b//a)
    return None

def word_triples(n, t, u, v):
    A, B = t*u - 1, t*v - 1
    c = []
    if A % 4 == 0 and (n+v) % u == 0: d, b = A//4, (n+v)//u; c.append((b*d*n, v*d, b*v*d))
    if B % 4 == 0 and (n+u) % v == 0: d, b = B//4, (n+u)//v; c.append((b*d*n, u*d, b*u*d))
    if t % 4 == 0: a, b, cc = u, v, t//4; c.append((a*b*cc, a*cc*n, b*cc*n))
    if u % 4 == 0: w = u//4; f = B; c.append((w*f, t*n*w, t*n*w*f))
    if v % 4 == 0: w = v//4; f = A; c.append((w*f, t*n*w, t*n*w*f))
    return [x for x in c if ok(n, *x)]

def mobius(n):
    r, p = 1, 2
    while p*p <= n:
        if n % p == 0:
            n //= p
            if n % p == 0: return 0
            r = -r
        p += 1
    return -r if n > 1 else r

def phi(N, x):
    num = den = 1
    for e in range(1, N+1):
        if N % e == 0:
            mu = mobius(N//e)
            if mu == 1: num *= x**e - 1
            elif mu == -1: den *= x**e - 1
    q, r = divmod(num, den); assert r == 0; return q

def x_word(k, m, s, p):
    u = k - 1; q = s//m; assert s % (4*m) == 0
    while q % p == 0: q //= p
    x = 2**q; M = 8*u
    divs = [d for d in range(1, m+1) if m % d == 0]
    F = {d: phi(2*d, x) for d in divs}
    prod = 1
    for d in divs: prod *= F[d]
    assert prod == x**m + 1 and (2**s + 1) % (x**m + 1) == 0
    reach = {c % M: (c, ()) for c in range(1, k+1) if k % c == 0}
    for d in divs:
        fm = F[d] % M
        for res, (c, T) in list(reach.items()):
            reach.setdefault(res*fm % M, (c, T + (d,)))
    c, T = reach[(7*u - 1) % M]
    A = c
    for d in T: A *= F[d]
    n = k*2**s + 1
    assert (n + u) % A == 0 and (A + 1) % u == 0
    t, v = (A + 1)//u, (n + u)//A
    assert t*u*v - u - v == n and min(t, u, v) >= 2
    tr = word_triples(n, t, u, v); assert tr, (k, s)
    return q % ({255: 7, 1023: 9, 4095: 11}[k])

def check(k, rows, s, n=None):
    n = k*2**s + 1 if n is None else n
    for P, j, R, *z in rows:
        if s % P != j: continue
        if R == 'X': return R
        if R == 'M':
            r = n % 840
            if gcd(r, 840) > 1 or r not in {1, 121, 169, 289, 361, 529}: return R
        elif R == 'D':
            q = z[0]
            if n % q == 0:
                if q < 10**6: assert es_small(q)
                return R
        elif R == 'W':
            A, u = z
            if (n + u) % A == 0 and (A + 1) % u == 0:
                t, v = (A+1)//u, (n+u)//A
                if min(t, u, v) >= 2 and word_triples(n, t, u, v): return R
        elif R == 'II':
            f, a, b = z
            if (f+1) % (4*a*b) == 0 and (b*n + a) % f == 0:
                d = (f+1)//(4*a*b); e, r1 = divmod(n + 4*a*a*d, f); b2, r2 = divmod(n + e, 4*a*d)
                if r1 == r2 == 0 and ok(n, a*b2*d, a*b*d*n, b2*b*d*n): return R
        elif R == 'K':
            f, K0, Da, Eb = z
            K, r = divmod(n + f, 4)
            if r or K % K0: continue
            Dv = lambda t: t[0]*n**t[1]*(K//K0)**t[2]
            D, E = Dv(Da), Dv(Eb)
            if K0 % Da[0] == 0 and K0 % Eb[0] == 0 and (D + E) % f == 0:
                y, z2 = n*K*(D+E)//(D*f), n*K*(D+E)//(E*f)
                if (n*K) % D == 0 and (n*K) % E == 0 and ok(n, K, y, z2): return R
    raise AssertionError(('uncovered', k, s))

def main(k, H, files, nsamp, seed=1):
    rows = sum((json.loads((root/f).read_text())['rules'] for f in files), [])
    rnd = random.Random(seed)
    res = list(range(H)) if nsamp >= H else rnd.sample(range(H), nsamp)
    from collections import Counter
    cnt = Counter()
    for j in res:
        for s in ([j] if j >= 32 else []) + [j + H]:
            cnt[check(k, rows, s)] += 1
    print(k, 'classes', len(res), dict(cnt), flush=True)

if __name__ == '__main__':
    which = sys.argv[1]
    if which == 'fixed':
        main(255, 5040, ['255-5040-0.json'], 5040)
        main(1023, 55440, ['1023-55440-0.json', '1023-55440-extra.json'], int(sys.argv[2]))
        main(4095, 720720, ['4095-55440-0.json', '4095-720720-extra.json'], int(sys.argv[3]))
    elif which == 'extra':  # every row of the two -extra files at its first exponent >= 32
        for k, H, files in [(1023, 55440, ['1023-55440-0.json', '1023-55440-extra.json']),
                            (4095, 720720, ['4095-55440-0.json', '4095-720720-extra.json'])]:
            rows = sum((json.loads((root/f).read_text())['rules'] for f in files), [])
            from collections import Counter
            c = Counter(check(k, rows, j if j >= 32 else j + H) for P, j, R, *z in json.loads((root/files[1]).read_text())['rules'])
            print(k, 'extra rows end-to-end', dict(c), flush=True)
    else:  # X rows at actual s; report residues r mod h hit
        for k, m, p, classes, P in [(255, 315, 7, [0], 5040), (1023, 1155, 3, [0, 13860, 41580], 55440),
                                    (4095, 315, 11, [0, 25200, 30240], 55440)]:
            hit = set()
            for cl in classes:
                for c in range(int(sys.argv[2])):
                    s = cl + P*c
                    if s: hit.add(x_word(k, m, s, p))
            print(k, 'X residues r mod h verified', sorted(hit), flush=True)
