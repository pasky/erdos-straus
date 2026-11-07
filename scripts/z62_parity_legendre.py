#!/usr/bin/env python3
"""z62 PARITY — KT2: the Legendre/Gauss parity-forced divisor of N_C = 4Cp + 1.

The principal cycle of reduced forms of discriminant N (N = 1 mod 4, non-square) has a reflection symmetry; besides the
principal form its centres are ambiguous forms (a | b, giving a divisor of N) or symmetric forms (c = -a, N(eps) = -1).
For each (p, C) we collect the divisors g = gcd(|a|, N) > 1 (g < N) forced by ambiguous forms in the principal cycle,
and test g = -1 (mod 4C) (a (★) certificate at level C), against the random-divisor baseline
(per (p,C): probability q = fraction of nontrivial divisor pairs of N in that class, if the forced pair were a uniformly
random nontrivial pair; expectation sum q, variance sum q(1-q); also the same with coprime pairs only).
Usage: z62_parity_legendre.py PMAX CMAX
"""
import sys
from math import isqrt, gcd
sys.path.insert(0, "scripts")
from z62_parity_river import rho, is_reduced


def principal_cycle(N):
    s = isqrt(N)
    b = s if s % 2 == 1 else s - 1
    a, c = 1, (b * b - N) // 4
    assert is_reduced(a, b, c, s)
    start = (a, b, c)
    cyc = [start]
    while True:
        a, b, c = rho(a, b, c, N, s)
        if (a, b, c) == start:
            break
        cyc.append((a, b, c))
    return cyc


def factor(m):
    f = {}
    d = 2
    while d * d <= m:
        while m % d == 0:
            f[d] = f.get(d, 0) + 1
            m //= d
        d += 1 if d == 2 else 2
    if m > 1:
        f[m] = f.get(m, 0) + 1
    return f


def divisors(m):
    ds = [1]
    for q, e in factor(m).items():
        ds = [d * q ** k for d in ds for k in range(e + 1)]
    return ds


def is_prime(m):
    return m > 1 and all(m % q for q in range(2, isqrt(m) + 1))


def main():
    PMAX, CMAX = int(sys.argv[1]), int(sys.argv[2])
    tot_pairs = 0
    exp_hits = 0.0
    var_hits = 0.0
    exp_cop = 0.0
    var_cop = 0.0
    hits = 0
    n_forced = 0
    n_sym = 0
    n_sq = 0
    per_p_any = 0
    per_p_star = 0
    nprimes = 0
    for p in range(25, PMAX + 1, 24):
        if not is_prime(p):
            continue
        nprimes += 1
        anyhit = False
        star = False
        for C in range(1, CMAX + 1):
            N = 4 * C * p + 1
            r = isqrt(N)
            if r * r == N:
                n_sq += 1
                continue
            divs = divisors(N)
            pairs = [g for g in divs if 1 < g and g * g < N]
            inclass = [g for g in pairs if (g + 1) % (4 * C) == 0]
            if inclass:
                star = True
            cyc = principal_cycle(N)
            forced = set()
            sym = False
            for (a, b, c) in cyc:
                for x in (a, c):
                    if abs(x) > 1 and b % x == 0:
                        g = gcd(abs(x), N)
                        if 1 < g < N:
                            forced.add(min(g, N // g))
                if c == -a:
                    sym = True
            if sym:
                n_sym += 1
            if forced and pairs:
                n_forced += 1
                tot_pairs += 1
                q = len(inclass) / len(pairs)
                exp_hits += q
                var_hits += q * (1 - q)
                cop = [g for g in pairs if gcd(g, N // g) == 1]
                qc = sum(1 for g in cop if (g + 1) % (4 * C) == 0) / len(cop) if cop else 0.0
                exp_cop += qc
                var_cop += qc * (1 - qc)
                h = any((g + 1) % (4 * C) == 0 for g in forced)
                hits += h
                anyhit |= h
        per_p_any += anyhit
        per_p_star += star
    sd = var_hits ** 0.5  # sum of per-(p,C) Bernoulli variances
    sdc = var_cop ** 0.5
    print(f"primes p=1(24) <= {PMAX}: {nprimes}; C <= {CMAX}")
    print(f"(p,C) with a forced nontrivial ambiguous divisor: {n_forced}; with symmetric centre (N(eps)=-1): {n_sym}; square N: {n_sq}")
    print(f"forced divisor in class -1 mod 4C: {hits}; random-divisor baseline expectation {exp_hits:.1f} (sd ~ {sd:.1f}); z = {(hits-exp_hits)/max(sd,1e-9):.2f}")
    print(f"baseline restricted to coprime divisor pairs: expectation {exp_cop:.1f} (sd {sdc:.1f}); z = {(hits-exp_cop)/max(sdc,1e-9):.2f}")
    print(f"primes with some forced (★) certificate (C<=CMAX): {per_p_any} / {nprimes}; with any (★) certificate at C<=CMAX: {per_p_star}")


if __name__ == "__main__":
    main()
