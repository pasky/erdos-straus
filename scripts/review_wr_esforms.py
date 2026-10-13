"""R164 from-scratch check of WINDMILL_REDUCTION §2.
(a) Computation 2.3: primes p = 1 (24), p <= N, with no g=1 ES-form [k,4b,e], ke = p+4b^2, 4b | k+1, k,e > 0.
    Exhaustive over b <= (p+1)/3 (bound re-derived in the review). Also counts primes with no *reduced* ES-form
    (|B| <= k <= e).
(b) Lemma 2.4: for all positive definite [k,B,c] of disc -4gp with 4g|B, B|k+1 (small p,g), build the
    Egyptian fraction and verify 4/p = 1/x+1/y+1/z exactly with positive integers.
(c) Counter-example to Lemma 2.4 *as literally stated* (no positivity): [-1, 4g, -g(p+4g)].
"""
import sys
from fractions import Fraction as F
from math import isqrt


def primes(n):
    s = bytearray([1]) * (n + 1); s[0] = s[1] = 0
    for i in range(2, isqrt(n) + 1):
        if s[i]:
            s[i * i::i] = bytearray(len(s[i * i::i]))
    return [i for i in range(n + 1) if s[i]]


def esforms_g(p, g, bmax):
    """yield (k, B, c, b, e) with B = 4gb, ke = p+4gb^2, k = -1 mod 4gb, k,e>0."""
    for b in range(1, bmax + 1):
        mod = 4 * g * b
        M = p + 4 * g * b * b
        r = isqrt(M)
        # smaller factor is k (k = -1 mod mod) or e (e = -p mod mod)
        k = mod - 1
        while k <= r:
            if M % k == 0:
                yield (k, mod, g * (M // k), b, M // k)
            k += mod
        e0 = (-p) % mod
        e = e0 if e0 else mod
        while e <= r:
            if M % e == 0:
                k2 = M // e
                if k2 > r:  # avoid double count of k<=r
                    yield (k2, mod, g * e, b, e)
            e += mod


def lemma24_solution(p, g, k, B, c):
    b = B // (4 * g); e = c // g
    assert k * e == p + 4 * g * b * b and (p + e) % (4 * b * g) == 0
    N = (p + e) // 4; al = N // (b * g); be = b
    x = N
    y = F(p * N * (al + be), e * al); z = F(p * N * (al + be), e * be)
    return x, y, z


if __name__ == "__main__":
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 20000
    P = [p for p in primes(N) if p % 24 == 1]
    none, nored = [], []
    for p in P:
        fs = list(esforms_g(p, 1, (p + 1) // 3))
        if not fs:
            none.append(p)
        if not any(abs(B) <= k <= e for (k, B, c, b, e) in fs):
            nored.append(p)
    print(f"(a) {len(P)} primes p=1(24) <= {N}; no ES-form: {len(none)} {none}; no reduced ES-form: {len(nored)}")
    # (b)
    cnt = 0
    for p in primes(3000):
        if p < 3:
            continue
        for g in range(1, 6):
            for (k, B, c, b, e) in esforms_g(p, g, (p + 1) // 3 + 1):
                assert B * B - 4 * k * c == -4 * g * p and (k + 1) % B == 0
                x, y, z = lemma24_solution(p, g, k, B, c)
                assert y.denominator == 1 and z.denominator == 1 and y > 0 and z > 0
                assert F(4, p) == F(1, x) + 1 / y + 1 / z, (p, g, k, B, c)
                cnt += 1
    print(f"(b) Lemma 2.4 formula verified on {cnt} positive ES-forms, p<3000, g<=5")
    # (c)
    p, g = 97, 1
    k, B, c = -1, 4 * g, -g * (p + 4 * g)
    print("(c) [k,B,c] =", (k, B, c), "disc", B * B - 4 * k * c, "== -4gp", -4 * g * p, " B|k+1:", (k + 1) % B == 0)
