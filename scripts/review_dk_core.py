"""R169 from-scratch checks: Lemma 1.1, Cor 1.2, (D2), (D3), Rademacher (R).
Usage: PYTHONPATH=scripts uv run python scripts/review_dk_core.py [NMAX_L3] [NMAX_DED]
"""
import sys
from fractions import Fraction as F
from math import gcd, floor


def hj(n, A):
    """HJ (negative) CF of n/A, 0<A<n coprime: list b_i>=2."""
    out = []
    a, b = n, A
    while b:
        q = -(-a // b)  # ceil
        out.append(q)
        a, b = b, q * b - a
    return out


def ded_direct(a, c):
    """Dedekind sum by definition (sawtooth), exact."""
    def saw(x):
        if x.denominator == 1:
            return F(0)
        return x - floor(x) - F(1, 2)
    return sum(saw(F(k, c)) * saw(F(a * k, c)) for k in range(1, c))


def jacobi(a, n):
    assert n > 0 and n % 2
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


def main():
    N1 = int(sys.argv[1]) if len(sys.argv) > 1 else 1500
    N2 = int(sys.argv[2]) if len(sys.argv) > 2 else 150
    bad = 0
    # Lemma 1.1 as set identity for ALL n in [2,N1]
    trip = {}
    for t in range(2, N1 + 2):
        for u in range(2, N1 + 2):
            if t * u * 2 - u - 2 > N1:
                break
            for v in range(2, N1 + 2):
                n = t * u * v - u - v
                if n > N1:
                    break
                trip.setdefault(n, []).append((t, u, v))
    for n in range(2, N1 + 1):
        L3 = {}
        for A in range(1, n):
            if gcd(A, n) == 1:
                w = hj(n, A)
                if len(w) == 3:
                    L3[A] = w
        T = trip.get(n, [])
        S = {}
        for (t, u, v) in T:
            A = t * u - 1
            if A in S:
                bad += 1; print("non-injective", n, t, u, v)
            S[A] = (t, u, v)
        if set(S) != set(L3):
            bad += 1; print("set mismatch", n)
        for A, (t, u, v) in S.items():
            if L3.get(A) != [v, t, u]:
                bad += 1; print("word mismatch", n, A)
            As = t * v - 1
            if not (0 < As < n and (A * As) % n == 1 and A * As == t * n + 1):
                bad += 1; print("A* fail", n, A)
            # Cor 1.2 Type I (4|A) and Type II (4|t): exact ES identity
            if A % 4 == 0:
                d, b, c = A // 4, F(n + v, u), v
                if b.denominator != 1 or F(4, n) != 1 / (b * d * n) + F(1, c * d) + 1 / (b * c * d):
                    bad += 1; print("TypeI fail", n, t, u, v)
            if t % 4 == 0:
                a_, b_, c_ = u, v, t // 4
                if F(4, n) != F(1, a_ * b_ * c_) + F(1, a_ * c_ * n) + F(1, b_ * c_ * n):
                    bad += 1; print("TypeII fail", n, t, u, v)
            # 4|u e-slice (reviewer's explicit ES solution): 4/n = 1/(wf)+1/(tnw)+1/(tnwf)
            for (uu, vv) in ((u, v), (v, u)):
                if uu % 4 == 0:
                    w_, f_ = uu // 4, t * vv - 1
                    N = F(n + vv, 4)
                    if N.denominator != 1 or N % f_ != 0 or f_ % vv != vv - 1:
                        bad += 1; print("e-slice divisibility fail", n)
                    if F(4, n) != F(1, w_ * f_) + F(1, t * n * w_) + F(1, t * n * w_ * f_):
                        bad += 1; print("e-slice ES fail", n)
    print("Lemma1.1/Cor1.2/e-slice: n<=%d bad=%d" % (N1, bad))
    # (D2), (D3), (R) by direct Dedekind sums, all A, n<=N2
    bad2 = 0; cnt = 0
    for n in range(3, N2 + 1):
        for A in range(1, n):
            if gcd(A, n) != 1:
                continue
            s = ded_direct(A, n)
            w = hj(n, A)
            As = pow(A, -1, n)
            if 12 * s != sum(b - 3 for b in w) + F(A + As, n):
                bad2 += 1; print("D2 fail", n, A)
            rp = len(hj(n, n - A)) if n - A > 0 else 0
            if len(w) - rp != -12 * s - 1 + F(A + As, n):
                bad2 += 1; print("D3 fail", n, A)
            if sum(b - 2 for b in w) != rp - 1:
                bad2 += 1; print("Riemenschneider fail", n, A)
            if n % 2:
                x = 12 * n * s
                assert x.denominator == 1
                if (int(x) - (n + 1 - 2 * jacobi(A, n))) % 8:
                    bad2 += 1; print("R fail", n, A)
            cnt += 1
    print("D2/D3/R direct: n<=%d pairs=%d bad=%d" % (N2, cnt, bad2))


if __name__ == "__main__":
    main()
