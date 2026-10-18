"""O276 numerics for POWER_LADDER_ES.md: the k-th power ladder ES_(k).

ES_(k)(n): 4/n = 1/x + 1/y + Q^k/Z, x,y,Z>0, gcd(Q,Z)=1, Q odd, gcd(Q,n)=1.
(1) odd k (3,5): Thm 2.1 construction, all primes 5<=p<=N, exact check + Type I shape.
(2) even k (4,6): Thm 2.3 construction (one prime r), exact check + Type II shape; stats of r, Q.
(3) T1 controls: odd squares / cubes.
(4) numerator 8 at 131, 241.
Usage: PYTHONPATH=scripts uv run python scripts/z44_ladder.py 1000000
"""
import sys
from fractions import Fraction
from math import gcd


def primes_upto(N):
    s = bytearray([1]) * (N + 1)
    s[0:2] = b"\x00\x00"
    for i in range(2, int(N ** 0.5) + 1):
        if s[i]:
            s[i * i::i] = bytearray(len(s[i * i::i]))
    return [i for i in range(N + 1) if s[i]]


SMALLP = primes_upto(5000)


def legendre(a, r):
    t = pow(a % r, (r - 1) // 2, r)
    return -1 if t == r - 1 else t


def check(num, n, x, y, Z, Q, k, shape):
    """exact check of num/n = 1/x + 1/y + Q^k/Z with lowest-terms, odd Q prime to n; shape test at primes of n."""
    assert x > 0 and y > 0 and Z > 0 and Q % 2 == 1 and gcd(Q, n) == 1
    assert Fraction(num, n) == Fraction(1, x) + Fraction(1, y) + Fraction(Q ** k, Z)
    assert gcd(Q, Z) == 1
    for l in [q for q in SMALLP if n % q == 0] or [n]:  # n prime or small factors
        if n % l:
            continue
        v = 0
        m = n
        while m % l == 0:
            m //= l
            v += 1
        vals = []
        for d in (x, y, Z):
            w = 0
            while d % l == 0:
                d //= l
                w += 1
            vals.append(w)
        big = sum(1 for w in vals if w >= v)
        unit = sum(1 for w in vals if w == 0)
        if shape == "I":
            assert big == 1 and unit == 2, (n, l, vals)
        elif shape == "II":
            assert big == 2 and unit == 1, (n, l, vals)


def odd_k(n, k, num=4):
    """Thm 2.1 (num=4) / numerator-m variant: m x = n + Q^k, Q ≡ -n (mod m), split 1/x = 2/(2x)."""
    Q = 1
    while (Q - (-n)) % num or gcd(Q, n) != 1 or Q % 2 == 0:
        Q += 1
        if Q > 10 ** 4:
            return None
    if pow(Q, k, num) != (-n) % num:
        return None
    x = (n + Q ** k) // num
    return (2 * x, 2 * x, n * x, Q)


def odd_part(t):
    while t % 2 == 0:
        t //= 2
    return t


def even_k(n, k, num=4):
    """Thm 2.3 construction: r ≡ -1 (mod num), r ≡ 3 (4), (-n/num | r)=... found by search; Q^k ≡ -n/num (mod r)."""
    kp = odd_part(k)
    bad = [l for l in SMALLP if kp % l == 0]
    for r in SMALLP:
        if r % num != num - 1 or r % 4 != 3 or n % r == 0:
            continue
        if any(r % l == 1 for l in bad):
            continue
        target = (-n * pow(num, -1, r)) % r
        if legendre(target, r) != 1:
            continue
        Q0 = next(q for q in range(1, r) if pow(q, k, r) == target)
        Q = Q0
        while Q % 2 == 0 or gcd(Q, n * (r + 1)) != 1:
            Q += r
        e = (n + num * Q ** k) // r
        assert (n + num * Q ** k) % r == 0 and (n + e) % num == 0
        x = (n + e) // num
        y = n * (r + 1) // num
        Zn = n * x * (r + 1)
        Zd = num * Q ** k
        g = gcd(Zn, Zd)
        assert Zd // g == Q ** k  # den(z) = Q^k
        Z = Zn // g
        return (x, y, Z, Q, r)
    return None


def main():
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 10 ** 5
    P = [p for p in primes_upto(N) if p >= 5]
    print(f"primes 5..{N}: {len(P)}")
    for k in (3, 5):
        mq = 0
        for p in P:
            x, y, Z, Q = odd_k(p, k)
            check(4, p, x, y, Z, Q, k, "I")
            mq = max(mq, Q)
        print(f"k={k}: Thm 2.1 solved all, Type I shape, max Q = {mq}")
    for k in (2, 4, 6):
        mr = mq = 0
        hist = {}
        for p in P:
            if p % 4 == 3:
                x = (p + 1) // 4
                check(4, p, 2 * x, 2 * x, p * x, 1, k, "I")
                continue
            res = even_k(p, k)
            assert res, p
            x, y, Z, Q, r = res
            check(4, p, x, y, Z, Q, k, "II")
            mr, mq = max(mr, r), max(mq, Q)
            hist[r] = hist.get(r, 0) + 1
        top = sorted(hist.items())[:6]
        print(f"k={k}: Thm 2.3 solved all p≡1(4), Type II shape, max r = {mr}, max Q = {mq}, r-hist {top}")
    # ES shot (Q = 1): p + 4 has a prime factor ≡ 3 (4)
    fail = 0
    for p in P:
        if p % 4 == 1:
            m, ok = p + 4, False
            for l in SMALLP:
                if l * l > m:
                    break
                while m % l == 0:
                    ok |= (l % 4 == 3)
                    m //= l
            ok |= (m > 1 and m % 4 == 3)
            fail += not ok
    print(f"ES modulus-4 shot (Q=1) fails at {fail} primes p≡1(4) (cf. ES^□/ES_(k): 0)")
    # T1 controls
    sq = [m * m for m in range(3, int(N ** 0.5) + 1, 2)]
    for k in (3, 5):
        for n in sq:
            x, y, Z, Q = odd_k(n, k)
            check(4, n, x, y, Z, Q, k, "I")
        cubes = [m ** 3 for m in range(3, int(round(N ** (1 / 3))) + 1, 2)]
        for n in cubes:
            x, y, Z, Q = odd_k(n, k)
            check(4, n, x, y, Z, Q, k, "I")
        print(f"k={k}: all {len(sq)} odd squares and {len(cubes)} odd cubes <= N solved with Type I shape")
    for k in (2, 4, 6):
        shots = 0
        for n in sq:
            m = int(round(n ** 0.5))
            for Q in range(1, 100, 2):
                if gcd(Q, m) != 1:
                    continue
                t = n + 4 * Q ** k
                for l in SMALLP:
                    if l * l > t:
                        break
                    if t % l == 0 and l % 4 == 3:
                        shots += 1
                        break
        print(f"k={k}: odd squares, Q<=99: {shots} modulus-4 shots (T1 predicts 0; trial division to 5000)")
    # numerator 8
    for p in (131, 241):
        for k in (3, 5):
            x, y, Z, Q = odd_k(p, k, num=8)
            check(8, p, x, y, Z, Q, k, "I")
            print(f"8/{p}, k={k}: 8/{p} = 1/{x} + 1/{y} + {Q}^{k}/{Z}")
        for k in (2, 4):
            res = even_k(p, k, num=8)
            if res:
                x, y, Z, Q, r = res
                check(8, p, x, y, Z, Q, k, "II")
                print(f"8/{p}, k={k}: r={r}: 8/{p} = 1/{x} + 1/{y} + {Q}^{k}/{Z}")
            else:
                print(f"8/{p}, k={k}: no r ≡ 7 (8) shot with r < 5000")


if __name__ == "__main__":
    main()
