"""R278 from-scratch spot check of QUESTION_R §3 (reciprocity singular series M_R vs naive M0 vs actual N-).
Independent implementation: N_t = t n + 1 factored by a linear sieve over t (t = -n^{-1} mod q), not trial division.
Per n: actual N- (range divisors d = -1 mod t with (d/n) = -1), W (range divisors d = -1 mod t),
M_R = sum_{range d, chi(d)=-1} rho_R(t, e(d)),  M0 = sum_{range d} rho_0(t, e(d)), where for d = 2^e d_o,
chi(d) = (2/n)^e J(-t, d_o) (Prop 1.2, re-verified directly here: we compute (d/n) itself, not the formula), and
rho's are probabilities for a uniform odd unit a mod 4t:  rho_0 = P(a = -2^{-e} (t), (2/n)^e J(-t,a) = -1),
rho_R = rho_0 / P((2/n)^e J(-t,a) = -1).
Usage: uv run python scripts/review_r278_rss.py SETNAME [T]   (SETNAME in generic, K1, K24, K25, K4, sq, check)
Output: one line per n: n Nminus W MR M0
"""
import sys
from functools import lru_cache

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

def primes_upto(L):
    s = bytearray([1]) * (L + 1); s[0] = s[1] = 0
    for i in range(2, int(L ** .5) + 1):
        if s[i]: s[i * i::i] = bytearray(len(s[i * i::i]))
    return [i for i in range(L + 1) if s[i]]

PR = primes_upto(120000)

def isprime(m):
    if m < 2: return False
    for q in PR:
        if q * q > m: return True
        if m % q == 0: return m == q
    raise ValueError

@lru_cache(maxsize=None)
def rho(t, e, two_n):
    """returns (P(a=c mod t and J=s), P(J=s)) with s=-(two_n)^e, over odd units a mod 4t (gcd(a,t)=1)."""
    s = -(two_n ** e)
    if t % 2 == 1:
        c = (-pow(pow(2, e, t), -1, t)) % t if t > 1 else 0
    else:
        if e > 0: return (0.0, None)
        c = t - 1
    tot = hit = js = 0
    for a in range(1, 4 * t, 2):
        J = jac(-t, a)
        if J == 0: continue
        tot += 1
        if J == s:
            js += 1
            if a % t == c % t: hit += 1
    return (hit / tot, js / tot)

def analyse(n, T):
    two_n = 1 if n % 8 in (1, 7) else -1
    ts = [t for t in range(2, T + 1) if (2 * t - 1) ** 2 <= t * n + 1]
    if not ts: return (0, 0, 0.0, 0.0)
    tmax = ts[-1]
    rem = {t: t * n + 1 for t in ts}
    fac = {t: [] for t in ts}
    for q in PR:
        if q > 2 * int((tmax * n + 1) ** .5) + 2: break
        if n % q == 0:
            continue  # q | n => q does not divide tn+1
        t0 = (-pow(n, -1, q)) % q
        start = t0 if t0 >= 2 else t0 + q * ((2 - t0 + q - 1) // q)
        for t in range(start, tmax + 1, q):
            m = rem[t]; k = 0
            while m % q == 0: m //= q; k += 1
            if k: rem[t] = m; fac[t].append((q, k))
    act = W = 0; MR = M0 = 0.0
    for t in ts:
        F = fac[t]
        if rem[t] > 1:
            F = F + [(rem[t], 1)]
        N = t * n + 1
        divs = [1]
        for q, k in F:
            divs = [d * q ** j for d in divs for j in range(k + 1)]
        lo, hi = 2 * t - 1, N // (2 * t - 1)
        for d in divs:
            if d < lo or d > hi: continue
            e = (d & -d).bit_length() - 1
            chi = jac(d, n)
            p0, pJ = rho(t, e, two_n)
            M0 += p0
            if chi == -1 and pJ: MR += p0 / pJ
            if d % t == t - 1:
                W += 1
                if chi == -1: act += 1
    return (act, W, MR, M0)

def brute_words(n, T):
    """direct enumeration of words with t<=T: (t,u,v), A=tu-1 | tn+1."""
    a = W = 0
    for t in range(2, T + 1):
        u = 2
        while True:
            A = t * u - 1
            if A * (2 * t - 1) > t * n + 1: break
            if (t * n + 1) % A == 0:
                W += 1; a += (jac(A, n) == -1)
            u += 1
    return a, W

def sets(name):
    lo, hi = 400000, 4000000
    if name == 'generic':
        g = [p for p in range(1000001, 1060000, 4) if isprime(p)]
        return g[::10]
    if name == 'sq':
        return [m * m for m in range(633, 2000, 2)][::10]
    K = int(name[1:])
    L = []; m = int(lo ** .5)
    while m * m + K <= hi:
        p = m * m + K
        if p % 4 == 1 and isprime(p): L.append(p)
        m += 1
    return L

if __name__ == "__main__":
    name = sys.argv[1]; T = int(sys.argv[2]) if len(sys.argv) > 2 else 3000
    if name == 'check':
        for n in (1009, 9409, 10009, 233, 4001):
            r = analyse(n, T); b = brute_words(n, T)
            print(n, r, "brute (N-, W):", b, "OK" if (r[0], r[1]) == b else "MISMATCH")
        sys.exit()
    for n in sets(name):
        r = analyse(n, T)
        print(n, r[0], r[1], f"{r[2]:.4f}", f"{r[3]:.4f}", flush=True)
