"""R172 from-scratch check of KUDLA_ES Thm 1.2 / 1.4 (and the e*T' remark).

Independent of the author's scripts and of geo_common: own Hilbert symbol (validated against a brute-force
p-adic solvability test), own enumeration of Type I / Type II tuples, and Diff(T, C) computed from the GRAM MATRIX
route (not from the author's algebra (-d,-dne)): T -> diagonal binary U = <T11, T11*det T> (mod squares),
ternary W = U + <det U>; T is represented by M2(Q_l)^0 iff W is isotropic at l iff Hasse c_l(W) = (-1,-1)_l
(W has square determinant).  C_inf positive definite represents every positive definite T.

Type I (n odd >= 3): a <= b, 4abd = n e + 1, a + b = c e.  Enumerated as a, d, e | 4a^2 d + 1, b = -a mod e.
Type II (n odd >= 3): a <= b, 4abd = n + e, a + b = c e.  T' = [[f,1],[1,f']], f = 4acd-1, f' = 4bcd-1.
Run: PYTHONPATH=scripts uv run --with sympy python scripts/review_kud_tuples.py N
"""
import sys
from math import isqrt
from functools import lru_cache
from collections import Counter
from sympy import factorint, divisors

N = int(sys.argv[1]) if len(sys.argv) > 1 else 3000


def v(x, p):
    k = 0
    while x % p == 0:
        x //= p
        k += 1
    return k, x


def leg(a, p):  # Legendre via Euler, p odd prime, p !| a
    r = pow(a % p, (p - 1) // 2, p)
    return 1 if r == 1 else -1


def hil(a, b, p):
    """(a,b)_p for nonzero integers a, b, p prime."""
    al, u = v(a, p)
    be, w = v(b, p)
    if p != 2:
        s = (-1) ** (al * be * ((p - 1) // 2) % 2)
        return s * leg(u, p) ** be * leg(w, p) ** al
    eps = lambda x: ((x - 1) // 2) % 2
    om = lambda x: ((x * x - 1) // 8) % 2
    e = eps(u % 8) * eps(w % 8) + al * om(w % 8) + be * om(u % 8)
    return -1 if e % 2 else 1


def brute_hil(a, b, p):
    """Brute force: z^2 = a x^2 + b y^2 has a primitive solution mod p^K that lifts (Hensel, conservative K)."""
    K = 5 if p == 2 else 3   # a, b squarefree => derivative valuation <= 1 (+1 at 2)
    M = p ** K
    sq = {}
    for z in range(M):
        sq.setdefault(z * z % M, []).append(z)
    for x in range(M):
        for y in range(M):
            if x % p == 0 and y % p == 0:
                continue
            t = (a * x * x + b * y * y) % M
            for z in sq.get(t, []):
                # Hensel-safe primitive solution: some partial derivative has small valuation
                g = [2 * a * x, 2 * b * y, 2 * z]
                vm = min(v(gi, p)[0] if gi else 99 for gi in g)
                if 2 * vm < K:
                    return 1
    return -1


def sf(x):
    return all(x % (q * q) for q in (2, 3))


@lru_cache(maxsize=None)
def fac(x):
    return tuple(factorint(x))


def sqfree_part_primes(*xs):
    ps = {2}
    for x in xs:
        ps |= set(fac(abs(x)))
    return ps


def diff_from_gram(t11, t12x2, t22):
    """T = [[t11, t12x2/2],[t12x2/2, t22]], positive definite.  Returns Diff(T, C) (finite primes)."""
    D4 = 4 * t11 * t22 - t12x2 * t12x2      # = 4 det T = det(2T) ~ det T mod squares
    A1, A2 = t11, t11 * D4                   # U ~ <t11, det T / t11> ~ <t11, t11 det T>
    A3 = D4                                  # <det U>
    out = set()
    for p in sqfree_part_primes(A1, A2, A3):
        c = hil(A1, A2, p) * hil(A1, A3, p) * hil(A2, A3, p)
        if c != hil(-1, -1, p):
            out.add(p)
    return frozenset(out)


def odd_ell_set(n, cond):
    return frozenset(l for l, k in factorint(n).items() if l != 2 and k % 2 == 1 and cond(l))


if __name__ == '__main__':
    # 0. validate own Hilbert symbol against brute force
    bad = 0
    for p in (2, 3, 5):
        for a in range(-12, 13):
            for b in range(-12, 13):
                if a and b and sf(a) and sf(b) and hil(a, b, p) != brute_hil(a, b, p):
                    bad += 1
    print('hilbert vs brute force (p in 2,3,5; |a|,|b|<=12) mismatches:', bad)

    S = Counter()
    perI, perII = Counter(), Counter()
    # Type I
    for a in range(1, N + 1):
        if 2 * a - 1 > N:   # n >= 2ad - 1/(2b) with d = 1
            break
        for d in range(1, N + 1):
            if 2 * a * d - 1 > N:
                break
            F = 4 * a * a * d + 1
            for e in divisors(F):
                b = (-a) % e
                while b < a:
                    b += e
                while True:
                    num = 4 * a * b * d - 1
                    if num > N * e:
                        break
                    n = num // e
                    assert num % e == 0 and (a + b) % e == 0
                    if n % 2 == 1 and n >= 3:
                        perI[n] += 1
                        S['I tuples'] += 1
                        Dg = diff_from_gram(d, -1, a * b)
                        P = odd_ell_set(n, lambda l: e % l != 0 and leg(-d, l) == -1)
                        S['I Diff==P'] += (Dg == P)
                        S['I 2 in Diff'] += (2 in Dg)
                        S['I |Diff| odd'] += (len(Dg) % 2)
                        if all(n % q for q in range(3, isqrt(n) + 1, 2)):
                            S['I prime n'] += 1
                            S['I prime: Diff=={n}'] += (Dg == {n})
                            S['I prime: n|e'] += (e % n == 0)
                    b += e
    # Type II
    for a in range(1, N + 1):
        if 2 * a * (2 * a - 1) > N:
            break
        for d in range(1, N + 1):
            if 2 * a * (2 * a * d - 1) > N:
                break
            b = a
            while 2 * b * (2 * a * d - 1) <= N:
                for c in divisors(a + b):
                    e = (a + b) // c
                    n = 4 * a * b * d - e
                    if n < 3 or n > N or n % 2 == 0:
                        continue
                    f, f2 = 4 * a * c * d - 1, 4 * b * c * d - 1
                    assert f * f2 - 4 * c * c * d * n == 1
                    perII[n] += 1
                    S['II tuples'] += 1
                    Dg = diff_from_gram(f, 2, f2)
                    P = odd_ell_set(n, lambda l: leg(-f, l) == -1)
                    S['II Diff==P'] += (Dg == P)
                    S['II 2 in Diff'] += (2 in Dg)
                    S['II |Diff| odd'] += (len(Dg) % 2)
                    De = diff_from_gram(e * f, 2 * e, e * f2)     # Gram e*T' of (2ai+j, 2bi-j)
                    # ambient algebra (-d,-n): ramified finite set via own Hilbert symbol
                    Amb = frozenset(p for p in sqfree_part_primes(d, n) if hil(-d, -n, p) == -1)
                    S["II Diff(eT')==Ram(-d,-n)"] += (De == Amb)
                    S["II Diff(eT')==Diff(T')"] += (De == Dg)
                b += 1
    sq = [m * m for m in range(3, isqrt(N) + 1, 2)]
    S['I at odd squares'] = sum(perI[s] for s in sq)
    S['II at odd squares'] = sum(perII[s] for s in sq)
    S['odd nonsq n<=N no I'] = [n for n in range(3, N + 1, 2) if not perI[n] and isqrt(n) ** 2 != n]
    S['odd nonsq n<=N no II'] = [n for n in range(3, N + 1, 2) if not perII[n] and isqrt(n) ** 2 != n]
    for k, val in S.items():
        print(k, val)
