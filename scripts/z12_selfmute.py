"""O236: the self-generated mute set construction (CAP_POINTWISE Thm 1.1).

For odd n = 1 (mod 4), non-square: pick a prime m = 4 - n (mod 8), (m/n) = -1, m not | n.
K := (m+n)/4 (odd), S := primes of K.  Find Q in <S> (as an integer) with Q^2 = -K (mod m),
g := (n+4Q^2)/m, shot solution x = (n+m)/4 = K, y = n(g+1)/4, z = n x (g+1)/(4Q^2).
Verify 4/n = 1/x+1/y+1/z exactly, and that den z = q^2, q odd, gcd(q,n)=1, rad q | y;
report e = max v_l(q) (the cap actually used).  Exponent search: minimise the cap.

usage: z12_selfmute.py N [mcount]   (all n = 1 mod 4 non-square, 5 <= n <= N; or primes only with 'p')
"""
import sys
from fractions import Fraction
from itertools import product
from math import gcd, isqrt
from sympy import factorint, jacobi_symbol, isprime, nextprime


def valid_ms(n, count):
    out = []
    m = 2
    while len(out) < count:
        m = nextprime(m)
        if m % 8 == (4 - n) % 8 and n % m and jacobi_symbol(m, n) == -1:
            out.append(m)
    return out


def best_Q(n, m, maxcap=None):
    """Return (cap, Q) minimising the cap over Q in <primes of K>, exponents reduced mod ord."""
    K = (m + n) // 4
    fK = factorint(K)
    S = sorted(fK)
    target = (-K) % m
    # discrete structure: exponents a_s in [0, ord_m(s)); search by increasing total box
    ords = []
    for s in S:
        o, v = 1, s % m
        while v != 1:
            v = v * s % m
            o += 1
        ords.append(o)
    best = None
    # increasing bound B on each exponent
    B = 0
    while True:
        for a in product(*[range(min(B, o - 1) + 1) for o in ords]):
            if max(a, default=0) != B and B > 0 and all(x < B for x in a):
                continue
            v = 1
            for s, x in zip(S, a):
                v = v * pow(s, 2 * x, m) % m
            if v == target:
                Q = 1
                for s, x in zip(S, a):
                    Q *= s ** x
                cap = shot_cap(n, m, Q)
                if best is None or cap < best[0]:
                    best = (cap, Q)
        if best is not None and best[0] <= 0:
            return best
        if B >= max(ords, default=1) or (best is not None and B >= best[0] + max(fK.values()) + 2):
            return best
        B += 1


def shot_cap(n, m, Q):
    N = n + 4 * Q * Q
    assert N % m == 0
    g = N // m
    assert g % 4 == 3
    x, y = (n + m) // 4, n * (g + 1) // 4
    assert (n + m) % 4 == 0 and (n * (g + 1)) % 4 == 0
    z = Fraction(n * x * (g + 1), 4 * Q * Q)
    assert Fraction(4, n) == Fraction(1, x) + Fraction(1, y) + 1 / z
    d = z.denominator
    q = isqrt(d)
    assert q * q == d and q % 2 == 1 and gcd(q, n) == 1 and y % max(1, _rad(q)) == 0
    return max(factorint(q).values(), default=0)


def _rad(q):
    r = 1
    for l in factorint(q):
        r *= l
    return r


if __name__ == "__main__":
    N = int(sys.argv[1])
    mcount = int(sys.argv[2]) if len(sys.argv) > 2 else 1
    primes_only = len(sys.argv) > 3 and sys.argv[3] == 'p'
    hist, mhist, worst = {}, {}, []
    cnt = 0
    for n in range(5, N + 1, 4):
        if isqrt(n) ** 2 == n or (primes_only and not isprime(n)):
            continue
        cnt += 1
        res = []
        for m in valid_ms(n, mcount):
            res.append((best_Q(n, m), m))
        (cap, Q), m = min(res)
        hist[cap] = hist.get(cap, 0) + 1
        m1 = res[0][1]
        worst.append((m1, n))
        worst.sort(reverse=True)
        worst = worst[:5]
    print("n checked", cnt, "cap histogram (best over first", mcount, "valid m):", sorted(hist.items()))
    print("largest least valid m:", worst)
