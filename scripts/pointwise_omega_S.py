#!/usr/bin/env python3
"""POINTWISE_OMEGA.md, section 2: the prime-local residual system after the class-of-one
quarantine at all primes <= y, and its sieve mass

    F_l = { -4D mod l :  m <= T/l, m*l = 3 (mod 4), D | ((m*l+1)/4)^2, m | 4D+1 },  y < l <= T prime,
    S(T,y) = sum_l |F_l|/(l-1),   g_max = max_l |F_l|/(l-1).

Also prints the rigorous majorant of Lemma 2.3,
    S <= (4/3)(3+log T) * sum_{s r^2 <= T/4+1, s squarefree} tau(4 s r^2 + 1)/(s r),
and the crude bound of POINTWISE_SIZE Lemma 11.7 (no congruence saving).

Usage: PYTHONPATH=scripts uv run python scripts/pointwise_omega_S.py T [yexp=0.5]
       (y = T^yexp; yexp must be >= 1/2 for prime-locality)"""
import sys
from math import log, isqrt


def spf_table(n):
    spf = list(range(n + 1))
    for i in range(2, isqrt(n) + 1):
        if spf[i] == i:
            for j in range(i * i, n + 1, i):
                if spf[j] == j:
                    spf[j] = i
    return spf


def factor(n, spf):
    f = {}
    while n > 1:
        p = spf[n]
        f[p] = f.get(p, 0) + 1
        n //= p
    return f


def divisors_from(f):
    ds = [1]
    for p, e in f.items():
        ds = [d * p ** k for d in ds for k in range(e + 1)]
    return ds


def residual_system(T, y, spf):
    """Return dict l -> set F_l for primes y < l <= T."""
    F = {}
    for l in range(int(y) + 1, T + 1):
        if spf[l] != l:
            continue
        S = set()
        for m in range(1, T // l + 1):
            M = m * l
            if M % 4 != 3:
                continue
            A = (M + 1) // 4
            f = {p: 2 * e for p, e in factor(A, spf).items()}
            for D in divisors_from(f):
                if (4 * D + 1) % m == 0:
                    S.add((-4 * D) % l)
        F[l] = S
    return F


def majorant(T, spf):
    """(4/3)(3+log T) * sum_{s r^2 <= T/4+1, s squarefree} tau(4 s r^2+1)/(s r)."""
    X = T // 4 + 1
    tot = 0.0
    r = 1
    while r * r <= X:
        for s in range(1, X // (r * r) + 1):
            fs = factor(s, spf)
            if any(e > 1 for e in fs.values()):
                continue
            N = 4 * s * r * r + 1
            # tau(N): N <= T+5 <= len(spf)
            t = 1
            for e in factor(N, spf).values():
                t *= e + 1
            tot += t / (s * r)
        r += 1
    return 4 / 3 * (3 + log(T)) * tot


def main():
    T = int(sys.argv[1])
    yexp = float(sys.argv[2]) if len(sys.argv) > 2 else 0.5
    y = T ** yexp
    spf = spf_table(T + 8)
    F = residual_system(T, y, spf)
    S = sum(len(v) / (l - 1) for l, v in F.items())
    gmax, lmax = max((len(v) / (l - 1), l) for l, v in F.items())
    Fmax = max(len(v) for v in F.values())
    # crude (Lemma 11.7) mass: drop the congruence m | 4D+1
    crude = 0.0
    for l in F:
        c = 0
        for m in range(1, T // l + 1):
            if (m * l) % 4 == 3:
                A = (m * l + 1) // 4
                t = 1
                for e in factor(A, spf).values():
                    t *= 2 * e + 1
                c += t
        crude += c / (l - 1)
    print(f"T={T} y=T^{yexp}={y:.1f} #primes={len(F)} S={S:.4f} g_max={gmax:.4f} (l={lmax}) "
          f"max|F_l|={Fmax} crude_mass={crude:.2f} logT={log(T):.2f}")
    if T <= 2 * 10 ** 6:
        print(f"  Lemma 2.3 majorant = {majorant(T, spf):.1f}")


if __name__ == "__main__":
    main()
