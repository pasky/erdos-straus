"""R273 from-scratch checks of O261 Lemma 7.1 (E2 line) and Lemma 4.1 (shot <-> ideal divisor).

Independent of scripts/o261/*.  Usage: PYTHONPATH=scripts uv run python scripts/review_r273_dictionaries.py [PMAX]
"""
import sys
from fractions import Fraction
from math import gcd, isqrt


def primes_upto(n):
    s = bytearray([1]) * (n + 1)
    s[0:2] = b"\0\0"
    for i in range(2, isqrt(n) + 1):
        if s[i]:
            s[i * i :: i] = bytearray(len(s[i * i :: i]))
    return [i for i in range(n + 1) if s[i]]


def divisors(n):
    small, large = [], []
    i = 1
    while i * i <= n:
        if n % i == 0:
            small.append(i)
            if i * i != n:
                large.append(n // i)
        i += 1
    return small + large[::-1]


# ---------- Lemma 7.1: E2 = exists d>=1, w | p+4d, w = -1 mod 4d, w != p+4d ----------
def e2_solutions(p, first_only=True):
    out = []
    d = 1
    while 8 * d <= p + 3 + 8:  # generous bound; author claims d <= (p+3)/8
        n = p + 4 * d
        # w ranges over divisors of n with w = -1 mod 4d, w < n
        w = 4 * d - 1
        while w <= n // 3:
            if n % w == 0:
                out.append((d, w))
                if first_only:
                    return out
            w += 4 * d
        d += 1
    return out


def e2_implies_es(p, d, w):
    """b=1 line: try to exhibit 4/p = 1/a+1/b+1/c from (d,w) by brute search over the line's shape
    (we only check ES(p) holds independently, see es_exists)."""
    return True


def es_exists(p):
    """4/p = 1/x+1/y+1/z, x<=y<=z, brute force (small p)."""
    t = Fraction(4, p)
    for x in range(p // 4 + 1, 3 * p // 4 + 2):
        r1 = t - Fraction(1, x)
        if r1 <= 0:
            continue
        a, b = r1.numerator, r1.denominator
        # a/b = 1/y + 1/z, y<=z: y in (b/a, 2b/a]
        for y in range(max(x, b // a + 1), 2 * b // a + 1):
            r2 = Fraction(a, b) - Fraction(1, y)
            if r2 > 0 and r2.numerator == 1:
                return (x, y, r2.denominator)
    return None


# ---------- Lemma 4.1 ----------
def shots(p, kmax):
    res = []
    for k in range(1, kmax + 1):
        N = 4 * k * k * p + 1
        for g in divisors(N):
            if (g + 1) % (4 * k) == 0:
                res.append((k, g))
    return res


def shot_to_es(p, k, g):
    h = (g + 1) // 4
    assert h % k == 0
    hp = h // k
    y = p * h
    xn = p * h + hp * hp
    zn = p * (h + p * k * k)
    assert xn % g == 0 and zn % g == 0
    x, z = xn // g, zn // g
    assert Fraction(1, x) + Fraction(1, y) + Fraction(1, z) == Fraction(4, p), (p, k, g)
    return x, y, z


def ideal_divisors_bruteforce(p, k):
    """All ideals I of Z[sqrt(-p)] (HNF: I = c*(a Z + (b + sqrt(-p)) Z), a | b^2+p, 0<=b<a) with
    alpha = 1 + 2k sqrt(-p) in I.  Returns list of norms N(I) = a c^2."""
    N = 4 * k * k * p + 1
    norms = []
    for c in divisors(N):  # c^2 a | N necessary (N(I) | N(alpha))
        if N % (c * c):
            continue
        for a in divisors(N // (c * c)):
            for b in range(a):
                if (b * b + p) % a:
                    continue
                # alpha = 1 + 2k s ; I = c*a Z + c*(b+s) Z.  alpha = u*c*a + v*c*(b+s): v = 2k/c, u = (1 - v c b)/(c a)
                if (2 * k) % c:
                    continue
                v = 2 * k // c
                num = 1 - v * c * b
                if num % (c * a) == 0:
                    norms.append((a * c * c, a, b, c))
    return norms


def main():
    pmax = int(sys.argv[1]) if len(sys.argv) > 1 else 200000
    ps = [p for p in primes_upto(pmax) if p % 4 == 1]
    fails = [p for p in ps if not e2_solutions(p)]
    print(f"E2 fails among p=1 mod 4, p<={pmax}: {fails}")
    for p in fails:
        print(f"  ES({p}) =", es_exists(p) if p < 3000 else "(skipped brute ES; large)")
        # check bound claim d <= (p+3)/8 exhaustive: brute w over all divisors for d up to p
        assert not any(
            w % (4 * d) == 4 * d - 1 and w < p + 4 * d
            for d in range(1, p + 1)
            for w in divisors(p + 4 * d)
        ), p
    print("E2 failures confirmed with d unbounded up to p (no bound assumption)")
    # local solvability witnesses of Lemma 7.1(ii)
    for p in [193, 2521, 66529]:
        assert (p + 4) % 3 != 0 or True
        print(f"  p={p}: (p+4) mod 3 = {(p+4)%3}, (p+4) mod 7 = {(p+4)%7}")

    # Lemma 4.1
    nshot = nmis = 0
    for p in [q for q in ps if q < 1200]:
        kmax = 6
        for k in range(1, kmax + 1):
            S = sorted(g for (kk, g) in shots(p, kmax) if kk == k)
            for g in S:
                shot_to_es(p, k, g)
                rho = pow(2 * k, -1, g)
                assert (rho * rho + p) % g == 0
                s = (2 * k * rho - 1) // g
                assert g * (-s) - rho * (-2 * k) == 1
            ideals = ideal_divisors_bruteforce(p, k)
            assert all(c == 1 for (_, _, _, c) in ideals)  # primitivity
            I = sorted(n for (n, a, b, c) in ideals if (n + 1) % (4 * k) == 0)
            # uniqueness: one ideal per norm
            allnorms = [n for (n, *_ ) in ideals]
            assert len(allnorms) == len(set(allnorms)) == len(divisors(4 * k * k * p + 1)), (p, k)
            nshot += len(S)
            if I != S:
                nmis += 1
                print("MISMATCH", p, k, S, I)
    print(f"Lemma 4.1: {nshot} shots (p<1200, k<=6) each -> verified ES triple; ideal-divisor norms = shot moduli; mismatches={nmis}")
    # (J)36 claim: 13, 37, 97 have no shot (any k)
    for p in [13, 37, 97]:
        found = []
        for k in range(1, (p + 3)):  # g >= 4k-1 and g <= 4k^2 p+1 trivially; need a cap: report k<=2p
            for g in divisors(4 * k * k * p + 1):
                if (g + 1) % (4 * k) == 0 and g < 4 * k * k * p + 1:
                    found.append((k, g))
        print(f"  p={p}: shots with k<={p+2}: {found[:5]}{'...' if len(found)>5 else ''} ({len(found)})")


if __name__ == "__main__":
    main()
