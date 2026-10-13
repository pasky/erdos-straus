"""O170: Eichler-Selberg trace formula (Cohen's form, Cohen-Stromberg Thm 12.4.11) for
Tr(T_n | S_k(Gamma0(N), chi)), k >= 2, chi(-1) = (-1)^k, gcd(n, N) = 1 not required except as in formula.
Returns the four terms A1..A4 separately, so the split-hyperbolic term A3 (where ES lives) can be inspected.
Self-tests: dim S_2(Gamma0(11)) = 1, Tr T_2 | S_12(1) = -24, dim S_2(Gamma0(N)) = genus.
"""
import cmath
from fractions import Fraction
from math import gcd, isqrt
from functools import lru_cache


def factor(n):
    f, p = {}, 2
    while p * p <= n:
        while n % p == 0:
            f[p] = f.get(p, 0) + 1
            n //= p
        p += 1
    if n > 1:
        f[n] = f.get(n, 0) + 1
    return f


def phi(n):
    r = n
    for p in factor(n):
        r = r // p * (p - 1)
    return r


def psi(n):
    r = n
    for p in factor(n):
        r = r // p * (p + 1)
    return Fraction(r, 1) if False else r


@lru_cache(None)
def h_w(D):
    """weighted class number of primitive forms of discriminant D < 0."""
    assert D < 0 and D % 4 in (0, 1)
    cnt = Fraction(0)
    a = 1
    while 3 * a * a <= -D:
        for b in range(-a + 1, a + 1):
            if (b * b - D) % (4 * a):
                continue
            c = (b * b - D) // (4 * a)
            if c < a:
                continue
            if b < 0 and c == a:
                continue
            if gcd(gcd(a, abs(b)), c) != 1:
                continue
            if a == b == c:
                cnt += Fraction(1, 3)
            elif b == 0 and a == c:
                cnt += Fraction(1, 2)
            else:
                cnt += 1
        a += 1
    return cnt


def characters(N):
    """all Dirichlet characters mod N as dicts a -> complex (a in units), via CRT on prime powers."""
    import itertools
    units = [a for a in range(1, N + 1) if gcd(a, N) == 1]
    if N == 1:
        return [{0: 1}]
    comps = []  # list of (modulus q, generator g, order o)
    for p, e in factor(N).items():
        q = p ** e
        if p == 2:
            if e >= 2:
                comps.append((q, q - 1, 2))
            if e >= 3:
                comps.append((q, 5, 2 ** (e - 2)))
        else:
            o = q // p * (p - 1)
            g = next(g for g in range(2, q) if gcd(g, p) == 1 and all(pow(g, o // r, q) != 1 for r in factor(o)))
            comps.append((q, g, o))
    # discrete logs of each unit in each component
    logs = {}
    for a in units:
        ex = []
        for (q, g, o) in comps:
            if q % 8 == 0 and g == q - 1:
                ex.append(0 if a % 4 == 1 else 1)
            elif q % 8 == 0 and g == 5:
                b = a if a % 4 == 1 else (-a) % q
                x, k = 1, 0
                while x != b % q:
                    x = x * 5 % q; k += 1
                ex.append(k)
            elif q == 4:
                ex.append(0 if a % 4 == 1 else 1)
            else:
                x, k = 1, 0
                while x != a % q:
                    x = x * g % q; k += 1
                ex.append(k)
        logs[a] = ex
    chars = []
    for js in itertools.product(*[range(o) for (_, _, o) in comps]):
        chars.append({a: cmath.exp(2j * cmath.pi * sum(js[i] * logs[a][i] / comps[i][2] for i in range(len(comps))))
                      for a in units})
    for c in chars[:3]:
        assert all(abs(c[a * b % N] - c[a] * c[b]) < 1e-9 for a in units for b in units)
    return chars


def chival(chi, N, a):
    if N == 1:
        return 1
    a %= N
    return chi.get(a, 0) if gcd(a, N) == 1 else 0


def conductor(chi, N):
    for M in sorted(d for d in range(1, N + 1) if N % d == 0):
        if all(abs(chi[a] - 1) < 1e-9 for a in chi if a % M == 1 % M):
            return M
    return N


def trace_terms(n, k, N, chi):
    f_chi = conductor(chi, N)
    A1 = A2 = A3 = A4 = 0
    r = isqrt(n)
    if r * r == n:
        A1 = n ** (k / 2 - 1) * chival(chi, N, r) * (k - 1) / 12 * psi(N)
    t = 0
    tmax = isqrt(4 * n)
    for t in range(-tmax, tmax + 1):
        D = t * t - 4 * n
        if D >= 0:
            continue
        rho = (t + cmath.sqrt(D)) / 2
        rhob = rho.conjugate()
        w = (rho ** (k - 1) - rhob ** (k - 1)) / (rho - rhob)
        s = 0
        f = 1
        while f * f <= -D:
            if D % (f * f) == 0 and (D // (f * f)) % 4 in (0, 1):
                Nf = gcd(N, f)
                mod = Nf * N
                mu = sum(chival(chi, N, x) for x in range(N) if (x * x - t * x + n) % mod == 0)
                mu *= psi(N) / psi(N // Nf)
                s += float(h_w(D // (f * f))) * mu
            f += 1
        A2 += -0.5 * w * s
    for d in range(1, n + 1):
        if n % d:
            continue
        dp = n // d
        inner = 0
        for tau in range(1, N + 1):
            if N % tau:
                continue
            g = gcd(tau, N // tau)
            if gcd(N // f_chi, dp - d) % g:
                continue
            # y = d mod tau, y = dp mod N/tau
            L = N // g
            ys = [y for y in range(L) if (y - d) % tau == 0 and (y - dp) % (N // tau) == 0]
            assert ys, (d, dp, tau)
            inner += phi(g) * chival(chi, N, ys[0])
        A3 += -0.5 * min(d, dp) ** (k - 1) * inner
    if k == 2 and all(abs(v - 1) < 1e-9 for v in chi.values()):
        A4 = sum(t for t in range(1, n + 1) if n % t == 0 and gcd(N, n // t) == 1)
    return A1, A2, A3, A4


def trace(n, k, N, chi):
    return sum(trace_terms(n, k, N, chi))


if __name__ == "__main__":
    triv = lambda N: [c for c in characters(N) if all(abs(v - 1) < 1e-9 for v in c.values())][0]
    print("dim S2(11) =", trace(1, 2, 11, triv(11)))
    print("Tr T2 S12(1) =", trace(2, 12, 1, triv(1)))
    print("dim S2(N), N=1..30:", [round(trace(1, 2, N, triv(N)).real, 6) for N in range(1, 31)])
    print("Tr T_n S2(11), n=1..10:", [round(trace(n, 2, 11, triv(11)).real, 6) for n in range(1, 11)])
