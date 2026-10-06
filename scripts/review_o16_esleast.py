"""R61 from-scratch check of OMEGA16 N2.

W(p) = min{M = 3 mod 4 : p = -4D (mod M), D | ((M+1)/4)^2}.
Mordell-hard: p a square mod 840.

usage: review_o16_esleast.py W <p>           -> W(p) by direct divisor search, hardness
       review_o16_esleast.py scan T lo hi     -> all primes in [lo,hi), square mod 840, with W>T
"""
import sys
import numpy as np


def divisors_of_square(a):
    f = {}
    x, d = a, 2
    while d * d <= x:
        while x % d == 0:
            f[d] = f.get(d, 0) + 1
            x //= d
        d += 1
    if x > 1:
        f[x] = f.get(x, 0) + 1
    divs = [1]
    for q, e in f.items():
        divs = [v * q**k for v in divs for k in range(2 * e + 1)]
    return divs


def W(p, Mmax=10**6):
    for M in range(3, Mmax, 4):
        A = (M + 1) // 4
        for D in divisors_of_square(A):
            if (p + 4 * D) % M == 0:
                return M, D
    return None


def is_prime(n):
    if n < 2:
        return False
    for q in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if n % q == 0:
            return n == q
    d, s = n - 1, 0
    while d % 2 == 0:
        d //= 2
        s += 1
    for a in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        x = pow(a, d, n)
        if x in (1, n - 1):
            continue
        for _ in range(s - 1):
            x = x * x % n
            if x == n - 1:
                break
        else:
            return False
    return True


def squares840():
    return sorted({(x * x) % 840 for x in range(840) if np.gcd(x, 840) == 1})


def scan(T, lo, hi, block=20_000_000):
    tables = []
    for M in range(3, T + 1, 4):
        A = (M + 1) // 4
        bad = np.zeros(M, dtype=bool)
        for D in divisors_of_square(A):
            bad[(-4 * D) % M] = True
        tables.append((M, bad))
    sq = np.array(squares840(), dtype=np.int64)
    out = []
    start = lo - lo % 840
    while start < hi:
        stop = min(start + block * 840 // len(sq), hi + 840)
        base = np.arange(start, stop, 840, dtype=np.int64)
        n = (base[:, None] + sq[None, :]).ravel()
        n = n[(n >= lo) & (n < hi) & (n > T)]
        for M, bad in tables:
            n = n[~bad[n % M]]
            if n.size == 0:
                break
        for v in n.tolist():
            if is_prime(v):
                out.append(v)
        start = stop - (stop - start) % 840 if (stop - start) % 840 else stop
    return out


if __name__ == "__main__":
    if sys.argv[1] == "W":
        p = int(sys.argv[2])
        print("p", p, "prime", is_prime(p), "p mod 840", p % 840,
              "square mod 840", p % 840 in squares840(), "W,D", W(p))
    else:
        T, lo, hi = int(sys.argv[2]), int(float(sys.argv[3])), int(float(sys.argv[4]))
        res = scan(T, lo, hi)
        print("T", T, "range", lo, hi, "count", len(res), "first", res[:5])
