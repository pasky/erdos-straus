"""review_fs2_bounds.py (R218, from scratch): exact-integer implementation of the route bounds of
FF_STERILE_PUSH Lemma 1.6 (Case B) written directly from the document text, NOT from fs_sum.c.
Used by review_fs2_brute.py (validation against brute-force tuple counts) and review_fs2_exact.py (exact sums)."""
from math import comb, factorial
from functools import lru_cache


def make(q):
    def Ns(d):
        return 1 if d <= 0 else q**d - q**(d - 1)

    def Som(e):  # sum over monic v of degree e of 2^omega(v) (closed form of Lemma 1.6)
        if e <= 0:
            return 1
        return 2 * q**e + (e - 1) * (q**e - q**(e - 1))

    @lru_cache(maxsize=None)
    def cop(n, d, rho, KMAX=200):
        """least m+k (m>=1,k>=0, m+k<=KMAX) with Delta(m,k) < (m+k+1) m d, X = d - rho >= 0; 0 if none."""
        X = d - rho
        if X < 0:
            return 1
        for K in range(1, KMAX + 1):
            for m in range(1, K + 1):
                k = K - m
                A = m * (m + 1) // 2
                Delta = n * A + X * (A + k * m + k * (k + 1) // 2)
                if Delta < (m + k + 1) * m * d:
                    return K
        return 0

    @lru_cache(maxsize=None)
    def cls(n, d, rho, both):
        if d < 0 or d > n:
            return 0
        best = comb(n, d)
        if d < rho or (both and n - d < rho):
            return min(best, 1)
        if 3 * rho > n:
            best = min(best, 2)
        c = cop(n, d, rho)
        if c:
            best = min(best, c)
        if both:
            c = cop(n, n - d, rho)
            if c:
                best = min(best, c)
        return best

    def routes(s, a, z, y, t):
        b = y + t
        W, WB, Z, Y, V = Ns(a - 1), Ns(b - 1), Ns(z), Ns(y), Ns(t - 2)
        e = {}
        e['T0'] = Z * Y * W
        e["R4'"] = Z * W * V
        e['X1'] = 2 * Y * V * Z
        e['X2'] = Y * V * W
        e['R1'] = V * (factorial(s - 2) // (factorial(z) * factorial(a - 1) * factorial(b - 1)))
        e['R2'] = Z * Y * cls(s + 2 * y + z, a + y + z, y + z + 1, 1)
        e['R3'] = W * Y * cls(s - 1 + y, a + y + z, a + y, 0)
        e['R4'] = Z * W * cls(s - 2, a + y + z, a + z, 1)
        e['R3C'] = WB * Y * cls(s - 1 + y, b + y + z, b + y, 0)
        e['R4C'] = Z * WB * cls(z + 2 * b - 2, b + y + z, b + z, 1)
        e['R5a'] = V * W * cls(s - 1 - a, b - 1, t - 1, 1)
        e['R5b'] = V * WB * cls(s - 1 - b, a - 1, t - 1, 1)
        e['R6a'] = V * comb(s - 2, a - 1) * cls(s - 1 - a, b - 1, t - 1, 1)
        e['R6b'] = V * comb(s - 2, b - 1) * cls(s - 1 - b, a - 1, t - 1, 1)
        e['R8a'] = Y * V * comb(s - 2, a - 1)
        e['R8b'] = Y * V * comb(s - 2, b - 1)
        e['R9a'] = Z * V * comb(a + b - 2, a - 1)
        e['R10a'] = Z * 2 * Som(t - 2) * cls(a + b - 2, a - 1, t - 1, 1)
        e['R10b'] = 2 * Som(t - 2) * comb(s - 2, z) * cls(a + b - 2, a - 1, t - 1, 1)
        return e

    def patterns(s):
        for a in range(1, s):
            for z in range(0, s - a):
                b = s - a - z
                if b < a:
                    continue
                for y in range(0, b - 1):
                    yield a, z, y, b - y

    return dict(Ns=Ns, Som=Som, cop=cop, cls=cls, routes=routes, patterns=patterns)
