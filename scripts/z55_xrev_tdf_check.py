"""Independent bounded TDF review checks: CRT mean square and square-event scope.

Run: ulimit -v 6000000; timeout 120s uv run python scripts/z55_xrev_tdf_check.py
No dependencies. Covariance pairs are streamed, never materialized (O(U^3)
resident support, at most 2805 entries here). These checks complement the
memo's FFT/Farey calculation rather than reimplementing its transform.
"""
import cmath
import math


def support(U, h):
    return [
        (m, s, cmath.exp(2j * math.pi * h * math.sqrt(s * s - 4 * m)))
        for m in range(U * U + 1, 4 * U * U + 1)
        for s in range(2 * U + 1, 4 * U + 1)
        if s * s > 4 * m
    ]


def crt_mass(terms):
    # The events n=-s (mod m), n=-t (mod q) coexist iff gcd(m,q)|s-t;
    # their density is 1/lcm(m,q). Pair conjugates before summation.
    def contributions():
        for i, (m, s, z) in enumerate(terms):
            yield abs(z) ** 2 / m
            for j in range(i):
                q, t, w = terms[j]
                g = math.gcd(m, q)
                if (s - t) % g == 0:
                    yield 2 * (z * w.conjugate()).real * g / (m * q)
    return math.fsum(contributions())


def small_denominator_mass(U, terms):
    total = 0.0
    for d in range(1, 2 * U + 1):
        residues = [0j] * d
        for m, s, z in terms:
            if m % d == 0:
                residues[s % d] += z / m
        for b in range(d):
            if math.gcd(b, d) == 1:
                gamma = sum(z * cmath.exp(2j * math.pi * r * b / d)
                            for r, z in enumerate(residues))
                total += abs(gamma) ** 2
    return total


for U, h in ((6, 1), (10, 1), (10, 3)):
    terms = support(U, h)
    mass = crt_mass(terms)
    assert 0 <= mass <= 2700 * h**4 * U + 32 * U * math.log(2 * U)
    small = small_denominator_mass(U, terms)
    assert 0 <= small <= mass
    print(f"CRT U={U} h={h} support={len(terms)} G={mass:.10f}; d<=2U share={small / mass:.3%}")


def prime(n):
    return n >= 2 and all(n % d for d in range(2, math.isqrt(n) + 1))


# Find an admissible prime with square D but roots outside the balanced block.
U, s, m = 10, 31, 210  # roots 10,21; both violate (10,20].
p = next(p for p in range(16 * U**3, 3 * U**4) if (p + s) % m == 0 and prime(p))
k = (p + s) // m
D = s * s - 4 * m
assert k > 4 * U and U * U < m <= 4 * U * U and 2 * U < s <= 4 * U
assert math.isqrt(D) ** 2 == D
assert ((s - math.isqrt(D)) // 2, (s + math.isqrt(D)) // 2) == (10, 21)
print(f"Square-event counterexample: U={U} p={p} k={k} m={m} s={s} D={D}, roots=10,21")

# Zero Fourier modes cannot be bounded by bounds on the nonzero modes alone:
# repeat the (H+1) equally spaced phases R times. This is a general Fourier
# obstruction to the cited implication, NOT an arithmetic counterexample to TD.
H, R = 10, 100
sums = [R * sum(cmath.exp(2j * math.pi * h * j / (H + 1)) for j in range(H + 1))
        for h in range(1, H + 1)]
assert max(map(abs, sums)) < 1e-8
print(f"Zero-mode example: mass={(H + 1) * R}; max nonzero mode={max(map(abs, sums)):.2e}")
