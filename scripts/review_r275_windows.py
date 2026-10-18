"""R275 from-scratch checks: Lemma 3.2 (incl. a strengthened Jacobi form), Gaussian supply, Prop 5.1 with ALL divisors.
Usage: review_r275_windows.py PMAX MMAX_LEMMA PMAX_LEMMA"""
import sys
from math import isqrt, gcd


def primes_upto(n):
    s = bytearray([1]) * (n + 1); s[0:2] = b"\0\0"
    for i in range(2, isqrt(n) + 1):
        if s[i]: s[i*i::i] = bytearray(len(s[i*i::i]))
    return [i for i in range(n + 1) if s[i]]


def jacobi(a, n):
    a %= n; r = 1
    while a:
        while a % 2 == 0:
            a //= 2
            if n % 8 in (3, 5): r = -r
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3: r = -r
        a %= n
    return r if n == 1 else 0


def fires(p, m):
    g = (-p) % (4 * m)
    return g > 0 and (m + 1) % g == 0


def sqrt_mod(n, p):  # Tonelli-Shanks
    n %= p
    if n == 0: return 0
    q, s = p - 1, 0
    while q % 2 == 0: q //= 2; s += 1
    z = 2
    while pow(z, (p - 1) // 2, p) != p - 1: z += 1
    mm, c, t, r = s, pow(z, q, p), pow(n, q, p), pow(n, (q + 1) // 2, p)
    while t != 1:
        i, t2 = 0, t
        while t2 != 1: t2 = t2 * t2 % p; i += 1
        b = pow(c, 1 << (mm - i - 1), p); mm, c, t, r = i, b * b % p, t * b * b % p, r * b % p
    return r


def cornacchia(D, p):
    if jacobi(-D % p, p) != 1: return None
    r = sqrt_mod(-D, p)
    if r < p - r: r = p - r
    a, b = p, r; lim = isqrt(p)
    while b > lim: a, b = b, a % b
    rest = p - b * b
    if rest % D: return None
    y2 = rest // D; y = isqrt(y2)
    return (b, y) if y * y == y2 else None


def divisors(n):
    ds = []
    for i in range(1, isqrt(n) + 1):
        if n % i == 0:
            ds.append(i)
            if i != n // i: ds.append(n // i)
    return ds


def odd_part(n):
    while n % 2 == 0: n //= 2
    return n


def main():
    PM = int(sys.argv[1]); ML = int(sys.argv[2]); PL = int(sys.argv[3])
    P = [p for p in primes_upto(PM) if p % 4 == 1]
    # ---- strengthened Lemma 3.2: (p/m') = +1 and (v2(m) even or p = 1 mod 8)  ==> m sterile
    tested = viol = 0; near = [0, 0]
    for p in P:
        if p > PL: break
        for m in range(1, ML + 1):
            mo = odd_part(m); s = (m // mo).bit_length() - 1
            if gcd(mo, p) != 1: continue
            if jacobi(p, mo) == 1 and (s % 2 == 0 or p % 8 == 1):
                tested += 1; viol += fires(p, m)
            elif jacobi(p, mo) == 1:   # s odd, p = 5 mod 8: hypothesis fails; does it fire sometimes?
                near[0] += 1; near[1] += fires(p, m)
    print(f"Strengthened Lemma 3.2 [(p/m')=+1 Jacobi, and v2(m) even or p=1(8)]: {tested} (p,m) pairs "
          f"(p<={PL}, m<={ML}), {viol} firings; complement (s odd, p=5(8), (p/m')=1): {near[1]}/{near[0]} fire")
    # ---- Gaussian supply + Prop 5.1 with all divisors
    st = {}
    def add(key, f):
        a = st.setdefault(key, [0, 0]); a[0] += 1; a[1] += f
    for p in P:
        reps = {}
        for D in (1, 2, 3, 7):
            r = cornacchia(D, p)
            if r:
                x, y = r
                assert x * x + D * y * y == p and gcd(x, D * y) == 1
                if D == 1 and x % 2 == 0: x, y = y, x
                reps[D] = (x, y)
        if p % 3 == 1:
            for M in range(1, isqrt(4 * p // 27) + 1):
                L2 = 4 * p - 27 * M * M; L = isqrt(L2)
                if L * L == L2: break
            else: raise ValueError(p)
            if L % 2 == 0 and M % 2 == 0: reps[27] = (L // 2, M // 2)   # p = (L/2)^2 + 27 (M/2)^2
            else: reps['27/4'] = (L, M)                                 # 4p = L^2 + 27 M^2, gcd(L, 27M) = 1
        for D, (x, y) in reps.items():
            DD = 27 if D == '27/4' else D
            assert gcd(x, DD * y) == 1, (p, D, x, y)
            for m in divisors(y):
                if m % 2: add((D, 'odd m|y'), fires(p, m))
            for m in divisors(x):
                if m % 2 and m > 1:
                    add((D, 'odd m|x, (D/m)=%+d' % jacobi(DD, m)), fires(p, m))
        # Gaussian supply: all m | ab odd; even m = 2^s m' with m' | ab, 1 <= s <= 2 v2(b) - 2
        a, b = reps[1]
        v = (b & -b).bit_length() - 1
        for m in divisors(a * b):
            if m % 2: add(('G', 'odd m|ab'), fires(p, m))
            else:
                s = (m & -m).bit_length() - 1
                if s + 2 <= 2 * v: add(('G', 'even m|ab, 2^(s+2)|b^2'), fires(p, m))
        add(('G', 'm=ab/2'), fires(p, a * b // 2))
    for k in sorted(st, key=str):
        n, f = st[k]
        print(f"{str(k):50s} trials {n:8d}  firings {f:6d}  ({100*f/n:.2f} %)")


if __name__ == "__main__":
    main()
