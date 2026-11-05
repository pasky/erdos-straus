#!/usr/bin/env python3
"""Bounded-memory checks of Theorem G's AP residue (not its tiny exponent box).
Run: uv run --with numpy --with sympy scripts/z57_bfii_thmG_check.py
L-values use the exact half-period formula for an odd primitive quadratic
character, not a truncated Euler product. Euler-product tail is bounded.
"""
import math
import numpy as np
from sympy import isprime, jacobi_symbol, factorint

CHUNK = 250_000
PRIMES = (1000033, 5212561, 8813281)
PAIRS = ((1, 1), (1, 5), (3, 5))


def sieve(n):
    spf = np.zeros(n + 1, dtype=np.int32)
    for ell in range(2, math.isqrt(n) + 1):
        if spf[ell] == 0:
            view = spf[ell * ell::ell]
            view[view == 0] = ell
    primes = np.flatnonzero(spf[2:] == 0) + 2
    spf[primes] = primes
    return spf, primes


def legendre_table(p):
    table = np.full(p, -1, dtype=np.int8)
    table[0] = 0
    for start in range(1, (p + 1) // 2, CHUNK):
        x = np.arange(start, min(start + CHUNK, (p + 1) // 2), dtype=np.int64)
        table[(x * x) % p] = 1
    return table


def exact_L(p, u, lp):
    factors = factorint(u)
    v = math.prod(int(q) for q, e in factors.items() if e % 2)
    jv = np.array([int(jacobi_symbol(n, v)) for n in range(v)], dtype=np.int8) if v > 1 else np.ones(1, dtype=np.int8)
    q = (4 if v % 4 == 1 else 1) * v * p
    half_sum = 0
    for start in range(1, q // 2 + 1, CHUNK):
        n = np.arange(start, min(start + CHUNK, q // 2 + 1), dtype=np.int64)
        chi = lp[n % p] * jv[n % v]
        if v % 4 == 1:
            chi *= np.where(n % 2 == 0, 0, np.where(n % 4 == 1, 1, -1)).astype(np.int8)
        half_sum += int(chi.sum(dtype=np.int64))
    chi2 = 0 if v % 4 == 1 else int(lp[2]) * int(jv[2 % v])
    value = math.pi * half_sum / ((2 - chi2) * math.sqrt(q))
    # Remove the factors at 2u, to obtain the odd Jacobi character chi_u.
    value *= 1 - chi2 / 2
    for ell in factors:
        if v % ell:
            cc = int(lp[ell % p]) * int(jv[ell % v])
            if v % 4 == 1:
                cc *= 1 if ell % 4 == 1 else -1
            value *= 1 - cc / ell
    return value


def check(p):
    assert isprime(p) and p % 4 == 1
    x, y = 9 * p // 10, p // 20
    spf, primes = sieve(x)
    lp = legendre_table(p)
    exact_total = predicted_total = 0.0
    print(f"p={p}; f-window ({y}, {x}]; Euler cutoff={x}")
    for a, c in PAIRS:
        u = a * c
        split = np.zeros(x + 1, dtype=np.int8)
        log_b = 0.0
        for ell_np in primes:
            ell = int(ell_np)
            if (2 * p * u) % ell == 0:
                continue
            residue = pow((-p * u) % ell, (ell - 1) // 2, ell)
            chi = 1 if residue == 1 else -1
            split[ell] = chi
            log_b += math.log1p(chi / (ell * ell))
        value = 0.0
        terms = 0
        for d in range((y + 1) // (4 * u) + 1, (x + 1) // (4 * u) + 1):
            f = 4 * u * d - 1
            assert y < f <= x < p
            rem, phi, omega = f, f, 0
            while rem > 1:
                ell = int(spf[rem])
                if split[ell] != 1:
                    break
                phi = phi // ell * (ell - 1)
                omega += 1
                while rem % ell == 0:
                    rem //= ell
            if rem == 1:
                value += (2 ** omega) / phi
                terms += 1
        lv = exact_L(p, u, lp)
        b = math.exp(log_b)
        predicted = (1 - 1 / p) * lv * b * math.log(x / y) / (4 * u)
        print(f"  (a,c)=({a},{c}) u={u}: L={lv:.10f} B={b:.10f} exact={value:.10f} main={predicted:.10f} ratio={value/predicted:.6f} nonzero={terms}")
        exact_total += value
        predicted_total += predicted
    print(f"  pooled slices: exact={exact_total:.10f} main={predicted_total:.10f} ratio={exact_total/predicted_total:.6f}")
    print(f"  |log(B_exact/B_truncated)| <= {2/x:.3g}; arrays < 200 MB, chunks={CHUNK}")


if __name__ == '__main__':
    print('Exact genus weights versus (1-1/p)L(1,chi_u)B_u log(X/Y)/(4u).')
    print('L: exact odd-character half-period formula; floating rounding only.')
    for prime in PRIMES:
        check(prime)
