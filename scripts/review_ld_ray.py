"""R177 from-scratch checks of LDP_DEEP §A.4 (F = Q(zeta_M)^+, O_F = Z[theta], theta = 2cos(2pi/M)).

(1) Prop A.4.1 (archimedean form): beta = 1 + M*gamma, gamma in Z[theta] random  =>  N(beta) = 1 (mod M) and N(beta) = (-1)^{#neg conj}|N(beta)|,
    hence f = |N(beta)| = (-1)^{#neg} (mod M): f = -1 <=> odd number of negative real conjugates.   (exact norm via resultant)
(2) Prop A.4.2: beta = -1 (mod M O_F) => N(beta) = (-1)^r (mod M), r = phi(M)/2.
(3) r = phi(M)/2 odd  <=>  M in {4, q^k, 2q^k : q = 3 mod 4}   (M <= 5000, M > 2); and M = 4cd > 4 => r even.
(4) residue degrees: for l prime, l not| M, the min poly of theta factors mod l into irreducibles of degree
    g = ord of l in (Z/M)^x/{+-1}; so l^g = +-1 (mod M) is the norm of a prime of F above l (Art_{K/F} = N mod M).
Run: PYTHONPATH=scripts uv run python scripts/review_ld_ray.py
"""
import random
from math import gcd
import mpmath as mp
from sympy import Poly, symbols, resultant, factor_list, primerange, totient, factorint

mp.mp.dps = 80
x = symbols('x')
random.seed(177)


def minpoly(M):
    ks = [k for k in range(1, M // 2 + 1) if gcd(k, M) == 1]
    roots = [2 * mp.cos(2 * mp.pi * k / M) for k in ks]
    coeffs = [mp.mpf(1)]
    for t in roots:  # multiply by (x - t)
        coeffs = [a - t * b for a, b in zip(coeffs + [0], [0] + coeffs)]
    ci = [int(mp.nint(c)) for c in coeffs]
    assert max(abs(c - ci_) for c, ci_ in zip(coeffs, ci)) < mp.mpf(10) ** -40
    return Poly(ci, x), roots


def ordpm(l, M):
    y, g = l % M, 1
    while y not in (1, M - 1):
        y = y * l % M; g += 1
    return g


bad = 0
for M in [8, 12, 16, 20, 24, 28, 36, 40, 44, 48, 52, 56, 60, 72, 84, 120]:
    P, roots = minpoly(M)
    r = len(roots)
    n1 = n2 = 0
    for trial in range(60):
        gam = [random.randint(-3, 3) for _ in range(r)]
        for sgn, cnt in ((1, 'A41'), (-1, 'A42')):
            coeffs = [M * g for g in gam]; coeffs[0] += sgn  # beta = sgn + M*gamma(theta)
            B = Poly(list(reversed(coeffs)), x)
            Nb = int(resultant(P.as_expr(), B.as_expr(), x))  # = prod beta(theta_k) since P monic
            neg = sum(1 for t in roots if sum(c * t ** i for i, c in enumerate(coeffs)) < 0)
            if Nb == 0: continue
            if sgn == 1:
                n1 += 1
                ok = (Nb - 1) % M == 0 and (abs(Nb) - (-1) ** neg) % M == 0  # N(beta) = 1, |N(beta)| = (-1)^neg (mod M)
            else:
                n2 += 1
                ok = (Nb - (-1) ** r) % M == 0
            if not ok and bad < 5: print("FAIL", M, cnt, coeffs, Nb, neg, r)
            bad += not ok
    # residue degrees
    rd_bad = 0
    for l in primerange(3, 400):
        if M % l == 0: continue
        g = ordpm(l, M)
        degs = [Poly(fct, x, modulus=l).degree() for fct, _ in factor_list(P.as_expr(), modulus=l)[1]]
        rd_bad += any(dg != g for dg in degs) or pow(l, g, M) not in (1, M - 1)
    print(f'M={M:4d} r={r:2d}  A.4.1 tests {n1}, A.4.2 tests {n2}, residue-degree mismatches {rd_bad}')
    bad += rd_bad
print('total failures:', bad)


def rodd_pred(M):
    if M == 4: return True
    fac = factorint(M)
    odd = {q: k for q, k in fac.items() if q != 2}
    return len(odd) == 1 and fac.get(2, 0) <= 1 and list(odd)[0] % 4 == 3
mism = [M for M in range(3, 5001) if (totient(M) // 2 % 2 == 1) != rodd_pred(M)]
print('r odd characterisation mismatches M<=5000:', mism)
print('M = 4cd > 4 with r odd:', [4 * m for m in range(2, 1251) if totient(4 * m) // 2 % 2 == 1])
