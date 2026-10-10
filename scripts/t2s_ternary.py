"""O128b: checks for §§7-9 of POINTWISE_TYPEII_SPECTRAL.md (ternary lattice / Pell / divisor-Eisenstein form).

For primes 5 <= p < PMAX:
  (1) Gram data: Q = [f,4ad,de], S_c = [0,2c,1] in the ternary lattice of binary forms with q = B^2-4AC,
      b(x,y) = 2BB' - 4AC' - 4A'C:  q(Q) = -4dp, q(S) = 4c^2, b(Q,S) = 4.
  (2) Pell form: T = 2cd(a+b) - 1, D' = d^2(a-b)^2 + dp:  T^2 - D'(2c)^2 = 1.
  (3) Divisor identity (Prop 8.1): f_II(p) = sum_{c,d} #{f | 4c^2dp+1 : f ≡ -1 (4cd), gcd((f+1)/4cd, c) = 1},
      and F(p) (no gcd condition) = sum over primitive quadruples of #{g : g^2 | d}.
  (4) Square check (Cor 6.2 / Prop 9.2): for odd s <= SMAX, F(s^2) = 0 although every (c,d) is locally fine.
Exit code 1 on any failure.
"""
import math, sys
from sympy import primerange, divisors

PMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 300
SMAX = int(sys.argv[2]) if len(sys.argv) > 2 else 41


def quads(n):
    out = []
    for a in range(1, n + 1):
        for c in range(1, n + 1):
            if 4 * a * c - 1 > a + n * c:
                break
            for d in range(1, n + 1):
                f = 4 * a * c * d - 1
                if f > a + n * c:
                    break
                if (a + n * c) % f == 0:
                    out.append((a, (a + n * c) // f, c, d))
    return out


def divcount(n, need_gcd):
    tot = 0
    # f, f' >= 4cd-1 and c | a+b with a+b <= ... ; bound: c <= a+b <= 2*max(a,b) and 4cd-1 <= sqrt(N)
    for d in range(1, n + 1):
        if 4 * d - 1 > n + 1:  # (4cd-1)^2 <= 4c^2 d n + 1 needs roughly 4d <= n
            break
        c = 1
        while True:
            N = 4 * c * c * d * n + 1
            M = 4 * c * d
            if (M - 1) ** 2 > N:
                break
            k = sum(1 for f in divisors(N) if f % M == M - 1
                    and (not need_gcd or math.gcd((f + 1) // M, c) == 1))
            tot += k
            c += 1
            if c > 4 * n:  # c <= a+b and a+b <= n+... (safety bound)
                break
    return tot


bad = 0
for p in primerange(5, PMAX):
    Qs = quads(p)
    prim = [q for q in Qs if math.gcd(q[0], q[2]) == 1]
    for (a, b, c, d) in prim:
        f, e = 4 * a * c * d - 1, (a + b) // c
        A, B, C = f, 4 * a * d, d * e
        qQ = B * B - 4 * A * C
        S = (0, 2 * c, 1)
        qS = S[1] ** 2 - 4 * S[0] * S[2]
        bQS = 2 * B * S[1] - 4 * A * S[2] - 4 * S[0] * C
        T, Dp = 2 * c * d * (a + b) - 1, d * d * (a - b) ** 2 + d * p
        if (qQ, qS, bQS) != (-4 * d * p, 4 * c * c, 4) or T * T - Dp * 4 * c * c != 1:
            bad += 1; print("GRAM/PELL FAIL", p, (a, b, c, d))
    fII = len(prim)
    F_expected = sum(sum(1 for g in range(1, d + 1) if d % (g * g) == 0) for (a, b, c, d) in prim)
    if divcount(p, True) != fII or divcount(p, False) != F_expected or len(Qs) != F_expected:
        bad += 1; print("DIVISOR IDENTITY FAIL", p, fII, divcount(p, True), F_expected, divcount(p, False), len(Qs))
print(f"primes < {PMAX}: Gram, Pell and divisor identities checked; failures so far = {bad}")
for s in range(3, SMAX + 1, 2):
    if divcount(s * s, False) != 0:
        bad += 1; print("SQUARE FAIL", s)
print(f"odd squares s^2, s <= {SMAX}: F(s^2) = 0 checked; total failures = {bad}")
sys.exit(1 if bad else 0)
