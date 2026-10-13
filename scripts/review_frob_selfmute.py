"""R196 from-scratch check of FROBENIUS_FIRING §4/§5.1 (self-mute ES^{(y)}, ES^{(s)}, Cor 4.3).
Own Miller-Rabin + Pollard rho; own exact verification with Fractions. Nothing imported from ff_frob_* / uo_*.

usage: review_frob_selfmute.py N [JMAX]       (primes 5 <= p < N, p != 3, and odd squares m^2 < N, 3 nmid m)
       review_frob_selfmute.py cor43 TRIALS   (Cor 4.3 iff-test on random shots, S = {3,5,7,11})
"""
import sys, random, math
from fractions import Fraction
from collections import Counter

random.seed(196)


def is_prime(n):
    if n < 2:
        return False
    for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if n % p == 0:
            return n == p
    d, s = n - 1, 0
    while d % 2 == 0:
        d //= 2; s += 1
    for a in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41):
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


def rho(n):
    if n % 2 == 0:
        return 2
    while True:
        c = random.randrange(1, n); y = random.randrange(0, n); m = 128; g = r = qq = 1
        while g == 1:
            x = y
            for _ in range(r):
                y = (y * y + c) % n
            k = 0
            while k < r and g == 1:
                ys = y
                for _ in range(min(m, r - k)):
                    y = (y * y + c) % n
                    qq = qq * abs(x - y) % n
                g = math.gcd(qq, n); k += m
            r *= 2
        if g == n:
            g = 1
            while g == 1:
                ys = (ys * ys + c) % n
                g = math.gcd(abs(x - ys), n)
        if g != n:
            return g


def primes_of(n):
    out = set()
    for p in range(2, 1000):
        if n % p == 0:
            out.add(p)
            while n % p == 0:
                n //= p
    stack = [n] if n > 1 else []
    while stack:
        m = stack.pop()
        if m == 1:
            continue
        if is_prime(m):
            out.add(m); continue
        d = rho(m)
        stack += [d, m // d]
    return out


def val(n, p):
    v = 0
    while n % p == 0:
        n //= p; v += 1
    return v


def build(n, Q, r):
    """UNIT_ORBIT Prop 2.1 formulas, recomputed here."""
    a = n + 4 * Q * Q
    assert a % r == 0
    e = a // r
    x = Fraction(n + e, 4); y = Fraction(n * (r + 1), 4); z = n * x * Fraction(r + 1, 4) / (Q * Q)
    return x, y, z


def check_esy(n, x, y, z, S=None):
    """returns (is ES^{(y)} solution, is ES solution, is ES^{(S)} solution if S given)."""
    if not (x.denominator == 1 and y.denominator == 1 and x > 0 and y > 0 and z > 0):
        return False, False, False
    if Fraction(4, n) != 1 / x + 1 / y + 1 / z:
        return False, False, False
    den = z.denominator
    es = den == 1
    ok_y = True; ok_S = True
    for l in primes_of(den) if den > 1 else []:
        v = val(den, l)
        if not (int(y) % l == 0 and l != 2 and n % l != 0 and v % 2 == 0):
            ok_y = False
        if S is not None and not (l in S and v % 2 == 0):
            ok_S = False
    return ok_y, es, ok_S


def least_j(n, s, jmax, variant):
    """variant 's': ES^{(s)}; 'y': ES^{(y)} (true criterion: any r with the solution in ES^{(y)});
    'y12': author's stricter criterion r = 11 mod 12 for all j (incl. j = 0)."""
    for j in range(jmax + 1):
        Q = s ** j
        for r in sorted(primes_of(n + 4 * Q * Q)):
            if r % 4 != 3:
                continue
            if variant == 'y12' and r % (4 * s) != 4 * s - 1:
                continue
            x, y, z = build(n, Q, r)
            oy, es, oS = check_esy(n, x, y, z, S={s})
            good = oS if variant == 's' else oy
            if good:
                return j
    return None


def main_scan(N, jmax):
    sieve = bytearray([1]) * N; sieve[0] = sieve[1] = 0
    for i in range(2, int(N ** 0.5) + 1):
        if sieve[i]:
            sieve[i * i::i] = bytearray(len(sieve[i * i::i]))
    ps = [p for p in range(5, N) if sieve[p]]
    s = 3
    for variant in ('s', 'y', 'y12'):
        h = Counter(); uns = []
        for p in ps:
            j = least_j(p, s, jmax, variant)
            h[j] += 1
            if j is None:
                uns.append(p)
        print(f"primes 5<=p<{N} (#={len(ps)}) variant {variant}: hist {dict(sorted((k, v) for k, v in h.items() if k is not None))} unsolved {len(uns)} {uns[:10]}")
    sq = [m * m for m in range(3, int(N ** 0.5) + 2, 2) if m * m < N and m % 3]
    hits = 0
    for n in sq:
        for j in range(0, 16):
            if any(r % 4 == 3 for r in primes_of(n + 4 * 9 ** j)):
                hits += 1; print("SQUARE HIT", n, j)
    print(f"odd squares m^2<{N}, 3 nmid m: {len(sq)}; hits with j<=15: {hits}")


def cor43(trials):
    S = [3, 5, 7, 11]
    mism = 0; tested = Counter()
    for _ in range(trials):
        n = random.randrange(5, 10 ** 5) | 1
        if any(n % s == 0 for s in S):
            continue
        Q = 1
        for s in S:
            Q *= s ** random.choice([0, 0, 1, 2, 3])
        for r in primes_of(n + 4 * Q * Q):
            if r % 4 != 3:
                continue
            x, y, z = build(n, Q, r)
            oy, es, oS = check_esy(n, x, y, z, S=set(S))
            k = (r + 1) // 4
            rad = math.prod(s for s in S if Q % s == 0)
            pred_y = k % rad == 0; pred_es = k % Q == 0
            tested[(pred_y, pred_es)] += 1
            if oy != pred_y or es != pred_es or not oS:
                mism += 1; print("MISMATCH", n, Q, r, oy, pred_y, es, pred_es, oS)
    print("Cor 4.3 shots tested by (pred ES^y, pred ES):", dict(tested), "mismatches", mism)


if __name__ == '__main__':
    if sys.argv[1] == 'cor43':
        cor43(int(sys.argv[2]))
    else:
        main_scan(int(sys.argv[1]), int(sys.argv[2]) if len(sys.argv) > 2 else 40)
