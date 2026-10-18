"""O276 §5: one mute prime q, ANY exponent (no parity normalisation).
ES^{<q>,*}(n): 4/n = 1/x + 1/y + 1/z, den z a power of q (q prime, q ∤ n).
(a) for each prime 3 <= q <= Qmax: witness = mod-4 trick (q ≡ 3 (4)), mod-3 trick (q ≡ 2 (3)), else least prime
    g ≡ 3 (4) with q a primitive root mod g.  Report max least g over q ≡ 1 (12).
(b) for q = 13 (g = 11): exact construction for all primes 5 <= p <= N, p ≠ 13, and odd squares; Type II shape check.
Usage: PYTHONPATH=scripts uv run python scripts/z44_one_mute.py 100000 1000000
"""
import sys
from fractions import Fraction
from math import gcd
from z44_ladder import primes_upto


def is_primroot(q, g):
    if q % g == 0:
        return False
    m, f, fs = g - 1, 2, set()
    while f * f <= m:
        while m % f == 0:
            fs.add(f)
            m //= f
        f += 1
    if m > 1:
        fs.add(m)
    return all(pow(q, (g - 1) // l, g) != 1 for l in fs)


def shot(n, q, g):
    """least c >= 0 with g | n + 4 q^c; Prop 2.1 formulas; returns (x,y,z) with z Fraction."""
    for c in range(g):
        W = q ** c
        if (n + 4 * W) % g == 0:
            e = (n + 4 * W) // g
            x = (n + e) // 4
            assert (n + e) % 4 == 0
            y = n * (g + 1) // 4
            z = Fraction(n * x * (g + 1), 4 * W)
            return x, y, z, c
    return None


def main():
    Qmax = int(sys.argv[1]) if len(sys.argv) > 1 else 10 ** 4
    N = int(sys.argv[2]) if len(sys.argv) > 2 else 10 ** 5
    G = primes_upto(10 ** 5)
    worst, cnt = (0, 0), 0
    for q in primes_upto(Qmax):
        if q < 3 or q % 4 == 3 or q % 3 == 2:
            continue
        cnt += 1
        g = next((g for g in G if g % 4 == 3 and g != q and is_primroot(q, g)), None)
        assert g, q
        worst = max(worst, (g, q))
    print(f"(a) primes q ≡ 1 (12) up to {Qmax}: {cnt}; each has a prime g ≡ 3 (4) with q primitive root; max least g = {worst[0]} (q = {worst[1]})")
    q, g = 13, 11
    P = [p for p in primes_upto(N) if p >= 5 and p not in (q, g)]
    maxc = 0
    for n in P + [m * m for m in range(3, int(N ** 0.5) + 1, 2) if m % 11 and m % 13]:
        x, y, z, c = shot(n, q, g)
        assert Fraction(4, n) == Fraction(1, x) + Fraction(1, y) + 1 / z
        d = z.numerator  # 1/z = den/num
        den = z.denominator
        while den % q == 0:
            den //= q
        assert den == 1  # den z is a power of q
        maxc = max(maxc, c)
    print(f"(b) q = 13, g = 11: all {len(P)} primes p <= {N} (p ≠ 11, 13) and odd squares (11, 13 ∤ m) solved; max exponent c = {maxc}")


if __name__ == "__main__":
    main()
