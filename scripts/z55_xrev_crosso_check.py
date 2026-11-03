"""Independent CROSSO audit: directed prime tail, Haar normalisation, four-cycle.

Run: ulimit -v 6000000; ulimit -t 120; timeout 120s uv run python scripts/z55_xrev_crosso_check.py
No dependencies. The largest allocation is a 2,000,001-byte sieve; pair sums
use a seven-member toy family, never the large Monte Carlo families.
"""
from collections import defaultdict
from decimal import Decimal, ROUND_CEILING, localcontext
from fractions import Fraction as F
from math import gcd, isqrt, lcm, log, pi, prod


def factors(n):
    result = []
    for d in range(2, isqrt(n) + 1):
        if n % d == 0:
            result.append(d)
            while n % d == 0:
                n //= d
    if n > 1:
        result.append(n)
    return result


def phi(n):
    return prod(p - 1 for p in factors(n))  # used only for squarefree n


def squarefree(n):
    return all(n % (d * d) for d in range(2, isqrt(n) + 1))


def constants():
    limit = 2_000_000
    prime = bytearray(b"\x01") * (limit + 1)
    prime[:2] = b"\x00\x00"
    for p in range(2, isqrt(limit) + 1):
        if prime[p]:
            prime[p * p::p] = b"\x00" * ((limit - p * p) // p + 1)
    with localcontext() as ctx:
        ctx.prec = 40
        ctx.rounding = ROUND_CEILING
        upper = sum((Decimal(1) / (p * p) for p in range(17, limit + 1)
                     if prime[p]), Decimal(0)) + Decimal(1) / limit
        assert upper < Decimal("0.016546991")
        print("prime reciprocal-square tail upper:", upper)
    kappa = prod(p / (p + 1) for p in (3, 5, 7, 11, 13)) / pi**2
    leading = 2 * (kappa - (5 / 3) * float(upper)) * (2 / pi**2 - 0.15)
    assert leading > 0.002
    print(f"density: kappa={kappa:.12f}, leading coefficient>{leading:.12f}")
    mu = log(0.1 / 0.075) * log(0.39 / 0.29) / 4
    proportion = 2 * mu * (1 - 2 * 0.49) / (2 * (1 - 2 * 0.49) + 32 * mu)
    print(f"Theorem P: mu={mu:.12f}, proportion={proportion:.12f}")
    for a0, a1, beta, gamma, r, eps in (
        (0.075, 0.1, 0.29, 0.39, 100, 2e-5),
        (0.07, 0.08, 0.28, 0.41, 1000, 1e-6),
    ):
        tau = (r + 1) / (4 * r) + r * eps
        c2, c3 = tau * (1 + a1) + 4 * eps, tau**2 * (1 + a1) + 3 * eps
        assert gamma < 1 - a1 and beta > c2 and a0 > c3 and a1 + gamma < 0.5
        print(f"window r={r}: C2 RHS={c2:.12f}, C3 RHS={c3:.12f}")


def haar():
    # Full family in the toy window (0,5,5,15); includes cross-sharing at 5.
    family = [(u, w, u * w, -(u + 2 * w))
              for u in range(1, 6, 4) for w in range(7, 16, 2)
              if squarefree(u) and squarefree(w) and gcd(u, w) == 1]
    modulus = lcm(*(8 * b for _, _, b, _ in family))
    assert len(family) == 7 and modulus <= 200_000
    print(f"Haar census: {len(family)} members, modulus={modulus}")
    for z in (3, 5, 7, 11, 17):
        smooth = prod(p for p in factors(modulus) if 2 < p < z)
        local_modulus = 8 * smooth
        groups = defaultdict(lambda: [0, 0, 0])
        for n in range(1, modulus, 4):
            if gcd(n, modulus) != 1:
                continue
            count = 2 * sum((n - a) % (8 * b) == 0 for _, _, b, a in family)
            group = groups[n % local_modulus]
            group[0] += 1
            group[1] += count
            group[2] += count * count
        sample_sizes = {c: sum(g[0] for s, g in groups.items() if s % 8 == c)
                        for c in (1, 5)}
        energy = F(0)
        for s, (number, total, total2) in groups.items():
            main = sum((F(2 * phi(gcd(b, smooth)), phi(b))
                        for _, _, b, a in family
                        if (s - a) % (8 * gcd(b, smooth)) == 0), F(0))
            assert main == F(total, number), (z, s, main, total, number)
            energy += (total2 - F(total * total, number)) / (4 * sample_sizes[s % 8])
        pair_energy, upper = F(0), F(0)
        for _, _, b, a in family:
            for _, _, bp, ap in family:
                if (a - ap) % 8:
                    continue
                h = gcd(b, bp)
                hs = gcd(h, smooth)
                positive = phi(h) if (a - ap) % h == 0 else 0
                negative = phi(hs) if (a - ap) % hs == 0 else 0
                denominator = phi(b) * phi(bp)
                pair_energy += F(positive - negative, denominator)
                if h != hs:
                    upper += F(positive, denominator)
        assert energy == pair_energy and 0 <= energy <= upper
        print(f"z={z}: direct Haar residual energy={energy}, pair energy={pair_energy}, W_z={upper}")


def cycle():
    u, w, up, wp = 33, 455, 145, 399
    assert all(squarefree(n) for n in (u, w, up, wp))
    assert u % 4 == up % 4 == 1 and min(w, wp) > max(u, up)
    assert gcd(u, w) == gcd(up, wp) == 1
    a, ap = -(u + 2 * w), -(up + 2 * wp)
    assert (a - ap) % gcd(8 * u * w, 8 * up * wp) == 0
    g11, g12, g21, g22 = gcd(u, up), gcd(u, wp), gcd(w, up), gcd(w, wp)
    k1, v = u // (g11 * g12), up // (g11 * g21)
    k2, t = w // (g21 * g22), wp // (g12 * g22)
    wrong = g12 * pow(g21, -1, g22) % g22
    correct = g21 * pow(g12, -1, g22) % g22
    assert (k1 - wrong * v) % g22 != 0
    assert (k1 - correct * v) % g22 == 0
    assert (g11 * k1 - 2 * g22 * t) % g21 == 0
    assert (g21 * k2 - g12 * t) % g11 == 0
    assert (2 * g22 * k2 - g11 * v) % g12 == 0
    print(f"cycle counterexample: (u,w)=({u},{w}), (u',w')=({up},{wp}), a=a'={a}")
    print(f"g=({g11},{g12},{g21},{g22}), k1={k1}, v={v}, k2={k2}, t={t}")
    print(f"mod {g22}: k1={k1 % g22}; printed lambda1*v={wrong * v % g22}; corrected={correct * v % g22}")


if __name__ == "__main__":
    constants()
    haar()
    cycle()
