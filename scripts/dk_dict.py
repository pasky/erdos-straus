"""O169 dictionary checks: ES X-slice certificates <-> Hirzebruch-Jung CF of length 3.

Usage: PYTHONPATH=scripts uv run python scripts/dk_dict.py NMAX
Checks for every n <= NMAX (n odd, n >= 5) [primes and odd squares reported]:
 (D1) {A in [1,n): gcd(A,n)=1, HJ(n/A) has length 3} == {tu-1 : tuv-u-v=n, t,u,v>=2}
 (D2) Hirzebruch-Zagier: 12 s(A,n) = sum(b_i-3) + (A+A*)/n   (all A coprime)
 (D3) r(n/A) - r(n/(n-A)) = -12 s(A,n) - 1 + (A+A*)/n
 (D4) T1: at odd squares no A = 0 mod 4 with HJ length 3 (X-slice of Type I, a=1)
"""
import sys
from fractions import Fraction
from math import gcd, isqrt


def hj(n, a):
    """Hirzebruch-Jung (negative) CF of n/a, 0<a<n: n/a = b1 - 1/(b2 - ...), b_i >= 2."""
    out = []
    while a:
        b = -(-n // a)  # ceil
        out.append(b)
        n, a = a, b * a - n
    return out


def dedekind(a, c):
    """s(a,c) exactly via reciprocity (Euclid)."""
    a %= c
    sign, acc = 1, Fraction(0)
    while a:
        # s(a,c) = -s(c,a) + (a/c + c/a + 1/(ac))/12 - 1/4
        acc += sign * (Fraction(a * a + c * c + 1, 12 * a * c) - Fraction(1, 4))
        sign = -sign
        a, c = c % a, a
    return acc


def certs_len3(n):
    S = set()
    t = 2
    while True:
        # minimal value with u=v=2: 4t-4
        if 4 * t - 4 > n:
            break
        u = 2
        while True:
            m = t * u - 1
            if m * 2 - u > n:  # v=2 gives 2tu-u-2 = n? v>=2 -> n >= v*m-u >= 2m-u
                break
            if (n + u) % m == 0:
                v = (n + u) // m
                if v >= 2:
                    S.add(m)
            u += 1
        t += 1
    return S


def main():
    N = int(sys.argv[1])
    bad = 0
    nprime = nsq = 0
    for n in range(5, N + 1, 2):
        is_sq = isqrt(n) ** 2 == n
        is_p = all(n % q for q in range(3, isqrt(n) + 1, 2))
        if not (is_sq or is_p):
            continue
        L3 = set()
        for A in range(1, n):
            if gcd(A, n) != 1:
                continue
            b = hj(n, A)
            if len(b) == 3:
                L3.add(A)
            if n < 3000:  # (D2),(D3) exact rationals, smaller range
                As = pow(A, -1, n)
                s = dedekind(A, n)
                if 12 * s != sum(x - 3 for x in b) + Fraction(A + As, n):
                    bad += 1; print("D2 fail", n, A)
                r2 = len(hj(n, n - A))
                if len(b) - r2 != -12 * s - 1 + Fraction(A + As, n):
                    bad += 1; print("D3 fail", n, A)
        if L3 != certs_len3(n):
            bad += 1; print("D1 fail", n)
        if is_sq:
            nsq += 1
            if any(A % 4 == 0 for A in L3):
                bad += 1; print("D4 fail", n)
        else:
            nprime += 1
    print(f"N={N}: primes {nprime}, odd squares {nsq}, failures {bad}")


if __name__ == "__main__":
    main()
