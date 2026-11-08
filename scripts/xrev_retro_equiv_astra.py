"""Independent boundary/screen audit for REVIEW_EQUIV_ASTRA.md (stdlib only).

Run: ulimit -v 4000000; timeout 120 uv run scripts/xrev_retro_equiv_astra.py
The existing z64_equiv scripts already cover the basic dictionaries and sign
census. This checks missing scope boundaries and enumerates orbifold exceptions
without either the original NMAX or its fourth-cone cutoff. All loops are bounded;
no dense arrays or Cartesian-product materializations are used.
"""
from fractions import Fraction as F
from math import ceil, isqrt
from pathlib import Path


def egyptian3(k, n):
    """Exhaustive sorted positive denominators for k/n < 1."""
    for x in range(n // k + 1, 3 * n // k + 1):
        remainder = F(k, n) - F(1, x)
        lo = max(x, remainder.denominator // remainder.numerator + 1)
        for y in range(lo, int(2 / remainder) + 1):
            last = remainder - F(1, y)
            if last.numerator == 1:
                z = last.denominator
                assert z >= y
                return x, y, z
    return None


def sporadic_four(k):
    """Sorted (a,b,c,d), excluding (2,2,c,d), with sum=1+k/n, n odd>k.

    sum>1 bounds a<=3, b<=5, c<=11. For s=sum(first three)-1:
    s>0 bounds n<k/s; s=0 forces n=k*d even; s<0 bounds d<-1/s.
    Thus neither an n cutoff nor an arbitrary d cutoff is required.
    """
    result = {}
    negative_max = (F(0), ())
    for a in range(2, 4):
        for b in range(a, 6):
            if (a, b) == (2, 2):
                continue
            for c in range(b, 12):
                s = F(1, a) + F(1, b) + F(1, c) - 1
                if s + F(1, c) <= 0:
                    continue
                if s > 0:
                    for n in range(k + 1, ceil(k / s), 2):
                        d = 1 / (F(k, n) - s)
                        if d.denominator == 1 and d >= c:
                            result.setdefault(n, []).append((a, b, c, int(d)))
                elif s < 0:
                    for d in range(c, ceil(-1 / s)):
                        n = k / (s + F(1, d))
                        negative_max = max(negative_max, (n, (a, b, c, d)))
                        if n.denominator == 1 and n > k and n.numerator % 2:
                            result.setdefault(int(n), []).append((a, b, c, d))
    return result, negative_max


def stars(n):
    """Complete: n >= 4C-2 and u+B <= n for positive (u,B,C)."""
    for c in range(1, (n + 2) // 4 + 1):
        for u in range(1, n):
            q, r = divmod(n + u, 4 * c * u - 1)
            if r == 0 and q >= 1:
                yield u, q, c


def word(n):
    """Complete W decision with symmetric endpoints u<=v.

    Choose the middle letter t first. Since u,v>=2, t<=(n+4)/4.
    For fixed t, t*u*u-2*u<=n bounds the smaller endpoint.
    """
    for t in range(2, (n + 4) // 4 + 1):
        for u in range(2, (1 + isqrt(1 + t * n)) // t + 1):
            v, r = divmod(n + u, t * u - 1)
            if r == 0 and v >= u:
                return t, u, v
    return None


def main():
    for k in (4, 8):
        result, negative_max = sporadic_four(k)
        print(f"{k}/n sporadic odd n: {sorted(result)}")
        print(f"  s<0 maximum n and signature: {negative_max}")
        for n in sorted(result):
            witness = egyptian3(k, n)
            assert witness is not None, (k, n, result[n])
            assert sum((F(1, x) for x in witness), F(0)) == F(k, n)
            print(f"  {k}/{n}: {witness}")
        # r=5 forces (2,2,2,a,b). Four 2's give n=k*b;
        # exactly three give (a,b)=(3,3),(3,4),(3,5), n=6k,12k,30k.
        assert all(n % 2 == 0 for n in (6 * k, 12 * k, 30 * k))

    # The memo's unqualified r=4 bound fails even for odd n:
    # n=4q-1, (2,2,q,nq); use q=2000 to exceed 6888.
    q = 2000
    n = 4 * q - 1
    signature = (2, 2, q, n * q)
    assert sum((F(1, x) for x in signature), F(0)) == 1 + F(4, n)
    print(f"Unbounded r=4 family: n={n}, signature={signature}")
    # Also an excluded s=0 family: (2,3,6,d), n=4d.
    assert F(1, 2) + F(1, 3) + F(1, 6) + F(1, 2000) == 1 + F(4, 8000)

    assert list(stars(409)) == []
    assert all(409 % d for d in range(2, isqrt(409) + 1))
    print("Lemma H: 409 prime, 409=1 mod 4, R(409)=0 (complete search)")

    # E8: if positivity is dropped, the Anosov/marked-torsion condition
    # alone holds even at a square with no star witness.
    n = 9
    a, b, c, d = -1, n, 4, -4 * n - 1
    assert a * d - b * c == 1 and abs(a + d) > 2
    assert (a + 1) % c == 0 and list(stars(n)) == []
    print(f"Bare E8 torus condition at R(9)=0: gamma={a,b,c,d}")

    assert list(stars(2)) == [(1, 1, 1)]
    indices = (1, 2, 2)
    assert sum((F(1, x) for x in indices), F(0)) == F(4, 2)
    print("Lemma F p=2 boundary: indices (1,2,2), only TWO branch points")

    assert egyptian3(8, 131) is None
    # Kollár (15.5): a1=16,a2=12,c1=3,c2=5 is admissible.
    assert 16 + 3 >= max(2, 12) and 12 + 5 >= max(2, 16)
    assert F(3 + 5, 3 * 5 + 16 * 5 + 12 * 3) == F(8, 131)
    print("F2: 8/131 has no 3-term representation; lct(x^16*y^12*(x^3+y^5))=8/131")

    screen = Path(__file__).resolve().parents[1] / "data/z58/screens/composite_zeros_le8e6.txt"
    numbers = [int(line) for line in screen.read_text().splitlines() if line and not line.startswith('#')]
    failures = [n for n in numbers if word(n) is None]
    print(f"F3: W fails on {failures} among {len(numbers)} supplied composite R-zeros")
    assert failures == [105]
    print("All checks passed.")


if __name__ == '__main__':
    main()
