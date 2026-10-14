"""R212 from-scratch check of FOUR_SPECIFIC Thm 4.2 (universal one-slot chi-witnesses).

(1) exact class scan: non-square A in [2, AMAX] is universal iff for every unit r mod L = lcm(8, A) with r = 1 (mod 4)
    and Jacobi(A, r) = -1, the residue -r^{-1} mod A is t mod A for some divisor t of A+1.
(2) the Rosser-Schoenfeld tail: phi(A)/4 > 2 sqrt(A+1) via phi(A) > A/(e^g loglog A + 3/loglog A); evaluate the
    bound on [3000, 10^7] on a grid AND exactly (true phi) check tau(A+1) < phi(A)/4 for all 3000 <= A <= TAU_MAX.
(3) prime cross-check p = 1 (mod 4), p < PMAX: witnesses {2,3,5,7,8,15,20} give a word (t, u, v) with tu - 1 = A and a
    slice solution of 4/p verified in exact rationals  <=>  p mod 840 not in Mordell's six classes.
"""
from fractions import Fraction as F
from math import gcd, isqrt, log, exp, sqrt
import sys

EG = exp(0.5772156649015329)


def jacobi(a, n):
    a %= n
    r = 1
    while a:
        while a % 2 == 0:
            a //= 2
            if n % 8 in (3, 5):
                r = -r
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3:
            r = -r
        a %= n
    return r if n == 1 else 0


def divisors(m):
    out = []
    for d in range(1, isqrt(m) + 1):
        if m % d == 0:
            out.append(d)
            out.append(m // d)
    return sorted(set(out))


def universal(A):
    L = 8 * A // gcd(8, A)
    D = {t % A for t in divisors(A + 1)}
    for r in range(1, L, 4):
        if gcd(r, L) != 1:
            continue
        if jacobi(A, r) != -1:
            continue
        if (-pow(r, -1, A)) % A not in D:
            return False
    return True


def phi_sieve(N):
    ph = list(range(N + 1))
    for i in range(2, N + 1):
        if ph[i] == i:
            for j in range(i, N + 1, i):
                ph[j] -= ph[j] // i
    return ph


def tau_sieve(N):
    t = [0] * (N + 1)
    for i in range(1, N + 1):
        for j in range(i, N + 1, i):
            t[j] += 1
    return t


def slice_solution(p, t, u, v):
    """4-slice solution from a word with 4 | some slot; returns denominators verified exactly"""
    A, As = t * u - 1, t * v - 1
    n = p
    sols = []
    if A % 4 == 0:
        d = A // 4
        sols.append((As * d * n, v * d, As * v * d))
    if As % 4 == 0:
        d = As // 4
        sols.append((A * d * n, u * d, A * u * d))
    if t % 4 == 0:
        c = t // 4
        sols.append((u * v * c, u * c * n, v * c * n))
    if u % 4 == 0:
        w = u // 4
        sols.append((w * As, t * n * w, t * n * w * As))
    if v % 4 == 0:
        w = v // 4
        sols.append((w * A, t * n * w, t * n * w * A))
    for s in sols:
        assert F(4, n) == sum(F(1, x) for x in s), (p, t, u, v, s)
    return sols


def main(AMAX, TAU_MAX, PMAX):
    U = [A for A in range(2, AMAX + 1) if isqrt(A) ** 2 != A and universal(A)]
    print("(1) universal non-square A <=", AMAX, ":", U)
    # (2)
    worst = 1e9
    A = 3000
    while A <= 10**12:
        ll = log(log(A))
        ratio = (A / (EG * ll + 3 / ll)) / 4 / (2 * sqrt(A + 1))
        worst = min(worst, ratio)
        A = int(A * 1.01) + 1
    A = 3000
    ll = log(log(A))
    print(f"(2) RS bound at 3000: phi/4 > {A/(EG*ll+3/ll)/4:.2f}, 2sqrt(A+1) = {2*sqrt(A+1):.2f};"
          f" min ratio on [3000,1e12] grid = {worst:.4f}")
    ph = phi_sieve(TAU_MAX + 1)
    ta = tau_sieve(TAU_MAX + 2)
    bad = [A for A in range(3000, TAU_MAX + 1) if 4 * ta[A + 1] >= ph[A]]
    rsbad = [A for A in range(3, TAU_MAX + 1)
             if not ph[A] > A / (EG * log(log(A)) + 3 / log(log(A)))]
    lastnec = max(A for A in range(2, 3000) if 4 * ta[A + 1] >= ph[A])
    print(f"    exact: tau(A+1) >= phi(A)/4 for A in [3000,{TAU_MAX}]: {len(bad)} cases; "
          f"RS(3) bound violations for 3<=A<={TAU_MAX}: {len(rsbad)}; largest A<3000 passing the necessary "
          f"condition: {lastnec}")
    # (3)
    sieve = bytearray([1]) * (PMAX + 1)
    sieve[0] = sieve[1] = 0
    for i in range(2, isqrt(PMAX) + 1):
        if sieve[i]:
            sieve[i * i::i] = bytearray(len(sieve[i * i::i]))
    mordell = {1, 121, 169, 289, 361, 529}
    W = [2, 3, 5, 7, 8, 15, 20]
    mism = 0
    cnt = 0
    for p in range(5, PMAX + 1, 4):
        if not sieve[p]:
            continue
        cnt += 1
        hit = False
        for A in W:
            if p % A == 0 or jacobi(-A % p, p) != -1:
                continue
            for t in divisors(A + 1):
                if (t * p + 1) % A == 0:
                    u = (A + 1) // t
                    v = (p + u) // A
                    assert (p + u) % A == 0 and t * u * v - u - v == p
                    if slice_solution(p, t, u, v):
                        hit = True
                        break
            if hit:
                break
        if hit == (p % 840 in mordell):
            mism += 1
            print("mismatch", p)
    print(f"(3) primes p=1 mod 4 < {PMAX}: {cnt}, mismatches vs Mordell's classes: {mism}")


if __name__ == "__main__":
    main(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]))
