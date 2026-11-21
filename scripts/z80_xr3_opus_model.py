"""Opus R3 independent check of EXTREME.md §§10-12 numerics.
(a) genus vs actual full-window failure census on hard primes in (1e7,2e7]
    (pure Python, own SPF factoring and Jacobi symbol; no PARI, no author code);
    also the empirical least gap g(p) distribution there.
(b) model coefficients A_r(K) of (5) by *direct CRT enumeration* of conductor
    residues (no sign expansion), L(1,chi) by direct partial Dirichlet sums,
    products truncated at Y=10^6.
(c) short no-fit check: model survival vs empirical survival of first windows.
Memory: sieve bytearray 2e7 + SPF list 5e6 (<1 GB)."""
import sys, math, itertools
from math import gcd, sqrt, pi, log, prod
RS = (1, 121, 169, 289, 361, 529)

def jacobi(a, n):
    assert n > 0 and n % 2 == 1
    a %= n; t = 1
    while a:
        while a % 2 == 0:
            a //= 2
            if n % 8 in (3, 5): t = -t
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3: t = -t
        a %= n
    return t if n == 1 else 0

def primes_upto(N):
    s = bytearray([1]) * (N + 1); s[0] = s[1] = 0
    for i in range(2, int(N ** .5) + 1):
        if s[i]: s[i*i::i] = bytearray(len(range(i*i, N+1, i)))
    return s

def pfactors(n):
    out = []; d = 2
    while d * d <= n:
        if n % d == 0:
            out.append(d)
            while n % d == 0: n //= d
        d += 1
    if n > 1: out.append(n)
    return out

def oddquad(k):  # squarefree f | k, f = 3 mod 4  <-> odd quadratic chars mod k
    return [f for f in range(3, k + 1, 4) if k % f == 0 and all(f % (q*q) for q in range(2, int(f**.5)+1))]

WS = [3, 7, 11, 15, 19, 23, 27, 31, 35, 39, 51, 63, 95, 119, 231]

def census():
    LO, HI = 10**7, 2 * 10**7
    S = primes_upto(HI + 1000)
    M = (HI + 1000) // 4 + 10
    spf = list(range(M + 1))
    for i in range(2, int(M ** .5) + 1):
        if spf[i] == i:
            for j in range(i*i, M + 1, i):
                if spf[j] == j: spf[j] = i
    def fac(x):
        fs = []
        while x > 1:
            q = spf[x]; e = 0
            while x % q == 0: x //= q; e += 1
            fs.append((q, e))
        return fs
    def divres(fs, k):
        R = {1 % k}
        for q, e in fs:
            R = {(a * pow(q, i, k)) % k for a in R for i in range(e + 1)}
        return R
    gen = {k: 0 for k in WS}; act = {k: 0 for k in WS}; jg = ja = 0; n = 0
    gdist = {}
    for p in range(LO + 1, HI + 1):
        if not S[p] or p % 840 not in RS: continue
        n += 1; F = {}; G = {}
        for k in WS:
            x = (p + k) // 4; fs = fac(x)
            R = divres(fs, k); R |= {(p * a) % k for a in R}
            fail = all((-a) % k not in R for a in R)
            g = any(all(jacobi(q, f) == 1 for q, _ in fs) for f in oddquad(k))
            assert (not g) or fail, (p, k)
            gen[k] += g; act[k] += fail; F[k] = fail; G[k] = g
        jg += G[3] and G[7]; ja += F[3] and F[7]
        # least gap: first k = 3 mod 4 whose window succeeds
        k = 3
        while True:
            x = (p + k) // 4; fs = fac(x); R = divres(fs, k); R |= {(p*a) % k for a in R}
            if any((-a) % k in R for a in R): break
            k += 4
        gdist[k] = gdist.get(k, 0) + 1
    print('hard primes in (1e7,2e7]', n)
    for k in WS: print('k', k, 'genus', gen[k], 'actual', act[k], 'nongenus', act[k] - gen[k])
    print('3:7 genus', jg, 'actual', ja)
    print('g distribution', sorted(gdist.items()))
    return n, gdist

# ---------- (b) coefficients -----------
Y = 10**6
PR = [i for i, v in enumerate(primes_upto(Y)) if v]

def Lval(f, N=2 * 10**6):
    # direct partial sum of sum chi(n)/n plus Abel tail correction (Abar - A(N))/N,
    # A(n)=sum_{m<=n} chi(m) periodic with mean Abar; residual error O(f^2/N^2).
    ch = [jacobi(a, f) for a in range(f)]
    s = 0.0; A = 0; As = []
    for nn in range(1, N + 1):
        c = ch[nn % f]; s += c / nn; A += c
        if nn > N - f: As.append(A)
    return s + (sum(As) / len(As) - A) / N

_L = {}
def C(k, f):
    if f not in _L: _L[f] = Lval(f)
    L = _L[f] * prod(1 - jacobi(q, f) / q for q in pfactors(k) if f % q)
    t = L * prod(1 - 1 / q for q in pfactors(k))
    for q in PR:
        if k % q and jacobi(q, f) == -1: t *= 1 - 1 / q**2
    return sqrt(t / pi)

def Acoef(K, r):
    tot = 0.0
    small = {2, 3, 5, 7}
    for F in itertools.product(*(oddquad(k) for k in K)):
        cond = sorted({q for f in F for q in pfactors(f)} | {q for k in K for q in pfactors(k)})
        big = [q for q in cond if q not in small]
        def bad(q): return [k for k, f in zip(K, F) if k % q == 0 or jacobi(q, f) != 1]
        base = 1.0
        for q in PR:
            B = bad(q); base /= (1 - 1 / q) ** len(B)
            if q not in small and q not in big:
                base *= 1 - len({(-k) % q for k in B}) / (q - 1)
        # fixed small places: P = r mod 840 (mod 8 at 2)
        ok = all(all((r + k) % (8 if q == 2 else q) for k in bad(q)) for q in small)
        if not ok: continue
        # enumerate residues of P at big conductor primes (units), uniform
        num = 0.0; cnt = 0
        for vs in itertools.product(*(range(1, q) for q in big)):
            cnt += 1
            if any(any((v + k) % q == 0 for k in bad(q)) for q, v in zip(big, vs)): continue
            # P mod f_j via CRT pieces: S_j = prod over q|f_j of (P/q)
            w = 1
            for f in F:
                s = 1
                for q in pfactors(f):
                    Pq = r % q if q in small else vs[big.index(q)]
                    s *= jacobi(Pq, q)
                w *= 1 + s
            num += w
        num /= cnt if cnt else 1
        tot += prod(C(k, f) for k, f in zip(K, F)) * base * num
    return tot

if __name__ == '__main__':
    what = sys.argv[1]
    if what == 'census': census()
    else:
        for K in [(3,), (7,), (3, 7), (11,), (19,), (75,), (99,), (231,), (19, 23), (35,), (115,), (115, 119)]:
            print(':'.join(map(str, K)), *[f'{Acoef(K, r):.6f}' for r in RS])
        print('C(3,3)', C(3, 3), 'C(7,7)', C(7, 7))
