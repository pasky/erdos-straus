"""O231 UNFORCED_WORDS §2: flip lemma census.  For primes p = 1 (8) in [LO,HI): enumerate all words (ordered), classify
non-certificate unforced words w by (a) 'flippable': some side N_X (X in t,u,v) has a prime r || N_X with psi(r)=-1 and
r = 1 (mod X), or a swap pair r | D, s | N_X/D (exact powers) with r = s (mod X), psi(r) != psi(s)  (D = A for X in {t,u},
B for X = v); (b) 'family-cert': one of its three families (same t / same u-value / same v-value) contains a certificate.
Flip Lemma says (a) => (b).  Output: totals + per-prime minima.  usage: z7_flip.py LO HI"""
import sys
from math import isqrt
LO, HI = int(sys.argv[1]), int(sys.argv[2])
M = 2 * HI + 10
spf = list(range(M + 1))
for i in range(2, isqrt(M) + 1):
    if spf[i] == i:
        for j in range(i * i, M + 1, i):
            if spf[j] == j: spf[j] = i
def jac(a, n):
    a %= n; r = 1
    while a:
        while a % 2 == 0:
            a //= 2
            if n % 8 in (3, 5): r = -r
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3: r = -r
        a %= n
    return r if n == 1 else 0
def factor(x):
    f = {}
    d = 2
    while x > M:  # trial division for large (t p + 1 up to ~p^2)
        while x % d == 0: f[d] = f.get(d, 0) + 1; x //= d
        d += 1 if d == 2 else 2
        if d * d > x:
            if x > 1: f[x] = f.get(x, 0) + 1
            return f
    while x > 1:
        r = spf[x]; f[r] = f.get(r, 0) + 1; x //= r
    return f
tot = dict(U_nc=0, flip=0, famcert=0, flip_not_fam=0)
for p in range(LO, HI):
    if p % 8 != 1 or p < 9 or spf[p] != p: continue
    W = []
    for u in range(1, p + 2):
        if (u - 2) * u > p: break
        x = p + u; fu = factor(x); ds = [1]
        for r, e in fu.items(): ds = [d * r ** k for d in ds for k in range(e + 1)]
        for v in ds:
            if v < u or (p + u + v) % (u * v): continue
            t = (p + u + v) // (u * v)
            W.append((t, u, v));
            if u != v: W.append((t, v, u))
    clean_cache = {}
    def fac_c(x):
        if x not in clean_cache: clean_cache[x] = factor(x)
        return clean_cache[x]
    def is_clean(x): return all(jac(r, p) != -1 for r in fac_c(x))
    cert_t, cert_u, cert_v = set(), set(), set()
    for (t, u, v) in W:
        if jac(t * u - 1, p) == -1: cert_t.add(t); cert_u.add(u); cert_v.add(v)
    for (t, u, v) in W:
        A, B = t * u - 1, t * v - 1
        if jac(A, p) == -1: continue
        sides = [(t, t * p + 1, A), (u, p + u, A), (v, p + v, B)]
        if any(is_clean(N) for _, N, _ in sides): continue
        tot['U_nc'] += 1
        fl = False
        for X, N, D in sides:
            f = fac_c(N)
            ex = [r for r, e in f.items() if (D % r == 0) == (D % r ** e == 0)]  # r^e exact part wholly in D or wholly out
            for r in ex:
                if jac(r, p) == -1 and f[r] == 1 and r % X == 1 % X: fl = True
            inD = [r for r in ex if D % r == 0 and f[r] == 1]; outD = [r for r in ex if D % r and f[r] == 1]
            for r in inD:
                for s in outD:
                    if (r - s) % X == 0 and jac(r, p) != jac(s, p): fl = True
        fc = (t in cert_t) or (u in cert_u) or (v in cert_v)
        tot['flip'] += fl; tot['famcert'] += fc; tot['flip_not_fam'] += (fl and not fc)
print(tot)
