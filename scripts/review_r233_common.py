"""R233 from-scratch helpers: SPF sieve, Jacobi symbol, cleanliness, word enumeration."""
import numpy as np


def spf_sieve(N):
    spf = np.zeros(N + 1, dtype=np.int64)
    for i in range(2, int(N ** 0.5) + 1):
        if spf[i] == 0:
            blk = spf[i * i::i]
            blk[blk == 0] = i
    idx = np.nonzero(spf == 0)[0]
    spf[idx] = idx
    return spf


def jacobi(a, n):
    assert n > 0 and n % 2 == 1
    a %= n
    s = 1
    while a:
        while a % 2 == 0:
            a //= 2
            if n % 8 in (3, 5):
                s = -s
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3:
            s = -s
        a %= n
    return s if n == 1 else 0


def factor(x, spf):
    out = {}
    if x < len(spf):
        while x > 1:
            r = int(spf[x])
            out[r] = out.get(r, 0) + 1
            x //= r
        return out
    r = 2
    while r * r <= x:
        while x % r == 0:
            out[r] = out.get(r, 0) + 1
            x //= r
        r += 1 if r == 2 else 2
    if x > 1:
        out[x] = out.get(x, 0) + 1
    return out


def clean(x, n, spf):
    """no prime r | x with (r/n) = -1"""
    return all(jacobi(r, n) != -1 for r in factor(x, spf))


def divisors(x, spf):
    ds = [1]
    for r, e in factor(x, spf).items():
        ds = [d * r ** k for d in ds for k in range(e + 1)]
    return ds


def word_data(t, u, v, n, spf):
    assert t * u * v - u - v == n
    A, B = t * u - 1, t * v - 1
    chi = jacobi(A, n)
    cA, cB, cu, cv = (clean(x, n, spf) for x in (A, B, u, v))
    forced = (cA and cB) or (cA and cv) or (cB and cu)  # N_t=AB, N_u=Av, N_v=Bu
    u2 = (not cA) and (not cB)
    return chi, forced, u2
