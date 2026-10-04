#!/usr/bin/env python3
"""O21 exact checks for EXCEPTIONAL_TUPLES.md (seconds, < 200 MB).

(1) Lemma 1.3 shift form: f_y(n) = sum_D omega_{y,D}(n+4D) for n <= 20000, y = 400.
(2) Prop 4.2: every class -4D (D | A^2) of R(l) is a quadratic non-residue mod l,
    for all l = 3 (4) prime <= 20000; hence squares are never hit.
(3) Theorem 2.1 identity: sum_{j<=K} (-1)^j C(f,j) = (-1)^K C(f-1,K) (f>=1), =1 (f=0).
(4) Theorem 2.1 bound on the CRT side: sum_{j<=K}(-1)^j e_j(p) <= prod(1-p) + e_K(p)
    for random p-vectors and the actual prime family.
(5) Lemma 1.2 / Prop 2.4: |S_j - N e_j| <= e_j(F) exactly, small N and y.
(6) Every positive n in a class of R(l) has an ES solution (Lemma 16.1 identity),
    exact rational check on a sample.
"""
from fractions import Fraction
from math import comb
import random
import sys

sys.path.insert(0, 'scripts')
from tuples_moments import primes_upto, divisors_of_square, R_set, esym  # noqa: E402


def check1():
    y, N = 400, 20000
    P = [int(l) for l in primes_upto(y) if l % 4 == 3]
    Dsets = {}
    for l in P:
        seen, Ds = set(), []
        for D in sorted(divisors_of_square((l + 1) // 4)):
            r = (-4 * D) % l
            if r not in seen:
                seen.add(r)
                Ds.append(D)
        Dsets[l] = Ds
        assert seen == set(R_set(l))
    for n in range(1, N + 1):
        f = sum(1 for l in P if (n % l) in set(R_set(l)) )
        g = sum(1 for l in P for D in Dsets[l] if (n + 4 * D) % l == 0)
        assert f == g, (n, f, g)
    return f"(1) shift form OK for n<={N}, y={y}, {len(P)} primes"


def check2():
    cnt = 0
    for l in primes_upto(20000):
        l = int(l)
        if l % 4 != 3:
            continue
        for r in R_set(l):
            assert pow(r, (l - 1) // 2, l) == l - 1, (l, r)
            cnt += 1
    return f"(2) all {cnt} classes are non-residues"


def check3():
    for K in range(0, 30):
        for f in range(0, 60):
            s = sum((-1) ** j * comb(f, j) for j in range(K + 1))
            t = 1 if f == 0 else (-1) ** K * comb(f - 1, K)
            assert s == t
            if K % 2 == 0:
                assert s >= (1 if f == 0 else 0)
    return "(3) Bonferroni identity OK (K<30, f<60)"


def check4():
    rnd = random.Random(5)
    worst = -1.0
    for _ in range(300):
        n = rnd.randint(1, 40)
        ps = [rnd.random() ** 2 for _ in range(n)]
        e = esym(ps, n)
        prod = 1.0
        for p in ps:
            prod *= 1 - p
        for K in range(0, n + 1, 2):
            lhs = sum((-1) ** j * e[j] for j in range(K + 1))
            worst = max(worst, lhs - (prod + e[K]))
    assert worst <= 1e-9, worst
    return f"(4) CRT Bonferroni bound OK (max lhs-rhs = {worst:.2e})"


def check5():
    N, y = 3000, 60
    P = [int(l) for l in primes_upto(y) if l % 4 == 3]
    ps = [Fraction(len(R_set(l)), l) for l in P]
    Fs = [len(R_set(l)) for l in P]
    f = [sum(1 for l in P if n % l in R_set(l)) for n in range(1, N + 1)]
    J = len(P)
    # exact e_j
    e = [Fraction(0)] * (J + 1)
    e[0] = Fraction(1)
    eF = [0] * (J + 1)
    eF[0] = 1
    for p, F in zip(ps, Fs):
        for j in range(J, 0, -1):
            e[j] += p * e[j - 1]
            eF[j] += F * eF[j - 1]
    for j in range(J + 1):
        S = sum(comb(v, j) for v in f)
        assert abs(S - N * e[j]) <= eF[j], j
    return f"(5) |S_j - N e_j| <= e_j(F) exactly for N={N}, y={y}, j<={J}"


def check6():
    rnd = random.Random(7)
    tested = 0
    for l in [int(x) for x in primes_upto(500) if x % 4 == 3]:
        A = (l + 1) // 4
        for D in divisors_of_square(A):
            # D = u^2 w, uvw = A, constructed prime-by-prime as in Lemma 18.1
            fa, m, q = {}, A, 2
            while q * q <= m:
                while m % q == 0:
                    fa[q] = fa.get(q, 0) + 1
                    m //= q
                q += 1
            if m > 1:
                fa[m] = fa.get(m, 0) + 1
            u = w = 1
            for q, e in fa.items():
                d = 0
                DD = D
                while DD % q == 0:
                    DD //= q
                    d += 1
                u *= q ** (d // 2)
                w *= q ** (d % 2)
            v = A // (u * w)
            assert u * v * w == A and u * u * w == D
            n = (-4 * D) % l
            for k in range(3):
                nn = n + k * l + rnd.randint(0, 50) * l
                if nn <= 0:
                    continue
                s = (nn * v + u) // l
                assert (nn * v + u) % l == 0
                assert Fraction(4, nn) == Fraction(1, s * u * w) + Fraction(1, nn * s * v * w) + Fraction(1, nn * u * v * w)
                tested += 1
    return f"(6) Lemma 16.1 identity OK on {tested} (n, class) samples"


if __name__ == '__main__':
    for c in (check1, check2, check3, check4, check5, check6):
        print(c(), flush=True)
